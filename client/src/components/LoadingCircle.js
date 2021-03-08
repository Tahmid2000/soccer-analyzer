import React from "react";

class LoadingCircle extends React.Component {
  render() {
    return (
      <div className="container center-align">
        <div class="preloader-wrapper big active">
          <div class="spinner-layer" style={{ borderColor: "#40916c" }}>
            <div class="circle-clipper left">
              <div class="circle"></div>
            </div>
            <div class="gap-patch">
              <div class="circle"></div>
            </div>
            <div class="circle-clipper right">
              <div class="circle"></div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default LoadingCircle;
