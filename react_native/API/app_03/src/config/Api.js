import axios from "axios";

const api = axios.create({
    baseURL: 'http://10.42.1.17:8000/api/v1'
});

export default api;