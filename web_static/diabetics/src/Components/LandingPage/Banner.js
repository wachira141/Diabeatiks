import React from 'react'
import { Link } from 'react-router-dom'
import styled from 'styled-components'
import { CgMenuRight, CgClose } from 'react-icons/cg'
import detailImage from '../../images/detailimage.jpg'
import logo from '../../images/logo.jpeg'

import {links} from '../../statics'

const Banner = () => {
  return (
    <Wrapper>
        <div className="background"></div>
        {/* navbar */}
        <div className="navbar">
            <div className="logo">
                <img src={logo} alt="logo" className='logo-img'/>
            </div>
            <ul className="navlinks">
                {
                    links.map((link, index)=>{
                        return (
                            <li className="link" key={index}><Link to={link.link} className="link-anchor">{link.name}</Link></li>
                        )
                    })
                }
                {/* <li className="link"><a href="#" className="link-anchor">About Us</a></li>
                <li className="link"><a href="#" className="link-anchor">Service</a></li>
                <li className="link"><a href="#" className="link-anchor">Contacts</a></li> */}
            </ul>
            <CgMenuRight className='icon menu'/>
        </div>
        {/* navbar */}
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
.navbar{
    display:flex;
    justify-content:space-between;
    align-items:center;
    background: var(--primary-clr-7);
    padding: 8px 1rem;
    position:fixed;
    top:0;
    width: 100%;
    z-index:9;
}

.navlinks {
display: none;
}
.navlinks > *+*{
    margin-left: 12px;
}
.navlinks .link .link-anchor{
    color: var(--primary-clr-1);
}
.link .link-anchor{

    text-transform: capitalize;
}

.logo{
    width: 40px;
    height:40px;
    background: white;
    border-radius: 25%;
}
.logo-img{
    border-radius: 75%;

}

.menu{
    color: var(--primary-clr-1);
    font-size: 2rem;
    margin-right: 1.55rem;
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

.sidebar-links .link .link-anchor{
font-size: 1.55rem;
}

@media (min-width: 672px){
    .navlinks{
        display:flex;
    }

    .menu,
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
    .navlinks{
        padding-right: 5rem;
    }
    
    .banner-img{
        width: 320px;
        height: 320px;
    }
}

`

export default Banner
