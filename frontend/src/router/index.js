import { createRouter, createWebHistory } from 'vue-router';
import UserLogin from '../components/UserLogin.vue';
import UserSignup from '../components/UserSignup.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
      // { path: '/', redirect: '/coaches' },
      { path: '/register', component: UserSignup },
      { path: '/login', component: UserLogin },
    ]
  });

export default router
