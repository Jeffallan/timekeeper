<template>
    <span>
        <b-form-group :label="this.TYPE"
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
import { required, numeric} from "vuelidate/lib/validators"
import { CLIENTS, USERS, LOCATIONS, SERVICES } from '@/util/constants/Urls.js'

export default {
    name: "SingleSelect",

    mounted(){
        this.$http.get(this.URL).then(r => {
        r.data.results.forEach(i => {
            this.$data.form.options.push({value: i.id, text: i.name ? i.name : i.email})
        })
    })
    .catch(e =>{
        console.log(e)
    })
  },
  props: {
    type: {
      validator: function (value) {
      return ["user", "client", "location", "service"].indexOf(value) !== -1
      },
    },
    id: {
        type: Number,
        default: null,
    }
  },
  data() {
      return {
      form:{
          selected: this.$props.id,
          options: [{ value: null, text: 'Make Selection' },],
      },
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
  computed: {
      TYPE() {
        switch (this.$props.type) {
            case "user":
                return "Provider"
            case "client":
                return "Client"
            case "location":
                return "Location"
            case "service":
                return "Service"
            default:
                return null
        }
      },
    URL() {
        switch (this.$props.type) {
            case "user":
                return USERS
            case "client":
                return CLIENTS
            case "location":
                return LOCATIONS
            case "service":
                return SERVICES
            default:
                return null
        }
    },
  },
}
</script>
