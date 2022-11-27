<template>
    <a-layout-header class="header">
            <div class="logo" />
            <a-menu  theme="dark" mode="horizontal" :style="{ lineHeight: '64px' }">
                <a-menu-item key="1"><router-link to="/"
						class="font-bold text-dark">Home</router-link></a-menu-item>
                <a-menu-item key="2"><router-link to="/login"
						class="font-bold text-dark">Login</router-link></a-menu-item>
                <a-menu-item key="3"><router-link to="/register"
						class="font-bold text-dark">Sign Up</router-link></a-menu-item>
            </a-menu>
        </a-layout-header>
</template>