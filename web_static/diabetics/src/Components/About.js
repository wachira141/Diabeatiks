import React from 'react'
import styled from 'styled-components'
import { FaFacebook, FaTwitter, FaLinkedin, FaGithub } from 'react-icons/fa'
import banner from '../images/banner.jpg'
const About = () => {
  return (
    <Wrapper>
        <div className="about-container">
            <div className="details">
                <h4>about</h4>
                <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Vero velit cupiditate esse et illo mollitia quasi doloremque distinctio obcaecati, dolor unde quis tempore voluptates, dolore sapiente. Architecto nemo quam alias.</p>
                <div className="socials">
                    <div className="persons">
                        <div className="person">
                            <a href="#" className="tweeter social"><FaFacebook className='svg'/> Facebook</a>
                            <a href="#" className="linkedn social"><FaTwitter className='svg'/> tweeter</a>
                            <a href="#" className="github social"><FaLinkedin className='svg'/> linkedin</a>
                        </div>
                    </div>
                    <a href="" className="code-link social"> <FaGithub className='svg'/> get code here</a>
                </div>
            </div>
            <img src={banner} alt="" className="about" />
        </div>
    </Wrapper>
  )
}

const Wrapper = styled.article`
margin-top: 2rem;
padding:1rem;
background: var(--clr-black);
color: var(--clr-gray-2);
display:flex;
justify-content:center;
align-items:center;

.about-container{
    width: 1130px;
    max-width:95%;
    margin: 0 auto;
    display:flex;
    flex-direction:column;

}

.details{
    margin-bottom: 1.5rem;
    h4{
        text-align: center;
        text-transform: capitalize;
    }
}

.socials{
    margin-top: 1rem;
    display:flex;
    flex-direction:column;
}

.social, .svg{
    color: white;
}
.person{
    display: flex;
    justify-content:center;
    gap: 2rem;
}
.person a:hover{
    color: var(--clr-gray-2)
}

.code-link{
    align-self:center;
    margin-top: 8px;
}


img{
    width: 380px;
    height:auto;
    margin:auto;
}


@media (min-width: 512px){
    img{
        width: 450px;
    }
}

@media (min-width: 672px)
{
img{
    width: 540px;
}
}

@media (min-width: 776px) {
    .about-container{
        flex-direction: row;
        column-gap: 2rem;
    }

    img{
        width:380px;
    }
}

@media (min-width: 976px){
    img{
        width:540px;
    }
} 


`


export default About