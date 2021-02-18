import React from "react";
import StatisticComparison from "./StatisticComparison";
import "./Statistics.css";
class Statistics extends React.Component {
  state = { quality: "attacking", type: "total" };
  typeSelector = (stat, appearances) => {
    if (this.state.type === "total") return stat;
    return (stat / appearances).toFixed(3);
  };
  renderContent = () => {
    if (this.state.quality === "attacking") {
      return (
        <React.Fragment>
          <StatisticComparison
            stat="Appearances"
            playerOneStat={this.typeSelector(
              this.props.playerOne.appearances,
              this.props.playerOne.appearances
            )}
            playerTwoStat={this.typeSelector(
              this.props.playerTwo.appearances,
              this.props.playerTwo.appearances
            )}
            type=">"
          />
          <StatisticComparison
            stat="Goals"
            playerOneStat={this.typeSelector(
              this.props.playerOne.goals,
              this.props.playerOne.appearances
            )}
            playerTwoStat={this.typeSelector(
              this.props.playerTwo.goals,
              this.props.playerTwo.appearances
            )}
            type=">"
          />
          <StatisticComparison
            stat="Assists"
            playerOneStat={this.typeSelector(
              this.props.playerOne.assists,
              this.props.playerOne.appearances
            )}
            playerTwoStat={this.typeSelector(
              this.props.playerTwo.assists,
              this.props.playerTwo.appearances
            )}
            type=">"
          />
          <StatisticComparison
            stat="Pass Accuracy"
            playerOneStat={(this.props.playerOne.pass_accuracy / 100).toFixed(
              3
            )}
            playerTwoStat={(this.props.playerTwo.pass_accuracy / 100).toFixed(
              3
            )}
            type=">"
          />
          <StatisticComparison
            stat="Total Passes"
            playerOneStat={this.typeSelector(
              this.props.playerOne.total_passes,
              this.props.playerOne.appearances
            )}
            playerTwoStat={this.typeSelector(
              this.props.playerTwo.total_passes,
              this.props.playerTwo.appearances
            )}
            type=">"
          />
          <StatisticComparison
            stat="Crosses"
            playerOneStat={this.typeSelector(
              this.props.playerOne.key_passes,
              this.props.playerOne.appearances
            )}
            playerTwoStat={this.typeSelector(
              this.props.playerTwo.key_passes,
              this.props.playerTwo.appearances
            )}
            type=">"
          />
          <StatisticComparison
            stat="Dribbles / Attempted"
            playerOneStat={this.props.playerOne.dribble_ratio.toFixed(3)}
            playerTwoStat={this.props.playerTwo.dribble_ratio.toFixed(3)}
            type=">"
          />
          <StatisticComparison
            stat="Total Dribbles"
            playerOneStat={this.typeSelector(
              this.props.playerOne.successful_dribbles,
              this.props.playerOne.appearances
            )}
            playerTwoStat={this.typeSelector(
              this.props.playerTwo.successful_dribbles,
              this.props.playerTwo.appearances
            )}
            type=">"
          />
          <StatisticComparison
            stat="Crosses / Attempted"
            playerOneStat={this.props.playerOne.cross_ratio.toFixed(3)}
            playerTwoStat={this.props.playerTwo.cross_ratio.toFixed(3)}
            type=">"
          />
          <StatisticComparison
            stat="Total Crosses"
            playerOneStat={this.typeSelector(
              this.props.playerOne.successful_crosses,
              this.props.playerOne.appearances
            )}
            playerTwoStat={this.typeSelector(
              this.props.playerTwo.successful_crosses,
              this.props.playerTwo.appearances
            )}
            type=">"
          />
        </React.Fragment>
      );
    } else if (this.state.quality === "defending") {
      return (
        <React.Fragment>
          <StatisticComparison
            stat="Appearances"
            playerOneStat={this.typeSelector(
              this.props.playerOne.appearances,
              this.props.playerOne.appearances
            )}
            playerTwoStat={this.typeSelector(
              this.props.playerTwo.appearances,
              this.props.playerTwo.appearances
            )}
            type=">"
          />
          <StatisticComparison
            stat="Tackles"
            playerOneStat={this.typeSelector(
              this.props.playerOne.tackles,
              this.props.playerOne.appearances
            )}
            playerTwoStat={this.typeSelector(
              this.props.playerTwo.tackles,
              this.props.playerTwo.appearances
            )}
            type=">"
          />
          <StatisticComparison
            stat="Clean Sheets"
            playerOneStat={this.typeSelector(
              this.props.playerOne.clean_sheets,
              this.props.playerOne.appearances
            )}
            playerTwoStat={this.typeSelector(
              this.props.playerTwo.clean_sheets,
              this.props.playerTwo.appearances
            )}
            type=">"
          />
          <StatisticComparison
            stat="Duels / Attempted"
            playerOneStat={this.props.playerOne.duels_ratio.toFixed(3)}
            playerTwoStat={this.props.playerTwo.duels_ratio.toFixed(3)}
            type=">"
          />
          <StatisticComparison
            stat="Total Duels"
            playerOneStat={this.typeSelector(
              this.props.playerOne.successful_duels,
              this.props.playerOne.appearances
            )}
            playerTwoStat={this.typeSelector(
              this.props.playerTwo.successful_duels,
              this.props.playerTwo.appearances
            )}
            type=">"
          />
          <StatisticComparison
            stat="Fouls Committed"
            playerOneStat={this.typeSelector(
              this.props.playerOne.fouls_committed,
              this.props.playerOne.appearances
            )}
            playerTwoStat={this.typeSelector(
              this.props.playerTwo.fouls_committed,
              this.props.playerTwo.appearances
            )}
            type="<"
          />
          <StatisticComparison
            stat="Yellow Cards"
            playerOneStat={this.typeSelector(
              this.props.playerOne.yellow_cards,
              this.props.playerOne.appearances
            )}
            playerTwoStat={this.typeSelector(
              this.props.playerTwo.yellow_cards,
              this.props.playerTwo.appearances
            )}
            type="<"
          />
          <StatisticComparison
            stat="Red Cards"
            playerOneStat={this.typeSelector(
              this.props.playerOne.red_cards,
              this.props.playerOne.appearances
            )}
            playerTwoStat={this.typeSelector(
              this.props.playerTwo.red_cards,
              this.props.playerTwo.appearances
            )}
            type="<"
          />
        </React.Fragment>
      );
    } else {
      return (
        <React.Fragment>
          <StatisticComparison
            stat="Appearances"
            playerOneStat={this.typeSelector(
              this.props.playerOne.appearances,
              this.props.playerOne.appearances
            )}
            playerTwoStat={this.typeSelector(
              this.props.playerTwo.appearances,
              this.props.playerTwo.appearances
            )}
            type=">"
          />
          <StatisticComparison
            stat="Clean Sheets"
            playerOneStat={this.typeSelector(
              this.props.playerOne.clean_sheets,
              this.props.playerOne.appearances
            )}
            playerTwoStat={this.typeSelector(
              this.props.playerTwo.clean_sheets,
              this.props.playerTwo.appearances
            )}
            type=">"
          />
          <StatisticComparison
            stat="Saves"
            playerOneStat={this.typeSelector(
              this.props.playerOne.saves,
              this.props.playerOne.appearances
            )}
            playerTwoStat={this.typeSelector(
              this.props.playerTwo.saves,
              this.props.playerTwo.appearances
            )}
            type=">"
          />
          <StatisticComparison
            stat="Penalties Saved"
            playerOneStat={this.typeSelector(
              this.props.playerOne.penalties_saved,
              this.props.playerOne.appearances
            )}
            playerTwoStat={this.typeSelector(
              this.props.playerTwo.penalties_saved,
              this.props.playerTwo.appearances
            )}
            type=">"
          />
        </React.Fragment>
      );
    }
    return "";
  };
  render() {
    return (
      <div className="center-align">
        <div className="row">
          <div className="col s12">
            <ul className="tabs">
              <li className="tab col s4">
                <a
                  className={this.state.quality === "attacking" ? "active" : ""}
                  href="#attacking"
                  onClick={() => this.setState({ quality: "attacking" })}
                >
                  Attacking
                </a>
              </li>
              <li className="tab col s4">
                <a
                  className={this.state.quality === "defending" ? "active" : ""}
                  href="#defending"
                  onClick={() => this.setState({ quality: "defending" })}
                >
                  Defending
                </a>
              </li>
              <li className="tab col s4">
                <a
                  className={
                    this.state.quality === "goalkeeping" ? "active" : ""
                  }
                  href="#goalkeeping"
                  onClick={() => this.setState({ quality: "goalkeeping" })}
                >
                  Goalkeeping
                </a>
              </li>
            </ul>
          </div>
        </div>
        <div className="row">
          <div className="col s12">
            <ul className="tabs">
              <li className="tab col s6">
                <a
                  className={this.state.type === "total" ? "active" : ""}
                  href="#total"
                  onClick={() => this.setState({ type: "total" })}
                >
                  Total
                </a>
              </li>
              <li className="tab col s6">
                <a
                  className={this.state.type === "per_game" ? "active" : ""}
                  href="#pergame"
                  onClick={() => this.setState({ type: "per_game" })}
                >
                  Per Game
                </a>
              </li>
            </ul>
          </div>
        </div>
        {this.renderContent()}
      </div>
    );
  }
}

export default Statistics;
