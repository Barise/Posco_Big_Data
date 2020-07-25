<template>
  <div class="subscriber-form">
    <div class="contact-form-action">
      <form method="post">
        <div class="form-group">
          <input class="form-control" type="email" name="email"
                 placeholder="Enter email address">
          <v-icon class="input-icon" name="mail"></v-icon>
        </div>
        <div class="btn-box">
          <button class="template-btn border-0 w-100" type="submit">Subscribe now</button>
        </div>
      </form>
    </div><!-- end contact-form-action -->
  </div>
</template>

<script>
    export default {
        name: "MailChimp"
    }
</script>

<style scoped>
  input:focus,
  textarea:focus,
  button:focus {
    box-shadow: none;
  }
</style>
