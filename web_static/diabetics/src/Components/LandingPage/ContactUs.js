import React from 'react'
import styled from 'styled-components'
import { SiGmail } from 'react-icons/si'
import { CiLocationOn } from 'react-icons/ci'
import {FaPhoneAlt } from 'react-icons/fa'

const ContactUs = () => {
  return (
    <Wrapper>
      <div className="title">
        <h2>contact us</h2>
      </div>
      <div className="contact-container">

      <div className="contact-details">
        <div className="form-intro">
          <h5>office line</h5>
          <p>Lorem ipsum dolor sit amet consectetur.</p>
        </div>
        <div className="contacts">
            <div className="contact">
              <FaPhoneAlt className='icon'/>
              <span>+254 876 4563 23</span>
            </div>
            <div className="contact">
              <CiLocationOn className='icon'/>
              <span>Muindi bingu streets</span>
            </div>
            <div className="contact">
              < SiGmail className='icon'/>
              <span>diabetics@email.com</span>
            </div>
        </div>
      </div>
      <form  action='' className="contact-form">
        {/* f_name */}
        <div className="f_name">
          <label htmlFor="f_name">first name</label>
          <input type="text" name='f_name' className='input half' placeholder='first name' />
        </div>
       {/* l_name */}
       <div className="l_name">
          <label htmlFor="l_name">last name</label>
          <input type="text" name='l_name' className='input half' placeholder='last name'/>
       </div>
        {/* email*/}
        <div className="email">
          <label htmlFor="email">email</label>
          <input type="text" name='email'  pattern=".+@globex\.com" className='input full' placeholder='enter email'/>
        </div>
       {/* phone number*/}
       <div className="phone">
          <label htmlFor="phone">phone number</label>
          <input type="number" name='phone' className='input full' placeholder='+254 000 0000'/>
       </div>
        {/* message*/}
        <div className="message">
          <label htmlFor="message">message</label>
          <input type="text" className='input full large'name='message' placeholder='start typing...'/>
        </div>
       { /* submit button*/}
        <button  action='submit' value='submit' className='btn'>
          submit
        </button>
      </form>
      </div>
    </Wrapper>
  )
}


const Wrapper = styled.section`
padding-inline: 8px;
border-radius:var(--border-radius);
border: var(--border);

.contact-container{
  display:grid;
  column-gap: 0.5em;
  grid-template-columns:1fr 2fr;
}


.contact-details{
  padding:1.55rem 8px;
  word-wrap: break-word;
  overflow:hidden;
/* -webkit-box-shadow: 0px 2px 5px 4px rgba(64,63,64,1);
-moz-box-shadow: 0px 2px 5px 4px rgba(64,63,64,1); */
/* box-shadow: 0px 2px 5px 4px rgba(64,63,64,1); */
}

.form-intro h5{
  text-align: center;
}

.contacts{
  margin-top: 1.25rem;
  display:flex;
  flex-direction:column;
  row-gap: 1em;
}

.contact{
  display: flex;
  gap: 7px;
  align-items:center;
}

.contact:hover,
.contact:focus{
  cursor:pointer;
  font-weight: 500;
}


.contact-form{
  margin-block: 0.75rem;
  background:var(--primary-clr-5) ;
  padding: 12px;
}

.contact-form > div{
  margin-bottom: 1.25em;
  margin-left: 12px;
}

label, input{
  width: 100%;
  display: block;
}

input{
  padding: 12px 6px;
  box-sizing: border-box;
  border: var(--border);
  border-radius: var(--radius);
}

input:focus{
  background:var(--primary-clr-2);
}

.f_name, .l_name{
  width: 45%;
  display: inline-block;
}

.l_name{
  margin-left: 12px;
}
.contact-form > div:not(.f_name, .l_name){
 width: calc(calc(45% + 45%) + 12px)
}

.message input{
  height: 180px;
  padding-block: 0;
}

@media (max-width: 640px){
  border-radius:0;
  border:none;
  border-top:var(--border);
  .contact-container{
    grid-template-columns:1fr;
    padding-inline: 3rem;
  }
  
  .contact-details .form-intro{
    text-align:center;
  }
}

@media (max-width: 476px){
  .contact-container{
    padding-inline: 1.5rem;
    
  }
}
`


export default ContactUs