<template>
    <span>

        <b-form-group   label="Providers"
                        label-cols="4"
                        content-cols
                        >

        <b-button v-b-toggle.collapse small variant="primary" class=""><b-icon icon="arrow-down"></b-icon></b-button>

        <b-collapse id="collapse" class="mt-2">

        <b-form-checkbox-group v-model=form.selected
                               :options=form.options
                               value-field="value"
                               text-field="text"
                               class="text-left"
                               stacked>

        </b-form-checkbox-group>
        </b-collapse>
        </b-form-group>
        <br />
        </span>
</template>

<script>
//import { required, numeric} from "vuelidate/lib/validators"
import { USERS, SERVICES, LOCATIONS } from '@/util/constants/Urls.js'

export default {
    name: "MultiSelect",

    beforeMount(){
        console.log("Props",this.$props.providers)
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
  computed: {
      URL(){
      return this.$route.query.type == "service" ? 
                                      `${SERVICES}${this.$route.query.id}/` :
                                      `${LOCATIONS}${this.$route.query.id}/`
      },
  }
}
</script>