import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import store from "@/store/index"

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
    meta: { requiresAuth: true },
  },
  {
    path: "/viewer",
    name: "Viewer",
    component: () => import("../views/Viewer.vue"),
    meta: { requiresAuth: true },
  },
  {
  path: "/password-reset",
  name: "PasswordResetRequest",
  component: () => import ('../views/PasswordResetRequest.vue')
  },
  {
    path: "/password-reset-confirm/:uid/:token",
    name: "PasswordResetConfirm",
    component: () => import ('../views/PasswordResetConfirm.vue')
  },
  {
  path: "/user-activate/:uid/:token",
  name: "UserActivate",
  component: () => import ('../views/UserActivate.vue')
  },

  //404 ERRORS
  // https://stackoverflow.com/questions/45619407/how-to-create-a-404-component-in-vuejs-using-vue-router
  {
    path: '/404', component: () => import ('../views/error/NotFound.vue')
  },
  {
    path: '*', redirect: '/404' 
  },

]

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(page => page.meta.requiresAuth)) {
    if (store.state.users.status == "success") {
      next()
    }
    else {
      next({
        name: "Home"
      })
    }
  }
  else {
    next()
  }
})

export default router
