import type { CreatePrivacyRequestType, CreatePrivacyRequestResponse } from "../../types/Request";

export async function CreatePrivacyRequest(data: CreatePrivacyRequestType, jwt_token: string): Promise<CreatePrivacyRequestResponse> {
  const response = await fetch('http://localhost:8000/api/privacy-requests', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${jwt_token}`
    },
    body: JSON.stringify(data),
  })

  if (!response.ok) {
    throw new Error('Error creating privacy request');
  }

  return response.json();
}