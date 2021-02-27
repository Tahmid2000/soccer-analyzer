import { combineReducers } from "redux";

const playersReducer = (state = [], action) => {
  switch (action.type) {
    case "FETCH_PLAYERS":
      return action.payload;
    case "CLEAR_PLAYERS":
      return [];
    default:
      return state;
  }
};

const teamsReducer = (state = [], action) => {
  switch (action.type) {
    case "FETCH_TEAM":
      return action.payload;
    case "CLEAR_TEAM":
      return [];
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
    case "CLEAR_PLAYERS":
      return [];
    default:
      return selectedPlayers;
  }
};

const selectedTeamsReducer = (selectedTeams = [], action) => {
  switch (action.type) {
    case "TEAM_SELECTED":
      return [...selectedTeams, action.payload];
    case "TEAM_REMOVED":
      return selectedTeams.filter(
        team => team.team_id !== action.payload.team_id
      );
    case "CLEAR_TEAMS":
      return [];
    default:
      return selectedTeams;
  }
};

export default combineReducers({
  players: playersReducer,
  teams: teamsReducer,
  selectedPlayers: selectedPlayersReducer,
  selectedTeams: selectedTeamsReducer 
});
