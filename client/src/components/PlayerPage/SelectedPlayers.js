import React from "react";
import { connect } from "react-redux";
import { removePlayer } from "../../actions";
import { Link } from "react-router-dom";
class SelectedPlayers extends React.Component {
  compareButton = () => {
    if (this.props.selectedPlayers.length == 2) {
      return (
        <Link
          to={`/compare/player/${this.props.selectedPlayers[0].player_id}/${this.props.selectedPlayers[1].player_id}`}
          exact
        >
          <div className="center-align">
            <a
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
    const renderedList = this.props.selectedPlayers.map(player => {
      /* <img src={player.image_path} alt={player.player_name} />; */
      return (
        <li>
          <div class="collapsible-header">
            {player.player_name}
            <span class="badge">
              <div
                style={{ color: "red" }}
                onClick={() => this.props.removePlayer(player)}
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
        {this.props.selectedPlayers.length === 0 ? (
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
  return { selectedPlayers: state.selectedPlayers };
};

export default connect(mapStateToProps, { removePlayer })(SelectedPlayers);
