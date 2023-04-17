import React from 'react'
import styled from 'styled-components'
import {
  FaUser,
   FaFacebook,
    FaTwitter, 
    FaLinkedin
  } from 'react-icons/fa'
  import { SiGmail } from 'react-icons/si'

const AboutUs = () => {
  return (
    <Wrapper>
      <div className="title">
        <h2>about us</h2>
      </div>
      <div className="about-cards">
        {/* single card start */}
        <div className="about-card">
            <FaUser className='icon user-icon'/>
            <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Incidunt labore deleniti nemo error corporis eaque vitae.</p>
            <div className="about-socials">
            <a href="/facebook"><FaLinkedin className='icon' /></a>
              <a href="/facebook"> <FaFacebook className='icon' /></a>
              <a href="/facebook"><FaTwitter className='icon'/></a>
              <a href="/facebook"><SiGmail className='icon'/></a>
            </div>
        </div>
        {/* single card end */}
        {/* single card start */}
        <div className="about-card">
            <FaUser className='icon user-icon'/>
            <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Incidunt labore deleniti nemo error corporis eaque vitae.</p>
            <div className="about-socials">
            <a href="/facebook"><FaLinkedin className='icon' /></a>
              <a href="/facebook"> <FaFacebook className='icon' /></a>
              <a href="/facebook"><FaTwitter className='icon'/></a>
              <a href="/facebook"><SiGmail className='icon'/></a>
            </div>
        </div>
        {/* single card end */}
        {/* single card start */}
        <div className="about-card">
            <FaUser className='icon user-icon' />
            <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Incidunt labore deleniti nemo error corporis eaque vitae.</p>
            <div className="about-socials">
              <a href="/facebook"><FaLinkedin className='icon' /></a>
              <a href="/facebook"> <FaFacebook className='icon' /></a>
              <a href="/facebook"><FaTwitter className='icon'/></a>
              <a href="/facebook"><SiGmail className='icon'/></a>
            </div>
        </div>
        {/* single card end */}
      </div>
    </Wrapper>
  )
}

const Wrapper = styled.section`

.about-cards{
  display:flex;
  gap: .75rem;
  justify-content:space-between;
  align-items:center;
  margin-block: .5rem;
}

.about-card{
  display:flex;
  flex-direction: column;
  align-items:center;
  text-align:center;
  border:var(--border);
  border-radius: var(--border-radius);
  padding:12px;

  p{
    margin-block:.5rem;
  }
}
.user-icon{
  background: white;
  font-size: 3rem;
  padding: 4px;
  border-radius: 50%;
  border: 1px solid var(--primary-clr-5);
  /* color: var(--secondary-clr-green-light); */
}

.about-socials{
  display:flex;
  justify-content:space-around;
  width:95%;
  margin:auto;

  .icon{
    font-size:1.55rem;
    /* color:rgba(0, 0, 255, 0.75); */
  }
}

@media (max-width: 542px){
  .about-cards{
    flex-direction: column;
    padding-inline: 3rem;
  }
 

  .about-card > *+*{
    margin-top: 1rem;
  }

  .about-socials{
    justify-content:center;
    .icon{
      margin-inline: 12px;
    }
  }
}

`

export default AboutUs