# ================================================================
# 15. GET PROCESSED FEATURE NAMES
# ================================================================

try:
    feature_names = preprocessor.get_feature_names_out()

    # Clean feature names for easier readability
    feature_names = [
        name.replace("num__", "")
            .replace("cat__", "")
            .replace("onehot__", "")
            .replace("remainder__", "")
        for name in feature_names
    ]

    print("Processed Feature Names:")
    for i, name in enumerate(feature_names, 1):
        print(f"{i}. {name}")

except Exception as e:
    print("Could not automatically retrieve feature names.")
    print("Error:", e)

    # Fallback: create generic feature names
    feature_names = [
        f"Feature_{i+1}"
        for i in range(X_train_processed.shape[1])
    ]

    print("\nUsing generic feature names:")
    print(feature_names)
    