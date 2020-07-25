<template>
  <main class="about">
    <!-- Header Menu -->
    <CustomerNavbar />

    <!-- CustomerBreadcrumb -->
    <CustomerBreadcrumb title="> <" />

    <!-- Teams -->
    <section class="team-area section--padding">
      <div class="container">
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
import CustomerTeam from "../../components/teams/CustomerTeam";
import Footer from "../../components/common/footer/Footer";
export default {
  name: "CustomerTeams",
  components: {
    Footer,
    CustomerTeam,
    CustomerBreadcrumb,
    CustomerNavbar
  }
};
</script>

<style scoped>
</style>
