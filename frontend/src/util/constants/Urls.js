const BACKEND_BASE = process.env.VUE_APP_BACKEND_URL

// AUTH STUFF
export const LOGIN = `${BACKEND_BASE}auth/token/login/`
export const LOGOUT = `${BACKEND_BASE}auth/token/logout/`
export const FORGOT = `${BACKEND_BASE}auth/users/reset_password/`
export const PASSWORD_CONFIRM = `${BACKEND_BASE}auth/users/reset_password_confirm/`
export const USER_ACTIVATE = `${BACKEND_BASE}auth/users/activation/`
export const USERNAME_RESET = `${BACKEND_BASE}auth/users/reset_email/`
export const USERS = `${BACKEND_BASE}auth/users/`

// USERS
export const ME = `${BACKEND_BASE}auth/users/me/`
export const PROFILE = `${BACKEND_BASE}auth/users/profiles/`

//CLIENTS
export const LOCATIONS =  `${BACKEND_BASE}locations/`
export const CLIENTS = `${BACKEND_BASE}clients/`
export const SERVICES = `${BACKEND_BASE}services/`

//WORK
export const WORK = `${BACKEND_BASE}work/`
