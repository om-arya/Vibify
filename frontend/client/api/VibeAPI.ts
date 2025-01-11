import axios, { HttpStatusCode } from 'axios';
import { VIBE_URL } from '../../appSecrets.ts';
import { User } from './UserAPI.ts';
import ClientState from "../ClientState";
import VibeDeserializer from './deserializer/VibeDeserializer.ts';

export interface Vibe {
    name: string;
    color: string;
};

const VibeAPI = () => {
    const state = ClientState();
    const vibeDeserializer = VibeDeserializer();

    /**
     * Create a new vibe in the database belonging to the signed in user.
     * 
     * @param name of the new vibe.
     * @param color of the new vibe.
     * @param updateState If true, store the created vibe in the client
     *                    state.
     * @returns the server response status code.
     */
    async function createVibe({ name, color, updateState=false }) {
        const user: User = state.getUser();
        const queryString = `username=${user.username}&name=${name}&color=${color}`;
        const response = await axios.post(VIBE_URL + 'create_vibe/', queryString);
        if (!updateState || response.status !== HttpStatusCode.Created) {
            return response.status as HttpStatusCode;
        }
        
        const vibes = state.getVibes() as Vibe[];
        const newVibe: Vibe = {
            name: name,
            color: color
        };
        vibes.push(newVibe);
        state.setVibes(vibes);

        return response.status as HttpStatusCode;
    }

    /**
     * Get an array of all vibes belonging to the signed in user.
     * 
     * @param updateState If true, set the array of vibes stored in the
     *                    client state to the retrieved vibes.
     * @returns the server response status code.
     */
    async function getUserVibes({ updateState=false }) {
        const user: User = state.getUser();
        const queryString = `?username=${user.username}`;
        const response = await axios.get(VIBE_URL + 'get_user_vibes/' + queryString);
        if (!updateState || response.status !== HttpStatusCode.Ok) {
            return response.status as HttpStatusCode;
        }

        const vibes = vibeDeserializer.array_from_json(response.data) as Vibe[];
        state.setVibes(vibes);

        return response.status as HttpStatusCode;
    }

    /**
     * Set the 'color' of the vibe with the specified name in the
     * database, and belonging to the signed in user, to the
     * specified 'newColor'.
     * 
     * @param name of the vibe to update the color of.
     * @param newColor to set the 'color' of the vibe to. 
     * @param updateState If true, update the vibe's 'color' in the
     *                    client state.
     * @returns the server response status code.
     */
    async function setVibeColor({ name, newColor, updateState=false }) {
        const user: User = state.getUser();
        const queryString = `username=${user.username}&name=${name}&new_color=${newColor}`;
        const response = await axios.post(VIBE_URL + 'set_vibe_color/', queryString);
        if (!updateState || response.status !== HttpStatusCode.Ok) {
            return response.status as HttpStatusCode;
        }

        const vibes = state.getVibes() as Vibe[];
        const updateIndex = vibes.findIndex(vibe => vibe.name === name);
        const updatedVibe: Vibe = {
            name: name,
            color: newColor
        };
        vibes[updateIndex] = updatedVibe;
        state.setVibes(vibes);

        return response.status as HttpStatusCode;
    }

    /**
     * Delete the vibe with the specified name, and belonging to the
     * signed in user, from the database.
     * 
     * @param name of the vibe to delete.
     * @param updateState If true, remove the vibe from the client state.
     * @returns the server response status code.
     */
    async function deleteVibe({ name, updateState=false }) {
        const user: User = state.getUser();
        const queryString = `username=${user.username}&name=${name}`;
        const response = await axios.post(VIBE_URL + 'delete_vibe/', queryString);
        if (!updateState || response.status !== HttpStatusCode.Ok) {
            return response.status as HttpStatusCode;
        }

        const vibes = state.getVibes() as Vibe[];
        state.setVibes(
            vibes.filter(vibe => vibe.name !== name)
        );

        return response.status as HttpStatusCode;
    }

    return { createVibe, getUserVibes, setVibeColor, deleteVibe }
}

export default VibeAPI;