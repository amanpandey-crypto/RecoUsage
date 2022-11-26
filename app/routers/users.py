from fastapi import APIRouter, Body
from database.model import User
from database.setup import user_collection, session_info
from auth.controller import get_password_hash, create_access_token, verify_password, validate_token
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import  HTTPException, Depends, status

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")

@router.post("/user/login", tags=["login"], status_code=200)
async def login(request: OAuth2PasswordRequestForm = Depends()):
    username = request.username
    password = request.password
    user = user_collection.find_one({"username": username})
    if not user:
        isLogin= False
        user_collection.update_one({"username": username}, { "$set": {"isLogin": isLogin}})
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User Not found with this {username} username')
    if not verify_password(password, user["password"]):
        isLogin= False
        user_collection.update_one({"username": username}, { "$set": {"isLogin": isLogin}})
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f'Wrong Username or password')
    else:
        isLogin= True
        access_token = create_access_token(data={"sub": user["username"] })
        isTokenValid = True
        user_collection.update_one({"username": username}, { "$set": {"isLogin": isLogin}})
        session_dict= {"username": username, "access_token": access_token, "isTokenvalid": isTokenValid}
        session_info.insert_one(session_dict)
        
    return {"access_token": access_token, "token_type": "bearer"}
	
	
@router.post("/user/register/", tags=["register"], status_code=201)
async def create_user(user: User = Body(default=None)):
    password = user.password
    hashed_pass = get_password_hash(password)
    user_dict = {
            "username": user.username,
            "name": user.full_name,
            "email": user.email,
            "password": hashed_pass,
            "state": user.state,
            "isLogin": user.isLogin
        }
    user_validate= user_collection.find_one({"username": user.username})
    if not user_validate:
        user_collection.insert_one(user_dict)
        raise HTTPException(status_code=status.HTTP_201_CREATED, 
                            detail = f'User Created')
    else:
        raise HTTPException(status_code=status.HTTP_302_FOUND, 
                            detail = f'Username already exist with this {user.username}, Try another one!')

async def get_decoded_token(token: str = Depends(oauth2_scheme)):
    print(token)
    decoded_token = validate_token(token)
    print(decoded_token)
    return decoded_token


@router.get("/users/me", tags=["users"], status_code=302)
async def read_user_me(token: str = Depends(get_decoded_token)):
    username= token['sub']
    return {"username": username}

@router.get("/user/logout", tags=["logout"], status_code=200)
async def logout(token: str = Depends(get_decoded_token)):
    username=token["sub"]
    print(username)
    isLogin= False
    user_collection.update_one({"username": username}, {"$set": {"isLogin": isLogin}})
    session_info.delete_one({"username": username})
    return {"response": "Logged out"}