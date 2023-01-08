
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
    <div className='navbar'>
      <div className='navbar-left'>

        <NavLink to='/' exact={true} activeClassName='active'>
          <img className='logo' src={require('./favicon.ico').default} alt='icoImage' />
        </NavLink>


        <NavLink to='/teams' exact={true} activeClassName='active'>
          See Teams
        </NavLink>

      </div>
      {/* <li>
          <NavLink to='/sign-up' exact={true} activeClassName='active'>
            Sign Up
            </NavLink>
          </li> */}
      {/* <li>
          <NavLink to='/users' exact={true} activeClassName='active'>
          Users
          </NavLink>
        </li> */}
      {/* {sessionUser &&
        <LogoutButton />
      } */}
      <div className='navbar-right'>
        <div className='about-page'>
          <button className='aboutPageBtn'>
            <NavLink to={`/about`} className='aboutUsLink'>About</NavLink>
          </button>
        </div>
        {!sessionUser &&
          <NavLink to='/login' exact={true} activeClassName='active'>
            Login
          </NavLink>
        }
        {sessionUser &&
          <ProfileButton />
        }
      </div>
    </div>
  );
}

export default NavBar;
