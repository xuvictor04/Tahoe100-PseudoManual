---
symbol: "ADGRE5"
type: "gene"
col: 4409
ensembl_id: "ENSG00000123146"
name: "adhesion G protein-coupled receptor E5"
location: "19p13.12"
module: 162
arm: "+"
pooled_cpm: 51.62
n_lines_expressing: 43
n_dd_up: 9
n_dd_down: 27
n_dd_up_clean: 5
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/162"]
generated_by: "tahoemap"
---

# ADGRE5

*adhesion G protein-coupled receptor E5* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.45× (z +7.9, q 1e-12, up in 22 of 40 measured lines) ⚠ cell-cycle shift, explains ~77% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.29× (z +5.4, q 1e-05, up in 21 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.602× (z -10.7, q 6e-24, down in 31 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SOX13]] (+0.68, fdr 7e-06), [[LMNA]] (+0.62, fdr 1e-05), [[MIR23AHG]] (+0.61, fdr 7e-06); moves opposite to [[VPS39]] (-0.51, fdr 9e-05), [[CLCC1]] (-0.50, fdr 3e-05), [[SDHD]] (-0.47, fdr 7e-05).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4409.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.45×** | +7.9 | 1e-12 | 22/40 (RKO, HOP62, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.78×** | +7.5 | 2e-11 | 20/41 (HOP62, H4, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +5.5 | 8e-06 | 20/40 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +5.4 | 1e-05 | 21/41 (C32, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.005 | 17/41 (SW1417, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.29×** | +3.8 | 0.011 | 18/41 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.43×** | +3.8 | 0.011 | 18/41 (H4, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.05 µM |  | **1.30×** | +3.8 | 0.012 | 13/41 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.096 | 13/40 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 1.22× | +3.1 | 0.13 | 12/41 (Panc 03.27, NCI-H2347, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4409.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.602×** | -10.7 | 6e-24 | 31/40 (MIA PaCa-2, SW1417, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.589×** | -7.9 | 8e-13 | 26/41 (SW480, A549, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.617×** | -7.2 | 1e-10 | 26/41 (A549, SNU-423, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.591×** | -6.8 | 1e-09 | 27/41 (SW48, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.600×** | -6.6 | 4e-09 | 30/41 (LS 180, RKO, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.626×** | -6.6 | 4e-09 | 29/41 (HOP62, A-172, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.690×** | -5.5 | 3e-06 | 26/41 (A-172, HOP62, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.674×** | -5.4 | 4e-06 | 27/41 (HCT15, LoVo, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.716×** | -5.0 | 4e-05 | 22/41 (A-172, A549, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.724×** | -4.8 | 9e-05 | 22/41 (HOP62, A-172, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.738×** | -4.5 | 3e-04 | 20/41 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.708×** | -4.5 | 4e-04 | 23/40 (LoVo, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.745×** | -4.4 | 5e-04 | 19/40 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.813×** | -4.4 | 5e-04 | 15/41 (HOP62, Hs 766T, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.718×** | -4.3 | 7e-04 | 23/40 (LoVo, HCT15, …) | all doses, flat | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.819×** | -4.2 | 0.001 | 24/41 (Hs 766T, A498, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.773×** | -3.8 | 0.004 | 13/41 (HCT15, LoVo, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.823×** | -3.6 | 0.008 | 14/41 (LoVo, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4409. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 43.2 | 2 (2 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +11.3) ⚠ cell-cycle shift, explains ~77% of this change | [[Ixazomib citrate (drug)]] 0.5 µM 0.304× (z -10.0) |
| [[LoVo (line)]] | wt | 49.3 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -11.1) |
| [[A-172 (line)]] | wt | 134 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.0) ⚠ cell-cycle shift, explains ~77% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.349× (z -11.3) ⚠ cell-cycle shift, explains ~44% of this change |
| [[KATO III (line)]] | alt | 46.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -9.2) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -9.1) |
| [[RKO (line)]] | wt | 45.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +14.0) ⚠ cell-cycle shift, explains ~77% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change |
| [[RPMI-7951 (line)]] | alt | 67.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +10.1) ⚠ cell-cycle shift, explains ~77% of this change | [[Bortezomib (drug)]] 5 µM 0.110× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~43% of this change |
| [[SNU-423 (line)]] | alt | 51.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.328× (z -8.9) |
| [[SW1417 (line)]] | alt | 59.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +11.2) ⚠ cell-cycle shift, explains ~77% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -14.3) |
| [[A549 (line)]] | wt | 42.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.253× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 90.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -12.2) |
| [[C32 (line)]] | wt | 38.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0635× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[CFPAC-1 (line)]] | alt | 28.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +9.1) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[HEC-1-A (line)]] | alt | 89.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -9.9) |
| [[Hs 766T (line)]] | wt | 75.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -13.1) |
| [[HS-578T (line)]] | alt | 57.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +8.6) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[LOX-IMVI (line)]] | wt | 30.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +9.9) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[LS 180 (line)]] | wt | 94.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 71.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -21.9) |
| [[NCI-H23 (line)]] | alt | 34.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +8.5) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[Panc 03.27 (line)]] | alt | 84.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -11.7) |
| [[PANC-1 (line)]] | alt | 38.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 45.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -12.1) |
| [[SW 900 (line)]] | alt | 44.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -9.1) |
| [[SW480 (line)]] | alt | 79.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.428× (z -8.5) |
| [[A-427 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 96.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.28 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.53 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.15 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.71 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.09 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 32.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4409), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOX13]] | +0.68 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[LMNA]] | +0.62 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[MIR23AHG]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[VDR]] | +0.58 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[MAP2K3]] | +0.57 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[HIVEP3]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[HES1]] | +0.56 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[IER2]] | +0.56 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[SFR1]] | +0.56 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[PLK3]] | +0.56 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[BAIAP2L1]] | +0.55 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[EPHB3]] | +0.55 | +0.43 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS39]] | -0.51 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[CLCC1]] | -0.50 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[SDHD]] | -0.47 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[WASH2P-1]] | -0.47 | -0.37 / -0.45 | both halves | 9e-05 |  |
| [[ADPGK]] | -0.47 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[GARS1-DT]] | -0.47 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[ANGEL2]] | -0.47 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[UQCC1]] | -0.47 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[C8orf76]] | -0.47 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[ATP6V1E1]] | -0.46 | -0.38 / -0.36 | both halves | 9e-05 |  |
| [[BABAM1]] | -0.46 | -0.42 / -0.40 | both halves | 4e-05 |  |
| [[GHITM]] | -0.45 | -0.43 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ADGRE5's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NEDD9]] | B | NEDD9 activity raises ADGRE5's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 1.80× lower at baseline in the lines without NEDD9 | 0.072 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction 0.715). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.8, -0.7); signed map (5.6, 27.1). **Vector** length 117, 32.9% of its response variance represented; |z| ≥ 3 in 977 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | +5.9 | +7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +5.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +5.5 | +7.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.1 | +0.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | -2.2 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +2.3 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +2.3 | +3.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -6.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.8 | -6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -3.7 | -5.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -6.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.4 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.1 | -5.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | adhesion G protein-coupled receptor E5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:14,380,501-14,408,725 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TM7LN1; previously CD97 |
| Gene groups (HGNC) | CD molecules; Adhesion G protein-coupled receptors, subfamily E |
| Reactome | 5 pathways, smallest: Class B/2 (Secretin family receptors); GPCR ligand binding; Signaling by GPCR |
| Matched by | ensembl_id |

**Function**, from UniProt [P48960](https://www.uniprot.org/uniprotkb/P48960) (Adhesion G protein-coupled receptor E5):

> Receptor potentially involved in both adhesion and signaling processes early after leukocyte activation. Plays an essential role in leukocyte migration.

**Summary**, from NCBI Gene [976](https://www.ncbi.nlm.nih.gov/gene/976):

> This gene encodes a member of the EGF-TM7 subfamily of adhesion G protein-coupled receptors, which mediate cell-cell interactions. These proteins are cleaved by self-catalytic proteolysis into a large extracellular subunit and seven-span transmembrane subunit, which associate at the cell surface as a receptor complex. The encoded protein may play a role in cell adhesion as well as leukocyte recruitment, activation and migration, and contains multiple extracellular EGF-like repeats which mediate …

**Accessions** — [HGNC:1711](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1711) · Entrez [976](https://www.ncbi.nlm.nih.gov/gene/976) · UniProt [P48960](https://www.uniprot.org/uniprotkb/P48960) · Ensembl [ENSG00000123146](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123146)

## Data

Gene col 4409: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4409); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4409, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4409]; `tensor/DDL_lfc|DDL_z.npy` [4409]; `embed/gene_vectors.npy` [4409]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4409 or target_col == 4409). Every well: [[ADGRE5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADGRE5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
