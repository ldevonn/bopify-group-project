import { csrfFetch } from "./csrf"

const GET_LIKES = 'likes/getLikes'
const GET_LIKES_PER_TRACK = 'likes/getLikesPerTrack'
const LIKED_TRACK = 'likes/likedTrack'
const DELETE_LIKED = 'likes/deleteLike'

const getLikes = (userLikes) => {
  return {
    type: GET_LIKES,
    userLikes
  }
}

const getNumLikesPerTrack = (trackLikes) => {
  return {
    type: GET_LIKES_PER_TRACK,
    trackLikes
  }
}

const likedTrack = (trackIsLiked) => {
  return {
    type: LIKED_TRACK,
    trackIsLiked
  }
}

const removeLiked = (liked) => {
  return {
    type: DELETE_LIKED,
    liked
  }
}

export const fetchGetLikedTracksByCurrentUser = () => async (dispatch) => {
  const res = await fetch('/api/likes')

  if (res.ok) {
    const data = await res.json()
    dispatch(getLikes(data))
    return data
  } else if (res.status < 500) {
    const errorMessages = await res.json()
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
}

export const fetchTotalLikesByTrack = (trackId) => async (dispatch) => {
  const res = await csrfFetch(`/api/likes/${trackId}`)
  if (res.ok) {
    const data = await res.json()
    dispatch(getNumLikesPerTrack(data))
    return data
  } else if (res.status < 500) {
    const errorMessages = await res.json()
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
}

export const likeTheTrack = (trackId, payload) => async (dispatch) => {
  const res = await csrfFetch(`/api/likes/${trackId}`, {
    method: 'POST',
    header: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  })
  if (res.ok) {
    const data = await res.json()
    dispatch(likedTrack(data))
    return data
  } else if (res.status < 500) {
    const errorMessages = await res.json()
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
}

export const removeLikedTrack = (trackId) => async (dispatch) => {
  const res = await csrfFetch(`/api/likes/${trackId}`, {
    method: 'DELETE',
  })
  if (res.ok) {
    dispatch(removeLiked())
    return res
  } else if (res.status < 500) {
    const errorMessages = await res.json()
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
}

const likesReducer = (state = {}, action) => {
  switch (action.type) {
    case GET_LIKES:
      return { ...state, userLikedTracks: action.userLikes }
    case GET_LIKES_PER_TRACK:
      return { ...state, numLikesPerTrack: action.trackLikes }
    case LIKED_TRACK:
      return { ...state, trackIsLiked: action.trackIsLiked }
    default:
      return state
  }
}

export default likesReducer
