---
symbol: "PTPRB"
type: "gene"
col: 4801
ensembl_id: "ENSG00000127329"
name: "protein tyrosine phosphatase receptor type B"
location: "12q15"
module: 44
arm: "+"
pooled_cpm: 43.97
n_lines_expressing: 28
n_dd_up: 7
n_dd_down: 36
n_dd_up_clean: 6
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 49
direction_downstream: 73
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# PTPRB

*protein tyrosine phosphatase receptor type B* — 12q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.35× (z +5.4, q 4e-05, up in 6 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (14 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.371× (z -12.4, q 1e-32, down in 23 of 26 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.467× (z -9.5, q 2e-19, down in 25 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPRR]] (+0.87, fdr 7e-06, ⚠ same locus), [[UGT1A9]] (+0.67, fdr 7e-06), [[B3GALT5]] (+0.67, fdr 1e-05), [[UGT1A6]] (+0.65, fdr 7e-06); moves opposite to [[CROCCP3-1]] (-0.48, fdr 4e-05), [[SEPTIN5]] (-0.47, fdr 3e-04), [[JCAD]] (-0.46, fdr 3e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 49 arrows point to it, the strongest [[IKZF2]] → it (grade B ⚠); 73 go from it, the strongest it → [[RBM47]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4801.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +5.4 | 4e-05 | 6/26 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.38×** | +4.6 | 0.001 | 12/26 (BT-474, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.42×** | +4.4 | 0.002 | 17/26 (NCI-H1792, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.37×** | +4.0 | 0.010 | 10/26 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.013 | 12/25 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.35×** | +3.8 | 0.014 | 6/25 (LOX-IMVI, NCI-H1573, …) | two highest doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.050 | 6/26 (KATO III, NCI-H2347, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.28× | +3.2 | 0.11 | 9/26 (NCI-H1792, NCI-H1573, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4801.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.371×** | -12.4 | 1e-32 | 23/26 (LS 180, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.416×** | -11.0 | 1e-25 | 24/26 (LoVo, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.425×** | -10.7 | 2e-24 | 23/26 (LoVo, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.447×** | -10.1 | 1e-21 | 25/26 (LoVo, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.467×** | -9.5 | 2e-19 | 25/25 (LS 180, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.587×** | -9.4 | 5e-19 | 20/26 (LS 180, LoVo, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.462×** | -9.3 | 1e-18 | 22/26 (AsPC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.527×** | -8.0 | 9e-14 | 23/25 (AsPC-1, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.564×** | -7.2 | 5e-11 | 20/26 (LS 180, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.552×** | -7.1 | 5e-11 | 20/25 (LoVo, KATO III, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.574×** | -6.9 | 2e-10 | 21/26 (NCI-H1792, COLO 205, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.602×** | -6.3 | 1e-08 | 20/26 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.680×** | -4.8 | 6e-05 | 11/25 (Hs 766T, LOX-IMVI, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.681×** | -4.8 | 6e-05 | 20/25 (LoVo, AsPC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.481×** | -4.8 | 6e-05 | 16/26 (LS 180, SNU-423, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.718×** | -4.1 | 0.001 | 13/25 (Hs 766T, LOX-IMVI, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.685×** | -4.1 | 0.002 | 10/25 (Hs 766T, LOX-IMVI, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.723×** | -3.9 | 0.003 | 8/26 (CFPAC-1, Hs 766T, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.722×** | -3.8 | 0.003 | 19/26 (LS 180, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.735×** | -3.8 | 0.003 | 16/26 (LS 180, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.750×** | -3.6 | 0.008 | 11/25 (Hs 766T, LOX-IMVI, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.599×** | -3.3 | 0.017 | 10/26 (LoVo, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.819×** | -3.3 | 0.019 | 7/26 (KATO III, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.58 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4801. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 234 | 0 | 21 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0906× (z -27.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.116× (z -17.3) |
| [[Hs 766T (line)]] | wt | 119 | 0 | 19 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0973× (z -20.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0671× (z -16.1) |
| [[KATO III (line)]] | alt | 91.6 | 0 | 18 (13 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0679× (z -20.9) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.175× (z -13.0) |
| [[LoVo (line)]] | wt | 408 | 0 | 18 (13 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0277× (z -32.2) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.190× (z -14.9) |
| [[AsPC-1 (line)]] | alt | 113 | 0 | 15 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0478× (z -20.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0223× (z -17.1) |
| [[NCI-H1792 (line)]] | alt | 118 | 0 | 15 (12 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0274× (z -21.4) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0595× (z -16.1) |
| [[HT-29 (line)]] | alt | 45.3 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -16.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.231× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 100 | 0 | 10 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 29.5 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -12.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 27.8 | 0 | 7 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.213× (z -12.6) |
| [[H4 (line)]] | wt | 37.5 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0349× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[NCI-H1573 (line)]] | alt | 22.5 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -14.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 42.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.62× (z +15.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.31× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.0961× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 45.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 19.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -11.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[RPMI-7951 (line)]] | alt | 39.4 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.110× (z -11.5) |
| [[BT-474 (line)]] | alt | 19.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.46× (z +11.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[COLO 205 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0278× (z -14.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HEC-1-A (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -8.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H2347 (line)]] | alt | 14.2 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.21× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW1417 (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -9.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 2.90 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.88 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.69 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.06 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.77 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.90 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.13 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.85 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.01 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.52 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.33 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.02 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.58 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.97 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.36 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.86 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.88 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.48 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4801), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRR]] | +0.87 | +0.88 / +0.84 | both halves | 7e-06 | same gene group; ⚠ same locus (0.6 kb, same strand: neighbours can correlate without regulation) |
| [[UGT1A9]] | +0.67 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[B3GALT5]] | +0.67 | +0.63 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[UGT1A6]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[UGT1A1]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[UGT1A8]] | +0.62 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[MECOM]] | +0.61 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[GNA14]] | +0.60 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[AOAH]] | +0.58 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[GCNT3]] | +0.56 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[DOK5]] | +0.56 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[TMPRSS3]] | +0.56 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[TSPAN8]] | +0.55 | +0.58 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP3-1]] | -0.48 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[SEPTIN5]] | -0.47 | -0.58 / -0.27 | both halves | 3e-04 |  |
| [[JCAD]] | -0.46 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[SLC45A1]] | -0.45 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[MCF2L2]] | -0.45 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[CROCCP3]] | -0.45 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[STEAP3]] | -0.44 | -0.40 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*49 arrows, 49 of them with an alert ⚠; grade A 0, B 11, C 38. Shown: the 12 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IKZF2]] | B | IKZF2 activity raises PTPRB's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 3.02× lower at baseline in the lines without IKZF2 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |
| [[GNA14]] | B | GNA14 activity raises PTPRB's level | lines that do not express GNA14 (5) vs lines expressing it (45) | 4.92× lower at baseline in the lines without GNA14 | 0.032 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |
| [[MECOM]] | B | MECOM activity raises PTPRB's level | lines that do not express MECOM (18) vs lines expressing it (32) | 2.86× lower at baseline in the lines without MECOM | 0.039 | ⚠ within organs, on part of the lines; also absent: STYK1, IKZF2, TSTD1; maybe low, not absent |
| [[BOLA3-DT]] | B | BOLA3-DT activity lowers PTPRB's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 3.95× higher at baseline in the lines without BOLA3-DT | 0.044 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[MARCOL]], [[SPINK13]] | B | MARCOL, SPINK13 activity raises PTPRB's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 3.76× lower at baseline in the lines without MARCOL, SPINK13 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent genes |
| [[CREB3L1]] | B | CREB3L1 activity raises PTPRB's level | lines that do not express CREB3L1 (24) vs lines expressing it (26) | 2.61× lower at baseline in the lines without CREB3L1 | 0.068 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1 |
| [[C4BPB]] | B | C4BPB activity raises PTPRB's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 3.41× lower at baseline in the lines without C4BPB | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |
| [[JAK1]], [[JAK3]] | B | JAK1, JAK3 activity lowers PTPRB's level | compounds that target JAK1, JAK3: 2 of 2 raise it (Filgotinib, Tofacitinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets |
| [[PTPN22]] | B | PTPN22 activity raises PTPRB's level | lines that do not express PTPN22 (8) vs lines expressing it (42) | 3.25× lower at baseline in the lines without PTPN22 | 0.091 | ⚠ within organs, on part of the lines; also absent: PTPRE; maybe low, not absent |
| [[SATB1]] | B | SATB1 activity raises PTPRB's level | lines that do not express SATB1 (15) vs lines expressing it (35) | 2.22× lower at baseline in the lines without SATB1 | 0.092 | ⚠ within organs, on part of the lines; also absent: STING1, EFNB2, NR3C2 |
| [[NR3C1]] | B | NR3C1 activity lowers PTPRB's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 7.0% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[PTPRR]] | C | PTPRR activity raises PTPRB's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 5.76× lower at baseline in the lines without PTPRR | 8e-05 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2; co-absent with the target |

### Downstream of this gene

*73 arrows, 73 of them with an alert ⚠; grade A 0, B 30, C 43. Shown: the 12 strongest; 61 more arrows (61 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBM47]] | B | PTPRB activity raises RBM47's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 3.27× lower at baseline in the lines without PTPRB | 0.002 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[SEPTIN5]] | B | PTPRB activity lowers SEPTIN5's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 2.28× higher at baseline in the lines without PTPRB | 0.003 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[MUC20]] | B | PTPRB activity raises MUC20's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 2.40× lower at baseline in the lines without PTPRB | 0.007 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[BOLA3-DT]] | B | PTPRB activity lowers BOLA3-DT's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 1.73× higher at baseline in the lines without PTPRB | 0.011 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[ATP8B1]] | B | PTPRB activity raises ATP8B1's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 2.66× lower at baseline in the lines without PTPRB | 0.013 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[CROCCP3]] | B | PTPRB activity lowers CROCCP3's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 1.34× higher at baseline in the lines without PTPRB | 0.015 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[SEPTIN9-DT]] | B | PTPRB activity raises SEPTIN9-DT's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 1.48× lower at baseline in the lines without PTPRB | 0.017 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[BAG1]] | B | PTPRB activity raises BAG1's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 1.39× lower at baseline in the lines without PTPRB | 0.030 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[CROCCP3-1]] | B | PTPRB activity lowers CROCCP3-1's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 1.44× higher at baseline in the lines without PTPRB | 0.034 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[IKZF2]] | B | PTPRB activity raises IKZF2's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 2.35× lower at baseline in the lines without PTPRB | 0.036 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[PTPN22]] | B | PTPRB activity raises PTPN22's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 1.70× lower at baseline in the lines without PTPRB | 0.039 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[PRR15-DT]] | B | PTPRB activity raises PRR15-DT's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 2.00× lower at baseline in the lines without PTPRB | 0.039 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.558). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.8, 51.3); signed map (64.0, 3.4). **Vector** length 105, 34.3% of its response variance represented; |z| ≥ 3 in 977 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glucuronidation* (reactome, mean cos +0.64 to 4); *Aspirin ADME* (reactome, mean cos +0.64 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +6.8 | -9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.1 | -1.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.0 | +0.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.9 | -0.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | +4.9 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | -4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | -1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +4.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +1.5 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -3.8 | -4.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.5 | -4.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.8 | -2.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.7 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.7 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase receptor type B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q15 — chr12:70,515,870-70,637,440 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PTPB |
| Gene groups (HGNC) | Fibronectin type III domain containing; Protein tyrosine phosphatases receptor type |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [P23467](https://www.uniprot.org/uniprotkb/P23467) (Receptor-type tyrosine-protein phosphatase beta):

> Plays an important role in blood vessel remodeling and angiogenesis. Not necessary for the initial formation of blood vessels, but is essential for their maintenance and remodeling. Can induce dephosphorylation of TEK/TIE2, CDH5/VE-cadherin and KDR/VEGFR-2. Regulates angiopoietin-TIE2 signaling in endothelial cells. Acts as a negative regulator of TIE2, and controls TIE2 driven endothelial cell proliferation, which in turn affects blood vessel remodeling during embryonic development and …

**Summary**, from NCBI Gene [5787](https://www.ncbi.nlm.nih.gov/gene/5787):

> The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This PTP contains an extracellular domain, a single transmembrane segment and one intracytoplasmic catalytic domain, thus belongs to receptor type PTP. The extracellular region of this PTP is composed of multiple fibronectin …

**Accessions** — [HGNC:9665](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9665) · Entrez [5787](https://www.ncbi.nlm.nih.gov/gene/5787) · UniProt [P23467](https://www.uniprot.org/uniprotkb/P23467) · Ensembl [ENSG00000127329](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127329)

## Data

Gene col 4801: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4801); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4801, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4801]; `tensor/DDL_lfc|DDL_z.npy` [4801]; `embed/gene_vectors.npy` [4801]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4801 or target_col == 4801). Every well: [[PTPRB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPRB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
