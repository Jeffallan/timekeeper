<template>
<div>
    <h1 class="text-center">{{results.name}}</h1>
    <b-card>
        <b-card-text>
            <p>Billing Unit: {{results.service_unit}}</p>
        </b-card-text>
        <b-card-text>
            <p>Duration: {{YESNO}}</p>
        </b-card-text>
    </b-card>
    <br />
    <b-button variant="outline-primary"
                  class="float-right"
                  @click="handleClick"
                  >edit
        </b-button>
</div>
</template>

<script>
import Router from "@/router/index"
import { SERVICES } from "@/util/constants/Urls.js"

export default {
    name: "ServiceDetail",
    data() {
        return {
            results: {}
        }
    },
    mounted(){
        this.$http.get(`${SERVICES}${this.$route.query.id}/`).then(r => {
            console.log(r.data)
            this.$data.results = r.data
            console.log(this.$data)
        }).catch(e => {
            console.log(e)
        })
    },
    methods: {
        handleClick(){
            Router.push({name: "ServiceCreate", 
            query: {providers: this.$route.query.providers, 
                    id: this.$route.query.id, 
                    type: 'service'}})
        },
    },
    computed: {
        YESNO(val){
            return val == false ? "No" : "yes"
        },
    },
}
</script>
