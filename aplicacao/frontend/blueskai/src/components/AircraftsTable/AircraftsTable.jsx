import React, { useState, useEffect } from "react";
import { Card, Input, Select, Table, Space, Row, Col, Button } from "antd";
import { SearchOutlined } from "@ant-design/icons";
import { isWithinInterval, subDays, parse, format } from "date-fns";

const { Option } = Select;

const data = [
    {
      key: "1",
      image:
        "https://aeroin.net/wp-content/uploads/2021/12/Azul-ATR-1024x684.jpg",
      serialNumber: "06120018",
      lastEntryDate: "06/10/2023",
      flightTime: "125 horas",
      failureOccurrences: 5,
    },
    {
      key: "2",
      image:
        "https://aeroin.net/wp-content/uploads/2021/12/Azul-ATR-1024x684.jpg",
      serialNumber: "06120022",
      lastEntryDate: "05/08/2023",
      flightTime: "98 horas",
      failureOccurrences: 2,
    },
    {
      key: "3",
      image:
        "https://aeroin.net/wp-content/uploads/2021/12/Azul-ATR-1024x684.jpg",
      serialNumber: "06120023",
      lastEntryDate: "01/10/2023",
      flightTime: "98 horas",
      failureOccurrences: 2,
    },
    {
      key: "4",
      image:
        "https://aeroin.net/wp-content/uploads/2021/12/Azul-ATR-1024x684.jpg",
      serialNumber: "06120024",
      lastEntryDate: "20/09/2023",
      flightTime: "75 horas",
      failureOccurrences: 3,
    },
    {
      key: "5",
      image:
        "https://aeroin.net/wp-content/uploads/2021/12/Azul-ATR-1024x684.jpg",
      serialNumber: "06120025",
      lastEntryDate: "15/08/2023",
      flightTime: "110 horas",
      failureOccurrences: 4,
    },
    // Adicione mais entradas conforme necessário
  ];

function AircraftsTable() {
  const [searchText, setSearchText] = useState("");
  const [selectedMonth, setSelectedMonth] = useState("lastMonth");

  const columns = [
    {
      title: "Imagem",
      dataIndex: "image",
      key: "image",
      render: (image) => (
        <img
          src={image}
          alt="Aircraft"
          width={100}
          style={{ borderRadius: "5%" }}
        />
      ),
    },
    {
      title: "Número de Série",
      dataIndex: "serialNumber",
      key: "serialNumber",
    },
    {
      title: "Última Data de Entrada",
      dataIndex: "lastEntryDate",
      key: "lastEntryDate",
    },
    {
      title: "Tempo de Voo",
      dataIndex: "flightTime",
      key: "flightTime",
    },
    {
      title: "Ocorrências de Falhas",
      dataIndex: "failureOccurrences",
      key: "failureOccurrences",
    },
    {
      title: "Acessar",
      key: "action",
      render: (text, record) => (
        <Space size="middle">
          <Button onClick={() => handleAircraftAccess(record)}>Acessar</Button>
        </Space>
      ),
    },
  ];

  const handleAircraftAccess = (record) => {
    // Lógica para acessar a aeronave com base nos dados do registro
    console.log("Acessar aeronave:", record.serialNumber);
    // Adicione sua lógica para a navegação ou outra ação desejada
  };

  const filteredData = data.filter((item) => {
    let shouldInclude = false;

    if (selectedMonth === "lastMonth") {
      const currentDate = new Date();
      const last30Days = subDays(currentDate, 30);
      const itemDate = parse(item.lastEntryDate, "dd/MM/yyyy", new Date());

      shouldInclude = isWithinInterval(itemDate, {
        start: last30Days,
        end: currentDate,
      });
    } else {
      const itemDate = parse(item.lastEntryDate, "dd/MM/yyyy", new Date());
      const monthName = format(itemDate, "MMMM");

      shouldInclude = monthName.toLowerCase() === selectedMonth.toLowerCase();
    }
    return (
      shouldInclude &&
      item.serialNumber.toLowerCase().includes(searchText.toLowerCase())
    );
  });

  return (
    <Card style={{ marginLeft: "50px", marginRight: "50px", width:'92%' }}>
      <Row>
        <Col span={12}>
          <h2>Selecionar Outra Aeronave</h2>
        </Col>
        <Col span={6}>
          <Input
            placeholder="Buscar aeronave"
            prefix={<SearchOutlined style={{ color: "#1890ff" }} />} // Ícone de lupa
            value={searchText}
            onChange={(e) => setSearchText(e.target.value)}
          />
        </Col>
        <Col span={6}>
          <Select
            style={{ width: 150, marginLeft: 10 }}
            value={selectedMonth}
            onChange={(value) => setSelectedMonth(value)}
          >
            <Option value="lastMonth">Último Mês</Option>
            <Option value="january">Janeiro</Option>
            <Option value="february">Fevereiro</Option>
            <Option value="march">Março</Option>
            <Option value="april">Abril</Option>
            <Option value="may">Maio</Option>
            <Option value="june">Junho</Option>
            <Option value="july">Julho</Option>
            <Option value="august">Agosto</Option>
            <Option value="september">Setembro</Option>
            <Option value="october">Outubro</Option>
            <Option value="november">Novembro</Option>
            <Option value="december">Dezembro</Option>

          </Select>
        </Col>
      </Row>
      <Table dataSource={filteredData} columns={columns} />
    </Card>
  );
}

export default AircraftsTable;