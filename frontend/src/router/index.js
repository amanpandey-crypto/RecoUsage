import { createRouter, createWebHistory } from 'vue-router';

import LoginUser from '../views/LoginUser.vue';
import SignupUser from '../views/SignupUser.vue';


const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/' },
    { path: '/login', component: LoginUser },
    { path: '/register', component: SignupUser },
  ]
});

export default router;