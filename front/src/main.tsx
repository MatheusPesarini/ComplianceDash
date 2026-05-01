import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import { ConfigProvider } from 'antd'
import ptBR from 'antd/locale/pt_BR'

const router = createBrowserRouter([
  {
    path: '/',
    element: <App />,
  },
])

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <ConfigProvider locale={ptBR} theme={{ token: { colorPrimary: '#1677ff' } }}>
      <RouterProvider router={router} />
    </ConfigProvider>
  </StrictMode>,
)
