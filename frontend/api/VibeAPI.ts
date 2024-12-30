import axios from "axios";

import { API_URL } from "../appSecrets.ts";
import SessionState from "../state/SessionState.ts";

export interface Vibe {
    name: string;
    color: string;
    danceability: number;
    energy: number;
    valence: number;
}

const VibeAPI = () => {
    const state = SessionState();

    axios.defaults.baseURL = API_URL + 'vibes/';
    axios.defaults.headers.withXSRFToken = true;
    axios.defaults.headers.common['X-CSRFToken'] = state.getCsrfToken();
}

export default VibeAPI;