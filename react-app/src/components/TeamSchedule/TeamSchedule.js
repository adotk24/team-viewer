import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink, useParams, useHistory } from "react-router-dom";
import { getAllGamesByTeam, deletingGame } from "../../store/game";
import { getOneTeam } from "../../store/team";
import './TeamSchedule.css'
import { IndiGames } from "../IndiGames/IndiGames";

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

    const sortedSchedule = schedule.sort((a, b) => {
        const aTime = new Date(a.datetime).getTime();
        const bTime = new Date(b.datetime).getTime();
        return aTime - bTime;
    })

    return isLoaded && (
        <div className="scheduleContainer">
            <div className="scheduleLoop">
                {sortedSchedule.map(game => (
                    <IndiGames key={game.id} game={game} team={team} user={user} />
                    // < div className="scheduleOneGame" >
                    //     <div>{game.datetime}</div>
                    //     <div className="scheduleMatchup">
                    //         <div>{game.team1.mascot} VS {game.team2.mascot}</div>
                    //     </div>
                    //     {
                    //         team[0].userId == user?.id &&
                    //         <div className="gameFunctions">
                    //             <NavLink to={`schedule/game/${game.id}/edit`}>
                    //                 <button
                    //                     className="schedule-btn">Edit Game</button>
                    //             </NavLink>
                    //             <button
                    //                 className="schedule-btn"
                    //                 onClick={async (e) => {
                    //                     e.preventDefault()
                    //                     const deleted = await dispatch(deletingGame(game.id))
                    //                     window.location.reload()
                    //                 }}>
                    //                 Delete Game
                    //             </button>
                    //         </div>
                    //     }
                    // </div>
                ))
                }
            </div>
        </div >
    )
}

export default TeamSchedule
