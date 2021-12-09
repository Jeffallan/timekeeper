<template>
<div>
    <h2 class="text-center">{{this.ACTION}} Service</h2>
<b-card :title=$data.results.name
        class="text-center">
    <b-form  @submit.stop.prevent="onSubmit" @reset="onReset" novalidate >
        <br />
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

        <multi-select ref="providers"
                      :providers="this.PROVIDERS"
                      v-bind="$data.form.approved_providers"
                      />

    </b-form>
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
    //    name: {
    //        type: String,
    //        default: ""
    //    },
    //    providers: {
    //        type: Array,
    //        default: () => []
    //    },
    },
    data() {
        return {
            results: {},
            options: {},
            form: {

            },
        }
    },
    mounted() {
        if (this.$route.query.id) {
            this.$http.get(this.URL).then(r => {
                this.$data.form = r.data
                console.log("Computed", this.PROVIDERS)
                console.log("Form",this.$data.form.approved_providers)
                console.log("Refs", Object.entries(this.$refs.providers.form))
            }).catch(e => {
                console.log(e)
            })
        }
    },
    computed: {
        ACTION() {
            return this.$route.query.id ? "Update" : "Create"
        },
        URL() {
            return this.$route.query.id ? `${SERVICES}${this.$route.query.id}/` : SERVICES
        },
        PROVIDERS() {
            if (this.$data.form.approved_providers){
                return this.$data.form.approved_providers
            }
            return []
        }
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
    },

    onCancel() {
        Router.go(-1)
    },

    validationState(name) {
      const { $dirty, $error } = this.$v.form[name]
      return $dirty ? !$error : null
      },
    }
}
</script>