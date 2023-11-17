import React from 'react';
import { Card, Row, Col, Button, Carousel, Space } from 'antd';
import { AlertOutlined, RightOutlined, LeftOutlined } from '@ant-design/icons';

const AircraftCard = ({ aircraft }) => {
  const { serialNumber, maintenanceStatus, flightHours, failures } = aircraft;

  // Função para determinar a cor do ícone de alerta com base no status de manutenção
  const getAlertColor = () => {
    if (maintenanceStatus === 'good') {
      return 'green';
    } else if (maintenanceStatus === 'warning') {
      return 'yellow';
    } else {
      return 'red';
    }
  };

  return (
    <Card style={{ width: 400, height: "70vh" }}>
        <Space direction='vertical' size={10}>
        <img src={aircraft.imageUrl} alt={serialNumber} style={{ maxWidth: '100%', borderRadius:10 }} />
      <h2>{serialNumber}</h2>
      <Space>
        <AlertOutlined style={{ color: getAlertColor() }} />
        <span>{maintenanceStatus}</span>
      </Space>
      <p><strong>Tempo de Voo:</strong> {flightHours} horas</p>
      <p><strong>Quantidade de Falhas Ocorridas:</strong> {failures}</p> {/* Adicione esta linha */}
      <Button type="primary">
        <a href="/">
        Visualizar Aeronave
        </a>
    </Button>
        </Space>
    </Card>
  );
};

function AircraftSlider({ aircraftList }) {
    const settings = {
            dots: false,
            autoplay: true,
            slidesToShow: 3,
            slidesToScroll: 3,
            infinite: true, // Loop infinito
            nextArrow: <RightOutlined style={{ fontSize: '24px', color: '#1890ff' }} />, // Ícone da seta direita
            prevArrow: <LeftOutlined style={{ fontSize: '24px', color: '#1890ff' }} />, // Ícone da seta esquerda
            appendDots: (dots) => <ul style={{ display: 'none' }}>{dots}</ul>, // Esconder os pontos (dots)
            customPaging: (i) => <div style={{ display: 'none' }}>{i}</div>, // Esconder os números de página
    };
  
    return (
      <div style={{ marginTop: 100 }}>
        <Carousel dots={true} autoplay {...settings}>
          {aircraftList.map((aircraft, index) => (
            <div key={index}>
              <Row justify="center">
                <Col>
                  <AircraftCard aircraft={aircraft} />
                </Col>
              </Row>
            </div>
          ))}
        </Carousel>
      </div>
    );
  }
  
  export default AircraftSlider;
