import React from 'react';
import { SideBar } from '../../components/SideBar'; // Certifique-se de fornecer o caminho correto
import { PlaneInformationCard } from '../../components/PlaneInformationCard';
import { Layout } from 'antd';
import { AircraftSlider } from '@/components/AircraftSlider';

export default function AirPlanes(){
  
  const aircraftList = [
    {
      serialNumber: '06120018',
      maintenanceStatus: 'good',
      flightHours: 750,
      imageUrl: 'https://cdn.panrotas.com.br/portal-panrotas-statics/media-files-cache/328821/c7ec14253136c02942e6199ee4aa42321azullinhasaereasiniciaoperacoesdeaeronaveinspiradaempatodonald/full/full,1/0/default.jpeg',
      failures: 5,
    },
    {
      serialNumber: '06120023',
      maintenanceStatus: 'warning',
      flightHours: 600,
      imageUrl: 'https://www.melhoresdestinos.com.br/wp-content/uploads/2021/12/aviao-azul-brasil-11.jpeg',
      failures: 10,
    },
    {
      serialNumber: '06120024',
      maintenanceStatus: 'critical',
      flightHours: 900,
      imageUrl: 'https://uploads.metropoles.com/wp-content/uploads/2021/01/15102427/Aviao-Azul-Vacina-Oxford-India-9.jpg',
      failures: 8,
    },
    {
      serialNumber: '06120018',
      maintenanceStatus: 'good',
      flightHours: 750,
      imageUrl: 'https://cdn.panrotas.com.br/portal-panrotas-statics/media-files-cache/328821/c7ec14253136c02942e6199ee4aa42321azullinhasaereasiniciaoperacoesdeaeronaveinspiradaempatodonald/full/full,1/0/default.jpeg',
      failures: 5,
    },
    {
      serialNumber: '06120023',
      maintenanceStatus: 'warning',
      flightHours: 600,
      imageUrl: 'https://www.melhoresdestinos.com.br/wp-content/uploads/2021/12/aviao-azul-brasil-11.jpeg',
      failures: 10,
    },
    {
      serialNumber: '06120024',
      maintenanceStatus: 'critical',
      flightHours: 900,
      imageUrl: 'https://uploads.metropoles.com/wp-content/uploads/2021/01/15102427/Aviao-Azul-Vacina-Oxford-India-9.jpg',
      failures: 8,
    },
  ];

  return (
    <>   
      <SideBar>
      <AircraftSlider aircraftList={aircraftList}/>
      </SideBar>
    </>
  );
}
