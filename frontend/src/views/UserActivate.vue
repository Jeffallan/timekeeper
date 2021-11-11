<template>
    <div>
        <b-card v-if="show"
            title="Activation Successful">
            <b-card-text>
                Please check your email to complete your account creation.
            </b-card-text>
        </b-card>
        <b-card v-if="showError"
            title="Activation Error"
            class="mx-3 text-center">
            <b-card-text>
                There was a problem activating your account. Please contact your administrator.
            </b-card-text>
        </b-card>
        <h1 v-if="show">SUCCESS</h1>
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