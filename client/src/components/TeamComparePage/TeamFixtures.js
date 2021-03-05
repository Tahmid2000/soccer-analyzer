import React from "react";
import TeamFixture from "./TeamFixture";

class TeamFixtures extends React.Component {
  render() {
    return (
      <React.Fragment>
        <h4>{this.props.name}</h4>
        <div className="row">
            <TeamFixture 
                teamFixture={this.props.teamFixtures}
            />
            {/* {this.props.teamFixtures.map(() => {
                return (
                    <TeamFixture 
                        teamFixture={this.props.teamFixtures}
                    />
                );
            })}  */}
        </div>
      </React.Fragment>
    );
  }
}

export default TeamFixtures;