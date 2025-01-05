import axios, { HttpStatusCode } from "axios";
import DjangoAPI from '../../client/api/DjangoAPI';

const djangoAPI = DjangoAPI();

test('Request a CSRF token to save as an Axios header', async () => {
    const responseStatus = await djangoAPI.acquireCsrfToken();
    expect(responseStatus).toBe(HttpStatusCode.Ok);
    expect(typeof(axios.defaults.headers.common['X-CSRFToken']) === 'string').toBe(true);
});