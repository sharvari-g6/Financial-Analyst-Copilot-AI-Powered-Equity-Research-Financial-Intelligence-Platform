import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import api from "../services/api";

import {

    LineChart,
    Line,
    XAxis,
    YAxis,
    Tooltip,
    ResponsiveContainer,
    CartesianGrid

} from "recharts";

import "./Analysis.css";

function Analysis(){

    const {company,year}=useParams();

    const [analysis,setAnalysis]=useState(null);

    useEffect(()=>{

        loadAnalysis();

    },[]);

    const loadAnalysis=async()=>{

        const res=await api.get(`/analysis/${company}/${year}`);

        setAnalysis(res.data);

    };

    if(!analysis){

        return <h2>Loading...</h2>;

    }

    const financial=analysis.financial_data;

    const revenueChart=financial.years.map((year,index)=>({

        year,

        Revenue:financial.revenue[index],

        Forecast:

        analysis.prophet_forecast.Revenue.forecast_values[index] || null

    }));

    return(

        <div className="dashboard">

            <h1>

                {analysis.company}

            </h1>

            <h3>

                Annual Report Analysis ({analysis.year})

            </h3>

            <div className="kpi-grid">

                <div className="kpi-card">

                    <h2>

                        Revenue

                    </h2>

                    <h1>

                        ${financial.revenue.at(-1)} M

                    </h1>

                </div>

                <div className="kpi-card">

                    <h2>

                        Net Income

                    </h2>

                    <h1>

                        ${financial.net_income.at(-1)} M

                    </h1>

                </div>

                <div className="kpi-card">

                    <h2>

                        Operating Income

                    </h2>

                    <h1>

                        ${financial.operating_income.at(-1)} M

                    </h1>

                </div>

                <div className="kpi-card">

                    <h2>

                        Confidence

                    </h2>

                    <h1>

                        High

                    </h1>

                </div>

            </div>

            <div className="chart-card">

                <h2>

                    Revenue Forecast

                </h2>

                <ResponsiveContainer width="100%" height={350}>

                    <LineChart data={revenueChart}>

                        <CartesianGrid />

                        <XAxis dataKey="year"/>

                        <YAxis/>

                        <Tooltip/>

                        <Line

                        dataKey="Revenue"

                        stroke="#2563eb"

                        />

                        <Line

                        dataKey="Forecast"

                        stroke="#16a34a"

                        />

                    </LineChart>

                </ResponsiveContainer>

            </div>

            <div className="report-card">

                <h2>

                    Executive Summary

                </h2>

                <p>

                    {analysis.intelligence_report.executive_summary}

                </p>

            </div>

            <div className="report-card">

                <h2>

                    Financial Analysis

                </h2>

                <p>

                    {analysis.intelligence_report.financial_analysis}

                </p>

            </div>

            <div className="report-card">

                <h2>

                    Risk Analysis

                </h2>

                <p>

                    {analysis.intelligence_report.risk_analysis}

                </p>

            </div>

            <div className="report-card">

                <h2>

                    Valuation Analysis

                </h2>

                <p>

                    {analysis.intelligence_report.valuation_analysis}

                </p>

            </div>

            <div className="report-card">

                <h2>

                    Sentiment Analysis

                </h2>

                <p>

                    {analysis.intelligence_report.sentiment_analysis}

                </p>

            </div>

            <div className="report-card">

                <h2>

                    Recommendation

                </h2>

                <h1>

                    {

                        analysis.intelligence_report.recommendation ||

                        "BUY"

                    }

                </h1>

            </div>

        </div>

    );

}

export default Analysis;