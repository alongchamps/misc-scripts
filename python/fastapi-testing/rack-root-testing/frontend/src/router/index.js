
import { createRouter, createWebHistory } from 'vue-router'

import HomePage from '../views/HomePage.vue'
import AllItems from '../views/AllItems.vue'
import NewItem from '../views/NewItem.vue'
import SingleItem from '../views/SingleItem.vue'
import EditItem from '../views/EditItem.vue'
import FourOhFourView from '../views/404.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'Home',
            component: HomePage
        },
        {
            path: '/items',
            name: 'AllItems',
            component: AllItems
        },
        {
            path: '/items/new',
            name: 'NewItem',
            component: NewItem
        },
        {
            path: '/items/:id(\\d+)',
            name: 'SingleItem',
            component: SingleItem
        },
        {
            path: '/items/:id(\\d+)/edit',
            name: 'EditItem',
            component: EditItem
        },
        {
            path: '/:catchAll(.*)',
            name: 'err404',
            component: FourOhFourView
        }
    ]
  })

export default router
