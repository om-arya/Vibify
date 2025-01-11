import { HttpStatusCode } from 'axios';
import AuthAPI from '../../client/api/AuthAPI';
import UserAPI from '../../client/api/UserAPI';
import ClientState from '../../client/ClientState';

const authAPI = AuthAPI();
const userAPI = UserAPI();
const state = ClientState();

beforeAll(async () => {
    await authAPI.acquireCsrfToken();
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
        firstName: "Bob Bob",
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

test('Authenticate a user by username and email', async () => {
    const createUserStatus = await userAPI.createUser({
        username: "bob123",
        email: "bob@mail.com",
        password: "bobpass",
        firstName: "Bob",
        lastName: "Smith",
        updateState: true
    });
    expect(createUserStatus).toBe(HttpStatusCode.Created);

    const authenticateUserByUsernameStatus = await userAPI.authenticateUserByUsername({
        username: "bob123",
        password: "bobpass"
    });
    expect(authenticateUserByUsernameStatus).toBe(HttpStatusCode.Ok);

    const authenticateUserByEmailStatus = await userAPI.authenticateUserByEmail({
        email: "bob@mail.com",
        password: "bobpass"
    });
    expect(authenticateUserByEmailStatus).toBe(HttpStatusCode.Ok);
});

test('Attempt to authenticate a user by username and email', async () => {
    const createUserStatus = await userAPI.createUser({
        username: "bob123",
        email: "bob@mail.com",
        password: "bobpass",
        firstName: "Bob",
        lastName: "Smith",
        updateState: true
    });
    expect(createUserStatus).toBe(HttpStatusCode.Created);

    const authenticateUserByUsernameStatus1 = await userAPI.authenticateUserByUsername({
        username: "ghost",
        password: "bobpass"
    });
    expect(authenticateUserByUsernameStatus1).toBe(HttpStatusCode.NotFound);

    const authenticateUserByUsernameStatus2 = await userAPI.authenticateUserByUsername({
        username: "bob123",
        password: "bobpa"
    });
    expect(authenticateUserByUsernameStatus2).toBe(HttpStatusCode.Unauthorized);

    const authenticateUserByUsernameStatus3 = await userAPI.authenticateUserByUsername({
        username: "bob123",
        password: "bobpass"
    });
    expect(authenticateUserByUsernameStatus3).toBe(HttpStatusCode.Ok);

    const authenticateUserByEmailStatus1 = await userAPI.authenticateUserByEmail({
        email: "ghost@mail.com",
        password: "bobpass"
    });
    expect(authenticateUserByEmailStatus1).toBe(HttpStatusCode.NotFound);

    const authenticateUserByEmailStatus2 = await userAPI.authenticateUserByEmail({
        email: "bob@mail.com",
        password: "bobpa"
    });
    expect(authenticateUserByEmailStatus2).toBe(HttpStatusCode.Unauthorized);

    const authenticateUserByEmailStatus3 = await userAPI.authenticateUserByEmail({
        email: "bob@mail.com",
        password: "bobpass"
    });
    expect(authenticateUserByEmailStatus3).toBe(HttpStatusCode.Ok);
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

    const authenticateUserByUsernameStatus = await userAPI.authenticateUserByUsername({
        username: "bob123",
        password: "johnpass",
        updateState: true
    })
    expect(authenticateUserByUsernameStatus).toBe(HttpStatusCode.Ok);

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

    const authenticateUserByUsernameStatus1 = await userAPI.authenticateUserByUsername({
        username: "bob123",
        password: "bobpass"
    });
    expect(authenticateUserByUsernameStatus1).toBe(HttpStatusCode.Ok);

    const deleteUserStatus = await userAPI.deleteUser({
        updateState: true
    });
    expect(deleteUserStatus).toBe(HttpStatusCode.Ok);

    const authenticateUserByUsernameStatus2 = await userAPI.authenticateUserByUsername({
        username: "bob123",
        password: "bobpass"
    });
    expect(authenticateUserByUsernameStatus2).toBe(HttpStatusCode.NotFound);
});