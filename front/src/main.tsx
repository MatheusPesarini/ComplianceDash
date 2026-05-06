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
      <RouterProvider router={router} />
    </QueryClientProvider>
  </StrictMode>,
)
