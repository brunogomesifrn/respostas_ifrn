// Importar a dependência Axios para conectar com a API
import axios from "axios";

// Criar a instância de conexão HTTP
const api = axios.create({
    baseURL: 'http://10.42.1.17:8000/api/v1'
});

// Exporta a instância configurada do Axios
export default api;