<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <a class="navbar-brand" href="/">SendTank</a>
        <div class="collapse navbar-collapse">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item">
                    <router-link to="/" exact>
                        <a class="nav-link">Home</a>
                    </router-link>
                </li>
                <li class="nav-item">
                    <router-link to="/lists/">
                        <a class="nav-link">Lists</a>
                    </router-link>
                </li>
                <li class="nav-item">
                    <router-link to="/campaigns/">
                        <a class="nav-link">Campaigns</a>
                    </router-link>
                </li>
                <li><span v-if="loading">Loading...</span></li>
            </ul>
            <form class="form-inline">
                <input class="form-control mr-sm-2" type="text" placeholder="Search..." aria-label="Search">
            </form>
            <ul class="navbar-nav">
                <li class="nav-item active"><a class="nav-link" href="{% url 'account_logout' %}">Sign Out</a></li>
                <li class="nav-item dropdown">
                    <button type="button" class="btn dropdown-toggle" data-toggle="dropdown" aria-haspopup="true"
                            aria-expanded="false">
                        User
                    </button>
                    <ul class="dropdown-menu dropdown-menu-right">
                        <li class="dropdown-item"><a href="{% url 'account_change_password' %}">Change Password</a></li>
                        <li class="dropdown-item"><a href="{% url 'socialaccount_connections' %}">Social Accounts</a></li>
                        <li class="dropdown-item"><a href="{% url 'account_logout' %}">Sign Out</a></li>
                    </ul>
                </li>
            </ul>
        </div>
    </nav>
</template>

<script>
    export default{
      props: ['loading']
    }
</script>