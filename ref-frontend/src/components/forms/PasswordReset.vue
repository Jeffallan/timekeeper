<template>
    <div class="col-md-5 mx-auto">
        <b-alert :show="onShow"
                dismissible
                @dismissed="onShow=false"
                >Check your email for a reset link
                </b-alert>
        <b-alert :show="showError"
                dismissible
                @dismissed="showError=false"
                variant="danger"
                >There was a problem processing your request
                <br />
                  Please enter a valid email address.
                </b-alert>
        <b-card header="Request Password Reset">
        <b-form @submit.stop.prevent="onSubmit" @reset="onReset" novalidate>
            <b-form-group
                id="email-input-group" 
                type="email"
                label="Email Address:"
                label-for="email">
                <b-form-input
                id="email"
                v-model="$v.form.email.$model"
                type="email"
                placeholder="Enter email"
                :state="validationState('email')"
                required >
                </b-form-input>
                 <b-form-invalid-feedback>This field is required.</b-form-invalid-feedback>
            </b-form-group>
            <hr />
      <b-form-group class="text-right">
        <b-button type="submit" variant="primary" class="pull-right">Submit</b-button>
      </b-form-group>
        </b-form>
        </b-card>
    </div>
</template>

<script>
//import Router from "@/router/index"
import axios from "axios"
import { FORGOT } from "@/util/constants/Urls"
import { validationMixin } from "vuelidate"
import { required, email } from "vuelidate/lib/validators"

export default {
    name: "PasswordReset",
    mixins: [validationMixin,],
    props: {

    },
    data() {
        return {
            form: {
                email: null
            },
            onShow: false,
            showError: false,
        }
    },
    validations: {
        form: {
            email: {
                required,
                email
            }
        }
    },
    methods: {
        validationState(name){
            const { $dirty, $error } = this.$v.form[name];
            return $dirty ? !$error : null;  
        },
        onSubmit() {
            this.$v.form.$touch()
            if (this.$v.form.$anyError){
                this.onReset()
                this.showError=true
                return
            }
            axios.post(FORGOT, {
                email: this.form.email
            })
            .then( (r) => {
                //console.log(r)
                if (r.status != 204) {
                    this.showError = true
                }
                else {
                    this.onShow = true
                }
            })
            .catch(( () => {
                //console.log(e)
                this.showError = true
            }))
        },
        onReset() {
            this.form = {
              email: null,
            }
            this.$nextTick(() => {
              this.$v.$reset()
            })
        },
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