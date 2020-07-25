<template>
  <main class="contact">
    <!-- Navbar -->
    <CustomerNavbar />

    <!-- CustomerBreadcrumb -->
    <CustomerBreadcrumb title="Contact Us" />

    <!-- Contact -->
    <section class="contact-area padding-top-140px padding-bottom-120px">
      <div class="container">
        <ContactWrap />
      </div>
    </section>

    <!-- Map -->
    <GoogleMap />

    <!-- Footer -->
    <Footer />
  </main>
</template>

<script>
import CustomerNavbar from "../../components/common/CustomerNavbar";
import CustomerBreadcrumb from "../../components/common/CustomerBreadcrumb";
import ContactWrap from "../../components/contact/contact/ContactWrap";
import Footer from "../../components/common/footer/Footer";
import GoogleMap from "../../components/contact/maps/GoogleMap";
export default {
  name: "Contact",
  components: {
    GoogleMap,
    Footer,
    ContactWrap,
    CustomerBreadcrumb,
    CustomerNavbar
  }
};
</script>

<style scoped>
</style>
