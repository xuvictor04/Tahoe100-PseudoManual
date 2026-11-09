---
symbol: "TTC3"
type: "gene"
col: 11313
ensembl_id: "ENSG00000182670"
name: "tetratricopeptide repeat domain 3"
location: "21q22.13"
module: 56
arm: "+"
pooled_cpm: 462.89
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 24
n_dd_up_clean: 2
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# TTC3

*tetratricopeptide repeat domain 3* — 21q22.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.25× (z +8.6, q 6e-15, up in 33 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (SHP-77 2.34×, C32 2.68×, A-427 1.72×, SNU-423 1.90×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Tucidinostat (drug)]] 5 µM in 4 lines (RKO 1.87×, HepG2/C3A 1.82×, SW1417 1.48×, SW480 1.41×); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SNU-423 1.95×, C32 2.12×, NCI-H1573 1.84×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.572× (z -15.7, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COG6]] (+0.84, fdr 7e-06), [[SEC63]] (+0.79, fdr 7e-06), [[SEC23A]] (+0.77, fdr 7e-06); moves opposite to [[ZNF629]] (-0.67, fdr 7e-06), [[GABPB1]] (-0.64, fdr 1e-05), [[E2F3]] (-0.63, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CARD6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11313.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (SHP-77 2.34×, C32 2.68×, A-427 1.72×, SNU-423 1.90×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Tucidinostat (drug)]] 5 µM in 4 lines (RKO 1.87×, HepG2/C3A 1.82×, SW1417 1.48×, SW480 1.41×); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SNU-423 1.95×, C32 2.12×, NCI-H1573 1.84×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +8.6 | 6e-15 | 33/48 (RKO, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.7 | 5e-04 | 20/48 (HepG2/C3A, RKO, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +4.6 | 5e-04 | 22/44 (SHP-77, C32, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.18× | +4.6 | 5e-04 | 21/49 (RKO, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.6 | 5e-04 | 22/48 (LOX-IMVI, SHP-77, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +4.0 | 0.006 | 19/48 (SHP-77, HepG2/C3A, …) | all doses, flat |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.034 | 19/48 (NCI-H2030, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[Trimetrexate (drug)]] 5 µM |  | 1.09× | +3.5 | 0.034 | 3/49 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.10× | +3.4 | 0.047 | 7/49 (BT-474, SHP-77, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 1.12× | +3.3 | 0.053 | 11/49 (C32, NCI-H1573, …) | two highest doses |  |
| [[Levobupivacaine (hydrochloride) (drug)]] 0.5 µM |  | 1.12× | +3.3 | 0.053 | 0/48 | all doses, flat |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.10× | +3.2 | 0.053 | 2/48 (HT-29, KATO III) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.12× | +3.2 | 0.053 | 21/49 (SNU-423, C32, …) | rises with dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11313.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.572×** | -15.7 | 0e+00 | 46/48 (hTERT-HPNE, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.661×** | -14.2 | 1e-43 | 38/48 (HS-578T, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.592×** | -14.1 | 4e-43 | 42/48 (RPMI-7951, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.608×** | -14.0 | 4e-42 | 41/48 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.622×** | -13.3 | 2e-38 | 43/48 (A-172, RPMI-7951, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.631×** | -12.9 | 3e-36 | 37/48 (HS-578T, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.624×** | -12.7 | 4e-35 | 41/47 (SW480, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.676×** | -11.0 | 4e-26 | 37/48 (H4, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.694×** | -10.3 | 7e-23 | 39/48 (SW 900, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.706×** | -9.7 | 1e-20 | 37/48 (NCI-H1573, SW 900, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.713×** | -9.5 | 1e-19 | 40/48 (NCI-H1573, H4, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.767×** | -9.3 | 7e-19 | 32/49 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.723×** | -9.1 | 5e-18 | 39/48 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.794×** | -8.5 | 8e-16 | 36/48 (HS-578T, A498, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.749×** | -8.1 | 2e-14 | 40/48 (hTERT-HPNE, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.603×** | -7.4 | 4e-12 | 36/49 (SW 900, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.757×** | -7.4 | 6e-12 | 36/47 (RPMI-7951, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11313. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 744 | 0 | 17 (5 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.235× (z -19.3) |
| [[H4 (line)]] | wt | 800 | 0 | 15 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.323× (z -14.7) |
| [[HOP62 (line)]] | alt | 539 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -19.5) |
| [[NCI-H1792 (line)]] | alt | 582 | 0 | 13 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.327× (z -17.0) |
| [[NCI-H460 (line)]] | wt | 251 | 1 (1 ⚠) | 11 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 1.67× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 0.05 µM 0.466× (z -13.7) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.532× (z -11.3) |
| [[SW 900 (line)]] | alt | 481 | 0 | 12 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.324× (z -16.0) |
| [[CFPAC-1 (line)]] | alt | 512 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -15.1) |
| [[A-172 (line)]] | wt | 581 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -21.0) |
| [[A549 (line)]] | wt | 326 | 0 | 9 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.336× (z -14.8) |
| [[AsPC-1 (line)]] | alt | 371 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.339× (z -19.7) |
| [[HS-578T (line)]] | alt | 690 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -24.9) |
| [[NCI-H1573 (line)]] | alt | 422 | 1 (1 ⚠) | 7 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.84× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.476× (z -11.8) |
| [[A498 (line)]] | wt | 622 | 0 | 7 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.445× (z -13.8) |
| [[NCI-H2030 (line)]] | alt | 381 | 0 | 7 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.554× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.555× (z -11.7) |
| [[SW480 (line)]] | alt | 573 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -14.8) |
| [[HepG2_C3A (line)]] | wt | 352 | 4 (3 ⚠) | 2 | [[Tucidinostat (drug)]] 5 µM 1.82× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.588× (z -9.7) |
| [[KATO III (line)]] | alt | 366 | 0 | 6 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.420× (z -11.4) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.446× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 399 | 1 (1 ⚠) | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.70× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.530× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 388 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.521× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 398 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -21.2) |
| [[SNU-423 (line)]] | alt | 332 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 1.95× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -14.6) |
| [[C32 (line)]] | wt | 303 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 0.05 µM 0.392× (z -12.4) |
| [[HT-29 (line)]] | alt | 359 | 0 | 5 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.529× (z -10.0) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.565× (z -9.3) |
| [[J82 (line)]] | alt | 278 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.492× (z -11.4) |
| [[LoVo (line)]] | wt | 677 | 0 | 5 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.466× (z -11.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.601× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 447 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -13.6) |
| [[SHP-77 (line)]] | alt | 346 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.34× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 411 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.72× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.585× (z -13.6) |
| [[RKO (line)]] | wt | 318 | 3 (2 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.87× (z +12.5) | [[Digitoxin (drug)]] 5 µM 0.537× (z -9.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 548 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.429× (z -12.3) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.520× (z -9.5) |
| [[SW1417 (line)]] | alt | 459 | 1 (1 ⚠) | 3 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.52× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.608× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.633× (z -9.1) |
| [[AN3 CA (line)]] | alt | 475 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.478× (z -9.9) |
| [[CHP-212 (line)]] | wt | 440 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -9.6) |
| [[HCT15 (line)]] | alt | 789 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.421× (z -10.6) |
| [[Hs 766T (line)]] | wt | 480 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.459× (z -10.8) |
| [[PANC-1 (line)]] | alt | 319 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.69× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 0.5 µM 0.572× (z -9.8) |
| [[SW48 (line)]] | wt | 710 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.623× (z -10.7) |
| [[COLO 205 (line)]] | alt | 553 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.345× (z -11.5) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 630 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.619× (z -10.9) |
| [[LS 180 (line)]] | wt | 701 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.504× (z -10.7) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 523 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.524× (z -9.0) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 753 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -10.2) |
| [[BT-474 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 621 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 430 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 291 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 485 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 405 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 271 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 328 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11313), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG6]] | +0.84 | +0.87 / +0.78 | both halves | 7e-06 |  |
| [[SEC63]] | +0.79 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[SEC23A]] | +0.77 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[SEC31A]] | +0.76 | +0.80 / +0.68 | both halves | 7e-06 |  |
| [[PDXDC1]] | +0.76 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[KDELR2]] | +0.75 | +0.79 / +0.65 | both halves | 7e-06 |  |
| [[SUCO]] | +0.74 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[LMAN1]] | +0.74 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[COPB1]] | +0.74 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.74 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[GFPT1]] | +0.73 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[PDXDC2P]] | +0.73 | +0.78 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF629]] | -0.67 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[GABPB1]] | -0.64 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[E2F3]] | -0.63 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[SFT2D3]] | -0.62 | -0.59 / -0.38 | both halves | 7e-05 |  |
| [[DDX20]] | -0.61 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[CARD6]] | -0.61 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[TOR1A]] | -0.61 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[ITPA]] | -0.60 | -0.57 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CARD6]] | B | CARD6 activity strengthens TTC3's drug response | lines that do not express CARD6 (17) vs lines expressing it (31) | the lines without CARD6 respond 0.64× as strongly (z diff +2.36); strongest at Ouabain (Octahydrate) 5 µM: 0.82x vs 0.61x (z diff +3.8) | 0.014 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.825). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.6, -33.1); signed map (-52.0, 10.1). **Vector** length 163, 63.9% of its response variance represented; |z| ≥ 3 in 1,687 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.65 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.66 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.66 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +8.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.8 | +1.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.8 | +4.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.2 | +4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +6.0 | +2.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +4.6 | +3.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +4.0 | +3.3 |
|  | [[Terfenadine (drug)]] 5 µM |  | +4.0 | +3.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -11.6 | -12.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -11.2 | -8.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -10.9 | -15.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -10.4 | -13.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.1 | -9.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -7.8 | -7.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -7.6 | -9.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -6.2 | -7.4 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.13 — chr21:37,073,226-37,203,112 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TPRD, TPRDI, DCRR1, TPRDII, TPRDIII, RNF105 |
| Gene groups (HGNC) | Ring finger proteins; Tetratricopeptide repeat domain containing; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [P53804](https://www.uniprot.org/uniprotkb/P53804) (E3 ubiquitin-protein ligase TTC3):

> E3 ubiquitin-protein ligase which catalyzes the formation of 'Lys-48'-polyubiquitin chains. Mediates the ubiquitination and subsequent degradation of phosphorylated Akt (AKT1, AKT2 and AKT3) in the nucleus. Acts as a terminal regulator of Akt signaling after activation; its phosphorylation by Akt, which is a prerequisite for ubiquitin ligase activity, suggests the existence of a regulation mechanism required to control Akt levels after activation. Positively regulates TGFB1-induced …

**Summary**, from NCBI Gene [7267](https://www.ncbi.nlm.nih.gov/gene/7267):

> Enables ubiquitin-protein transferase activity. Involved in protein K48-linked ubiquitination and ubiquitin-dependent protein catabolic process. Located in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:12393](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12393) · Entrez [7267](https://www.ncbi.nlm.nih.gov/gene/7267) · UniProt [P53804](https://www.uniprot.org/uniprotkb/P53804) · Ensembl [ENSG00000182670](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182670)

## Data

Gene col 11313: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11313); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11313, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11313]; `tensor/DDL_lfc|DDL_z.npy` [11313]; `embed/gene_vectors.npy` [11313]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11313 or target_col == 11313). Every well: [[TTC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
