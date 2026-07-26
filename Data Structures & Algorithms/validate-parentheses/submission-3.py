class Solution:
    def isValid(self, s: str) -> bool:
        chars = {'(':')', '[':']', '{':'}'}

        s_list = list(s)
        n = len(s_list)

        fechador_atual = ''
        abridores = []          # stack para guardar os abridores
        aberto = False

        for i in range(n):
            char = s_list[i]    # o caractere analisado

            # é um abridor
            if char in chars.keys():
                aberto = True
                abridores.append(i)
                fechador_atual = chars[char]
            
            # é um fechador
            elif char in chars.values():
                
                if char == fechador_atual:
                    abridores.pop()     # retira o idx do abridor atual

                    # se ainda há abridores abertos restantes
                    if len(abridores) > 0:
                        aberto = True  
                        prox_abridor = abridores[-1]                    # índice do abridor anterior ao último  
                        fechador_atual = chars[s_list[prox_abridor]]    # fechador do abridor anterior
                    
                    else:
                        aberto = False
                        fechador_atual = ''
                
                else:
                    return False

            # não é um caractere válido
            else:
                return False

        return not aberto       
                

            
