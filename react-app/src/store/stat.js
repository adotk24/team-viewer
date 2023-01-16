const LOAD_STATS_BY_GAME = 'stats/LOAD_STATS_BY_GAME'
const LOAD_STATS_BY_PLAYER = 'stats/LOAD_STATS_BY_PLAYER'
const LOAD_SCORE_BY_GAME = 'stats/LOAD_SCORE_BY_GAME'
const LOAD_ONE_SCORE = 'stats/LOAD_ONE_SCORE'
const ADD_STAT = 'stats/ADD_STAT'

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

const oneScore = (gameId, score) => {
    return {
        type: LOAD_ONE_SCORE, score
    }
}

const addStat = (gameId, teamId, stat) => {
    return {
        type: ADD_STAT, stat
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

export const addingStat = (gameId, teamId, stat) => async dispatch => {
    console.log('THUNKER THUNKER', stat)

    const response = await fetch(`/api/stats/${gameId}/${teamId}/${stat.player}/add`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(stat)
    })
    if (response.ok) {
        const stat = response.json()
        dispatch(addStat(stat))
        return stat
    }
}



export default function reducer(state = { oneStat: {}, allStats: {}, oneScore: {}, allScores: {}, onePlayerStat: {}, allPlayerStats: {} }, action) {
    switch (action.type) {
        case LOAD_STATS_BY_GAME: {
            const newState = { oneStat: {}, allStats: {}, oneScore: {}, allScores: { ...state.allScores }, onePlayerStat: {}, allPlayerStats: { ...state.allPlayerStats } }
            if (action.stats) {
                action.stats.forEach(e => {
                    newState.allStats[e.id] = e
                })
            }
            return newState
        }
        case LOAD_SCORE_BY_GAME: {
            const newState = { ...state, oneStat: {}, allStats: { ...state.allStats }, oneScore: {}, allScores: { ...state.allScores }, onePlayerStat: {}, allPlayerStats: { ...state.allPlayerStats } }
            newState.allScores[action.gameid] = action.scores
            newState.oneScore = action.scores
            return newState
        }
        case LOAD_STATS_BY_PLAYER: {
            const newState = { ...state, oneStat: {}, allStats: {}, oneScore: {}, allScores: { ...state.allStats }, onePlayerStat: {}, allPlayerStats: {} }
            if (action.stats.Stats) {
                action.stats.Stats.forEach(e => {
                    newState.allPlayerStats[e.id] = e
                })
                return newState
            }
        }
        case ADD_STAT: {
            const newState = { ...state, oneStat: {}, allStats: {}, oneScore: {}, allScores: { ...state.allStats }, allScores: { ...state.allScores }, onePlayerStat: {}, allPlayerStats: {} }
            newState.oneStat = action.stat
            return newState
        }
        default: return state
    }
}
