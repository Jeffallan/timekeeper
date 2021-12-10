<template>
    <div>
        <h1 class="text-center">Work Performed</h1>
        <b-button variant="outline-primary" 
                  class="float-right my-2"
                  @click="handleClick"> add
            <b-icon icon="plus"></b-icon>
        </b-button>
        <br />
        <b-table striped :items="this.results" :fields="this.fields" 
                @row-clicked="$router.push({name: 'WorkCreate', query:{id: item.id}})" small>
            <template #cell(location)="d">
                {{ d.item.location.name }}
            </template>
            <template #cell(service)="d">
                {{ d.item.service.name }}
            </template>
            <template #cell(details)="d" >
                 <router-link :to="{ name: 'WorkDetail',
                                    query: {id: d.item.id}
                                    }" >
                    Go
                </router-link >
            </template>
        </b-table>
    </div>
</template>

<script>
import {WORK} from '@/util/constants/Urls.js'
import Router from "@/router/index"

export default {
    name: "Work",

    data(){
        return {
            results: [],
            fields: ["location","service", "details"]
        }
    },
    mounted() {
        this.$http.get(`${WORK}?expand=location,service`).then(r => {
            this.results = r.data.results
        }).catch(e => {
            console.log(e)
        })
    },
    methods: {
        handleClick() {
            Router.push({name: "WorkCreate"})
        },
        ROUND(val) {
            return Math.round(val *100) / 100
        }
    },
    computed: {

    }
}
</script>