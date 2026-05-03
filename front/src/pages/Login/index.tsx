import { Card, Checkbox, Form, Button, Input, message } from 'antd';
import { useMutation } from '@tanstack/react-query';
import { LoginUser } from '../../services/auth/LoginUser';
import type { LoginRequest } from '../../types/Auth';
import { useNavigate } from 'react-router-dom';

export default function LoginPage() {
  const [form] = Form.useForm();
  const navigate = useNavigate();

  const mutation = useMutation({
    mutationFn: LoginUser,
    onSuccess: () => {
      message.success('User logged with success!');

      navigate('/');
    },
    onError: (Error) => {
      message.error(`Error in login: ${Error.message}`);
    }
  })

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
            <Input.Password placeholder='Write your password' size='large' maxLength={25} />
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