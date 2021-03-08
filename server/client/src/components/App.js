import React from "react";
import NavBar from "./NavBar";
import PlayerPage from "./PlayerPage/PlayerPage";
import TeamPage from "./TeamPage/TeamPage";
import HomePage from "./HomePage/HomePage";
import AboutPage from "./AboutPage/AboutPage";
import PlayerCompare from "./PlayerComparePage/PlayerCompare";
import TeamCompare from "./TeamComparePage/TeamCompare";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
class App extends React.Component {
  render() {
    return (
      <Router>
        <React.Fragment>
          <NavBar />
          <Switch>
            <Route path="/" exact component={HomePage}></Route>
            <Route path="/players" exact component={PlayerPage}></Route>
            <Route path="/teams" exact component={TeamPage}></Route>
            <Route path="/about" exact component={AboutPage}></Route>
            <Route
              path="/compare/player/:id1/:id2"
              exact
              component={PlayerCompare}
            ></Route>
            <Route
              path="/compare/team/:id1/:id2"
              exact
              component={TeamCompare}
            ></Route>
          </Switch>
        </React.Fragment>
      </Router>
    );
  }
}

export default App;
