<template>
	<div>
		<!-- Sign Up Image And Headings -->
		<div class="sign-up-header" style="background-image: url('./images/bg-signup.jpg')">
			<div class="content">
				<h1 class="mb-5">Sign Up</h1>
				<p class="text-lg">Recommender system for energy saving from Household appliances</p>
			</div>
		</div>
		<!-- / Sign Up Image And Headings -->

		<!-- Sign Up Form -->
		<a-card :bordered="false" class="card-signup header-solid h-full" :bodyStyle="{ paddingTop: 0 }">
			<a-form id="components-form-demo-normal-login" :form="form" class="login-form" @submit="handleSubmit">
				<a-form-item class="mb-10" style="margin-top: 6px">
					<a-input v-decorator="[
						'name',
						{ rules: [{ required: true, message: 'Please input your name!' }] },
					]" placeholder="Name">
					</a-input>
				</a-form-item>
				<a-form-item class="mb-10">
					<a-input v-decorator="[
						'email',
						{ rules: [{ required: true, message: 'Please input your email!' }] },
					]" placeholder="Email">
					</a-input>
				</a-form-item>
				<a-form-item class="mb-5">
					<a-input v-decorator="[
						'password',
						{ rules: [{ required: true, message: 'Please input your Password!' }] },
					]" type="password" placeholder="Password">
					</a-input>
				</a-form-item>
				<a-form-item class="mb-10">
					<a-checkbox v-decorator="[
						'remember',
						{
							valuePropName: 'checked',
							initialValue: true,
						},
					]">
						I agree the <a href="#" class="font-bold text-dark">Terms and Conditions</a>
					</a-checkbox>
				</a-form-item>
				<a-form-item>
					<a-button type="primary" block html-type="submit" class="login-form-button">
						SIGN UP
					</a-button>
				</a-form-item>
			</a-form>
			<p class="font-semibold text-muted text-center">Already have an account? <router-link to="/login"
					class="font-bold text-dark">Sign In</router-link>
			</p>
		</a-card>
		<!-- / Sign Up Form -->

	</div>
</template>

<script>

export default ({
	data() {
		return {
		}
	},
})

</script>

<style lang="scss">

</style>