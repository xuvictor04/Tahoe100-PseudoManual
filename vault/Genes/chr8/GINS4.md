---
symbol: "GINS4"
type: "gene"
col: 7197
ensembl_id: "ENSG00000147536"
name: "GINS complex subunit 4"
location: "8p11.21"
module: 6
arm: "+"
pooled_cpm: 11.72
n_lines_expressing: 50
n_dd_up: 41
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# GINS4

*GINS complex subunit 4* — 8p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (28 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.52× (z +24.2, q 0e+00, up in 41 of 45 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.74× (z +10.6, q 2e-24, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 0.470× (z -5.4, q 4e-05, down in 22 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLSPN]] (+0.78, fdr 7e-06), [[ASF1B]] (+0.78, fdr 7e-06), [[ATAD5]] (+0.76, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 29 with an alert ⚠; shown: the 15 strongest and the 13 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 28 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7197.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **3.52×** | +24.2 | 0e+00 | 41/45 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **3.92×** | +18.5 | 0e+00 | 47/47 (SW480, HS-578T, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **3.53×** | +17.1 | 0e+00 | 43/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **3.61×** | +16.8 | 0e+00 | 41/44 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **3.56×** | +16.6 | 0e+00 | 42/45 (SW480, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **2.84×** | +14.2 | 2e-43 | 45/47 (SW480, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **2.78×** | +13.9 | 8e-42 | 29/36 (SW480, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **2.46×** | +11.7 | 6e-30 | 12/16 (SNU-423, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **2.44×** | +11.7 | 1e-29 | 32/37 (J82, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.74×** | +10.6 | 2e-24 | 34/48 (A-172, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | **2.03×** | +8.9 | 4e-17 | 21/27 (SNU-423, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.78×** | +7.8 | 3e-13 | 31/47 (J82, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.37×** | +6.0 | 1e-07 | 23/48 (HS-578T, LoVo, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.58×** | +6.0 | 1e-07 | 23/46 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.52×** | +5.6 | 7e-07 | 23/47 (J82, A549, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +5.1 | 1e-05 | 17/47 (A-427, HOP62, …) | rises with dose |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.8 | 4e-05 | 15/47 (HOP62, A-427, …) | top dose only | plate-row cell shift |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.45×** | +4.7 | 9e-05 | 17/43 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.002 | 15/47 (J82, NCI-H23, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.004 | 13/47 (A-427, NCI-H460, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.62×** | +3.4 | 0.011 | 3/44 (SW480, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +3.4 | 0.011 | 7/47 (SW480, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 5 µM |  | **1.35×** | +3.0 | 0.039 | 2/45 (HCT15, H4) | inconsistent across doses | noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.27×** | +3.0 | 0.045 | 8/46 (A-427, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.24×** | +2.9 | 0.047 | 3/47 (A-427, RKO, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **1.25×** | +2.8 | 0.073 | 5/46 (A-427, SW480, …) | all doses, flat |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 1.18× | +2.7 | 0.082 | 6/48 (C32, RKO, …) | inconsistent across doses |  |
| [[Irinotecan (drug)]] 5 µM |  | **1.47×** | +2.7 | 0.090 | 8/46 (A-427, NCI-H460, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7197.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.470×** | -5.4 | 4e-05 | 22/43 (LS 180, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.546×** | -4.3 | 0.004 | 18/46 (MIA PaCa-2, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **0.654×** | -4.1 | 0.006 | 14/48 (SW480, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.825×** | -3.7 | 0.026 | 13/48 (Panc 03.27, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.768×** | -3.6 | 0.033 | 19/43 (A-427, A498, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 5 µM |  | **0.771×** | -3.4 | 0.058 | 10/45 (C-33 A, A-427, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.769× | -3.1 | 0.14 | 11/45 (AsPC-1, HCT15, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.856× | -3.0 | 0.17 | 12/47 (A498, RPMI-7951, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.32 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7197. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.7 | 7 (7 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.67× (z +13.2) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[A498 (line)]] | wt | 14.7 | 4 (4 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +13.5) ⚠ cell-cycle shift, explains ~25% of this change | [[Selinexor (drug)]] 5 µM 0.388× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 15.4 | 4 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +11.7) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[LOX-IMVI (line)]] | wt | 10.3 | 4 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.03× (z +10.7) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[A-172 (line)]] | wt | 10.2 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.38× (z +12.6) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[A549 (line)]] | wt | 10.2 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +15.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[HOP62 (line)]] | alt | 15.1 | 3 (3 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.99× (z +11.4) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[J82 (line)]] | alt | 27.0 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +12.7) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 28.2 | 0 | 3 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.565× (z -13.2) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.242× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 7.35 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.88× (z +14.6) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[A-427 (line)]] | wt | 24.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -12.8) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0834× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 31.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.23× (z +8.6) ⚠ cell-cycle shift, explains ~62% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[PANC-1 (line)]] | alt | 7.31 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +9.9) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[AsPC-1 (line)]] | alt | 6.36 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.21× (z +9.1) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[CFPAC-1 (line)]] | alt | 6.06 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.67× (z +10.1) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[HEC-1-A (line)]] | alt | 22.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +9.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 4.79 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +9.8) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[KATO III (line)]] | alt | 13.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +9.0) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[LoVo (line)]] | wt | 8.55 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.73× (z +14.2) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[Panc 03.27 (line)]] | alt | 10.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.60× (z +12.9) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[RKO (line)]] | wt | 19.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.92× (z +12.8) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SHP-77 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.155× (z -9.2) ⚠ transcription drop |
| [[SW 900 (line)]] | alt | 6.11 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +8.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[AN3 CA (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7197), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLSPN]] | +0.78 | +0.77 / +0.80 | both halves | 7e-06 | STRING 930 |
| [[ASF1B]] | +0.78 | +0.77 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[ATAD5]] | +0.76 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[RAD51AP1]] | +0.76 | +0.73 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[PSMC3IP]] | +0.75 | +0.69 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[DDIAS]] | +0.75 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[TYMS]] | +0.74 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[MCM8]] | +0.74 | +0.75 / +0.72 | both halves | 7e-06 | pathway: DNA Replication; STRING 853 |
| [[TK1]] | +0.74 | +0.69 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[FANCI]] | +0.73 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[PCLAF]] | +0.73 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[CENPK]] | +0.72 | +0.72 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GINS4's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.9% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP1]] | B | TOP1 activity lowers GINS4's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 5.9% of all compounds | 0.079 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.707). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-37.2, -47.1); signed map (-40.9, -45.7). **Vector** length 87.9, 20.3% of its response variance represented; |z| ≥ 3 in 1,168 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F G1/S* (control, mean cos +0.58 to 23); *Cell Cycle Checkpoints* (reactome, mean cos +0.61 to 45); *Activation of the pre-replicative complex* (reactome, mean cos +0.59 to 22).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +6.9 | +16.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +6.4 | +16.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +5.6 | +24.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | +4.9 | +13.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +4.7 | +7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +10.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.6 | +4.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.6 | +3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.6 | +5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.3 | +4.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -4.3 | -3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | -4.2 | +3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -5.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -1.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.6 | +0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -1.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | GINS complex subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.21 — chr8:41,529,218-41,545,030 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC14799, SLD5 |
| Gene groups (HGNC) | GINS complex |
| Hallmark sets | E2F_TARGETS |
| Reactome | 7 pathways, smallest: Unwinding of DNA; DNA strand elongation; Synthesis of DNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRT9](https://www.uniprot.org/uniprotkb/Q9BRT9) (DNA replication complex GINS protein SLD5):

> Required for correct functioning of the GINS complex, a complex that plays an essential role in the initiation of DNA replication, and progression of DNA replication forks. GINS complex is a core component of CDC45-MCM-GINS (CMG) helicase, the molecular machine that unwinds template DNA during replication, and around which the replisome is built.

**Summary**, from NCBI Gene [84296](https://www.ncbi.nlm.nih.gov/gene/84296):

> The yeast heterotetrameric GINS complex is made up of Sld5, Psf1 (GINS1; MIM 610608), Psf2 (GINS2; MIM 610609), and Psf3 (GINS3; MIM 610610). The formation of the GINS complex is essential for the initiation of DNA replication in yeast and Xenopus egg extracts (Ueno et al., 2005 [PubMed 16287864]). See GINS1 for additional information about the GINS complex.[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:28226](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28226) · Entrez [84296](https://www.ncbi.nlm.nih.gov/gene/84296) · UniProt [Q9BRT9](https://www.uniprot.org/uniprotkb/Q9BRT9) · Ensembl [ENSG00000147536](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147536)

## Data

Gene col 7197: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7197); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7197, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7197]; `tensor/DDL_lfc|DDL_z.npy` [7197]; `embed/gene_vectors.npy` [7197]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7197 or target_col == 7197). Every well: [[GINS4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GINS4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
