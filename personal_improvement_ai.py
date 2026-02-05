print("🧠 AI Personal Improvement Engine \n")

productivity = int(input("Productivity score today (0–100): "))
energy = int(input("Energy level (1–5): "))
stress = int(input("Stress level (1–5): "))
sleep = float(input("Sleep hours last night: "))
exercise = int(input("Exercise minutes today: "))

print("\n📊 PERSONAL ANALYSIS")

# Productivity
if productivity >= 80:
    print("✅ Productivity: Excellent")
elif productivity >= 60:
    print("⚠️ Productivity: Moderate")
else:
    print("❌ Productivity: Low")

# Energy & Stress
if energy <= 2 or stress >= 4:
    state = "Overloaded"
else:
    state = "Stable"

print("Overall State:", state)

print("\n🧭 AI IMPROVEMENT RECOMMENDATIONS")

if productivity < 70:
    print("• Reduce task overload and focus on top priorities")
if energy < 3:
    print("• Improve sleep and take short breaks")
if stress >= 4:
    print("• Practice stress-relief activities (walk, meditation)")
if sleep < 7:
    print("• Aim for at least 7–8 hours of sleep")
if exercise < 30:
    print("• Add at least 30 minutes of physical activity")
if productivity >= 80 and stress <= 2:
    print("• You are doing great — maintain this routine")
