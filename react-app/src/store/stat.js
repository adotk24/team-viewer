const LOAD_STATS_BY_GAME = 'stats/LOAD_STATS_BY_GAME'
const LOAD_STATS_BY_PLAYER = 'stats/LOAD_STATS_BY_PLAYER'
const LOAD_SCORE_BY_GAME = 'stats/LOAD_SCORE_BY_GAME'

const statsBygame = stats => {
    return {
        type: LOAD_STATS_BY_GAME, stats
    }
}

const statsByPlayer = stats => {
    return {
        type: LOAD_STATS_BY_PLAYER, stats
    }
}

const scoreByGame = (gameid, scores) => {
    return {
        type: LOAD_SCORE_BY_GAME,
        gameid,
        scores
    }
}

export const getStatsBygame = (gameId) => async dispatch => {
    const response = await fetch(`/api/stats/team/${gameId}`)
    if (response.ok) {

        const stats = await response.json()
        dispatch(statsBygame(stats.Stats))
        dispatch(scoreByGame(gameId, stats.scores))
    }
}

export const getStatsByPlayer = playerId => async dispatch => {
    const response = await fetch(`/api/stats/player/${playerId}`)
    if (response.ok) {
        const stats = await response.json()
        dispatch(statsByPlayer(stats))
        return stats
    }
}




export default function reducer(state = { oneStat: {}, allStats: {}, allScores: {}, onePlayerStat: {}, allPlayerStats: {} }, action) {
    switch (action.type) {
        case LOAD_STATS_BY_GAME: {
            const newState = { oneStat: {}, allStats: {}, allScores: { ...state.allScores }, onePlayerStat: {}, allPlayerStats: { ...state.allPlayerStats } }
            if (action.stats) {
                action.stats.forEach(e => {
                    newState.allStats[e.id] = e
                }
                )

            }
            return newState
        }
        case LOAD_SCORE_BY_GAME: {
            const newState = { ...state, oneStat: {}, allStats: { ...state.allStats }, allScores: { ...state.allScores }, onePlayerStat: {}, allPlayerStats: { ...state.allPlayerStats } }
            newState.allScores[action.gameid] = action.scores
            return newState
        }
        case LOAD_STATS_BY_PLAYER: {
            const newState = { ...state, oneState: {}, allStats: {}, allScores: { ...state.allStats }, allScores: { ...state.allScores }, onePlayerStat: {}, allPlayerStats: {} }
            if (action.stats.Stats) {
                action.stats.Stats.forEach(e => {
                    newState.allPlayerStats[e.id] = e
                })
                return newState
            }

        }
        default: return state
    }

}
