import axios, { HttpStatusCode } from "axios";
import AuthAPI from '../../client/api/AuthAPI';

const authAPI = AuthAPI();

test('Request a CSRF token to save as an Axios header', async () => {
    const responseStatus = await authAPI.acquireCsrfToken();
    expect(responseStatus).toBe(HttpStatusCode.Ok);
    expect(typeof(axios.defaults.headers.common['X-CSRFToken']) === 'string').toBe(true);
});