import React, { useState, useEffect } from 'react';
import { Button, Modal } from 'antd';

const DiagnosticModal = ({ modalTitle }) => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const showModal = () => {
    setIsModalOpen(true);
  };
  const handleOk = () => {
    setIsModalOpen(false);
  };
  const handleCancel = () => {
    setIsModalOpen(false);
  };

  // const [aircrafts, setAircrafts] = useState([]);

  // const fetchData = async () => {
  //   const response = await fetch('http://localhost:3001/dash/airplanes')
  //   if (!response.ok) {
  //     throw new Error('Data coud not be fetched!')
  //   } else {
  //     return response.json()
  //   }
  // }
  // useEffect(() => {
  //   fetchData()
  //     .then((res) => {
  //       setAircrafts(res)
  //     })
  //     .catch((e) => {
  //       console.log(e.message)
  //     })
  // }, [])
    

  // console.log(aircrafts.serialNumber)

  return (
    <>
      <Button type="primary" onClick={showModal}>
        Diagnóstico
      </Button>
      <Modal title={modalTitle} open={isModalOpen} onOk={handleOk} onCancel={handleCancel}>

        <br></br>
        <p>A mais recente previsão de manutenção apontou a probabilidade de 18% de falha nos proximos 10 ciclos desta aeronave</p>
        <br></br>
        <p>A probabilidade aumentou 3% desde o ultimo ciclo analisado </p>
        
      </Modal>
    </>
  );
};
export default DiagnosticModal;