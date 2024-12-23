import { StyleSheet } from 'react-native';

const styles = StyleSheet.create({
    home: {
        display: "flex",
        height: "100%",
        padding: 30,
        alignItems: "center",
        backgroundColor: "white",
    },

    homeTopBar: {
        display: "flex",
        width: "100%",
        alignItems: "flex-end",
    },

    accountButton: {
        display: "flex",
    },

    createVibeButton: {
        padding: 10,
        textAlign: "center",
        borderRadius: 20,
        backgroundColor: "green",
    },
    
    createVibeButtonText: {
        color: "white",
    },

    /* VIBE MAKER */

    vibeMaker: {
        display: "flex",
        height: "100%",
        padding: 30,
        alignItems: "center",
        backgroundColor: "white",
    },

    vibeMakerTopBar: {
        display: "flex",
        width: "100%",
        alignItems: "flex-start",
    },

    makeItButton: {
        padding: 10,
        textAlign: "center",
        borderRadius: 20,
        backgroundColor: "blue",
    },

    makeItButtonText: {
        color: "white",
    },

    /* ACCOUNT PANEL */

    accountPanel: {
        padding: 30,
    },

    /* DELETE ACCOUNT PANEL */

    deleteAccountPanel: {
        padding: 30,
    },

    /* LOGIN PANEL */

    loginPanel: {
        padding: 30,
    },

    /* SIGNUP PANEL */

    signupPanel: {
        padding: 30,
    },
})

export default styles;