import React, { Component } from "react";
import { render } from "react-dom";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import InputPage from "./InputPage";
import MindMapPage from "./MindMapPage";

export default function App() {
    return <Router>
        <Routes>
            <Route path="/" element={<InputPage />} />
            <Route path="/input" element={<InputPage />} />
            <Route path="/mindmap" element={<MindMapPage />} />
        </Routes>
    </Router>;
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);