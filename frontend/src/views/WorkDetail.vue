<template>
    <div>
        <h1 class="text-center">Work Item</h1>

        <b-card :title="results.location.name" class="text-center">
            <hr />
            <b-card-text class="text-left">
                <b-row>
                <b-col cols="4">
                Provider:
                </b-col>
                <b-col>
                {{ results.provider.email }}
                </b-col>
                </b-row>
            </b-card-text>
            <b-card-text  class="text-left">
                <b-row>
                <b-col cols="4">
                Service:
                </b-col>
                <b-col>
                {{ results.service.name }}
                </b-col>
                </b-row>
            </b-card-text>
            <b-card-text  class="text-left">
                <b-row>
                <b-col cols="4">
                Date:
                </b-col>
                <b-col>
                {{ results.service_date }}
                </b-col>
                </b-row>
            </b-card-text>
            <b-card-text  class="text-left">
                <b-row>
                <b-col cols="4">
                Start Time:
                </b-col>
                <b-col>
                {{ results.start_time }}
                </b-col>
                </b-row>
            </b-card-text>
            <b-card-text class="text-left">
                <b-row>
                <b-col cols="4">
                End Time:
                </b-col>
                <b-col>
                {{ results.stop_time }}
                </b-col>
                </b-row>
            </b-card-text>
            <b-card-text  class="text-left">
                <b-row>
                <b-col cols="4">
                Units:
                </b-col>
                <b-col>
                {{ results.units }}
                </b-col>
                </b-row>
            </b-card-text>
            <hr />
            <b-row v-if="results.permissions.write">
             <b-col cols=4>
             <b-icon icon="exclamation-circle-fill" variant="danger" font-scale="1.25"></b-icon>
             </b-col>
             <b-col class="text-left">
             <h4>Not Billed</h4>
             </b-col>
         </b-row>
            <span v-if="results.permissions.write">
            <hr />
           <b-button
            variant="outline-danger"
            class="float-left"
            @click="handleDelete"
            >
            delete
        </b-button>
        <b-button
            variant="outline-primary"
            class="float-right"
            @click="handleEdit"
            >
            edit
        </b-button>
        </span >
         <b-row v-if="!this.results.permissions.write">
             <b-col cols=5>
             <b-icon icon="exclamation-circle-fill" variant="success" font-scale="1.5"></b-icon>
             </b-col>
             <b-col class="text-left">
             <h4>Billed</h4>
             </b-col>
         </b-row>
        </b-card>

    </div>
</template>

<script>
import {WORK} from '@/util/constants/Urls.js'
import Router from "@/router/index"

export default {
    name: "WorkDetail",
    data() {
        return {
            results: {
                billed: false,
                id: null,
                location: {},
                permissions: {},
                service: {},
                provider: {},
                service_date: "",
                start_time: "",
                stop_time: "",
                units: null,
            },
            provider_name: ""
        }
    },
    mounted() {
    this.$http.get(this.URL).then(r => {
        this.results = r.data
        }).catch(e => {
            console.log(e)
        })
    },

    methods: {
        ROUND(val) {
            return Math.round(val *100) / 100
        },
        handleEdit() {
            Router.push({name: "WorkCreate", query: {id: this.results.id, 
                                                    location: this.results.location.id,
                                                    service: this.results.service.id,
                                                    provider: this.results.provider.id}})
        },
        handleDelete(){
            return
        },
        confirmDelete(){
            this.$http.delete(`${WORK}${this.$route.query.id}`)
            Router.push("Work")
        },
    },
    computed: {
        URL() {
            return `${WORK}${this.$route.query.id}/?expand=location,service,provider`
        },
    },
}
</script>