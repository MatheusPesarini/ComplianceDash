import { CheckCircleOutlined, ClockCircleOutlined, SyncOutlined } from "@ant-design/icons";
import { Breadcrumb, Card, Col, Row, Statistic, theme } from "antd";
import { Content } from "antd/es/layout/layout";

export default function UserPage() {
  const {
    token: { borderRadiusLG, colorBgContainer }
  } = theme.useToken();

  return (
    <>
      <Breadcrumb style={{ margin: '16px 0' }} items={[{ title: 'User Panel' }, { title: 'Dashboard' }]} />
      <Content
        style={{
          padding: 24,
          background: colorBgContainer,
          borderRadius: borderRadiusLG,
          display: 'flex',
          flexDirection: 'column',
          gap: 24
        }}
      >
        <Card style={{ width: '100%' }} variant='borderless' title="Compliance Dashboard">
          Welcome to the compliance dashboard! Here you can find information about your compliance status, manage your compliance data and access compliance-specific features. Explore the options available to you and make the most of your experience on our platform.
        </Card>

        <Row gutter={16}>
          <Col span={8}>
            <Card variant='borderless' style={{ background: '#253746' }}>
              <Statistic
                title="Approved"
                value={1}
                styles={{ content: { color: '#52c41a' } }}
                prefix={<CheckCircleOutlined />}
              />
            </Card>
          </Col>
          <Col span={8}>
            <Card variant='borderless' style={{ background: '#253746' }}>
              <Statistic
                title="In Analysis"
                value={0}
                styles={{ content: { color: '#1677ff' } }}
                prefix={<SyncOutlined />}
              />
            </Card>
          </Col>
          <Col span={8}>
            <Card variant='borderless' style={{ background: '#253746' }}>
              <Statistic
                title="Pending"
                value={2}
                styles={{ content: { color: '#faad14' } }}
                prefix={<ClockCircleOutlined />}
              />
            </Card>
          </Col>
        </Row>
      </Content>
    </>
  )
}