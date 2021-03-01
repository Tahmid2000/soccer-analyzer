import React from "react";
import TeamCard from "./TeamCard";
// import "./TeamList.css";
class TeamList extends React.Component {
  render() {
    const renderedList = this.props.teams.map(team => {
      return (
        <div class="col s12 m6 l4">
          <TeamCard
            key={team.team_id}
            team_id={team.team_id}
            image_path={team.image_path}
            team_name={team.team_name}
            team={team}
          />
        </div>
      );
    });

    return (
      <React.Fragment>
        <div class="row">{renderedList}</div>
      </React.Fragment>
    );
  }
}
export default TeamList;
