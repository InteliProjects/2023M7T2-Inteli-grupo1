import React, { useState, useEffect } from 'react';
import { SideBar } from '../../components/SideBar'; // Certifique-se de fornecer o caminho correto
// import { FlightDataForm } from '../../components/FlightDataForm';
import { DiagnosticCard } from '../../components/DiagnosticCard'
import aircraftList from '../../shared/global'
import { Card } from 'antd';

const { Meta } = Card;

export default function Diagnostic(){

  const [hours, setHours] = useState(0)

  useEffect(() => {
    setHours((aircraftList[0].flightMinutes/60).toFixed(2))
  })

  return (
    <>   
      <SideBar>
        {/* <DiagnosticCard
          // img = 'https://www.techrepublic.com/wp-content/uploads/2021/12/united-za-techrepublic.jpg'
          img = {aircraftList[0].imageUrl}
          // title={aircraftList[0].aircraftSerNum}
          // title= {`Voo ${aircraftList[0].created_at}`}
          title= {`Aeronave ${aircraftList[0].aircraftSerNum}`}
          description = {`Voo ${aircraftList[0].created_at}`}
          modalTitle='Diagnóstico AZ/PS-AEK'
        /> */}

        {aircraftList.map((aircraft, index) => (
            <div key={index} style={{display: 'inline-block', margin: '20px'}}>
              <DiagnosticCard
                // img = 'https://www.techrepublic.com/wp-content/uploads/2021/12/united-za-techrepublic.jpg'
                img = {aircraftList[index].imageUrl}
                // title={aircraftList[0].aircraftSerNum}
                // title= {`Voo ${aircraftList[0].created_at}`}
                title= {`Aeronave ${aircraftList[index].aircraftSerNum}`}
                description = {`Voo ${aircraftList[index].created_at}`}
                modalTitle='Diagnóstico AZ/PS-AEK'
              />
            </div>
        ))}

    
      </SideBar>
    </>
  );
}
