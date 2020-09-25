import React from 'react';
import { P } from './Grid';

const Bet = ({ bet }) => {
  if (bet) {
    const spread = (bet.spread <= 0 ? '' : '+') + bet.spread;
    const netScore = bet.homeBet ? bet.netScore : -bet.netScore;
    const win = (netScore + bet.spread) > 0;
    return <P win={win}>{bet.betOn} ({spread})</P>
  } else {
    return <p style={{color: "white"}}>1</p>
  }
}

export default Bet;