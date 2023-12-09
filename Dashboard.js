// src/Dashboard.js
import React, { useState, useEffect } from "react";
import { fetchData } from "./api";
import "./Dashboard.css";


const Dashboard = () => {
  const [quarter, setQuarter] = useState("q1");
  const [metrics, setMetrics] = useState({});

  useEffect(() => {
    fetchData(quarter).then((data) => setMetrics(data));
  }, [quarter]);

  const handleQuarterChange = (event) => {
    setQuarter(event.target.value);
  };

  return (
    <div>
      <h1>SBI Dashboard</h1>
      <select value={quarter} onChange={handleQuarterChange}>
        <option value="q1">Quarter 1 (Dec 22)</option>
        <option value="q2">Quarter 2 (Mar 23)</option>
        <option value="q3">Quarter 3 (Jun 23)</option>
        <option value="q4">Quarter 4 (Sep 23)</option>
      </select>
      <div className="tile">Revenue: {metrics.revenue}</div>
      <div className="tile">Net Income: {metrics.netIncome}</div>
      <div className="tile">Net Profit: {metrics.netProfit}</div>
      <div className="tile">Operating Income: {metrics.operatingIncome}</div>
    </div>
  );
};

export default Dashboard;
