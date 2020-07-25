<template>
  <div class="footer-widget">
    <router-link to="/">
      <img v-bind:src="footerLogo" alt="footer logo" class="footer__logo">
    </router-link>
    <p class="padding-top-30px padding-bottom-20px">
      {{desc}}
    </p>
    <h3 class="widget-title font-size-16 font-weight-medium pb-3 mb-0">Connect with us</h3>
    <ul class="social-links">
      <li><a href="#"><font-awesome-icon :icon="['fab', 'facebook-f']" /></a></li>
      <li><a href="#"><font-awesome-icon :icon="['fab', 'twitter']" /></a></li>
      <li><a href="#"><font-awesome-icon :icon="['fab', 'linkedin-in']" /></a></li>
      <li><a href="#"><font-awesome-icon :icon="['fab', 'instagram']" /></a></li>
    </ul>
  </div>
</template>

<script>
    export default {
      name: "FooterWidget1",
      data() {
        return {
          footerLogo: require('@/assets/images/logo.png'),
          desc: 'Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan. sed do eiusmod tempor incididunt ut labor'
        }
      }
    }
</script>

<style scoped>

</style>
