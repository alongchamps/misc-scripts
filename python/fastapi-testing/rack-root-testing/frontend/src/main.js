import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index.js'

import PrimeVue from 'primevue/config'
import Aura from '@primevue/themes/aura'
import MenuBar from 'primevue/menubar'
import pvinput from 'primevue/inputtext'
import pvbutton from 'primevue/button'

const app = createApp(App)

app.use(PrimeVue, {
    theme: {
        preset: Aura
    }
});

app.component('Menubar', MenuBar)
app.component('pvinput', pvinput)
app.component('pvbutton', pvbutton)

app.use(router)

app.mount('#app')
