<template>
    <span>
        <b-form-group   label="Providers"
                        label-cols="4"
                        content-cols>
            <b-form-select v-model="$v.form.selected.$model" 
                          :options="form.options"
                          :state="validationState('selected')"
                          multiple
                          required>
            </b-form-select>
            <b-form-invalid-feedback>This field is required.</b-form-invalid-feedback>
        </b-form-group>
        </span>
</template>

<script>
//import { required, numeric} from "vuelidate/lib/validators"
import { USERS } from '@/util/constants/Urls.js'

export default {
    name: "SingleSelect",

    mounted(){
        this.$http.get(USERS).then(r => {
        r.data.results.forEach(i => {
            this.$data.form.options.push({value: i.id, text: i.email})
        })
    })
    .catch(e =>{
        console.log(e)
    })
  },
  props: {
    providers: {
            type: Array,
            default: () => [],
        },
  },
  data() {
      return {
      form:{
          selected: this.$props.providers,
          options: [],
      },
    }
  },
  validations: {
      form: {
          selected: {
              //required,
              //numeric,
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