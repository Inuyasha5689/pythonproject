/**
 * Created by dasco on 3/28/2017.
 */

import Home from './components/home.vue';
import Content from './components/content.vue';
import UserDisplay from './components/userDisplay.vue';
import List from './components/list.vue';


export const routes = [
    { path: '/', component: Home},
    { path: '/userDisplay', component: UserDisplay},
    { path: '/list', component: List}

];