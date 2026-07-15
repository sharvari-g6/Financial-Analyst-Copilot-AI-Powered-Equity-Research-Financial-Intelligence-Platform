# 📊 Financial Analyst Copilot

An AI-powered Financial Analysis Platform that combines **RAG (Retrieval-Augmented Generation), GraphRAG, Multi-Agent AI, Financial Forecasting, and Large Language Models** to automate the analysis of company annual reports.

The system enables users to upload a company's annual report (PDF), automatically extracts financial information, builds a knowledge graph, stores semantic embeddings for retrieval, generates financial forecasts, and produces an executive-level investment intelligence report.

---

# 🚀 Features

### 📄 Annual Report Processing

* Upload company annual reports (PDF)
* Automatic PDF text extraction
* Intelligent document chunking
* Metadata generation
* Vector embedding generation
* Semantic indexing using Pinecone

---

### 🧠 Retrieval-Augmented Generation (RAG)

* Semantic search over annual reports
* Context-aware question answering
* OpenAI-powered responses
* Financial document retrieval
* Company-specific chat assistant

---

### 🌐 GraphRAG

Automatically extracts and stores:

* Company
* Products
* Technologies
* Risks
* Business Segments
* Countries
* Key People

using **Neo4j Knowledge Graphs**.

---

### 🤖 Multi-Agent Financial Intelligence

The system uses multiple specialized AI agents.

#### Financial Analysis Agent

Analyzes

* Revenue
* Profitability
* Margins
* Financial performance
* Balance sheet health

---

#### Risk Analysis Agent

Evaluates

* Business risks
* Market risks
* Operational risks
* Legal risks

---

#### Valuation Agent

Analyzes

* Company valuation
* Growth potential
* Competitive positioning
* Investment attractiveness

---

#### Sentiment Agent

Analyzes

* Management tone
* Future outlook
* Positive/negative sentiment
* Business confidence

---

### 🧩 Executive Fusion Agent

Combines all individual agent reports into a single

**Investment Intelligence Report**

containing

* Executive Summary
* Financial Analysis
* Risk Analysis
* Valuation Analysis
* Sentiment Analysis
* Investment Thesis
* Recommendation
* Confidence Score

---

### 📈 Financial Forecasting

Historical financial statements are extracted automatically.

Metrics include

* Revenue
* Operating Income
* Net Income
* Operating Cash Flow
* Total Assets
* Total Liabilities
* Shareholders' Equity

Forecasting models:

* Prophet
* XGBoost

Forecast reports are generated using LLMs.

---

### 💬 AI Financial Chatbot

Ask natural language questions such as

* What are Apple's biggest risks?
* Explain the revenue growth.
* What products contribute most to revenue?
* Summarize the management discussion.
* What are the future opportunities?

The chatbot answers using the uploaded report as context.

---

### 🗄 Database Support

#### Pinecone

Stores semantic embeddings for RAG.

#### Neo4j

Stores company knowledge graph.

#### PostgreSQL

Stores

* Financial statements
* Prophet forecasts
* XGBoost forecasts
* Forecast reports
* Intelligence reports
* Upload history

---

# 🏗 System Architecture

```
                    Annual Report PDF
                           │
                           ▼
                  PDF Text Extraction
                           │
                           ▼
                   Intelligent Chunking
                           │
          ┌────────────────┴────────────────┐
          ▼                                 ▼
   Pinecone Vector DB                 Graph Builder
          │                                 │
          ▼                                 ▼
     Semantic Search                  Neo4j Graph
          │
          ▼
     Financial Extractor
          │
          ▼
 Historical Financial Statements
          │
     ┌────┴─────┐
     ▼          ▼
 Prophet     XGBoost
     ▼          ▼
 Forecast Generation
          │
          ▼
 Forecast Agent
          │
          ▼
 Multi-Agent Intelligence Engine
          │
          ▼
 Executive Fusion
          │
          ▼
 Investment Intelligence Report
          │
          ▼
 PostgreSQL Storage
          │
          ▼
 React Dashboard
```

---

# 🛠 Tech Stack

## Frontend

* React.js
* JavaScript
* React Router
* Axios
* Recharts
* CSS3

---

## Backend

* FastAPI
* Python
* SQLAlchemy
* Pydantic

---

## AI / LLM

* OpenAI GPT
* RAG
* GraphRAG
* Multi-Agent Architecture

---

## Machine Learning

* Prophet
* XGBoost
* Scikit-learn
* NumPy
* Pandas

---

## Vector Database

* Pinecone

---

## Graph Database

* Neo4j

---

## Relational Database

* PostgreSQL

---

# 📁 Project Structure

```
backend/
│
├── api/
│   ├── routes/
│   ├── services/
│   └── schemas/
│
├── processing/
│
├── rag/
│
├── graph/
│
├── forecasting/
│
├── agents/
│
├── fusion/
│
├── analysis/
│
├── repositories/
│
├── database/
│
├── models/
│
└── utils/

frontend/

├── components/
├── pages/
├── services/
├── assets/
└── styles/
```

---

# ⚙️ Workflow

## Step 1

Upload Annual Report

↓

## Step 2

Extract PDF Text

↓

## Step 3

Chunk Document

↓

## Step 4

Generate Metadata

↓

## Step 5

Store Embeddings in Pinecone

↓

## Step 6

Build Neo4j Knowledge Graph

↓

## Step 7

Extract Financial Statements

↓

## Step 8

Forecast Future Financial Metrics

↓

## Step 9

Generate Forecast Report

↓

## Step 10

Run Multi-Agent Financial Intelligence

↓

## Step 11

Fuse Reports into Executive Intelligence Report

↓

## Step 12

Store Results in PostgreSQL

↓

## Step 13

Display Interactive Dashboard

↓

## Step 14

Ask Questions via AI Chatbot

---

# 📊 Dashboard Features

* Upload annual reports
* View upload history
* Executive summary
* Financial analysis
* Risk analysis
* Valuation analysis
* Sentiment analysis
* Revenue forecast
* Financial charts
* AI chatbot
* Analysis history

---

# 📡 API Endpoints

## Upload

```
POST /api/upload
```

Uploads a company annual report and triggers the complete AI analysis pipeline.

---

## Chat

```
POST /api/chat
```

Ask questions about uploaded reports.

---

## Get All Analyses

```
GET /api/analysis
```

Returns all stored analyses.

---

## Get Analysis

```
GET /api/analysis/{company}/{year}
```

Returns a complete financial analysis.

---

## Delete Analysis

```
DELETE /api/analysis/{id}
```

Deletes an analysis record.

---

# 📈 Future Improvements

* Authentication & user accounts
* Multi-company comparison dashboard
* Portfolio analysis
* Stock price prediction
* Interactive financial ratio analysis
* SEC filing support (10-K, 10-Q)
* Export reports as PDF
* Email report sharing
* Dark mode
* Real-time financial news integration
* Company benchmarking
* Multi-document RAG
* Agent orchestration using LangGraph or CrewAI
* Deployment on AWS/GCP/Azure
* CI/CD with GitHub Actions
* Docker & Kubernetes support

---

# 👩‍💻 Author

**Sharvari Gupte**

B.Tech Computer Science (Data Science)

AI | Machine Learning | Financial Analytics | Generative AI | Full Stack Development

---

# 📄 License

This project is intended for educational and portfolio purposes.


