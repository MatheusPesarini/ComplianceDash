export type CreatePrivacyRequest = {
  type: 'access' | 'deletion' | 'correction' | 'portability' | 'opt_out';
  details: string;
}

export type CreatePrivacyRequestResponse = {
  id: number;
  status: 'pending' | 'in_progress' | 'resolved' | 'rejected';
  created_at: string;
}

export type GetUserPrivacyRequestResponse = {
  id: number;
  status: 'pending' | 'in_progress' | 'resolved' | 'rejected';
  admin_notes?: string;
  created_at: string;
  resolved_at?: string;
  user_id: number;
}[];