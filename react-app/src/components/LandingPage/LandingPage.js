import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink } from "react-router-dom";
import './LandingPage.css'

const LandingPage = () => {


    return (
        <div className="landingPageContainer">
            <NavLink to={`/teams`}>
                <button> Click Here For Teams!</button>
            </NavLink>
        </div>
    )
}

export default LandingPage
