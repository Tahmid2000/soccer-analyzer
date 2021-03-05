import React from "react";

// for (let index = 0; index < this.props.teamFixture.length; index++) {
//     console.log(this.props.teamFixture[index].score)   
// }

class TeamFixture extends React.Component {
  render() {
    return (
      <React.Fragment>
        <div className="row">
        {this.props.teamFixture.map(() => {
            return (
                <React.Fragment>
                    <div className="col s4">
                        <img src={this.props.teamFixture[1].home_logo} />
                    </div>
                    <div className="col s4">
                        <h4>{this.props.teamFixture[1].score}</h4>
                        {/* <h7><i>{this.props.teamFixture[1].date.substring(0,10)}</i></h7> */}
                    </div>
                    <div className="col s4">
                        <img src={this.props.teamFixture[1].away_logo} />
                    </div> 
                </React.Fragment>
            );
        })}
        </div>
      </React.Fragment>
    );
  }
}

export default TeamFixture;