import React from "react";
import styled from "styled-components";
import {
Main,
Filters,
Header,
} from './CornerTemplates'

const CornerTemplate = () => {
  return(
    <Wrapper>
    <Header />
    <section>
        <Filters />
        <Main />
    </section>
    </Wrapper>
    )
};


const Wrapper = styled.div`
    background: var(--primary-clr-7);
    padding-bottom: 2rem;
    overflow:hidden;
    section{
      border: none;
    display:grid;
    grid-template-columns: 1fr 3fr;
    gap: 5px;
    position:relative;
  }
  @media (max-width: 640px){
    section{
  grid-template-columns:1fr;

}
}

`

export default CornerTemplate;
