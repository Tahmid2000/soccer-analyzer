import React from "react";
import AboutCard from "./AboutCard";

class AboutPage extends React.Component {
  render() {
    return (
      <React.Fragment>
        <div className="container">
          <div className="row">
            <div className="col m1"></div>
            <div className="col s12 m4">
              <AboutCard
                name="Raiyan Mahbub"
                description="asdfsdf"
                link="raiyan.jpg"
                portfolio="https://raiyanmahbub.com"
                linkedin="https://www.linkedin.com/in/raiyan-mahbub/"
                github="https://github.com/mahbu006"
              />
            </div>
            <div className="col m2"></div>
            <div className="col s12 m4">
              <AboutCard
                name="Tahmid Imran"
                description="I'm Computer Science student at UT Dallas, graduating in May 2022. I love building full-stack applications like this!"
                link="tahmid.jpg"
                portfolio="https://tahmidimran.com"
                linkedin="https://www.linkedin.com/in/tahmidimran/"
                github="https://github.com/Tahmid2000"
              />
            </div>
            <div className="col m1"></div>
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default AboutPage;
