import React from "react";

class TeamFixture extends React.Component {
  render() {
    return (
      <React.Fragment>
        <div className="row">
          <div className="col s4">
            <img
              className="responsive-img"
              src={this.props.fixture.home_logo}
            />
          </div>
          <div className="col s4">
            <h4>{this.props.fixture.score}</h4>
          </div>
          <div className="col s4">
            <img
              className="responsive-img"
              src={this.props.fixture.away_logo}
            />
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default TeamFixture;
