import React, { useState } from 'react';
import { View, Text, Pressable } from 'react-native';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { Vibe } from '../../client/api/VibeAPI';
import SpotifyAPI from '../../client/api/SpotifyAPI';
import styles from '../../styles/HomeStyles';

import Navbar from '../Navbar';
import VibeCard from './VibeCard';

interface HomeProps {
    navigation: any;
}

function Home({ navigation }: HomeProps) {
    const spotifyAPI = SpotifyAPI();

    const samplevibe1: Vibe = {
        name: "Bob",
        color: "green",
    };

    const samplevibe2: Vibe = {
        name: "Steve",
        color: "red",
    };

    const vibes: Vibe[] = [samplevibe1, samplevibe2]; // TODO: Pull vibes from SessionState

    const noVibesMessage = "You don't have any vibes!"

    function openVibeMaker() {
        navigation.navigate("VibeMaker");
    }

    function openAccountPanel() {
        navigation.navigate("Account");
    }

    async function openSpotifyAuthPage() {
        const spotifyAuthURL = await spotifyAPI.getSpotifyAuthURL();
        if (typeof spotifyAuthURL === 'number') {
            // TODO: Error page
            return;
        }

        window.location.href = spotifyAuthURL;
    }

    return (
        <>
            <View style={ styles.home }>
                <View style={ styles.homeTopBar }>
                    <Pressable style={ styles.accountButton }
                            onPressOut={ () => openAccountPanel() }>
                        <MaterialCommunityIcons name="account" size={ 24 } color="black" />
                    </Pressable>
                </View>

                <Pressable style={ styles.createVibeButton }
                           onPressOut={ () => openVibeMaker() }>
                    <Text style={ styles.createVibeButtonText }>
                        + Create Vibe
                    </Text>
                </Pressable>

                { vibes.length === 0 &&
                    <View>
                        <Text>
                            { noVibesMessage }
                        </Text>
                    </View> }

                { vibes.map((vibe) => (
                    <VibeCard key={ vibe.name } name={ vibe.name } color={ vibe.color } />
                )) }
            </View>

            <Navbar navigation={ navigation }/>
        </>
    )
}

export default Home;