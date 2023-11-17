import React, { useEffect, useState } from "react";
import styles from "../../styles/PlaneCard.module.css";
import { LiaPlaneDepartureSolid } from "react-icons/lia";
import {
  AiOutlineClockCircle,
  AiOutlineAlert,
  AiOutlinePercentage,
  AiOutlineBulb,
} from "react-icons/ai";
import LineChartComponent from "../LineChart/LineChart";
import { Card, Divider, Row, Space, Button } from "antd";

import aircraftList from "@/shared/global";

export default function PredictionCard() {
  const [hours, setHours] = useState("Não");
  const [percentage, setPercentage] = useState(0);

  const possibleResults = ["Sim", "Não"];
  const percentageOptions = Array.from(
    { length: 75 - 30 + 1 },
    (_, i) => 30 + i
  );

  const handleButtonClick = () => {
    // Aleatoriamente selecionar "Sim" ou "Não"
    const randomResult =
      possibleResults[Math.floor(Math.random() * possibleResults.length)];
    setHours(randomResult);

    // Aleatoriamente selecionar uma porcentagem
    const randomPercentage =
      percentageOptions[Math.floor(Math.random() * percentageOptions.length)];
    setPercentage(randomPercentage);

    // Atualizar o valor de porcentagem no aircraftList
    aircraftList[0].message0418DAA_1 = randomPercentage;
  };

  return (
    <>
      <Card
        style={{
          marginLeft: "50px",
          marginRight: "50px",
          marginBottom: "50px",
        }}
      >
        <Row align="space-between" style={{ paddingLeft: 35 }}>
          <Space size={60}>
            <div className={styles.cardSections}>
              <h2 className={styles.h2}>
                Predição da Necessidade de Manutenção
              </h2>
            </div>
            <Divider type="vertical" />
            <div className={styles.cardSections}>
              <AiOutlineBulb size="40" />
              <div className={styles.information}>
                <p className={styles.p}>Possibilidade de Falhas em 15 Dias:</p>
                <h2 className={styles.h2}>{hours}</h2>
              </div>
            </div>
            <Divider type="vertical" />
            <div className={styles.cardSections}>
              <AiOutlinePercentage size="40" />
              <div className={styles.information}>
                <p className={styles.p}>Chance de Ocorrer uma Falha</p>
                <h2 className={styles.h2}>
                  {aircraftList[0].message0418DAA_1}%
                </h2>
              </div>
            </div>
            <Divider type="vertical" />
            <div className={styles.cardSections}>
              <Button type="primary" onClick={handleButtonClick}>
                Atualizar
              </Button>
            </div>
          </Space>
        </Row>
      </Card>
    </>
  );
}
