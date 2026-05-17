import { Layout } from "antd";
import Sidebar from "../components/sidebar";
import { Content, Footer, Header } from "antd/es/layout/layout";
import { Outlet } from "react-router-dom";

export default function BaseLayout() {
  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Sidebar />
      <Layout>
        <Header style={{ padding: 0 }} />
        <Content style={{ margin: '0 16px' }}>
          <Outlet />
        </Content>
        <Footer style={{ textAlign: 'center' }}>
          ComplianceDash ©2026 - User Portal
        </Footer>
      </Layout>
    </Layout>
  )
}