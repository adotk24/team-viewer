import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink } from "react-router-dom";
import './AllTeams.css'
import { getAllTeams } from "../../store/team";

const AllTeams = () => {
    const getTeams = useSelector(state => Object.values(state.team.allTeams))
    const dispatch = useDispatch()
    const [isLoaded, setLoaded] = useState(false)
    useEffect(() => {
        dispatch(getAllTeams()).then(() => {
            setLoaded(true)
        })
    }, [dispatch])


    return isLoaded && (
        <div className="allTeamsContainer">
            <NavLink to={`/teams/team/add`}>
                <button>
                    ADD A TEAM HERE
                </button>
            </NavLink>
            {getTeams.map(team => (
                <NavLink to={`/teams/${team.id}`}>
                    <div className="teamCard">
                        {team.name} {team.mascot} {team.city} {team.state}
                    </div>
                </NavLink>
            ))}
        </div>
    )

}


export default AllTeams
