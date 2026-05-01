import { Layout } from "antd";
import { Outlet } from "react-router-dom";

export default function AuthLayout() {
  return (
    <Layout>
      <Outlet />
    </Layout>
  )
}