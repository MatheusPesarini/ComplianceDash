import { Card, Form, Input } from 'antd';

export default function LoginPage() {
  return (
    <div>
      <Card style={{ width: 640 }} variant='borderless' title="Login">
        <Form layout='vertical'>
          <Form.Item label='E-mail' name='email' rules={[{ required: true, message: 'O e-mail é obrigatório!' }]}><Input placeholder='Digite seu e-mail' /></Form.Item>
        </Form>
      </Card>
    </div>
  )
}