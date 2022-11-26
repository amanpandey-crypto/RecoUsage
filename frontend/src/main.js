import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index.js'
// import UserLogin from '../components/UserLogin.vue';
// import UserSignup from '../components/UserSignup.vue'

import 'bootstrap/dist/css/bootstrap.min.css'
import '@/assets/css/main.css'

const app = createApp(App)
app.use(router);
app.mount('#app')
