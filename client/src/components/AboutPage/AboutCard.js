import React from "react";

const AboutCard = ({
  name,
  description,
  link,
  portfolio,
  linkedin,
  github
}) => {
  return (
    <div class="card large" style={{ marginTop: "100px" }}>
      <div class="card-image">
        <img src={process.env.PUBLIC_URL + link} alt={name} />
      </div>
      <div class="card-content center">
        <span class="card-title">
          <strong>{name}</strong>
        </span>
        <p>{description}</p>
      </div>
      <div class="card-action center">
        <a
          href={portfolio}
          style={{ color: "#40916c" }}
          target="_blank"
          rel="noreferrer"
        >
          <i class="fas fa-user"></i>
        </a>
        <a
          href={linkedin}
          style={{ color: "#40916c" }}
          target="_blank"
          rel="noreferrer"
        >
          <i class="fab fa-linkedin-in"></i>
        </a>
        <a
          href={github}
          style={{ color: "#40916c" }}
          target="_blank"
          rel="noreferrer"
        >
          <i class="fab fa-github"></i>
        </a>
      </div>
    </div>
  );
};

export default AboutCard;
