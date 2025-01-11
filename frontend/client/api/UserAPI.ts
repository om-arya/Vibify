import axios, { HttpStatusCode } from 'axios';
import { USER_URL } from '../../appSecrets.ts';
import ClientState from "../ClientState";
import UserDeserializer from './deserializer/UserDeserializer.ts';

export interface User {
    username: string;
    email: string;
    firstName: string;
    lastName: string;
};

const UserAPI = () => {
    const state = ClientState();
    const userDeserializer = UserDeserializer();

    /**
     * Create a new user in the database. If a user with this username
     * or email already exists, the server returns a 409 CONFLICT HTTP
     * status.
     * 
     * @param username of the new user.
     * @param email of the new user.
     * @param password of the new user.
     * @param firstName of the new user.
     * @param lastName of the new user.
     * @param updateState If true, store the created user in the client
     *                    state.
     * @returns the server response status code.
     */
    async function createUser({ username, email, password, firstName, lastName, updateState=false }) {
        const queryString = `username=${username}&email=${email}&password=${password}&first_name=${firstName}&last_name=${lastName}`;
        const response = await axios.post(USER_URL + 'create_user/', queryString);
        if (!updateState || response.status !== HttpStatusCode.Created) {
            return response.status as HttpStatusCode;
        }

        const newUser: User = {
            username: username,
            email: email,
            firstName: firstName,
            lastName: lastName
        }
        state.setUser(newUser);

        return response.status as HttpStatusCode;
    }

    /**
     * Get the user from the database with the specified username, if the
     * password is correct. If the password does not match, the server
     * returns a 401 UNAUTHENTICATED HTTP status. If the username does not
     * exist, the server returns a 404 NOT_FOUND HTTP status.
     * 
     * @param username of the user to get.
     * @param password to attempt.
     * @param updateState If true, store the retrieved user in the client
     *                    state.
     * @returns the response status code.
     */
    async function authenticateUserByUsername({ username, password, updateState=false }) {
        const queryString = `?username=${username}&password=${password}`;
        const response = await axios.get(USER_URL + 'authenticate_user_by_username/' + queryString);
        if (!updateState || response.status !== HttpStatusCode.Ok) {
            return response.status as HttpStatusCode;
        }

        const user: User = userDeserializer.from_json(response.data);
        state.setUser(user);

        return response.status as HttpStatusCode;
    }

    /**
     * Get the user from the database with the specified email, if the
     * password is correct. If the password does not match, the server
     * returns a 401 UNAUTHENTICATED HTTP status. If the email does not
     * exist, the server returns a 404 NOT_FOUND HTTP status.
     * 
     * @param email of the user to get.
     * @param password to attempt.
     * @param updateState If true, store the retrieved user in the client
     *                    state.
     * @returns the response status code.
     */
    async function authenticateUserByEmail({ email, password, updateState=false }) {
        const queryString = `?email=${email}&password=${password}`;
        const response = await axios.get(USER_URL + 'authenticate_user_by_email/' + queryString);
        if (!updateState || response.status !== HttpStatusCode.Ok) {
            return response.status as HttpStatusCode;
        }

        const user: User = userDeserializer.from_json(response.data);
        state.setUser(user);

        return response.status as HttpStatusCode;
    }

    /**
     * Set the 'email' of the signed in user in the database to the
     * specified 'newEmail'.
     * 
     * @param updateState If true, update the user's 'email' in the client
     *                    state.
     * @returns the response status code.
     */
    async function setUserEmail({ newEmail, updateState=false }) {
        const user: User = state.getUser();
        const queryString = `username=${user.username}&new_email=${newEmail}`;
        const response = await axios.post(USER_URL + 'set_user_email/', queryString);
        if (!updateState || response.status !== HttpStatusCode.Ok) {
            return response.status as HttpStatusCode;
        }

        user.email = newEmail;
        state.setUser(user);

        return response.status as HttpStatusCode;
    }

    /**
     * Set the 'password' of the signed in user in the database to the
     * specified 'newPassword'.
     * 
     * @returns the response status code.
     */
    async function setUserPassword({ newPassword }) {
        const user: User = state.getUser();
        const queryString = `username=${user.username}&new_password=${newPassword}`;
        const response = await axios.post(USER_URL + 'set_user_password/', queryString);

        return response.status as HttpStatusCode;
    }

    /**
     * Set the 'firstName' of the signed in user in the database to the
     * specified 'newFirstName'.
     * 
     * @param updateState If true, update the user's 'firstName' in the
     *                    client state.
     * @returns the response status code.
     */
    async function setUserFirstName({ newFirstName, updateState=false }) {
        const user: User = state.getUser();
        const queryString = `username=${user.username}&new_first_name=${newFirstName}`;
        const response = await axios.post(USER_URL + 'set_user_first_name/', queryString);
        if (!updateState || response.status !== HttpStatusCode.Ok) {
            return response.status as HttpStatusCode;
        }

        user.firstName = newFirstName;
        state.setUser(user);

        return response.status as HttpStatusCode;
    }

    /**
     * Set the 'lastName' of the signed in user in the database to the
     * specified 'newLastName'.
     * 
     * @param updateState If true, update the user's 'lastName' in the
     *                    client state.
     * @returns the response status code.
     */
    async function setUserLastName({ newLastName, updateState=false }) {
        const user: User = state.getUser();
        const queryString = `username=${user.username}&new_last_name=${newLastName}`;
        const response = await axios.post(USER_URL + 'set_user_last_name/', queryString);
        if (!updateState || response.status !== HttpStatusCode.Ok) {
            return response.status as HttpStatusCode;
        }

        user.lastName = newLastName;
        state.setUser(user);

        return response.status as HttpStatusCode;
    }

    /**
     * Delete the signed in user from the database.
     * 
     * @param updateState If true, remove all data from the client state.
     * @returns the response status code.
     */
    async function deleteUser({ updateState=false }) {
        const user: User = state.getUser();
        const queryString = `username=${user.username}`;
        const response = await axios.post(USER_URL + 'delete_user/', queryString);
        if (!updateState || response.status !== HttpStatusCode.Ok) {
            return response.status as HttpStatusCode;
        }

        state.clear();

        return response.status as HttpStatusCode;
    }

    return { createUser, authenticateUserByUsername, authenticateUserByEmail, setUserFirstName, setUserLastName, setUserEmail,
             setUserPassword, deleteUser }
}

export default UserAPI;