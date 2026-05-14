import { Navigate } from "react-router-dom";
import { useAuthStore } from "../stores/authStore";

export default function RouteDispatcher() {
  const isAdmin = useAuthStore(state => state.is_admin)

  if (isAdmin) {
    if (isAdmin) {
      return <Navigate to="/admin" replace />
    } else {
      return <Navigate to="/user" replace />
    }
  }

  return <Navigate to="/login" replace />;
}