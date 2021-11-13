<template>

    <b-card class="mx-3 text-center" title="Edit Profile">

    <b-form  @submit.stop.prevent="onSubmit" @reset="onReset" novalidate >
      <b-form-group label="First Name"
                    label-cols="4"
                    content-cols>
         <b-form-input
        id="first_name"
        v-model="$v.form.first_name.$model"
        type="text"
        placeholder="first name"
        :state="validationState('first_name')"
        required >
        </b-form-input>
         <b-form-invalid-feedback>This field is required.</b-form-invalid-feedback>
      </b-form-group >
    <b-form-group label="Last Name"
                  label-cols="4"
                  content-cols>
      <b-form-input
        id="last_name"
        v-model="$v.form.last_name.$model"
        type="text"
        placeholder="last name"
        :state="validationState('last_name')"
        required >
      </b-form-input>
        <b-form-invalid-feedback>This field is required.</b-form-invalid-feedback>
      </b-form-group> 
      <b-form-group label="Phone"
                    label-cols="4"
                    content-cols>
      <b-form-input
        id="phone"
        v-model="$v.form.phone_number.$model"
        type="tel"
        placeholder="phone number"
        :state="validationState('phone_number')"
        required >
      </b-form-input>
        <b-form-invalid-feedback>This field is required.</b-form-invalid-feedback>
      </b-form-group>
    <b-form-group label="Address 1"
                    label-cols="4"
                    content-cols>
      <b-form-input
        id="address_1"
        v-model="$v.form.address_1.$model"
        type="text"
        placeholder="Address 1"
        :state="validationState('address_1')"
        required >
      </b-form-input>
        <b-form-invalid-feedback>This field is required.</b-form-invalid-feedback>
    </b-form-group>
      <b-form-group label="Address 2"
                    label-cols="4"
                    content-colslabel-cols="4"
                    content-cols>
      <b-form-input
        id="address_2"
        v-model="$v.form.address_2.$model"
        type="text"
        placeholder="Address 2"
        :state="validationState('address_2')"
        >
      </b-form-input>
    </b-form-group>
    <b-form-group label="City"
                  label-cols="4"
                  content-cols>
      <b-form-input
        id="city"
        v-model="$v.form.city.$model"
        type="text"
        placeholder="City"
        :state="validationState('city')"
        required >
      </b-form-input>
        <b-form-invalid-feedback>This field is required.</b-form-invalid-feedback>
    </b-form-group>
    <b-form-group label="State"
                  label-cols="4"
                  content-cols>
    <b-form-input
        id="state"
        v-model="$v.form.state.$model"
        type="text"
        placeholder="State"
        :state="validationState('state')"
        required >
      </b-form-input>
        <b-form-invalid-feedback>This field is required.</b-form-invalid-feedback>
      </b-form-group>
      <b-form-group label="Zip"
                    label-cols="4"
                    content-cols>
      <b-form-input
        id="zip"
        v-model="$v.form.zip_code.$model"
        type="text"
        placeholder="Zip code"
        :state="validationState('zip_code')"
        required >
      </b-form-input>
        <b-form-invalid-feedback>This field is required.</b-form-invalid-feedback>
      </b-form-group>
      
      <b-button variant="outline-primary" 
                class="float-right"
                @click="onSubmit">submit</b-button>
      <b-button variant="outline-primary" 
                class=""
                @click="onCancel">cancel</b-button>
      
      
    </b-form>
    <br />
    <b-card-footer class="bg-white">
      <b-button
      variant="link">
        reset email
      </b-button>
    </b-card-footer>
</b-card>
  

</template>

<script>
import { validationMixin } from "vuelidate"
import { required, numeric, alpha, alphaNum } from "vuelidate/lib/validators"
import { PROFILE } from '@/util/constants/Urls.js'
import Router from "@/router/index"

  export default {
    name: "ProfileForm",
    mixins: [validationMixin,],

    data() {
      return {
        form: {
          //email: this.$props.email,
          phone_number: this.$props.phone_number,
          first_name: this.$props.first_name,
          last_name: this.$props.last_name,
          address_1: this.$props.address_1,
          address_2: this.$props.address_2,
          city: this.$props.city,
          state: this.$props.state,
          zip_code: this.$props.zip_code,
          id: this.$props.id,
        },

      }
    },
    props: {
      id: {
        type: Number,
        default: 0,
      },

      phone_number: {
        type: String,
        default: "",
      },
      first_name: {
        type: String,
        default: "",
      },
      last_name: {
        type: String,
        default: ""
      },
      address_1: {
        type: String,
        default: "",
      },
      address_2: {
        type: String,
        default: ""
      },
      city: {
        type: String,
        default: "",
      },
      state: {
        type: String,
        default: ""
      },
      zip_code: {
        type: Number,
        default: null
      },
    },
    computed: {
      showError() {
        return this.$store.state.users.status == "error"
      },
      //curr_email(){ return this.$store.state.users.user.email },

    },
    validations: {
      form: {
      //  email: {
      //    required,
      //    email,
      //  },
        first_name: {
          required,
          alpha,
        },
        last_name: {
          required,
          alpha,
        },
        phone_number: {
          required,
          //alphaNum,
        },
        address_1: {
          required,
          alphaNum
        },
        address_2: {

        },
        city: {
          required,
          alpha
        },
        state: {
          required,
          alpha
        },
        zip_code: {
          required,
          numeric,
        },
      },
    },
    methods: {
      onSubmit() {

        if (this.$v.form.$anyError){
          this.onReset()
          return
        }
        const {id, ...data} = this.$data.form
        this.$http({url: `${PROFILE}${id}/`, data: data, method: "PUT"}).then( () => {
          Router.push({name: "Profile"})
        }).catch( e => {
          console.log(e)
        })
      },
    validationState(name) {
      const { $dirty, $error } = this.$v.form[name]
      return $dirty ? !$error : null
    },

      onReset() {
        //this.form = {
        //
        //}
        //this.$nextTick(() => {
        //  this.$v.$reset()
        //})
      },
      onCancel() {
        Router.push({name: "Profile"})
      }
    },
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