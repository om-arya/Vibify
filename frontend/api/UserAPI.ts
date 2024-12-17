import axios from "axios";

import SessionState from "../state/SessionState.ts";

const API_URL = "localhost:8000";

export interface User {
    username: string;
    password: string;
    firstName: string;
    lastName: string
    emailAddress: string;
}

const UserAPI = () => {
    const state = SessionState();
}

export default UserAPI;