import React from "react";
import Image from "./Image";
import { Link } from "react-router-dom";
class HomePage extends React.Component {
  render() {
    return (
      <React.Fragment>
        <div id="index-banner" class="parallax-container">
          <div class="section no-pad-bot">
            <div class="container">
              <br />
              <br />
              <br />
              <br />
              <h1 class="header center black-text text-darken-3">Clasico</h1>
              <div class="row center">
                <h4 class="header col s12 black-text text-darken-3">
                  Analyze statistics between any 2 players or teams
                </h4>
              </div>
            </div>
          </div>
          <div class="parallax">
            <Image link="/cover.webp" />
          </div>
        </div>
        <div class="container">
          <div class="section">
            <div class="row">
              <div class="col s12 m6">
                <div class="icon-block">
                  <h2 class="center">
                    <i class="material-icons">directions_run</i>
                  </h2>
                  <h5 class="center">Compare Players</h5>

                  <p class="light center">
                    Compare various statistics between your favorite players
                    from attackers to goalkeepers. Visualize quantitative data
                    numerically and in graph form.
                  </p>
                  <Link to="/players" exact>
                    <div className="center-align">
                      <button
                        className="waves-effect waves-light btn-large"
                        style={{ backgroundColor: "#40916c", color: "white" }}
                      >
                        <strong>Take me there</strong>
                      </button>
                    </div>
                  </Link>
                </div>
              </div>

              <div class="col s12 m6">
                <div class="icon-block">
                  <h2 class="center">
                    <i class="material-icons">group</i>
                  </h2>
                  <h5 class="center">Compare Teams</h5>
                  <p class="light center">
                    Compare various statistics between your favorite teams to
                    see who really holds the crown. Visualize quantitative data
                    numerically and in graph form.
                  </p>
                  <Link to="/teams" exact>
                    <div className="center-align">
                      <button
                        className="waves-effect waves-light btn-large"
                        style={{ backgroundColor: "#40916c", color: "white" }}
                      >
                        <strong>Take me there</strong>
                      </button>
                    </div>
                  </Link>
                </div>
              </div>
            </div>
          </div>
          <br />
          <br />
        </div>

        <div class="parallax-container valign-wrapper">
          <div class="section no-pad-bot">
            <div class="container">
              <div class="row center"></div>
            </div>
          </div>
          <div class="parallax">
            <Image link="stadium.webp" />
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default HomePage;
