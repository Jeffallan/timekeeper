<template>
    <span>
        <b-form-group label="Client"
                        label-cols="4"
                        content-cols>
            <b-form-select v-model="$v.form.selected.$model" 
                          :options="form.options"
                          :state="validationState('selected')"
                          required>
            </b-form-select>
            <b-form-invalid-feedback>This field is required.</b-form-invalid-feedback>
            </b-form-group>
             <b-form-group label="Providers"
                        >
            <b-form-select v-model="$v.form.selected_providers.$model" 
                          :options="form.provider_options"
                          :state="validationState('selected_providers')"
                          multiple
                          :select-size="5"
                          required
                          class="text-center">
            </b-form-select>
            <b-form-invalid-feedback>This field is required.</b-form-invalid-feedback>
            </b-form-group>
    </span>
</template>

<script>
import { validationMixin } from "vuelidate"
import { required, numeric} from "vuelidate/lib/validators"
import { CLIENTS, USERS } from '@/util/constants/Urls.js'

export default {
    name: "LocationFields",
    mixins: {validationMixin,},
    mounted() {
    //console.log("Extra props", Object.entries(this.$props))
    this.$http.get(CLIENTS).then(r => {
        r.data.results.forEach(i => {
            this.$data.form.options.push({value: i.id, text: i.name})
        })
    })
    .catch(e =>{
        console.log(e)
    })
    this.$http.get(USERS).then(r => {
        r.data.results.forEach(i => {
            this.$data.form.provider_options.push({value: i.id, text: i.email})
        })
    })
    .catch(e =>  {
        console.log(e)
    })
    },
    props: {
        client: {
            type: Number,
            default: null
        },
        providers: {
            type: Array,
            default: () => [],
        },
    },
    data() {
        return {
            form: {
                selected: this.$props.client,
                options: [{ value: null, text: 'Make Selection' },],
                selected_provider: this.$props.providers,
                provider_options: [],
            }
        }
    },
    validations: {
        form: {
        selected: {
            required,
            numeric,
        },
        selected_providers: {
            //required,
        }
        },
    },
    methods: {
        validationState(name) {
          const { $dirty, $error } = this.$v.form[name]
          return $dirty ? !$error : null
        },
    },
}
</script>