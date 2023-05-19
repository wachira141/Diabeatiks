import React from 'react'
import styled from 'styled-components'
import { Link } from 'react-router-dom'
import { CgMenuRight } from 'react-icons/cg'


import  logo from '../images/logo.jpeg'
import {links} from '../statics'

const Navbar = () => {
  return (
    <Wrapper>
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
            </ul>
            <CgMenuRight className='icon menu'/>
        </div>
    </Wrapper>
  )
}


const Wrapper = styled.div`
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

.logo{
    width: 40px;
    height:40px;
    background: white;
    border-radius: 25%;
}
.logo-img{
    border-radius: 75%;

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


.menu{
    color: var(--primary-clr-1);
    font-size: 2rem;
    margin-right: 1.55rem;
}

@media (min-width: 672px){
    .navlinks{
        display:flex;
    }

    .menu{
        display: none;
    }
    
}

@media (min-width: 768px){
    .navlinks{
        padding-right: 5rem;
    }
}

`

export default Navbar