<template>
  <div class="row">
    <div class="col-lg-7">
      <ContactFields stitle="Get In Touch" title="Contact with us! for help" />
    </div>
    <div class="col-lg-5">
      <div class="contact-content pl-4">
        <ContactPlace />
        <Divider />
        <ContactHours />
        <Divider />
        <ContactSocialProfile />
      </div>
    </div>
  </div>
</template>

<script>
    import ContactFields from "../forms/ContactFields";
    import ContactPlace from "./ContactPlace";
    import Divider from "../../common/Divider";
    import ContactHours from "./ContactHours";
    import ContactSocialProfile from "./ContactSocialProfile";
    export default {
        name: "ContactWrap",
      components: {ContactSocialProfile, ContactHours, Divider, ContactPlace, ContactFields}
    }
</script>

<style scoped>

</style>
