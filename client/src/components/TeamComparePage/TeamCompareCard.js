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
            </div>
        );
    }
}

export default TeamCompareCard;