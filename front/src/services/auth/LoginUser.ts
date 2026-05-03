import type { LoginRequest, LoginResponse } from "../../types/Auth";

export async function LoginUser(data: LoginRequest): Promise<LoginResponse> {
  const response = await fetch('http://localhost:8000/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data),
  })

  if (!response.ok) {
    throw new Error('Erro ao logar');
  }

  return response.json();
} 