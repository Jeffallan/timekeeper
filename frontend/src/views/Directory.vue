<template>
    <div>

        <b-button variant="outline-primary" 
                  class="float-right my-2"
                  v-if="this.$store.state.users.user.role == 1">
            <b-icon icon="plus"></b-icon>
        </b-button>
 
        <br />
        <b-table striped :items="this.data.items" :fields="this.data.fields">
            <template #cell(name)="d">
                <router-link to="/profile/">
                    {{d.item.name}}
                </router-link>
            </template>
            <template #cell(call)="d">
                <a :href="'tel:'+d.item.phone_number"
                >
                     <b-icon icon="telephone" variant="success" font-scale="1.5"></b-icon>
                    </a>
            </template>
            <template #cell(email)="d">
                <a :href="'mailto:'+d.item.email">
                <b-icon icon="envelope" variant="info" font-scale="1.5"></b-icon>
            </a>
            </template>
        </b-table>
    </div>
</template>

<script>

import { PROFILE } from "@/util/constants/Urls.js"

export default {

    name: "Directory",

    data() {
        return {
            data: {
                results: {},
                items: [],
                fields: ["name", "call", "email"],
            },
        }
    },

    created() {
        this.$http.get(PROFILE)
            .then( r => {
                this.data.results = r.data
                let data = r.data.results
                console.log(data)
                data.forEach(e => {
                    this.data.items.push({name: e.first_name + " " + e.last_name,
                                          call: e.phone_number,
                                          email: e.user.email,
                                          id: e.id
                                         })
                });
            })
            .catch( e => console.log(e))
    },
    computed: {

    }
}
</script>

<style scoped>

</style>