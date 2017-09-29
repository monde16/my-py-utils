def main():
    map = {
        "subscriberName": "text",
        "subscriberPassword": "text",
        "subscriberCode": "text",
        "appId": "text",
        "segment": "text",
        "productDescription": "text",
        "termType": "text",
        "escalation": "text",
        "disability": "text",
        "gender": "text",
        "bmi": "text",
        "dateOfBirth": "text",
        "smoker": "text",
        "monthlyIncome": "text",
        "educationLevel": "text",
        "inceptionDate": "text",
        "em": "text",
        "pm": "text",
        "lifeDecision": "text",
        "occDecision": "text",
        "adwDecision": "text",
        "commissionSacrifice": "text",
        "commissionModel": "text",
        "coverAmount": "text"
    }

    for k, v in map.items():
        print(f"""<div class="form-group">
        <label for="{k}">{k}</label>
        <input type="{v}" name="{k}">
    </div>""")


if __name__ == '__main__':
    main()
