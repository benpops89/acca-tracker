import React from 'react';

const Game = ({ game }) => {
  return (
    <p>{game.visitor} {game.visitorScore} @ {game.homeScore} {game.home}</p>
  )
};

export default Game;