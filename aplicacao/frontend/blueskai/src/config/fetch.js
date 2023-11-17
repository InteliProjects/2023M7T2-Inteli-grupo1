const { authOptions } = require("@/app/api/auth/[...nextauth]/route");
const { getServerSession } = require("next-auth");
const { isServerSide } = require("./environment");
const { getSession } = require("next-auth/react");

const fetchInstance = async (endpoint, options) => {
  let baseURL = "http://localhost:3001";

  let session = null;
  if (isServerSide()) {
    session = await getServerSession(authOptions);
    baseURL = "http://backend:3001";
  } else {
    session = await getSession();
  }

  if (!session) {
    throw new Error("No session found");
  }

  const finalURL = `${baseURL}${endpoint}`;

  const mergedOptions = {
    ...options,
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${session.accessToken}`,
      ...(options && options.headers),
    },
  };

  const response = await fetch(finalURL, mergedOptions);

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.message || "Fetch request failed");
  }

  return await response.json();
};

// Exemplo de uso
// fetchInstance("/api/data", { method: "GET" })
//   .then(data => console.log(data))
//   .catch(error => console.error(error));
