---
symbol: "SLC1A4"
type: "gene"
col: 3734
ensembl_id: "ENSG00000115902"
name: "solute carrier family 1 member 4"
location: "2p14"
module: 63
arm: "+"
pooled_cpm: 17.52
n_lines_expressing: 46
n_dd_up: 35
n_dd_down: 23
n_dd_up_clean: 27
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# SLC1A4

*solute carrier family 1 member 4* — 2p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.14× (z +17.6, q 0e+00, up in 35 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.339× (z -17.1, q 0e+00, down in 35 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTHFD2]] (+0.81, fdr 7e-06), [[ASNS]] (+0.80, fdr 7e-06), [[PHGDH]] (+0.79, fdr 7e-06).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NUPR1]] → it (grade B ⚠); 5 go from it, the strongest it → [[NUPR1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3734.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +17.6 | 0e+00 | 35/41 (HOP62, A549, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.88×** | +10.3 | 1e-22 | 32/43 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.53×** | +9.8 | 3e-20 | 30/44 (NCI-H2030, SW480, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.71×** | +8.8 | 2e-16 | 29/41 (NCI-H2030, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.42×** | +8.1 | 6e-14 | 28/44 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.55×** | +7.2 | 6e-11 | 23/44 (NCI-H460, C-33 A, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.53×** | +7.0 | 3e-10 | 25/43 (A-172, NCI-H460, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.49×** | +6.5 | 7e-09 | 20/42 (C-33 A, NCI-H2030, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.47×** | +6.2 | 3e-08 | 22/44 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.45×** | +5.9 | 2e-07 | 17/40 (HOP62, NCI-H2030, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.98×** | +5.9 | 2e-07 | 15/40 (NCI-H2030, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.8 | 2e-07 | 16/42 (HOP62, KATO III, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.41×** | +5.6 | 8e-07 | 18/44 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +5.6 | 8e-07 | 16/44 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.25×** | +5.1 | 1e-05 | 18/44 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +5.1 | 1e-05 | 16/42 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.78×** | +5.0 | 2e-05 | 9/40 (A498, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.31×** | +4.4 | 3e-04 | 11/43 (C-33 A, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3734.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.339×** | -17.1 | 0e+00 | 35/43 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.384×** | -15.7 | 0e+00 | 36/41 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.386×** | -15.7 | 0e+00 | 37/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.544×** | -14.2 | 1e-43 | 30/43 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.529×** | -10.5 | 9e-24 | 30/43 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.529×** | -10.5 | 9e-24 | 29/42 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.530×** | -10.5 | 1e-23 | 30/42 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.511×** | -10.2 | 1e-22 | 27/39 (H4, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **0.662×** | -9.6 | 4e-20 | 28/43 (A-427, LS 180, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.558×** | -9.6 | 4e-20 | 30/42 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.433×** | -7.2 | 3e-11 | 22/42 (RKO, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.651×** | -7.1 | 6e-11 | 23/43 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.702×** | -5.9 | 2e-07 | 21/40 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.528×** | -5.5 | 2e-06 | 17/39 (SK-MEL-2, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.533×** | -5.4 | 2e-06 | 16/41 (H4, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.725×** | -5.3 | 4e-06 | 18/42 (H4, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.731×** | -5.2 | 7e-06 | 17/43 (KATO III, PANC-1, …) | rises with dose |  |
| [[8-Hydroxyquinoline (drug)]] 5 µM |  | 0.863× | -3.5 | 0.016 | 7/44 (CHP-212, HT-29, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.828×** | -3.1 | 0.046 | 10/44 (H4, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3734. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 16.5 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0832× (z -27.9) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.106× (z -17.8) |
| [[A-427 (line)]] | wt | 28.6 | 0 | 11 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.105× (z -15.3) |
| [[SW480 (line)]] | alt | 19.4 | 1 | 7 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.6) | [[Harringtonine (drug)]] 5 µM 0.220× (z -13.3) |
| [[SK-MEL-2 (line)]] | alt | 125 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -23.9) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0760× (z -19.4) |
| [[A-172 (line)]] | wt | 19.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -18.9) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.171× (z -11.5) |
| [[KATO III (line)]] | alt | 37.4 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.190× (z -12.4) |
| [[H4 (line)]] | wt | 41.7 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0934× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.0917× (z -12.3) |
| [[LoVo (line)]] | wt | 17.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.208× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 28.9 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +9.4) | [[Digitoxin (drug)]] 5 µM 0.0970× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.129× (z -11.3) |
| [[SW48 (line)]] | wt | 22.9 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0428× (z -13.8) |
| [[C32 (line)]] | wt | 49.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.212× (z -9.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 20.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -13.1) ⚠ cell-cycle shift, explains ~48% of this change |
| [[J82 (line)]] | alt | 17.0 | 0 | 2 (1 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.193× (z -10.8) |
| [[LS 180 (line)]] | wt | 11.7 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.246× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 16.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.110× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 19.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0576× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.116× (z -10.7) |
| [[SNU-1 (line)]] | wt | 15.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0629× (z -10.0) |
| [[SW 900 (line)]] | alt | 26.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.180× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.181× (z -10.7) |
| [[A498 (line)]] | wt | 13.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -12.6) ⚠ cell-cycle shift, explains ~52% of this change |
| [[A549 (line)]] | wt | 6.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.66× (z +10.7) | — |
| [[HCT15 (line)]] | alt | 19.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 11.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +11.4) | — |
| [[Hs 766T (line)]] | wt | 15.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -12.1) ⚠ cell-cycle shift, explains ~48% of this change |
| [[HS-578T (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.208× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 4.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.15× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 15.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -9.9) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SW1417 (line)]] | alt | 14.2 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.152× (z -10.3) |
| [[AN3 CA (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3734), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTHFD2]] | +0.81 | +0.77 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[ASNS]] | +0.80 | +0.78 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 502 |
| [[PHGDH]] | +0.79 | +0.79 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 504 |
| [[CARS1]] | +0.78 | +0.71 / +0.79 | both halves | 7e-06 | STRING 425 |
| [[AARS1]] | +0.78 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[PSAT1]] | +0.78 | +0.77 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 627 |
| [[MARS1]] | +0.77 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[GARS1]] | +0.77 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[SLC6A9]] | +0.76 | +0.72 / +0.75 | both halves | 7e-06 | pathway: SLC-mediated transmembrane transport; STRING 590 |
| [[XPOT]] | +0.75 | +0.73 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[CHAC1]] | +0.75 | +0.68 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[PCK2]] | +0.74 | +0.72 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUPR1]] | B | NUPR1 activity raises SLC1A4's level | lines that do not express NUPR1 (24) vs lines expressing it (26) | 1.72× lower at baseline in the lines without NUPR1 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TTTY14, SPARC, PCDH18 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUPR1]] | C | SLC1A4 activity raises NUPR1's level | lines that do not express SLC1A4 (4) vs lines expressing it (46) | 3.40× lower at baseline in the lines without SLC1A4 | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCNP, PSAT1, KAZN; maybe low, not absent; its own permutation p |
| [[PSAT1]] | C | SLC1A4 activity raises PSAT1's level | lines that do not express SLC1A4 (4) vs lines expressing it (46) | 3.35× lower at baseline in the lines without SLC1A4 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCNP, PSAT1, KAZN; maybe low, not absent; co-absent with the target; its own permutation p |
| [[TMEM268]] | C | SLC1A4 activity raises TMEM268's level | lines that do not express SLC1A4 (4) vs lines expressing it (46) | 2.11× lower at baseline in the lines without SLC1A4 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCNP, PSAT1, KAZN; maybe low, not absent; its own permutation p |
| [[SARS1]] | C | SLC1A4 activity raises SARS1's level | lines that do not express SLC1A4 (4) vs lines expressing it (46) | 1.55× lower at baseline in the lines without SLC1A4 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCNP, PSAT1, KAZN; maybe low, not absent; its own permutation p |
| [[PHGDH]] | C | SLC1A4 activity raises PHGDH's level | lines that do not express SLC1A4 (4) vs lines expressing it (46) | 2.86× lower at baseline in the lines without SLC1A4 | 0.090 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCNP, PSAT1, KAZN; maybe low, not absent |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.816). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.4, 48.1); signed map (-13.4, 24.6). **Vector** length 108, 27.1% of its response variance represented; |z| ≥ 3 in 1,245 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.71 to 16); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.72 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.72 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.8 | +3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.5 | +10.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +17.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.4 | +7.0 |
|  | [[Artesunate (drug)]] 5 µM |  | +4.3 | +8.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.7 | +9.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +7.2 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +3.5 | +5.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.3 | +3.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.3 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.4 | -10.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -10.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.2 | -5.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -17.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.7 | -10.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.1 | -3.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.8 | -1.8 |
|  | [[AZD-8055 (drug)]] 5 µM |  | -1.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 1 member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p14 — chr2:64,988,477-65,023,865 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SATT, ASCT1, ASCT-1 |
| Gene groups (HGNC) | Solute carrier family 1 |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY, MTORC1_SIGNALING |
| Reactome | 4 pathways, smallest: Amino acid transport across the plasma membrane; SLC-mediated transport of amino acids; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P43007](https://www.uniprot.org/uniprotkb/P43007) (Neutral amino acid transporter A):

> Sodium-coupled antiporter of neutral amino acids. In a tri-substrate transport cycle, exchanges neutral amino acids between the extracellular and intracellular compartments, coupled to the inward cotransport of at least one sodium ion. Exchanges neutral amino acids such as L- and D-serine, L-threonine, L-asparagine and L-alanine in a bidirectional way. Involved in homeostasis of D-serine, a coagonist of synaptic NMDA receptors. In astrocytes at excitatory synapses, mediates electrogenic …

**Summary**, from NCBI Gene [6509](https://www.ncbi.nlm.nih.gov/gene/6509):

> The protein encoded by this gene is a sodium-dependent neutral amino acid transporter for alanine, serine, cysteine, and threonine. Defects in this gene have been associated with developmental delay, microcephaly, and intellectual disability. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:10942](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10942) · Entrez [6509](https://www.ncbi.nlm.nih.gov/gene/6509) · UniProt [P43007](https://www.uniprot.org/uniprotkb/P43007) · Ensembl [ENSG00000115902](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115902)

## Data

Gene col 3734: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3734); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3734, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3734]; `tensor/DDL_lfc|DDL_z.npy` [3734]; `embed/gene_vectors.npy` [3734]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3734 or target_col == 3734). Every well: [[SLC1A4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC1A4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
