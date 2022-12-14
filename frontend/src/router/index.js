import { createRouter, createWebHistory } from 'vue-router';

import LoginUser from '../views/LoginUser.vue';
import SignupUser from '../views/SignupUser.vue';
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: HomeView },
    { path: '/login', component: LoginUser },
    { path: '/register', component: SignupUser },
  ]
});

export default router;