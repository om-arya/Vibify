import axios from "axios";

import { API_URL } from "../appSecrets.ts";

const USER_URL = API_URL + 'users/'

export interface User {
    username: string;
    email: string;
    firstName: string;
    lastName: string
}

const UserAPI = () => {
    
    async function createUser(username: string, email: string, password: string, firstName: string, lastName: string) {
        const userQueryString = `username=${username}&email=${email}&password=${password}&first_name=${firstName}&last_name=${lastName}`;
        const response = await axios.post(USER_URL + 'create_user/', userQueryString);
        return response.data;
    }

    return { createUser }
}

export default UserAPI;