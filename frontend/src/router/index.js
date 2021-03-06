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
    path: "/profile",
    name: "Profile",
    props: true,
    component: () => import("../views/Profile.vue"),
    meta: {requiresAuth: true},
  },
  {
    path: "/profile/edit",
    name: "ProfileEdit",
    props: true,
    component: () => import("@/components/forms/ProfileForm.vue"),
    meta: {requiresAuth: true}
  },
  {
    path: "/users",
    name: "Directory",
    component: () => import("../views/Directory.vue"),
    meta: {requiresAuth: true},
  },
  {
    path: "/user-create",
    name: "UserCreate",
    component: () => import ("@/components/forms/UserForm.vue"),
    meta: {requiresAuth: true}
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
  {
    path: "/username-reset/:uid/:token",
    name: "UsernameReset",
    component: () => import ("../views/UsernameReset.vue")
  },
  {
    path: "/services",
    name: "Services",
    component: () => import("../views/Services.vue"),
    meta: {requiresAuth: true},
  },
  {
    path: "/services-detail/",
    name: "ServiceDetail",
    props: true,
    component: () => import("../views/ServiceDetail.vue"),
    meta: {requiresAuth: true},
  },
  {
    path: "/services-create/",
    name: "ServiceCreate",
    props:  true, //route => ({ ...route.query, ...route.params }),
    component: () => import("@/components/forms/ServiceCreate.vue"),
    meta: {requiresAuth: true},
  },
  {
    path: "/clients",
    name: "Clients",
    component: () => import("../views/Clients.vue"),
    meta: {requiresAuth: true},
  },
  {
    path: "/locations-clients-detail",
    name: "LocationsClientDetail",
    props: true,
    component: () => import("../views/LocationsClientDetail.vue"),
    meta: {requiresAuth: true},
  },
  {
    path: "/locations-clients-create",
    name: "LocationsClientCreate",
    props: true,
    component: () => import("@/components/forms/LocationsClientCreate.vue"),
    meta: {requiresAuth: true},
  },
  {
    path: "/locations",
    name: "Locations",
    component: () => import("../views/Locations.vue"),
    meta: {requiresAuth: true},
  },
  {
    path: "/locations-detail",
    name: "LocationsClientDetail",
    props: true,
    component: () => import("../views/LocationsClientDetail.vue"),
    meta: {requiresAuth: true},
  },
  {
    path: "/locations-create",
    name: "LocationsClientCreate",
    props: true,
    component: () => import("@/components/forms/LocationsClientCreate.vue"),
    meta: {requiresAuth: true},
  },
  {
    path: "/work",
    name: "Work",
    component: () => import("../views/Work.vue"),
    meta: {requiresAuth: true},
  },
  {
    path: "/work-detail",
    name: "WorkDetail",
    component: () => import("../views/WorkDetail.vue"),
    meta: {requiresAuth: true},
  },
  {
    path: "/work-create",
    name: "WorkCreate",
    props: true,
    component: () => import("@/components/forms/WorkForm.vue"),
    meta: {requiresAuth: true},
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
  //mode: "history", //breaks password reset and activation flows
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(page => page.meta.requiresAuth == true)) {
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
