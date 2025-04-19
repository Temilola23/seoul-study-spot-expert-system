% study spots identifiers
study_spot(jaksim_chungmuro).
study_spot(tongue_seongsu).
study_spot(mailroom_sindang).
study_spot(solbangul_bakery).
study_spot(coffee_smith_itaewon).
study_spot(mouse_rabbit).
study_spot(lang_study_cafe).
study_spot(starfield_library).
study_spot(burnt_seoul).
study_spot(from_hearts_coffee).
study_spot(conhas_ddp).
study_spot(endlong).
study_spot(mangrove_sinseol_20f).
study_spot(mangrove_sinseol_b2).
study_spot(mangrove_dongdaemun_15f).
study_spot(mangrove_dongdaemun_b1).

% study spots names
study_spot_name(jaksim_chungmuro, 'Jaksim Study Cafe Chungmuro Station Branch').
study_spot_name(tongue_seongsu, 'Tongue Seongsu space').
study_spot_name(mailroom_sindang, 'Mailroom Sindang').
study_spot_name(solbangul_bakery, 'Solbangul Bakery').
study_spot_name(coffee_smith_itaewon, 'Coffee Smith Itaewon Hamilton Branch').
study_spot_name(mouse_rabbit, 'MouseRabbit').
study_spot_name(lang_study_cafe, 'Lang Study Cafe').
study_spot_name(starfield_library, 'Starfield Library').
study_spot_name(burnt_seoul, 'BurntSeoul').
study_spot_name(from_hearts_coffee, 'From Hearts Coffee').
study_spot_name(conhas_ddp, 'conhas ddp').
study_spot_name(endlong, 'Endlong').
study_spot_name(mangrove_sinseol_20f, 'Mangrove Sinseol 20F').
study_spot_name(mangrove_sinseol_b2, 'Mangrove Sinseol B2').
study_spot_name(mangrove_dongdaemun_15f, 'Mangrove Dongdaemun 15F').
study_spot_name(mangrove_dongdaemun_b1, 'Mangrove Dongdaemun B1').

% study spots types
type(jaksim_chungmuro, study_cafe).
type(tongue_seongsu, cafe).
type(mailroom_sindang, cafe).
type(solbangul_bakery, cafe).
type(coffee_smith_itaewon, cafe).
type(mouse_rabbit, cafe).
type(lang_study_cafe, study_cafe).
type(starfield_library, library).
type(burnt_seoul, cafe).
type(from_hearts_coffee, cafe).
type(conhas_ddp, cafe).
type(endlong, cafe).
type(mangrove_sinseol_20f, coworking).
type(mangrove_sinseol_b2, coworking).
type(mangrove_dongdaemun_15f, coworking).
type(mangrove_dongdaemun_b1, coworking).

% travel times to study spots
travel(jaksim_chungmuro, t16_30, t6_15).
travel(tongue_seongsu, t16_30, t16_30).
travel(mailroom_sindang, t6_15, t6_15).
travel(solbangul_bakery, t16_30, t16_30).
travel(coffee_smith_itaewon, t16_30, t16_30).
travel(mouse_rabbit, t16_30, t16_30).
travel(lang_study_cafe, t16_30, t6_15).
travel(starfield_library, t31, t31).
travel(burnt_seoul, t16_30, t16_30).
travel(from_hearts_coffee, t0_5, t16_30).
travel(conhas_ddp, t16_30, t0_5).
travel(endlong, t0_5, t16_30).
travel(mangrove_sinseol_20f, t0_5, t16_30).
travel(mangrove_sinseol_b2, t0_5, t16_30).
travel(mangrove_dongdaemun_15f, t16_30, t0_5).
travel(mangrove_dongdaemun_b1, t16_30, t0_5).

% work type at study spots
work(jaksim_chungmuro, [deep_focus]).
work(tongue_seongsu, [deep_focus, casual, group]).
work(mailroom_sindang, [casual, group]).
work(solbangul_bakery, [deep_focus, casual, group]).
work(coffee_smith_itaewon, [casual, group]).
work(mouse_rabbit, [casual, group]).
work(lang_study_cafe, [deep_focus]).
work(starfield_library, [casual, group]).
work(burnt_seoul, [deep_focus, casual, group]).
work(from_hearts_coffee, [casual, group]).
work(conhas_ddp, [casual, group]).
work(endlong, [casual, group]).
work(mangrove_sinseol_20f, [casual, group]).
work(mangrove_sinseol_b2, [deep_focus]).
work(mangrove_dongdaemun_15f, [casual, group]).
work(mangrove_dongdaemun_b1, [deep_focus]).

% power outlets available at the study spots
outlets(jaksim_chungmuro, yes).
outlets(tongue_seongsu, yes).
outlets(mailroom_sindang, yes).
outlets(solbangul_bakery, no).
outlets(coffee_smith_itaewon, yes).
outlets(mouse_rabbit, yes).
outlets(lang_study_cafe, yes).
outlets(starfield_library, no).
outlets(burnt_seoul, limited).
outlets(from_hearts_coffee, limited).
outlets(conhas_ddp, yes).
outlets(endlong, yes).
outlets(mangrove_sinseol_20f, yes).
outlets(mangrove_sinseol_b2, yes).
outlets(mangrove_dongdaemun_15f, yes).
outlets(mangrove_dongdaemun_b1, yes).


% study spot vibe
vibe(jaksim_chungmuro, [quiet]).
vibe(tongue_seongsu, [quiet, cozy]).
vibe(mailroom_sindang, [lively, cozy]).
vibe(solbangul_bakery, [quiet, cozy]).
vibe(coffee_smith_itaewon, [lively, cozy]).
vibe(mouse_rabbit, [lively, cozy]).
vibe(lang_study_cafe, [quiet]).
vibe(starfield_library, [lively, cozy]).
vibe(burnt_seoul, [quiet, cozy]).
vibe(from_hearts_coffee, [lively, cozy]).
vibe(conhas_ddp, [lively, cozy]).
vibe(endlong, [lively, cozy]).
vibe(mangrove_sinseol_20f, [lively]).
vibe(mangrove_sinseol_b2, [quiet]).
vibe(mangrove_dongdaemun_15f, [lively]).
vibe(mangrove_dongdaemun_b1, [quiet]).

% table options for study spots
seating(jaksim_chungmuro, [individual_desk, open_table, booth]).
seating(tongue_seongsu, [open_table, lounge]).
seating(mailroom_sindang, [individual_desk]).
seating(solbangul_bakery, [open_table, lounge, individual_desk]).
seating(coffee_smith_itaewon, [lounge, individual_desk]).
seating(mouse_rabbit, [lounge, individual_desk]).
seating(lang_study_cafe, [individual_desk, open_table, booth]).
seating(starfield_library, [lounge, individual_desk]).
seating(burnt_seoul, [lounge, individual_desk]).
seating(from_hearts_coffee, [lounge, individual_desk]).
seating(conhas_ddp, [open_table, lounge, individual_desk]).
seating(endlong, [open_table, lounge, individual_desk]).
seating(mangrove_sinseol_20f, [open_table, lounge, individual_desk]).
seating(mangrove_sinseol_b2, [booth, open_table, lounge, individual_desk]).
seating(mangrove_dongdaemun_15f, [open_table, lounge, individual_desk]).
seating(mangrove_dongdaemun_b1, [booth, open_table, lounge, individual_desk]).

% pricing for study spots
price(jaksim_chungmuro, medium).
price(tongue_seongsu, free).
price(mailroom_sindang, free).
price(solbangul_bakery, free).
price(coffee_smith_itaewon, free).
price(mouse_rabbit, free).
price(lang_study_cafe, low).
price(starfield_library, free).
price(burnt_seoul, free).
price(from_hearts_coffee, free).
price(conhas_ddp, free).
price(endlong, free).
price(mangrove_sinseol_20f, free).
price(mangrove_sinseol_b2, free).
price(mangrove_dongdaemun_15f, free).
price(mangrove_dongdaemun_b1, free).


% closing time period for study spots
open_late(jaksim_chungmuro, yes).
open_late(tongue_seongsu, no).
open_late(mailroom_sindang, yes).
open_late(solbangul_bakery, no).
open_late(coffee_smith_itaewon, yes).
open_late(mouse_rabbit, yes).
open_late(lang_study_cafe, yes).
open_late(starfield_library, no).
open_late(burnt_seoul, no).
open_late(from_hearts_coffee, no).
open_late(conhas_ddp, no).
open_late(endlong, no).
open_late(mangrove_sinseol_20f, yes).
open_late(mangrove_sinseol_b2, yes).
open_late(mangrove_dongdaemun_15f, yes).
open_late(mangrove_dongdaemun_b1, yes).

% naver maps links for study spots
link(jaksim_chungmuro, 'https://naver.me/xIeG1TdK').
link(tongue_seongsu, 'https://naver.me/xucLmQmc').
link(mailroom_sindang, 'https://naver.me/FbOdq3Ih').
link(solbangul_bakery, 'https://naver.me/xyTrdE2s').
link(coffee_smith_itaewon, 'https://naver.me/F2ZMn9WD').
link(mouse_rabbit, 'https://naver.me/IFg3GfzQ').
link(lang_study_cafe, 'https://naver.me/5GpiGLBb').
link(starfield_library, 'https://naver.me/xeANnNSv').
link(burnt_seoul, 'https://naver.me/FqWrZ18N').
link(from_hearts_coffee, 'https://naver.me/5vc0JZgw').
link(conhas_ddp, 'https://naver.me/5iTrmPMh').
link(endlong, 'https://naver.me/xxYDo1wf').
link(mangrove_sinseol_20f, 'https://naver.me/xKEpyD9q').
link(mangrove_sinseol_b2, 'https://naver.me/xKEpyD9q').
link(mangrove_dongdaemun_15f, 'https://naver.me/GlJMRxlV').
link(mangrove_dongdaemun_b1, 'https://naver.me/GlJMRxlV').




% KB Rules
% rules for time conversion from integer to categorical
map_travel_times(Minutes, t0_5) :- Minutes =< 5.
map_travel_times(Minutes, t6_15) :- Minutes > 5, Minutes =< 15.
map_travel_times(Minutes, t16_30) :- Minutes > 15, Minutes =< 30.
map_travel_times(Minutes, t31) :- Minutes > 30.


% strict rule for matching based on preference
recommend_spot(Origin, MaxMinutes, WorkType, OutletPref, VibePref, SeatingPref, PricePref, OpenLate, Name, Link) :-
    map_travel_times(MaxMinutes, TimeCode),
    (Origin=sinseol -> travel(Spot, TimeCode, _)
    ; Origin=dongdaemun -> travel(Spot, _, TimeCode)
    ; throw(error(invalid_origin(Origin), recommend_spot/11))
    ),

    work(Spot, WorkList), member(WorkType, WorkList),
    outlets(Spot, OutletPref),
    vibe(Spot, VibeList), member(VibePref, VibeList),
    seating(Spot, SeatList), member(SeatingPref, SeatList),
    price(Spot, PricePref),
    open_late(Spot, OpenLate),
    study_spot_name(Spot, Name),
    link(Spot, Link).
    
% fallback strategy based on preference scoring + ranking
score_spot(
    Origin, MaxMinutes, TravelWeight, 
    WorkType, WorkWeight, 
    OutletPref, OutletWeight, 
    VibePref, VibeWeight, 
    SeatingPref, SeatingWeight,
    PricePref, PriceWeight,
    OpenLate, LateWeight,
    Mode, Name, Link, 
    Score, Explanation) :-
    % start scoring from 0
    Exp1 = [],
    study_spot(Spot),
    Score1 = 0,

    (var(Mode) -> ExplainMode = long ; ExplainMode = Mode),

    % weight travel time by TravelWeight
    map_travel_times(MaxMinutes, TimeCode),
     (
        (   (Origin == sinseol,    travel(Spot, TimeCode, _))
    ;   (Origin == dongdaemun, travel(Spot, _, TimeCode))
)
        ->  Score2 is Score1 + TravelWeight,
        (ExplainMode == short -> Msg2 = "✔ travel. " ; Msg2 = "Matched travel time. "),
        % append explanation for matched travel time
        append(Exp1, [Msg2], Exp2)
        ;   Score2 is Score1,
        (ExplainMode == short -> Msg2 = "✘ travel. " ; Msg2 = "Did not match travel time. "),
        append(Exp1, [Msg2], Exp2)
    ),


    work(Spot, WorkList), 
    (   
        WorkType == skip
            -> Score3 is Score2, 
            (ExplainMode == short -> Msg3 = "✔ work type. " ; Msg3 = "No work type preference. "),
            append(Exp2, [Msg3], Exp3)
            ; (member(WorkType, WorkList) 
                -> Score3 is Score2 + WorkWeight,
                (ExplainMode == short -> Msg3 = "✔ work type. " ; Msg3 = "Matched work type preferences. "),
                append(Exp2, [Msg3], Exp3) 
                ; Score3 is Score2, 
                (ExplainMode == short -> Msg3 = "✘ work type. " ; Msg3 = "Did not match work type preferences. "),
                append(Exp2, [Msg3], Exp3)
            )
    ),


    outlets(Spot, OutletVal), 
    (   
        OutletPref == skip
            -> Score4 is Score3, 
            (ExplainMode == short -> Msg4 = "✔ outlet preference. " ; Msg4 = "No outlet preference. "),
            append(Exp3, [Msg4], Exp4)
            ; (OutletVal == OutletPref 
                -> Score4 is Score3 + OutletWeight, 
                (ExplainMode == short -> Msg4 = "✔ outlet preference. " ; Msg4 = "Matched outlets preferences. "),
                append(Exp3, [Msg4], Exp4)
                ; Score4 is Score3,
                (ExplainMode == short -> Msg4 = "✘ outlet preference. " ; Msg4 = "Did not match outlet preferences. "),
                append(Exp3, [Msg4], Exp4)
            )
        ),

    % weight vibe by 1
    vibe(Spot, VibeList),
    (
        VibePref == skip 
        -> Score5 is Score4, 
        (ExplainMode == short -> Msg5 = "✔ vibe preference. " ; Msg5 = "No vibe preference. "),
        append(Exp4, [Msg5], Exp5)
        ; (member(VibePref, VibeList) 
            -> Score5 is Score4 + VibeWeight, 
            (ExplainMode == short -> Msg5 = "✔ vibe preference. " ; Msg5 = "Matched vibe preferences. "),
            append(Exp4, [Msg5], Exp5)
            ; Score5 is Score4,
            (ExplainMode == short -> Msg5 = "✘ vibe preference. " ; Msg5 = "Did not match vibe preferences. "),
            append(Exp4, [Msg5], Exp5)
        )
    ),

    % weight seating by 1
    seating(Spot, SeatList),
    (
        SeatingPref == skip 
        -> Score6 is Score5, 
        (ExplainMode == short -> Msg6 = "✔ seating preference. " ; Msg6 = "No seating preference. "),
        append(Exp5, [Msg6], Exp6)
        ; (member(SeatingPref, SeatList) 
            -> Score6 is Score5 + SeatingWeight,
            (ExplainMode == short -> Msg6 = "✔ seating preference. " ; Msg6 = "Matched seating preferences. "),
            append(Exp5, [Msg6], Exp6) 
            ; Score6 is Score5,
            (ExplainMode == short -> Msg6 = "✘ seating preference. " ; Msg6 = "Did not match seating preferences. "),
            append(Exp5, [Msg6], Exp6)
        )
    ),

    % weight price by 2
    price(Spot, PriceVal),
    (
        PricePref == skip
        -> Score7 is Score6, 
        (ExplainMode == short -> Msg7 = "✔ price preference. " ; Msg7 = "No price preference. "),
        append(Exp6, [Msg7], Exp7)
        ; (PriceVal == PricePref 
            -> Score7 is Score6 + PriceWeight, 
            (ExplainMode == short -> Msg7 = "✔ price preference. " ; Msg7 = "Matched price preferences. "),
            append(Exp6, [Msg7], Exp7)
            ; Score7 is Score6, 
            (ExplainMode == short -> Msg7 = "✘ price preference. " ; Msg7 = "Did not match price preferences. "),
            append(Exp6, [Msg7], Exp7)
        )
        ),

    % weight opening time period by 1
    open_late(Spot, OpenVal),
    (
        OpenLate == skip
        -> Score8 is Score7,
        (ExplainMode == short -> Msg8 = "✔ opening time preference. " ; Msg8 = "No opening time preference. "), 
        append(Exp7, [Msg8], Exp8)
        ; (OpenVal == OpenLate 
            -> Score8 is Score7 + LateWeight,
            (ExplainMode == short -> Msg8 = "✔ opening time preference. " ; Msg8 = "Matched opening time preferences. "),
            append(Exp7, [Msg8], Exp8) 
            ; Score8 is Score7, 
            (ExplainMode == short -> Msg8 = "✘ opening time preference. " ; Msg8 = "Did not match opening time preferences. "),
            append(Exp7, [Msg8], Exp8)
        )
        ),

    % output
    Score = Score8,
    study_spot_name(Spot, Name),
    % explanation for the score
    atomic_list_concat(Exp8, " ", Explanation),
    
    link(Spot, Link).


% predicate to get the top "n" spots
top_n(List, N, Output) :-
    length(Output, N),
    append(Output, _, List).
    


% Get the top study spots!
find_top_study_spots(Origin, MaxMinutes, TravelWeight, 
    WorkType, WorkWeight,
    OutletPref, OutletWeight,
    VibePref, VibeWeight,
    SeatingPref, SeatingWeight,
    PricePref, PriceWeight,
    OpenLate, LateWeight,
    Mode, TopN, Results) :-
    findall(
        [Score, Name, Link, Explanation],
        score_spot(
            Origin, MaxMinutes, TravelWeight, 
            WorkType, WorkWeight, 
            OutletPref, OutletWeight, 
            VibePref, VibeWeight, 
            SeatingPref, SeatingWeight,
            PricePref, PriceWeight,
            OpenLate, LateWeight,
            Mode, Name, Link, 
            Score, Explanation) ,
        AllResults
    ),
    sort(AllResults, SortedAscending),
    reverse(SortedAscending, SortedDescending),  % Sort by score descending

    (
        var(TopN)
        -> Results = SortedDescending
        ; top_n(SortedDescending, TopN, Results)
        ).

    