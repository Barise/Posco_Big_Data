import CustomerHome from "./pages/CustomerHome";
import CustomerAbout from "./pages/innerpages/CustomerAbout";
import CustomerTeams from "./pages/innerpages/CustomerTeams";
import CustomerContact from "./pages/innerpages/CustomerContact";
import CustomerFAQ from "./pages/innerpages/CustomerFAQ";
import LogIn from "./pages/innerpages/LogIn";
import CustomerRecommend from "./pages/innerpages/CustomerRecommend";

import CompanyHome from "./pages/CompanyHome";
import CompanyManage from "./pages/innerpages/CompanyManage";
import CompanyAbout from "./pages/innerpages/CompanyAbout";
import CompanyTeams from "./pages/innerpages/CompanyTeams";
import CompanyContact from "./pages/innerpages/CompanyContact";
import CompanyFAQ from "./pages/innerpages/CompanyFAQ";
import CompanyBloodTestManage from "./pages/innerpages/CompanyBloodTestManage";
export default [
    { path: "/", redirect: "/customer" },
    { path: "/customer", component: CustomerHome },
    { path: "/customer/about", component: CustomerAbout },
    { path: "/customer/teams", component: CustomerTeams },
    { path: "/customer/contact", component: CustomerContact },
    { path: "/customer/faq", component: CustomerFAQ },
    { path: "/customer/recommend", component: CustomerRecommend },
    { path: "/login", component: LogIn },
    // 고객용 테이블
    { path: "/company", component: CompanyHome },
    { path: "/company/about", component: CompanyAbout },
    { path: "/company/teams", component: CompanyTeams },
    { path: "/company/contact", component: CompanyContact },
    { path: "/company/faq", component: CompanyFAQ },
    { path: "/company/manage", component: CompanyManage },
    { path: "/company/bloodtest", name: 'bloodtest', component: CompanyBloodTestManage, props: true },
];