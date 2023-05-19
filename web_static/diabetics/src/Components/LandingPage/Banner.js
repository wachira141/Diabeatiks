import React from 'react'
import { Link } from 'react-router-dom'
import styled from 'styled-components'
import { CgClose } from 'react-icons/cg'
import detailImage from '../../images/detailimage.jpg'


import {links} from '../../statics'

const Banner = () => {
  return (
    <Wrapper>
        <div className="background"></div>
        <div className="banner-details">
            <div className="intro">
                <h1>Diabetics</h1>
                <h5>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nulla eaque illo soluta culpa voluptatem repellendus nemo quod ad maiores? Non.</h5>
            </div>
               <img src={detailImage} alt="" className="banner-img" />
        </div>
        <div className="sidebar">
            <CgClose className='icon close-icon'/>
            <ul className="sidebar-links">
            {
                    links.map((link, index)=>{
                        return (
                            <li className="link" key={index}><Link to={link.link}  className="link-anchor">{link.name}</Link></li>
                        )
                    })
                }
            </ul>
        </div>
    </Wrapper>
  )
}

const Wrapper = styled.header`
width:100%;
height: 100vh;
min-height: 100vh;
overflow:hidden;
background-image: url(${detailImage});
object-fit: cover;
background-position: center;
background-size: cover;
display:flex;
flex-direction:column ;
position: relative;
/* border-bottom:1px solid var(--secondary-clr-4) ; */

.background{
    background:var(--primary-clr-3) ;
    height: 100%;
    width: 100%;
    position: absolute;
    top:0;
    z-index:1;
}




.banner-details{
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: 4px;
    width: 75%;
    height: 50%;
    max-height:50%;
    align-items:center;
    justify-items:center ;
    margin: auto;
    z-index:5;
    overflow:hidden;
}

.banner-details .intro{
    h1{
        color: purple;
    }
    p{
        color: var(--secondary-clr-1);
    }
}

.banner-img{
    object-fit:cover;
    width: 240px;
    border-radius: 25%;
    background: red;
}


.sidebar{
    width: 75%;
    background: var( --primary-clr-1);
    height: 100vh;
    position: fixed;
    display:none;
    padding: 1.5rem;
    top:0;
    right:0;
    z-index: 99;


    .close-icon{
        font-size: 1.55rem;
        /* margin-block: 1rem; */
    }
}

.sidebar-links{
    margin-top: 1.5rem;
}

.sidebar-links li{
    margin-bottom: 0.75rem;
    border-bottom:1px solid var(--secondary-clr-4) ;
}

.link .link-anchor{

text-transform: capitalize;
}

.sidebar-links .link .link-anchor{
font-size: 1.55rem;
}

@media (min-width: 672px){
    .navlinks{
        display:flex;
    }

    .sidebar,
    .close-icon{
        display: none;
    }
    
}

@media (max-width: 576px){
    .banner-details{
        grid-template-columns: 1fr;
        background: var(--secondary-clr-1);
        height:auto;
        padding:12px;
        border-radius: 14px;
        .intro h1, h5{
            color: var(--primary-clr-1);
        }
    }
    .banner-img{
        display:none;
    }
}

@media (min-width: 768px){
    
    .banner-img{
        width: 320px;
        height: 320px;
    }
}

`

export default Banner
