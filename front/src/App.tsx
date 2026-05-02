import { Outlet } from "react-router-dom"
import { ConfigProvider } from "antd"
import ptBR from "antd/locale/pt_BR"

export default function App() {
  return (
    <ConfigProvider locale={ptBR} theme={{
      token: {
        colorPrimary: '#1677ff', colorBgContainer: '#192734', colorText: '#E0E0E0', colorSplit: '#E0E0E0'
      },
      components: {
        Card: {
          colorBorderSecondary: '#E0E0E0',
        }
      }
    }}>
      <Outlet />
    </ConfigProvider>
  )
}