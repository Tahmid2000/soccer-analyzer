import React from "react";
import analyzer from "../../apis/analyzer";
import LoadingCircle from "../LoadingCircle";
import PlayerCompareCard from "./PlayerCompareCard";
import Statistics from "./Statistics";
import { clearPlayers } from "../../actions";
import { connect } from "react-redux";
class PlayerCompare extends React.Component {
  state = {
    playerOne: [],
    playerTwo: [],
    loading: true,
    width: window.innerWidth,
    error: false
  };

  handleResize = () => {
    this.setState({ width: window.innerWidth });
  };
  componentDidMount() {
    window.addEventListener("resize", this.handleResize);
    this.getData();
    this.props.clearPlayers();
  }

  getData = async () => {
    try {
      const response1 = await analyzer.get(
        `/player/stats/${this.props.match.params.id1}`
      );
      const response2 = await analyzer.get(
        `/player/stats/${this.props.match.params.id2}`
      );
      this.setState({
        playerOne: response1.data,
        playerTwo: response2.data,
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
    if (this.state.width <= 600) {
      return (
        <React.Fragment>
          <h1 className="center-align">
            {`${this.state.playerOne.player_name} vs. ${this.state.playerTwo.player_name}`}
          </h1>
          <div className="row">
            <div className="col s12 m1"></div>
            <div className="col s12 m3">
              <PlayerCompareCard player={this.state.playerOne} />
              <img
                className="responsive-img"
                src={this.state.playerOne.graph_path}
                alt=""
              />
            </div>
            <div className="col s12 m3">
              <PlayerCompareCard player={this.state.playerTwo} />
              <img
                className="responsive-img"
                src={this.state.playerTwo.graph_path}
                alt=""
              />
            </div>
            <div className="col s12 m4">
              <Statistics
                playerOne={this.state.playerOne}
                playerTwo={this.state.playerTwo}
              />
            </div>
            <div className="col s12 m1"></div>
          </div>
        </React.Fragment>
      );
    }
    return (
      <React.Fragment>
        <h1 className="center-align">
          {`${this.state.playerOne.player_name} vs. ${this.state.playerTwo.player_name}`}
        </h1>
        <div className="row">
          <div className="col s12 m1"></div>
          <div className="col s12 m3">
            <PlayerCompareCard player={this.state.playerOne} />
            <img
              src={this.state.playerOne.graph_path}
              alt=""
              className="responsive-img"
            />
          </div>
          <div className="col s12 m4">
            <Statistics
              playerOne={this.state.playerOne}
              playerTwo={this.state.playerTwo}
            />
          </div>
          <div className="col s12 m3">
            <PlayerCompareCard player={this.state.playerTwo} />
            <img
              src={this.state.playerTwo.graph_path}
              alt=""
              className="responsive-img"
            />
          </div>
          <div className="col s12 m1"></div>
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
export default connect(mapStateToProps, { clearPlayers })(PlayerCompare);
