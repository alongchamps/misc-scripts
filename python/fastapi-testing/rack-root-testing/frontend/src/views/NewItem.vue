<script>
    export default {
        data(){
            return {
                form: {
                    itemName: '',
                    itemDescription: ''
                }
            }
        },
        methods: {
            async newItem() {
                const res = await fetch('http://localhost:8000/items/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                            name: this.itemName,
                            description: this.itemDescription
                        })
                    // body: JSON.stringify(this.form)
                })
                // .then(this.$router.push('/items'))
                // todo: make this go to the SingleItem.vue page for the new item
                // the backend may need to return the new ID
                this.$router.push('/items')
            },
        },
    }
</script>

<template>
    <h2>Make a new item</h2><br />
    <form v-on:submit.prevent="newItem()">
        <p>Name</p>
        <input v-model="itemName" />
        <p>Description</p>
        <input v-model="itemDescription" />
        <br /><br />
        <button>Create Item</button>
    </form>
</template>
