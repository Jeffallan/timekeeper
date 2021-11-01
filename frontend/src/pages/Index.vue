<template>
  <q-page class="flex flex-center">
    <div class="q-gutter-md" style="min-width: 350px">
      <q-input outlined v-model="email" label="email"></q-input>
      <q-input outlined v-model="text" label="password"></q-input>

        <q-btn color="primary"  >Submit</q-btn>

    </div>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'PageIndex'
})
</script>
