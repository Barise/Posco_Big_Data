<template>
  <div class="contact-form-action">
    <form method="post">
      <div class="input-box">
        <div class="form-group">
          <input class="form-control" type="email" name="email" placeholder="Enter email address">
          <v-icon class="input-icon" name="mail"></v-icon>
        </div><!-- end form-group -->
      </div>
      <div class="input-box">
        <div class="form-group">
          <button class="template-btn border-0" type="submit">reset password</button>
        </div><!-- end form-group -->
      </div>
      <div class="account-action d-flex align-items-center justify-content-between">
        <p class="font-size-16"><router-link to="/login">login</router-link></p>
        <p class="font-size-16">Not a member?
          <router-link to="/sign-up">Register</router-link>
        </p>
      </div><!-- end account-action -->
    </form>
  </div>
</template>

<script>
    export default {
        name: "RecoverPasswordForm"
    }
</script>

<style scoped>

</style>
