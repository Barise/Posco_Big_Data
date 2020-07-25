<template>
  <div class="user-form">
    <h2 class="widget-title font-size-30">Reset Password!</h2>
    <div class="section-description pt-3">
      <p class="section__desc font-size-16">
        Enter the email of your account to reset password.
        Then you will receive a link to email to reset the
        password.If you have any issue about reset password <a href="contact.html" class="text-color-2">contact us</a>
      </p>
    </div>
    <RecoverPasswordForm />
  </div>
</template>

<script>
    import RecoverPasswordForm from "./RecoverPasswordForm";
    export default {
      name: "RecoverPasswordContent",
      components: {RecoverPasswordForm}
    }
</script>

<style scoped>

</style>
