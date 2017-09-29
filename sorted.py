

def sort_strings(s, delim):
    return sorted(s.split(delim))


def main():
    s = '''ageNextBirthday: Int
classOfLife: Int
levelRiskRate: BigDecimal
baseRiskPremium: BigDecimal
loadingRiskPremium: BigDecimal
decisionRiskPremium: BigDecimal
basePreCommissionPemium: BigDecimal
decisionPreCommissionPremium: BigDecimal
basePremium: BigDecimal
decisionPremium: BigDecimal
finalPremium: BigDecimal
premiumPayable: BigDecimal
netDecisionPremium: BigDecimal
loadRate: BigDecimal
riskGap: BigDecimal
loadGap: BigDecimal
expenseGap: BigDecimal
coverAmount: BigDecimal
accept: String
comment: String'''
    [print(x) for x in sort_strings(s, '\n')]

if __name__ == '__main__':
    main()
