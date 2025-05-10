import { initializeApp } from "firebase/app";
import { getAuth, signInWithEmailAndPassword } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyDU1SVXNrTn9hmOy03nxe8wp8451Bv9bDQ",
  authDomain: "vacaci-da6bd.firebaseapp.com",
  projectId: "vacaci-da6bd",
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

const email = "roiky82@gmail.com";
const password = "vacaci";

signInWithEmailAndPassword(auth, email, password)
  .then(async (userCredential) => {
    const token = await userCredential.user.getIdToken();
    console.log("✅ TOKEN JWT:");
    console.log(token);
  })
  .catch((error) => {
    console.error("❌ Error al autenticar:", error.message);
  });
