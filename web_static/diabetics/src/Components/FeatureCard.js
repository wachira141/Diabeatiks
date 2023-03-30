import React from 'react'
import styled from 'styled-components'
import { FaEnvelopeOpen, FaUserShield , FaFileMedical} from 'react-icons/fa'

const FeatureCard = () => {
  return (
    <Wrapper>
      <div className="container">

      <div className="row">
        <div className="head">
          <span>

          <FaEnvelopeOpen className='svg'/>
          </span>
          <h5>Appointments</h5>
        </div>
        <div className="description">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. In explicabo ea assumenda placeat rerum earum voluptatibus tempora minima voluptas. Delectus!
        </div>
      </div>
        {/* feature 2 */}
      <div className="row">
        <div className="head">
          <span>

          <FaUserShield className='svg'/>
          </span>
          <h5>community</h5>
        </div>
        <div className="description">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. In explicabo ea assumenda placeat rerum earum voluptatibus tempora minima voluptas. Delectus!
        </div>
      </div>
        {/* feature 3 */}
      <div className="row">
        <div className="head">
          <span>

          <FaFileMedical className='svg'/>
          </span>
          <h5>Expert's corner</h5>
        </div>
        <div className="description">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. In explicabo ea assumenda placeat rerum earum voluptatibus tempora minima voluptas. Delectus!
        </div>
      </div>
      </div>
    </Wrapper>
  )
}


const Wrapper = styled.div`
margin: 2rem 0;
.container{
  display: flex;
  justify-content:center;
  gap:12px;
  flex-wrap:wrap;
  margin:auto;
  /* background: black; */
}
.row{
  padding:1rem 1.5rem;
  text-align:center;
  background-repeat: no-repeat;
  background-position:0 .0.62em ;
  box-shadow: 0 0 2.5em rgba(0, 0, 0, 0.15);
  border-radius: 0.5em;
  transition:0.5s ;
}

.row:hover{
  background-position: 0;
  background: linear-gradient(0deg, #397ef6 10px, transparent 10px);

}

.row .head h5{
  text-transform: capitalize;
}
span{
  background: #397ef6;
  display:flex;
  justify-content:center;
  align-items:center;
  border-radius: 50%;
  color: #ffffff;
  height: 4rem;
  width:4rem;
  margin:auto;
  margin-bottom: 2rem;
}
span::after{
  border: 2px solid black;

}
.svg{
  font-size: 2rem;
  /* margin-bottom: 1rem; */
}

.description{
  margin-top: 0.75rem;
}

@media (min-width: 768px){
  .row{
    padding:3rem 2rem;
  width:320px;

  }
}

@media (min-width){
  .row{
    padding: 1.5rem;
  }
}
`

export default FeatureCard