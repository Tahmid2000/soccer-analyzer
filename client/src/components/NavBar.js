import React from 'react'
import { Link } from "react-router-dom";
class NavBar extends React.Component {
    render() {
        return (
            <React.Fragment>
                <nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
                    <div class="container">
                        <Link class="navbar-brand" to="/">
                            Fútbol Analyzer
                        </Link>
                        <button class="navbar-toggler" type="button" data-mdb-toggle="collapse"
                            data-mdb-target="#navbarRightAlignExample" aria-controls="navbarRightAlignExample" aria-expanded="false"
                            aria-label="Toggle navigation">
                            <i class="fas fa-bars"></i>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarRightAlignExample">
                            <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                                <li class="nav-item">
                                    <Link class="nav-link active" aria-current="page" to="#">Home</Link>
                                </li>
                                <li class="nav-item">
                                    <Link class="nav-link" to="/players">Players</Link>
                                </li>
                                <li class="nav-item">
                                    <Link class="nav-link" to="/teams">Teams</Link>
                                </li>
                                <li class="nav-item">
                                    <Link class="nav-link" to="/about">About Us</Link>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>
                <div style={{ marginTop: "75px" }}></div>
            </React.Fragment>)
    }
}

export default NavBar