<template>
  <main class="signup-page">
    <!--Navbar-->
    <CustomerNavbar />

    <!--CustomerBreadcrumb-->
    <CustomerBreadcrumb title="보험 상품" />

    <section class="contact-area padding-top-140px padding-bottom-none">
      <div class="container">
        <div class="row">
          <div class="col-lg-7 mx-auto">
            <div class="user-form">
              <AccountSectionTitle stitle="정보를 선택하세요" title="고객님께 적합한 보험을 찾아보세요." />

              <div class="contact-form-action mt-4">
                <form method="post" @submit.prevent="recommend">
                  <!-- <SignInUpWay /> -->
                  <div class="row">
                    <div class="col-lg-2"></div>
                    <div class="col-lg-5 text">보험 상품 가입 목적은</div>
                    <div class="col-lg-3">
                      <div class="input-box">
                        <div class="form-group">
                          <v-select :items="names" label="자녀의 미래" single-line></v-select>
                          <!-- <vue-icon class="input-icon" name="user"></vue-icon> -->
                        </div>
                        <!-- end form-group -->
                      </div>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-lg-1"></div>
                    <div class="text">성별</div>
                    <div class="col-lg-1">
                      <div class="input-box">
                        <div class="form-group">
                          <v-select :items="genders" label="남" single-line></v-select>
                          <!-- <vue-icon class="input-icon" name="user"></vue-icon> -->
                        </div>
                        <!-- end form-group -->
                      </div>
                    </div>
                    <div class="text">, 나이</div>
                    <div class="col-lg-2">
                      <div class="input-box">
                        <div class="form-group">
                          <v-select :items="ages" label="20대미만" single-line></v-select>
                          <!-- <vue-icon class="input-icon" name="mail"></vue-icon> -->
                        </div>
                        <!-- end form-group -->
                      </div>
                    </div>
                    <div class="text">, 결혼여부</div>
                    <div class="col-lg-2">
                      <div class="input-box">
                        <div class="form-group">
                          <v-select :items="isSmokes" label="미혼" single-line></v-select>
                          <!-- <vue-icon class="input-icon" name="mail"></vue-icon> -->
                        </div>
                        <!-- end form-group -->
                      </div>
                    </div>
                    <div class="col-lg-12">
                      <div class="btn-box">
                        <div class="form-group text-center mb-0">
                          <button class="template-btn border-0 w-100">추천 받기</button>
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
    <dvider />

    <!-- How It Work -->
    <section class="hiw-area section--padding text-center">
      <div class="container">
        <div class="row">
          <!-- <SectionTitle stitle="Virus Spread" title="How Coronavirus Spreads" /> -->
        </div>
        <HowItWorkThree v-if="flag ==0" />
      </div>
    </section>

    <!--Footer-->
    <Footer />
  </main>
</template>

<script>
import HowItWorkThree from "../../components/hiw/hiw3/HowItWorkThree";
import CustomerNavbar from "../../components/common/CustomerNavbar";
import CustomerBreadcrumb from "../../components/common/CustomerBreadcrumb";
import Footer from "../../components/common/footer/Footer";
import AccountSectionTitle from "../../components/others/account/AccountSectionTitle";
export default {
  name: "Recommend",
  components: {
    Footer,
    CustomerBreadcrumb,
    CustomerNavbar,
    AccountSectionTitle,
    HowItWorkThree,
  },
  data() {
    return {
      names: ["자녀의 미래", "은퇴", "중대질병", "투자"],
      genders: ["남", "여"],
      ages: ["20대", "30대", "40대", "50대"],
      isSmokes: ["미혼", "기혼"],
      teams: [],
      flag: 1,
    };
  },
  methods: {
    recommend() {
      console.log("--------------------");
      this.flag = 0;
    },
  },
};
</script>

<style scoped>
.text {
  font-size: 1.7em;
  line-height: 60px;
  padding: 5px;
}
</style>
