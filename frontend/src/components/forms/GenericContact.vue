<template>
    <!--
    <b-card class="mx-3 text-center" :title="getEdit">

    <b-form  @submit.stop.prevent="onSubmit" @reset="onReset" novalidate >
    -->
    <span>
    <b-form-group label="Name"
                  label-cols="4"
                  content-cols>
      <b-form-input
        id="name"
        v-model="$v.form.name.$model"
        type="text"
        placeholder="name"
        :state="validationState('name')"
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
      </span>
        <!--
        <slot />
    </b-form>
    
</b-card>
-->

</template>

<script>
import { validationMixin } from "vuelidate"
import { required, numeric, alpha, minLength, maxLength} from "vuelidate/lib/validators"
import Router from "@/router/index"

  export default {
    name: "ProfileForm",
    mixins: [validationMixin,],

    data() {
      return {
        form: {
          phone_number: this.$props.phone_number,
          name: this.$props.name,
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
      },

      phone_number: {
        type: String,
        default: "",
      },
      name: {
        type: String,
        default: "",
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
      type: {
          type: String,
           validator: function (value) {
            return ['location', 'client'].indexOf(value) !== -1
          },
      }
    },
    computed: {
    //  showError() {
    //  },
    //  //curr_email(){ return this.$store.state.users.user.email },
    //
        getEdit() {
            return `Edit ${this.$props.type}`
        }
    },
    validations: {
      form: {

        name: {
          required,
        },
        phone_number: {
          required,
          minLength: minLength(10),
          maxLength: maxLength(10)
        },
        address_1: {
          required,
          //alphaNum
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
    mounted() {
      console.log(this.props)
    },
    methods: {
      onSubmit() {
        this.$v.form.$touch()
        if (this.$v.form.$anyError){
          this.onReset()
          return
        }
        const {id, ...data} = this.$data.form
        this.$http({url: `${id}/`, data: data, method: "PUT"}).then( () => {
          Router.push({name: "Directory"})
        }).catch( e => {
          console.log(e)
        })
      },
    validationState(name) {
      const { $dirty, $error } = this.$v.form[name]
      return $dirty ? !$error : null
    },

      onReset() {

      },
      onCancel() {
        Router.push({name: "Profile", params: {...this.$props}})
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