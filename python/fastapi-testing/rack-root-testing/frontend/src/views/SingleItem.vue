<script>
    export default {
        data() {
            return {
                item: {}
            }
        },
        methods: {
            async getSingleItem(id) {
                const res = await fetch("http://localhost:8000/items/" + id);
                const itemResult = await res.json();

                if( res.status == 404 ) {
                    console.error("item not found")
                    this.$router.push('/404')
                }

                this.item = itemResult;
            },
            async deleteItem(id) {
                fetch('http://localhost:8000/items/' + id, {
                    method: 'DELETE'
                })
                    .then(resposne => response.json())
                    .then(data => console.log(data));
                
                this.$router.push('/items');
            },
            async editItem(id) {
                this.$router.push('/items/' + id + '/edit')
            }
        },
        mounted() {
            this.getSingleItem(this.$route.params.id);
        }
    }
</script>

<template>
    <h2>Single item page</h2><br />
    <ul>
        <li>Name: {{ item.name }}</li>
        <li>Description: {{ item.description }}</li>
        <li>Item ID in the DB: {{ item.id }}</li>
    </ul>
    <br />
    <form @submit.prevent="deleteItem(item.id)">
        <button>Delete Item</button>
    </form>
    <form @submit.prevent="editItem(item.id)">
        <button>Edit Item</button>
    </form>
</template>
