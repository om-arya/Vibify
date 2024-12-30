const SessionState = () => {
    function setCsrfToken(csrfToken: string) {
        sessionStorage.setItem('csrfToken', csrfToken);
    }

    function getCsrfToken() {
        const csrfTokenJSON = sessionStorage.getItem('csrfToken');
        return csrfTokenJSON ? JSON.parse(csrfTokenJSON) as string : null;
    }

    return { setCsrfToken, getCsrfToken }
}

export default SessionState;