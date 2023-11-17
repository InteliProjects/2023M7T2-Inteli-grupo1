import { PieChart, Pie, Cell, Text } from "recharts";
import { NoSSRWrapper } from "../NoSSRWrapper";

const data = [
  { name: "Quantidade de voos bem sucedidos", value: 9 },
  { name: "Quantidade de falhas", value: 3 },
];

const COLORS = ["#0088FE", "#00C49F", "#FFBB28", "#FF8042"];

const calculatePercentage = (value, total) =>
  ((value / total) * 100).toFixed(2) + "%";

export default function DonutChart() {
  const totalValue = data.reduce((acc, entry) => acc + entry.value, 0);

  return (
    <NoSSRWrapper>
      <PieChart width={340} height={400}>
        <Pie
          data={data}
          cx={165}
          cy={200}
          innerRadius={60}
          outerRadius={100}
          fill="#8884d8"
          paddingAngle={5}
          dataKey="value"
        >
          {data.map((entry, index) => (
            <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
          ))}
          <Text
            x={180}
            y={200}
            textAnchor="middle"
            dominantBaseline="middle"
            fill="#000000" // Cor do texto
            fontSize={24} // Tamanho da fonte
          ></Text>
        </Pie>
      </PieChart>
    </NoSSRWrapper>
  );
}
