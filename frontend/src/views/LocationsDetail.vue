<template>
    <div>

    <b-card class="mx-4 text-center" :key="this.counter">
        <b-row >
            <b-col col sm="12" md="4">
          <b-card-text>
            <h4>Name</h4>
            <p>{{ this.data.location.name }}</p>
          </b-card-text>
          </b-col>

          <b-col col sm="12" md="4">
                <b-card-text>
                <h4>Phone</h4>
                <a :href="'tel:'+this.data.location.phone_number"
                >
                     <b-icon icon="telephone" variant="success" font-scale="1.5"></b-icon>
                    </a>
                </b-card-text>
          </b-col>
        </b-row>
        <b-card-text>

        </b-card-text>
        <b-card-text  v-if="this.$store.state.users.user.role == 1">
            <h4>Mailing Address</h4>
            <p>{{ this.data.location.mailing_address }}</p>
        <hr />
        <b-button v-if="this.$store.state.users.user.role == 1"
            variant="outline-danger"
            class="float-left"
            @click="handleDeactivate"
            >
            deactivate
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
import { LOCATIONS } from '@/util/constants/Urls.js'
//import ProfileForm from "@/components/forms/ProfileForm.vue"
import Router from "@/router/index"

export default {

    name: "LocationsDetail",

    data () {
        return { 
            data: {
                location: {},
                providers: {},
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
                return `(${this.data.location.phone_number.slice(2,5)}) ${this.data.phone_number.slice(5,8)}-${this.data.phone_number.slice(8,12)}`
            }
            return "-"
        }
    },
    created() {
        console.log(this.$props)
        this.$http
        .get(`${LOCATIONS}${this.$props.id}/`)
        .then(r => (this.data.location = r.data)).catch(e => console.log(e))
    },
    methods: {

        handleClick() {
            const data = {...this.data}
            data.id = this.data.location.id
            Router.push({name: "LocationsClientCreate", params: this.data})
        },
        handleDeactivate() {
            this.$http({url: `${LOCATIONS}${this.data.user.id}/`,
                        data: {"is_active": false},
                        method: "PATCH"}).then( () => {
                        console.log("Location Deactivated")
                        Router.push({name: "Locations"})
                        }).catch( e => {
                            console.log(e)
                        })
        },
    }
}
</script>

<style scoped>

</style>