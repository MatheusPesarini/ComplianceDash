import { Card, Form, Button, Input } from 'antd';

export default function RegisterPage() {
  return (
    <div>
      <Card style={{ width: 640 }} variant='borderless' title="Register">
        <Form layout='vertical'>
          <Form.Item label='Name' name='name' rules={[{ required: true, message: 'Name is obrigatory!' }]}>
            <Input placeholder='Write your name' size='large' maxLength={100} />
          </Form.Item>

          <Form.Item label='E-mail' name='email' rules={[{ required: true, message: 'E-mail is obrigatory!' }]}>
            <Input placeholder='Write your e-mail' size='large' maxLength={100} />
          </Form.Item>

          <Form.Item label='Senha' name='senha' rules={[{ required: true, message: 'Password is obrigatory!' }]}>
            <Input.Password placeholder='Write your password' size='large' maxLength={25} />
          </Form.Item>

          <Form.Item label='Phone' name='phone' rules={[{ required: true, message: 'Phone is obrigatory!' }]}>
            <Input placeholder='Write your phone' size='large' maxLength={100} />
          </Form.Item>

          <Form.Item label={null}>
            <Button type='primary' htmlType='submit'>
              Submit
            </Button>
          </Form.Item>
        </Form>
      </Card>
    </div>
  )
}