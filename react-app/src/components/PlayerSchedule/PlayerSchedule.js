import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink, useParams, useHistory } from "react-router-dom";
import { getAllGamesByTeam } from "../../store/game";
import './PlayerSchedule.css'


const PlayerSchedule = ({ playerTeam }) => {
    const dispatch = useDispatch()
    const findSchedule = useSelector(state => state.game.allGames)
    const [isLoaded, setLoaded] = useState(false)
    const schedule = Object.values(findSchedule)
    useEffect(() => {
        dispatch(getAllGamesByTeam(playerTeam)).then(() => setLoaded(true))
    }, [dispatch, playerTeam])
    return isLoaded && (
        <div className="scheduleContainer">
            {schedule.map(e => (
                <div className="scheduleOneGame">
                    <div>{e.datetime}</div>
                    <div>{e.team1.mascot} VS {e.team2.mascot}</div>

                </div>
            ))}
        </div>
    )
}


export default PlayerSchedule
