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
    console.log(this.state.playerOne.clicks);
    console.log(this.state.playerTwo.clicks);
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
              className="responsive-img"
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
              className="responsive-img"
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

export default PlayerCompare;
