<template>
  <main class="about">
    <!-- Header Menu -->
    <CompanyNavbar />

    <!-- Breadcrumb -->
    <CompanyBreadcrumb title="Teams" />

    <!-- Teams -->
    <section class="team-area section--padding">
      <div class="container">
        <div class="row text-center">
          <SectionTitle stitle="Our Teams" title="Meet Our Teams" />
        </div>
        <CompanyTeams />
      </div>
    </section>

    <!-- Footer -->
    <Footer />
  </main>
</template>

<script>
import CompanyNavbar from "../../components/common/CompanyNavbar";
import CompanyBreadcrumb from "../../components/common/CompanyBreadcrumb";
import SectionTitle from "../../components/common/SectionTitle";
import CompanyTeams from "../../components/teams/CompanyTeam";
import Footer from "../../components/common/footer/Footer";
export default {
  name: "About",
  components: {
    Footer,
    CompanyTeams,
    SectionTitle,
    CompanyBreadcrumb,
    CompanyNavbar,
  },
};
</script>

<style scoped>
.about5 {
  z-index: 7;
}
</style>
