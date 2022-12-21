const LOAD_ALL_TEAMS = '/teams/LOAD_ALL_TEAMS'
const LOAD_ONE_TEAM = '/teams/LOAD_ONE_TEAM'
const DELETE_TEAM = '/teams/DELETE_TEAM'
const EDIT_TEAM = '/teams/EDIT_TEAM'
const ADD_TEAM = '/teams/ADD_TEAM'

const allTeams = teams => {
    return {
        type: LOAD_ALL_TEAMS, teams
    }
}

const oneTeam = team => {
    return {
        type: LOAD_ONE_TEAM, team
    }
}

const deleteTeam = team => {
    return {
        type: DELETE_TEAM, team
    }
}

const addTeam = team => {
    return {
        type: ADD_TEAM, team
    }
}

const editTeam = team => {
    return {
        type: EDIT_TEAM, team
    }
}

export const getAllTeams = () => async dispatch => {
    const response = await fetch(`/api/teams`)
    if (response.ok) {
        const teams = await response.json()
        dispatch(allTeams(teams))
    }
}

export const getOneTeam = teamId => async dispatch => {
    const response = await fetch(`/api/teams/${teamId}`)
    if (response.ok) {
        const team = await response.json()
        dispatch(oneTeam(team))
        return team
    }
}

export const addingTeam = team => async dispatch => {
    const response = await fetch(`/api/teams/add`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(team)
    })
    if (response.ok) {
        const team = response.json()
        dispatch(editTeam(team))
        return team
    }
}

export const edittingTeam = (team, id) => async dispatch => {
    const response = await fetch(`/api/teams/${id}/edit`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(team)
    })
    console.log('IS THIS EVEN HITTING?', response)
    if (response.ok) {
        const team = response.json()
        dispatch(editTeam(team))
        return team
    }
}

export const deletingTeam = id => async dispatch => {
    const response = await fetch(`/api/teams/${id}`, { method: 'DELETE' })
    if (response.ok) {
        const team = await response.json()
        await dispatch(deleteTeam(team))
        return team
    }
}


export default function reducer(state = { oneTeam: {}, allTeams: {} }, action) {
    switch (action.type) {
        case LOAD_ALL_TEAMS: {
            const newState = { oneTeam: {}, allTeams: {} }
            action.teams.Teams.forEach(e => {
                newState.allTeams[e.id] = e
            })
            return newState
        }
        case LOAD_ONE_TEAM: {
            const newState = { oneTeam: {}, allTeams: {} }
            newState.oneTeam = action.team
            return newState
        }
        case ADD_TEAM: {
            const newState = { ...state, oneTeam: { ...state.oneTeam }, allTeams: { ...state.allTeams } }
            newState.oneTeam = action.team
            return newState
        }
        case EDIT_TEAM: {
            const newState = { ...state, oneTeam: { ...state.oneTeam }, allTeams: { ...state.allTeams } }
            newState.allTeams[action.team.id] = action.team
            newState.oneTeam = action.team
            return newState
        }
        case DELETE_TEAM: {
            const newState = { ...state, oneTeam: { ...state.oneTeam }, allTeams: { ...state.allTeams } }
            delete newState.allTeams[action.team.id]
            return newState
        }
        default: return state
    }
}
