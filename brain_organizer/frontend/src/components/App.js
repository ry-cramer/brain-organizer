import React, { Component } from "react";
import ReactFlow from 'reactflow';
import 'reactflow/dist/base.css';
import { render } from "react-dom";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import InputPage from "./InputPage";
import MindMap from "./MindMap";

export default function App() {
    return <Router>
        <Routes>
            {/* Input page is home page for now */}
            <Route path="/" element={<InputPage />} />
            <Route path="/input" element={<InputPage />} />
            <Route path="/mindmap" element={<MindMap />} />
        </Routes>
    </Router>;
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);