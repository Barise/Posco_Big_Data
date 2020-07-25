<template>
  <main class="about">
    <!-- Header Menu -->
    <CompanyNavbarTeams />

    <!-- CompanyBreadcrumb -->
    <CompanyBreadcrumb title="> <" />

    <!-- Teams -->
    <section class="team-area section--padding">
      <div class="container">
        <CompanyTeam />
      </div>
    </section>

    <!-- Footer -->
    <Footer />
  </main>
</template>

<script>
import CompanyNavbarTeams from "../../components/common/CompanyNavbarTeams";
import CompanyBreadcrumb from "../../components/common/CompanyBreadcrumb";
import CompanyTeam from "../../components/teams/CompanyTeam";
import Footer from "../../components/common/footer/Footer";
export default {
  name: "CompanyTeams",
  components: {
    Footer,
    CompanyTeam,
    CompanyBreadcrumb,
    CompanyNavbarTeams,
  },
};
</script>

<style scoped></style>
