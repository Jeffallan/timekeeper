<template>

<b-navbar toggleable="lg" type="dark" variant="info" >
    <b-navbar-brand href="#">
        {{title}}
    </b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-item v-for="u in urls" :key="u.name" class="text-center">
              <router-link :to="u.path">
                {{u.name}}
              </router-link>
          </b-nav-item>

          <b-nav-item class=text-center
            v-if="role">
              <router-link :to="urls[0].path"
              @click.native="logout"
              >Log Out</router-link>
          </b-nav-item>

        </b-navbar-nav>
    </b-collapse>
</b-navbar>


</template>

<script>


export default {
        name: "Header",
        props: {

        },
        data: () => {
          return {
            title: "NavBar",
            urls: [
                { name: 'Home', path: '/', },
                { name: 'About', path: '/about', },
                { name: 'Viewer', path: '/viewer' },
                { name: "Directory", path: "/users"},
                { name: 'Profile', path: '/profile' },
           ],

          }
        },
        methods: {
          logout () {
            this.$store.dispatch("users/logout")
          }
        },
        computed: {
          role() {
            return this.$store.state.users.user.role
          }
        },
    }

</script>

<style scoped>
    /*
    active classes for vue-router
    nav li:hover,
    nav li.router-link-active,
    nav li.router-link-exact-active {
        background-color: lightgrey; 
    }
    */
    nav {
        /*
        margin-bottom: 10em;
        */
    }
    a {
        color: white;
    }
</style>