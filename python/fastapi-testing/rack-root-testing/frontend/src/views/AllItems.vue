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
    <div class="p-md-10 p-jc-left">
        <Panel>
            <template #header>
                All items list
                <input></input>
            </template>
            <div class="grid">
                <div class="col-12">
                    <DataTable :value="items" dataKey="id">
                        <Column field="name" header="Name" ref="name" :sortable="true" :style="{width:'200px'}">
                        </Column>

                        <Column field="id" header="ID" :sortable="true" :style="{width:'100px'}">
                        </Column>

                        <Column field="description" header="Description" :sortable="true" :style="{width:'200px'}">
                        </Column>

                        <Column header="Delete" :style="{width:'100px'}">
                            #todo
                        </column>

                    </DataTable>
                </div>
            </div>
        </Panel>
    </div>
</template>

<!-- 
<li v-for="item in items" :key="item.id">
    <router-link :to="{ name: 'SingleItem', params: { id: item.id } }">{{ item.name }}</router-link> - {{ item.description }} - {{ item.id }}
    <form @submit.prevent="deleteItem(item.id)">
        <pvbutton>Delete Item</pvbutton>
    </form>
    <br />
</li> -->


<!-- 

<div class="col-12">
    <div class="card">
        <h5>Frozen Columns</h5>

        <DataTable :value="customer2" :scrollable="true" scrollHeight="400px" :loading="loading2" scrollDirection="both" class="mt-3">
            <Column field="name" header="Name" :style="{width:'150px'}" frozen></Column>
            <Column field="id" header="Id" :style="{width:'100px'}" :frozen="idFrozen"></Column>
            <Column field="name" header="Name" :style="{width:'200px'}"></Column>
            <Column field="country.name" header="Country" :style="{width:'200px'}">
                <template #body="{data}">
                    <img src="../assets/demo/flags/flag_placeholder.png" :class="'flag flag-' + data.country.code" width="30" />
                    <span style="margin-left: .5em; vertical-align: middle" class="image-text">{{data.country.name}}</span>
                </template>
            </Column>
            <Column field="date" header="Date" :style="{width:'200px'}"></Column>
            <Column field="company" header="Company" :style="{width:'200px'}"></Column>
            <Column field="status" header="Status" :style="{width:'200px'}">
                <template #body="{data}">
                    <span :class="'customer-badge status-' + data.status">{{data.status}}</span>
                </template>
            </Column>
            <Column field="activity" header="Activity" :style="{width:'200px'}"></Column>
            <Column field="representative.name" header="Representative" :style="{width:'200px'}">
                <template #body="{data}">
                    <img :alt="data.representative.name" :src="'images/avatar/' + data.representative.image" width="32" style="vertical-align: middle" />
                    <span style="margin-left: .5em; vertical-align: middle" class="image-text">{{data.representative.name}}</span>
                </template>
            </Column>
            <Column field="balance" header="Balance" :style="{width:'150px'}" frozen alignFrozen="right">
                <template #body="{data}">
                    <span class="text-bold">{{formatCurrency(data.balance)}}</span>
                </template>
            </Column>
        </DataTable>
    </div>
</div> -->


<!-- <template>
    <h2>All items page</h2>
    <router-link :to="{ name: 'NewItem' }">New Item</router-link>
    <ul>
        <li v-for="item in items" :key="item.id">
            <router-link :to="{ name: 'SingleItem', params: { id: item.id } }">{{ item.name }}</router-link> - {{ item.description }} - {{ item.id }}
            <form @submit.prevent="deleteItem(item.id)">
                <pvbutton>Delete Item</pvbutton>
            </form>
            <br />
        </li>
    </ul>
</template> -->