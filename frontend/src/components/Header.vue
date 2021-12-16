<template>

<b-navbar toggleable="lg" type="dark" variant="info" >
    <b-navbar-brand href="#">
        {{title}}
    </b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav v-if="role">
        <b-navbar-nav class="ml-auto">
          <b-nav-item v-for="u in urls" :key="u.name" class="text-center">
              <router-link :to="u.path">
                {{u.name}}
              </router-link>
          </b-nav-item>
          <span class="text-center" v-if="role==1" text="More" type="dark" variant="info">
            <b-dropdown-item v-for="a in admin" :key="a.name" class="text-center">
              <router-link :to="a.path">
                {{a.name}}
              </router-link>
          </b-dropdown-item>
          </span>
           <b-nav-item class="text-center">
            <router-link :to="{name:'Profile', params:{id: this.uid }  }">
              Profile
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
            title: "Nav",
            urls: [
                { name: 'Home', path: '/', },
                { name: "Directory", path: "/users"},
                { name: "Work", path: "/work"}
           ],
            admin: [
              { name: "Services", path: "/services"},
              { name: "Clients", path: "/clients" },
              { name: "Locations", path: "/locations" }
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
          },
        uid() {
          return this.$store.state.users.user.id
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