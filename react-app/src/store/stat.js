// const LOAD_STATS_BY_GAME = 'stats/LOAD_STATS_BY_GAME'
// const LOAD_STATS_BY_PLAYER = 'stats/LOAD_STATS_BY_PLAYER'
// const LOAD_SCORE_BY_GAME = 'stats/LOAD_SCORE_BY_GAME'
// const statsBygame = stats => {
//     return {
//         type: LOAD_STATS_BY_GAME, stats
//     }
// }

// const statsByPlayer = stats => {
//     return {
//         type: LOAD_STATS_BY_PLAYER, stats
//     }
// }

// const scoreByGame = (gameid, score1, score2) => {
//     return {
//         type: LOAD_SCORE_BY_GAME, gameid, score1, score2
//     }
// }

// export const getStatsBygame = (gameId) => async dispatch => {
//     const response = await fetch(`/api/stats/team/${gameId}`)
//     if (response.ok) {
//         const stats = await response.json()
//         if (stats.toLowerCase() == stats.toUpperCase()) return null
//         dispatch(statsBygame(stats.stats))
//         dispatch(scoreByGame(gameId, stats.Score1, stats.Score2))
//     }
// }




// export default function reducer(state = { oneStat: {}, allStats: {}, allScores: {} }, action) {
//     switch (action.type) {
//         case LOAD_STATS_BY_GAME: {
//             const newState = { oneStat: {}, allStats: {} }
//             action.stats.Stats.forEach(e => {
//                 newState.allStats[e.id] = e
//             })
//             return newState
//         }
//         case LOAD_SCORE_BY_GAME: {
//             const newState = { ...state, oneStat: {}, allStats: { ...state.allStats }, allScores: {} }
//             console.log('REDUCER', action)
//         }
//         default: return state
//     }

// }
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




export default function reducer(state = { oneStat: {}, allStats: {}, allScores: {} }, action) {
    switch (action.type) {
        case LOAD_STATS_BY_GAME: {
            const newState = { oneStat: {}, allStats: {}, allScores: { ...state.allScores } }
            if (action.stats) {
                action.stats.forEach(e => {
                    newState.allStats[e.id] = e
                }
                )

            }
            return newState
        }
        case LOAD_SCORE_BY_GAME: {
            const newState = { ...state, oneStat: {}, allStats: { ...state.allStats }, allScores: { ...state.allScores } }
            newState.allScores[action.gameid] = action.scores
            return newState
        }
        default: return state
    }

}
