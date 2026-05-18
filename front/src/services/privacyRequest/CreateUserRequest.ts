import type { CreatePrivacyRequest, CreatePrivacyRequestResponse } from "../../types/Request";

export async function CreatePrivacyRequest(data: CreatePrivacyRequest): Promise<CreatePrivacyRequestResponse> {
  const response = await fetch('http://localhost:8000/api/privacy-requests', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })

  if (!response.ok) {
    throw new Error('Error creating privacy request');
  }

  return response.json();
}