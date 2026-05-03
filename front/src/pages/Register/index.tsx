import { Card, Form, Button, Input, message } from 'antd';
import { useMutation, useQueryClient } from '@tanstack/react-query';
import { CreateUser } from '../../services/auth/CreateUser';
import type { RegisterRequest } from '../../types/Auth';
import { useNavigate } from 'react-router-dom';


export default function RegisterPage() {
  const [form] = Form.useForm();
  const queryClient = useQueryClient();
  const navigate = useNavigate();

  const mutation = useMutation({
    mutationFn: CreateUser,
    onSuccess: () => {
      message.success('User created with success!');

      queryClient.invalidateQueries({ queryKey: ['users'] });

      navigate('/login');
    },
    onError: (Error) => {
      message.error(`Error in create: ${Error.message}`);
    }
  })

  const onFinish = (values: RegisterRequest) => {
    mutation.mutate(values);
  }

  return (
    <div>
      <Card style={{ width: 640 }} variant='borderless' title="Register">
        <Form layout='vertical' form={form} onFinish={onFinish}>
          <Form.Item label='Name' name='name' rules={[{ required: true, message: 'Name is obrigatory!' }]}>
            <Input placeholder='Ex: João da Silva' size='large' maxLength={100} />
          </Form.Item>

          <Form.Item label='E-mail' name='email' rules={[{ required: true, message: 'E-mail is obrigatory!' }, { type: 'email', message: 'E-mail is not valid!' }]}>
            <Input placeholder='Ex: matheus@email.com' size='large' maxLength={100} type={'email'} />
          </Form.Item>

          <Form.Item label='Password' name='password' rules={[{ required: true, message: 'Password is obrigatory!' }]}>
            <Input.Password placeholder='Write your password' size='large' maxLength={25} />
          </Form.Item>

          <Form.Item label='Phone' name='phone' rules={[{ required: true, message: 'Phone is obrigatory!' }]}>
            <Input placeholder='Write your phone' size='large' maxLength={100} />
          </Form.Item>

          <Form.Item label={null}>
            <Button type='primary' htmlType='submit' loading={mutation.isPending}>
              Submit
            </Button>
          </Form.Item>
        </Form>
      </Card>
    </div >
  )
}