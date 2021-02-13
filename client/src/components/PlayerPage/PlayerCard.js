import React from "react";

class PlayerCard extends React.Component {
  render() {
    return (
      <div className="card">
        <div className="card-image">
          <img src={this.props.image_path} alt={this.props.player_name} />

          <a
            className="btn-floating halfway-fab waves-effect waves-light red"
            title="Select for Comparison"
          >
            <i className="material-icons">add</i>
          </a>
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

export default PlayerCard;
