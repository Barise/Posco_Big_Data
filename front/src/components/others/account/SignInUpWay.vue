<template>
<div class="row">
  <div class="col-lg-4">
    <div class="form-group">
      <button class="template-btn btn-bg-1 border-0 w-100" type="submit">
        <font-awesome-icon class="mr-2" :icon="['fab', 'google']" /> Google
      </button>
    </div>
  </div>

  <div class="col-lg-4">
    <div class="form-group">
      <button class="template-btn btn-bg-2 border-0 w-100" type="submit">
        <font-awesome-icon class="mr-2" :icon="['fab', 'facebook-f']" /> Facebook
      </button>
    </div>
  </div>

  <div class="col-lg-4">
    <div class="form-group">
      <button class="template-btn btn-bg-3 border-0 w-100" type="submit">
        <font-awesome-icon class="mr-2" :icon="['fab', 'twitter']" /> Twitter
      </button>
    </div>
  </div>

  <div class="col-lg-12">
    <div class="account-assist mt-4 mb-4 text-center">
      <p class="account__desc">or</p>
    </div>
  </div>
</div>
</template>

<script>
    export default {
        name: "SignInUpWay"
    }
</script>

<style scoped>

</style>
