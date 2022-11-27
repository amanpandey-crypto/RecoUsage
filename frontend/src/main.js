import { createApp } from 'vue';
import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/antd.css';
import App from './App.vue'
import router from './router'
import CardInfo from './components/CardInfo.vue'
// import CalenderView from './components/CalenderView.vue'

import './scss/app.scss';
const app = createApp(App)

app.use(router);
app.use(Antd);
app.component('CardInfo', CardInfo)
// app.component('CalenderView', CalenderView)


app.config.productionTip = false

app.mount('#app');