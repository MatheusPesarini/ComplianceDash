import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import AuthLayout from './layouts/AuthLayout'
import LoginPage from './pages/Login/index.tsx'
import RegisterPage from './pages/Register/index.tsx'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import ProtectedRoute from './layouts/ProtectedRoute.tsx'

// IMPORTADOS DAQUI
import { ConfigProvider, theme } from "antd"
import ptBR from "antd/locale/pt_BR"

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false,
      refetchOnReconnect: false,
      refetchOnMount: false,
    }
  }
})

const router = createBrowserRouter([
  {
    errorElement: <div>Page not found</div>,
    children: [
      {
        element: <AuthLayout />,
        children: [
          { path: 'login', element: <LoginPage /> },
          { path: 'register', element: <RegisterPage /> },
        ]
      }
    ]
  },
  {
    errorElement: <div>Page not found</div>,
    element: <ProtectedRoute />,
    children: [
      {
        element: <App />
      }
    ]
  }
])

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <QueryClientProvider client={queryClient}>
      <ConfigProvider
        locale={ptBR}
        theme={{
          algorithm: theme.darkAlgorithm, // não esqueça o darkAlgorithm
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
        }}
      >
        <RouterProvider router={router} />
      </ConfigProvider>
    </QueryClientProvider>
  </StrictMode>,
)