import SessionState from "../state/SessionState.ts";

const API_URL = "localhost:8000";

export interface Song {
    name: string;
    duration: number;
}

export interface Playlist {
    name: string;
    songs: Song[];
}

const SongAPI = () => {
    const state = SessionState();
}

export default SongAPI;