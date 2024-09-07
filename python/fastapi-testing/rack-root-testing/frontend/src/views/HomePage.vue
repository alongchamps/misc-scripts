<script>
export default {
    data() {
        return {
            itemCount: 0
        }
    },
    methods: {
        async getItems() {
            const res = await fetch("http://localhost:8000/items")
            const finalItems = await res.json()
            this.itemCount = finalItems.length
        }
    },
    mounted() {
        this.getItems()
    }
}
</script>
<!-- 
<template>
    <Panel header="Summary">
        <tempalte>
            <p class="m-0">You have {{ itemCount }} items.</p>
        </tempalte>
    </Panel>
</template> -->




<template>
    <div class="p-md-10 p-jc-center">
        <Panel>
            <template #header>
                Home Page
            </template>
            <tempalte>
                <p class="m-0">You have {{ itemCount }} items.</p>
            </tempalte>
        </Panel>
    </div>
</template>
