import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'

import Home from '../views/Home.vue'

// import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import Posts from '../views/Posts.vue'
import Post from '../views/Post.vue'
import AddPost from '../views/AddPost.vue'
import EditPost from '../views/EditPost.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  // {
  //   path: '/sign-up',
  //   name: 'SignUp',
  //   component: SignUp
  // },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/posts',
    name: 'Posts',
    component: Posts,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/posts/:id',
    name: 'Post',
    component: Post,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/posts/add',
    name: 'AddPost',
    component: AddPost,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/posts/:id/edit',
    name: 'EditPost',
    component: EditPost,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path } })
  } else {
    next()
  }
})

export default router
