import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink } from "react-router-dom";
import './LandingPage.css'

const LandingPage = () => {


    return (
        <NavLink to={`/teams`}>
            <button> Click Here For Teams!</button>
        </NavLink>
    )
}

export default LandingPage
