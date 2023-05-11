import { OceanClient } from "../src/index";

const PORT = process.env.PORT || "8000";
const URL = "http://localhost:" + PORT;
const ocean = new OceanClient(URL);

export default ocean;
