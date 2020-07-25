import axios from "axios";

// 1. HTTP Request & Response와 관련된 기본 설정
const config = {
    baseUrl: "http://127.0.0.1:8080/",
};

// 2. API 함수들을 정리
function recommendInsurance(params) {
    // return axios.get(config.baseUrl + '/news/1.json');
    return axios.post(`${config.baseUrl}customer/recommend`, { params });
}

function manageCustomer(params) {
    // return axios.get(config.baseUrl + '/news/1.json');
    return axios.post(`${config.baseUrl}company/manage`, { params });
}

function bloodTestCustomer(params) {
    // return axios.get(config.baseUrl + '/news/1.json');
    return axios.post(`${config.baseUrl}company/bloodtest`, { params });
}

function fetchAskList() {
    return axios.get(`${config.baseUrl}ask/1.json`);
}

function fetchJobsList() {
    return axios.get(`${config.baseUrl}jobs/1.json`);
}

function fetchUserInfo(username) {
    return axios.get(`${config.baseUrl}user/${username}.json`);
}

function fetchCommentItem(id) {
    return axios.get(`${config.baseUrl}item/${id}.json`);
}

export {
    manageCustomer,
    recommendInsurance,
    bloodTestCustomer,
    fetchAskList,
    fetchJobsList,
    fetchUserInfo,
    fetchCommentItem,
};