import { create } from "zustand";
import { persist } from "zustand/middleware";

type AuthState = {
  user_id: number | null;
  jwt_token: string | null;
  setAuth: (jwt_token: string, user_id: number) => void;
  logout: () => void;
};

export const useAuthStore = create<AuthState>()(
  persist((set) => ({
    jwt_token: null,
    user_id: null,

    setAuth: (jwt_token: string, user_id: number) => set({ jwt_token, user_id }),

    logout: () => set({ jwt_token: null, user_id: null }),
  }), {
    name: "auth-storage",
  })
)