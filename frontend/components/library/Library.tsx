import React from 'react';
import { View, Text } from 'react-native';
import styles from '../../styles/LibraryStyles';

import { Playlist } from '../../api/SongAPI';

import Navbar from '../Navbar';

interface LibraryProps {
    navigation: Object;
}

function Library({ navigation }: LibraryProps) {
    const playlists: Playlist[] = []; // TODO: Pull from SessionState
    
    const noPlaylistsMessage = "You don't have any playlists yet!";

    return (
        <>
            <View style={ styles.library }>
                { playlists.length === 0 &&
                    <View>
                        <Text>
                            { noPlaylistsMessage }
                        </Text>
                    </View> }

                { playlists.map((playlist) => (
                    <View key={`playlist-${playlist.name}`}>
                        <Text>
                            { playlist.name }
                        </Text>
                    </View>
                )) }
            </View>

            <Navbar navigation={ navigation }/>
        </>
    )
}

export default Library;