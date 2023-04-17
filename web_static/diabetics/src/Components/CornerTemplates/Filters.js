import React from "react";
import { BiSearch } from "react-icons/bi";
import { IoMdArrowDropdown } from "react-icons/io";
import { MdKeyboardArrowDown, MdKeyboardArrowUp,  MdKeyboardArrowLeft } from 'react-icons/md'
import { CgClose } from "react-icons/cg";
import styled from "styled-components";

const Filters = () => {
  return (
    <Wrapper>
      {/* Search */}
    <div className="filter-big-screen">
      <div className="filter-title">
        <MdKeyboardArrowLeft className="icon"/>
        <h6>filter</h6>
        <h6>reset</h6>
      </div>
      <div className="filter search">
        <div className="col">
          <label htmlFor="search">search</label>
          <input
            type="text"
            name="search"
            className="input"
            placeholder="search"
          />
        </div>
        <BiSearch className="icon"/>
      </div>
      {/* location filters */}
      <div className="location-filters">
      <div className="filter sml-display-half">
        <div className="col ">

        <label htmlFor="country">country</label>
        <input
          type="text"
          name="country"
          className="input"
          placeholder="kenya"
          > 
          </input>
          </div>
        <div className="icons">
            <CgClose className="icon close"/>
            <IoMdArrowDropdown className="icon drop-down"/>
            </div>
      </div>
      {/* County/State*/}
      <div className="filter sml-display-half">
        <div className="col">

        <label htmlFor="county">County</label>
        <input
          type="text"
          name="county"
          className="input"
          placeholder="county"
          />
          </div>
          <div className="icons">
            <CgClose className="icon close"/>
            <IoMdArrowDropdown className="icon drop-down"/>
            </div>
      </div>
      {/* Location*/}
      <div className="filter sml-display-half">
        <div className="col">

        <label htmlFor="location">location</label>
        <input
          type="text"
          name="location"
          className="input"
          placeholder="location"
          />
          </div>
          <div className="icons">
            <CgClose className="icon close"/>
            <IoMdArrowDropdown className="icon drop-down"/>
            </div>
      </div>
      {/* Location*/}
      <div className="filter col">
        <label htmlFor="facility">by clinic/facility</label>
        <input
          type="text"
          name="facility"
          className="input"
          placeholder="facility name"
        />
      </div>
      </div>
      {/* *********subfilter********* */}
      <div className="sub-filter">
        {/* speciality*/}
        <div className="filter col">
          <label htmlFor="speciality">speciality</label>
          <input
            type="text"
            name="speciality"
            className="input"
            placeholder="search"
          />
        </div>
      <div className="sml-display-flex">
        {/* select 1 */}
        <div className="input-select">
          <input type="checkbox" />
          <h5>BSC health</h5>
        </div>
        {/* select 2 */}
        <div className="input-select">
          <input type="checkbox"/>
          <h5>clinical officer</h5>
        </div>
        {/* select 3 */}
        <div className="input-select">
          <input type="checkbox" />
          <h5>BSC comm Health</h5>
        </div>
        </div>
      </div>
    </div>
    <div className="filter-sort-btn">
      <div className="btn">
        <span className="sort">
          <MdKeyboardArrowUp className="icon"/>
          <MdKeyboardArrowDown className="icon"/>
        </span>
        sort
      </div>
      <div className="btn">
        <span className="filter-btn">
          <span className="line icon"></span>
          <span className="line icon"></span>
          <span className="line icon"></span>
          <span className="line icon"></span>
          <span className="line icon"></span>
        </span>
        filter
      </div>
    </div>

    </Wrapper>
  );
};

const Wrapper = styled.article`
.filter-big-screen{
  background: var(--primary-clr-1);
  display: flex;
  flex-direction: column;
  padding: 1rem 0.55rem;
  color: var(--primary-clr-5);
  height:auto;
  /* position: sticky; */
  /* position: -webkit-sticky; Safari */
  /* top: 0;  */

}


.filter-title{
  display: flex;
  justify-content: space-between;
  align-items:center;
  width: 95%;
  color: var(--secondary-clr-1);
  margin-block: 1rem;
  .icon,
    h6{
    font-weight: 500;
    font-size: 1.15rem;
  }
  .icon{
    font-size: 1.55rem;
  }
}

  .filter{
    display:flex;
    position:relative;
    margin-bottom: .75rem;
    max-width: 100%;
  }

  .col{
      display:flex;
      flex-direction:column ;
    text-transform:capitalize;
    width: 95%;
  }



  label{
    font-size: 0.95rem;
    padding-left: 2px;
    margin-bottom: 4px;
  }

  .filter input{
    padding-block: 5px;
    padding-inline: 8px;
    text-transform: capitalize;
    border:var(--border);
  }

  input:hover,
  input:focus{
    border:1px solid var(--secondary-clr-orange);
  }

  .search{
    position:relative;
  }

  .search .icon{
    cursor: pointer;
    position:absolute;
    top:50%;
    right: 20px;
  }


  .icons{
    display:flex;
    align-items:center;
    justify-content:space-between;
    position:absolute;
    right: 20px;
    top:50%;
  }

  .icons .close{
    font-size: 14px;
  }


  .sub-filter{
      border: var(--border);
      margin-block: 4px;
      padding:5px 10px;
      width: 95%;
  }

.input-select{
    display:flex;
    gap: 8px;
    align-items:center;
    cursor: pointer;
    margin-bottom: 5px;
}

/* .input-select *+*{
    color: red;
} */


.input-select h5{
    font-size: 1rem;
    font-weight:400 ;
    font-size:1rem ;
    text-transform: capitalize;
}


.filter-sort-btn{
  background: var(--primary-clr-4);
  display:none;
  justify-content: space-around;
  padding: 1rem 4px;


  .btn{
    background: var(--primary-clr-1);
    padding: 0.25rem 2rem;
    border-radius: var(--radius);
    text-transform:capitalize ;
    font-weight: 500;
    letter-spacing: 2px;
    display:flex;
    align-items:center;
    gap: 12px;
    cursor:pointer;
  }
  
  .sort, .filter-btn{
    display:flex;
    flex-direction:column;
    justify-content:center ;
    align-items:center ;
    text-align:center;
  }

}


.line{
      width: 30px;
      height:2px;
      background: var(--secondary-clr-1) ;
      margin-bottom: 2px;
    }
    
  .line:nth-child(2){
    width: 25px;
  }
  .line:nth-child(3){
    width: 20px;
  }
  .line:nth-child(4){
    width: 15px;
  }

  .line:nth-child(5){
    width: 10px;
  }


@media (max-width: 640px){
  .filter-big-screen{
    display: none;
    position:fixed;
    z-index: 99;
    bottom: 0;
    right:0;
    border-radius: 30px 30px 0 0;
    box-shadow: rgba(9, 30, 66, 0.25) 0px 4px 8px -2px, rgba(9, 30, 66, 0.08) 0px 0px 0px 1px;
  }

  
  .filter{
    margin-bottom: 1.25rem;
  }


  .search{
    width: 75%;
  }
  .location-filters{
    display:flex;
    flex-wrap: wrap;
  }

  .sml-display-half{
    width: calc(calc(calc(100% - 0.55rem))/2);
    display: inline-block;
  }

  .filter-sort-btn{
    display:flex;
  }

  .sub-filter{
    border: 1px solid var(--secondary-clr-1);
    padding-block: 2rem;
  }

  .sml-display-flex{
  display:flex;
  flex-wrap: wrap;
  gap: 12px;
}



}

`

export default Filters;
