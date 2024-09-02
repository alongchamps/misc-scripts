<script>
    export default {
        data() {
            return {
                items: []
            }
        },
        methods: {
            async getItems() {
                const res = await fetch("http://localhost:8000/items")
                const finalItems = await res.json()
                this.items = finalItems;
            },
            async deleteItem(id) {
                fetch('http://localhost:8000/items/' + id, {
                    method: 'DELETE'
                })
                    // .then(resposne => response.json())
                    // .then(data => console.log(data))
                this.items = this.getItems()
            }
        },
        mounted() {
            this.getItems()
        }
    }
</script>

<template>
    <h2>All items page</h2>
    <router-link :to="{ name: 'NewItem' }">New Item</router-link>
    <ul>
        <li v-for="item in items" :key="item.id">
            <router-link :to="{ name: 'SingleItem', params: { id: item.id } }">{{ item.name }}</router-link> - {{ item.description }} - {{ item.id }}
            <form @submit.prevent="deleteItem(item.id)">
                <button>Delete Item</button>
            </form>
            <br />
        </li>
    </ul>
</template>
