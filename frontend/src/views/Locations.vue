<template>
    <div>
        <h1 class="text-center">Locations</h1>
        <b-button variant="outline-primary" 
                  class="float-right my-2"
                  v-if="this.$store.state.users.user.role == 1"
                  @click="handleClick"> add
            <b-icon icon="plus"></b-icon>
        </b-button>
 
        <br />
        <b-table striped :items="this.data.items" :fields="this.data.fields">
            <template #cell(name)="d">
                <router-link :to="{ name: 'LocationsClientDetail', 
                                    params: {id: d.item.id, type: 'location'},
                                    }" >
                    {{d.item.name}}
                </router-link>
            </template>
            <template #cell(call)="d">
                <a :href="'tel:'+d.item.phone_number"
                >
                     <b-icon icon="telephone" variant="success" font-scale="1.5"></b-icon>
                    </a>
            </template>
            <template #cell(mail)>

                <b-icon icon="envelope" variant="info" font-scale="1.5"></b-icon>

            </template>
        </b-table>
    </div>
</template>

<script>

import { LOCATIONS } from "@/util/constants/Urls.js"
import Router from "@/router/index"

export default {

    name: "Directory",

    data() {
        return {
            data: {
                results: {},
                items: [],
                fields: ["name", "call", "mail"],
            },
        }
    },

    created() {
        this.$http.get(LOCATIONS)
            .then( r => {
                this.data.results = r.data
                let data = r.data.results
                console.log(data)
                data.forEach(e => {
                    this.data.items.push({name: e.name,
                                          call: e.phone_number,
                                          mail: e.mailing_address,
                                          id: e.id
                                         })
                });
            })
            .catch( e => console.log(e))
    },
    computed: {

    },
    methods: {
        handleClick() {
            Router.push({name:"LocationsClientCreate", params: {type: "location"}})
        }
    },
}
</script>

<style scoped>

</style>