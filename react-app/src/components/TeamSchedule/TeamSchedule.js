import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink, useParams, useHistory } from "react-router-dom";
import { getAllGamesByTeam, deletingGame } from "../../store/game";
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
    }, [dispatch, teamId, findSchedule])
    return isLoaded && (
        <div className="scheduleContainer">
            {schedule.map(game => (
                < div className="scheduleOneGame" >
                    <div>{game.datetime}</div>
                    <div>{game.team1.mascot} VS {game.team2.mascot}</div>
                    {
                        team[0].userId == user.id &&

                        <div className="gamefunctions">
                            <NavLink to={`schedule/game/${game.id}/edit`}>
                                <button>Edit This Game</button>
                            </NavLink>
                            <button onClick={async (e) => {
                                e.preventDefault()
                                const deleted = await dispatch(deletingGame(game.id))
                                window.location.reload()
                            }}>
                                Delete This team
                            </button>
                        </div>
                    }
                </div>
            ))
            }
        </div >
    )
}

export default TeamSchedule
