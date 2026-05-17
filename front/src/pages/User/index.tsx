import { Breadcrumb, theme } from "antd";
import { Content } from "antd/es/layout/layout";

export default function UserPage() {
  const {
    token: { borderRadiusLG }
  } = theme.useToken();

  return (
    <>
      <Breadcrumb style={{ margin: '16px 0' }} items={[{ title: 'User' }, { title: 'Bill' }]} />
      <Content
        style={{
          padding: 24,
          minHeight: 360,
          background: '#192734',
          borderRadius: borderRadiusLG,
        }}
      >
        Bill is a cat.
      </Content>
    </>
  )
}