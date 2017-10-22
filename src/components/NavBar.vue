<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <router-link to="/" exact><a href="/" class="navbar-brand">
            <span v-if="role">{{role.company.name}}</span>
            SendTank
        </a></router-link>
        <div class="collapse navbar-collapse">
            <ul class="navbar-nav mr-auto" v-if="user">
                <li class="nav-item">
                    <router-link to="/lists/"><a class="nav-link">Lists</a></router-link>
                </li>
                <li class="nav-item">
                    <router-link to="/campaigns/"><a class="nav-link">Campaigns</a></router-link>
                </li>

            </ul>
            <div class="loader mx-auto" v-if="loading">
                <div class='inner'></div>
            </div>
            <form class="form-inline" v-if="user">
                <input class="form-control mr-sm-2" type="text" placeholder="Search..." aria-label="Search">
            </form>
            <ul class="navbar-nav">
                <li class="nav-item" v-if="!user">

                    <router-link to="/login/"><a class="nav-link">Login</a></router-link>
                </li>
                <li class="nav-item dropdown" v-if="user">
                    <button type="button" class="btn dropdown-toggle" data-toggle="dropdown" aria-haspopup="true"
                            aria-expanded="false">
                        User
                    </button>
                    <ul class="dropdown-menu dropdown-menu-right">
                        <li class="dropdown-item">
                            <div>Using as:</div>
                            {{ role.type }} @ {{ role.company.name }}
                        </li>
                        <li class="dropdown-divider"></li>
                        <li class="dropdown-item" v-if="roles.length>1">Use as:</li>
                        <li v-for="(role, index) in roles" class="dropdown-item" v-if="!role.active">

                            <a href="#" @click.prevent="change_role(role.id)">
                                {{ role.type }} @ {{ role.company.name }}
                            </a>
                        </li>
                        <li class="dropdown-divider"></li>
                        <li class="dropdown-item"><a @click.prevent="logout" href="#">Sign Out</a>
                        </li>
                    </ul>
                </li>
            </ul>
        </div>
    </nav>
</template>

<script>
  import {mapState, mapActions} from 'vuex'

  export default {
    props: ['loading'],
    computed: mapState([
      'roles', 'user', 'role'
    ]),
    methods: {
      logout() {
        this.$store.dispatch('logout').then(() => {
          this.$router.push('/login');
          this.$notify.success('Logged out!');
        });
      },
      ...mapActions([
        'change_role',
      ])
    }
  }
</script>

<style>

</style>