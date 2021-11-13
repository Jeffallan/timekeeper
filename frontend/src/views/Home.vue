<template >
<div>
  <div v-show="mustLogin">
    <Login />
  </div>
  <div class="text-center" v-show="!mustLogin">
    <h1>Welcome</h1>
  </div>
  </div>
</template>

<script>

// https://dev.to/briancaffey/how-to-authenticate-django-rest-framework-api-calls-from-a-vue-js-client-using-session-authentication-and-httponly-cookies-817
// https://yoongkang.com/blog/cookie-based-authentication-spa-django/
import Login from "@/components/forms/Login"

export default {
  name: 'Home',
  components: {
    Login,
  },
  computed: {
    mustLogin() {
      console.log(this.$store.state.users.status )
      return this.$store.state.users.status != "success"
    },
  },
}
</script>
