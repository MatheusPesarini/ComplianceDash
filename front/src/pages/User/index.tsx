import { Breadcrumb } from "antd";
import { Content, Footer, Header } from "antd/es/layout/layout";

export default function UserPage() {
  return (
    <>
      <Header style={{ padding: 0 }} />
      <Content style={{ margin: '0 16px' }}>
        <Breadcrumb style={{ margin: '16px 0' }} items={[{ title: 'User' }, { title: 'Bill' }]} />
        <div
          style={{
            padding: 24,
            minHeight: 360,
            // background: colorBgContainer,
            // borderRadius: borderRadiusLG,
          }}
        >
          Bill is a cat.
        </div>
      </Content>
      <Footer style={{ textAlign: 'center' }}>
        Ant Design Created by Ant UED
      </Footer>
    </>
  )
}