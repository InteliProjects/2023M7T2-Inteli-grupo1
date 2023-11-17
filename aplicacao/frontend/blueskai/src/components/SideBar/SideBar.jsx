import { useState } from 'react';
import { Layout, Menu } from 'antd';
import Image from 'next/image';
import {PieChartOutlined, CloudDownloadOutlined, RocketOutlined, SearchOutlined, QuestionCircleOutlined} from '@ant-design/icons';
import Link from 'next/link';
import { useRouter } from 'next/router';

const { Sider, Content } = Layout;

import logo from '../../assets/images/logo_blueskai.png';

function SideBar({ children }){
  const router = useRouter();
  const [collapsed, setCollapsed] = useState(false);

  const toggleCollapsed = () => {
    setCollapsed(!collapsed);
  };

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Sider collapsible collapsed={collapsed} onCollapse={toggleCollapsed} style={{backgroundColor:'#fff'}}>
        <div style={{display:'flex', justifyContent: 'center', alignItems: 'center'}}>
        <Image src={logo} style={{width:'100px', height: '70px', marginTop:'5vh'}}></Image>
        </div>
        <div style={{ height: '10px', backgroundColor: '#fff'}}/>
        <Menu
          theme="light"
          mode="vertical"
          defaultSelectedKeys={['dashboard']}
          selectedKeys={[router.pathname.substring(1)]}
        >
          <Menu.Item key="dashboard" icon={<PieChartOutlined />}>
            <Link href="/">Dashboard</Link>
          </Menu.Item>
          <Menu.Item key="prediction" icon={<CloudDownloadOutlined />}>
            <Link href="/prediction">Input - Dados</Link>
          </Menu.Item>
          <Menu.Item key="aircraft" icon={<RocketOutlined />}>
            <Link href="/aircraft">Aeronaves</Link>
          </Menu.Item>
          <Menu.Item key="diagnostics" icon={<SearchOutlined />}>
            <Link href="/diagnostic">Diagnóstico</Link>
          </Menu.Item>
          <Menu.Item key="help" icon={<QuestionCircleOutlined />}>
            <Link href="/help">Help</Link>
          </Menu.Item>
        </Menu>
      </Sider>
      <Layout className="site-layout">
        <Content style={{ margin: '16px' }}>{children}</Content>
      </Layout>
    </Layout>
  );
};

export default SideBar;
