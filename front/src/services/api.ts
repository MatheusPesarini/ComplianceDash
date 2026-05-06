import axios from 'axios';
import { useAuthStore } from '../stores/authStore';

// Criamos uma instância do axios já apontando pro seu FastAPI
export const api = axios.create({
  baseURL: 'http://localhost:8000',
});

// INTERCEPTOR DE REQUEST: Roda ANTES de enviar pro backend
// Onde injetamos o JWT no Cabeçalho (Header) para você não ter que fazer na mão toda vez
api.interceptors.request.use((config) => {
  // Pega o token direto da memória do zustand
  const token = useAuthStore.getState().jwt_token;
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// INTERCEPTOR DE RESPONSE: Roda quando o backend te responde algo
// Aqui capturamos o erro 401 GLOBALMENTE, independente de qual tela ou requisição errou
api.interceptors.response.use(
  (response) => response,
  (error) => {
    // Se a API responder 401 (Não autorizado), forçamos o deslog
    if (error.response && error.response.status === 401) {
      useAuthStore.getState().logout();
      window.location.href = '/login'; // Chuta pra tela de login
    }
    return Promise.reject(error);
  }
);
