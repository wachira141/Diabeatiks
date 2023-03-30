import React, {useState} from "react";
import styled from "styled-components";
import { CgMenuLeftAlt } from 'react-icons/cg'
import { FaHome } from "react-icons/fa";
import { GiMedicines } from 'react-icons/gi'
import { AiOutlineClose} from 'react-icons/ai'

import {
  Features,
  About,
} from '../Components'

import banner from '../images/banner2.webp'





const Landing = () => {
  const [isOpen, setIsOpen] = useState(false)
  
  const open_menu = ()=>{
    setIsOpen(!isOpen)
  }

  const close_menu = ()=>{
    setIsOpen(!isOpen)
  }


  return (
    <Wrapper>
      <div className="main">
    
        <CgMenuLeftAlt className="menu" onClick={open_menu}/>
            <div className="header">
              <div className="links-container">
                <a href="#">home</a>
                <a href='#'>community</a>
                <a href='#'>Doctors</a>
                <a href='#'>daetician</a>
                <a href='#'>pharmacists</a>
              </div>
            </div>
            <span className={isOpen ? 'close show' : 'hide'} onClick={close_menu}>
                <AiOutlineClose className="svg icon"/>
            </span>
         
          <ul className={isOpen ? 'navbar' : 'hide'} >
            <li className="link">
              <FaHome className="svg icon" /> <a href="#">Home</a>
            </li>
            <li className="link">
              <GiMedicines className="svg icon" /> <a href="#">Pharmacist</a>
            </li>
          </ul>
        <div className="banner">
          <h4>Together we achieve a Diabetes free world</h4>
          <h5>we are diabetiks free</h5>
          <div></div>
        </div>
      </div>

     <Features />
     <About />
    </Wrapper>
  );
};

const Wrapper = styled.section`
.main{
  min-height: 100vh;
  width: 100%;
  max-width:100%;
  background-image: url(${banner});
  background-position: center;
  background-size:cover;
  background-repeat:no-repeat ; ;
  display:flex;
  justify-content:center;
}

.header{
  background: var(--clr-black-fade-2);
  /* border-radius: var(--radius); */
  width:100%;
  height:4rem;
  margin-top:0;
  position: fixed;
  display:none;
}

.links-container{
  display:flex;
  justify-content:flex-end;
  align-items:center;
  text-transform: capitalize;
  margin-right: 12px;
  height:100%;
}

.links-container a{
  color: var(--clr-secondary-1);
  font-size: 14px;
  margin-left: 12px;
}

.links-container a:hover{
 font-weight: 600 ;
 cursor:pointer;
}

  .menu {
    position: absolute;
    background:rgba(255, 255, 255, 0.75);
    border-radius: 5px;
    top: 25px;
    margin-left: 1.75rem;
    right:2rem;
    font-size: 2.25rem;
    cursor: pointer;
  }
  .navbar{
    position:absolute;
    width:75%;
    right:0;
    height: min(100%, 100%);
    background:rgba(255, 255, 255, 0.90);
    padding: 2rem 2rem;
    font-weight: bold;
    display:block;
  }

  .hide{
    display:none;
  }

  .close{
    position:absolute;
    right:2rem;
    top:2rem;
    z-index:10;
    display:flex;
    justify-content:center;
    align-items:center;
    .svg{
      font-size: 2.25rem;
      color:black;
    }
  }
  
  .show{
    display:inline-block;
  }


  .link{
    display:flex;
    gap:1.5rem;
    cursor: pointer;
    align-items:center;
    border-bottom: 1px gray solid ;
    padding: 0.5rem 0;
    margin-top: 0.45rem;
  }
  .link a{
    color:gray;

  }

  .icon{
    color:purple;
    font-size: 1.5rem;
  }

  .banner{
    align-self: center;
    margin:0 0.5rem;
    color:var(--clr-gray-2);
    font-family: 'Times New Roman', Times, serif;
    background:var(--clr-black-fade-2) ;
    padding: 0.45rem;
    border-radius: 7px;
    h4{
      text-align:center;
    }
    
    h5{
      font-size:1.5rem;
      text-align:right;
      color: red;
    }

    div{
      border:1px solid var(--clr-green-dark);
      margin-left: 2rem;
    }
  }

  @media (min-width: 690px){
    .navbar{
      width:420px;
    }
    .banner{
      margin-left: 5rem;
    }

    .links-container{
      justify-content:center;
    }
    .links-container a{
      font-size: 1rem;
    }
  }

  @media (min-width: 776px) {
      .menu {
      display:none;
    }
    .navbar{
      display:none;
    }
    

    .close{
      display:none;
    }
    .header{
      display:block;
    }




.banner{
  padding: 0.45rem 2.25rem;
  h4{
    font-size: 1.75rem;
  }
  h5{
    font-size: 1.5rem;
  }
}

  }

`;

export default Landing;
