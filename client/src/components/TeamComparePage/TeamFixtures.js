import React from "react";

class TeamFixtures extends React.Component {
  render() {
    return (
      <React.Fragment>
        <h4>{this.props.name}</h4>
        
        <div className="row">
            <div className="col s2">
            {this.props.teamFixtures.map((index) => {
                console.log(this.props.teamFixtures[index]);
                // return <li >{this.props.teamFixtures[index]}</li>
            }).score}
            </div>
            <div className="col s3">
                <img src={this.props.teamFixtures[0].home_logo} />
            </div>
            <div className="col s2">
                <h3>{this.props.teamFixtures[0].score}</h3>
            </div>
            <div className="col s3">
                <img src={this.props.teamFixtures[0].away_logo} />
            </div>
            <div className="col s2"></div>
        </div>
      </React.Fragment>
    );
  }
}

export default TeamFixtures;