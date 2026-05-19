import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { Breadcrumb, Button, Card, Form, Input, message, Modal, Select, Table, Tag, theme } from "antd";
import { Content } from "antd/es/layout/layout";
import { CreatePrivacyRequest } from "../../services/privacyRequest/CreateUserRequest";
import { GetUserRequests } from "../../services/privacyRequest/GetUserRequests";
import { useAuthStore } from "../../stores/authStore";
import type { CreatePrivacyRequestType } from "../../types/Request";
import React from "react";
import { PlusOutlined } from "@ant-design/icons";

const { TextArea } = Input;

export default function UserRequests() {
  const {
    token: { borderRadiusLG, colorBgContainer }
  } = theme.useToken();

  const jwt_token = useAuthStore(state => state.jwt_token)
  const queryClient = useQueryClient();

  const [isModalOpen, setIsModalOpen] = React.useState(false);
  const [form] = Form.useForm();

  const created_privacy_request = useMutation({
    mutationFn: (values: CreatePrivacyRequestType) => CreatePrivacyRequest(values, jwt_token as string),
    onSuccess: () => {
      message.success('Privacy request created with success!');
      setIsModalOpen(false);
      form.resetFields();

      queryClient.invalidateQueries({ queryKey: ['get_user_privacy_requests'] });
    },
    onError: (Error) => {
      message.error('Failed to create privacy request. Error: ' + Error.message);
    }
  })

  const get_user_privacy_requests = useQuery({
    queryKey: ['get_user_privacy_requests'],
    queryFn: () => GetUserRequests(jwt_token as string),
    enabled: !!jwt_token,
  })

  const handleFinish = (values: CreatePrivacyRequestType) => {
    created_privacy_request.mutate(values);
  };

  const columns = [
    {
      title: 'ID', dataIndex: 'id', key: 'id'
    },
    {
      title: 'Type', dataIndex: 'request_type', key: 'request_type', render: (text: string) => text?.toUpperCase()
    },
    {
      title: 'Status', dataIndex: 'status', key: 'status', render: (status: string) => {
        const color = status === 'resolved' ? 'green' : status === 'pending' ? 'orange' : 'blue';
        return <Tag color={color}>{status?.toUpperCase()}</Tag>;
      }
    },
    {
      title: 'Created At', dataIndex: 'created_at', key: 'created_at', render: (date: string) => new Date(date).toLocaleDateString()
    },
    {
      title: 'Admin Notes', dataIndex: 'admin_notes', key: 'admin_notes'
    },
    {
      title: 'Resolved At', dataIndex: 'resolved_at', key: 'resolved_at', render: (date: string) => date ? new Date(date).toLocaleDateString() : '-'
    }
  ]

  return (
    <>
      <Breadcrumb style={{ margin: '16px 0' }} items={[{ title: 'User Panel' }, { title: 'Requests' }]} />
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
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h2>My Privacy Requests</h2>
          <Button
            type="primary"
            icon={<PlusOutlined />}
            onClick={() => setIsModalOpen(true)}
          >
            New Request
          </Button>
        </div>

        <Card style={{ width: '100%' }} variant='borderless'>
          <p style={{ margin: 0 }}>
            Manage your Data Subject Access Requests (DSAR). Here you can open new requests to access, modify, or delete your personal data. Track the status of your existing requests and view responses from our compliance team.
          </p>
        </Card>

        <Table
          dataSource={get_user_privacy_requests.data}
          columns={columns}
          rowKey="id"
          loading={get_user_privacy_requests.isLoading}
          pagination={{ pageSize: 5 }}
        />

        <Modal
          title="Open New Privacy Request"
          open={isModalOpen}
          onCancel={() => setIsModalOpen(false)}
          onOk={() => form.submit()}
          okText="Submit Request"
          confirmLoading={created_privacy_request.isPending}
        >
          <Form form={form} layout="vertical" onFinish={handleFinish}>
            <Form.Item
              name="request_type"
              label="Request Type"
              rules={[{ required: true, message: 'Please select a request type' }]}
            >
              <Select
                placeholder="Select the type of request"
                options={[
                  { value: 'access', label: 'Access my data' },
                  { value: 'deletion', label: 'Delete my data' },
                  { value: 'correction', label: 'Correct my data' },
                  { value: 'portability', label: 'Portability' },
                  { value: 'opt_out', label: 'Opt-out of processing' },
                ]}
              />
            </Form.Item>

            <Form.Item
              name="details"
              label="Additional Details (Optional)"
            >
              <TextArea rows={4} placeholder="Provide any extra context for our compliance team..." />
            </Form.Item>
          </Form>
        </Modal>
      </Content>
    </>
  )
}