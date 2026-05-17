import { Navigate, Outlet } from "react-router-dom";
import { useAuthStore } from "../stores/authStore";

export default function RequireUser() {
  const isAdmin = useAuthStore(state => state.is_admin);

  if (isAdmin) {
    return <Navigate to='/admin' replace />
  }

  return <Outlet />
}