import SessionState from "../state/SessionState.ts";

const API_URL = "localhost:8000";

export interface Vibe {
    name: string;
    color: string;
    danceability: number;
    energy: number;
    valence: number;
}

const VibeAPI = () => {
    const state = SessionState();
}

export default VibeAPI;