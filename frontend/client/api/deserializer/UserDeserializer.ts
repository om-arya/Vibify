import { User } from "../UserAPI";

const UserDeserializer = () => {
    /**
     * Deserialize the given user from its server
     * JSON representation to its client object
     * representation.
     * 
     * @param user in its server JSON representation.
     * @returns the user in its client object
     *          representation.
     */
    function from_json(user) {
        return {
            username: user.username,
            email: user.email,
            firstName: user.first_name,
            lastName: user.last_name
        } as User;
    }

    return { from_json }
}

export default UserDeserializer;