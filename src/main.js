import Vue from 'vue'
import VueRouter from 'vue-router';
import { Observable } from 'rxjs/Observable';
import { Subscription } from 'rxjs/Subscription'; // Disposable if using RxJS4
import { Subject } from 'rxjs/Subject';
import VueRx from 'vue-rx';
import App from './App.vue'
import VueResource from 'vue-resource';
import moment from 'moment';
import VeeValidate from 'vee-validate';
import { Validator } from 'vee-validate';

Validator.installDateTimeValidators(moment);

Vue.use(VueResource);
Vue.use(VueRouter);
Vue.use(VueRx, {
    Observable,
    Subscription,
    Subject
});
Vue.use(VeeValidate);

import Home from './components/home.vue';
import List from './components/list.vue';


const routes = [
    { path: '/', component: Home },
    { path: '/list', component: List }
];

const router = new VueRouter({
    routes
});

export const eventBus = new Vue({
    methods: {
        UserClass() {
            class User {
                constructor(data = {
                    attributes: {
                        firstName: '',
                        lastName: '',
                        email: '',
                        age: null,
                        birthDate: '',
                        zipcode: null
                    },
                    id: null,
                    type: "users"
                }) {
                    this.data.attributes.firstName = data.attributes.firstName;
                    this.data.attributes.lastName = data.attributes.lastName;
                    this.data.attributes.email = data.attributes.email;
                    this.data.attributes.age = data.attributes.age;
                    this.data.attributes.birthDate = data.attributes.birthDate;
                    this.data.attributes.zipcode = data.attributes.zipcode;
                    this.id = data.id;
                    this.type = data.type;
                }
            }
        }
    },
});

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
