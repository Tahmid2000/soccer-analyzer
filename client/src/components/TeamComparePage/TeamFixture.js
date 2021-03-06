import React from "react";

class TeamFixture extends React.Component {
  render() {
    return (
      <React.Fragment>
        <div className="row hoverable" style={{margin : '1em'}}>
          <div className="col s4" style={{padding : '1em'}}>
            <img
              className="responsive-img"
              src={this.props.fixture.home_logo}
            />
          </div>
          <div className="col s4" style={{padding : '1em'}}>
            <h4>{!this.props.fixture.score ? this.props.fixture.status : this.props.fixture.score}</h4>
            <h6><i>{this.props.fixture.league}</i></h6>
            <h6><i>{this.props.fixture.date.substring(0,10)}</i></h6>

          </div>
          <div className="col s4" style={{padding : '1em'}}>
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
