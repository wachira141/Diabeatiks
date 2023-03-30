import React from 'react'
import styled from 'styled-components'
import { FaAngleRight, FaAngleLeft } from 'react-icons/fa'
import {
    FeatureCard
} from './index'

const Features = () => {
  return (
    <Wrapper className='article'>
            <h4 className='title'>our features</h4>
                <FeatureCard />
    </Wrapper>
  )
}

const Wrapper = styled.article`

margin-top:2rem;
padding: auto;
overflow:hidden;

.title{
    text-transform: capitalize ;
    font-family:Georgia, 'Times New Roman', Times, serif ;
    text-align:center;
    margin-bottom: 0.75rem;
}


`

export default Features