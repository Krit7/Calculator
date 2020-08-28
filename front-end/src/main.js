import Vue from 'vue'
import App from './App.vue'
// import { BootstrapVue } from 'bootstrap-vue'
import AxiosPlugin from 'vue-axios-cors';
import JsonCSV from 'vue-json-csv'
 
Vue.component('downloadCsv', JsonCSV)
//VUE BOOTSTRAP CONFIG
// Vue.use(BootstrapVue)

//VUE AXIOS CONFIG
Vue.use(AxiosPlugin)

//MAIN VUE LOADER
new Vue({
  render: h => h(App),
}).$mount('#app')
