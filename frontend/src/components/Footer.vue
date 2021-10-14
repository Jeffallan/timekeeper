<template>
    <b-navbar class="footer" type="dark" variant="info">
    <footer>
        <b-nav-text>
        Raven Security Associates, INC. &copy; {{currentYear.getFullYear()}}
        </b-nav-text>
    </footer>
    </b-navbar>
</template>

<script>
export default {
    name: "Footer",
    props: {
        
    },
    data: () => {
        return {
                currentYear: new Date,
            }
        }   
    }
</script>

<style scoped>
    .footer{
        /*
        margin-top: 1em;
        height: 3em;
        */
        
    }
</style>