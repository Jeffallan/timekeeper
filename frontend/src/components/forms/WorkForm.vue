<template>
    <div>
        <h2 class="text-center">{{this.ACTION}} Service</h2>
        <b-card >
            <b-form @submit.stop.prevent="onSubmit" @reset="onReset" novalidate>
                <br />

                    <single-select type="location" 
                                   :id="parseInt($route.query.location)"
                                   ref="location"
                                   />
                    <single-select type="service" 
                                  :id="parseInt($route.query.service)" 
                                  ref="service" />
                    <single-select type="user" 
                                  :id="parseInt($route.query.provider)" 
                                  ref="provider"/>

                <b-row class="text-center">
                    <b-col cols=7>
                <b-form-group label="Date"

                 >
                <b-form-datepicker
                  id="date"
                  v-model="$v.form.service_date.$model"
                  type="text"
                  placeholder=""
                  :state="validationState('service_date')"
                  today-button
                  reset-button
                  close-button
                  :date-format-options="{ year: 'numeric', month: 'numeric', day: 'numeric' }"
                  locale="en"
                  size="sm"
                  required >
                </b-form-datepicker>
                  <b-form-invalid-feedback>This field is required.</b-form-invalid-feedback>
                </b-form-group>
                </b-col>
                <b-col>
                    <b-form-group label="Units"

                 >
                <b-form-input
                  id="units"
                  v-model="$v.form.units.$model"
                  type="number"
                  placeholder="Units"
                  :state="validationState('units')"
                  size="sm"
                  :disabled="isDuration"
                  >
                </b-form-input>
                  <b-form-invalid-feedback>This field is required.</b-form-invalid-feedback>
                </b-form-group>
                </b-col>
                </b-row>

            </b-form>
        </b-card>
    </div>
</template>

<script>
import {WORK} from '@/util/constants/Urls.js'
import Router from "@/router/index"
import SingleSelect from "@/components/forms/SingleSelect"
import { required, requiredUnless } from "vuelidate/lib/validators"


export default {
  components: { SingleSelect },
    name: "WorkForm",
    data() {
        return {
            results: {
                location: {},
                service: {},
                permissions: {},
                provider: {},
                },
            form: {
                billed: false,
                units: null,
                provider: null,
                stop_time: null,
                start_time: null,
                service_date: null,
                service: null,
                location: null,
                id: null,

            }
        }
    },
    validations: {
        form: {
            billed: {required},
            units: {required: requiredUnless("isDuration")},
            provider: {required},
            stop_time: {required},
            start_time: {required},
            service_date: {required},
            location: {required},
        },
    },
    mounted() {
        if (this.$route.query.id){
          this.$http.get(`${WORK}${this.$route.query.id}/?expand=location,service,provider`)
            .then(r => {
                this.results = r.data

                this.form.id = r.data.id
                this.form.billed = r.data.billed
                this.form.units = r.data.units
                this.form.provider = r.data.provider.id
                this.form.stop_time = r.data.stop_time
                this.form.start_time = r.data.start_time
                this.form.service_date = r.data.service_date
                this.form.service = r.data.service.id
                this.form.location = r.data.location.id

            }).catch(e => 
                    console.log(e)
            )
        }
    },
    methods: {
        onReset(){
            return
        },
        onCancel(){
            Router.push(-1)
        },
        onSubmit(){
            return
        },
        validationState(name) {
            const { $dirty, $error } = this.$v.form[name]
            return $dirty ? !$error : null
            },
    },
    computed: {
         ACTION() {
            return this.$route.query.id ? "Update" : "Create"
        },
        URL() {
            return this.$route.query.id ? `${WORK}${this.$route.query.id}/` : WORK
        },
        METHOD() {
            return this.$route.query.id ? "PUT" : "POST"
        },
        isDuration(){
            return true
        }
    },
}
</script>