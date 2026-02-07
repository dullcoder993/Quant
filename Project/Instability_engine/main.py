import pandas as pd
from data.input.db_data import read_prices_for_lppl
from analysis.rolling_windows import run_rolling_lppl
from analysis.convergence_metrics import lppl_convergence_metrics
from analysis.convergence_tests import calculate_criticality_index
from analysis.hazard_score import calculate_hazard_score
from analysis.regime_classifier import classify_lppl_regime
# NEW: Import your DB connection to save results
# Assuming you have a database/storage.py or similar
# from database.storage import save_lppl_signal
import datetime
import os

 

def main():
    symbol = "TCS.NS"

    df = read_prices_for_lppl(symbol)
    if df is None or len(df) < 120:
        raise ValueError("Not enough data for LPPL")

    t = df["t"].values
    log_prices = df["log_price"].values
    t_today = t[-1]

    # --- THE ANALYSIS ENGINE ---
    lppl_result = run_rolling_lppl(t, log_prices)
    
    print(f"DEBUG: Windows analyzed: {lppl_result.get('total_windows')}")
    print(f"DEBUG: Successful fits: {len(lppl_result['fits'])}")

    metrics = lppl_convergence_metrics(lppl_result["fits"])
    print(f"DEBUG: Metrics calculated: {metrics}")

    criticality = calculate_criticality_index(
        metrics,
        lppl_result["probability_score"]
    )

    avg_tc = metrics["tc_median"] if metrics else None

    hazard = calculate_hazard_score(
        criticality_index=criticality,
        avg_tc=avg_tc,
        tc_std=metrics["tc_std"] if metrics else None,
        t_today=t_today
    )

    regime = classify_lppl_regime(criticality)

    # --- THE MITHRIL OUTPUT ---
    output = {
        "symbol": symbol,
        "t_today": int(t_today),
        "criticality": float(criticality),
        "hazard": float(hazard),
        "regime": regime,
        "tc_median": float(avg_tc) if avg_tc else None,
        "n_fits": metrics["n_fits"] if metrics else 0
    }

    print("\n--- FINAL SIGNAL ---")
    print(output)
    def log_mithril_signal(symbol, output):
        log_entry = {
            "timestamp": datetime.datetime.now(),
            "symbol": symbol,
            "criticality": output['criticality'],
            "hazard": output['hazard'],
            "regime": output['regime'],
            "predicted_crash": output['tc_median']
        }
        # For now, let's append to a CSV so you can see the history
        df_log = pd.DataFrame([log_entry])
        df_log.to_csv("mithril_signals.csv", mode='a', header=not os.path.exists("mithril_signals.csv"), index=False)
        print(f"Signal logged to mithril_signals.csv")
    # NEXT LOGIC: SAVE TO DATABASE
    # If the regime is CRITICAL, you should log it for backtesting
    # save_lppl_signal(output)

if __name__ == "__main__":
    main()