import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink, useParams, useHistory } from "react-router-dom"
import './PlayerDetail.css'
import { getOnePlayer, deletingPlayer } from "../../store/player";
import { getOneTeam } from "../../store/team";
import PlayerSchedule from "../PlayerSchedule/PlayerSchedule";
import { getStatsByPlayer } from "../../store/stat";
const PlayerDetail = () => {
    const { playerId } = useParams()
    const dispatch = useDispatch()
    const history = useHistory()
    const [isLoaded, setLoaded] = useState(false)
    const user = useSelector(state => state.session.user)
    const player = useSelector(state => state.player.onePlayer)
    const findTeam = useSelector(state => state.team.oneTeam)
    const team = findTeam[0]
    const stats = useSelector(state => Object.values(state.stat.allPlayerStats))

    useEffect(() => {
        dispatch(getOnePlayer(playerId)).then(() => {
            dispatch(getOneTeam(player.teamId)).then(() => {
                dispatch(getStatsByPlayer(playerId)).then(() => {
                    setLoaded(true)
                })
            })
        })
    }, [dispatch, playerId, player.teamId])

    const heightConvert = num => {
        let feet = Math.floor(num / 12)
        let inches = num - (feet * 12)
        return `${feet}' ${inches}`
    }

    const findPoints = () => {
        let points = 0;
        let games = 0
        stats.forEach(stat => {
            points += stat.points
            games += 1
        })
        if (games == 0) return 0
        else return points / games
    }
    const findAssists = () => {
        let assists = 0;
        let games = 0;
        stats.forEach(stat => {
            assists += stat.assists
            games += 1
        })
        if (games == 0) return 0
        else return assists / games
    }
    const findRebounds = () => {
        let rebs = 0
        let games = 0
        stats.forEach(stat => {
            rebs += stat.rebounds
            games += 1
        })
        if (games == 0) return 0
        else return rebs / games
    }

    return isLoaded && player && findTeam && (

        <div className="playerDetailContainer">
            <div className="playerDetailCard">
                <div className="playerDetailCard-left">
                    <h1>{player.firstName} {player.lastName}</h1>
                    <div>{team?.name} High School</div>
                    <div>{team?.city}, {team?.state}</div>
                    <div>
                        {heightConvert(player.height)} {player.position} #{player.number} {player.year}
                    </div>
                </div>
                <div className="playerDetailCard-right">
                    <div>{Math.round(findPoints() * 10) / 10} PPG</div>
                    <div>{Math.round(findAssists() * 10) / 10} APG</div>
                    <div>{Math.round(findRebounds() * 10) / 10} RPG</div>
                </div>
            </div>

            <div className="playerDetailFunctions">
                <NavLink to={`/teams/${player.teamId}`}>
                    <button
                        className="playerDetailBtn"
                    >Back To Team Home</button>
                </NavLink>
                {team?.userId == user?.id &&
                    <NavLink to={`/teams/players/${player.id}/edit`}>
                        <button
                            className="playerDetailBtn"
                        >Edit This Player</button>
                    </NavLink>
                }
                {team?.userId == user?.id &&
                    <button
                        className="playerDetailBtn"
                        onClick={async (e) => {
                            e.preventDefault()
                            const deleted = await dispatch(deletingPlayer(player.id))
                            if (deleted) history.push(`/teams/${player.teamId}/roster`)
                        }}
                    >Delete This Player</button>
                }
            </div>
            <PlayerSchedule playerTeamid={team?.id} team={team} />
        </div>
    )
}


export default PlayerDetail
