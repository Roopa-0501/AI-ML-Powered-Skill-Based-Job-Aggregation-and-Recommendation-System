import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:5000"
});

export const processResume = async (file) => {
  const formData = new FormData();
  formData.append("resume", file);

  const response = await API.post("/predict", formData, {
    headers: {
      "Content-Type": "multipart/form-data"
    }
  });

  return response.data;
};