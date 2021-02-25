import React from "react";
import moment from "moment";
class PlayerCompareCard extends React.Component {
  calculateAge = birthday => {
    // birthday is a date
    var ageDifMs = Date.now() - birthday.getTime();
    var ageDate = new Date(ageDifMs); // miliseconds from epoch
    return Math.abs(ageDate.getUTCFullYear() - 1970);
  };
  render() {
    return (
      <div className="card">
        <div className="card-image">
          <img
            src={this.props.player.image_path}
            alt={this.props.player.player_name}
          />
        </div>
        <div className="card-content center-align">
          {this.props.player.player_name.length > 25 ? (
            <span className="card-title truncate">
              <strong>{this.props.player.player_name}</strong>
            </span>
          ) : (
            <span className="card-title">
              <strong>{this.props.player.player_name}</strong>
            </span>
          )}
          <p>
            <i>{this.props.player.position}</i>
          </p>
          <p>
            <i>
              {this.props.player.team_name} and {this.props.player.nationality}
            </i>
          </p>
          <p>
            <i>
              {moment().diff(moment(this.props.player.birthdate), "years")}{" "}
              years old
            </i>
          </p>
          <p>
            <i>
              {this.props.player.height} inches --- {this.props.player.weight}{" "}
              pounds
            </i>
          </p>
        </div>
      </div>
    );
  }
}
/* <p>
  <i>Country ID: {this.props.player.country_id}</i>
</p> */
export default PlayerCompareCard;
