import { StyleSheet } from 'react-native';

const styles = StyleSheet.create({
    navbar: {
        position: "absolute",
        right: 0,
        bottom: 0,
        left: 0,
        display: "flex",
        flexDirection: "row",
        gap: 50,
        width: "100%",
        height: 80,
        alignItems: "center",
        justifyContent: "center",
        backgroundColor: "black",
    },

    navbarButton: {
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
    },

    navbarButtonLabel: {
        color: "white",
    },
})

export default styles;