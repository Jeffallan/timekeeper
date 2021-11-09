<template>
  <div >

    <section>
        <b-message 
            title="Error"
            type="is-danger"
            has-icon
            v-model="showError" 
            aria-close-label="Close message">
           Incorect Username or Password
        </b-message>
    </section>
     <div >

    <form  >
      <b-field>
        <b-input
          id="input-1"
          v-model="$v.form.email.$model"
          type="email"
          placeholder="Enter email"
          :state="validationState('email')"
          required
        />
      </b-field>
      <b-field>
        <b-input
          id="input-2"
          type="password"
          v-model="$v.form.password.$model"
          placeholder="Enter Password"
          :state="validationState('password')"
          required
        ></b-input>
      </b-field>

      <hr />
      <b-form-group class="text-right">
        <b-button type="submit" variant="primary" class="pull-right">Login</b-button>
      </b-form-group>
      <hr />

        <b-button variant="link" @click="onForgot">Forgot Password</b-button>

    </form>
    </div>
  </div>
</template>

<script>
import Router from "@/router/index"
//import axios from "axios"
//import { LOGIN } from "@/util/constants/Urls"
import { validationMixin } from "vuelidate"
import { required, email } from "vuelidate/lib/validators"


  export default {
    name: "Login",
    mixins: [validationMixin,],
    props: {

    },
    data() {
      return {
        form: {
          email: null,
          password: null,
        },
        showError: false
      }
    },
    validations: {
      form: {
        email: {
          required,
          email,
        },
        password: {
          required,
        },
      },
    },
    methods: {
      validationState(name) {
      const { $dirty, $error } = this.$v.form[name]
      return $dirty ? !$error : null
    },
      onSubmit() {
        this.$v.form.$touch()
        if (this.$v.form.$anyError){
          this.onReset()
          return
        }
        let user = {
          email: this.form.email,
          password: this.form.password
        }
        this.$store.dispatch("users/login", user)
        this.$store.dispatch("users/getUserDetails")
      },
      onReset() {
        this.form = {
          email: null,
          password: null,
        }
        this.$nextTick(() => {
          this.$v.$reset()
        })
      },
      onForgot() {
        Router.push("/password-reset")
      }
    }
    
  }
</script>

<style scoped>
    .card {
        padding-right: 0;
        padding-left: 0; 
    }
    .card-header {
        text-align: center;
        font-size: 2em;
    }
</style>

/*
<b-alert :show="showError" 
              dismissible 
              variant="danger"
              @dismissed="showError=false"
              >Incorrect username or password
    </b-alert>
 
 
  <div header="Login">

    <form @submit.stop.prevent="onSubmit" @reset="onReset" novalidate >
      <b-form-group
        id="input-group-1"
        type="email"
        label="Email address:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="$v.form.email.$model"
          type="email"
          placeholder="Enter email"
          :state="validationState('email')"
          required
        ></b-form-input>
        <b-form-invalid-feedback>This required field must be an email address</b-form-invalid-feedback>
      </b-form-group>
      <b-form-group id="input-group-2" label="Password:" label-for="input-2">
        <b-form-input
          id="input-2"
          type="password"
          v-model="$v.form.password.$model"
          placeholder="Enter Password"
          :state="validationState('password')"
          required
        ></b-form-input>
        <b-form-invalid-feedback>This field is required</b-form-invalid-feedback>
      </b-form-group >
      <hr />
      <b-form-group class="text-right">
        <b-button type="submit" variant="primary" class="pull-right">Login</b-button>

      <hr />

        <b-button variant="link" @click="onForgot">Forgot Password</b-button>

    </form>
    </div>
 
 */