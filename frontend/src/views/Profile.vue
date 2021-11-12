<template>
    <div>
    <!--
    <b-modal id="edit" @ok="handleOk" title="Edit Profile">
        <ProfileForm ref="edit"
        :email=this.data.user.email
        :id=this.data.user.id
        :first_name=this.data.first_name
        :last_name=this.data.last_name
        :phone_number=this.data.phone_number
        :address_1= this.data.address_1
        :address_2= this.data.address_2
        :city=this.data.city
        :state=this.data.state
        :zip_code=this.data.zip_code
        />
    </b-modal>
    -->
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
            <a :href="'mailto:'+this.data.user.email">{{ this.data.user.email }}</a>
            </b-card-text>
          </b-col>
          <b-col col sm="12" md="4">
                <b-card-text>
                <h4>Phone</h4>
                <a :href="'tel:'+this.data.phone_number">
                    ({{ this.data.phone_number.slice(2,5) }})
                    {{ this.data.phone_number.slice(5,8) }}-{{ this.data.phone_number.slice(8,12) }}
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

        <b-button variant="outline-primary"
                  class="float-right"
                  v-b-modal.edit
                  @click="handleClick"
                  >edit
        </b-button>
        </b-card-text>
    </b-card>
    </div>

</template>

<script>
//import axios from 'axios'
import { PROFILE } from '@/util/constants/Urls.js'
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
    components: {
        //ProfileForm,
    },
    computed: {
        user() {
            return this.$store.state.users.user
        },
    },
    created() {
        this.$http
        .get(`${PROFILE}${this.$store.state.users.user.id}/`)
        .then(r => (this.data = r.data)).catch(e => console.log(e))
    },
    methods: {

        handleClick() {
            const data = {...this.data}
            data.id = this.data.user.id
            Router.push({name: "ProfileEdit", params: {...data}})
        },
    }
}
</script>

<style scoped>

</style>
