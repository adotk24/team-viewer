
import React, { useState } from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import { useSelector } from 'react-redux'
import ProfileButton from './ProfileButton';


const NavBar = () => {

  const sessionUser = useSelector(state => state.session.user)
  const [showModal, setShowModal] = useState(false)

  return (
    <nav>
      <div className='navbar-left'>
        <NavLink to='/' exact={true} activeClassName='active'>
          Home
        </NavLink>
      </div>
      {!sessionUser &&
        <NavLink to='/login' exact={true} activeClassName='active'>
          Login
        </NavLink>
      }
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
      {sessionUser &&
        <ProfileButton />
      }
    </nav>
  );
}

export default NavBar;
