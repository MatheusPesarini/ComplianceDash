import { Outlet } from "react-router-dom";

const layoutStyle = {
  minHeight: '100vh',
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
}

export default function AuthLayout() {
  return (
    <div style={layoutStyle}>
      <Outlet />
    </div>
  )
}