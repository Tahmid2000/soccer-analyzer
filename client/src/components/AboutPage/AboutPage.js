import React from "react";
import AboutCard from "./AboutCard";
import "./AboutPage.css";
class AboutPage extends React.Component {
  state = { width: window.innerWidth };
  handleResize = () => {
    this.setState({ width: window.innerWidth });
  };
  componentDidMount() {
    window.addEventListener("resize", this.handleResize);
  }
  render() {
    return (
      <React.Fragment>
        <div className="container">
          <h1 className="center-align">Creators</h1>
          <div className="row negative-margin">
            <div className="col m1"></div>
            <div className="col s12 m4">
              <AboutCard
                name="Raiyan Mahbub"
                description="I am a Computer Engineering student at University of Minnesota, graduating in December 2021. "
                link="raiyan.jpg"
                portfolio="https://raiyanmahbub.com"
                linkedin="https://www.linkedin.com/in/raiyan-mahbub/"
                github="https://github.com/mahbu006"
              />
            </div>
            <div className="col m2"></div>
            <div
              className={`col s12 m4 ${
                this.state.width <= 600 ? "negative-margin" : ""
              }`}
            >
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
          <h6 className="center-align">
            We made this website to give soccer (or fútbol) fans everywhere to
            put their favorite players and teams head to head. Growing up, we
            supported rival teams so this project gave us a great way to find
            out who's club is really the best. We hope you enjoy this app as
            much as we did making it!
          </h6>
        </div>
      </React.Fragment>
    );
  }
}

export default AboutPage;
