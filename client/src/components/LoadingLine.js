import React from "react";

class LoadingLine extends React.Component {
  render() {
    return (
      <div className="container">
        <div class="progress" style={{ backgroundColor: "#74c69d" }}>
          <div
            class="indeterminate"
            style={{ backgroundColor: "#40916c" }}
          ></div>
        </div>
      </div>
    );
  }
}

export default LoadingLine;
