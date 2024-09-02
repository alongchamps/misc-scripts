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
            async newItem(event) {
                const res = await fetch('http://localhost:8000/items/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify( this.form )
                })
                const newItem = await res.json()
                this.$router.push('/items/' + newItem.id)
                // .then(this.$router.push('/items/' + response.json().id ))
                // todo: make this go to the SingleItem.vue page for the new item
                // the backend may need to return the new ID
                // this.$router.push('/items/' + JSON.parse(res.json()).id)
            },
        },
    }
</script>

<template>
    <h2>Make a new item</h2><br />
    <form v-on:submit.prevent="newItem()">
        <p>Name</p>
        <input v-model="form.name" lazy/>
        <p>Description</p>
        <input v-model="form.description" lazy/>
        <br /><br />
        <button>Create Item</button>
    </form>
</template>
