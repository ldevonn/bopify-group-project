const GET_TRACKS = 'tracks/getTracks'
const GET_TRACK_DETAILS = 'tracks/getTrackDetails'
const GET_TRACK_BY_USER = 'tracks/getTrackByUser'
const ADD_TRACK = 'tracks/addTrack'
const UPDATE_TRACK = 'tracks/updateTrack'
const DELETE_TRACK = 'tracks/deleteTrack'

const getTracks = (allTracks) => {
  return {
    type: GET_TRACKS,
    allTracks
  }
}

const getTrackDetails = (trackDetails) => {
  return {
    type: GET_TRACK_DETAILS,
    trackDetails
  }
}

const getTrackByCurrentUser = (trackByUser) => {
  return {
    type: GET_TRACK_BY_USER,
    trackByUser
  }
}

const addTrack = (newTrack) => {
  return {
    type: ADD_TRACK,
    newTrack
  }
}

const modifiedTrack = (updatedTrack) => {
  return {
    type: UPDATE_TRACK,
    updatedTrack
  }
}

const deleteTrack = (track) => {
  return {
    type: DELETE_TRACK,
    track
  }
}

export const fetchGetTracks = () => async (dispatch) => {
  const res = await fetch('/api/tracks')
  if(res.ok) {
    const data = await res.json()
    const tracksData = {}

    for (let i = 0; i < data.tracks.length; i++) {
      let currObj = data.tracks[i]
      tracksData[currObj.id] = currObj
    }

    dispatch(getTracks(tracksData))

    return tracksData
  }  else if (res.status < 500) {
    const errorMessages = await res.json()
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
}

export const fetchGetTrackDetails = (trackId) => async (dispatch) => {
  const res = await fetch(`/api/tracks/${trackId}`)
  if (res.ok) {
    const data = await res.json()
    dispatch(getTrackDetails(data))
    return data
  } else if (res.status < 500) {
    const errorMessages = await res.json()
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
}

export const fetchCurrentUserTracks = () => async (dispatch) => {
  const res = await fetch('/api/tracks/current')
  if (res.ok) {
    const data = await res.json()
    dispatch(getTrackByCurrentUser(data))
    return data
  } else if (res.status < 500) {
    const errorMessages = await res.json()
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
}

export const createTrack = (payload) => async (dispatch) => {
  const res = await fetch('/api/tracks/new', {
    method: 'POST',
    header: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  })
  
  if (res.ok) {
    const data = await res.json()
    dispatch(addTrack(data))
    return data
  } else if (res.status < 500) {
    const errorMessages = await res.json()
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
}

export const updateTrack = (payload, trackId) => async (dispatch) => {
  const res = await fetch(`/api/tracks/${trackId}`, {
    method: 'PUT',
    header: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  })

  if (res.ok) {
    const data = await res.json()
    dispatch(modifiedTrack(data))
    return data
  } else if (res.status < 500) {
    const errorMessages = await res.json()
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
}

export const fetchDeleteTrack = (trackId) => async (dispatch) => {
  const res = await fetch(`api/tracks/${trackId}`, {
    method: 'DELETE'
  })

  if (res.ok) {
    dispatch(deleteTrack())
    return res
  } else if (res.status < 500) {
    const errorMessages = await res.json()
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
}

const tracksReducer = (state = {}, action) => {
  switch (action.type) {
    case GET_TRACKS:
      return { ...state, allTracks: action.allTracks }
    case GET_TRACK_DETAILS:
      return { ...state, trackDetails: action.trackDetails }
    case GET_TRACK_BY_USER:
      return { ...state, trackByUser: action.trackByUser }
    case ADD_TRACK:
      return { ...state, trackDetails: action.addTrack }
    case UPDATE_TRACK:
      return { ...state, trackDetails: action.updatedTrack }
    default:
      return state
  }
}

export default tracksReducer