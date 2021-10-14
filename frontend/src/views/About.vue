<template>
  <div class="text-center">
    <h1>This is an about page</h1>
    <!--
      <LorIp />
    -->
    <p>User Details</p>
    <p>Token: {{ token }} </p>
    <p>Status: {{ status }}</p>
    <p>Email: {{ user.email }}</p>
    <p>Role: {{ user.role }}</p>
  </div>
</template>

<script>
//import LorIp from "@/components/LorIp"
//import getters from "@/store/modules/users"


export default {
  name: "About",

  components: {
    //LorIp,
  },
  // data: () => {
  //   return {
  //     user: USER,
  //   }
  // },
  computed: {
    user ()  {
      //if (Object.keys(this.$store.state.users.user) == 0){
      //  this.$store.dispatch("users/getUserDetails")
      //} 
      return this.$store.state.users.user
      
    },
    token () {
      return this.$store.state.users.token
    },
    status () {
      return this.$store.state.users.status
    }
  } 
  
}
</script>
