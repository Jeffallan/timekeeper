import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import "./plugins/vuelidate"
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

Vue.config.productionTip = false

Vue.prototype.$http = axios;

Vue.prototype.$http.interceptors.request.use(
  config => {
      const token = store.state.users.token
      if (token) {
          config.headers = Object.assign({
              Authorization: `Token ${token}`
          }, config.headers);
      }
      return config;
  },
  e => {
      return Promise.reject(e);
  }
)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

// https://dev.to/nickitax/persistent-store-with-vuejs-vuex-and-vuex-persisted-state-354n
// https://medium.com/@adamkpurdy_23346/vuex-simple-state-management-e5676371c13a