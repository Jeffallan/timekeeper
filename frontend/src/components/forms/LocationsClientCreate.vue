<template>
  <div>
    <h1 class="text-center" v-if="$props.id">Update {{$props.type}} </h1>
    <h1 class="text-center" v-if="!$props.id">Create {{$props.type}} </h1>
  </div>
</template>

<script>
import { LOCATIONS, CLIENTS } from '@/util/constants/Urls.js'
export default {
  name: "Location Client Create",
  props: {
    id: {
      type: Number,
      default: null
    },
    type: {
      validator: function (value) {
        return ["location", "client"].indexOf(value) !== -1
      }
    }
  },
  computed: {
    URL() {
      return this.$props.type == "location" ? LOCATIONS : CLIENTS
    },

  },
}
</script>


<style>

</style>