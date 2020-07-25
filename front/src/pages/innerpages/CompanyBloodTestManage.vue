<template>
  <main class="signup-page">
    <!--Navbar-->
    <CompanyNavbar />

    <CompanyBreadcrumb title="심화 심사" />
    <section class="contact-area padding-top-140px padding-bottom-120px">
      <div class="container">
        <div class="row">
          <div class="col-lg-7 mx-auto">
            <!-- AccoutSectionTitle Form -->
            <div class="user-form">
              <div class="section-heading text-center">
                <h5 class="section__meta">정보를 입력하세요</h5>
                <h2 class="section__title font-size-30">{{ user.name }}님의 혈액 검사 결과</h2>
              </div>
              <div class="contact-form-action mt-4">
                <form method="post" @submit.prevent="submit">
                  <div class="row">
                    <div class="col-lg-12">
                      <div class="input-box">
                        <div class="form-group">
                          <input
                            class="form-control"
                            type="text"
                            name="text"
                            v-model="bloodTest.bt_chol"
                            placeholder="bt_chol"
                          />
                          <v-icon class="input-icon" name="bt_chol"></v-icon>
                        </div>
                        <!-- end form-group -->
                      </div>
                    </div>
                    <div class="col-lg-12">
                      <div class="input-box">
                        <div class="form-group">
                          <input
                            class="form-control"
                            type="text"
                            name="text"
                            v-model="bloodTest.bt_gluc"
                            placeholder="bt_gluc"
                          />
                          <v-icon class="input-icon" name="bt_gluc"></v-icon>
                        </div>
                        <!-- end form-group -->
                      </div>
                    </div>
                    <div class="col-lg-12">
                      <div class="input-box">
                        <div class="form-group">
                          <input
                            class="form-control"
                            type="text"
                            name="text"
                            v-model="bloodTest.bt_rgpt"
                            placeholder="bt_rgpt"
                          />
                          <v-icon class="input-icon" name="bt_rgpt"></v-icon>
                        </div>
                        <!-- end form-group -->
                      </div>
                    </div>
                    <div class="col-lg-12">
                      <div class="input-box">
                        <div class="form-group">
                          <input
                            class="form-control"
                            type="text"
                            name="text"
                            v-model="bloodTest.bt_sgot"
                            placeholder="bt_sgot"
                          />
                          <v-icon class="input-icon" name="bt_sgot"></v-icon>
                        </div>
                        <!-- end form-group -->
                      </div>
                    </div>
                    <div class="col-lg-12">
                      <div class="input-box">
                        <div class="form-group">
                          <input
                            class="form-control"
                            type="text"
                            name="text"
                            v-model="bloodTest.bt_sgpt"
                            placeholder="bt_sgpt"
                          />
                          <v-icon class="input-icon" name="bt_sgpt"></v-icon>
                        </div>
                        <!-- end form-group -->
                      </div>
                    </div>
                    <div class="col-lg-12">
                      <div class="input-box">
                        <div class="form-group">
                          <div class="custom-checkbox d-block mr-0">
                            <input type="checkbox" id="chb3" />
                            <label for="chb3">
                              I Agree to ForBig's
                              <a href="#" class="color-text">Privacy Policy</a>
                            </label>
                          </div>
                          <!-- end custom-checkbox -->
                        </div>
                      </div>
                    </div>
                    <div class="col-lg-12">
                      <div class="btn-box">
                        <div class="form-group text-center mb-0">
                          <button class="template-btn border-0 w-100" type="submit">혈액검사 결과확인</button>
                        </div>
                        <!-- end form-group -->
                      </div>
                    </div>
                  </div>
                  <!-- end row -->
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="contact-area section--padding">
      <div class="container">
        <div class="col-lg-7 mx-auto">
          <BloodTestResultAccept v-if="judge == 0"></BloodTestResultAccept>
          <BloodTestResultReject v-else-if="judge == 1"></BloodTestResultReject>
        </div>
      </div>
    </section>
    <!--Footer-->
    <Footer />
  </main>
</template>

<script>
import CompanyNavbar from "../../components/common/CompanyNavbar";
import CompanyBreadcrumb from "../../components/common/CompanyBreadcrumb";
import Footer from "../../components/common/footer/Footer";
// import AccountSectionTitle from "../../components/others/account/AccountSectionTitle";
import { bloodTestCustomer } from "../../api/index.js";
import BloodTestResultAccept from "../../components/service/BloodTestResultAccept.vue";
import BloodTestResultReject from "../../components/service/BloodTestResultReject.vue";
export default {
  props: {
    user: {
      type: Object,
      default: () => {
        return {
          name: "고객",
        };
      },
    },
  },
  components: {
    Footer,
    CompanyBreadcrumb,
    CompanyNavbar,
    BloodTestResultAccept,
    BloodTestResultReject,
    // AccountSectionTitle,
  },
  data() {
    return {
      bloodTest: {},
      judge: {},
    };
  },
  mounted() {
    console.log(this.user);
  },
  methods: {
    submit() {
      const params = {
        name: this.user.name,
        gender: this.user.gender,
        age: this.user.age,
        height: this.user.height,
        weight: this.user.weight,
        waist: this.user.waist,
        bp_min: this.user.bp_min,
        bp_max: this.user.bp_max,
        bt_chol: this.bloodTest.bt_chol,
        bt_gluc: this.bloodTest.bt_gluc,
        bt_rgpt: this.bloodTest.bt_rgpt,
        bt_sgot: this.bloodTest.bt_sgot,
        bt_sgpt: this.bloodTest.bt_sgpt,
      };
      console.log(this.user);
      console.log(this.bloodTest);
      bloodTestCustomer(params)
        .then(({ data }) => {
          this.judge = data["judge"][0];
          console.log(data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped></style>
