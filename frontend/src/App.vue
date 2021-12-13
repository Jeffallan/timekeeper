<template>
  <div id="app" class="vh-100">

    <b-container class="appWrapper " fluid >
      <Header />
        <b-container class="routerWrapper" fluid >
            <router-view />
        </b-container>
      <Footer />
    </b-container>
     
  </div>
</template>

<script>

import Header from "@/components/Header.vue"
import Footer from "@/components/Footer.vue"

export default {
    name: "App", 
    components: {
        Header, 
        Footer,
    },
    computed: {
      user ()  {
        if (Object.keys(this.$store.state.users.user) == 0){
          this.$store.dispatch("users/getUserDetails")
        } 
        return this.$store.state.users.user
      },
      token () {
        return this.$store.state.users.token
      },
      status () {
        return this.$store.state.users.status
      }
  },
}
</script>

<style>

html, body {
  /*  min-height: 100vh; */
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
 /* min-height: 100% */
  
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
.appWrapper {

  padding-left: 0;
  padding-right: 0;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 100vh;
}
.routerWrapper {
  padding-top: 15px;
  padding-bottom: 15px;
  max-width: 800px
}

</style>
