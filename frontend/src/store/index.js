import Vue from 'vue'
import Vuex from 'vuex'
import users from "./modules/users"
import createPersistedState from "vuex-persistedstate"
import SecureLS from "secure-ls"


const ls = new SecureLS({ 
                          encodingType: 'aes',
                        })

Vue.use(Vuex)

 const store = new Vuex.Store({
  modules: {
    users,
  },
plugins: [createPersistedState({
    storage: { storage: window.sessionStorage,
               getItem: (key) => ls.get(key),
               setItem: (key, value) => ls.set(key, value),
               removeItem: (key) => ls.remove(key),
    }
  })
],
});
export default store