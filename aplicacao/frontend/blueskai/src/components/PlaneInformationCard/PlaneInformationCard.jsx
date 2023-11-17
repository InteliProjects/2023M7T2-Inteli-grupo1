import React, { useState, useEffect } from "react";
import styles from "../../styles/PlaneCard.module.css";
import { LiaPlaneDepartureSolid } from "react-icons/lia";
import { AiOutlineClockCircle, AiOutlineAlert } from "react-icons/ai";
import LineChartComponent from "../LineChart/LineChart";
import { Card, Divider, Row, Space } from "antd";

import aircraftList from "@/shared/global";

function PlaneInformationCard() {
  // const [hours, setHours] = useState(0)

  // useEffect(() => {
  //   setHours((aircraftList[0].flightMinutes/60).toFixed(2))
  // })

  return (
    <>
      <h2 className={styles.title}>Hello, Teste!</h2>
      <Card
        style={{
          marginLeft: "50px",
          marginRight: "50px",
          marginBottom: "50px",
        }}
      >
        <Row align="space-around" style={{ paddingLeft: 35 }}>
          <Space size={60}>
            <div className={styles.cardSections}>
              <LiaPlaneDepartureSolid size="40" className={styles.planeIcon} />
              <div className={styles.information}>
                <p className={styles.p}>Aeronave</p>
                <h2 className={styles.h2}>06120024</h2>
              </div>
            </div>
            <Divider type="vertical" />
            <div className={styles.cardSections}>
              <AiOutlineClockCircle size="40" className={styles.clockIcon} />
              <div className={styles.information}>
                <p className={styles.p}>Tempo de Voo</p>
                <h2 className={styles.h2}>10h</h2>
              </div>
            </div>
            <Divider type="vertical" />
            <div className={styles.cardSections}>
              <AiOutlineAlert size="40" className={styles.alertIcon} />
              <div className={styles.information}>
                <p className={styles.p}>Falhas Ocorridas</p>
                <h2 className={styles.h2}>3</h2>
              </div>
            </div>
          </Space>
        </Row>
      </Card>
    </>
  );
}

export default PlaneInformationCard;
