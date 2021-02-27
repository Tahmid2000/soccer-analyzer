import React from "react";

const Image = ({ link }) => {
  return <img src={process.env.PUBLIC_URL + link} alt="" />;
};

export default Image;
