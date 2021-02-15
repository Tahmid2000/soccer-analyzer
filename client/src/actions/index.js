import analyzer from "../apis/analyzer";
export const fetchPlayers = term => {
  return async dispatch => {
    const response = await analyzer.get(`/players/${term}`);
    dispatch({ type: "FETCH_PLAYERS", payload: response.data });
  };
};

export const fetchPlayerStats = id => {
  return async dispatch => {
    const response = await analyzer.get(`/player/stats/${id}`);
    dispatch({ type: "FETCH_PLAYER_STATS", payload: response.data });
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
