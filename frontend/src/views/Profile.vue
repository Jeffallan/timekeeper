<template>
    <div>

    <b-card class="mx-4 text-center" :key="this.counter">
        <b-row >
            <b-col col sm="12" md="4">
          <b-card-text>
            <h4>Name</h4>
            <p>{{ this.data.first_name }} {{ this.data.last_name }}</p>
          </b-card-text>
          </b-col>
          <b-col col sm="12" md="4">
              <b-card-text>
              <h4>Email</h4>
            <a :href="'mailto:'+this.data.user.email">
                <b-icon icon="envelope" variant="info" font-scale="1.5"></b-icon>
            </a>
            </b-card-text>
          </b-col>
          <b-col col sm="12" md="4">
                <b-card-text>
                <h4>Phone</h4>
                <a :href="'tel:'+this.data.phone_number"
                >
                     <b-icon icon="telephone" variant="success" font-scale="1.5"></b-icon>
                    </a>
                </b-card-text>
          </b-col>
        </b-row>
        <b-card-text>

        </b-card-text> 
        <b-card-text  v-if="this.data.permissions.update == true">
            <h4>Mailing Address</h4>
            <p>{{ this.data.mailing_address }}</p>
        <hr />
        <b-button v-if="this.$store.state.users.user.role == 1 && this.data.user.is_active == true"
            variant="outline-danger"
            class="float-left"
            @click="handleDeactivate"
            >
            deactivate
        </b-button>
        <b-button v-if="this.$store.state.users.user.role == 1 && this.data.user.is_active == false"
            variant="outline-success"
            class="float-left"
            @click="handleDeactivate"
            >
            activate
        </b-button>
        <b-button variant="outline-primary"
                  class="float-right"
                  @click="handleClick"
                  >edit
        </b-button>
        </b-card-text>
    </b-card>
    </div>

</template>

<script>
//import axios from 'axios'
import { PROFILE, USERS } from '@/util/constants/Urls.js'
//import ProfileForm from "@/components/forms/ProfileForm.vue"
import Router from "@/router/index"

export default {

    name: "Profile",

    data () {
        return { 
            data: {
                user: {},
                phone_number: "",
                permissions: {},
            },
            counter: 0
            }
    },
    props: {
        id: {
            type: Number
        }
    },
    computed: {
        user() {
            return this.$store.state.users.user
        },
        phone() {
            if (this.data.phone_number != ""){
                return `(${this.data.phone_number.slice(2,5)}) ${this.data.phone_number.slice(5,8)}-${this.data.phone_number.slice(8,12)}`
            }
            return "-"
        }
    },
    created() {
        this.$http
        .get(`${PROFILE}${this.$props.id}/`)
        .then(r => (this.data = r.data)).catch(e => console.log(e))
    },
    methods: {

        handleClick() {
            const data = {...this.data}
            data.id = this.data.user.id
            Router.push({name: "ProfileEdit", params: this.data})
        },
        handleDeactivate() {
            this.$http({url: `${USERS}${this.data.user.id}/`,
                        data: {"is_active": !this.data.user.is_active},
                        method: "PATCH"}).then( (r) => {
                        console.log(r)
                        Router.push({name: "Directory"})
                        }).catch( e => {
                            console.log(e)
                        })
        },
    }
}
</script>

<style scoped>

</style>
