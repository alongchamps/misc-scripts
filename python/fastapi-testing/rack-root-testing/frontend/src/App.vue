<script>
    export default {
        data() {
            return {
                items: [
                    {
                        label: "Home",
                        route: "Home",
                    },
                    {
                        label: "All Items",
                        route: "AllItems"
                    }
                ]
            };
        }
    };
</script>
<!-- 
<template>
    <Menubar>
        <template>
            <router-link :to="{ name: 'Home' }">Home</router-link>
            <router-link :to="{ name: 'AllItems' }">Items</router-link>
        </template>
    </Menubar>
</template> -->

<template>
    <Menubar :model="items">
        <template #item="{ item, props, hasSubmenu }">
            <router-link v-if="item.route" v-slot="{ href, navigate }" :to="{ name: item.route }" custom>
                <a :href="href" v-bind="props.action" @click="navigate">
                    <!-- <span :class="item.icon" /> -->
                    <span class="ml-2">{{ item.label }}</span>
                </a>
            </router-link>
            <a v-else :href="item.targetRoute" :target="item.targetRoute" v-bind="props.action">
                <span :class="item.icon" />
                <span class="ml-2">{{ item.label }}</span>
                <span v-if="hasSubmenu" class="pi pi-fw pi-angle-down ml-2" />
            </a>
        </template>
    </Menubar>
    <br />
    <router-view />
</template>

<!-- <template>
    <Menubar :model="items">
        <template #start></template>
        <template #item="{ item, props }">
            <router-link v-if="item.route" v-slot="{href, navigate}" :to="{ name: item.targetRoute }" custom>
                <a :href="href" v-bind="props.action" @click="navigate">
                    <span class="ml-2">{{ item.label }}</span>
                </a>
            </router-link>
        </template>
        <template #end></template>
        <router-view />
    </Menubar>
</template> -->

<!-- 
<template>
    <div>
        <router-link :to="{ name: 'Home' }">Home</router-link>
        <router-link :to="{ name: 'AllItems' }">Items</router-link>
    </div>
    <br />
    <router-view />
</template> -->

<!-- 
<style>
    .router-link-exact-active {
        color: white
    }
</style> -->

<!-- 
<Menubar :model="items">
    <template #item="{ item, props, hasSubmenu }">
        <router-link v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
            <a v-ripple :href="href" v-bind="props.action" @click="navigate">
                <span :class="item.icon" />
                <span class="ml-2">{{ item.label }}</span>
            </a>
        </router-link>
        <a v-else v-ripple :href="item.url" :target="item.target" v-bind="props.action">
            <span :class="item.icon" />
            <span class="ml-2">{{ item.label }}</span>
            <span v-if="hasSubmenu" class="pi pi-fw pi-angle-down ml-2" />
        </a>
    </template>
</Menubar> -->
