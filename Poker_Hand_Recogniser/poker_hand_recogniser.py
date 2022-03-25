# This Program takes in the hole cards (player hand) and community cards (river) as argument to the function
# hand and returns what hand the player has got. It also returns this hand with required tiebreaker cards
# to be used when necessary.

def card_rank(card):
    # Converts a card into a more useful integer data type
    rank_conversions = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                       '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    
    return rank_conversions[card]

def check_straight(cards):
    # Checks if a hand contains a straight or not
    cards = set(cards)
    
    cards_ranked = [*map(card_rank, cards)]    # Convert cards into integers
    cards_ranked.sort(reverse = True)
        
    count = 0   
    
    # Check if 5 cards in a row exists
    for i, number in enumerate(cards_ranked):
        count += 1
        
        if count == 5:
            cards = sorted(cards, key = card_rank, reverse = True)
            return cards[i-4:i+1]
        
        if (number - 1) not in cards_ranked:
            count = 0
            continue

def check_straight_flush(suits_count, hand):
    # Check if there is more than 5 occurances of a suit that also forms a straight
    
    if any(count >= 5 for count in suits_count.values()):
        flush_suit = [k for k, v in suits_count.items() if v >= 5][0]
        flush_ranks = [card[:-1] for card in hand if card[-1] == flush_suit]
        
        if check_straight(flush_ranks):           
            return check_straight(flush_ranks)
            
def check_four_of_a_kind(rank_count, hand):
    
    if 4 in rank_count.values():
        card = [card for card, count in rank_count.items() if count == 4][0]
        tiebreak = max(filter(lambda x: x != card, hand), key = card_rank)  # Highest non paired card
        
        return [card, tiebreak]

def check_full_house(rank_count, hand):
    
    if 3 in rank_count.values() and 2 in rank_count.values():
        three = [card for card, count in rank_count.items() if count == 3][0]
        two = [card for card, count in rank_count.items() if count == 2][0]
        
        return [three, two]

def check_flush(suit_count, hand):
    
    if any(count >= 5 for count in suit_count.values()):
        flush_suit = [k for k, v in suit_count.items() if v >= 5][0]
        flush_ranks = [card[:-1] for card in hand if card[-1] == flush_suit]
        
        flush_ranks.sort(key = card_rank, reverse = True)
        return flush_ranks[:5]
        
def check_three_of_a_kind(rank_count, ranks):
    
    if 3 in rank_count.values():
        three = [k for k, v in rank_count.items() if v == 3][0]
        tiebreak1 = max(filter(lambda x: x != three, ranks), key = card_rank)   # Highest non paired card
        tiebreak2 = max(filter(lambda x: x != three and x != tiebreak1, ranks), key = card_rank)    # Second highest non paired card
        
        return [three, tiebreak1, tiebreak2]
    
def check_two_pair(rank_count, ranks):
    
    values = list(rank_count.values())
    
    if values.count(2) == 2:
        high = max([k for k, v in rank_count.items() if v == 2], key = card_rank)
        low = min([k for k, v in rank_count.items() if v == 2], key = card_rank)
        tiebreak = max(filter(lambda x: x != high and x != low, ranks), key = card_rank)    # Highest non paired card
        
        return [high, low, tiebreak]

def check_pair(rank_count, ranks):
    
    ranks.sort(key = card_rank, reverse = True)
    
    if 2 in rank_count.values():
        pair = [k for k, v in rank_count.items() if v == 2][0]
        ranks = [*filter(lambda x: x != pair, ranks)]   # 3 highest non paired cards
        
        return [pair] + ranks[:3]
        
        
def hand(hole_cards, community_cards):

    ranks = [x[:-1] for x in (hole_cards + community_cards)]    
    suits = [x[-1] for x in (hole_cards + community_cards)]   
    
    rank_count = {card: ranks.count(card) for card in ranks}
    suits_count = {suit: suits.count(suit) for suit in suits}
    
    # Check hand
    if check_straight_flush(suits_count, hole_cards + community_cards):
        return "straight-flush", check_straight_flush(suits_count, hole_cards + community_cards)
    
    if check_four_of_a_kind(rank_count, ranks):
        return "four-of-a-kind", check_four_of_a_kind(rank_count, ranks)
    
    if check_full_house(rank_count, ranks):
        return "full house", check_full_house(rank_count, ranks)
    
    if check_flush(suits_count, hole_cards + community_cards):
        return "flush", check_flush(suits_count, hole_cards + community_cards)

    if check_straight(ranks):
        return "straight", check_straight(ranks)
    
    if check_three_of_a_kind(rank_count, ranks):
        return "three-of-a-kind", check_three_of_a_kind(rank_count, ranks)
    
    if check_two_pair(rank_count, ranks):
        return "two pair", check_two_pair(rank_count, ranks)
    
    if check_pair(rank_count, ranks):
        return "pair", check_pair(rank_count, ranks)
    
    else:
        ranks.sort(key = card_rank, reverse = True)        
        return "nothing", ranks[:5]