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
  if (action.type === "PLAYER_SELECTED") return action.payload;
  return selectedPlayers;
};

export default combineReducers({
  players: playersReducer,
  selectedPlayer: selectedPlayersReducer
});
