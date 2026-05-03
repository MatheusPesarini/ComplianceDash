export type RegisterRequest = {
  name: string;
  email: string;
  password: string
  phone: string;
}

export type RegisterResponse = {
  successful: boolean;
  error_message?: string;
}

export type LoginRequest = {
  email: string;
  password: string;
}

export type LoginResponse = {
  successful: boolean;
  error_message?: string
  user_id: number;
  access_token: string;
}