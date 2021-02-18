import React from "react";
import "./StatisticComparison.css";
class StatisticComparison extends React.Component {
  compare = (stat1, stat2) => {
    if (this.props.type === ">") {
      if (stat1 > stat2) return "better";
      else if (stat1 < stat2) return "worse";
      return "neutral";
    } else if (this.props.type === "<") {
      if (stat1 < stat2) return "better";
      else if (stat1 > stat2) return "worse";
      return "neutral";
    }
    return "";
  };
  render() {
    return (
      <React.Fragment>
        <h4>{this.props.stat}</h4>
        <div className="row">
          <div className="col s2"></div>
          <div className="col s3">
            <div
              className={`z-depth-3 ${this.compare(
                this.props.playerOneStat,
                this.props.playerTwoStat
              )}`}
            >
              <h5>{this.props.playerOneStat}</h5>
            </div>
          </div>
          <div className="col s2"></div>
          <div className="col s3">
            <div
              className={`z-depth-3 ${this.compare(
                this.props.playerTwoStat,
                this.props.playerOneStat
              )}`}
            >
              <h5>{this.props.playerTwoStat}</h5>
            </div>
          </div>
          <div className="col s2"></div>
        </div>
      </React.Fragment>
    );
  }
}

export default StatisticComparison;
