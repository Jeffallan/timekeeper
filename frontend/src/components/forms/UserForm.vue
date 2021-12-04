<template>
    <b-card class="mx-3 text-center" title="Create User">
        <b-form @submit.stop.prevent="onSubmit" @reset="onReset" novalidate>
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
            </b-form-group>
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
            <b-form-group label="Email"
                        label-cols="4"
                        content-cols>
            <b-form-input
                id="email"
                v-model="$v.form.email.$model"
                type="email"
                placeholder="email"
                :state="validationState('email')"
                required >
            </b-form-input>
            <b-form-invalid-feedback>This field is required.</b-form-invalid-feedback>
            </b-form-group>

            <b-form-group label="Role"
                        label-cols="4"
                        content-cols>
            <b-form-select v-model="selected" :options="options" required>
            </b-form-select>
            <b-form-invalid-feedback>This field is required.</b-form-invalid-feedback>
            </b-form-group>

            <b-card-footer class="bg-white">
            <b-button variant="outline-primary" 
                class="float-right"
                @click="onSubmit">submit</b-button>
            <b-button variant="outline-primary" 
                class=""
                @click="onCancel">cancel</b-button>
            </b-card-footer>
        </b-form>
    </b-card>
</template>

<script>
import { validationMixin } from "vuelidate"
import { required, alpha, email } from "vuelidate/lib/validators"
import { PROFILE, USERS } from '@/util/constants/Urls.js'
import Router from "@/router/index"

export default {
    name: "USerForm",
    mixins: [validationMixin,],

    data() {
      return {
          selected: 2,
          options: [
              {value: 2, text:"Subcontractor"},
              {value: 1, text: "General Contractor"},
          ],
        form: {
          email: this.$props.email,
          first_name: this.$props.first_name,
          last_name: this.$props.last_name,
        },
      }
    },

     props: {
    
      first_name: {
        type: String,
        default: "",
      },
      last_name: {
        type: String,
        default: ""
      },
      email: {
          type: String,
          default: ""
      },
    },
    computed: {
      showError() {
        return this.$store.state.users.status == "error"
      },
    },
    validations: {
      form: {

        first_name: {
          required,
          alpha,
        },
        last_name: {
          required,
          alpha,
        },
        email: {
          required,
          email
        },
        role: {
          required,
        }
      },
    },
    mounted() {
      console.log(this.props)
    },

    methods: {
      onSubmit() {

        if (this.$v.form.$anyError){
          this.onReset()
          return
        }
        this.$data.form.role = this.$data.selected
        const {first_name, last_name, ...data} = this.$data.form
        console.log(data)
        console.log(first_name, last_name, PROFILE)
        this.$http({url: USERS, data: data, method: "POST"}).then( (r) => {
            const id = r.data.id
            this.$http({url: `${PROFILE}${id}/`, data: {first_name: first_name, 
                                                    last_name: last_name}, 
                                                    method: "PATCH"}).then( (r) => {
                                                        console.log(r)
                                                        Router.push({name: "Directory"})
                                                    }).catch( e => {
                                                        console.log(e)
                                                    })
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
        Router.push({name: "Directory"})
      }
    },
}
</script>
