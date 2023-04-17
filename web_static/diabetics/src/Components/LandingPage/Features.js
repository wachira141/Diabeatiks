import React from 'react'
import phone from '../../images/phone.png'
import {FaNotesMedical, FaStore, FaPeopleCarry, FaStar} from 'react-icons/fa'
import styled from 'styled-components'


const Features = () => {
  return (
    <Wrapper>
        <div className='title'>
            <h2>
                features
            </h2>
            <h6>explore our world and experience the connectivity</h6>
        </div>
        <div className="feature-body">
                <div className="feature-cards">
                        <div className="feature-card">
                            <FaNotesMedical className='icon feature-icon'/>
                            <div className="card-infor">
                                <h5>Appointments</h5>
                                <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Fuga magni eaque soluta tempore pariatur omnis asperiores.</p>
                            </div>
                        </div>
                        <div className="feature-card">
                            <FaStar className='icon feature-icon'/>
                            <div className="card-infor">
                                <h5>meet experts</h5>
                                <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Fuga magni eaque soluta tempore pariatur omnis asperiores.
                                Lorem, ipsum dolor sit amet consectetur adipisicing elit. Fuga magni eaque soluta tempore pariatur omnis asperiores
                                </p>
                            </div>
                        </div>
                        <div className="feature-card">
                            <FaStore className='icon feature-icon'/>
                            <div className="card-infor">
                                <h5>access marketplace</h5>
                                <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Fuga magni eaque soluta tempore pariatur omnis asperiores.</p>
                                <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Fuga magni eaque soluta tempore pariatur omnis asperiores.</p>
                            </div>
                        </div>
                        <div className="feature-card">
                            <FaPeopleCarry className='icon feature-icon'/>
                            <div className="card-infor">
                                <h5>community</h5>
                                <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Fuga magni eaque soluta tempore pariatur omnis asperiores.</p>
                            </div>
                        </div>
                </div>
                <img src={phone} alt="phone showing a conversation" className="feature-img img" />
        </div>
    </Wrapper>
  )
}


const Wrapper = styled.section`

.feature-body{
    display:grid;
    column-gap: 0.25rem;
    grid-template-columns: 3fr 1fr;
    justify-content:center;
    align-items:center;
    margin-block: 0.75rem;
}

.feature-cards{
    display:grid;
    gap: .75rem;
    grid-template-columns: 1fr 1fr;
}

.feature-card{
    display:flex;
    position:relative;
    flex-direction: column;
    align-items:center;
}

.feature-card .card-infor{
    margin-top: 1.25rem;
    h5{
        text-align:center;
        color: var(--secondary-clr-green-dark);
    }
}

.feature-icon{
    font-size: 2rem;
    color: purple;
    position: absolute;
    top:4px;
    left: 12px;
}

.feature-img{
    width: 100%;
    max-width:100%;
    object-fit:cover ;
    height: 85%;
}

@media (max-width: 481px){
    .feature-body{
        width:85%;
        margin:auto;
    }
    .feature-cards{
        grid-template-columns:1fr;
    }
    
    .feature-icon{
        position:relative;
    }
    .feature-card .card-infor{
        text-align:center;
        margin-top:1rem;
    }
}

@media (max-width: 576px){
    .feature-body{
        grid-template-columns:1fr;
    }
    
    .feature-img{
        display:none;
    }
}
`

export default Features