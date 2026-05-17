import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import AuthLayout from './layouts/AuthLayout'
import LoginPage from './pages/Login/index.tsx'
import RegisterPage from './pages/Register/index.tsx'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import ProtectedRoute from './layouts/ProtectedRoute.tsx'
import { ConfigProvider, theme } from "antd"
import ptBR from "antd/locale/pt_BR"
import UserPage from './pages/User/index.tsx'
import AdminPage from './pages/Admin/index.tsx'
import RouteDispatcher from './layouts/RouteDispatcher.tsx'
import BaseLayout from './layouts/BaseLayout.tsx'
import RequireUser from './layouts/RequireUser.tsx'
import UserTasks from './pages/UserTasks/index.tsx'
import RequireAdmin from './layouts/RequireAdmin.tsx'
import AdminTasks from './pages/AdminTasks/index.tsx'

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
    path: '/',
    errorElement: <div>Page not found</div>,
    element: <ProtectedRoute />,
    children: [
      {
        element: <BaseLayout />,
        children: [
          { index: true, element: <RouteDispatcher /> },
          {
            element: <RequireUser />,
            children: [
              { path: 'user', element: <UserPage /> },
              { path: 'user-tasks', element: <UserTasks /> }
            ]
          },
          {
            element: <RequireAdmin />,
            children: [
              { path: 'admin', element: <AdminPage /> },
              { path: 'admin-tasks', element: <AdminTasks /> }
            ]
          }
        ]
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
          algorithm: theme.darkAlgorithm,
          token: {
            colorPrimary: '#1677ff',
            colorBgContainer: '#192734',
            colorText: '#E0E0E0',
            colorSplit: '#e0e0e0',
            colorTextPlaceholder: '#e0e0e079',
            borderRadiusLG: 8,
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
            },
            Layout: {
              colorBgHeader: '#192734',
            }
          }
        }}
      >
        <RouterProvider router={router} />
      </ConfigProvider>
    </QueryClientProvider>
  </StrictMode>,
)