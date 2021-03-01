import React from "react";
import TeamStatisticComparison from "./TeamStatisticComparison";

class TeamStatistics extends React.Component {
    state = { quality: "total", type: "statistics" };
    totalCalculate = (home, away) => {
        return (home + away);
    };
    renderContent = () => {
        if (this.state.quality === "total") {
            return (
                <React.Fragment>
                    <TeamStatisticComparison
                        stat="Games"
                        teamOneStat={this.totalCalculate(
                            this.props.teams.home_id1_games,
                            this.props.teams.away_id1_games
                        )}
                        teamTwoStat={this.totalCalculate(
                            this.props.teams.home_id2_games,
                            this.props.teams.away_id2_games
                        )}
                        type=">"
                    />
                    <TeamStatisticComparison
                        stat="Wins"
                        teamOneStat={this.totalCalculate(
                            this.props.teams.home_id1_wins,
                            this.props.teams.away_id1_wins
                        )}
                        teamTwoStat={this.totalCalculate(
                            this.props.teams.home_id2_wins,
                            this.props.teams.away_id2_wins
                        )}type=">"
                    />
                    <TeamStatisticComparison
                        stat="Losses"
                        teamOneStat={this.totalCalculate(
                            this.props.teams.home_id1_losses,
                            this.props.teams.away_id1_losses
                        )}
                        teamTwoStat={this.totalCalculate(
                            this.props.teams.home_id2_losses,
                            this.props.teams.away_id2_losses
                        )}
                        type="<"
                    />
                    <TeamStatisticComparison
                        stat="Draws"
                        teamOneStat={this.totalCalculate(
                            this.props.teams.home_id1_draws,
                            this.props.teams.away_id1_draws
                        )}
                        teamTwoStat={this.totalCalculate(
                            this.props.teams.home_id2_draws,
                            this.props.teams.away_id2_draws
                        )}
                        type=">"
                    />
                    <TeamStatisticComparison
                        stat="Goals For"
                        teamOneStat={this.totalCalculate(
                            this.props.teams.home_id1_goals_for,
                            this.props.teams.away_id1_goals_for
                        )}
                        teamTwoStat={this.totalCalculate(
                            this.props.teams.home_id2_goals_for,
                            this.props.teams.away_id2_goals_for
                        )}type=">"
                    />
                    <TeamStatisticComparison
                        stat="Goals Against"
                        teamOneStat={this.totalCalculate(
                            this.props.teams.home_id1_goals_against,
                            this.props.teams.away_id1_goals_against
                        )}
                        teamTwoStat={this.totalCalculate(
                            this.props.teams.home_id2_goals_against,
                            this.props.teams.away_id2_goals_against
                        )}type="<"
                    />
                </React.Fragment>
            );
        }
        else if (this.state.quality === "home") {
            return (
                <React.Fragment>
                    <TeamStatisticComparison
                        stat="Games"
                        teamOneStat={this.props.teams.home_id1_games}
                        teamTwoStat={this.props.teams.home_id2_games}
                        type=">"
                    />
                    <TeamStatisticComparison
                        stat="Wins"
                        teamOneStat={this.props.teams.home_id1_wins}
                        teamTwoStat={this.props.teams.home_id2_wins}
                        type=">"
                    />
                    <TeamStatisticComparison
                        stat="Losses"
                        teamOneStat={this.props.teams.home_id1_losses}
                        teamTwoStat={this.props.teams.home_id2_losses}
                        type="<"
                    />
                    <TeamStatisticComparison
                        stat="Draws"
                        teamOneStat={this.props.teams.home_id1_draws}
                        teamTwoStat={this.props.teams.home_id2_draws}
                        type="<"
                    />
                    <TeamStatisticComparison
                        stat="Goals For"
                        teamOneStat={this.props.teams.home_id1_goals_for}
                        teamTwoStat={this.props.teams.home_id2_goals_for}
                        type=">"
                    />
                    <TeamStatisticComparison
                        stat="Goals Against"
                        teamOneStat={this.props.teams.home_id1_goals_against}
                        teamTwoStat={this.props.teams.home_id2_goals_against}
                        type="<"
                    />
                </React.Fragment>
            );
        }
        else {
            return (
                <React.Fragment>
                    <TeamStatisticComparison
                        stat="Games"
                        teamOneStat={this.props.teams.away_id1_games}
                        teamTwoStat={this.props.teams.away_id2_games}
                        type=">"
                    />
                    <TeamStatisticComparison
                        stat="Wins"
                        teamOneStat={this.props.teams.away_id1_wins}
                        teamTwoStat={this.props.teams.away_id2_wins}
                        type=">"
                    />
                    <TeamStatisticComparison
                        stat="Losses"
                        teamOneStat={this.props.teams.away_id1_losses}
                        teamTwoStat={this.props.teams.away_id2_losses}
                        type="<"
                    />
                    <TeamStatisticComparison
                        stat="Draws"
                        teamOneStat={this.props.teams.away_id1_draws}
                        teamTwoStat={this.props.teams.away_id2_draws}
                        type=">"
                    />
                    <TeamStatisticComparison
                        stat="Goals For"
                        teamOneStat={this.props.teams.away_id1_goals_for}
                        teamTwoStat={this.props.teams.away_id2_goals_for}
                        type=">"
                    />
                    <TeamStatisticComparison
                        stat="Goals Against"
                        teamTwoStat={this.props.teams.away_id2_goals_against}
                        teamOneStat={this.props.teams.away_id1_goals_against}
                        type="<"
                    />
                </React.Fragment>
            );
        }
    };
    render() {
        return (
            <div className="center-align">
                <div className="row">
                    <div className="col s12">
                    <ul className="tabs">
                        <li className="tab col s6">
                        <a
                            className={this.state.type === "statistics" ? "active" : ""}
                            href="#statistics"
                            onClick={() => this.setState({ type: "statistics" })}
                        >
                            Statistics
                        </a>
                        </li>
                        <li className="tab col s6">
                        <a
                            className={this.state.type === "fixtures" ? "active" : ""}
                            href="#fixtures"
                            onClick={() => this.setState({ type: "fixtures" })}
                        >
                            Fixtures
                        </a>
                        </li>
                    </ul>
                    </div>
                </div>
                <div className="row">
                    <div className="col s12">
                    <ul className="tabs">
                        <li className="tab col s4">
                        <a
                            className={this.state.quality === "total" ? "active" : ""}
                            href="#total"
                            onClick={() => this.setState({ quality: "total" })}
                        >
                            Total
                        </a>
                        </li>
                        <li className="tab col s4">
                        <a
                            className={this.state.quality === "home" ? "active" : ""}
                            href="#home"
                            onClick={() => this.setState({ quality: "home" })}
                        >
                            Home
                        </a>
                        </li>
                        <li className="tab col s4">
                        <a
                            className={
                            this.state.quality === "away" ? "active" : ""
                            }
                            href="#away"
                            onClick={() => this.setState({ quality: "away" })}
                        >
                            Away
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

export default TeamStatistics;
