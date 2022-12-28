import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink } from "react-router-dom";
import { getAllUserTeams } from "../../store/team";

import './UserTeams.css'


const UserTeams = () => {
    const dispatch = useDispatch();
    const currentUser = useSelector(state => state.session.user)
    const teams = useSelector(state => Object.values(state.team.allTeams))

    console.log('THESE ARE USER TEAMS', teams)

    useEffect(() => {
        dispatch(getAllUserTeams())
    }, [dispatch, currentUser])

    return (
        <div className="userTeamsContainer">
            {
                teams.map(team => (
                    <NavLink to={`/teams/${team.id}`}>
                        <div>
                            {team.name} {team.mascot} {team.city} {team.state}
                        </div>
                    </NavLink>
                ))
            }
        </div>
    )
}

export default UserTeams
