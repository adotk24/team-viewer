import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { NavLink, useParams, useHistory } from "react-router-dom"
import './PlayerDetail.css'
import { getOnePlayer, deletingPlayer } from "../../store/player";
import { getOneTeam } from "../../store/team";

const PlayerDetail = () => {
    const { playerId } = useParams()
    const dispatch = useDispatch()
    const history = useHistory()
    const [isLoaded, setLoaded] = useState(false)
    const user = useSelector(state => state.session.user)
    const player = useSelector(state => state.player.onePlayer)
    const findTeam = useSelector(state => state.team.oneTeam)
    const team = findTeam[0]
    console.log('this is my findTeam', team.userId, user.id)

    useEffect(() => {
        dispatch(getOnePlayer(playerId)).then(() => {
            setLoaded(true)
        })
    }, [dispatch, playerId])
    useEffect(() => {
        dispatch(getOneTeam(player.teamId)).then(() => {
            setLoaded(true)
        })
    }, [dispatch, player.teamId])

    const heightConvert = num => {
        let feet = Math.floor(num / 12)
        let inches = num - (feet * 12)
        return `${feet}' ${inches}`
    }

    return isLoaded && (

        <div className="playerDetailContainer">
            {team.userId == user.id &&
                <NavLink to={`/teams/players/${player.id}/edit`}>
                    <button>Edit This Player</button>
                </NavLink>
            }
            {team.userId == user.id &&
                <button
                    onClick={async (e) => {
                        e.preventDefault()
                        const deleted = await dispatch(deletingPlayer(player.id))
                        if (deleted) history.push(`/teams/${player.teamId}/roster`)
                    }}
                >Delete This Player</button>
            }
            <h1>{player.firstName} {player.lastName}</h1>
            <div> {heightConvert(player.height)} {player.position} #{player.number} {player.year}</div>
        </div>
    )
}


export default PlayerDetail
