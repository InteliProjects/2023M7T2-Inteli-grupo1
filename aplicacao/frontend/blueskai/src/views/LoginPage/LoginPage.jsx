import React, { useState } from 'react';
import Image from 'next/image'
import { Card, Input, Button, Form, Typography, Divider } from 'antd';
import { EyeInvisibleOutlined, EyeTwoTone } from '@ant-design/icons';
import Styles from './LoginPage.module.scss'

import {signIn} from 'next-auth/react'
const { Title, Text } = Typography;

import logo from '../../assets/images/logo_blueskai.png'
import Credentials from 'next-auth/providers/credentials';

const LoginPage = () => {
  const [isSignup, setIsSignup] = useState(false);
  const [showPassword, setShowPassword] = useState(false);

  const togglePasswordVisibility = () => {
    setShowPassword(prevState => !prevState);
  };

  const onFinish = async (values) => {
    console.log('Received values:', values);
    // const res = await signIn('credentials', {
    //   redirect: false,
    //   email: values.email,
    //   password: values.password,
    // })
  };

  return (
    <div
        style={{
          backgroundImage: "url('https://i.pinimg.com/originals/c5/4f/31/c54f31a07242ad970d97285a1ebbadfa.jpg')",
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
            backgroundColor: '#F2EFFF',
            padding: '0px 28px 0px',
            width: '45%',
            height: '60%',
            borderRadius: '8px',
            boxShadow: '0px 4px 8px rgba(0, 0, 0, 0.1)',
          }}>
          <div>
            <div className={Styles.title} level={3}>{isSignup ? 'Cadastro' : 'Entrar'}</div>
            <div className={Styles.description}>{isSignup ? 'Preencha os campos abaixo para se cadastrar:' : 'Realize o Login para Acessar as Informações do Dashboard:'}</div>
          </div>

          <Form
            onFinish={onFinish}
            style={{ marginTop: '24px' }}
          >
            <Form.Item
              name="email"
              rules={[
                { required: true, message: 'Por favor, insira seu e-mail!' },
                { type: 'email', message: 'Por favor, insira um e-mail válido!' },
              ]}
            >
              <div className={Styles.description}>Email:</div>
              <Input className={Styles.input}/>
            </Form.Item>

            <Form.Item
              name="password"
              rules={[{ required: true, message: 'Por favor, insira sua senha!' }]}
            >
              <div className={Styles.description}>Senha:</div>
              <Input.Password
                className={Styles.input}
                iconRender={visible => (visible ? <EyeTwoTone onClick={togglePasswordVisibility} /> : <EyeInvisibleOutlined onClick={togglePasswordVisibility} />)}
              />
            </Form.Item>

            {isSignup && (
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
            )}

            <Form.Item>
              <Button className={Styles.button} type="primary" htmlType="submit" style={{ width: '100%' }}>
                Entrar
              </Button>
            </Form.Item>
          </Form>

        </Card>
    </div>
    
  );
};

export default LoginPage;