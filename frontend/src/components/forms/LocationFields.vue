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
    </span>
</template>

<script>
import { validationMixin } from "vuelidate"
import { required, numeric} from "vuelidate/lib/validators"

export default {
    name: "LocationFields",
    mixins: {validationMixin,},
    mounted() {
    console.log("Extra props", Object.entries(this.$props))
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
                options: []
            }
        }
    },
    validations: {
        form: {
        selected: {
            required,
            numeric,
        },
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