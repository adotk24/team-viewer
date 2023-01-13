import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink, useParams, useHistory } from "react-router-dom";
import { getAllGamesByTeam } from "../../store/game";
import './PlayerSchedule.css'
import { IndiGames } from "../IndiGames/IndiGames";

const PlayerSchedule = ({ playerTeamid, team }) => {
    const dispatch = useDispatch()
    const findSchedule = useSelector(state => state.game.allGames)
    const [isLoaded, setLoaded] = useState(false)
    const schedule = Object.values(findSchedule)
    const user = useSelector(state => state.session.user)

    useEffect(() => {
        dispatch(getAllGamesByTeam(playerTeamid)).then(() => setLoaded(true))
    }, [dispatch, playerTeamid])

    const sortedSchedule = schedule.sort((a, b) => {
        const aTime = new Date(a.datetime).getTime();
        const bTime = new Date(b.datetime).getTime();
        return aTime - bTime;
    })

    return isLoaded && (
        <div className="playerScheduleContainer">
            <div className="playerScheduleLoop">
                {sortedSchedule.map(e => (
                    <IndiGames key={e.id} game={e} team={team} user={user} />
                ))}
            </div>
        </div>
    )
}


export default PlayerSchedule
