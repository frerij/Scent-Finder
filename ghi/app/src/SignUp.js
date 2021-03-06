import { useToken } from "./authApi";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

function SignUp() {
  // eslint-disable-next-line no-unused-vars
  const [token, login, logout, signup] = useToken();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  // eslint-disable-next-line no-unused-vars
  const [user, setUser] = useState(null);
  const [error, setError] = useState(null);
  const canSignup = username && password && email && firstName && lastName;
  const navigate = useNavigate();

  useEffect(() => {
    async function getCurrentUser() {
      const url = `${process.env.REACT_APP_ACCOUNTS_HOST}/api/accounts/me/`;
      const response = await fetch(url, {
        credentials: "include",
      });
      if (response.ok) {
        const user = await response.json();
        console.log(user);
        setUser(user);
      }
    }
    if (token) {
      getCurrentUser();
    }
  }, [token]);

  return (
    <div>
      {token ? (
        navigate("/")
      ) : (
        <div className="row">
          <div className="offset-4 col-4 mt-4 mb-4">
            <div className="shadow p-4 mt-4">
              <h1>Sign Up</h1>
              <div className="form-floating mb-3">
                <input
                  className="form-control"
                  type="text"
                  onChange={(e) => setUsername(e.target.value)}
                  value={username}
                  placeholder="username"
                />
                <label htmlFor="username">Username</label>
              </div>
              <div className="form-floating mb-3">
                <input
                  className="form-control"
                  type="email"
                  onChange={(e) => setEmail(e.target.value)}
                  value={email}
                  placeholder="email"
                />
                <label htmlFor="email">Email</label>
              </div>
              <div className="form-floating mb-3">
                <input
                  className="form-control"
                  type="text"
                  onChange={(e) => setFirstName(e.target.value)}
                  value={firstName}
                  placeholder="first name"
                />
                <label htmlFor="first_name">First Name</label>
              </div>
              <div className="form-floating mb-3">
                <input
                  className="form-control"
                  type="text"
                  onChange={(e) => setLastName(e.target.value)}
                  value={lastName}
                  placeholder="last name"
                />
                <label htmlFor="last_name">Last Name</label>
              </div>
              <div className="form-floating mb-3">
                <input
                  className="form-control"
                  type="password"
                  onChange={(e) => setPassword(e.target.value)}
                  value={password}
                  placeholder="password"
                />
                <label htmlFor="password">Password</label>
              </div>
              <p>
                {error ? (
                  <div
                    className="alert alert-danger"
                    role="alert"
                    dangerouslySetInnerHTML={{ __html: error }}
                  />
                ) : null}
              </p>
              <button
                className="btn btn-primary"
                disabled={!canSignup}
                onClick={async () =>
                  setError(
                    await signup(username, password, email, firstName, lastName)
                  )
                }
              >
                Sign up
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default SignUp;
