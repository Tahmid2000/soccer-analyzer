import analyzer from "../apis/analyzer";
export const fetchPlayers = term => {
  return async dispatch => {
    const response = await analyzer.get(`/players/${term}`);
    dispatch({ type: "FETCH_PLAYERS", payload: response.data });
  };
};
