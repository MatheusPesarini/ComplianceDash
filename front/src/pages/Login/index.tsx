import { Card, Checkbox, Form, Button, Input, message } from 'antd';
import { useMutation } from '@tanstack/react-query';
import { LoginUser } from '../../services/auth/LoginUser';
import type { LoginRequest } from '../../types/Auth';
import { Navigate, useNavigate } from 'react-router-dom';
import { useAuthStore } from '../../stores/authStore';

export default function LoginPage() {
  const [form] = Form.useForm();
  const navigate = useNavigate();

  const setAuth = useAuthStore((state) => state.setAuth);
  const jwt_token = useAuthStore((state) => state.jwt_token);

  const mutation = useMutation({
    mutationFn: LoginUser,
    onSuccess: (data) => {
      message.success('User logged with success!');

      setAuth(data.jwt_token, data.user_id);

      navigate('/');
    },
    onError: (Error) => {
      message.error(`Error in login: ${Error.message}`);
    }
  })

  if (jwt_token) {
    return <Navigate to="/" replace />;
  }

  const onFinish = (values: LoginRequest) => {
    mutation.mutate(values);
  }

  return (
    <div>
      <Card style={{ width: 640 }} variant='borderless' title="Login">
        <Form layout='vertical' form={form} onFinish={onFinish}>
          <Form.Item label='E-mail' name='email' rules={[{ required: true, message: 'E-mail is obrigatory!' }, { type: 'email', message: 'E-mail is not valid!' }]}>
            <Input placeholder='Write your e-mail' size='large' maxLength={100} />
          </Form.Item>

          <Form.Item label='Password' name='password' rules={[{ required: true, message: 'Password is obrigatory!' }]}>
            <Input.Password placeholder='Write your password' size='large' minLength={3} maxLength={25} />
          </Form.Item>

          <Form.Item name='remember' label={null} valuePropName='checked'>
            <Checkbox>Remember-me</Checkbox>
          </Form.Item>

          <Form.Item label={null}>
            <Button type='primary' htmlType='submit' loading={mutation.isPending}>
              Submit
            </Button>
          </Form.Item>
        </Form>
      </Card>
    </div>
  )
}