import { useNavigate } from "react-router-dom";
import { useAuthStore } from "../stores/authStore";
import { Menu, Layout } from "antd";
import { CheckSquareOutlined, HomeOutlined, LogoutOutlined } from "@ant-design/icons";

const { Sider } = Layout;

export default function Sidebar() {
  const navigate = useNavigate();
  const logout = useAuthStore((state) => state.logout);

  return (
    <Sider width={250} theme="dark" style={{ background: '#192734' }}>
      <div style={{ padding: '20px', color: '#E0E0E0', textAlign: 'center', fontSize: '20px', fontWeight: 'bold' }}>
        Sidebar
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
    </Sider>
  )
}