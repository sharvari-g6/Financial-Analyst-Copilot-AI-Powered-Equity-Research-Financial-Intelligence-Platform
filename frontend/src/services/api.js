import axios from "axios";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000/api",
    headers: {
        "Content-Type": "application/json",
    },
});

// Global request counter to emit loading events for the UI
let pendingRequests = 0;
const emitLoading = (loading) => {
    try {
        window.dispatchEvent(new CustomEvent("api-loading", { detail: { loading } }));
    } catch (e) {
        // ignore in non-browser environments
    }
};

api.interceptors.request.use((config) => {
    pendingRequests += 1;
    emitLoading(true);
    return config;
}, (error) => {
    pendingRequests = Math.max(0, pendingRequests - 1);
    if (pendingRequests === 0) emitLoading(false);
    return Promise.reject(error);
});

api.interceptors.response.use((response) => {
    pendingRequests = Math.max(0, pendingRequests - 1);
    if (pendingRequests === 0) emitLoading(false);
    return response;
}, (error) => {
    pendingRequests = Math.max(0, pendingRequests - 1);
    if (pendingRequests === 0) emitLoading(false);
    return Promise.reject(error);
});

export default api;