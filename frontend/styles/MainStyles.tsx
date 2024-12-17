import { StyleSheet } from 'react-native';

const styles = StyleSheet.create({
    navbar: {
        position: "absolute",
        right: 0,
        bottom: 0,
        left: 0,
        display: "flex",
        width: "100%",
        height: 100,
        alignItems: "center",
        justifyContent: "center",
        backgroundColor: "black"
    },

    navbarText: {
        color: "white",
    },
})

export default styles;