import React from "react";
import { selectPlayer } from "../../actions";
import { connect } from "react-redux";
class PlayerCard extends React.Component {
  render() {
    return (
      <div className="card">
        <div className="card-image">
          <img src={this.props.image_path} alt={this.props.player_name} />
          <button
            className={`btn-floating halfway-fab waves-effect ${
              this.props.selectedPlayers.length === 2 ? "disabled" : ""
            }`}
            style={{ color: "#2d6a4f" }}
            title="Select for Comparison"
            onClick={() => this.props.selectPlayer(this.props.player)}
          >
            <i className="material-icons">add</i>
          </button>
        </div>
        <div className="card-content">
          {this.props.player_name.length > 25 ? (
            <span className="card-title" style={{ fontSize: "140%" }}>
              {this.props.player_name}
            </span>
          ) : (
            <span className="card-title">{this.props.player_name}</span>
          )}
        </div>
      </div>
    );
  }
}
const mapStateToProps = state => {
  return { selectedPlayers: state.selectedPlayers };
};
export default connect(mapStateToProps, { selectPlayer })(PlayerCard);
