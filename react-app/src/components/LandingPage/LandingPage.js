import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink } from "react-router-dom";
import './LandingPage.css'

const LandingPage = () => {
    const user = useSelector(state => state.session.user)

    return (
        <div className="landingPageContainer">
            <img className="landingPageBackPic" src={require('./landingpage.png').default} alt='landingPageBall' />
            <div className="landingPageTop">
                <div className="landingPageHeader">
                    Welcome to TeamViewer!
                    Your One Spot for all Your Teams Needs!
                </div>
                <div className="landingPageBottom">
                    <NavLink to={`/teams`}>
                        <button className="viewTeamsBtn"> Click Here To View Teams!</button>
                    </NavLink>
                    {/* <button className="aboutBtn">About</button> */}
                    {!user &&
                        <NavLink to={`/login`}>
                            <button className="landingPageStart"> Get Started Here!</button>
                        </NavLink>
                    }
                </div>
            </div>
        </div>
    )
}

export default LandingPage
