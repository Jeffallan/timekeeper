// BASE URL //TODO move to env var
const BACKEND_BASE = "http://localhost:8000/api/v1/"

// AUTH STUFF
export const LOGIN = `${BACKEND_BASE}auth/token/login/`
export const LOGOUT = `${BACKEND_BASE}auth/token/logout/`
export const FORGOT = `${BACKEND_BASE}auth/users/reset_password/`
export const PASSWORD_CONFIRM = `${BACKEND_BASE}auth/users/reset_password_confirm/`
export const USER_ACTIVATE = `${BACKEND_BASE}auth/users/activation/`

// USERS
export const ME = `${BACKEND_BASE}auth/users/me/`
export const PROFILE = `${BACKEND_BASE}auth/users/profiles/`