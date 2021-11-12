<template>
    <div>
        <b-card v-if="show"
            title="Success"
            class="mx-3 text-center">
            <b-card-text>
                Your email address has been changed successfully.
            </b-card-text>
        </b-card>
        <b-card v-if="showError"
            title="Error"
            class="mx-3 text-center">
            <b-card-text>
                There was a problem while trying to change your email.
            </b-card-text>
        </b-card>
    </div>
</template>

<script>
import axios from "axios"
import { USERNAME_RESET } from "@/util/constants/Urls"

export default {
    name: "UsernameReset",
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
           axios.post(USERNAME_RESET, {
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