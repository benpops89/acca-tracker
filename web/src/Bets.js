import React from 'react';
import { useParams } from '@reach/router';
import { useQuery } from 'urql';
import gql from 'graphql-tag';
import { Column, Header } from './Grid';
import Bet from './Bet';

const betQuery = gql`
  query($week: Int!, $year: Int!) {
    accas(week: $week, year: $year) {
      id
      name
      bets {
        gameId
        betOn
        spread
        netScore
      }
    }
  }
`

const Bets = ({ ids }) => {
  const {week ,year} = useParams();
  const [result, reexectueQuery] = useQuery({
    query: betQuery,
    variables: {
      week: parseInt(week),
      year: parseInt(year)
    }
  });

  const { data, fetching, error } = result;

  if (fetching) return <p>Loading...</p>;
  if (error) return <p>Oh no... {error.message}</p>
  
  return (
    data.accas.map((acca, i) => {
      const bets = acca.bets.reduce((obj, item) => {
        obj[item.gameId] = item
        return obj
      }, {})

      return (
        <Column col={i+2}>
          <Header id={i}>{acca.name}</Header>
          {ids.map((id, i) => (
            <Bet key={i} bet={bets[id]}/>
          ))}
        </Column>
      )
    })
  )
}

export default Bets;