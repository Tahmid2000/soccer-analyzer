import React from "react";
import analyzer from "../../apis/analyzer";
import TeamCompareCard from "./TeamCompareCard";
import { clearTeams } from "../../actions";
import { connect } from "react-redux";


class TeamCompare extends React.Component {
    state = { teams: [], loading: true};
    componentDidMount() {
        this.getData();
        this.props.clearTeams();
    }

    getData = async () => {
        const response = await analyzer.get(
            `/teams/h2h/${this.props.match.params.id1}/${this.props.match.params.id1}`
        );
        this.setState({ 
            teams: response.data,
            loading: false
        });
    };
    render() {
        console.log(this.state.teams.data);
        return (
            <React.Fragment>
                <h1 className="center-align">
                     {`${this.state.teams.data} vs. ${this.state.teams.data}`}
                </h1>
            </React.Fragment>
        );
    }
};
const mapStateToProps = state => {
    return {};
  };
  export default connect(mapStateToProps, { clearTeams })(TeamCompare);

