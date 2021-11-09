<template>
    <div>
        <h1 v-if="show">SUCCESS</h1>
        <h1 v-if=showError>Token Expired</h1>
    </div>
</template>

<script>
import axios from "axios"
import { USER_ACTIVATE } from "@/util/constants/Urls"

export default {
    name: "UserActivate",
    data () {
        return {
            uid: "",
            token: "",
            show: false,
            showError: false,
        }
    },
    methods: {
        onSubmit() {
           axios.post(USER_ACTIVATE, {
               uid: this.uid,
               token: this.token,
           })
        .then( r => {
            if (r.status != 204) {
                this.showError
            }
            else {
                this.show = true
            }
        })
        .catch( () => {
            this.showError = true
        })
        }
    },
    mounted () {
        const path = this.$route.path.split("/")
        this.token = path[3]
        this.uid = path[2]
        this.onSubmit()
    }
}

</script>

<style scoped>

</style>