import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

const AppRoutes = () => (
    <Router>
        <Routes>
            <Route path="*" element={<div>404 Not Found</div>} />
        </Routes>
    </Router>
);

export default AppRoutes;