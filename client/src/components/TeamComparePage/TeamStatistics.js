import React from "react";
import TeamCompareCard from "./TeamCompareCard";

class TeamStatistics extends React.Component {
    state = { quality: "total", type: "statistics" };
    renderContent = () => {
        if (this.state.quality === "total") {
            return (
                <React.Fragment>
                    <h4></h4>
                </React.Fragment>
            );
        }
        else if (this.state.quality === "home") {
            return (
                <React.Fragment>
                    <h4></h4>
                </React.Fragment>
            );
        }
        else {
            return (
                <React.Fragment>
                    <h4></h4>
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
