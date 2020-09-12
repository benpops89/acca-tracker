import styled from '@emotion/styled';

export const Wrapper = styled.div`
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
`

export const Grid = styled.div`
  display: grid;
  column-gap: 50px;
  grid-auto-columns: 1fr;
  grid-auto-rows: 1fr;
`

export const Column = styled.div`
  grid-column: ${props => props.col};
`

export const Row = styled.div`
  place-self: center;
  text-align: center;
  margin: 1em 0;
`

export const Header = styled.h3`
  place-self: center;
  text-align: center;
`

