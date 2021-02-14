import React from "react";
import PlayerCard from "./PlayerCard";
import "./PlayerList.css";
class PlayerList extends React.Component {
  render() {
    const renderedList = this.props.players.map(player => {
      return (
        <div class="col s12 m6 l4">
          <PlayerCard
            key={player.player_id}
            player_id={player.player_id}
            image_path={player.image_path}
            player_name={player.player_name}
            player={player}
          />
        </div>
      );
    });

    return (
      <React.Fragment>
        <div class="row">{renderedList}</div>
      </React.Fragment>
    );
  }
}
export default PlayerList;
