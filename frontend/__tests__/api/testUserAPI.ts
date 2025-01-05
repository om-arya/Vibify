import { HttpStatusCode } from 'axios';
import DjangoAPI from '../../client/api/DjangoAPI';
import UserAPI from '../../client/api/UserAPI';
import ClientState from '../../client/ClientState';

const djangoAPI = DjangoAPI();
const userAPI = UserAPI();
const state = ClientState();

beforeAll(async () => {
    await djangoAPI.acquireCsrfToken();
});

afterEach(async () => {
    // Reset the user state
    if (state.getUser()) {
        await userAPI.deleteUser({
            updateState: true
        })
    }
})

test('Create a user and delete it', async () => {
    const createUserStatus = await userAPI.createUser({
        username: "bob123",
        email: "bob@mail.com",
        password: "bobpass",
        firstName: "Bob",
        lastName: "Smith",
        updateState: true
    });
    expect(createUserStatus).toBe(HttpStatusCode.Created);

    const deleteUserStatus = await userAPI.deleteUser({
        updateState: true
    });
    expect(deleteUserStatus).toBe(HttpStatusCode.Ok);
});

test('Fail to create a user with a used username', async () => {
    const createUserStatus1 = await userAPI.createUser({
        username: "bob123",
        email: "bob@mail.com",
        password: "bobpass",
        firstName: "Bob",
        lastName: "Smith",
        updateState: true
    });
    expect(createUserStatus1).toBe(HttpStatusCode.Created);

    const createUserStatus2 = await userAPI.createUser({
        username: "bob123",
        email: "john@mail.com",
        password: "johnpass",
        firstName: "John",
        lastName: "Roberts",
        updateState: true
    });
    expect(createUserStatus2).toBe(HttpStatusCode.Conflict);
});

test('Fail to create a user with a used email', async () => {
    const createUserStatus1 = await userAPI.createUser({
        username: "bob123",
        email: "bob@mail.com",
        password: "bobpass",
        firstName: "Bob",
        lastName: "Smith",
        updateState: true
    });
    expect(createUserStatus1).toBe(HttpStatusCode.Created);

    const createUserStatus2 = await userAPI.createUser({
        username: "johnny456",
        email: "bob@mail.com",
        password: "johnpass",
        firstName: "John",
        lastName: "Roberts",
        updateState: true
    });
    expect(createUserStatus2).toBe(HttpStatusCode.Conflict);
});

test('Get an existing user by username and email', async () => {
    const createUserStatus = await userAPI.createUser({
        username: "bob123",
        email: "bob@mail.com",
        password: "bobpass",
        firstName: "Bob",
        lastName: "Smith",
        updateState: true
    });
    expect(createUserStatus).toBe(HttpStatusCode.Created);

    const getUserByUsernameStatus = await userAPI.getUserByUsername({
        username: "bob123"
    });
    expect(getUserByUsernameStatus).toBe(HttpStatusCode.Ok);

    const getUserByEmailStatus = await userAPI.getUserByEmail({
        email: "bob@mail.com"
    });
    expect(getUserByEmailStatus).toBe(HttpStatusCode.Ok);
});

test('Fail to get a nonexistent user by username and email', async () => {
    const getUserByUsernameStatus = await userAPI.getUserByUsername({
        username: "bob123"
    });
    expect(getUserByUsernameStatus).toBe(HttpStatusCode.NotFound);

    const getUserByEmailStatus = await userAPI.getUserByEmail({
        email: "bob@mail.com"
    });
    expect(getUserByEmailStatus).toBe(HttpStatusCode.NotFound);
});

test('Update a user\'s fields', async () => {
    const createUserStatus = await userAPI.createUser({
        username: "bob123",
        email: "bob@mail.com",
        password: "bobpass",
        firstName: "Bob",
        lastName: "Smith",
        updateState: true
    });
    expect(createUserStatus).toBe(HttpStatusCode.Created);

    const setUserFirstNameStatus = await userAPI.setUserFirstName({
        newFirstName: "Jimmy",
        updateState: true
    });
    expect(setUserFirstNameStatus).toBe(HttpStatusCode.Ok);

    const setUserLastNameStatus = await userAPI.setUserLastName({
        newLastName: "John",
        updateState: true
    });
    expect(setUserLastNameStatus).toBe(HttpStatusCode.Ok);

    const setUserEmailStatus = await userAPI.setUserEmail({
        newEmail: "jimmy@mail.com",
        updateState: true
    });
    expect(setUserEmailStatus).toBe(HttpStatusCode.Ok);

    const setUserPasswordStatus = await userAPI.setUserPassword({
        newPassword: "johnpass"
    });
    expect(setUserPasswordStatus).toBe(HttpStatusCode.Ok);

    const getUserByUsernameStatus = await userAPI.getUserByUsername({
        username: "bob123",
        updateState: true
    })
    expect(getUserByUsernameStatus).toBe(HttpStatusCode.Ok);

    const updatedUser = state.getUser();
    expect(updatedUser.username).toBe("bob123");
    expect(updatedUser.firstName).toBe("Jimmy");
    expect(updatedUser.lastName).toBe("John");
    expect(updatedUser.email).toBe("jimmy@mail.com");
});

test('Delete a user and fail to get it', async () => {
    const createUserStatus = await userAPI.createUser({
        username: "bob123",
        email: "bob@mail.com",
        password: "bobpass",
        firstName: "Bob",
        lastName: "Smith",
        updateState: true
    });
    expect(createUserStatus).toBe(HttpStatusCode.Created);

    const getUserStatus1 = await userAPI.getUserByUsername({
        username: "bob123"
    });
    expect(getUserStatus1).toBe(HttpStatusCode.Ok);

    const deleteUserStatus = await userAPI.deleteUser({
        updateState: true
    });
    expect(deleteUserStatus).toBe(HttpStatusCode.Ok);

    const getUserStatus2 = await userAPI.getUserByUsername({
        username: "bob123"
    });
    expect(getUserStatus2).toBe(HttpStatusCode.NotFound);
});