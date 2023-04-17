import React from 'react'
import styled from 'styled-components'

const Header = () => {
  return (
    <Wrapper>
      <div className="header">
        <h5>Doctors corner</h5>
        <p>Explore and meet qualified doctors to meet your needs. Experts are all ready to make your life easy</p>
      </div>
      <div className="display-floating">
      <div className="search">
        <div className="infor">
          <h6>appointments only</h6>
          <p>please find a doctor</p>
        </div>
        <div className="inputs-fields">
          <div className="input-field">
              <label htmlFor="name">name</label>
              <input type="text" name='name' className='search-input' placeholder='enter name'/>
          </div>

          <div className="input-field">
            <label htmlFor="email">email</label>
              <input type="text" name='email' className='search-input' placeholder='enter email'/>
          </div>
          <input type="button" value="submit" className='submit button'/>
        </div>
      </div>
      </div>
    </Wrapper>
  )
}

const Wrapper = styled.article`
background: var(--primary-clr-1);
text-align: center;
margin-block: 5rem;
display:flex;
flex-direction: column;
max-width: 100%;

.display-floating{
  position: relative;
  display: block;
  height: 50px;
  max-width: 100%;
}


.search{
  background: var( --secondary-clr-1);
  color: var(--primary-clr-1);
  display: flex;
  justify-content: space-between;
  position: absolute;
  top: 25%;
  /* right:calc(100% - 25%); */
  left: 25%;
  gap: 8px;
  padding: 8px;
  border-bottom: 1px var(--primary-clr-1) solid;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
  /* box-shadow: rgba(6, 24, 44, 0.4) 0px 0px 0px 2px, rgba(6, 24, 44, 0.65) 0px 4px 6px -1px, rgba(255, 255, 255, 0.08) 0px 1px 0px inset; */
}

.infor{
  align-self:center;
  h6{
    font-size: 1rem;
  }
  p{
    font-size: 0.9rem;
    color: var(  --primary-clr-3);
  }
}
.inputs-fields{
  display:flex;
  gap: 8px;

  .input-field{
    display:flex;
    flex-direction: column;
    gap: 2px;
    text-transform: capitalize;
    label{
      align-self: start;
      margin-left: 8px;
    }

    .search-input{
      padding: 8px;
      border: var(--border);
      text-transform: capitalize;
      color: gray;
    }
    /* .search-input:hover{
      border: var(--secondary-clr-orange);
    } */

  }
}

.submit{
  height: 32px;
  width: auto;
  padding: 2px 4px;
  text-transform: uppercase;
  color: var(--primary-clr-1);
  background: var(--secondary-clr-orange);
  border: none;
  align-self: center;
  margin-top: 22px;
}
.submit:hover{
  cursor:pointer;
  font-weight: bold;
}

`
export default Header