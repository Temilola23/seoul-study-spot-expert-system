% -----------------------------------------------------------------------------
%     Study Spot Identifiers (Atomic Facts)
%     These atoms are used as internal keys to identify each study spot
% -----------------------------------------------------------------------------
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
study_spot(left_coffee).
study_spot(eightstreet).
study_spot(metcha_myeongdong).
study_spot(lang_study_cafe_sinchon).



% -----------------------------------------------------------------------------
%               Study Spot Display Names (for UI/Explanations)
% -----------------------------------------------------------------------------
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
study_spot_name(left_coffee, 'Left Coffee').
study_spot_name(eightstreet, '8street').
study_spot_name(metcha_myeongdong, 'METCHA Myeong-dong').
study_spot_name(lang_study_cafe_sinchon, 'Lang Study Cafe (Sinchon)').



% -----------------------------------------------------------------------------
%                    Study Spot Type Classification
% -----------------------------------------------------------------------------
%           Types include: study_cafe, cafe, library, coworking
% -----------------------------------------------------------------------------
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
type(left_coffee, cafe).
type(eightstreet, cafe).
type(metcha_myeongdong, cafe).
type(lang_study_cafe_sinchon, study_cafe).


% -----------------------------------------------------------------------------
%                           Travel Time Encoding
% -----------------------------------------------------------------------------
% Each fact encodes the travel time from a specific origin (sinseol or dongdaemun)
% to a study spot. The time categories are:
% - t0_5     → 0–5 minutes
% - t6_15    → 6–15 minutes
% - t16_30   → 16–30 minutes
% - t31      → 31+ minutes
%
% Format: travel(Spot, TimeFromSinseol, TimeFromDongdaemun).
% -----------------------------------------------------------------------------

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
travel(left_coffee, t16_30, t16_30).
travel(eightstreet, t16_30, t16_30).
travel(metcha_myeongdong, t31, t16_30).
travel(lang_study_cafe_sinchon, t31, t16_30).


% -----------------------------------------------------------------------------
%                           Supported Work Types
% -----------------------------------------------------------------------------
% These facts indicate what kinds of work are suitable at each study spot.
% Options include: deep_focus, casual, group.
% Format: work(Spot, [ListOfSupportedWorkTypes]).
% -----------------------------------------------------------------------------

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
work(left_coffee, [deep_focus]).
work(eightstreet, [casual, group]).
work(metcha_myeongdong, [casual, group]).
work(lang_study_cafe_sinchon, [deep_focus]).


% -----------------------------------------------------------------------------
%                       Power Outlet Availability
% -----------------------------------------------------------------------------
% Whether each spot has power outlets, limited outlets, or none.
% Values: yes, limited, no
% Format: outlets(Spot, Availability).
% -----------------------------------------------------------------------------

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
outlets(left_coffee, yes).
outlets(eightstreet, yes).
outlets(metcha_myeongdong, yes).
outlets(lang_study_cafe_sinchon, yes).


% -----------------------------------------------------------------------------
%                            Study Spot Vibe
% -----------------------------------------------------------------------------
% Indicates the general ambience or vibe of a spot.
% Options: quiet, cozy, lively.
% Format: vibe(Spot, [ListOfVibes]).
% -----------------------------------------------------------------------------

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
vibe(left_coffee, [lively, cozy]).
vibe(eightstreet, [lively]).
vibe(metcha_myeongdong, [quiet, cozy]).
vibe(lang_study_cafe_sinchon, [quiet]).


% -----------------------------------------------------------------------------
%                        Seating Types Available
% -----------------------------------------------------------------------------
% Specifies what seating options are available at each spot.
% Options: individual_desk, open_table, booth, lounge.
% Format: seating(Spot, [ListOfSeatingTypes]).
% -----------------------------------------------------------------------------

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
seating(left_coffee, [open_table, individual_desk]).
seating(eightstreet, [open_table, individual_desk]).
seating(metcha_myeongdong, [open_table, individual_desk]).
seating(lang_study_cafe_sinchon, [individual_desk, open_table, booth]).


% -----------------------------------------------------------------------------
%                                Pricing Category
% -----------------------------------------------------------------------------
% Indicates the relative cost to use the space.
% Values: free, low, medium, high
% Format: price(Spot, PriceCategory).
% -----------------------------------------------------------------------------

price(jaksim_chungmuro, medium).
price(tongue_seongsu, high).
price(mailroom_sindang, medium).
price(solbangul_bakery, medium).
price(coffee_smith_itaewon, low).
price(mouse_rabbit, high).
price(lang_study_cafe, low).
price(starfield_library, free).
price(burnt_seoul, high).
price(from_hearts_coffee, medium).
price(conhas_ddp, medium).
price(endlong, low).
price(mangrove_sinseol_20f, free).
price(mangrove_sinseol_b2, free).
price(mangrove_dongdaemun_15f, free).
price(mangrove_dongdaemun_b1, free).
price(left_coffee, high).
price(eightstreet, medium).
price(metcha_myeongdong, high).
price(lang_study_cafe_sinchon, low).



% -----------------------------------------------------------------------------
%                               Open Late?
% -----------------------------------------------------------------------------
% Whether the study spot is open late into the evening.
% Values: yes, no
% Format: open_late(Spot, IsOpenLate).
% -----------------------------------------------------------------------------

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
open_late(left_coffee, yes).
open_late(eightstreet, yes).
open_late(metcha_myeongdong, yes).
open_late(lang_study_cafe_sinchon, yes).


% -----------------------------------------------------------------------------
%                           Naver Map Links
% -----------------------------------------------------------------------------
% Direct map links to each study spot location.
% Format: link(Spot, NaverURL).
% -----------------------------------------------------------------------------
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
link(left_coffee, 'https://naver.me/5kXfFqGD').
link(eightstreet, 'https://naver.me/Fbin70YB').
link(metcha_myeongdong, 'https://naver.me/GcWrD6IG').
link(lang_study_cafe_sinchon, 'https://naver.me/GJTqa5Gx').





% ===========================
% KB Rules: Utility Predicates
% ===========================

% Converts integer travel time (in minutes) to a categorical time band
% This helps us match user constraints with pre-defined categories
map_travel_times(Minutes, t0_5)   :- Minutes =< 5.
map_travel_times(Minutes, t6_15)  :- Minutes > 5, Minutes =< 15.
map_travel_times(Minutes, t16_30) :- Minutes > 15, Minutes =< 30.
map_travel_times(Minutes, t31)    :- Minutes > 30.



% ======================================
% STRICT MATCHING: All preferences must match exactly
% ======================================

% recommend_spot/11 is a deterministic rule that succeeds only if all user preferences are met exactly
recommend_spot(Origin, MaxMinutes, WorkType, OutletPref, VibePref, SeatingPref, PricePref, OpenLate, Name, Link) :-
    % Convert the user's travel time into a category
    map_travel_times(MaxMinutes, TimeCode),

    % Match travel time based on origin (sinseol or dongdaemun)
    (Origin = sinseol     -> travel(Spot, TimeCode, _)
    ; Origin = dongdaemun -> travel(Spot, _, TimeCode)
    ; throw(error(invalid_origin(Origin), recommend_spot/11))  % catch unexpected origin input
    ),

    % Check if the spot supports user's work type
    work(Spot, WorkList), member(WorkType, WorkList),

    % Check power outlet match
    outlets(Spot, OutletPref),

    % Match preferred vibe (e.g., cozy, quiet)
    vibe(Spot, VibeList), member(VibePref, VibeList),

    % Match seating preference (e.g., booth, lounge)
    seating(Spot, SeatList), member(SeatingPref, SeatList),

    % Match price category (e.g., low, medium, free)
    price(Spot, PricePref),

    % Match if the place is open late
    open_late(Spot, OpenLate),

    % Return name and link of matched spot
    study_spot_name(Spot, Name),
    link(Spot, Link).


% =========================================================
% FLEXIBLE MATCHING: Score-based fallback strategy
% =========================================================

% score_spot/20 assigns a weighted score to each spot and builds an explanation string
% It handles skipped preferences and gives users partial matches when exact ones don't exist
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
    
    % Start with zero score and empty explanation list
    Exp1 = [],
    study_spot(Spot),
    Score1 = 0,
    
    % Determine explanation verbosity (short/long)
    (Mode == "" -> ExplainMode = long ; ExplainMode = Mode),

    
    % === Travel Time ===
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

    % === Work Type ===
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

    % === Outlet Availability ===
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

    % === Vibe Preference ===
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

    % === Seating Preference ===
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

    % === Price Preference ===
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

    % === Open Late Preference ===
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

    % Final output
    Score = Score8,
    study_spot_name(Spot, Name),
    atomic_list_concat(Exp8, " ", Explanation),
    % Get the link for the spot
    link(Spot, Link).


% % =========================================================
% % Utility Predicate to take top-N results from a list
% % =========================================================
top_n(List, N, Output) :-
    length(List, Len),
    Min is min(N, Len),
    length(Output, Min),
    append(Output, _, List).

    

% % ===================================
% % Rule: Find Top Ranked Study Spots
% % ===================================

% % find_top_study_spots/18 takes all user preferences and scoring weights, ranks all options, and returns the top N
find_top_study_spots(Origin, MaxMinutes, TravelWeight, 
    WorkType, WorkWeight,
    OutletPref, OutletWeight,
    VibePref, VibeWeight,
    SeatingPref, SeatingWeight,
    PricePref, PriceWeight,
    OpenLate, LateWeight,
    Mode, TopN, Results) :-

    % Collect all scored results using score_spot/20
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

    % Sort by score ascending and reverse to get descending            
    sort(AllResults, SortedAscending),
    reverse(SortedAscending, SortedDescending),  % Sort by score descending

    (
        % Extract the top-N results (or all if TopN is not set)
        var(TopN)
        -> Results = SortedDescending
        ; top_n(SortedDescending, TopN, Results)
        ).

    