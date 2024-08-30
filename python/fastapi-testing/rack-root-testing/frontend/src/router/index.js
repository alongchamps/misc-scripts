
import { createRouter, createWebHistory } from 'vue-router'

import AllItems from '../views/AllItems.vue'
import SingleItem from '../views/SingleItem.vue'
import FourOhFourView from '../views/404.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'Home',
            component: AllItems
        },
        {
            path: '/items',
            name: 'SingleItem',
            component: SingleItem
        },
        {
            path: '/:catchAll(.*)',
            name: 'err404',
            component: FourOhFourView
        }
    ]
  })

export default router
