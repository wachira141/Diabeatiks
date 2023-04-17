import React from 'react'
const date = new Date().getFullYear()

const Footer = () => {
  return (
    <div className='footer'>
      <h5>diabetics</h5>
      <p>&copy;{date}</p>
    </div>
  )
}

export default Footer