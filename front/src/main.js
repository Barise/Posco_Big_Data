import Vue from 'vue'
import BootstrapVue from "bootstrap-vue/dist/bootstrap-vue.esm";
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
// Bootstrap
Vue.use(BootstrapVue);
import VueRouter from 'vue-router'
import Routes from './routes'
import * as VueGoogleMaps from 'vue2-google-maps'
import feather from 'vue-icon'

import { library } from '@fortawesome/fontawesome-svg-core'
import { faReply } from '@fortawesome/free-solid-svg-icons'
import { faFacebookF, faGoogle, faTwitter, faInstagram, faDribbble, faBehance, faLinkedinIn } from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
library.add(faFacebookF, faGoogle, faTwitter, faInstagram, faDribbble, faBehance, faLinkedinIn, faReply);

Vue.component('font-awesome-icon', FontAwesomeIcon);
Vue.config.productionTip = false;

Vue.use(feather, 'vue-icon');

/* Main CSS*/
import "./assets/css/style.css";

import vuetify from './plugins/vuetify';

// google map
Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyAYzby4yYDVaXPmtu4jZAGR258K6IYwjIY',
  },
});

// Router
Vue.use(VueRouter);
const router = new VueRouter({
  routes: Routes,
  mode: 'history',
  scrollBehavior () {
    return { x: 0, y: 0 }
  }
});

new Vue({
  el: '#app',
  render: h => h(App),
  vuetify,
  router: router
});
