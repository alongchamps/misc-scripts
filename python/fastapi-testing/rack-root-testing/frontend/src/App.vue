<!-- <script>
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
        .then(resposne => response.json())
        .then(data => console.log(data))
      }
    },
    mounted() {
      this.getItems()
    }
  }
</script> -->

<!-- 
<template>
  <!-- <div v-for="item in items">
    {{ item.name }} - {{ item.description }}
  </div> 
  <ul>
    <li v-for="item in items">
      {{ item.name }} - {{ item.description }} - {{ item.id }}
      <form @submit.prevent="deleteItem(item.id)">
        <button>Delete Item</button>
      </form>
    </li>
  </ul>
</template> -->

<template>
    <div>
        <!-- Example below this line to link by a name -->
        <router-link :to="{ name: 'Home' }">Home</router-link>
        <router-link :to="{ name: 'AllItems' }">Items</router-link>
    </div>
    <br />
    <router-view />
</template>

<style>
    .router-link-exact-active {
        color: white
    }
</style>
