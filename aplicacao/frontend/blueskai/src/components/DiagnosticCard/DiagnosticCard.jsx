import React, { useState, useEffect } from 'react';
import { DiagnosticModal } from '../../components/DiagnosticModal'

import { Card } from 'antd';

import { handleApi } from '../../shared/api'
import {aircraftsList} from '../../shared/global'


const { Meta } = Card;

export default function DiagnosticCard({ img, title, description, modalTitle }){
  const [aircrafts, setAircrafts] = useState([]);

  useEffect(() => {
    // Fazer a solicitação HTTP para buscar todos os dados da tabela
    fetch('http://localhost:3001/dash/airplanes')
        .then((response) => response.json())
        .then((data) => {
            // Aqui, você pode filtrar apenas as colunas necessárias do objeto de dados
            const filteredAircrafts = data.airplanes.map((item) => ({
                serialNumber: item.aircraftSerNum_1,
            }));

            setAircrafts(filteredAircrafts);
        })
        .catch((error) => {
            console.error('Erro ao buscar dados:', error);
        });
  }, []);

  console.log(aircrafts);

  return (
    <>   
      <Card
        style={{
          width: 300,
        }}
        cover={
          <img
            alt="example"
            src={img}
          />
        }
        // Ativa os icones abaixo do card
        actions={[
          <DiagnosticModal modalTitle={modalTitle}/>
        ]}
        hoverable
      >
        <Meta
          // title={title}
          title={title}
          description={description}
        />
      </Card>
    </>
  );
}
