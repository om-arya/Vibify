const VibeDeserializer = () => {
    /**
     * Deserialize the given array of vibes from
     * its server JSON representation to its client
     * object representation.
     * 
     * @param vibes array in its server JSON
     *              representation.
     * @returns the vibes array in its client
     *          object representation.
     */
    function array_from_json(vibes) {
        return vibes.map((vibe) => {
            return {
                name: vibe.fields.name,
                color: vibe.fields.color
            } as Vibe;
        }) as Vibe[];
    }

    return { array_from_json };
}

export default VibeDeserializer;