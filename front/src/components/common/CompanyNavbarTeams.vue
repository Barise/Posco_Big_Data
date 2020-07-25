<template>
  <section
    class="header-menu-area header-menu-area-3"
    :class="{ active: navFixed }"
  >
    <div class="header-menu-fluid header-menu-fluid-3">
      <div class="container-fluid">
        <div class="main-menu-content main-menu-content-3">
          <div class="row align-items-center h-100">
            <div class="col-lg-3">
              <div class="logo-box">
                <router-link to="/company" class="logo">
                  <img src="../../assets/images/teams_image.jpg" alt="logo" />
                </router-link>
              </div>
            </div>
            <div class="col-lg-9">
              <div class="menu-wrapper">
                <nav class="main-menu">
                  <ul>
                    <li>
                      <router-link to="/company">Home</router-link>
                    </li>
                    <li>
                      <router-link to="/company/manage">일반 심사</router-link>
                    </li>
                    <li>
                      <router-link to="/company/bloodtest"
                        >심화 심사</router-link
                      >
                    </li>
                    <li>
                      <router-link to="/company/about">teams</router-link>
                    </li>
                  </ul>
                </nav>
                <div class="logo-right-button">
                  <ul>
                    <li>
                      <Button url="/customer" title="고객 페이지" />
                    </li>
                  </ul>
                  <div class="side-menu-open" v-on:click="showMenu">
                    <i class="la la-bars"></i>
                    <v-icon class="show-menu" name="menu"></v-icon>
                  </div>
                </div>

                <div
                  v-bind:class="{ active: ismenuVisible }"
                  class="side-nav-container"
                >
                  <div class="humburger-menu">
                    <div
                      class="humburger-menu-lines side-menu-close"
                      v-on:click="showMenu"
                    ></div>
                  </div>
                  <div class="side-menu-wrap">
                    <ul class="side-menu-ul">
                      <li class="sidenav__item">
                        <router-link to="/company">home</router-link>
                      </li>
                      <li class="sidenav__item">
                        <router-link to="/company/manage"
                          >일반 심사</router-link
                        >
                      </li>
                      <li class="sidenav__item">
                        <router-link to="/company/bloodtest"
                          >심화 심사</router-link
                        >
                      </li>
                      <li class="sidenav__item">
                        <router-link to="/company/about">about</router-link>
                      </li>
                      <li class="sidenav__item">
                        <router-link to="/company/teams"
                          >company teams</router-link
                        >
                      </li>
                      <li class="sidenav__item">
                        <router-link to="/contact">contact</router-link>
                      </li>
                    </ul>
                    <div class="side-btn-box">
                      <router-link to="/customer">고객 페이지</router-link>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import Button from "./Button";

export default {
  name: "CompanyNavbar",
  components: {
    Button,
  },
  data() {
    return {
      ismenuVisible: false,
      navFixed: false,
    };
  },
  methods: {
    showMenu: function() {
      this.ismenuVisible = !this.ismenuVisible;
    },
    showHiddenMenu: function(event) {
      event.target.classList.toggle("is-open");
    },
  },
  mounted() {
    window.document.onscroll = () => {
      if (window.scrollY > 25) {
        this.navFixed = true;
      } else {
        this.navFixed = false;
      }
    };
  },
};
</script>

<style scoped></style>
