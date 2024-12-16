import React from 'react';
import { View, Image, PixelRatio, Pressable, Text, TextInput } from 'react-native';
import styles from '../styles/EntryStyles';

const Entry: React.FC<any> = ({ navigation }) => {

    return (
        <View style={styles.entry}>
            <Image style={styles.vibifyLogo}
                   source={require("../assets/vibify-logo.png")}
                   width={PixelRatio.getPixelSizeForLayoutSize(150)}
                   height={PixelRatio.getPixelSizeForLayoutSize(59)}/>
            
            <View style={styles.signupInputContainer}>
                <TextInput style={styles.signupInput} placeholder="Username"></TextInput>
                <TextInput style={styles.signupInput} placeholder="Password" secureTextEntry={true}></TextInput>
            </View>

            <Pressable style={styles.signUpButton} onPressOut={() => navigation.navigate("Home")}>
                <Text style={styles.signUpButtonText}>
                    Sign Up
                </Text>
            </Pressable>

            <Pressable style={styles.logInButton} onPressOut={() => navigation.navigate("Home")}>
                <Text style={styles.signUpButtonText}>
                    Log In
                </Text>
            </Pressable>
        </View>
    )
}

export default Entry;