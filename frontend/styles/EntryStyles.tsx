import { StyleSheet } from 'react-native';

const styles = StyleSheet.create({
    entry: {
        display: "flex",
        flexDirection: "column",
        height: "100%",
        alignItems: "center",
        justifyContent: "center",
        backgroundColor: "#0A071E",
    },

    vibifyLogo: {
        marginBottom: 50,
        width: 300,
        height: 118,
    },

    signupInputContainer: {
        display: "flex",
        flexDirection: "column",
        gap: 10,
        marginBottom: 50,
    },

    signupInput: {
        padding: 10,
        height: 50,
        width: 300,
        fontSize: 20,
        borderWidth: 1,
        borderColor: "black",
        backgroundColor: "white",
    },

    signUpButton: {
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        height: 50,
        width: 200,
        backgroundColor: "#e84d42",
    },

    signUpButtonText: {
        textAlign: "center",
        width: "50%",
        fontSize: 20,
        color: "white",
        fontFamily: "Montserrat",
    },

    logInButton: {
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        height: 50,
        width: 200,
        backgroundColor: "#e84d42",
    },

    logInButtonText: {
        textAlign: "center",
        width: "50%",
        fontSize: 20,
        color: "white",
        fontFamily: "Montserrat",
    },
})

export default styles;