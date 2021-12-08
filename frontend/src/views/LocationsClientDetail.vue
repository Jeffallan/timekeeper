<template>
    <div>
    <h2 class="text-center">{{this.data.name}}</h2>
    <b-card class="mx-4 text-center">
        <b-row >
            <hr />
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
        <br />
        </b-card-text>
        <b-card-text  v-if="this.$store.state.users.user.role == 1">
            <h4>Mailing Address</h4>
            <p>{{ this.data.mailing_address }}</p>
        <hr />
        <b-button v-if="this.$store.state.users.user.role == 1 && this.data.is_active == true"
            variant="outline-danger"
            class="float-left"
            @click="handleDeactivate"
            >
            deactivate
        </b-button>
        <b-button v-if="this.$store.state.users.user.role == 1 && this.data.is_active == false"
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
import { LOCATIONS, CLIENTS } from '@/util/constants/Urls.js'
//import ProfileForm from "@/components/forms/ProfileForm.vue"
import Router from "@/router/index"

export default {

    name: "LocationsDetail",

    data () {
        return { 
            data: {

            },
            }
    },
    props: {
        id: {
            type: Number
        },
        type: {
        validator: function (value) {
        return ["location", "client"].indexOf(value) !== -1
      }
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
        },
        URL(){
            return this.$props.type == "location" ? LOCATIONS : CLIENTS
        },
        PUSH() {
            return this.$props.type == "location" ? "Locations" : "Clients"
        },
    },
    created() {
        console.log(this.$props)
        this.$http
        .get(`${this.URL}${this.$props.id}/`)
        .then(r => (this.data = r.data)).catch(e => console.log(e))
    },
    methods: {

        handleClick() {
            const data = {...this.data}
            data.id = this.data.id
            data.type = this.$props.type
            Router.push({name: "LocationsClientCreate", params: data})
        },
        handleDeactivate() {
            this.$http({url: `${this.URL}${this.data.id}/`,
                        data: {"is_active": !this.data.is_active},
                        method: "PATCH"}).then( () => {
                        console.log("Location Deactivated")
                        Router.push({name: this.PUSH})
                        }).catch( e => {
                            console.log(e)
                        })
        },
    }
}
</script>

<style scoped>

</style>