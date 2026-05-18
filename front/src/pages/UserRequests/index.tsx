import { useMutation, useQuery } from "@tanstack/react-query";
import { Breadcrumb, Card, theme } from "antd";
import { Content } from "antd/es/layout/layout";
import { CreatePrivacyRequest } from "../../services/privacyRequest/CreateUserRequest";
import { GetUserRequests } from "../../services/privacyRequest/GetUserRequests";
import { useAuthStore } from "../../stores/authStore";

export default function UserRequests() {
  const {
    token: { borderRadiusLG, colorBgContainer }
  } = theme.useToken();

  const jwt_token = useAuthStore(state => state.jwt_token)

  const created_privacy_request = useMutation({
    mutationFn: CreatePrivacyRequest,
    onSuccess: () => {

    },
    onError: (Error) => {
      console.error(`Error in create: ${Error.message}`);
    }
  })

  const get_user_privacy_requests = useQuery({
    queryKey: ['get_user_privacy_requests'],
    queryFn: () => GetUserRequests(jwt_token as string),
    enabled: !!jwt_token,
  })

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
        <Card style={{ width: '100%' }} variant='borderless' title="User Requests">
          Manage your Data Subject Access Requests (DSAR). Here you can open new requests to access, modify, or delete your personal data. Track the status of your existing requests and view responses from our compliance team.
        </Card>

      </Content>
    </>
  )
}