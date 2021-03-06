import React from "react";
import TeamFixture from "./TeamFixture";

class TeamFixtures extends React.Component {
  render() {
    const renderedList = this.props.fixtures.map(fixture => {
      return <TeamFixture fixture={fixture} />;
    });
    return (
      <React.Fragment>
        <h4>Fixtures</h4>
        <div className="row">
            {renderedList}
        </div>
      </React.Fragment>
    );
  }
}

export default TeamFixtures;
