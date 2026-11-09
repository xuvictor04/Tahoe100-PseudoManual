---
symbol: "C9orf24"
type: "gene"
col: 9046
ensembl_id: "ENSG00000164972"
name: "sperm microtubule inner protein 6"
location: "9p13.3"
module: 39
arm: "+"
pooled_cpm: 12.53
n_lines_expressing: 42
n_dd_up: 11
n_dd_down: 23
n_dd_up_clean: 10
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# C9orf24

*sperm microtubule inner protein 6* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.31× (z +20.2, q 0e+00, up in 36 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.285× (z -12.3, q 8e-32, down in 32 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM219A]] (+0.74, fdr 7e-06, ⚠ same locus), [[NOXRED1]] (+0.72, fdr 7e-06), [[MYOCOS]] (+0.67, fdr 7e-06), [[ANKUB1]] (+0.66, fdr 7e-06); moves opposite to [[FOXRED2]] (-0.58, fdr 3e-05), [[ALDH7A1]] (-0.55, fdr 3e-05), [[SORT1]] (-0.55, fdr 1e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LINC01619]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9046.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.31×** | +20.2 | 0e+00 | 36/36 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.49×** | +11.5 | 2e-28 | 31/38 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.25×** | +11.1 | 3e-26 | 31/36 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.92×** | +10.5 | 2e-23 | 32/40 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.49×** | +8.6 | 1e-15 | 26/36 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.39×** | +8.5 | 2e-15 | 30/39 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.79×** | +5.2 | 1e-05 | 15/29 (PANC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.90×** | +4.5 | 5e-04 | 16/39 (NCI-H1573, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.010 | 14/40 (HOP62, A498, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.014 | 15/38 (LoVo, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.034 | 14/39 (A-172, PANC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.36× | +3.0 | 0.13 | 8/37 (A498, BT-474, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9046.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.285×** | -12.3 | 8e-32 | 32/40 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.294×** | -12.0 | 1e-30 | 28/35 (H4, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.329×** | -10.9 | 3e-25 | 31/39 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.365×** | -9.8 | 1e-20 | 30/39 (BT-474, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.392×** | -8.8 | 1e-16 | 26/34 (HS-578T, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.479×** | -6.9 | 4e-10 | 24/39 (H4, SNU-423, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.549×** | -5.9 | 4e-07 | 25/40 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.551×** | -5.8 | 4e-07 | 21/29 (HS-578T, RPMI-7951, …) | inconsistent across doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.374×** | -5.0 | 3e-05 | 19/38 (BT-474, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.378×** | -5.0 | 4e-05 | 19/36 (BT-474, PANC-1, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.629×** | -4.4 | 7e-04 | 21/40 (HOP62, SK-MEL-2, …) | top dose only | plate-row cell shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.668×** | -3.9 | 0.004 | 18/38 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.678×** | -3.8 | 0.006 | 19/39 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.687×** | -3.7 | 0.009 | 19/40 (H4, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.687×** | -3.7 | 0.009 | 18/40 (H4, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.498×** | -3.6 | 0.013 | 15/36 (BT-474, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.706×** | -3.4 | 0.021 | 16/38 (NCI-H1573, H4, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.726×** | -3.1 | 0.053 | 17/40 (hTERT-HPNE, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **0.730×** | -3.1 | 0.061 | 14/40 (SNU-423, NCI-H1573, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.735×** | -3.0 | 0.072 | 13/40 (HS-578T, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9046. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 87.2 | 0 | 10 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0180× (z -25.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0622× (z -17.6) |
| [[NCI-H460 (line)]] | wt | 15.0 | 3 | 6 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.64× (z +15.0) | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.0708× (z -16.3) |
| [[BT-474 (line)]] | alt | 31.4 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0346× (z -16.2) |
| [[HOP62 (line)]] | alt | 36.9 | 1 | 6 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.0743× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0793× (z -15.1) |
| [[RPMI-7951 (line)]] | alt | 29.3 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0401× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0916× (z -13.0) |
| [[LOX-IMVI (line)]] | wt | 9.38 | 2 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.41× (z +13.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0169× (z -17.2) |
| [[HS-578T (line)]] | alt | 39.1 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +8.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0243× (z -20.6) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 11.2 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.88× (z +15.1) | [[Digitoxin (drug)]] 5 µM 0.0889× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0964× (z -14.2) |
| [[A-172 (line)]] | wt | 31.5 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.101× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[J82 (line)]] | alt | 21.1 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0280× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0660× (z -15.2) |
| [[SNU-423 (line)]] | alt | 24.4 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0730× (z -13.3) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.117× (z -11.3) |
| [[A549 (line)]] | wt | 12.9 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.07× (z +10.4) | [[Harringtonine (drug)]] 0.5 µM 0.0773× (z -11.7) |
| [[hTERT-HPNE (line)]] | wt | 32.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -9.2) |
| [[LoVo (line)]] | wt | 5.02 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 9.64× (z +9.8) | — |
| [[A498 (line)]] | wt | 10.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.03× (z +13.1) | — |
| [[C32 (line)]] | wt | 14.2 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0726× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 15.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.42× (z +8.6) | [[Digitoxin (drug)]] 0.05 µM 0.0607× (z -10.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[Hs 766T (line)]] | wt | 13.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.10× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.107× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[KATO III (line)]] | alt | 14.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.43× (z +9.4) | [[Digitoxin (drug)]] 5 µM 0.152× (z -8.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 3.69 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.35× (z +9.0) | [[Menadione (drug)]] 0.5 µM 0.0699× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 15.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0989× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SK-MEL-2 (line)]] | alt | 17.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0756× (z -12.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 21.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.0506× (z -15.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 8.88 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0892× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 3.88 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 9.84× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.75× (z +10.3) | — |
| [[NCI-H23 (line)]] | alt | 3.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.48× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 4.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.89× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 7.93 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0660× (z -9.8) |
| [[SW480 (line)]] | alt | 3.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +9.6) | — |
| [[A-427 (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9046), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM219A]] | +0.74 | +0.74 / +0.70 | both halves | 7e-06 | STRING 566; ⚠ same locus (0.4 kb, same strand: neighbours can correlate without regulation) |
| [[NOXRED1]] | +0.72 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[ANKUB1]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[SLC51A]] | +0.65 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[GPATCH2L]] | +0.64 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[LINC00672]] | +0.64 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[LINC01588]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[ZNF432]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[CDKL4]] | +0.63 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[RABGEF1]] | +0.63 | +0.49 / +0.69 | both halves | 2e-05 |  |
| [[LINC03016]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[C9]] | +0.62 | +0.54 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXRED2]] | -0.58 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[ALDH7A1]] | -0.55 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[SORT1]] | -0.55 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[EFR3A]] | -0.54 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[ALDH5A1]] | -0.54 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[VMA21]] | -0.54 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[MED14]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[TMEM237]] | -0.53 | -0.46 / -0.61 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers C9orf24's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01705]] | B | LINC01705 activity raises C9orf24's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 2.69× lower at baseline in the lines without LINC01705 | 0.007 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137 |
| [[COL27A1]] | B | COL27A1 activity raises C9orf24's level | lines that do not express COL27A1 (12) vs lines expressing it (38) | 2.36× lower at baseline in the lines without COL27A1 | 0.029 | ⚠ within organs, on part of the lines; also absent: C13orf46, ENSG00000285804, GSDME; maybe low, not absent |
| [[C9]] | B | C9 activity raises C9orf24's level | lines that do not express C9 (21) vs lines expressing it (29) | 2.60× lower at baseline in the lines without C9 | 0.095 | ⚠ within organs, on part of the lines; also absent: DAB2, ENSG00000253891, PTGFR |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01619]] | B | C9orf24 activity raises LINC01619's level | lines that do not express C9orf24 (8) vs lines expressing it (42) | 1.57× lower at baseline in the lines without C9orf24 | 0.090 | ⚠ within organs, on part of the lines; also absent: ZNF772, FGD1, DNAAF9; maybe low, not absent |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.593). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.5, -20.1); signed map (11.2, 9.1). **Vector** length 119, 31.9% of its response variance represented; |z| ≥ 3 in 1,235 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.9 | +20.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.4 | +11.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.7 | +10.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.8 | +8.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +3.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.7 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +3.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.2 | +2.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -5.3 | -10.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.8 | -12.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.9 | -8.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.8 | -12.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.7 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -0.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.7 | -3.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -2.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.6 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | sperm microtubule inner protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:34,379,019-34,397,828 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA573M23.4, NYD-SP22, MGC32921, MGC33614, CBE1, SMRP1; previously C9orf24 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCR6](https://www.uniprot.org/uniprotkb/Q8NCR6) (Sperm microtubule inner protein 6):

> May participate in intramanchette transport and midpiece formation of the sperm tail. May play a potential role in somatic cell proliferation.

**Summary**, from NCBI Gene [84688](https://www.ncbi.nlm.nih.gov/gene/84688):

> This gene encodes a nuclear- or perinuclear-localized protein with no predicted domains or similarity to other known proteins. Expression of this gene is induced during the differentiation of bronchial epithelial cells, and the encoded protein may play a role in ciliogenesis. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:19919](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19919) · Entrez [84688](https://www.ncbi.nlm.nih.gov/gene/84688) · UniProt [Q8NCR6](https://www.uniprot.org/uniprotkb/Q8NCR6) · Ensembl [ENSG00000164972](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164972)

## Data

Gene col 9046: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9046); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9046, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9046]; `tensor/DDL_lfc|DDL_z.npy` [9046]; `embed/gene_vectors.npy` [9046]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9046 or target_col == 9046). Every well: [[C9orf24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C9orf24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
