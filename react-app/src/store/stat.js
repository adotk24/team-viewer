const LOAD_STATS_BY_GAME = 'stats/LOAD_STATS_BY_GAME'
const LOAD_STATS_BY_PLAYER = 'stats/LOAD_STATS_BY_PLAYER'

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

export const getStatsBygame = (gameId) => async dispatch => {
    const response = await fetch(`/api/stats/team/${gameId}`)
    if (response.ok) {
        const stats = await response.json()
        dispatch(statsBygame(stats))
    }
}


export default function reducer(state = { oneStat: {}, allStats: {} }, action) {
    switch (action.type) {
        case LOAD_STATS_BY_GAME: {
            const newState = { oneStat: {}, allStats: {} }
            action.stats.Stats.forEach(e => {
                newState.allStats[e.id] = e
            })
            return newState
        }



        default: return state
    }

}
