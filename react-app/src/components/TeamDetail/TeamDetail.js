import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink, useParams, useHistory } from "react-router-dom";
import { deletingTeam, getOneTeam } from "../../store/team";
import TeamSchedule from "../TeamSchedule/TeamSchedule";
import './TeamDetail.css'

const OneTeam = () => {
    const { teamId } = useParams()
    const dispatch = useDispatch()
    const history = useHistory()
    const findTeam = useSelector(state => state.team.oneTeam)
    const team = findTeam[0]
    const [isLoaded, setLoaded] = useState(false)
    const user = useSelector(state => state.session.user)
    useEffect(() => {
        dispatch(getOneTeam(teamId)).then(() => {
            setLoaded(true)
        })
    }, [dispatch, teamId])
    return isLoaded && (
        <div className="oneTeamContainer">
            <div className="oneTeamBanner">
                Welcome to the Team Viewer for your {team.name} {team.mascot}
            </div>
            <div className="oneTeamFunctions">
                <NavLink to={`/teams`}>
                    <button
                        className="oneTeamBtn"
                    >
                        See All Teams Here!
                    </button>
                </NavLink>
                <NavLink to={`/teams/${teamId}/roster`}>
                    <button
                        className="oneTeamBtn"
                    >
                        Check out This Teams Roster!
                    </button>
                </NavLink>
                {user?.id == team.userId &&
                    <NavLink to={`/teams/team/add`}>
                        <button
                            className="oneTeamBtn"
                        >
                            Add Team Here
                        </button>
                    </NavLink>
                }
                {user?.id == team.userId &&
                    <NavLink to={`/teams/${teamId}/edit`}>
                        <button
                            className="oneTeamBtn"
                        >
                            Edit the Team Here
                        </button>
                    </NavLink>
                }
                {user?.id == team.userId &&
                    <button
                        onClick={async (e) => {
                            e.preventDefault()
                            const deleted = await dispatch(deletingTeam(team.id));
                            if (deleted) history.push('/teams')
                        }}
                        className="oneTeamBtn"
                    >
                        Delete This Team
                    </button>
                }
            </div>
            <TeamSchedule teamId={teamId} />
        </div >
    )
}

export default OneTeam
