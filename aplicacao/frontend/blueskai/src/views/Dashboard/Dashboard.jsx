import React, { useState } from "react";
import { SideBar } from "../../components/SideBar"; // Certifique-se de fornecer o caminho correto
import { PlaneInformationCard } from "../../components/PlaneInformationCard";
import { AircraftsTable } from "../../components/AircraftsTable";
import LineChartComponent from "../../components/LineChart/LineChart";
import { Card, Divider, Row, Col, Select } from "antd";
import { DonutChart } from "@/components/DonutChart";
import { PredictionCard } from "@/components/PredictionCard";

import aircraftList from "@/shared/global";

export default function Dashboard() {
  const [selectedOption, setSelectedOption] = useState("bimestre");

  const { Option } = Select;

  const handleSelectChange = (value) => {
    setSelectedOption(value);
  };

  return (
    <>
      <PlaneInformationCard />
      <PredictionCard />
      <Row>
        <Col span={16}>
          <Card
            style={{
              marginLeft: "50px",
              marginRight: "50px",
              marginBottom: "50px",
              width: "auto",
              height: "65vh",
            }}
          >
            <Row style={{ marginBottom: "5vh" }}>
              <Col span={18}>
                <h2>Porcentagem de Falha por Horas de voo</h2>
              </Col>
              <Col span={6}>
                <Select
                  defaultValue="bimestre" // Opção padrão selecionada
                  style={{ width: 120 }}
                  onChange={handleSelectChange}
                >
                  <Option value="bimestre">Bimestre</Option>
                  <Option value="trimestre">Trimestre</Option>
                  <Option value="semestre">Semestre</Option>
                </Select>
              </Col>
            </Row>
            <LineChartComponent />
          </Card>
        </Col>
        <Col span={7}>
          <Card
            style={{
              textAlign: "center",
              height: "65vh",
              alignContent: "center",
            }}
          >
            <h2>Quantidade de Voos vs Falha</h2>
            <DonutChart />
          </Card>
        </Col>
      </Row>
      <Row>
        <AircraftsTable />
      </Row>
    </>
  );
}
