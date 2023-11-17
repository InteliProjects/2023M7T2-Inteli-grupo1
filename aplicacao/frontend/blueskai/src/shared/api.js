import React from 'react';

// transformar isso em um objeto com mais funções e useEffects, 
// aircraftList sera uma lista que tem seus valores atualizados a partir do fetch que ocorre dentro do useEffect


export default function handleApi(aircrafts, setAircrafts){
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
  }

