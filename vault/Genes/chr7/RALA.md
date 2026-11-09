---
symbol: "RALA"
type: "gene"
col: 110
ensembl_id: "ENSG00000006451"
name: "RAS like proto-oncogene A"
location: "7p14.1"
module: 3
arm: "+"
pooled_cpm: 170.67
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 4
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# RALA

*RAS like proto-oncogene A* — 7p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.83× (z +7.8, q 3e-12, up in 37 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.582× (z -12.9, q 3e-35, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.749× (z -10.1, q 1e-21, down in 33 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (AsPC-1 0.194×, NCI-H1792 0.278×, Hs 766T 0.422×, NCI-H2030 0.446×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (AsPC-1 0.328×, CFPAC-1 0.417×, NCI-H1792 0.397×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (AsPC-1 0.240×, Panc 03.27 0.294×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (SW48 0.400×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL7]] (+0.68, fdr 7e-06), [[MGST3]] (+0.67, fdr 7e-06), [[COMMD6]] (+0.67, fdr 3e-05); moves opposite to [[HNRNPK]] (-0.66, fdr 1e-05), [[CHRAC1]] (-0.65, fdr 1e-05), [[SRSF1]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 110.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.83×** | +7.8 | 3e-12 | 37/49 (SW480, BT-474, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.30×** | +6.5 | 2e-08 | 28/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.24×** | +5.2 | 2e-05 | 28/48 (SNU-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +5.2 | 2e-05 | 16/49 (Panc 03.27, LS 180, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.49×** | +5.2 | 2e-05 | 31/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.21×** | +4.7 | 3e-04 | 25/48 (NCI-H2030, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.5 | 6e-04 | 21/48 (PANC-1, NCI-H2030, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.003 | 20/48 (Panc 03.27, BT-474, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.9 | 0.006 | 20/48 (NCI-H460, RKO, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.17× | +3.7 | 0.014 | 17/47 (Panc 03.27, BT-474, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.4 | 0.029 | 16/48 (SW480, HT-29, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.15× | +3.4 | 0.029 | 13/48 (H4, SW48, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.15× | +3.4 | 0.029 | 19/48 (Panc 03.27, SW480, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.15× | +3.4 | 0.032 | 14/47 (A-172, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.037 | 21/49 (BT-474, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.14× | +3.3 | 0.041 | 10/48 (NCI-H23, SHP-77, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.20×** | +3.2 | 0.041 | 17/48 (PANC-1, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.042 | 15/46 (Panc 03.27, BT-474, …) | two highest doses | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.18× | +2.9 | 0.094 | 12/48 (PANC-1, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 110.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (AsPC-1 0.194×, NCI-H1792 0.278×, Hs 766T 0.422×, NCI-H2030 0.446×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (AsPC-1 0.328×, CFPAC-1 0.417×, NCI-H1792 0.397×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (AsPC-1 0.240×, Panc 03.27 0.294×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (SW48 0.400×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.582×** | -12.9 | 3e-35 | 40/44 (AsPC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.749×** | -10.1 | 1e-21 | 33/48 (AsPC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.701×** | -8.8 | 3e-16 | 36/49 (SNU-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.700×** | -8.2 | 5e-14 | 33/45 (SW 900, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.839× | -4.4 | 0.001 | 23/48 (AsPC-1, NCI-H2347, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.855× | -3.7 | 0.017 | 21/48 (AsPC-1, Hs 766T, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.867× | -3.6 | 0.030 | 16/48 (AsPC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.874× | -3.3 | 0.060 | 13/47 (A-172, A549, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.882× | -3.1 | 0.11 | 15/48 (NCI-H1792, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 110. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 332 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -29.8) |
| [[NCI-H2347 (line)]] | alt | 292 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.597× (z -11.6) |
| [[A-172 (line)]] | wt | 259 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.439× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 252 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -20.5) |
| [[SW480 (line)]] | alt | 178 | 3 (1 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 2.62× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.638× (z -13.8) |
| [[CFPAC-1 (line)]] | alt | 199 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.436× (z -14.8) |
| [[LoVo (line)]] | wt | 220 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -15.4) |
| [[Panc 03.27 (line)]] | alt | 240 | 1 | 2 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.81× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.484× (z -12.3) |
| [[SW48 (line)]] | wt | 262 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.400× (z -9.1) |
| [[C32 (line)]] | wt | 91.1 | 1 | 1 | [[PH-797804 (drug)]] 5 µM 4.66× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 153 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.568× (z -9.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 153 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -16.0) |
| [[NCI-H2030 (line)]] | alt | 126 | 1 | 1 | [[Belinostat (drug)]] 5 µM 1.88× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -15.4) |
| [[NCI-H460 (line)]] | wt | 108 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.62× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 1.92× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 191 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.481× (z -10.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 133 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -12.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 119 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.592× (z -9.6) |
| [[A549 (line)]] | wt | 177 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.387× (z -11.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 162 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -9.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 202 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.84× (z +10.5) | — |
| [[C-33 A (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.368× (z -10.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 251 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.326× (z -12.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 156 | 1 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 1.97× (z +9.4) ⚠ cell-cycle shift, explains ~7% of this change | — |
| [[KATO III (line)]] | alt | 175 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.559× (z -8.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 133 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.578× (z -10.8) |
| [[LS 180 (line)]] | wt | 146 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.618× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 108 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1573 (line)]] | alt | 57.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.407× (z -9.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 120 | 1 | 0 | [[Belinostat (drug)]] 5 µM 1.79× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 216 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 2.85× (z +9.0) | — |
| [[SNU-1 (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -13.5) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 314 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -9.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 231 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.482× (z -11.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 312 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 85.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 170 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 152 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 280 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 100 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 131 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 110), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL7]] | +0.68 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[MGST3]] | +0.67 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[COMMD6]] | +0.67 | +0.46 / +0.69 | both halves | 3e-05 |  |
| [[MACO1]] | +0.65 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[LCMT1]] | +0.64 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[SIRT7]] | +0.64 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[MRPL55]] | +0.63 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[TSPAN33]] | +0.63 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[CARD19]] | +0.62 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[SLC15A4]] | +0.62 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[CGRRF1]] | +0.62 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[RPS26]] | +0.62 | +0.43 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPK]] | -0.66 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[CHRAC1]] | -0.65 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[SRSF1]] | -0.64 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[HNRNPL]] | -0.63 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[ILF3]] | -0.63 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[CBX5]] | -0.62 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[CPSF2]] | -0.62 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[ABCE1]] | -0.62 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[SNX5]] | -0.62 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[NEK9]] | -0.62 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[DDX3X]] | -0.60 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[HNRNPA2B1]] | -0.60 | -0.53 / -0.51 | both halves | 1e-05 | pathway: Gene and protein expression by JAK-STAT signaling after Interleukin-12 stimulation |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers RALA's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.693). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-40.1, -26.2); signed map (-24.0, 12.6). **Vector** length 142, 43.8% of its response variance represented; |z| ≥ 3 in 1,136 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +7.0 | +5.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.4 | +6.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.5 | +7.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.2 | +4.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.0 | +5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.9 | +3.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.7 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.6 | -10.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -6.4 | -4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.3 | -8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.9 | -12.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.3 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.1 | -3.1 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | -2.6 | -2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.5 | -1.8 |
|  | [[Encorafenib (drug)]] 5 µM |  | -2.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | RAS like proto-oncogene A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.1 — chr7:39,623,565-39,708,120 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously RAL |
| Gene groups (HGNC) | RAS type GTPase family |
| Hallmark sets | DNA_REPAIR |
| Reactome | 14 pathways, smallest: p38MAPK events; Signalling to RAS; Gene and protein expression by JAK-STAT signaling after Interleukin-12 stimulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P11233](https://www.uniprot.org/uniprotkb/P11233) (Ras-related protein Ral-A):

> Multifunctional GTPase involved in a variety of cellular processes including gene expression, cell migration, cell proliferation, oncogenic transformation and membrane trafficking. Accomplishes its multiple functions by interacting with distinct downstream effectors. Acts as a GTP sensor for GTP-dependent exocytosis of dense core vesicles. The RALA-exocyst complex regulates integrin-dependent membrane raft exocytosis and growth signaling. Key regulator of LPAR1 signaling and competes with GRK2 …

**Summary**, from NCBI Gene [5898](https://www.ncbi.nlm.nih.gov/gene/5898):

> The product of this gene belongs to the small GTPase superfamily, Ras family of proteins. GTP-binding proteins mediate the transmembrane signaling initiated by the occupancy of certain cell surface receptors. This gene encodes a low molecular mass ras-like GTP-binding protein that shares about 50% similarity with other ras proteins. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9839](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9839) · Entrez [5898](https://www.ncbi.nlm.nih.gov/gene/5898) · UniProt [P11233](https://www.uniprot.org/uniprotkb/P11233) · Ensembl [ENSG00000006451](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006451)

## Data

Gene col 110: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 110); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 110, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 110]; `tensor/DDL_lfc|DDL_z.npy` [110]; `embed/gene_vectors.npy` [110]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 110 or target_col == 110). Every well: [[RALA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RALA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
