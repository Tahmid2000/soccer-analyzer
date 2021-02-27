import React from "react";
import { selectTeam } from "../../actions";
import { connect } from "react-redux";
class TeamCard extends React.Component {
    render() {
        return (
            <div className="card">
                <div className="card-image">
                    <img src={this.props.image_path} alt={this.props.team_name} />
                    <button
                        className={`btn-floating halfway-fab waves-effect ${
                        this.props.selectedTeams.length === 2 ? "disabled" : ""
                        }`}
                        style={{ color: "#2d6a4f" }}
                        title="Select for Comparison"
                        onClick={() => this.props.selectTeam(this.props.team)}
                    >
                        <i className="material-icons">add</i>
                    </button>
                </div>
                <div className="card-content">
                    {this.props.team_name.length > 25 ? (
                        <span className="card-title truncate">
                            {this.props.team_name}
                        </span>
                    ) : (
                    <span className="card-title">{this.props.team_name}</span>
                )}
                </div>
            </div>
        );
    }   
}
const mapStateToProps = state => {
    return { selectedTeams: state.selectedTeams };
  };
  export default connect(mapStateToProps, { selectTeam })(TeamCard);