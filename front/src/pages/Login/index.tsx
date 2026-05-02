import { Card, Checkbox, Form, Button, Input } from 'antd';

export default function LoginPage() {
  return (
    <div>
      <Card style={{ width: 640 }} variant='borderless' title="Login">
        <Form layout='vertical'>
          <Form.Item label='E-mail' name='email' rules={[{ required: true, message: 'E-mail is obrigatory!' }]}>
            <Input placeholder='Write your e-mail' size='large' maxLength={100} />
          </Form.Item>

          <Form.Item label='Senha' name='senha' rules={[{ required: true, message: 'Password is obrigatory!' }]}>
            <Input.Password placeholder='Write your password' size='large' maxLength={25} />
          </Form.Item>

          <Form.Item name='remember' label={null}>
            <Checkbox>Remember-me</Checkbox>
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