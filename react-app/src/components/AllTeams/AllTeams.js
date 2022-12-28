import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink } from "react-router-dom";
import './AllTeams.css'
import { getAllTeams } from "../../store/team";

const AllTeams = () => {
    const getTeams = useSelector(state => Object.values(state.team.allTeams))
    const dispatch = useDispatch()
    const user = useSelector(state => state.session.user)
    const [isLoaded, setLoaded] = useState(false)
    useEffect(() => {
        dispatch(getAllTeams()).then(() => {
            setLoaded(true)
        })
    }, [dispatch])


    return isLoaded && (
        <div className="allTeamsContainer">
            <div className="allTeamsTop">
                <div className="allTeamsHeader">
                    All Schools
                </div>
                <div className="allTeamsCounter">
                    results: {getTeams.length}
                </div>
            </div>
            {user &&
                <NavLink to={`/teams/team/add`}>
                    <button className="addTeamBtn">
                        ADD A TEAM HERE
                    </button>
                </NavLink>}
            <div className="teamsLoopContainer">
                {getTeams.map(team => (
                    <div className="indiTeaminLoop">
                        <NavLink to={`/teams/${team.id}`}>
                            <div className="teamCard">
                                {team.name} {team.mascot} {team.city} {team.state}
                            </div>
                        </NavLink>
                    </div>
                ))}
            </div>
        </div>
    )

}


export default AllTeams
