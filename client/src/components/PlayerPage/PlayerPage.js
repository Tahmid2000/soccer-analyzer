import React from "react";
import SearchBar from "../SearchBar";
import PlayerList from "./PlayerList";
import Loading from "../Loading";
import { fetchPlayers } from "../../actions";
import { connect } from "react-redux";
class PlayerPage extends React.Component {
  state = {
    loading: false,
    searched: false
  };
  searchFunction = async term => {
    this.setState({ loading: true });
    this.props
      .fetchPlayers(term)
      .then(() => this.setState({ loading: false, searched: true }));
  };

  renderSearch = () => {
    if (this.state.searched) {
      if (this.props.players.length === 0) return "No results found.";
    }
    return <PlayerList players={this.props.players} />;
  };
  render() {
    return (
      <div className="container">
        <h1>Player</h1>
        <SearchBar onSubmit={this.searchFunction} />
        {this.state.loading === true ? <Loading /> : this.renderSearch()}
      </div>
    );
  }
}
const mapStateToProps = state => {
  return { players: state.players };
};
export default connect(mapStateToProps, { fetchPlayers })(PlayerPage);
