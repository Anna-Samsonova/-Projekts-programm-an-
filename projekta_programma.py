
print("Recepsu un mervienibu parveidotajs")
print("Standarta jaizmanto recepte, kas domata 1 personai!")
print("=====================================================")
receptes_rindas_skaits = int(input("Cik receptes rindas jus gribat lai programma parveido? "))
cilveku_skaits = int(input("Cik cilvekiem recepte paredzeta? "))
print("")
print("Mervienibu opcijas no kuram var parveidot mervienibas: (L; mL; kg; g; lb; fl oz; oz; tbsp; tsp; cups)")

mervienibu_indekss = ["l", "ml", "kg", "g", "lb", "fl oz", "oz", "tbsp", "tsp", "cups"]
mervieniba_uz_kg = [1, 0.001, 1, 0.001, 0.45359237, 0.02957353, 0.0283495231, 0.014786765, 0.004928922, 0.236588237]
kg_uz_2_mervienibu = [1, 1000, 1, 1000, 2.20462262, 33.814, 35.2739619, 67.6280454, 202.8841362, 4.226752838]
rezultats_arr = []

for i in range(receptes_rindas_skaits):
    mervieniba_1 = input("No kadas mervienibas jus gribat parveidot? ").strip().lower()
    mervieniba_2 = input("Uz kadu mervienibu jus gribat parveidot? ").strip().lower()
    mervienibas_skaits = float(input("Cik " + mervieniba_1 + " jus velaties parveidot? "))
    rezultats = round(mervieniba_uz_kg[mervienibu_indekss.index(mervieniba_1)] * kg_uz_2_mervienibu[mervienibu_indekss.index(mervieniba_2)] * cilveku_skaits * mervienibas_skaits, 3)
    rezultats = str(rezultats)
    rezultats += " " + str(mervieniba_2)
    rezultats_arr.append(rezultats)
    print(rezultats + " pievienoti receptei")

print("")
print("Visa recepte prieks " + str(cilveku_skaits) + " cilvekiem")
print("===============================")
for i in rezultats_arr:
    print(i)

