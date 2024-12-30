import VibifyAPI from '../api/VibifyAPI';

// https://jestjs.io/docs/getting-started

async function testAcquireCsrfToken() {
    const vibifyApi = VibifyAPI();
    const responseData = await vibifyApi.acquireCsrfToken();
    console.log(responseData);
    console.log(responseData['csrfToken']);
}