import React from "react";
import { Link } from "react-router-dom";
import M from "materialize-css";
class NavBar extends React.Component {
  componentDidMount() {
    M.AutoInit();
  }
  render() {
    return (
      <React.Fragment>
        <nav style={{ backgroundColor: "#2d6a4f" }}>
          <div class="nav-wrapper">
            <div className="container">
              <Link to="/" class="brand-logo">
                Clasico
              </Link>
              <a href="/#" data-target="mobile-demo" class="sidenav-trigger">
                <i class="material-icons">menu</i>
              </a>
              <ul
                id="nav-mobile"
                class="right hide-on-med-and-down"
                ref={sidenav => {
                  this.sidenav = sidenav;
                }}
              >
                <li>
                  <Link to="/">Home</Link>
                </li>
                <li>
                  <Link to="/players">Players</Link>
                </li>
                <li>
                  <Link to="/teams">Teams</Link>
                </li>
                <li>
                  <Link to="/about">About Us</Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>
        <ul class="sidenav" id="mobile-demo">
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/players">Players</Link>
          </li>
          <li>
            <Link to="/teams">Teams</Link>
          </li>
          <li>
            <Link to="/about">About Us</Link>
          </li>
        </ul>
      </React.Fragment>
    );
  }
}

export default NavBar;
