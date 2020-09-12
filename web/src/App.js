import React from 'react';
import { createClient, Provider } from 'urql';
import { Router } from '@reach/router';
import Games from './Games'

const client = createClient({
  url: 'http://localhost:8000/graphql',
});

const App = () => (
  <Provider value={client}>
    <Router>
      <Games path=":year/:week"/>
    </Router>
  </Provider>
);

export default App;
