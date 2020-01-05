def token_loop(self):
        tokens = []
        tokens_matched = []
        for i in range(1,11):
            input("next? i = "+str(i))        
            e = self.driver.find_element_by_class_name("tokens li:nth-of-type("+str(i)+")")
            current_token = e.text
            if current_token in tokens:
                tokens.append(e.text+'_DUPLICATE')
            else:
                tokens.append(e.text)
        print(str(tokens))

        import story1
        d = story1.expand_dict(story1.dict)
        print(d)
        for j in range(len(tokens)):
            input('next?')
            t = tokens[j]
            print("token= " + t)
            if t in tokens_matched:
                continue

            t_match = d[t]
            print(t + " --> " + t_match)
            
            e_token = self.driver.find_element_by_class_name("tokens li:nth-of-type("+str(j+1)+")")
            print(e_token.text)
            e_token.click()

            if t == t_match:
                t_match = t_match+'_DUPLICATE'
                print('Modified t_match : ' + t_match)

            j_match = tokens.index(t_match)
            e_token_matched = self.driver.find_element_by_class_name("tokens li:nth-of-type("+str(j_match+1)+")")
            print(e_token_matched.text)
            e_token_matched.click()

            tokens_matched.append(t)
            tokens_matched.append(t_match)