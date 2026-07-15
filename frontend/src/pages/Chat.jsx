import {useState} from "react";
import api from "../services/api";
import "./Chat.css";

function Chat(){
    const [question,setQuestion]=useState("");
    const [answer,setAnswer]=useState("");
    const [note,setNote]=useState("");

    const ask=async()=>{
        try{
            const res=await api.post("/chat",{ question });
            setAnswer(res.data.answer);
        }
        catch(err){
            console.log(err);
            setAnswer("Error: could not get response from server.");
        }
    };

    return(
        <div className="chat-page">
            <div className="chat-grid container">
                <div className="chat-left card">
                    <h1>Chat with Financial Reports</h1>
                    <p>Ask any question about the uploaded reports or financial data.</p>

                    <textarea
                        rows="6"
                        value={question}
                        onChange={(e)=>setQuestion(e.target.value)}
                        placeholder="Type your question here..."
                    />

                    <div className="chat-actions">
                        <input
                            value={note}
                            onChange={(e)=>setNote(e.target.value)}
                            placeholder="Optional note / context"
                        />
                        <button onClick={ask}>Ask</button>
                    </div>
                </div>

                <div className="chat-right card">
                    <h2>Response</h2>
                    { answer ? (
                        <div className="answer-card">{answer}</div>
                    ) : (
                        <div className="answer-empty">No response yet. Ask a question to see results here.</div>
                    )}
                </div>
            </div>
        </div>
    );
}

export default Chat;