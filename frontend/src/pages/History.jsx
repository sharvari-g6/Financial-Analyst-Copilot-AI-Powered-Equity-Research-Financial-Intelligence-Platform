import {useEffect,useState} from "react";
import {useNavigate} from "react-router-dom";
import api from "../services/api";
import "./History.css";

function History(){

    const [reports,setReports]=useState([]);

    const navigate=useNavigate();

    useEffect(()=>{

        loadHistory();

    },[]);

    const loadHistory=async()=>{

        try{

            const res=await api.get("/analysis");

            setReports(res.data);

        }

        catch(err){

            console.log(err);

        }

    };

    return(

        <div className="history-page">

            <h1>📂 Analysis History</h1>

            <div className="history-grid">

            {

                reports.map((report)=>(

                    <div

                    className="history-card"

                    key={report.id}

                    >

                        <h2>{report.company}</h2>

                        <h3>{report.year}</h3>

                        <p>

                            Uploaded :

                            {

                                new Date(

                                    report.upload_date

                                ).toLocaleDateString()

                            }

                        </p>

                        <button

                        onClick={()=>navigate(

                            `/analysis/${report.company}/${report.year}`

                        )}

                        >

                            Open Analysis

                        </button>

                    </div>

                ))

            }

            </div>

        </div>

    );

}

export default History;