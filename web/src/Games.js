import React from 'react';
import { useParams } from '@reach/router';
import { useQuery } from 'urql';
import gql from 'graphql-tag';
import { orderBy } from 'lodash';
import Bets from './Bets';
import Game from './Game';
import { Wrapper, Column, Row, Header, Grid } from './Grid';

const gameQuery  = gql`
  query($week: Int!, $year: Int!) {
    games(week: $week, year: $year) {
      id
      home
      homeScore
      visitor
      visitorScore
      date
    }
  }
`

const Games = () => {
  const {week, year} = useParams();
  const [result, reexectueQuery] = useQuery({
      query: gameQuery,
      variables: {
        week: parseInt(week),
        year: parseInt(year)
      },
      requestPolicy: 'network-only',
      pollInterval: 2000
  });

  const { data, fetching, error } = result;

  if (fetching) return <p>Loading...</p>;
  if (error) return <p>Oh no... {error.message}</p>

  const games = orderBy(
    data.games,
    'date'
  )
  const ids = games.map(g => g.id);

  return (
    <Wrapper>
      <h1>Week {week}</h1>
      <Grid>
        <Column col={1}>
          <Header>Games</Header>
          {games.map(game => (
            <Row key={game.id}>
              <Game key={game.id} game={game}/>
            </Row>
          ))}
        </Column>
        <Bets ids={ids}/>
      </Grid>
    </Wrapper>
  )
}

export default Games;