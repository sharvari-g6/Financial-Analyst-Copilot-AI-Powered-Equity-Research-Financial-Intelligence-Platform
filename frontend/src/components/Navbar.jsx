import { Link } from "react-router-dom";
import "./Navbar.css";

function Navbar() {

    return (

        <nav className="navbar">

            <div className="logo">

                📊 Financial Analyst Copilot

            </div>

            <div className="nav-links">

                <Link to="/">Home</Link>

                <Link to="/upload">Upload</Link>

                <Link to="/chat">Chat</Link>

                <Link to="/analysis">Analysis</Link>

                <Link to="/history">History</Link>

            </div>

        </nav>

    );

}

export default Navbar;