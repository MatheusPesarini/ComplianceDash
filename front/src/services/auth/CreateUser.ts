import type { RegisterRequest, RegisterResponse } from "../../types/Auth";

export async function CreateUser(data: RegisterRequest): Promise<RegisterResponse> {
  const response = await fetch('http://localhost:8000/register', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })

  if (!response.ok) {
    throw new Error('Erro ao criar usuário');
  }

  return response.json();
}