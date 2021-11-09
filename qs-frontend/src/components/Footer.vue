<template>
    <footer class="is-footer p-4 has-background-primary has-text-primary-light">
        <b-nav-text>
        Raven Security Associates, INC. &copy; {{currentYear.getFullYear()}}
        </b-nav-text>
    </footer>

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