<template>
  <div class="user-form">
    <div class="section-heading">
      <h5 class="section__meta">{{stitle}}</h5>
      <h2 class="section__title font-size-28">{{title}}</h2>
    </div><!-- end section-heading -->
    <div class="contact-form-action mt-4">
      <form class="contact-form" method="POST" name="contactform" action="">
        <div class="input-box">
          <div class="form-group">
            <input class="form-control" type="text" name="name" placeholder="Your Name">
            <v-icon class="input-icon" name="user"></v-icon>
          </div><!-- end form-group -->
        </div>
        <div class="input-box">
          <div class="form-group">
            <input class="form-control" type="email" name="email" placeholder="Email Address">
            <v-icon class="input-icon" name="mail"></v-icon>
          </div><!-- end form-group -->
        </div>
        <div class="input-box">
          <div class="form-group">
            <input class="form-control" type="text" name="subject" placeholder="Subject">
            <v-icon class="input-icon" name="book"></v-icon>
          </div><!-- end form-group -->
        </div>
        <div class="input-box">
          <div class="form-group">
            <textarea class="message-control form-control" name="message" placeholder="Write Message Here"></textarea>
            <v-icon class="input-icon" name="edit"></v-icon>
          </div><!-- end form-group -->
        </div>
        <div class="btn-box">
          <div class="form-group text-center mb-0">
            <button class="template-btn border-0 w-100">Submit message</button>
          </div><!-- end form-group -->
        </div>
      </form>
    </div><!-- end contact-form-action -->
  </div>
</template>

<script>
    export default {
      name: "ContactFields",
      props: ['stitle', 'title']
    }
</script>

<style scoped>

</style>
