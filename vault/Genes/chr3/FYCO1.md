---
symbol: "FYCO1"
type: "gene"
col: 8789
ensembl_id: "ENSG00000163820"
name: "FYVE and coiled-coil domain autophagy adaptor 1"
location: "3p21.31"
module: 33
arm: "+"
pooled_cpm: 29.36
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 22
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# FYCO1

*FYVE and coiled-coil domain autophagy adaptor 1* — 3p21.31

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.385× (z -19.4, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL42]] (+0.62, fdr 3e-05), [[DLD]] (+0.60, fdr 1e-04), [[RABGGTB]] (+0.58, fdr 3e-05); moves opposite to [[THUMPD3-AS1]] (-0.68, fdr 7e-06), [[ZNF846]] (-0.58, fdr 1e-05), [[PIPOX]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8789.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 1.27× | +3.4 | 0.35 | 17/46 (SW480, HCT15, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8789.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.385×** | -19.4 | 0e+00 | 46/47 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.510×** | -13.7 | 4e-40 | 36/46 (NCI-H23, C32, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.479×** | -10.6 | 7e-24 | 39/46 (KATO III, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.530×** | -9.1 | 1e-17 | 38/47 (PANC-1, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.533×** | -9.1 | 2e-17 | 37/47 (SNU-423, RPMI-7951, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.517×** | -8.8 | 9e-17 | 37/46 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.577×** | -7.9 | 2e-13 | 37/46 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.592×** | -7.0 | 1e-10 | 33/47 (SW48, SW480, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.423×** | -6.5 | 7e-09 | 34/47 (PANC-1, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.619×** | -6.4 | 7e-09 | 30/47 (J82, HEC-1-A, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.666×** | -5.8 | 3e-07 | 29/46 (SNU-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.670×** | -5.8 | 4e-07 | 31/47 (PANC-1, SNU-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.771×** | -5.3 | 5e-06 | 26/47 (SW1417, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.685×** | -5.1 | 2e-05 | 26/44 (RKO, SNU-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **0.709×** | -4.6 | 1e-04 | 29/46 (COLO 205, PANC-1, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.778×** | -3.6 | 0.011 | 19/47 (SW48, RKO, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.779×** | -3.6 | 0.011 | 19/46 (HS-578T, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.645×** | -3.3 | 0.027 | 17/46 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8789. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 43.0 | 0 | 8 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0977× (z -14.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -12.9) |
| [[PANC-1 (line)]] | alt | 21.2 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -17.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.207× (z -14.5) |
| [[RKO (line)]] | wt | 51.1 | 0 | 7 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.119× (z -16.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 68.2 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -17.2) |
| [[MIA PaCa-2 (line)]] | alt | 34.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0936× (z -18.6) |
| [[NCI-H2030 (line)]] | alt | 34.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -11.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -10.1) |
| [[SNU-423 (line)]] | alt | 34.6 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.218× (z -11.0) |
| [[HCT15 (line)]] | alt | 46.2 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -11.2) |
| [[HS-578T (line)]] | alt | 31.1 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -11.9) |
| [[LoVo (line)]] | wt | 30.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -13.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[LS 180 (line)]] | wt | 37.2 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.314× (z -9.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 21.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -15.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.379× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 38.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -15.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -11.6) |
| [[SW1417 (line)]] | alt | 33.2 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -16.8) |
| [[SW480 (line)]] | alt | 33.6 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -18.4) |
| [[A-172 (line)]] | wt | 25.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -11.4) |
| [[A498 (line)]] | wt | 19.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -9.0) |
| [[C-33 A (line)]] | alt | 42.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[C32 (line)]] | wt | 25.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -17.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -14.9) |
| [[COLO 205 (line)]] | alt | 23.2 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.111× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~46% of this change · without an alert: [[XRK3F2 (drug)]] 0.5 µM 0.0976× (z -8.9) |
| [[HOP62 (line)]] | alt | 21.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -14.9) |
| [[J82 (line)]] | alt | 23.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -12.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[KATO III (line)]] | alt | 29.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -13.9) |
| [[LOX-IMVI (line)]] | wt | 22.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -12.7) |
| [[NCI-H23 (line)]] | alt | 35.6 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0533× (z -22.1) |
| [[SK-MEL-2 (line)]] | alt | 51.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -15.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -14.0) |
| [[SW48 (line)]] | wt | 46.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -11.6) |
| [[A-427 (line)]] | wt | 32.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -18.5) |
| [[CFPAC-1 (line)]] | alt | 18.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -10.1) |
| [[CHP-212 (line)]] | wt | 36.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0917× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 18.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0771× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HT-29 (line)]] | alt | 22.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -12.3) |
| [[hTERT-HPNE (line)]] | wt | 20.1 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0914× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 36.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -10.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H2347 (line)]] | alt | 32.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -13.0) |
| [[Panc 03.27 (line)]] | alt | 38.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -11.5) |
| [[SHP-77 (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 21.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -11.0) |
| [[A549 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.94 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8789), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL42]] | +0.62 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[DLD]] | +0.60 | +0.36 / +0.58 | both halves | 1e-04 |  |
| [[RABGGTB]] | +0.58 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[ACTR5]] | +0.58 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[NDRG3]] | +0.58 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[PRPF19]] | +0.58 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[MTG1]] | +0.57 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[OCRL]] | +0.57 | +0.34 / +0.67 | both halves | 1e-04 |  |
| [[PTGES2]] | +0.57 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[FXN]] | +0.56 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[PRELID3B]] | +0.56 | +0.34 / +0.62 | both halves | 1e-04 |  |
| [[RPE]] | +0.55 | +0.53 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THUMPD3-AS1]] | -0.68 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[ZNF846]] | -0.58 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[PIPOX]] | -0.56 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[SNHG31]] | -0.56 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[C2orf92]] | -0.56 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[IRF3]] | -0.55 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[FBXO11]] | -0.55 | -0.19 / -0.59 | ⚠ one half (not replicated) | 9e-04 |  |
| [[GPAT4-AS1]] | -0.55 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[ANKHD1-DT]] | -0.55 | -0.48 / -0.37 | both halves | 7e-05 |  |
| [[AVIL]] | -0.55 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[PYY]] | -0.55 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[IPO9-AS1]] | -0.55 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[INTS6]] | -0.54 | -0.59 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises FYCO1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ENPP4]] | B | ENPP4 activity raises FYCO1's level | lines that do not express ENPP4 (17) vs lines expressing it (33) | 1.47× lower at baseline in the lines without ENPP4 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ACTR3C, SAMD12, ATP8A1 |
| [[CDCA7L]] | B | CDCA7L activity raises FYCO1's level | lines that do not express CDCA7L (8) vs lines expressing it (42) | 1.19× lower at baseline in the lines without CDCA7L | 0.071 | ⚠ within organs, on part of the lines |
| [[MRC2]] | B | MRC2 activity raises FYCO1's level | lines that do not express MRC2 (17) vs lines expressing it (33) | 1.17× lower at baseline in the lines without MRC2 | 0.075 | ⚠ within organs, on part of the lines; also absent: FBXO17, ENSG00000269547, FSD1 |
| [[NBEAP2]] | B | NBEAP2 activity raises FYCO1's level | lines that do not express NBEAP2 (5) vs lines expressing it (45) | 1.64× lower at baseline in the lines without NBEAP2 | 0.094 | ⚠ within organs, on part of the lines; also absent: C2orf27A, ROPN1L, ENSG00000287621 |
| [[C2orf92]] | C | C2orf92 activity raises FYCO1's level | lines that do not express C2orf92 (3) vs lines expressing it (47) | 1.83× lower at baseline in the lines without C2orf92 | 0.065 | ⚠ few lines (3 vs 47); across organs; also absent: HHAT, TBCEL, RUNDC3A-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.501). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-23.2, -35.1); signed map (-16.2, -46.5). **Vector** length 82.1, 18.2% of its response variance represented; |z| ≥ 3 in 1,107 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | -0.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +0.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.2 | +0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.1 | -1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | -0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +1.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -19.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -8.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -9.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -5.3 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.7 | -1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | +0.5 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | FYVE and coiled-coil domain autophagy adaptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:45,917,903-45,995,824 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13335, ZFYVE7 |
| Gene groups (HGNC) | Zinc fingers FYVE-type; GOLD domain containing; RUN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQS8](https://www.uniprot.org/uniprotkb/Q9BQS8) (FYVE and coiled-coil domain-containing protein 1):

> May mediate microtubule plus end-directed vesicle transport.

**Summary**, from NCBI Gene [79443](https://www.ncbi.nlm.nih.gov/gene/79443):

> The gene encodes a Rab7 adapter protein that is implicated in the microtubule transport of autophagosomes. The encoded protein contains a RUN domain, a FYVE-type zinc finger domain, and Golgi dynamics (GOLD) domain. The encoded protein plays a role in microtubule plus end-directed transport of autophagic vesicles through interactions with the small GTPase Rab7, phosphatidylinositol-3-phosphate (PI3P), the autophagosome marker LC3, and the kinesin KIF5. Mutations in this gene are associated with …

**Accessions** — [HGNC:14673](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14673) · Entrez [79443](https://www.ncbi.nlm.nih.gov/gene/79443) · UniProt [Q9BQS8](https://www.uniprot.org/uniprotkb/Q9BQS8) · Ensembl [ENSG00000163820](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163820)

## Data

Gene col 8789: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8789); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8789, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8789]; `tensor/DDL_lfc|DDL_z.npy` [8789]; `embed/gene_vectors.npy` [8789]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8789 or target_col == 8789). Every well: [[FYCO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FYCO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
