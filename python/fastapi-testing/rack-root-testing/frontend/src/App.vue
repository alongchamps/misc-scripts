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
        .then(resposne => response.json())
        .then(data => console.log(data))
      }
    },
    mounted() {
      this.getItems()
    }
  }
</script>

<template>
  <!-- <div v-for="item in items">
    {{ item.name }} - {{ item.description }}
  </div> -->
  <ul>
    <li v-for="item in items">
      {{ item.name }} - {{ item.description }} - {{ item.id }}
      <form @submit.prevent="deleteItem(item.id)">
        <button>Delete Item</button>
      </form>
    </li>
  </ul>
</template>
