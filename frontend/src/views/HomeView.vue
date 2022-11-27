<template>
    <a-layout class="layout">
        
        <a-layout-content style="padding: 0 50px">
            <!-- <a-breadcrumb style="margin: 16px 0">
                <a-breadcrumb-item>Home</a-breadcrumb-item>
                <a-breadcrumb-item>List</a-breadcrumb-item>
                <a-breadcrumb-item>App</a-breadcrumb-item>
            </a-breadcrumb> -->
            <div :style="{ background: '#fff', padding: '24px', minHeight: '280px' }">
                <card-info/>
                <card-info/>
            </div>
        </a-layout-content>
        <a-layout-footer style="text-align: center">
        </a-layout-footer>
    </a-layout>
</template>
<script>
import { defineComponent} from 'vue';
export default defineComponent({
    setup() {
        return {
           
        };
    },
});
</script>
<style>
.site-layout-content {
    min-height: 280px;
    padding: 24px;
    background: #fff;
}

#components-layout-demo-top .logo {
    float: left;
    width: 120px;
    height: 31px;
    margin: 16px 24px 16px 0;
    background: rgba(255, 255, 255, 0.3);
}

.ant-row-rtl #components-layout-demo-top .logo {
    float: right;
    margin: 16px 0 16px 24px;
}

[data-theme='dark'] .site-layout-content {
    background: #141414;
}
</style>
  