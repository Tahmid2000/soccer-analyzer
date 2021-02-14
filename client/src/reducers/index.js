import { combineReducers } from "redux";

const playersReducer = (state = [], action) => {
  switch (action.type) {
    case "FETCH_PLAYERS":
      return action.payload;
    default:
      return state;
  }
};

const selectedPlayersReducer = (selectedPlayers = [], action) => {
  switch (action.type) {
    case "PLAYER_SELECTED":
      return [...selectedPlayers, action.payload];
    case "PLAYER_REMOVED":
      return selectedPlayers.filter(
        player => player.player_id !== action.payload.player_id
      );
    default:
      return selectedPlayers;
  }
};

export default combineReducers({
  players: playersReducer,
  selectedPlayers: selectedPlayersReducer
});
