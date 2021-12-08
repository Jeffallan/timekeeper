<template>
  <div>
    <h1 class="text-center" v-if="$props.id">Update {{$props.type}} </h1>
    <h1 class="text-center" v-if="!$props.id">Create {{$props.type}} </h1>
    <b-card class="mx-3 text-center">
      <b-form  @submit.stop.prevent="onSubmit" @reset="onReset" novalidate >
        <generic-contact ref="contact" v-bind="$data.contact"></generic-contact>

        <b-button variant="outline-primary" 
                class="float-right"
                @click="onSubmit">submit</b-button>
      <b-button variant="outline-primary" 
                class=""
                @click="onCancel">cancel</b-button>
      </b-form>
    </b-card>
  </div>
</template>

<script>
import { LOCATIONS, CLIENTS } from '@/util/constants/Urls.js'
import GenericContact from "@/components/forms/GenericContact"
import Router from "@/router/index"


export default {
  name: "LocationClientCreate",
  components: {GenericContact,},

  data () {
    return {
      contact: {
          phone_number: this.$props.phone_number,
          name: this.$props.name,
          address_1: this.$props.address_1,
          address_2: this.$props.address_2,
          city: this.$props.city,
          state: this.$props.state,
          zip_code: this.$props.zip_code,
          id: this.$props.id,
      },
      extra: {

      },
    }
  },
  props: {
    id: {
      type: Number,
      default: null
    },
    type: {
      validator: function (value) {
        return ["location", "client"].indexOf(value) !== -1
      }
    },
     phone_number: {
        type: String,
        default: "",
      },
      name: {
        type: String,
        default: "",
      },
      address_1: {
        type: String,
        default: "",
      },
      address_2: {
        type: String,
        default: ""
      },
      city: {
        type: String,
        default: "",
      },
      state: {
        type: String,
        default: ""
      },
      zip_code: {
        type: Number,
        default: null
      },
  },
  computed: {
    baseURL() {
      return this.$props.type == "location" ? LOCATIONS : CLIENTS
    },
  METHOD() {
    return this.$props.id ? "PUT" : "POST"
  },
  URL() {
    return this.METHOD == "PUT" ? `${this.baseURL}${this.$props.id}/` : this.baseURL
  },
  NAME(){
    return this.$props.type == "location" ? "Locations" : "Clients"
  },
  PARAMS(){
    return {id: this.$props.id, type: this.$props.type}
  },
  },
  mounted() {

    console.log(Object.entries(this.$refs.contact))

  },
  methods: {
    onReset() {
      return
    },
    onCancel() {
      Router.push({name: this.NAME, params: this.PARAMS})
    },
    onSubmit() {

      this.$refs.contact.$v.form.$touch()
        if (this.$refs.contact.$v.form.$anyError){
          this.onReset()
          return
        }
      if (this.$props.type == "client"){
        const data = this.$refs.contact.form

        this.$http({url: this.URL, data: data, method: this.METHOD})
        .then( () => Router.push({name: this.NAME, params: this.PARAMS}))
        .catch( e => {
          console.log(e)
        })
      }
      else {
        return
      }
    },
  },
}
</script>


<style>

</style>