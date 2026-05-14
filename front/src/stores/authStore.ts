import { create } from "zustand";
import { persist } from "zustand/middleware";

type AuthState = {
  user_id: number | null;
  is_admin: boolean | null;
  jwt_token: string | null;
  setAuth: (jwt_token: string, user_id: number, is_admin: boolean) => void;
  logout: () => void;
};

export const useAuthStore = create<AuthState>()(
  persist((set) => ({
    jwt_token: null,
    is_admin: null,
    user_id: null,

    setAuth: (jwt_token: string, user_id: number, is_admin: boolean) => set({ jwt_token, user_id, is_admin }),

    logout: () => set({ jwt_token: null, user_id: null, is_admin: null }),
  }), {
    name: "auth-storage",
  })
)