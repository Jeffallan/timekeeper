<template>
    <div>
        <h2 class="text-center">{{this.ACTION}} Work Item</h2>
        <b-card >
            <b-form @submit.stop.prevent="onSubmit" @reset="onReset" novalidate>
                <br />

                    <single-select type="location" 
                                   :id="parseInt($route.query.location)"
                                   ref="location"
                                   />
                    <single-select type="service"
                                  :id="parseInt($route.query.service)"
                                  @updateComponent="handleUpdate"
                                  ref="service" />
                    <single-select type="user"
                                  :id="USER"
                                  ref="provider"
                                  :disabled="CONTRACTOR"
                                  />

                <b-row class="text-center">
                    <b-col cols=6>
                <b-form-group label="Date"

                 >
                <b-form-datepicker
                  id="date"
                  v-model="$v.form.service_date.$model"
                  type="text"
                  placeholder="No Date Selected"
                  :state="validationState('service_date')"
                  today-button
                  reset-button
                  close-button
                  :date-format-options="{ year: '2-digit', month: 'numeric', day: 'numeric' }"
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
                  :disabled="$data.is_duration"
                  >
                </b-form-input>
                  <b-form-invalid-feedback>This field is required.</b-form-invalid-feedback>
                </b-form-group>
                </b-col>
                </b-row>
                <br />
                <b-row class="text-center">
                    <b-col>
                        <b-form-group label="Start Time">
                            <b-form-timepicker
                              id="start_time"
                              v-model="$v.form.start_time.$model"
                              :state="validationState('start_time')"
                              size="sm"
                              now-button
                              reset-button
                              minutes-step="15"
                              right
                              locale="en"
                            ></b-form-timepicker>
                            <b-form-invalid-feedback>This field is required.</b-form-invalid-feedback>
                        </b-form-group>
                    </b-col>
                    <b-col>
                        <b-form-group label="Stop Time">
                            <b-form-timepicker
                              id="stop_time"
                              v-model="$v.form.stop_time.$model"
                              :state="validationState('stop_time')"
                              size="sm"
                              now-button
                              reset-button
                              minutes-step="15"
                              right
                              locale="en"
                            ></b-form-timepicker>
                            <b-form-invalid-feedback>This field is required.</b-form-invalid-feedback>
                        </b-form-group>
                    </b-col>
                </b-row>
                <hr />
                <b-row>
                <b-col>
                <b-button variant="outline-primary" 
                class="text-center"
                @click="onCancel">cancel</b-button>
                </b-col>
                <b-col>
                <b-button variant="outline-success"
                v-if="this.$route.query.id"
                class=""
                @click="onBill">bill</b-button>
                </b-col>
                <b-col>
                <b-button variant="outline-primary" 
                class=""
                @click="onSubmit">submit</b-button>
                </b-col>
                </b-row>
            </b-form>
        </b-card>
    </div>
</template>

<script>
import {WORK, SERVICES} from '@/util/constants/Urls.js'
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

            },
            is_duration: false
        }
    },
    validations: {
        form: {
            billed: {required},
            units: {required: requiredUnless(function () {
                return this.$data.is_duration
            })},
            stop_time: {required},
            start_time: {required},
            service_date: {required},
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
                this.form.stop_time = r.data.stop_time
                this.form.start_time = r.data.start_time
                this.form.service_date = r.data.service_date

                this.$data.is_duration = r.data.service.is_duration

            }).catch(e => 
                    console.log(e)
            )
        }
    },
    updated(){
    },
    methods: {
        onReset(){
            return
        },
        onCancel(){
            Router.go(-1)
        },
        onSubmit(){
            this.$v.form.$touch()
            this.$refs.provider.$v.form.$touch()
            this.$refs.service.$v.form.$touch()
            this.$refs.location.$v.form.$touch()

            if (this.$v.form.$anyError || this.$refs.provider.$v.form.$anyError ||
                this.$refs.service.$v.form.$anyError || this.$refs.location.$v.form.$anyError){
               this.onReset()
               return
             }
            let data = this.form
            data.service = this.$refs.service.form.selected
            data.location = this.$refs.location.form.selected
            data.provider = this.$refs.provider.form.selected
            data.billed = false
            this.$http({url: this.URL, data: data, method: this.METHOD}).then( r =>{
                console.log(r.data)
                Router.go(-1)
            }).catch(e => {
                console.log(e)
            })
        },
        onBill() {
            return
        },
        validationState(name) {
            const { $dirty, $error } = this.$v.form[name]
            return $dirty ? !$error : null
            },
        handleUpdate(){
            this.$http.get(`${SERVICES}${this.$refs.service.form.selected}/`).then( r => {
                this.$data.is_duration = r.data.is_duration
                if (r.data.is_duration && !this.form.units){
                    this.form.units = 1
                }
            })
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
        CONTRACTOR() {
            return this.$store.state.users.user.role != 1
        },
        USER() {
            if (this.$route.query.provider && !this.CONTRACTOR) {
                return parseInt(this.$route.query.provider)
            }
            return this.$store.state.users.user.id
        },
    },
}
</script>