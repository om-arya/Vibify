import { User } from "./api/UserAPI";
import { Vibe } from "./api/VibeAPI";

const sessionStorage = require('sessionstorage'); // For testing via Jest

/**
* This function provides several setter and getter methods to streamline
* client-side state management via session storage.
*/
const ClientState = () => {
    function clear() {
        sessionStorage.clear();
    }

    function setUser(user: User) {
        sessionStorage.setItem('user', JSON.stringify(user));
    }

    function setVibes(vibes: Vibe[]) {
        sessionStorage.setItem('vibes', JSON.stringify(vibes));
    }

    function getUser() {
        const userJSON = sessionStorage.getItem('user');
        return userJSON ? JSON.parse(userJSON) as User : null;
    }

    function getVibes() {
        const vibesJSON = sessionStorage.getItem('vibes');
        return vibesJSON ? JSON.parse(vibesJSON) as Vibe[] : [];
    }

    return { clear, setUser, getUser, setVibes, getVibes }
}

export default ClientState;