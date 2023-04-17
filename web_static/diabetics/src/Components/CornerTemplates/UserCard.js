import React, {useState} from 'react'
import approved from '../../images/approve.png'

const UserCard = ({user}) => {
    const {image, status, speciality, name} = user

    const [openModal, setIsModalOpen] = useState(false)

    const show_modal = (e)=>{
      // setIsModalOpen(true)
    }

    // console.log(openModal);

  return (
    <div className="user-card" onMouseOver={()=>show_modal()}>
    <div className="profile">
    <img src={image} alt="user image" className="profile-img" />
    </div>
    <div className="user-details">
      <h6>{name}</h6>
      <p className='speciality'>{speciality}</p>
    </div>
    <div className="status">
      <p>status...</p>
      <p className={status == 'active'? 'action active' : 'action in-active'}>{status}</p>
    </div>
      {user?.approved &&
    <img src={approved} alt="approved" className="approved icon" />
  }
  </div>
  )
}

export default UserCard