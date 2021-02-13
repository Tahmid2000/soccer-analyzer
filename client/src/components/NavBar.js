import React from 'react'
import { Link } from "react-router-dom";
//import M from 'materialize-css';
class NavBar extends React.Component {
    render() {
        return (
            <React.Fragment>
                <nav>
                    <div class="nav-wrapper">
                        <div className="container">
                            <Link to="#" class="brand-logo">Fútbol Analyzer</Link>
                            <ul id="nav-mobile" class="right hide-on-med-and-down">
                                <li><Link to="/">Home</Link></li>
                                <li><Link to="/players">Players</Link></li>
                                <li><Link to="/teams">Teams</Link></li>
                                <li><Link to="/about">About Us</Link></li>
                            </ul>
                        </div>
                    </div>
                </nav>
            </React.Fragment>)
    }
}

export default NavBar