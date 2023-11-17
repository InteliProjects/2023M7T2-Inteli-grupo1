import React from 'react';
import { SideBar } from '../../components/SideBar'; // Certifique-se de fornecer o caminho correto
import { FlightDataForm } from '../../components/FlightDataForm';

export default function Prediction(){
  return (
    <>   
      <SideBar>
        <FlightDataForm/>
      </SideBar>
    </>
  );
}
