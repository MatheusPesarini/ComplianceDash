import { Navigate } from "react-router-dom";
import { useAuthStore } from "../stores/authStore";

export default function RouteDispatcher() {
  const token = useAuthStore(state => state.jwt_token)
  const isAdmin = useAuthStore(state => state.is_admin)

  if (token) {
    if (isAdmin === true) {
      return <Navigate to="/admin" replace />
    } else {
      return <Navigate to="/user" replace />
    }
  }

  return <Navigate to="/login" replace />;
}