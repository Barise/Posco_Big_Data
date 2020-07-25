<template>
  <div class="user-form">
    <AccountSectionTitle
      stitle="계정 정보 확인"
      title="비밀 번호를 입력해주세요"
    />

    <div class="contact-form-action mt-4">
      <!-- <SignInUpWay /> -->

      <div class="row">
        <div class="col-lg-12">
          <div class="input-box">
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
                placeholder="Password"
              />
              <v-icon class="input-icon" name="lock"></v-icon>
            </div>
            <!-- end form-group -->
          </div>
        </div>
        <div class="col-lg-12">
          <div class="form-group">
            <div
              class="custom-checkbox mr-0 d-flex align-items-center justify-content-between"
            >
              <div>
                <input type="checkbox" id="chb1" />
                <label for="chb1" class="mb-0">Keep me logged in</label>
              </div>
              <div>
                <router-link
                  to="/company"
                  class="text-color-2 font-weight-medium"
                  >Forgot password?</router-link
                >
              </div>
            </div>
          </div>
        </div>
        <div class="col-lg-12">
          <div class="btn-box">
            <div class="form-group text-center mb-0">
              <div class="btn-box">
                <router-link to="/company" class="template-btn">{{
                  buttonText
                }}</router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- </form> -->
    </div>
  </div>
</template>

<script>
import AccountSectionTitle from "../AccountSectionTitle";
export default {
  name: "LoginForm",
  components: {
    AccountSectionTitle,
    // SignInUpWay
  },
  data() {
    return {
      buttonText: "LogIn",
    };
  },
};
</script>

<style scoped>
.v-application a {
  color: white !important;
}
input:focus,
textarea:focus,
button:focus {
  outline: none;
  box-shadow: none;
}
.custom-checkbox input[type="checkbox"]:not(:checked) + label:after,
.custom-checkbox input[type="checkbox"]:checked + label:after {
  content: "x";
  font-weight: 300;
  top: -1px;
  left: 5px;
  font-size: 17px;
}
</style>
