import { Navigate, Outlet } from "react-router-dom";
import { useAuthStore } from "../stores/authStore";
import { jwtDecode } from "jwt-decode";

const isValidToken = (token: string | null): boolean => {
  if (!token) return false;

  try {
    const decoded = jwtDecode(token);
    return decoded.exp ? (decoded.exp * 1000) > Date.now() : true;
  } catch {
    return false;
  }
};

export default function ProtectedRoute() {
  const jwt_token = useAuthStore((state) => state.jwt_token);
  const logout = useAuthStore((state) => state.logout);

  const isAuthenticated = isValidToken(jwt_token);

  if (!isAuthenticated) {
    if (jwt_token) logout();

    return <Navigate to="/login" replace />;
  }

  return <Outlet />;
}