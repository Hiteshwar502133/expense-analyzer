import { useEffect, useState } from "react";
import API from "../services/api";
import { PieChart, Pie, Cell, Tooltip, Legend } from "recharts";
import { motion } from "framer-motion";

export default function Dashboard() {
  const [expenses, setExpenses] = useState([]);
  const [filter, setFilter] = useState("All");

  // Fetch data
  useEffect(() => {
    const fetchExpenses = async () => {
      try {
        const res = await API.get("/expenses/");
        setExpenses(res.data);
      } catch (err) {
        console.error(err);
      }
    };

    fetchExpenses();
  }, []);

  // Total
  const total = expenses.reduce((sum, exp) => sum + exp.amount, 0);

  // Categories
  const categories = ["All", ...new Set(expenses.map(e => e.category))];

  // Filter logic
  const filteredExpenses =
    filter === "All"
      ? expenses
      : expenses.filter(e => e.category === filter);

  // Group data for chart (IMPORTANT: use filteredExpenses)
  const categoryMap = {};

  filteredExpenses.forEach((exp) => {
    if (categoryMap[exp.category]) {
      categoryMap[exp.category] += exp.amount;
    } else {
      categoryMap[exp.category] = exp.amount;
    }
  });

  const data = Object.keys(categoryMap).map((key) => ({
    name: key,
    value: categoryMap[key],
  }));

  const COLORS = ["#00C49F", "#FF8042", "#0088FE", "#FFBB28", "#AA336A"];

  return (
  <div
    style={{
      padding: "30px",
      color: "white",
      minHeight: "100vh",
      background: "#0f172a",
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
    }}
  >
    <h1 style={{ fontSize: "40px", marginBottom: "10px" }}>
      Dashboard
    </h1>

    <h2 style={{ marginBottom: "20px" }}>
      Total: ₹ {total}
    </h2>

    {/* ✅ FILTER */}
    <select
  value={filter}
  onChange={(e) => setFilter(e.target.value)}
  style={{
    padding: "12px 20px",
    borderRadius: "10px",
    border: "1px solid #334155",
    marginBottom: "30px",
    background: "#1e293b",
    color: "white",
    fontSize: "16px",
    minWidth: "180px",
    textAlign: "center",
    outline: "none",
    cursor: "pointer",
  }}
>
  {categories.map((cat, i) => (
    <option key={i} value={cat}>
      {cat}
    </option>
  ))}
</select>

    {/* ✅ MAIN CONTAINER */}
    <div
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        gap: "60px",
        flexWrap: "wrap",
        width: "100%",
        maxWidth: "1000px",
      }}
    >
      {/* ✅ CHART SECTION */}
      <div
        style={{
          background: "#1e293b",
          padding: "20px",
          borderRadius: "15px",
          boxShadow: "0 0 20px rgba(0,0,0,0.3)",
        }}
      >
        <PieChart width={350} height={350}>
          <Pie data={data} dataKey="value" outerRadius={120} label>
            {data.map((entry, index) => (
              <Cell
                key={index}
                fill={COLORS[index % COLORS.length]}
              />
            ))}
          </Pie>
          <Tooltip />
          <Legend layout="horizontal" verticalAlign="bottom" />
        </PieChart>
      </div>

      {/* ✅ LIST SECTION */}
      <div style={{ minWidth: "250px" }}>
        {filteredExpenses.length === 0 ? (
          <p>No expenses found</p>
        ) : (
          filteredExpenses.map((exp, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.05 }}
              style={{
                background: "#1e293b",
                padding: "12px",
                borderRadius: "10px",
                marginBottom: "12px",
                boxShadow: "0 0 10px rgba(0,0,0,0.2)",
              }}
            >
              ₹ {exp.amount} - {exp.category}
            </motion.div>
          ))
        )}
      </div>
    </div>
  </div>
);
}