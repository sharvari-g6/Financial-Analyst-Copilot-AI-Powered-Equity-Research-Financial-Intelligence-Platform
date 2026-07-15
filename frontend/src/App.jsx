import { Routes, Route } from "react-router-dom";
import { useEffect, useState } from "react";

import Navbar from "./components/Navbar";

import Home from "./pages/Home";
import Upload from "./pages/Upload";
import Chat from "./pages/Chat";
import Analysis from "./pages/Analysis";
import History from "./pages/History";

import "./App.css";

function App() {
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        const handler = (e) => {
            const detail = e?.detail || {};
            setLoading(Boolean(detail.loading));
        };
        window.addEventListener("api-loading", handler);
        return () => window.removeEventListener("api-loading", handler);
    }, []);

    return (
        <>
            <Navbar />

            <main className="app-shell">
                <div className="container">
                    <Routes>
                        <Route path="/" element={<Home />} />
                        <Route path="/upload" element={<Upload />} />
                        <Route path="/chat" element={<Chat />} />
                        <Route path="/analysis/:company/:year" element={<Analysis />} />
                        <Route path="/history" element={<History />} />
                    </Routes>
                </div>
            </main>

            {loading && (
                <div className="loading-overlay" role="status" aria-live="polite">
                    <div className="loading-card">
                        <div className="spinner" />
                        <div className="loading-text">Generating response — please wait...</div>
                    </div>
                </div>
            )}
        </>
    );
}

export default App;