import axios from "axios";

const api = axios.create({
    baseURL: 'http://10.41.1.84:8000/api/v1'
});

export default api;