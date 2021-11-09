<template>
    <div class= "col-md-5 mx-auto">
        <b-alert :show="onShow"
                 dismissible
                 @dismissed="onShow=false">
            Password reset successful.
        </b-alert>
        <b-alert :show="showError"
                 dismissible
                 @dismissed="showError=false"
                 variant="danger"
                 >
            There was a problem processing your request.
        </b-alert>
        <b-card header="Password Reset">
            <b-form @submit.stop.prevent="onSubmit" @reset="onReset" novalidate>
                <b-form-group
                    id="password-form-group"
                    type="password"
                    label="New Password"
                    label-for="password" >
                    <b-form-input id="password"
                                  v-model="$v.form.new_password.$model"
                                  type="password"
                                  placeholder="New Password"
                                  :state="validationState('new_password')"
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

import { validationMixin } from "vuelidate"
import { required } from "vuelidate/lib/validators"
import axios from "axios"
import { PASSWORD_CONFIRM } from "@/util/constants/Urls"

export default {
    
    name: "PasswordResetConfirm",
    mixins: [validationMixin,],
    props: {

    },
    validations: {
        form: {
            new_password: {
                required,
            }
        }
    },
    data () {
        return {
            form: {
               uid: "",
               token: "",
               new_password: "",
            },
            onShow: false,
            showError: false,
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
            axios.post(PASSWORD_CONFIRM, {
                new_password: this.form.new_password,
                uid: this.form.uid,
                token: this.form.token,
            })
            .then(( (r) => {
                //console.log(r)
                if (r.status != 204) {
                    this.showError = true
                }
                else {
                    this.onShow=true
                }
            }))
            .catch(( () => {
                //console.log(e)
                this.showError=true
            }))
        },
        onReset() {
            this.form = {
              password: null,
            }
            this.$nextTick(() => {
              this.$v.$reset()
            })
        },
    },
    mounted () {
        const path = this.$route.path.split("/")
        this.form.token = path[3]
        this.form.uid = path[2]
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