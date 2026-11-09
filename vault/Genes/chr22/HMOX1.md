---
symbol: "HMOX1"
type: "gene"
col: 1914
ensembl_id: "ENSG00000100292"
name: "heme oxygenase 1"
location: "22q12.3"
module: 125
arm: "+"
pooled_cpm: 23.22
n_lines_expressing: 41
n_dd_up: 37
n_dd_down: 13
n_dd_up_clean: 31
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# HMOX1

*heme oxygenase 1* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 103× (z +43.6, q 0e+00, up in 38 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.627× (z -4.4, q 0.007, down in 15 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SQSTM1]] (+0.62, fdr 7e-06), [[OSGIN1]] (+0.59, fdr 1e-05), [[LINC02154]] (+0.54, fdr 2e-05); moves opposite to [[ACTL6A]] (-0.53, fdr 8e-05), [[MCM8]] (-0.50, fdr 4e-05), [[ODF2]] (-0.50, fdr 3e-05).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RPLP0P2]] → it (grade B ⚠); 2 go from it, the strongest it → [[PPP2R5C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1914.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **103×** | +43.6 | 0e+00 | 38/38 (A498, NCI-H2347, …) | rises with dose |  |
| [[Auranofin (drug)]] 0.5 µM |  | **6.20×** | +17.2 | 0e+00 | 36/37 (RKO, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.75×** | +9.5 | 3e-19 | 27/35 (CFPAC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Infigratinib (drug)]] 5 µM |  | **6.84×** | +9.5 | 4e-19 | 29/37 (A498, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.51×** | +8.7 | 4e-16 | 27/38 (A-427, SNU-423, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.01×** | +6.6 | 4e-09 | 22/38 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.09×** | +6.6 | 5e-09 | 25/37 (A-172, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.98×** | +6.4 | 9e-09 | 27/38 (NCI-H460, A549, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.97×** | +6.4 | 1e-08 | 20/38 (SNU-423, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.47×** | +5.1 | 2e-05 | 23/39 (A-427, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +4.8 | 8e-05 | 23/38 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.50×** | +4.5 | 3e-04 | 14/30 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.60×** | +4.5 | 4e-04 | 17/37 (A-172, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.51×** | +3.9 | 0.004 | 15/38 (COLO 205, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.50×** | +3.8 | 0.005 | 14/38 (J82, NCI-H23, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.52×** | +3.8 | 0.005 | 18/38 (A549, NCI-H1573, …) | rises with dose | position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.006 | 17/39 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1914.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.627×** | -4.4 | 0.007 | 15/38 (NCI-H1573, HS-578T, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.675×** | -3.7 | 0.027 | 15/38 (HS-578T, NCI-H1573, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.676×** | -3.7 | 0.027 | 17/38 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.677×** | -3.6 | 0.027 | 15/38 (NCI-H1573, HS-578T, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.680×** | -3.6 | 0.027 | 14/38 (HS-578T, NCI-H1573, …) | all doses, flat |  |
| [[Ciclopirox (drug)]] 5 µM |  | **0.762×** | -3.6 | 0.027 | 15/38 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.671×** | -3.6 | 0.027 | 19/37 (MIA PaCa-2, SNU-423, …) | rises with dose |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **0.679×** | -3.4 | 0.045 | 11/38 (HepG2/C3A, NCI-H1573, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.697×** | -3.4 | 0.046 | 14/38 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ciclopirox (drug)]] 0.5 µM |  | **0.699×** | -3.3 | 0.046 | 5/38 (A549, RPMI-7951, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.699×** | -3.2 | 0.063 | 16/36 (MIA PaCa-2, HS-578T, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.709×** | -3.2 | 0.063 | 7/38 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 5 µM |  | **0.536×** | -3.1 | 0.098 | 3/39 (PANC-1, SNU-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1914. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 63.6 | 2 | 12 (9 ⚠) | [[Auranofin (drug)]] 5 µM 7.42× (z +14.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -20.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.206× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 86.1 | 2 | 7 (7 ⚠) | [[Auranofin (drug)]] 5 µM 14.0× (z +15.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0737× (z -14.3) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H2030 (line)]] | alt | 166 | 4 (1 ⚠) | 5 (5 ⚠) | [[Auranofin (drug)]] 5 µM 8.00× (z +14.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -17.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 47.3 | 2 | 5 (3 ⚠) | [[Auranofin (drug)]] 5 µM 12.5× (z +17.0) | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.172× (z -11.8) |
| [[HS-578T (line)]] | alt | 65.8 | 2 | 4 (4 ⚠) | [[Auranofin (drug)]] 5 µM 40.5× (z +22.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -12.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 35.5 | 2 | 4 (1 ⚠) | [[Auranofin (drug)]] 5 µM 20.6× (z +13.5) | [[Belinostat (drug)]] 5 µM 0.0911× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ciclopirox (drug)]] 5 µM 0.183× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 68.7 | 2 | 4 (3 ⚠) | [[Auranofin (drug)]] 5 µM 10.1× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.133× (z -10.9) |
| [[SNU-423 (line)]] | alt | 21.1 | 3 (1 ⚠) | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 93.8× (z +22.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0595× (z -13.1) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H460 (line)]] | wt | 9.04 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 99.8× (z +19.1) | — |
| [[A498 (line)]] | wt | 23.6 | 3 | 0 | [[Auranofin (drug)]] 5 µM 56.5× (z +27.2) | — |
| [[CFPAC-1 (line)]] | alt | 7.35 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 203× (z +20.1) | — |
| [[HOP62 (line)]] | alt | 6.24 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 154× (z +18.0) | — |
| [[HT-29 (line)]] | alt | 6.79 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 92.7× (z +14.8) | — |
| [[NCI-H1792 (line)]] | alt | 26.0 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 41.4× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.132× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[NCI-H2347 (line)]] | alt | 9.84 | 3 | 0 | [[Auranofin (drug)]] 5 µM 81.9× (z +23.9) | — |
| [[A-172 (line)]] | wt | 6.41 | 2 | 0 | [[Auranofin (drug)]] 5 µM 235× (z +21.5) | — |
| [[HCT15 (line)]] | alt | 8.82 | 2 | 0 | [[Auranofin (drug)]] 5 µM 24.9× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 6.01 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 126× (z +14.6) | — |
| [[J82 (line)]] | alt | 21.8 | 2 | 0 | [[Auranofin (drug)]] 5 µM 45.0× (z +17.4) | — |
| [[KATO III (line)]] | alt | 7.10 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 62.0× (z +14.7) | — |
| [[RKO (line)]] | wt | 12.5 | 2 | 0 | [[Auranofin (drug)]] 5 µM 65.2× (z +17.0) | — |
| [[RPMI-7951 (line)]] | alt | 17.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 125× (z +18.1) | — |
| [[SK-MEL-2 (line)]] | alt | 6.51 | 2 | 0 | [[Auranofin (drug)]] 5 µM 106× (z +15.7) | — |
| [[SNU-1 (line)]] | wt | 23.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 42.5× (z +15.5) | — |
| [[A549 (line)]] | wt | 22.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 22.7× (z +14.4) | — |
| [[AN3 CA (line)]] | alt | 22.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 133× (z +15.1) | — |
| [[C-33 A (line)]] | alt | 12.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 25.4× (z +9.1) | — |
| [[C32 (line)]] | wt | 5.90 | 1 | 0 | [[Auranofin (drug)]] 5 µM 151× (z +16.5) | — |
| [[COLO 205 (line)]] | alt | 13.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 131× (z +16.1) | — |
| [[H4 (line)]] | wt | 5.86 | 1 | 0 | [[Auranofin (drug)]] 5 µM 186× (z +11.6) | — |
| [[HepG2_C3A (line)]] | wt | 13.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 44.6× (z +14.1) | — |
| [[hTERT-HPNE (line)]] | wt | 13.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 118× (z +15.1) | — |
| [[LoVo (line)]] | wt | 7.27 | 1 | 0 | [[Auranofin (drug)]] 5 µM 116× (z +16.6) | — |
| [[LOX-IMVI (line)]] | wt | 5.84 | 1 | 0 | [[Auranofin (drug)]] 5 µM 74.7× (z +13.0) | — |
| [[SW 900 (line)]] | alt | 6.54 | 1 | 0 | [[Auranofin (drug)]] 5 µM 147× (z +15.4) | — |
| [[SW1417 (line)]] | alt | 5.87 | 1 | 0 | [[Auranofin (drug)]] 5 µM 74.7× (z +15.1) | — |
| [[SW48 (line)]] | wt | 9.67 | 1 | 0 | [[Auranofin (drug)]] 5 µM 143× (z +12.3) | — |
| [[AsPC-1 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.89 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.56 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.92 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.51 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.46 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.47 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.58 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1914), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SQSTM1]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_APOPTOSIS; STRING 684 |
| [[OSGIN1]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[LINC02154]] | +0.54 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[TRADD]] | +0.53 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[SEPHS2]] | +0.51 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[RPLP0P2]] | +0.51 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[PHYKPL]] | +0.50 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[SLC26A11]] | +0.50 | +0.36 / +0.53 | both halves | 1e-04 |  |
| [[RNF223]] | +0.50 | +0.35 / +0.52 | both halves | 1e-04 |  |
| [[SPINK1]] | +0.49 | +0.32 / +0.55 | both halves | 2e-04 |  |
| [[CPEB1]] | +0.49 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[EID3]] | +0.49 | +0.52 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTL6A]] | -0.53 | -0.37 / -0.58 | both halves | 8e-05 |  |
| [[MCM8]] | -0.50 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[ODF2]] | -0.50 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[ATAD2]] | -0.49 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[CHEK1]] | -0.49 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[DUT]] | -0.49 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[KNTC1]] | -0.48 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[RAD51AP1]] | -0.48 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[GINS1]] | -0.47 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[SLF1]] | -0.47 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[DDX12P]] | -0.47 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[ALDH7A1]] | -0.47 | -0.43 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPLP0P2]] | B | RPLP0P2 activity lowers HMOX1's level | lines that do not express RPLP0P2 (7) vs lines expressing it (43) | 2.44× higher at baseline in the lines without RPLP0P2 | 0.054 | ⚠ within organs, on part of the lines; also absent: CAMK2N1, ETS2, CSTB; maybe low, not absent |
| [[CLIC2]] | B | CLIC2 activity lowers HMOX1's level | lines that do not express CLIC2 (14) vs lines expressing it (36) | 2.51× higher at baseline in the lines without CLIC2 | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526; maybe low, not absent |
| [[RNF223]] | B | RNF223 activity lowers HMOX1's level | lines that do not express RNF223 (28) vs lines expressing it (22) | 1.88× higher at baseline in the lines without RNF223 | 0.061 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, MPZL2 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP2R5C]] | B | HMOX1 activity lowers PPP2R5C's level | lines that do not express HMOX1 (9) vs lines expressing it (41) | 1.30× higher at baseline in the lines without HMOX1 | 0.050 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CACFD1]] | B | HMOX1 activity lowers CACFD1's level | lines that do not express HMOX1 (9) vs lines expressing it (41) | 1.42× higher at baseline in the lines without HMOX1 | 0.066 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.574). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-9.3, 43.5); signed map (36.4, 21.0). **Vector** length 110, 26.8% of its response variance represented; |z| ≥ 3 in 1,180 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +12.2 | +43.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +9.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.6 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +6.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +8.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.7 | +1.5 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.9 | -1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | -5.2 | -2.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -4.2 | -3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -3.4 | -3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.4 | +0.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.9 | -3.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -4.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.7 | -2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | heme oxygenase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:35,380,361-35,394,214 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bK286B10, HO-1 |
| Gene groups (HGNC) | Heme oxygenase family |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, APOPTOSIS, UV_RESPONSE_UP, XENOBIOTIC_METABOLISM, HYPOXIA, P53_PATHWAY |
| Reactome | 26 pathways, smallest: Regulation of HMOX1 expression and activity; The NLRP3 inflammasome; Heme degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P09601](https://www.uniprot.org/uniprotkb/P09601) (Heme oxygenase 1):

> [Heme oxygenase 1]: Catalyzes the oxidative cleavage of heme at the alpha-methene bridge carbon, released as carbon monoxide (CO), to generate biliverdin IXalpha, while releasing the central heme iron chelate as ferrous iron. Affords protection against programmed cell death and this cytoprotective effect relies on its ability to catabolize free heme and prevent it from sensitizing cells to undergo apoptosis.; [Heme oxygenase 1]: (Microbial infection) During SARS-COV-2 infection, promotes …

**Summary**, from NCBI Gene [3162](https://www.ncbi.nlm.nih.gov/gene/3162):

> Heme oxygenase, an essential enzyme in heme catabolism, cleaves heme to form biliverdin, which is subsequently converted to bilirubin by biliverdin reductase, and carbon monoxide, a putative neurotransmitter. Heme oxygenase activity is induced by its substrate heme and by various nonheme substances. Heme oxygenase occurs as 2 isozymes, an inducible heme oxygenase-1 and a constitutive heme oxygenase-2. HMOX1 and HMOX2 belong to the heme oxygenase family. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5013](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5013) · Entrez [3162](https://www.ncbi.nlm.nih.gov/gene/3162) · UniProt [P09601](https://www.uniprot.org/uniprotkb/P09601) · Ensembl [ENSG00000100292](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100292)

## Data

Gene col 1914: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1914); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1914, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1914]; `tensor/DDL_lfc|DDL_z.npy` [1914]; `embed/gene_vectors.npy` [1914]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1914 or target_col == 1914). Every well: [[HMOX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMOX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
