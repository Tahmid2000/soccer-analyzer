import React from "react";

class TeamCompareCard extends React.Component {
    render() {
        return (
            <div className="card">
                <div className="card-image">
                    <img 
                        src={this.props.team.image_path}
                        alt={this.props.team.team_name}
                    />
                </div>
                <div className="card-content center-align">
                    <span className="card-title">
                    <strong>{this.props.team.team_name}</strong>
                    </span>
                    <p>
                        <i>{this.props.team.country}</i>
                    </p>
                    <p>
                        <i>{this.props.team.venue_name}</i>
                    </p>
                    <p>
                        <i>Founded {this.props.team.founded}</i>
                    </p>
                </div>
            </div>
        );
    }
}

export default TeamCompareCard;