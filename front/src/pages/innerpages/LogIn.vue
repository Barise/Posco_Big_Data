<template>
  <main class="login-page">
    <!--Navbar-->
    <CustomerNavbar />

    <!--CustomerBreadcrumb-->
    <CustomerBreadcrumb title="Login" />

    <!--Login Form-->
    <section class="contact-area padding-top-140px padding-bottom-120px">
      <div class="container">
        <div class="row">
          <div class="col-lg-7 mx-auto">
            <LoginForm />
          </div>
        </div>
      </div>
    </section>

    <!--Footer-->
    <Footer />
  </main>
</template>

<script>
import CustomerNavbar from "../../components/common/CustomerNavbar";
import CustomerBreadcrumb from "../../components/common/CustomerBreadcrumb";
import LoginForm from "../../components/others/account/login/LoginForm";
import Footer from "../../components/common/footer/Footer";
export default {
  name: "LogIn",
  components: { Footer, LoginForm, CustomerBreadcrumb, CustomerNavbar }
};
</script>

<style scoped>
</style>
