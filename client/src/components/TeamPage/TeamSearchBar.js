import React from "react";

class SearchBar extends React.Component {
  state = { term: "" };
  onFormSubmit = event => {
    event.preventDefault();
    this.props.onSubmit(this.state.term);
  };
  render() {
    return (
      <div className="row">
        <form onSubmit={this.onFormSubmit}>
          <div className="input-field">
            <input
              id="team_name"
              type="text"
              className="validate"
              value={this.state.term}
              onChange={e => this.setState({ term: e.target.value })}
            />
            <label htmlFor="team_name">Team Name</label>
          </div>
        </form>
      </div>
    );
  }
}

export default SearchBar;
