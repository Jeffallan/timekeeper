<template>
    <b-card class="mx-5">
        <b-card-text>
            {{ this.data }}
        </b-card-text>
    </b-card>
</template>

<script>
//import axios from 'axios'
import { PROFILE } from '@/util/constants/Urls.js'

export default {
    name: "Profile",

    data () {
        return { 
            data: null,
            }
    },

    computed: {
        user() {
            return this.$store.state.users.user
        },
    },
    mounted() {
        this.$http
        .get(PROFILE)
        .then(r => (this.data = r.data)).catch(e => console.log(e))
        console.log(this.data)
    },
}
</script>

<style scoped>

</style>
