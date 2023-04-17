import React from 'react'
import styled from 'styled-components'
import { FaCalendarAlt, FaWhatsapp, FaPhone } from 'react-icons/fa'
import { BsArrowRight } from 'react-icons/bs'
import UserCard from './UserCard'
import user_image from '../../images/userplaceholder.jpg'
import { users } from '../../statics'


const Main = () => {
  return (
    <Wrapper>
      {/* user card */}
      {
        users.map((user, index)=>{
          return <UserCard user={user} key={index}/>
        })
      }

        {/* ******************popup model******************** */}
        <div className="user-model-container">
          <div className="user-model">
            <div className="intro">
              <div className="model-img">
                 <img src={user_image} alt="user profile" />
              </div>
              <h6>jael nyambura</h6>
              <p className='speciality'>senior orthopeadic</p>
              <div className="model-socials">
                  <span className='social'><FaCalendarAlt  className='icon'/></span>
                  <span className='social'><FaPhone  className='icon'/></span>
                  <span className='social'><FaWhatsapp  className='icon'/></span>
              </div>
            </div>
            <div className="details-field">
              {/* field */}
              <div className="field">
                <h6 className='heading'>education</h6>
                <h6>mbbs fbsc</h6>
              </div>
              {/* field */}
              <div className="field">
                <h6 className='heading'>speciality</h6>
                <h6>senior orthopeadic</h6>
              </div>
              {/* field */}
              <div className="field">
                <h6 className='heading'>facility</h6>
                <h6>mengi clinic</h6>
              </div>
            </div>
          </div>
          {/* absolute displays */}
          <div className="profile-link">
            <p>view profile</p>
          </div>
          <div className="booking">
              <BsArrowRight className='icon'/>
              <p>booking available online</p>
          </div>
          <div className="border"></div>
        </div>
        {/* ******************popup model******************** */}

    </Wrapper>
  )
}


const Wrapper = styled.article`
background: var( --primary-clr-1);
display:grid;
grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
padding: 4px;
gap: 0.95px;
position: relative;

.user-card{
  border: 1px #8080808c solid;
  /* width: 180px; */
  display:flex;
  flex-direction:column;
  padding:8px 4px;
  cursor: pointer;
  box-shadow: rgba(0, 0, 0, 0.07) 0px 1px 1px, rgba(0, 0, 0, 0.07) 0px 2px 2px, rgba(0, 0, 0, 0.07) 0px 4px 4px, rgba(0, 0, 0, 0.07) 0px 8px 8px, rgba(0, 0, 0, 0.07) 0px 16px 16px;
}


.profile{
  max-width: 65%;
  border: 1px solid var(--secondary-clr-green-dark);
  border-radius: 50%;
  padding: 1px;
  margin-bottom: 8px;
  object-fit:cover;
  overflow:hidden;
  align-self:center ;
}
img{
  width: 100%;
  border-radius: 50%;
}

.user-details{
  align-self: center;
  text-align:center;
  margin-bottom: 1.25rem;
  h6{
    font-weight: 500;
    font-size: 0.95rem;
  }
  p{
    text-transform: lowercase;
  }
}

.status{
  display: flex;
  justify-content: space-between;
  margin-inline: 1rem;
  
  .action{
    text-transform: capitalize;
    font-size: 0.85rem;
  }
}

.active{
  color: var(--secondary-clr-green-dark);
}

.in-active{
  color: var( --secondary-clr-red);
}

.approved {
  width: 32px;
  color: var(--secondary-clr-orange);
  position: absolute;
}



/* pop-up model */
.user-model-container{
  background-color: var( --secondary-clr-1) ;
  color: var(--primary-clr-1);
  max-width: 360px;
  position:absolute;
  padding:20px 8px;
}

.user-model{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap: 10px;
  width: 100%;
  overflow:hidden;
  color: var(--primary-clr-2);
}

.intro{
  display:flex;
  flex-direction:column;
  justify-content:center;
  align-items:center;
}

.intro > *{
  color: var(--primary-clr-2);
  text-transform: capitalize;
}

.intro h6{
  font-weight: bold ;
}
.intro .model-img{
  width: 50%;
  border-radius: 50%;
  border: 1px solid green;
  overflow:hidden;
  object-fit: cover;
  margin-bottom: 12px;

  img{
    width: 100%;
  border-radius: 50%;
  overflow:hidden;
  padding: 2px;
  }
}

.model-socials{
  margin-top: 12px;
  display:flex;
  width: 75%;
  gap: 8px;
  justify-content:space-between;
}

.details-field{
  padding-left: 4px;
  align-self: center;
  
  .field{
    margin-bottom: 4px;

    .heading{
      font-weight: bold;
    }
    h6{
      font-size: 0.85rem;
    }
  }
}


.profile-link, .booking{
  position: absolute;
  color: white;
  cursor: pointer;
  p{
    font-size: 0.85rem;
    color: var(--primary-clr-2);
  }
}
.profile-link{
  border: 2px solid var(--primary-clr-2);
  top: 2%;
  right: 5%;
  padding: 2px;
  font-weight: 500;
}

.booking{
  display: flex;
  gap: 8px;
  left: 45%;
  bottom: 2px;
  text-transform: capitalize;
}

.border{
  border: 1px solid var(--primary-clr-2);
  position: absolute;
  height: 50%;
  top: 25%;
  left: 49.55%;
}


`

export default Main