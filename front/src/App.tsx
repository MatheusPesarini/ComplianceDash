import { Outlet } from "react-router-dom"
import { ConfigProvider } from "antd"
import ptBR from "antd/locale/pt_BR"

export default function App() {
  return (
    <ConfigProvider locale={ptBR} theme={{ token: { colorPrimary: '#1677ff' } }}>
      <Outlet />
    </ConfigProvider>
  )
}