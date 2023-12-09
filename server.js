// server.js
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();
const port = 5000;

app.use(cors());
app.use(express.json());

mongoose.connect('mongodb://localhost:27017/sbi_dashboard', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const financialQuarterSchema = new mongoose.Schema({
  quarter: String,
  revenue: String,
  netIncome: String,
  netProfit: String,
  operatingIncome: String,
});

const FinancialQuarter = mongoose.model('FinancialQuarter', financialQuarterSchema);

app.get('/api/financialQuarters/:quarter', async (req, res) => {
  const { quarter } = req.params;

  try {
    const data = await FinancialQuarter.findOne({ quarter });
    res.json(data);
  } catch (error) {
    console.error(error);
    res.status(500).send('Internal Server Error');
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
