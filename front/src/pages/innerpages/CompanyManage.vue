<template>
  <main class="signup-page">
    <!--Navbar-->
    <CompanyNavbar />

    <!--CompanyBreadcrumb-->
    <CompanyBreadcrumb title="일반 심사" />

    <section class="contact-area padding-top-140px padding-bottom-120px">
      <div class="container">
        <div class="row">
          <div class="col-lg-7 mx-auto">
            <!-- <SignUpForm /> -->
            <div class="user-form">
              <AccountSectionTitle stitle="정보를 입력하세요" title="일반심사 대상자 가입 승인 판단" />

              <div class="contact-form-action mt-4">
                <form method="post" @submit.prevent="submit">
                  <!-- <SignInUpWay /> -->

                  <div class="row">
                    <div class="col-lg-12">
                      <div class="input-box">
                        <div class="form-group">
                          <input
                            class="form-control"
                            type="text"
                            name="text"
                            v-model="user.name"
                            placeholder="이름"
                          />
                          <vue-icon class="input-icon" name="name"></vue-icon>
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
                            v-model="user.age"
                            placeholder="연령"
                          />
                          <vue-icon class="input-icon" name="age"></vue-icon>
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
                            v-model="user.height"
                            placeholder="키"
                          />
                          <vue-icon class="input-icon" name="height"></vue-icon>
                        </div>
                      </div>
                    </div>
                    <div class="col-lg-12">
                      <div class="input-box">
                        <div class="form-group">
                          <input
                            class="form-control"
                            type="text"
                            name="text"
                            v-model="user.weight"
                            placeholder="몸무게"
                          />
                          <vue-icon class="input-icon" name="weight"></vue-icon>
                        </div>
                      </div>
                    </div>
                    <div class="col-lg-12">
                      <div class="input-box">
                        <div class="form-group">
                          <input
                            class="form-control"
                            type="text"
                            name="text"
                            v-model="user.waist"
                            placeholder="허리둘레"
                          />
                          <vue-icon class="input-icon" name="waist"></vue-icon>
                        </div>
                      </div>
                    </div>
                    <div class="col-lg-12">
                      <div class="input-box">
                        <div class="form-group">
                          <input
                            class="form-control"
                            type="text"
                            name="text"
                            v-model="user.bp_min"
                            placeholder="최저 혈압"
                          />
                          <vue-icon class="input-icon" name="bp_min"></vue-icon>
                        </div>
                      </div>
                    </div>
                    <div class="col-lg-12">
                      <div class="input-box">
                        <div class="form-group">
                          <input
                            class="form-control"
                            type="text"
                            name="text"
                            v-model="user.bp_max"
                            placeholder="최고 혈압"
                          />
                          <vue-icon class="input-icon" name="bp_max"></vue-icon>
                        </div>
                      </div>
                    </div>
                    <div class="col-lg-12">
                      <div class="input-box">
                        <div class="form-group">
                          <v-select :items="user_gender" filled label="성별" v-model="user.gender"></v-select>
                          <vue-icon class="input-icon" name="gender"></vue-icon>
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
                          <button class="template-btn border-0 w-100" type="submit">일반검사 결과확인</button>
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
          <BloodTestAccept v-if="judge == 0"></BloodTestAccept>
          <BloodTestReject v-else-if="judge == 1" :user="user"></BloodTestReject>
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
import AccountSectionTitle from "../../components/others/account/AccountSectionTitle";
import { manageCustomer } from "../../api/index.js";
import BloodTestAccept from "../../components/service/BloodTestAccept.vue";
import BloodTestReject from "../../components/service/BloodTestReject.vue";
export default {
  name: "companymanage",
  components: {
    Footer,
    CompanyBreadcrumb,
    CompanyNavbar,
    AccountSectionTitle,
    BloodTestAccept,
    BloodTestReject,
  },
  data() {
    return {
      judge: {},
      user_gender: ["M", "F"],
      user: {},
      customers: [],
    };
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
      };
      manageCustomer(params)
        .then(({ data }) => {
          this.judge = data["judge"][0];
          console.log(this.judge);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped></style>
