import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bulma-vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Axios from 'axios'


Vue.config.productionTip = false

Vue.prototype.$http = Axios;
const token = sessionStorage.getItem('token')
if (token) {
  Vue.prototype.$http.defaults.headers.common['Authorization'] = `Token ${token}`
}

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

// https://dev.to/nickitax/persistent-store-with-vuejs-vuex-and-vuex-persisted-state-354n
// https://medium.com/@adamkpurdy_23346/vuex-simple-state-management-e5676371c13a