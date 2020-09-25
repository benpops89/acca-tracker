/**  @jsx jsx*/
import { jsx } from '@emotion/core';

const P = props => {
  return (
    <p
      css={{
        backgroundColor: props.win ? 'rgba(0, 255, 0)' : 'red',
        color: props.win ? 'black' : 'white',
        textAlign: 'center'
      }}
      {...props}
    />
  )
}

const Wrapper = props => {
  return (
    <div
      css={{
        height: '100vh',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center'
      }}
      {...props}
    />
  )
}

const Grid = props => {
  return (
    <div
      css={{
        display: 'grid',
        columnGap: '50px',
        gridAutoColumns: '1fr',
        gridAutoRows: '1fr'
      }}
      {...props}
    />
  )
}

const Column = props => {
  return (
    <div
      css={{
        gridColumn: props.col
      }}
      {...props}
    />
  )
}

const Row = props => {
  return (
    <div
      css={{
        placeSelf: 'center',
        textAlign: 'center',
        margin: '1em 0'
      }}
      {...props}
    />
  )
}

const Header = props => {
  return (
    <h3
      css={{
        placeSelf: 'center',
        textAlign: 'center'
      }}
      {...props}
    />
  )
}

export {
  P,
  Wrapper,
  Grid,
  Column,
  Row,
  Header
};
