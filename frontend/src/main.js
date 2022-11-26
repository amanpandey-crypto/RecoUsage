import { createApp } from 'vue';
import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/antd.css';
import App from './App.vue'
import router from './router'

import './scss/app.scss';
const app = createApp(App)

app.use(router);
app.use(Antd);

app.config.productionTip = false

app.mount('#app');