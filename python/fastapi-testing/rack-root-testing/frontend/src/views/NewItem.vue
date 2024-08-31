<script>
    export default {
        methods: {
            async newItem() {
                // todo
                this.$router.push('/items')
            },
        },
    }
</script>

<template>
    <h2>Make a new item</h2><br />
    <form v-on:submit.prevent="newItem()">
        <p>Name</p>
        <input v-model="name" placeholder="Device name" />
        <p>Description</p>
        <input v-model="description" placeholder="Description" />
        <br /><br />
        <button>Create Item</button>
    </form>
</template>
