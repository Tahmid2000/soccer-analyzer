import React from "react";
import TeamSearchBar from "./TeamSearchBar";
import TeamList from "./TeamList";
import LoadingLine from "../LoadingLine";
import SelectedTeams from "./SelectedTeams";
import { fetchTeams } from "../../actions";
import { connect } from "react-redux";
class TeamPage extends React.Component {
  state = {
    loading: false,
    searched: false
  };
  searchFunction = async term => {
    this.setState({ loading: true });
    this.props
      .fetchTeams(term)
      .then(() => this.setState({ loading: false, searched: true }));
  };

  renderSearch = () => {
    if (this.state.searched) {
      if (this.props.teams.length === 0) return "No results found.";
    }
    return <TeamList teams={this.props.teams} />;
  };
  render() {
    return (
      <div className="container">
        <h1 className="center-align">Compare Teams</h1>
        <SelectedTeams />
        <TeamSearchBar onSubmit={this.searchFunction} />
        {this.state.loading === true ? <LoadingLine /> : this.renderSearch()}
      </div>
    );
  }
}
const mapStateToProps = state => {
  return { teams: state.teams };
};
export default connect(mapStateToProps, { fetchTeams })(TeamPage);
