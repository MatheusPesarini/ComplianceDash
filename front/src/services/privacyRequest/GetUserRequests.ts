import type { GetUserPrivacyRequestResponse } from "../../types/Request";

export async function GetUserRequests(token: string): Promise<GetUserPrivacyRequestResponse> {

  const response = await fetch('http://localhost:8000/api/privacy-requests/me', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${`jwt_token ${token}`}`
    },
  })

  if (!response.ok) {
    throw new Error('Error fetching user requests');
  }

  return response.json();
}