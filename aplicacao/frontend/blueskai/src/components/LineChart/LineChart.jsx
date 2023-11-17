import React from "react";
import dynamic from "next/dynamic";
import {
  LineChart,
  Line,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  ReferenceLine,
} from "recharts";
import { NoSSRWrapper } from "../NoSSRWrapper";

const data = [
  { date: "Jan", failure: 1 },
  { date: "Fev", failure: 2 },
  { date: "Mar", failure: 4 },
  { date: "Abr", failure: 6 },
  { date: "Mai", failure: 2 },
  { date: "Jun", failure: 3 },
  { date: "Jul", failure: 3.5 },
  { date: "Ago", failure: 4 },
  { date: "Set", failure: 5 },
  { date: "Out", failure: 6 },
  { date: "Nov", failure: 4 },
  { date: "Dez", failure: 6 },
];

const thresholdValue = 5.5;

const CustomDot = (props) => {
  const { cx, cy, stroke, payload, value } = props;

  const aboveThreshold = value > thresholdValue;

  return (
    <g>
      <circle
        cx={cx}
        cy={cy}
        r={5}
        fill={aboveThreshold ? "red" : "blue"}
        stroke={stroke}
        strokeWidth={2}
      />
    </g>
  );
};

function LineChartComponent() {
  return (
    <NoSSRWrapper>
      <LineChart
        data={data}
        margin={{ top: 5, right: 5, bottom: 5, left: 0 }}
        width={650}
        height={350}
      >
        <Line
          type="monotone"
          dataKey="failure"
          stroke="#5932EA"
          strokeWidth={2}
          dot={CustomDot}
        />
        <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
        <XAxis dataKey="date" />
        <YAxis />
        <ReferenceLine y={5.5} stroke="black" />
        <Tooltip />
      </LineChart>
    </NoSSRWrapper>
  );
}

export default LineChartComponent;
