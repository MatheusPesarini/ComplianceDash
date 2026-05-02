import { Outlet } from "react-router-dom"
import { ConfigProvider } from "antd"
import ptBR from "antd/locale/pt_BR"

export default function App() {
  return (
    <ConfigProvider locale={ptBR} theme={{
      token: {
        colorPrimary: '#1677ff',
        colorBgContainer: '#192734',
        colorText: '#E0E0E0',
        colorSplit: '#e0e0e0',
        colorTextPlaceholder: '#e0e0e079'
      },
      components: {
        Card: {
          colorBorderSecondary: '#e0e0e0',
        },
        Input: {
          colorBorder: '#e0e0e0',
          colorIcon: '#e0e0e079'
        },
        Button: {
          primaryShadow: 'none'
        }
      }
    }}>
      <Outlet />
    </ConfigProvider>
  )
}