#RafaelsDambis18.10.2024
vecums = int(input("Kāds ir tavs vecums"))#terminālis tev jautās tavu vecumu


if vecums < 13 :
  print("tu esi bērns")#ja tavs vecums ir mazāks par 13 gadiem, tad tu esi bērns
elif vecums >= 20:
  print("tu esi pieaugušais")#ja tavs vecums ir lielāks vai vienāds par 20 gadiem, tad tu esi pieaugušais
elif vecums >= 13 and vecums <= 19:
  print("tu esi tīnis")#ja tavs vecums ir vienāds vai lielāks par 13 gadiem un vienāds vai mazāks par 20 gadiem, tad tu esi tīnis
  