---
symbol: "LRRC41"
type: "gene"
col: 5276
ensembl_id: "ENSG00000132128"
name: "leucine rich repeat containing 41"
location: "1p34.1-p33"
module: 156
arm: "+"
pooled_cpm: 49.15
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 16
n_dd_up_clean: 10
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/156"]
generated_by: "tahoemap"
---

# LRRC41

*leucine rich repeat containing 41* — 1p34.1-p33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.43× (z +10.3, q 5e-22, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.267× (z -26.9, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXW9]] (+0.72, fdr 3e-05), [[ISY1-RAB43]] (+0.71, fdr 1e-05), [[TRIM39]] (+0.69, fdr 3e-05); moves opposite to [[SSX2IP]] (-0.62, fdr 2e-05), [[AFDN]] (-0.59, fdr 3e-04), [[TSPAN15]] (-0.58, fdr 1e-04).
> It is in [[Module 156]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PLS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5276.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +10.3 | 5e-22 | 37/48 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +9.6 | 2e-19 | 37/48 (SW480, A-172, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.92×** | +6.9 | 7e-10 | 30/49 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +6.7 | 3e-09 | 31/48 (SW480, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +6.4 | 2e-08 | 29/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +5.5 | 3e-06 | 27/48 (PANC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +5.0 | 5e-05 | 22/48 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.24×** | +4.5 | 6e-04 | 24/48 (PANC-1, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +4.3 | 9e-04 | 20/48 (NCI-H2030, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +4.0 | 0.004 | 19/48 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.060 | 14/48 (MIA PaCa-2, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.088 | 19/48 (PANC-1, SW480, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.088 | 10/48 (SW480, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5276.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.267×** | -26.9 | 0e+00 | 48/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.281×** | -25.9 | 0e+00 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.345×** | -21.7 | 0e+00 | 47/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.458×** | -15.9 | 0e+00 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.578×** | -15.8 | 0e+00 | 47/48 (SW480, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.535×** | -12.2 | 2e-32 | 34/42 (LoVo, SHP-77, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.578×** | -11.2 | 4e-27 | 44/48 (H4, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.415×** | -9.4 | 5e-19 | 44/48 (SW480, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.658×** | -8.5 | 1e-15 | 34/47 (LoVo, RKO, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.690×** | -7.3 | 2e-11 | 31/47 (SHP-77, C-33 A, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.720×** | -6.2 | 3e-08 | 25/44 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.738×** | -6.2 | 3e-08 | 32/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.766×** | -5.2 | 8e-06 | 28/48 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.775×** | -5.2 | 9e-06 | 28/48 (AN3 CA, C32, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.791×** | -4.6 | 2e-04 | 24/48 (LoVo, C32, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.848× | -3.2 | 0.036 | 14/47 (Hs 766T, CHP-212, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.746×** | -3.1 | 0.049 | 13/47 (Hs 766T, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.865× | -3.0 | 0.078 | 14/49 (AsPC-1, MIA PaCa-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5276. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 72.5 | 0 | 9 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -20.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.173× (z -20.2) |
| [[PANC-1 (line)]] | alt | 38.2 | 5 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.266× (z -14.9) |
| [[SW480 (line)]] | alt | 43.2 | 1 | 6 | [[Auranofin (drug)]] 5 µM 2.18× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.235× (z -19.4) |
| [[H4 (line)]] | wt | 86.6 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -14.1) |
| [[HOP62 (line)]] | alt | 60.6 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -18.4) |
| [[A-172 (line)]] | wt | 47.3 | 1 | 4 | [[Auranofin (drug)]] 5 µM 2.60× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -14.0) |
| [[C32 (line)]] | wt | 59.1 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.250× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 47.8 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -13.7) |
| [[HS-578T (line)]] | alt | 64.1 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.202× (z -15.7) |
| [[J82 (line)]] | alt | 46.0 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.228× (z -16.3) |
| [[LOX-IMVI (line)]] | wt | 42.2 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.216× (z -13.8) |
| [[NCI-H2347 (line)]] | alt | 33.2 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.292× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 51.1 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -18.5) |
| [[RKO (line)]] | wt | 87.4 | 0 | 5 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -15.4) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.202× (z -13.2) |
| [[RPMI-7951 (line)]] | alt | 63.8 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.238× (z -12.6) |
| [[SHP-77 (line)]] | alt | 48.9 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.267× (z -12.2) |
| [[SK-MEL-2 (line)]] | alt | 50.4 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.268× (z -11.1) |
| [[A498 (line)]] | wt | 43.6 | 1 (1 ⚠) | 3 | [[Selinexor (drug)]] 5 µM 1.86× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.242× (z -14.5) |
| [[AN3 CA (line)]] | alt | 73.7 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.149× (z -10.6) |
| [[HCT15 (line)]] | alt | 86.4 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.215× (z -13.0) |
| [[HepG2_C3A (line)]] | wt | 47.2 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.158× (z -13.8) |
| [[hTERT-HPNE (line)]] | wt | 66.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.148× (z -14.9) |
| [[MIA PaCa-2 (line)]] | alt | 73.9 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.233× (z -14.3) |
| [[NCI-H2030 (line)]] | alt | 53.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.290× (z -12.4) |
| [[SNU-423 (line)]] | alt | 47.4 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.223× (z -13.8) |
| [[SW 900 (line)]] | alt | 49.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.208× (z -13.2) |
| [[SW48 (line)]] | wt | 64.3 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.233× (z -10.9) |
| [[A-427 (line)]] | wt | 49.8 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -16.3) |
| [[A549 (line)]] | wt | 41.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.256× (z -12.5) |
| [[AsPC-1 (line)]] | alt | 38.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.281× (z -11.3) |
| [[BT-474 (line)]] | alt | 56.1 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.245× (z -12.6) |
| [[Hs 766T (line)]] | wt | 51.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.315× (z -11.1) |
| [[KATO III (line)]] | alt | 38.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.137× (z -17.5) |
| [[LS 180 (line)]] | wt | 37.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.315× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 36.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.356× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 54.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.227× (z -12.7) |
| [[Panc 03.27 (line)]] | alt | 47.2 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -12.1) |
| [[C-33 A (line)]] | alt | 63.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -12.5) |
| [[HEC-1-A (line)]] | alt | 29.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 50.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -12.2) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.318× (z -11.2) |
| [[SW1417 (line)]] | alt | 32.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.299× (z -10.9) |
| [[SNU-1 (line)]] | wt | 74.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -9.6) |
| [[CHP-212 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 79.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5276), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW9]] | +0.72 | +0.45 / +0.68 | both halves | 3e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[ISY1-RAB43]] | +0.71 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[TRIM39]] | +0.69 | +0.44 / +0.71 | both halves | 3e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[TRMT1]] | +0.69 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[ZNF263]] | +0.68 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[SPAG7]] | +0.67 | +0.39 / +0.69 | both halves | 5e-05 |  |
| [[TMEM11-DT]] | +0.66 | +0.39 / +0.64 | both halves | 5e-05 |  |
| [[FAM209A]] | +0.66 | +0.41 / +0.65 | both halves | 4e-05 |  |
| [[ZNF546]] | +0.66 | +0.33 / +0.58 | both halves | 1e-04 |  |
| [[GPN2]] | +0.66 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[RECQL5]] | +0.66 | +0.32 / +0.69 | both halves | 1e-04 |  |
| [[QRICH1]] | +0.65 | +0.68 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSX2IP]] | -0.62 | -0.46 / -0.63 | both halves | 2e-05 |  |
| [[AFDN]] | -0.59 | -0.28 / -0.49 | both halves | 3e-04 |  |
| [[TSPAN15]] | -0.58 | -0.33 / -0.63 | both halves | 1e-04 |  |
| [[HLTF]] | -0.58 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[HMGN3]] | -0.57 | -0.29 / -0.59 | both halves | 3e-04 |  |
| [[HMSD]] | -0.57 | -0.35 / -0.65 | both halves | 1e-04 |  |
| [[TMEM14A]] | -0.57 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[GDE1]] | -0.57 | -0.23 / -0.56 | both halves | 5e-04 |  |
| [[PLS1]] | -0.57 | -0.32 / -0.56 | both halves | 1e-04 |  |
| [[EFR3A]] | -0.57 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[CYB5A]] | -0.56 | -0.31 / -0.61 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLS1]] | B | PLS1 activity lowers LRRC41's level | lines that do not express PLS1 (14) vs lines expressing it (36) | 1.25× higher at baseline in the lines without PLS1 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: NRARP, MYO5C, MLXIPL |
| [[HMSD]] | B | HMSD activity raises LRRC41's level | lines that do not express HMSD (26) vs lines expressing it (24) | 1.14× lower at baseline in the lines without HMSD | 0.034 | ⚠ within organs, on part of the lines; also absent: LGSN, LRRN2, HEYL |
| [[TSPAN15]] | B | TSPAN15 activity lowers LRRC41's level | lines that do not express TSPAN15 (15) vs lines expressing it (35) | 1.33× higher at baseline in the lines without TSPAN15 | 0.041 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent |
| [[PRKAR2B]] | B | PRKAR2B activity raises LRRC41's level | lines that do not express PRKAR2B (12) vs lines expressing it (38) | 1.32× lower at baseline in the lines without PRKAR2B | 0.048 | ⚠ within organs, on part of the lines; also absent: EML1, GALNT16, KATNAL2 |
| [[RAB3IP]] | B | RAB3IP activity lowers LRRC41's level | lines that do not express RAB3IP (8) vs lines expressing it (42) | 1.25× higher at baseline in the lines without RAB3IP | 0.059 | ⚠ within organs, on part of the lines; also absent: TBC1D30, CXCL16, ENSG00000288591; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 156]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.637). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.3, 18.6); signed map (6.8, 0.5). **Vector** length 107, 29.8% of its response variance represented; |z| ≥ 3 in 1,192 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +15.5 | +10.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.9 | +9.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.3 | -0.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.6 | +6.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.9 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | -0.6 |
|  | [[EX229 (drug)]] 5 µM |  | +3.2 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.0 | +3.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.5 | -15.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.8 | -11.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.6 | -7.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.6 | -15.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.6 | -9.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.5 | -2.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 41 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1-p33 — chr1:46,261,196-46,303,616 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MUF1 |
| Reactome | 6 pathways, smallest: RHOBTB3 ATPase cycle; Neddylation; Antigen processing: Ubiquitination & Proteasome degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15345](https://www.uniprot.org/uniprotkb/Q15345) (Leucine-rich repeat-containing protein 41):

> Probable substrate recognition component of an ECS (Elongin BC-CUL2/5-SOCS-box protein) E3 ubiquitin ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins.

**Summary**, from NCBI Gene [10489](https://www.ncbi.nlm.nih.gov/gene/10489):

> Predicted to enable identical protein binding activity. Predicted to be involved in protein ubiquitination. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16917](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16917) · Entrez [10489](https://www.ncbi.nlm.nih.gov/gene/10489) · UniProt [Q15345](https://www.uniprot.org/uniprotkb/Q15345) · Ensembl [ENSG00000132128](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132128)

## Data

Gene col 5276: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5276); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5276, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5276]; `tensor/DDL_lfc|DDL_z.npy` [5276]; `embed/gene_vectors.npy` [5276]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5276 or target_col == 5276). Every well: [[LRRC41 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC41.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
