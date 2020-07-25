<template>
  <main class="about">
    <!-- Header Menu -->
    <CustomerNavbar />

    <!-- CustomerBreadcrumb -->
    <CustomerBreadcrumb title="Teams" />

    <!-- Teams -->
    <section class="team-area section--padding">
      <div class="container">
        <div class="row text-center">
          <SectionTitle stitle="Our Teams" title="Meet Our Teams" />
        </div>
        <CustomerTeam />
      </div>
    </section>

    <!-- Footer -->
    <Footer />
  </main>
</template>

<script>
import CustomerNavbar from "../../components/common/CustomerNavbar";
import CustomerBreadcrumb from "../../components/common/CustomerBreadcrumb";
import SectionTitle from "../../components/common/SectionTitle";
import CustomerTeam from "../../components/teams/CustomerTeam";
import Footer from "../../components/common/footer/Footer";
export default {
  name: "About",
  components: {
    Footer,
    CustomerTeam,
    SectionTitle,
    CustomerBreadcrumb,
    CustomerNavbar,
  },
};
</script>

<style scoped>
.about5 {
  z-index: 7;
}
</style>
