<template>
<div>
    <h1 class="text-center">Services</h1>
    <b-button variant="outline-primary" 
                  class="float-right my-2"
                  v-if="this.$store.state.users.user.role == 1"
                  @click="handleClick"> add
            <b-icon icon="plus"></b-icon>
        </b-button>
    <br />
    <b-table striped :items="this.results" :fields="this.fields">
            <template #cell(name)="d">
                <router-link :to="{ name: 'ServiceDetail', 
                                    query: {providers: d.item.providers, id: d.item.id, type: 'service'}
                                    }" >
                    {{d.item.name}}
                </router-link >
            </template>
            <template #cell(unit)="d">
                <p>{{ d.item.service_unit }}</p>
            </template>
            <template #cell(is_duration)="d">

                <b-icon icon="check" 
                        variant="success" 
                        font-scale="1.5" 
                        v-if="d.item.is_duration"
                        ></b-icon>
                <b-icon icon="x"
                variant="danger"
                font-scale="1.5"
                v-else></b-icon>

            </template>
        </b-table>
</div> 
</template>

<script>
import { SERVICES } from "@/util/constants/Urls.js"
import Router from "@/router/index"

export default {
    name: "Services",

    data() {
        return {
            results: [],
            fields: ["name", "unit", "is_duration"]
        }
    },
    mounted() {
        this.$http.get(SERVICES).then( r => {
            r.data.results.forEach(i => {
                this.results.push(i)
            })
        }).catch(e =>{
            console.log(e)
        })
    },
    methods: {
        handleClick(){
            Router.push({name: "ServiceCreate"})
        },
    },

}
</script>