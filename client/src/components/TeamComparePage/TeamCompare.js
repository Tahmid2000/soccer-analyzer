import React from "react";
import analyzer from "../../apis/analyzer";
import TeamCompareCard from "./TeamCompareCard";
import TeamStatistics from "./TeamStatistics";
import LoadingCircle from "../LoadingCircle";
import { clearTeams } from "../../actions";
import { connect } from "react-redux";

class TeamCompare extends React.Component {
  state = {
    team1: [],
    team2: [],
    stats: [],
    fixtures: [],
    loading: true,
    error: false
  };
  componentDidMount() {
    this.getData();
    this.props.clearTeams();
  }

  getData = async () => {
    try {
      const response = await analyzer.get(
        `/teams/h2h/${this.props.match.params.id1}/${this.props.match.params.id2}`
      );
      this.setState({
        team1: response.data.data.team1,
        team2: response.data.data.team2,
        stats: response.data.data.stats,
        fixtures: response.data.data.fixtures,
        loading: false,
        error: false
      });
    } catch (err) {
      this.setState({ error: true });
    }
  };
  renderContent() {
    if (this.state.error)
      return (
        <React.Fragment>
          <h1>An error has occured.</h1>
        </React.Fragment>
      );
    return (
      <React.Fragment>
        <h1 className="center-align">
          {`${this.state.team1.team_name} vs. ${this.state.team2.team_name}`}
        </h1>
        <div className="row">
          <div className="col s1"></div>
          <div className="col s3 m3">
            <TeamCompareCard team={this.state.team1} />
            <img
              className="responsive-img"
              src={this.state.stats.id1_graph_path}
              alt=""
            />
          </div>
          <div className="col s4">
            <TeamStatistics teams={this.state.stats} />
          </div>
          <div className="col s3 m3">
            <TeamCompareCard team={this.state.team2} />
            <img
              className="responsive-img"
              src={this.state.stats.id2_graph_path}
              alt=""
            />
          </div>
          <div className="col s1"></div>
        </div>
      </React.Fragment>
    );
  }
  render() {
    return (
      <React.Fragment>
        {this.state.loading === true ? (
          <div className="mt-5" style={{ marginTop: "100px" }}>
            <LoadingCircle />
          </div>
        ) : (
          this.renderContent()
        )}
      </React.Fragment>
    );
  }
}
const mapStateToProps = state => {
  return {};
};
export default connect(mapStateToProps, { clearTeams })(TeamCompare);
