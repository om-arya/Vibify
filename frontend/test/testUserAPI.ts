import VibifyAPI from '../api/VibifyAPI';
import UserAPI from '../api/UserAPI';

const vibifyApi = VibifyAPI();
const userApi = UserAPI();

await vibifyApi.acquireCsrfToken();

async function testCreateUser() {
    const responseData = await userApi.createUser("bob", "bob@mail.com", "bobpass", "Bob", "Smith");
    console.log(responseData);
}