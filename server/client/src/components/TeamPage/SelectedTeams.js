import React from "react";
import { connect } from "react-redux";
import { removeTeam } from "../../actions";
import { Link } from "react-router-dom";
class SelectedTeams extends React.Component {
  compareButton = () => {
    if (this.props.selectedTeams.length === 2) {
      return (
        <Link
          to={`/compare/team/${this.props.selectedTeams[0].team_id}/${this.props.selectedTeams[1].team_id}`}
          exact
        >
          <div className="center-align">
            <a
              href="/#"
              className="waves-effect waves-light btn-large"
              style={{ backgroundColor: "#40916c", color: "white" }}
            >
              <strong>COMPARE</strong>
            </a>
          </div>
        </Link>
      );
    }
    return "";
  };
  render() {
    const renderedList = this.props.selectedTeams.map(team => {
      return (
        <li>
          <div class="collapsible-header">
            {team.team_name}
            <span class="badge">
              <div
                style={{ color: "red" }}
                onClick={() => this.props.removeTeam(team)}
              >
                Remove
              </div>
            </span>
          </div>
        </li>
      );
    });

    return (
      <React.Fragment>
        {this.props.selectedTeams.length === 0 ? (
          ""
        ) : (
          <React.Fragment>
            <div className="container">
              <ul class="collapsible">{renderedList}</ul>
            </div>

            {this.compareButton()}
          </React.Fragment>
        )}
      </React.Fragment>
    );
  }
}

const mapStateToProps = state => {
  return { selectedTeams: state.selectedTeams };
};

export default connect(mapStateToProps, { removeTeam })(SelectedTeams);
