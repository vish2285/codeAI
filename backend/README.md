# codeAI  

Welcome to **codeAI** 👋  

This project is built around one simple idea: **let Clerk handle logins, and let our backend double-check who you are without having to ask Clerk every single time.**  

---

## 🚀 How it Works  

Think of it like going to a concert:  

- **Frontend (the ticket booth)**  
  - You walk up, show your ID, and Clerk (our security guard) says: *“Cool, you’re in.”*  
  - They give you a **ticket** (a JWT token).  
  - That ticket proves you’re legit and you can now head into the show.  

- **Backend (the venue gates)**  
  - Instead of calling the guard again every time you walk around the venue, the gate staff just check your ticket.  
  - If it looks real (signed properly, not expired), you get through.  
  - If not, you’re stopped right there.  

The magic here is that the backend can check tickets **locally**, using Clerk’s secret key (`JWT_KEY`), so it doesn’t need to “phone home” to Clerk’s servers every time. This makes the whole thing faster and more reliable.  

---

## 🔄 Flow  

1. **User logs in** → Clerk takes care of authentication.  
2. **Clerk hands out a JWT** → This token is cryptographically signed.  
3. **Frontend attaches JWT to requests** → Sent in the `Authorization` header.  
4. **Backend checks the JWT** → Using Clerk’s `JWT_KEY`, it verifies:  
   - Is this token real?  
   - Has it expired?  
   - Who does it belong to?  
5. **Backend responds** →  
   - ✅ If valid → the request goes through.  
   - ❌ If invalid → access denied.  

---

## 🎯 Why This Setup Rocks  

- 🚀 **Fast** – No constant back-and-forth with Clerk servers.  
- 🔒 **Secure** – Tokens are signed; if someone tampers with one, we’ll know.  
- 🌍 **Scalable** – Works smoothly even if Clerk’s servers are busy.  
- 🛠 **Simple** – Once set up, it’s just “log in → get token → validate token.”  

---

## 📊 Visual Flow  

```plaintext
[ You log in ]
       ↓
[ Clerk (frontend) ]
   ✔ Authenticates you
   🎟 Gives you a JWT
       ↓
[ Backend ]
   🔑 Uses JWT_KEY to check your token
   ✅ If valid → access granted
   ❌ If invalid → access denied
