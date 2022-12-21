import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink, useParams, useHistory } from "react-router-dom";
import { deletingTeam, getOneTeam } from "../../store/team";
import './TeamDetail.css'

const OneTeam = () => {
    const { teamId } = useParams()
    const dispatch = useDispatch()
    const history = useHistory()
    const findTeam = useSelector(state => state.team.oneTeam)
    const team = findTeam[0]
    const [isLoaded, setLoaded] = useState(false)

    useEffect(() => {
        dispatch(getOneTeam(teamId)).then(() => {
            setLoaded(true)
        })
    }, [dispatch, teamId])
    return isLoaded && (
        <div className="oneTeamContainer">
            <NavLink to={`/teams`}>
                <button>
                    See All Teams Here!
                </button>
            </NavLink>
            <NavLink to={`/teams/team/add`}>
                <button>
                    ADD A TEAM HERE
                </button>
            </NavLink>
            <NavLink to={`/teams/${teamId}/edit`}>
                <button>
                    Edit the Team Here
                </button>
            </NavLink>
            <button
                onClick={async (e) => {
                    e.preventDefault()
                    const deleted = await dispatch(deletingTeam(team.id));
                    if (deleted) history.push('/teams')
                }}>
                DELETE THIS TEAM
            </button>
            <div>
                {team.name} {team.mascot} {team.city} {team.state}
            </div>

        </div >
    )
}

export default OneTeam
