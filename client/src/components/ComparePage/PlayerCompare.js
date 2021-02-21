import React from "react";
import analyzer from "../../apis/analyzer";
import LoadingCircle from "../LoadingCircle";
import PlayerCompareCard from "./PlayerComapreCard";
import Statistics from "./Statistics";
import { Link } from "react-router-dom";
class PlayerCompare extends React.Component {
  state = { playerOne: [], playerTwo: [], loading: true };
  componentDidMount() {
    this.getData();
  }

  getData = async () => {
    const response1 = await analyzer.get(
      `/player/stats/${this.props.match.params.id1}`
    );
    const response2 = await analyzer.get(
      `/player/stats/${this.props.match.params.id2}`
    );
    this.setState({
      playerOne: response1.data,
      playerTwo: response2.data,
      loading: false
    });
  };
  renderContent() {
    console.log(this.state.playerTwo.graph_path);
    return (
      <React.Fragment>
        <h1 className="center-align">
          {`${this.state.playerOne.player_name} vs. ${this.state.playerTwo.player_name}`}
        </h1>
        <div className="row">
          <div className="col s1"></div>
          <div className="col s3">
            <PlayerCompareCard player={this.state.playerOne} />
            <img
              style={{ marginLeft: "-80px" }}
              src={this.state.playerOne.graph_path}
              alt=""
            />
          </div>
          <div className="col s4">
            <Statistics
              playerOne={this.state.playerOne}
              playerTwo={this.state.playerTwo}
            />
          </div>
          <div className="col s3">
            <PlayerCompareCard player={this.state.playerTwo} />
            <img
              style={{ marginLeft: "-80px" }}
              src={this.state.playerTwo.graph_path}
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

/* <div className="row">
  <div className="col s5 offset-s1">
    <img src={this.state.playerOne.image_path} alt="" />
    <p>Nationality: {this.state.playerOne.nationality}</p>
    <p>Birth Date: {this.state.playerOne.birthdate}</p>
    <p>Height: {this.state.playerOne.height}</p>
    <p>Weight: {this.state.playerOne.weight}</p>
    <p>Appearances: {this.state.playerOne.appearances}</p>
    <p>Goals: {this.state.playerOne.goals}</p>
    <p>Assists: {this.state.playerOne.assists}</p>
    <p>Total Passes: {this.state.playerOne.total_passes}</p>
    <p>Clean Sheets: {this.state.playerOne.clean_sheets}</p>
    <p>Penalties Saved: {this.state.playerOne.penalties_saved}</p>
    <p>Yellow Cards: {this.state.playerOne.yellow_cards}</p>
    <p>Red Cards: {this.state.playerOne.red_cards}</p>
    <p>Clean Sheets: {this.state.playerOne.clean_sheets}</p>
    <p>Country Id: {this.state.playerOne.country_id}</p>
    <p>Fouls Committed: {this.state.playerOne.fouls_committed}</p>
    <p>Pass accuracy: {this.state.playerOne.pass_accuracy}</p>
    <p>Position Id: {this.state.playerOne.position_id}</p>
    <p>Saves: {this.state.playerOne.saves}</p>
    <p>Tackles: {this.state.playerOne.tackles}</p>
    <p>Team Id: {this.state.playerOne.team_id}</p>
  </div>
  <div className="col s1 offset-s5">
    <img src={this.state.playerTwo.image_path} alt="" />
    <p>Nationality: {this.state.playerTwo.nationality}</p>
    <p>Birth Date: {this.state.playerTwo.birthdate}</p>
    <p>Height: {this.state.playerTwo.height}</p>
    <p>Weight: {this.state.playerTwo.weight}</p>
    <p>Appearances: {this.state.playerTwo.appearances}</p>
    <p>Goals: {this.state.playerTwo.goals}</p>
    <p>Assists: {this.state.playerTwo.assists}</p>
    <p>Total Passes: {this.state.playerTwo.total_passes}</p>
    <p>Clean Sheets: {this.state.playerTwo.clean_sheets}</p>
    <p>Penalties Saved: {this.state.playerTwo.penalties_saved}</p>
    <p>Yellow Cards: {this.state.playerTwo.yellow_cards}</p>
    <p>Red Cards: {this.state.playerTwo.red_cards}</p>
    <p>Clean Sheets: {this.state.playerTwo.clean_sheets}</p>
    <p>Country Id: {this.state.playerTwo.country_id}</p>
    <p>Fouls Committed: {this.state.playerTwo.fouls_committed}</p>
    <p>Pass accuracy: {this.state.playerTwo.pass_accuracy}</p>
    <p>Position Id: {this.state.playerTwo.position_id}</p>
    <p>Saves: {this.state.playerTwo.saves}</p>
    <p>Tackles: {this.state.playerTwo.tackles}</p>
    <p>Team Id: {this.state.playerTwo.team_id}</p>
  </div>
</div>; */

export default PlayerCompare;
