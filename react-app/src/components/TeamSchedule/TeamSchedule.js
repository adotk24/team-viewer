import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink, useParams, useHistory } from "react-router-dom";
import { getAllGamesByTeam } from "../../store/game";
import { getOneTeam } from "../../store/team";
import './TeamSchedule.css'

const TeamSchedule = ({ teamId }) => {
    const dispatch = useDispatch()
    const findSchedule = useSelector(state => state.game.allGames)
    const [isLoaded, setLoaded] = useState(false)
    const schedule = Object.values(findSchedule)
    useEffect(() => {
        dispatch(getAllGamesByTeam(teamId)).then(() => setLoaded(true))
    }, [dispatch, teamId])
    const team = useSelector(state => {
        return state.team.oneTeam
    })
    const user = useSelector(state => state.session.user)
    useEffect(() => {
        dispatch(getOneTeam(teamId))
    }, [dispatch, teamId])
    return isLoaded && (
        <div className="scheduleContainer">
            {schedule.map(e => (
                < div className="scheduleOneGame" >
                    <div>{e.datetime}</div>
                    <div>{e.team1.mascot} VS {e.team2.mascot}</div>
                    {
                        team[0].userId == user.id &&
                        <NavLink to={`schedule/game/${e.id}/edit`}>
                            <button>Edit This Game</button>
                        </NavLink>
                    }
                </div>
            ))
            }
        </div >
    )
}

export default TeamSchedule
