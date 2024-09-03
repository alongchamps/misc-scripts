<script>
    export default {
        data() {
            return {
                form: {
                    name: '',
                    description: ''
                }
            }
        },
        methods: {
            async populateInputs() {
                const result = await fetch('http://localhost:8000/items/' + this.$route.params.id )
                this.form = await result.json()
            },
            async updateItemDetails() {
                const res = await fetch('http://localhost:8000/items/' + this.$route.params.id, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify( this.form )
                })
                this.$router.push('/items/' + this.$route.params.id)
            },
        },
        mounted() {
            this.populateInputs()
        }
    }
</script>

<template>
    <h2>Edit an item</h2><br />
    <form v-on:submit.prevent="updateItemDetails()">
        <p>Name</p>
        <input v-model="form.name" lazy/>
        <p>Description</p>
        <input v-model="form.description" lazy/>
        <br /><br />
        <button>Update Item Details</button>
    </form>
</template>
