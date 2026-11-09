---
symbol: "VSIG10"
type: "gene"
col: 10754
ensembl_id: "ENSG00000176834"
name: "V-set and immunoglobulin domain containing 10"
location: "12q24.23"
module: 46
arm: "+"
pooled_cpm: 24.06
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 25
n_dd_up_clean: 7
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# VSIG10

*V-set and immunoglobulin domain containing 10* — 12q24.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.51× (z +12.7, q 5e-34, up in 36 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.54× (z +8.4, q 1e-14, up in 30 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.460× (z -15.0, q 0e+00, down in 35 of 46 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF362]] (+0.59, fdr 1e-04), [[ALDH1A3-AS1]] (+0.58, fdr 3e-05), [[AK3]] (+0.58, fdr 1e-04); moves opposite to [[MRPL17]] (-0.59, fdr 3e-05), [[RING1]] (-0.58, fdr 3e-05), [[MRPL2]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[OXCT1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10754.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.51×** | +12.7 | 5e-34 | 36/40 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.54×** | +12.3 | 2e-32 | 31/33 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +8.4 | 1e-14 | 30/46 (LS 180, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.55×** | +5.6 | 3e-06 | 20/34 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.49×** | +5.5 | 4e-06 | 28/47 (KATO III, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.29×** | +5.0 | 6e-05 | 22/47 (LOX-IMVI, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.003 | 17/47 (NCI-H23, AsPC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.34×** | +4.0 | 0.004 | 23/46 (KATO III, RKO, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.29×** | +3.5 | 0.025 | 15/46 (A549, PANC-1, …) | inconsistent across doses |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.29×** | +3.5 | 0.025 | 10/46 (AsPC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.071 | 13/46 (NCI-H1573, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | 1.25× | +3.0 | 0.11 | 6/46 (SNU-423, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10754.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.460×** | -15.0 | 0e+00 | 35/46 (COLO 205, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.407×** | -11.8 | 7e-30 | 41/46 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.467×** | -10.4 | 4e-23 | 40/47 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.484×** | -9.9 | 4e-21 | 35/46 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.560×** | -7.9 | 2e-13 | 28/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.388×** | -6.8 | 1e-09 | 33/47 (A-427, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.617×** | -6.6 | 3e-09 | 27/46 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.622×** | -6.5 | 6e-09 | 24/46 (SW480, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.406×** | -6.5 | 7e-09 | 30/45 (RKO, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.634×** | -6.2 | 3e-08 | 30/46 (HT-29, PANC-1, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.648×** | -5.9 | 2e-07 | 29/46 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.651×** | -5.9 | 2e-07 | 29/46 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.663×** | -5.6 | 9e-07 | 31/46 (PANC-1, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.675×** | -5.1 | 2e-05 | 26/46 (PANC-1, NCI-H661, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.729×** | -4.3 | 6e-04 | 25/46 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.647×** | -4.2 | 8e-04 | 16/47 (PANC-1, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.760×** | -3.7 | 0.006 | 21/47 (SW480, HT-29, …) | two highest doses | cell-cycle shift (explains ~15% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10754. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 32.7 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -16.4) |
| [[PANC-1 (line)]] | alt | 28.3 | 2 (2 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.10× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -19.8) |
| [[SW480 (line)]] | alt | 27.2 | 0 | 7 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.152× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.194× (z -15.6) |
| [[COLO 205 (line)]] | alt | 47.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0352× (z -33.6) |
| [[BT-474 (line)]] | alt | 37.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -13.2) |
| [[HEC-1-A (line)]] | alt | 41.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +11.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.279× (z -12.2) |
| [[LoVo (line)]] | wt | 27.2 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.92× (z +13.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -13.2) |
| [[SNU-1 (line)]] | wt | 30.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -12.3) |
| [[A-427 (line)]] | wt | 45.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.245× (z -12.8) |
| [[A498 (line)]] | wt | 30.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -18.9) |
| [[LOX-IMVI (line)]] | wt | 17.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -12.2) |
| [[SW1417 (line)]] | alt | 40.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +10.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.301× (z -10.1) |
| [[A-172 (line)]] | wt | 25.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -15.4) |
| [[A549 (line)]] | wt | 21.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -14.7) |
| [[HepG2_C3A (line)]] | wt | 28.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.176× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.305× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 31.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 22.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 15.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 39.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.246× (z -9.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 26.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.212× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[C32 (line)]] | wt | 9.94 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.108× (z -9.3) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 9.63 | 0 | 1 | — | [[Macitentan (drug)]] 5 µM 0.0966× (z -8.6) |
| [[J82 (line)]] | alt | 27.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -16.0) |
| [[KATO III (line)]] | alt | 29.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.325× (z -8.5) |
| [[LS 180 (line)]] | wt | 25.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +9.7) | — |
| [[NCI-H23 (line)]] | alt | 22.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -16.5) |
| [[NCI-H661 (line)]] | alt | 47.5 | 0 | 1 | — | [[Capmatinib (drug)]] 0.05 µM 0.0612× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 20.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.258× (z -8.6) |
| [[RKO (line)]] | wt | 22.8 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0323× (z -10.7) |
| [[AN3 CA (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.83 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10754), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF362]] | +0.59 | +0.55 / +0.36 | both halves | 1e-04 |  |
| [[ALDH1A3-AS1]] | +0.58 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[AK3]] | +0.58 | +0.51 / +0.33 | both halves | 1e-04 |  |
| [[ABRACL]] | +0.57 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[GALNT7]] | +0.56 | +0.51 / +0.34 | both halves | 1e-04 |  |
| [[HOTAIR]] | +0.56 | +0.42 / +0.29 | both halves | 2e-04 |  |
| [[HOXB7]] | +0.56 | +0.49 / +0.35 | both halves | 1e-04 |  |
| [[GOLGA2P5-1]] | +0.55 | +0.56 / +0.23 | both halves | 5e-04 |  |
| [[LAMTOR5-AS1]] | +0.55 | +0.49 / +0.36 | both halves | 9e-05 |  |
| [[TMCO4]] | +0.55 | +0.55 / +0.31 | both halves | 2e-04 |  |
| [[RCC2]] | +0.55 | +0.46 / +0.33 | both halves | 1e-04 |  |
| [[IQCH-AS1]] | +0.54 | +0.47 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL17]] | -0.59 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[RING1]] | -0.58 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[MRPL2]] | -0.54 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[RARS1]] | -0.54 | -0.51 / -0.29 | both halves | 3e-04 |  |
| [[RELA]] | -0.52 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[XRRA1]] | -0.52 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[COPE]] | -0.51 | -0.48 / -0.29 | both halves | 3e-04 |  |
| [[CFDP1]] | -0.51 | -0.52 / -0.25 | both halves | 4e-04 |  |
| [[MED8]] | -0.51 | -0.50 / -0.22 | both halves | 6e-04 |  |
| [[DDX50]] | -0.50 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[DIABLO]] | -0.50 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[SLFN11]] | -0.50 | -0.33 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OXCT1]] | B | OXCT1 activity lowers VSIG10's level | lines that do not express OXCT1 (8) vs lines expressing it (42) | 1.63× higher at baseline in the lines without OXCT1 | 0.038 | ⚠ within organs, on part of the lines |
| [[CA12]] | B | CA12 activity lowers VSIG10's level | lines that do not express CA12 (29) vs lines expressing it (21) | 1.45× higher at baseline in the lines without CA12 | 0.084 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1 |
| [[OXCT1]] | B | OXCT1 activity weakens VSIG10's drug response | lines that do not express OXCT1 (8) vs lines expressing it (39) | the lines without OXCT1 respond 1.30× as strongly (z diff -1.34); strongest at Digitoxin 5 µM: 0.38x vs 0.56x (z diff -3.2) | 0.094 | ⚠ within organs, on part of the lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.531). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-1.5, 24.8); signed map (35.9, -16.6). **Vector** length 76.7, 17.4% of its response variance represented; |z| ≥ 3 in 1,091 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +5.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +3.3 | +5.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +12.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +4.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +1.9 | +1.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.6 | +4.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.1 | -6.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.8 | -11.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.7 | -15.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -0.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -3.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.8 | -4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | V-set and immunoglobulin domain containing 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.23 — chr12:118,063,593-118,136,026 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | V-set domain containing; I-set domain containing |
| Matched by | ensembl_id |

UniProt [Q8N0Z9](https://www.uniprot.org/uniprotkb/Q8N0Z9) carries no function annotation.

**Summary**, from NCBI Gene [54621](https://www.ncbi.nlm.nih.gov/gene/54621):

> Predicted to enable cell adhesion molecule binding activity. Predicted to be involved in cell-cell adhesion and synapse assembly. Predicted to be located in membrane. Predicted to be active in cell-cell junction and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26078](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26078) · Entrez [54621](https://www.ncbi.nlm.nih.gov/gene/54621) · UniProt [Q8N0Z9](https://www.uniprot.org/uniprotkb/Q8N0Z9) · Ensembl [ENSG00000176834](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176834)

## Data

Gene col 10754: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10754); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10754, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10754]; `tensor/DDL_lfc|DDL_z.npy` [10754]; `embed/gene_vectors.npy` [10754]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10754 or target_col == 10754). Every well: [[VSIG10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VSIG10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
