import React from 'react'

const Footer = () => {
    const date = new Date()
  return (
    <>
    <div className="footer">
        <h5>Diabeatiks</h5>
        <p> <span>&copy;</span> {date.getFullYear()}</p>
    </div>
    </>
  )
}

export default Footer