import random

def choose_options():
  options = ('piedra', 'papel', 'tijera')
  user_option = input('''
  Por favor escoja una opcion 
  Piedra, Papel o Tijera: ''')
  user_option = user_option.lower()

  if not user_option in options:
    print('Ingrese una opcion valida')
    return None, None
  
  machine_option = random.choice(options)
  print(f'PC escogio {machine_option}!')
  return user_option, machine_option

def check_rules(user_option, machine_option, user_wins, machine_wins, name):
  if user_option == machine_option:
    print('Esto es un empate!!  No hay punto para ninguno')
  elif user_option == 'piedra':
    if machine_option == 'tijera':
      print(f'Piedra gana a tijera, {name} gano!!!')
      user_wins += 1
    else:
      print('Papel gana a piedra, Computador gano!!!')
      machine_wins += 1
  elif user_option == 'papel':
    if machine_option == 'piedra':
      print(f'Papel gana a piedra, {name} gano!!!')
      user_wins += 1
    else:
      print('Tijera gana a papel, Computador gano!!!')
      machine_wins += 1
  elif user_option == 'tijera':
    if machine_option == 'papel':
      print(f'Tijera gana a Papel, {name} gano!!!')
      user_wins += 1
    else:
      print('Piedra gana a Tijera, Computador gano!!!')
      machine_wins += 1
  return user_wins, machine_wins

def run_game():  
  user_wins = 0
  machine_wins = 0
  rounds = 1
  name = input('Ingresa tu nombre: ').title()
  
  while True:
    print(' ')
    print('*' * 20)
    print(f'''ROUND {rounds}''')
    print('*' * 20)
    
    user_option, machine_option = choose_options()
    if user_option == None:
      continue
    user_wins, machine_wins = check_rules(user_option, machine_option,     user_wins, machine_wins, name)
    rounds += 1  
  
    print(f'''
    {name} = {user_wins} PC = {machine_wins}
    ''')
    if user_wins == 3:
      print(f'Felicitaciones {name}, ganasteeee!!')
      break
    elif machine_wins == 3:
      print(f'Sigue intentando {name}!!')
      break

run_game()
