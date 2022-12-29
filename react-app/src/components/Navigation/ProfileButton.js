import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useHistory } from "react-router-dom";
import * as sessionActions from '../../store/session';
import LogoutButton from "../auth/LogoutButton";
import './ProfileButton.css'


function ProfileButton() {
    const sessionUser = useSelector(state => state.session.user);
    const dispatch = useDispatch()
    const [showMenu, setShowMenu] = useState(false)
    const history = useHistory()
    const openMenu = () => {
        if (showMenu) return
        setShowMenu(true)
    }

    useEffect(() => {
        if (!showMenu) return;

        const closeMenu = () => {
            setShowMenu(false);
        };

        document.addEventListener('click', closeMenu);

        return () => document.removeEventListener("click", closeMenu);
    }, [showMenu]);
    const logout = (e) => {
        e.preventDefault()
        dispatch(sessionActions.logout())

        history.push('/')
    }

    console.log('THIS IS MY SESSION USER', sessionUser)

    return (
        <div className="profile-icon" onClick={openMenu}>
            <i style={{ fontSize: '35px', color: "rgb(29, 29, 29)" }} className="fa-regular fa-user" />
            <img className="profile-logo" src={require('./user_account.svg').default} alt='svgImage' />
            {showMenu &&
                <div className="profile-dropdown">
                    <div className="dropdownItems">
                        {sessionUser.username}
                    </div>
                    <div className="dropdownItems">
                        <NavLink id="profileItems" to="/user/team">
                            <button>Your Teams</button>
                        </NavLink>
                    </div>
                    <div className="dropdownItems">
                        <i id="logout" onClick={logout} style={{ fontSize: '30px' }} className="fa-solid fa-right-to-bracket" />
                        <button id="logout" style={{ fontFamily: 'Helvetica' }} onClick={logout}>Log Out</button>
                    </div>
                </div>
            }
        </div>
    )
}


export default ProfileButton
