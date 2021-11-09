<template v-if="">
  <div >
    <Login />
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

  }
}
</script>
