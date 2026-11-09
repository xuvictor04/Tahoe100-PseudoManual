---
symbol: "CENPA"
type: "gene"
col: 3629
ensembl_id: "ENSG00000115163"
name: "centromere protein A"
location: "2p23.3"
module: 22
arm: "+"
pooled_cpm: 31.79
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 14
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CENPA

*centromere protein A* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.50× (z +9.3, q 8e-18, up in 30 of 45 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.33× (z +6.6, q 6e-09, up in 20 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.738× (z -9.8, q 4e-20, down in 26 of 48 measured lines) ⚠ cell-cycle shift, explains ~63% of this change. The strongest without an alert is [[Cytarabine (hydrochloride) (drug)]] 0.05 µM: 0.720× (z -7.0, q 3e-10, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIF1]] (+0.81, fdr 7e-06), [[FAM72B]] (+0.80, fdr 7e-06), [[TROAP]] (+0.80, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 20 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3629.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.50×** | +9.3 | 8e-18 | 30/45 (HOP62, SW1417, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.28×** | +8.1 | 1e-13 | 25/47 (NCI-H2347, NCI-H2030, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +6.6 | 6e-09 | 20/47 (A-172, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.33×** | +6.6 | 8e-09 | 19/48 (NCI-H23, KATO III, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.31×** | +6.2 | 7e-08 | 20/47 (HOP62, LOX-IMVI, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.30×** | +6.0 | 2e-07 | 20/47 (NCI-H23, SNU-423, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.28×** | +5.6 | 1e-06 | 19/47 (KATO III, C-33 A, …) | all doses, flat |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.27×** | +5.5 | 2e-06 | 16/47 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 1.18× | +5.5 | 2e-06 | 15/48 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.26×** | +5.3 | 5e-06 | 14/48 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.17× | +5.1 | 2e-05 | 11/48 (HT-29, HEC-1-A, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.24×** | +4.9 | 5e-05 | 15/48 (KATO III, CFPAC-1, …) | all doses, flat | composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.23×** | +4.9 | 5e-05 | 16/48 (HOP62, BT-474, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.24×** | +4.8 | 6e-05 | 14/47 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.22×** | +4.6 | 1e-04 | 11/47 (HOP62, NCI-H23, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +4.6 | 1e-04 | 14/48 (HOP62, LoVo, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.22×** | +4.2 | 8e-04 | 11/47 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 0.5 µM |  | 1.19× | +4.1 | 0.001 | 10/47 (CFPAC-1, H4, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.18× | +3.7 | 0.006 | 10/48 (NCI-H23, H4, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.013 | 6/47 (HEC-1-A, CFPAC-1, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.016 | 5/48 (PANC-1, A-172, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.15× | +3.3 | 0.018 | 12/48 (BT-474, A549, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.028 | 4/44 (HOP62, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 0.05 µM |  | 1.13× | +2.7 | 0.097 | 3/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3629.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.738×** | -9.8 | 4e-20 | 26/48 (A498, HOP62, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.655×** | -9.7 | 8e-20 | 28/48 (A-427, SNU-1, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.711×** | -7.5 | 1e-11 | 29/47 (SW48, SHP-77, …) | all doses, flat |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.733×** | -7.1 | 2e-10 | 24/47 (HEC-1-A, A-427, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.727×** | -7.0 | 2e-10 | 27/48 (HOP62, CHP-212, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.727×** | -7.0 | 2e-10 | 25/47 (SK-MEL-2, A-427, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.720×** | -7.0 | 3e-10 | 27/47 (NCI-H1573, SW48, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.749×** | -6.6 | 3e-09 | 25/48 (A-172, C32, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.743×** | -6.6 | 4e-09 | 21/48 (SK-MEL-2, RKO, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.598×** | -6.2 | 4e-08 | 25/47 (BT-474, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.782×** | -5.6 | 9e-07 | 22/48 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.774×** | -5.4 | 3e-06 | 21/47 (A-427, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.800×** | -5.1 | 1e-05 | 19/47 (LOX-IMVI, A-172, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.869× | -4.6 | 2e-04 | 19/48 (A-427, LOX-IMVI, …) | two highest doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.880× | -4.1 | 0.001 | 12/48 (A-172, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.837× | -3.8 | 0.006 | 11/47 (LOX-IMVI, A498, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.849× | -3.8 | 0.006 | 3/48 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.851× | -3.7 | 0.007 | 12/48 (SK-MEL-2, HT-29, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.863× | -3.4 | 0.021 | 17/48 (A-172, HOP62, …) | rises with dose |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.819×** | -3.3 | 0.029 | 3/48 (SW480, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.863× | -3.2 | 0.029 | 7/47 (C32, BT-474, …) | top dose only |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 0.899× | -3.2 | 0.029 | 9/48 (A-427, HOP62, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.869× | -3.1 | 0.046 | 6/47 (HS-578T, NCI-H2030, …) | top dose only |  |
| [[Ciclopirox (drug)]] 5 µM |  | 0.911× | -3.0 | 0.055 | 5/48 (NCI-H1573, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3629. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 76.2 | 0 | 3 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.421× (z -12.2) |
| [[A-172 (line)]] | wt | 40.6 | 0 | 2 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.351× (z -9.5) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A498 (line)]] | wt | 58.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.495× (z -11.1) ⚠ cell-cycle shift, explains ~63% of this change |
| [[H4 (line)]] | wt | 28.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.238× (z -9.7) ⚠ cell-cycle shift, explains ~63% of this change |
| [[HEC-1-A (line)]] | alt | 24.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.04× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change | — |
| [[HepG2_C3A (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.136× (z -9.9) ⚠ transcription drop; unreliable plate only |
| [[HOP62 (line)]] | alt | 36.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.440× (z -10.0) ⚠ cell-cycle shift, explains ~63% of this change |
| [[KATO III (line)]] | alt | 32.7 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.78× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[LoVo (line)]] | wt | 23.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change |
| [[NCI-H2347 (line)]] | alt | 18.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SHP-77 (line)]] | alt | 36.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.236× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~45% of this change |
| [[SK-MEL-2 (line)]] | alt | 33.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -8.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 1271 (line)]] | alt | 51.3 | 0 | 1 | — | [[Clofarabine (drug)]] 5 µM 0.0635× (z -8.6) |
| [[SW48 (line)]] | wt | 25.5 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.102× (z -11.3) |
| [[SW480 (line)]] | alt | 36.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.578× (z -8.5) ⚠ cell-cycle shift, explains ~63% of this change |
| [[A549 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3629), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIF1]] | +0.81 | +0.79 / +0.79 | both halves | 7e-06 | pathway: Chromosome Maintenance |
| [[FAM72B]] | +0.80 | +0.73 / +0.81 | both halves | 7e-06 |  |
| [[TROAP]] | +0.80 | +0.78 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 656 |
| [[CCNB1]] | +0.79 | +0.77 / +0.79 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 953 |
| [[PLK1]] | +0.78 | +0.76 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 988 |
| [[TACC3]] | +0.78 | +0.76 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 672 |
| [[DLGAP5]] | +0.78 | +0.79 / +0.74 | both halves | 7e-06 | STRING 945 |
| [[KNSTRN]] | +0.78 | +0.78 / +0.77 | both halves | 7e-06 | STRING 587 |
| [[CDKN3]] | +0.77 | +0.77 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 824 |
| [[CENPE]] | +0.76 | +0.76 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 993 |
| [[CDCA8]] | +0.76 | +0.76 / +0.74 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 971 |
| [[FAM72D]] | +0.76 | +0.78 / +0.73 | both halves | 7e-06 | STRING 464 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CENPA's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HYLS1]] | B | HYLS1 activity raises CENPA's level | lines that do not express HYLS1 (5) vs lines expressing it (45) | 1.53× lower at baseline in the lines without HYLS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: DNAJB5, PPP2R3A, CEP170; maybe low, not absent; its own permutation p |
| [[NEURL1B]] | B | NEURL1B activity raises CENPA's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.62× lower at baseline in the lines without NEURL1B | 0.068 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[CDC20]] | C | CDC20 activity raises CENPA's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 1.93× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[FAM72D]] | C | FAM72D activity raises CENPA's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.01× lower at baseline in the lines without FAM72D | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | CENPA's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | CENPA's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.57 | 0.511 over the table, 0.096 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.756). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.7, -58.4); signed map (-52.2, -42.8). **Vector** length 121, 32.4% of its response variance represented; |z| ≥ 3 in 1,011 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.56 to 46); *mitotic spindle* (hallmark, mean cos +0.59 to 38); *G2/M Transition* (reactome, mean cos +0.57 to 28).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | +5.5 | +9.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | +4.3 | +6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.2 | +8.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.7 | +1.8 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +3.6 | +5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.5 | +4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +3.4 | +5.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.4 | +6.2 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -5.4 | -9.7 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -4.9 | -7.5 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -4.9 | -7.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -4.8 | -9.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -6.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.7 | -6.2 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -3.6 | -7.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.5 | -4.1 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -3.3 | -5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | centromere protein A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:26,764,289-26,801,067 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CENP-A, CenH3 |
| Gene groups (HGNC) | H3 histones |
| Hallmark sets | GLYCOLYSIS, G2M_CHECKPOINT |
| Reactome | 20 pathways, smallest: Deposition of new CENPA-containing nucleosomes at the centromere; Nucleosome assembly; Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal |
| Matched by | ensembl_id |

**Function**, from UniProt [P49450](https://www.uniprot.org/uniprotkb/P49450) (Histone H3-like centromeric protein A):

> Histone H3-like nucleosomal protein that is specifically found in centromeric nucleosomes. Replaces conventional H3 in the nucleosome core of centromeric chromatin that serves as an assembly site for the inner kinetochore. The presence of CENPA subtly modifies the nucleosome structure and the way DNA is wrapped around the nucleosome and gives rise to protruding DNA ends that are less well-ordered and rigid compared to nucleosomes containing histone H3. May serve as an epigenetic mark that …

**Summary**, from NCBI Gene [1058](https://www.ncbi.nlm.nih.gov/gene/1058):

> Centromeres are the differentiated chromosomal domains that specify the mitotic behavior of chromosomes. This gene encodes a centromere protein which contains a histone H3 related histone fold domain that is required for targeting to the centromere. Centromere protein A is proposed to be a component of a modified nucleosome or nucleosome-like structure in which it replaces 1 or both copies of conventional histone H3 in the (H3-H4)2 tetrameric core of the nucleosome particle. The protein is a …

**Accessions** — [HGNC:1851](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1851) · Entrez [1058](https://www.ncbi.nlm.nih.gov/gene/1058) · UniProt [P49450](https://www.uniprot.org/uniprotkb/P49450) · Ensembl [ENSG00000115163](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115163)

## Data

Gene col 3629: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3629); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3629, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3629]; `tensor/DDL_lfc|DDL_z.npy` [3629]; `embed/gene_vectors.npy` [3629]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3629 or target_col == 3629). Every well: [[CENPA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CENPA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
