import "./Home.css";

function Home(){

    return(

        <div className="home">

            <section className="hero">

                <div>

                    <h1>

                        AI Powered Financial Analyst

                    </h1>

                    <p>

                        Upload annual reports, chat with documents,
                        generate financial forecasts and receive
                        institutional-quality investment analysis.

                    </p>

                    <button>

                        Get Started

                    </button>

                </div>

                <img

                src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"

                alt="finance"

                />

            </section>


            <section className="features">

                <div className="feature-card">

                    📄

                    <h2>Upload Reports</h2>

                    <p>

                        Upload Annual Reports,
                        10-Ks and Financial Statements.

                    </p>

                </div>

                <div className="feature-card">

                    🤖

                    <h2>GraphRAG Chat</h2>

                    <p>

                        Ask any question about
                        company reports.

                    </p>

                </div>

                <div className="feature-card">

                    📈

                    <h2>Forecasting</h2>

                    <p>

                        Prophet & XGBoost
                        financial forecasting.

                    </p>

                </div>

                <div className="feature-card">

                    🧠

                    <h2>AI Intelligence</h2>

                    <p>

                        Multi-Agent financial
                        investment reports.

                    </p>

                </div>

            </section>

        </div>

    )

}

export default Home;