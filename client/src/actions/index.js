import analyzer from "../apis/analyzer";

export const fetchPlayers = term => {
  return async dispatch => {
    const response = await analyzer.get(`/players/${term}`);
    dispatch({ type: "FETCH_PLAYERS", payload: response.data });
  };
};

export const selectPlayer = player => {
  return {
    type: "PLAYER_SELECTED",
    payload: player
  };
};

export const removePlayer = player => {
  return {
    type: "PLAYER_REMOVED",
    payload: player
  };
};

export const clearPlayers = () => {
  return {
    type: "CLEAR_PLAYERS",
    payload: []
  };
};

export const fetchTeams = term => {
  return async dispatch => {
    const response = await analyzer.get(`/teams/${term}`);
    dispatch({ type: "FETCH_TEAMS", payload: response.data });
  };
};

export const selectTeam = team => {
  return {
    type: "TEAM_SELECTED",
    payload: team
  };
};

export const removeTeam = team => {
  return {
    type: "TEAM_REMOVED",
    payload: team
  };
};

export const clearTeamss = () => {
  return {
    type: "CLEAR_TEAMS",
    payload: []
  };
};
