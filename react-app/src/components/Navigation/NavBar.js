
import React, { useState } from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import { useSelector } from 'react-redux'
import ProfileButton from './ProfileButton';
import './navigation.css'

const NavBar = () => {

  const sessionUser = useSelector(state => state.session.user)
  const [showModal, setShowModal] = useState(false)

  return (
    <div className='navbar-total'>
        <div className='navbar-top'>
          <div className='navbar-tl'>Max Preps Clone by Andrew Kim</div>
          <div className='about-page'>
            <NavLink to={`/about`} className='aboutUsLink'>
          <button className='aboutPageBtn'>
            About
          </button>
          </NavLink>
        </div>
      </div>
    <div className='navbar-bottom'>
      <div className='navbar-left'>

        <NavLink to='/' exact={true} activeClassName='active'>
          <img className='logo' src={require('./favicon.ico').default} alt='icoImage' />
        </NavLink>


        <NavLink to='/teams' exact={true} activeClassName='active' className='nav-words'>
          See Teams
        </NavLink>

      </div>
      <div className='navbar-right'>

        {!sessionUser &&
          <NavLink to='/login' exact={true} activeClassName='active' className='nav-words'>
            Login
          </NavLink>
        }
        {sessionUser &&
          <ProfileButton />
        }
      </div>
     </div>
    </div>
  );
}

export default NavBar;
