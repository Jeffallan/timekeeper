import { createStore } from 'vuex'
import users from './modules/users'

export default function (/* { ssrContext } */) {
  const Store = createStore({
    modules: {
      users
    },

    // enable strict mode (adds overhead!)
    // for dev mode and --debug builds only
    strict: process.env.DEBUGGING
  })

  return Store
}