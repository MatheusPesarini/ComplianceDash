import { Layout } from "antd";
import Sidebar from "../components/sidebar";
import { Content, Footer, Header } from "antd/es/layout/layout";
import { Outlet } from "react-router-dom";

export default function BaseLayout() {
  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Sidebar />
      <Layout>
        <Header style={{ padding: 0, background: '#fff' }} />
        <Content style={{ margin: '0 16px', display: 'flex', flexDirection: 'column' }}>
          <Outlet />
        </Content>
        <Footer style={{ textAlign: 'center' }}>
          ComplianceDash ©2026 - Data Subject Portal
        </Footer>
      </Layout>
    </Layout>
  )
}