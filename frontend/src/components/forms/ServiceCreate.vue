<template>
<div>
    <h2 class="text-center">{{this.ACTION}} Service</h2>
<b-card :title=$data.form.name
        class="text-center">
    <b-form  @submit.stop.prevent="onSubmit" @reset="onReset" novalidate >
        <br />
        <b-form-group label="Name"
                 >
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

      <b-row>
        <b-col cols="4">
      <b-form-group label="Duration"
                  >

      <b-form-checkbox
        id="duration"
        v-model="form.is_duration"
        switch
        size="lg"
        required >
      </b-form-checkbox>
        <b-form-invalid-feedback>This field is required.</b-form-invalid-feedback>
      </b-form-group> 
      </b-col>
      <b-col >
          <b-form-group label="Unit"
                        >
          <b-form-select v-model="selected"
                         :options="options"
                         text-field="display_name">

          </b-form-select>
          <b-form-invalid-feedback>This field is required.</b-form-invalid-feedback>
          </b-form-group>
      </b-col>
    </b-row>

        <multi-select ref="providers"
                     :providers="PROVIDERS"
                      v-bind="form.providers"
                      />

    </b-form>
    <b-button @click="onSubmit()">button</b-button>
</b-card>
</div>

</template>

<script>
import { SERVICES } from '@/util/constants/Urls.js'
import Router from "@/router/index"
import MultiSelect from "@/components/forms/MultiSelect"
import { required } from "vuelidate/lib/validators"

export default {
    name: "ServiceCreate",
    components: {MultiSelect},
    props: {

    },
    data() {
        return {
            selected: null,
            results: {},
            options: [
                { value: null, display_name: 'Please select an option' },
                ],
            form: {
                id: 0,
                name: "",
                is_duration: false,
                providers: []
            },
        }
    },
    mounted() {

        if (this.$route.query.id) {
            this.$http.get(this.URL).then(r => {
                this.$data.form = r.data
                this.$data.selected = r.data.service_unit
            }).catch(e => {
                console.log(e)
            })
        }
        this.$http.options(SERVICES).then(r => {
            this.options = r.data.actions.POST.service_unit.choices
            console.log("options", Object.values(this.options))
            //r.data.actions.POST.service_unit.choices.forEach(i => {
            //    console.log("foreacj",i)
            //    this.options.push({ value: i.value, text: i.display_name})
            }).catch(e => {
                console.log(e)
            })
        },

    computed: {
        ACTION() {
            return this.$route.query.id ? "Update" : "Create"
        },
        URL() {
            return this.$route.query.id ? `${SERVICES}${this.$route.query.id}/` : SERVICES
        },
        PROVIDERS() {
            return this.form.providers
            // return [1,2,3,4,5,6,7,8,]
        },
    },
    validations: {
        form: {
            name: {
                required,
            },
        },
    },
    methods: {
        onReset() {
            return
        },

    onSubmit() {
        console.log("Refs", this.$refs.providers.form.selected)
    },

    onCancel() {
        Router.go(-1)
    },

    validationState(name) {
      const { $dirty, $error } = this.$v.form[name]
      return $dirty ? !$error : null
      },
      getProviders(){
          return this.$data.results.providers
      },
    }
}
</script>