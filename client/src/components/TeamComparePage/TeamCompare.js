import React from "react";
import analyzer from "../../apis/analyzer";
import TeamCompareCard from "./TeamCompareCard";
import TeamStatistics from "./TeamStatistics";
import { clearTeams } from "../../actions";
import { connect } from "react-redux";

class TeamCompare extends React.Component {
  state = { team1: [], team2: [], stats: [], fixtures: [], loading: true };
  componentDidMount() {
    this.getData();
    this.props.clearTeams();
  }

  getData = async () => {
    const response = await analyzer.get(
      `/teams/h2h/${this.props.match.params.id1}/${this.props.match.params.id2}`
    );
    this.setState({
      team1: response.data.data.team1,
      team2: response.data.data.team2,
      stats: response.data.data.stats,
      fixtures: response.data.data.fixtures,
      loading: false
    });
  };
  render() {
    return (
      <React.Fragment>
        <h1 className="center-align">
          {`${this.state.team1.team_name} vs. ${this.state.team2.team_name}`}
        </h1>
        <div className="row">
            <div className="col s1"></div>
            <div className="col c3 m3">
                <TeamCompareCard team={this.state.team1}/>
            </div>
            <div className="col s4">
                <TeamStatistics 
                    teams={this.state.stats}
                />
            </div>
            <div className="col s3 m3">
                <TeamCompareCard team={this.state.team2}/>
            </div>
            <div className="col s1"></div>
        </div>
      </React.Fragment>
    );
  }
}
const mapStateToProps = state => {
  return {};
};
export default connect(mapStateToProps, { clearTeams })(TeamCompare);
