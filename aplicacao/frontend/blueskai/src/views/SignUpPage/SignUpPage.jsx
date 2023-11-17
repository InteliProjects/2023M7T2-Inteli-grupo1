import React, { useState } from 'react';
import Image from 'next/image'
import { Card, Input, Button, Form, Typography, Divider } from 'antd';
import { EyeInvisibleOutlined, EyeTwoTone } from '@ant-design/icons';

const { Title, Text } = Typography;

import logo from '../../assets/images/logo_blueskai.png'

const SignUpPage = () => {
  const [showPassword, setShowPassword] = useState(false);

  const togglePasswordVisibility = () => {
    setShowPassword(prevState => !prevState);
  };

  const onFinish = values => {
    console.log('Received values:', values);
    // Here you can implement your login or signup logic
  };

  return (
    <div
      style={{
        background: `url('https://github.com/2023M7T2-Inteli/Blue-SkAI/blob/frontend/aplicacao/frontend/blueskai/src/assets/images/login-background.png?raw=true')`,
        backgroundSize: 'cover',
        minHeight: '100vh',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
      }}
    >
      <Image
        src={logo}
        alt="Logo"
        style={{ position: 'absolute', top: '5%', width: '90px', height:'65px' }}
      />

<Card
        style={{
          width: '45%',
          height: '60%',
          borderRadius: '8px',
          boxShadow: '0px 4px 8px rgba(0, 0, 0, 0.1)',
        }}
      >
        <div style={{ textAlign: 'center' }}>
          <Title level={3}>'Cadastro'</Title>
          <Text>'Preencha os campos abaixo para se cadastrar:'</Text>
        </div>

        <Form
          onFinish={onFinish}
          style={{ marginTop: '24px' }}
        >
          
            <Form.Item
              name="fullName"
              rules={[{ required: true, message: 'Por favor, insira seu nome completo!' }]}
            >
              <Input placeholder="Nome Completo" />
            </Form.Item>
          

          <Form.Item
            name="email"
            rules={[
              { required: true, message: 'Por favor, insira seu e-mail!' },
              { type: 'email', message: 'Por favor, insira um e-mail válido!' },
            ]}
          >
            <Input placeholder="E-mail" />
          </Form.Item>

          <Form.Item
            name="password"
            rules={[{ required: true, message: 'Por favor, insira sua senha!' }]}
          >
            <Input.Password
              placeholder="Senha"
              iconRender={visible => (visible ? <EyeTwoTone onClick={togglePasswordVisibility} /> : <EyeInvisibleOutlined onClick={togglePasswordVisibility} />)}
            />
          </Form.Item>

            <Form.Item
              name="confirmPassword"
              dependencies={['password']}
              rules={[
                { required: true, message: 'Por favor, confirme sua senha!' },
                ({ getFieldValue }) => ({
                  validator(_, value) {
                    if (!value || getFieldValue('password') === value) {
                      return Promise.resolve();
                    }
                    return Promise.reject(new Error('As senhas não coincidem!'));
                  },
                }),
              ]}
            >
              <Input.Password placeholder="Confirmar Senha" />
            </Form.Item>
          

          <Form.Item>
            <Button type="primary" htmlType="submit" style={{ width: '100%' }}>
              'Cadastrar'
            </Button>
          </Form.Item>
        </Form>

        <Divider />

        <Text>
            'Já tem uma conta?'
          <Button type="link" onClick={() => setIsSignup(prevState => !prevState)}>
            'Fazer Login'
          </Button>
        </Text>
      </Card>
    </div>
  );
};

export default SignUpPage;