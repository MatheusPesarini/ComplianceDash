import { useNavigate } from "react-router-dom";
import { useAuthStore } from "../stores/authStore";
import { Menu, Layout, Button } from "antd";
import { CheckSquareOutlined, DoubleRightOutlined, HomeOutlined, LogoutOutlined, MenuFoldOutlined, MenuUnfoldOutlined } from "@ant-design/icons";
import { useState } from "react";

const { Sider } = Layout;

export default function Sidebar() {
  const [collapsed, setCollapsed] = useState(false);
  const navigate = useNavigate();
  const logout = useAuthStore((state) => state.logout);

  return (
    <Sider trigger={null} collapsible collapsed={collapsed}>
      <div style={{ height: 64, display: 'flex', justifyContent: 'center', alignItems: 'center', fontSize: 24, color: 'white', gap: 8 }}>
        <DoubleRightOutlined />
        <DoubleRightOutlined />
      </div>
      <Menu
        theme="dark"
        mode="inline"
        style={{ background: 'transparent' }}
        items={[
          {
            key: '1',
            icon: <HomeOutlined />,
            label: 'Dashboard',
            onClick: () => navigate('/')
          },
          {
            key: '2',
            icon: <CheckSquareOutlined />,
            label: 'Tarefas',
            onClick: () => navigate('/tarefas')
          },
          {
            key: '3',
            icon: <LogoutOutlined />,
            label: 'Sair',
            onClick: () => logout(),
            style: { marginTop: 'auto' }
          },
        ]}
      />
      <Button
        type="text"
        icon={collapsed ? <MenuUnfoldOutlined /> : <MenuFoldOutlined />}
        onClick={() => setCollapsed(!collapsed)}
        style={{
          fontSize: '20px',
          width: 64,
          height: 64,
          position: 'absolute',
          bottom: '16px',
          left: '50%',
          transform: 'translateX(-50%)',
        }}
      />
    </Sider>
  )
}