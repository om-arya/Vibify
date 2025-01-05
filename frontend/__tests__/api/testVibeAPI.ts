import { HttpStatusCode } from 'axios';
import DjangoAPI from '../../client/api/DjangoAPI';
import UserAPI from '../../client/api/UserAPI';
import VibeAPI from '../../client/api/VibeAPI';
import ClientState from '../../client/ClientState';

const djangoAPI = DjangoAPI();
const userAPI = UserAPI();
const vibeAPI = VibeAPI();
const state = ClientState();

beforeAll(async () => {
    await djangoAPI.acquireCsrfToken();

    await userAPI.createUser({
        username: "bob123",
        email: "bob@mail.com",
        password: "bobpass",
        firstName: "Bob",
        lastName: "Smith",
        updateState: true
    });
});

beforeEach(async () => {
    // Reset the vibes state
    await vibeAPI.getUserVibes({
        updateState: true
    });

    const vibes = state.getVibes();
    for (const vibe of vibes) {
        await vibeAPI.deleteVibe({
            name: vibe.name,
            updateState: true
        })
    }
})

afterEach(async () => {
    // Reset the vibes state
    await vibeAPI.getUserVibes({
        updateState: true
    });
    
    const vibes = state.getVibes();
    for (const vibe of vibes) {
        await vibeAPI.deleteVibe({
            name: vibe.name,
            updateState: true
        })
    }
})

afterAll(async () => {
    await userAPI.deleteUser({
        updateState: true
    });
})

test('Create a vibe and delete it', async () => {
    const newVibeName = "Sunny beach day";
    const createVibeStatus = await vibeAPI.createVibe({
        name: newVibeName,
        color: "green",
        updateState: true
    });
    expect(createVibeStatus).toBe(HttpStatusCode.Created);

    const deleteVibeStatus = await vibeAPI.deleteVibe({
        name: newVibeName,
        updateState: true
    });
    expect(deleteVibeStatus).toBe(HttpStatusCode.Ok);
});

test('Create one vibe, check the length of the user\'s vibes, and get the vibes', async () => {
    const createVibeStatus = await vibeAPI.createVibe({
        name: "Purple haze",
        color: "blue",
        updateState: true
    });
    expect(createVibeStatus).toBe(HttpStatusCode.Created);

    const vibes1 = state.getVibes();
    expect(vibes1.length).toBe(1);

    const getUserVibesStatus = await vibeAPI.getUserVibes({
        updateState: true
    });
    expect(getUserVibesStatus).toBe(HttpStatusCode.Ok);

    const vibes2 = state.getVibes();
    expect(vibes2.length).toBe(1);
});

test('Create multiple vibes, check the length of the user\'s vibes, and get the vibes', async () => {
    const createVibeStatus1 = await vibeAPI.createVibe({
        name: "Purple haze",
        color: "blue",
        updateState: true
    });
    expect(createVibeStatus1).toBe(HttpStatusCode.Created);

    const createVibeStatus2 = await vibeAPI.createVibe({
        name: "cats and dogs...",
        color: "green",
        updateState: true
    });
    expect(createVibeStatus2).toBe(HttpStatusCode.Created);

    const createVibeStatus3 = await vibeAPI.createVibe({
        name: "HYPE STUFF",
        color: "red",
        updateState: true
    });
    expect(createVibeStatus3).toBe(HttpStatusCode.Created);

    const vibes1 = state.getVibes();
    expect(vibes1.length).toBe(3);

    const getUserVibesStatus = await vibeAPI.getUserVibes({
        updateState: true
    });
    expect(getUserVibesStatus).toBe(HttpStatusCode.Ok);

    const vibes2 = state.getVibes();
    expect(vibes2.length).toBe(3);
});

test('Create no vibes, check the length of the user\'s vibes, and get the vibes', async () => {
    const vibes1 = state.getVibes();
    expect(vibes1.length).toBe(0);

    const getUserVibesStatus = await vibeAPI.getUserVibes({
        updateState: true
    });
    expect(getUserVibesStatus).toBe(HttpStatusCode.Ok);

    const vibes2 = state.getVibes();
    expect(vibes2.length).toBe(0);
});

test('Update a vibe\'s color', async () => {
    const vibeName = "HYPE STUFF";
    const createVibeStatus = await vibeAPI.createVibe({
        name: vibeName,
        color: "red",
        updateState: true
    });
    expect(createVibeStatus).toBe(HttpStatusCode.Created);

    const newColor = "green";
    const setVibeColorStatus = await vibeAPI.setVibeColor({
        name: vibeName,
        newColor: newColor,
        updateState: true
    })
    expect(setVibeColorStatus).toBe(HttpStatusCode.Ok);

    const vibes = state.getVibes();
    expect(vibes.length).toBe(1);
    expect(vibes[0].color).toBe(newColor);
});