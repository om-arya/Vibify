declare global {
  interface User {
    username: string;
    email: string;
    firstName: string;
    lastName: string;
  };

  interface Vibe {
    name: string;
    color: string;
  };
}
  
export default global;