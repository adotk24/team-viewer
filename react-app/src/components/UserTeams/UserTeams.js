import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink } from "react-router-dom";
import { getAllUserTeams } from "../../store/team";

import './UserTeams.css'


const UserTeams = () => {
    const dispatch = useDispatch();
    const currentUser = useSelector(state => state.session.user)
    const teams = useSelector(state => Object.values(state.team.allTeams))
    const user = useSelector(state => state.session.user)

    useEffect(() => {
        dispatch(getAllUserTeams())
    }, [dispatch, currentUser])

    return (
        <div className="userTeamsContainer">
            <div className="allTeamsTop">
                <div className="allTeamsHeader">
                    Your Teams
                </div>
                <div className="allTeamsCounter">
                    results: {teams.length}
                </div>
                {user &&
                    <NavLink to={`/teams/team/add`}>
                        <button className="addTeamBtn">
                            ADD A TEAM HERE
                        </button>
                    </NavLink>}
            </div>
            <div className="teamsLoopContainer">
                {
                    teams.map(team => (
                        <div className="indiTeaminLoop">
                            <NavLink to={`/teams/${team.id}`}>
                                <div className="teamCard">
                                    {team.name} {team.mascot} {team.city} {team.state}
                                </div>
                            </NavLink>
                        </div>
                    ))
                }
            </div>
        </div>
    )
}

export default UserTeams
