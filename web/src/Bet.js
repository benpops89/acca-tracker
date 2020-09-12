import React from 'react';
import styled from '@emotion/styled';

const P = styled.p`
  background-color: ${props => props.win ? 'rgb(0, 255, 0)': 'red'};
  color: ${props => props.win ? 'black' : 'white'};
  text-align: center;
`

const Bet = ({ bet }) => {
  if (bet) {
    const spread = (bet.spread <= 0 ? '' : '+') + bet.spread;
    const netScore = bet.homeBet ? bet.netScore : -bet.netScore;
    const win = bet.spread > netScore;
    return <P win={win}>{bet.betOn} ({spread})</P>
  } else {
    return <p style={{color: "white"}}>1</p>
  }
}

export default Bet;