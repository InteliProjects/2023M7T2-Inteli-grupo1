  import NextAuth, { NextAuthOptions } from "next-auth";
  import CredentialsProvider from 'next-auth/providers/credentials';

  const URL_API = 'http://54.224.65.58:3001'
  const authOptions = {
    providers: [
      CredentialsProvider({
        credentials: {
          email: { label: "Email", type: "text", placeholder: "email" },
          password: {
            label: "Password",
            type: "password",
            placeholder: "password",
          },
        },
        async authorize(credentials, req) {
          const { email, password } = credentials;
            const response = await fetch(`${URL_API}/auth/login`, {
              method: "POST",
              body: JSON.stringify({ email, password }),
              headers: { "Content-Type": "application/json" },
            });
          if (response.status === 200) {
            const jsonResponse = await response.json();
            const user_response = await fetch(`${URL_API}/user`, {
              method: "GET",
              headers: {
                Authorization: `Bearer ${jsonResponse.token}`
              },
            });
            if (user_response.status === 200) {
              const {user} = await user_response.json();
              delete jsonResponse.message;
              return { ...jsonResponse, name: user.name, email: user.email, roles: user.role };
            } else {
              return null;
            }
          } else {
            return null;
          }
        },
      }),
    ],
    callbacks: {
      async jwt({ token, user }) {
        if (user) {
          token.accessToken = user.token;
          token.roles = user.roles;
        }
        return token;
      },
      async session({ session, token }) {
        if(token=! null){
          session.accessToken = token.accessToken;
      }
      return session;
      },
    },
    session: {
      maxAge: 60 * 60 * 2, // A sessão expirará após 2 horas
    },
    secret: process.env.NEXTAUTH_SECRET,
    pages:{
      signIn: '/singin',
      signOut: '/singin',
    }
  };

  module.exports = NextAuth(authOptions);
