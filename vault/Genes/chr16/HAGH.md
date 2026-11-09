---
symbol: "HAGH"
type: "gene"
col: 733
ensembl_id: "ENSG00000063854"
name: "hydroxyacylglutathione hydrolase"
location: "16p13.3"
module: 145
arm: "+"
pooled_cpm: 18.55
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 20
n_dd_up_clean: 12
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# HAGH

*hydroxyacylglutathione hydrolase* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +9.2, q 2e-17, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.393× (z -12.4, q 2e-32, down in 43 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.521× (z -8.6, q 2e-15, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WIPI2]] (+0.70, fdr 4e-05), [[ZER1]] (+0.69, fdr 2e-05), [[SAP30L]] (+0.65, fdr 1e-05); moves opposite to [[GDAP1]] (-0.52, fdr 4e-04), [[KICS2]] (-0.51, fdr 5e-04), [[N6AMT1]] (-0.50, fdr 2e-04).
> It is in [[Module 145]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[STEAP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 733.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +9.2 | 2e-17 | 35/47 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.74×** | +7.3 | 6e-11 | 27/41 (SHP-77, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +6.9 | 8e-10 | 33/47 (A498, KATO III, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.51×** | +5.4 | 7e-06 | 30/47 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +5.3 | 1e-05 | 28/47 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +4.7 | 2e-04 | 16/28 (NCI-H1792, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +4.7 | 2e-04 | 26/48 (AsPC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.36×** | +4.0 | 0.004 | 15/47 (Hs 766T, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.005 | 22/48 (A498, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +3.9 | 0.006 | 15/36 (Hs 766T, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.67×** | +3.6 | 0.019 | 11/48 (NCI-H460, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.034 | 12/44 (SHP-77, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.039 | 12/45 (Hs 766T, HOP62, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.100 | 11/48 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.39×** | +3.0 | 0.100 | 6/46 (PANC-1, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 733.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.393×** | -12.4 | 2e-32 | 43/47 (PANC-1, A498, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.521×** | -8.6 | 2e-15 | 37/48 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.642×** | -8.3 | 2e-14 | 32/46 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.546×** | -7.7 | 2e-12 | 33/47 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.562×** | -7.6 | 2e-12 | 32/47 (A-427, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.411×** | -6.2 | 7e-08 | 31/45 (Hs 766T, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.651×** | -5.7 | 1e-06 | 29/46 (SNU-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.663×** | -5.5 | 4e-06 | 28/47 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.689×** | -4.9 | 5e-05 | 24/47 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.586×** | -4.8 | 7e-05 | 25/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.692×** | -4.6 | 2e-04 | 20/48 (PANC-1, NCI-H460, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.521×** | -4.5 | 3e-04 | 20/46 (A498, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.524×** | -4.5 | 3e-04 | 21/43 (HCT15, HepG2/C3A, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.527×** | -4.4 | 4e-04 | 20/45 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.532×** | -4.4 | 5e-04 | 18/47 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.548×** | -4.2 | 0.001 | 21/48 (SW 900, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.572×** | -3.9 | 0.004 | 19/45 (A498, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 733. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 40.2 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.182× (z -11.3) |
| [[PANC-1 (line)]] | alt | 15.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -13.5) |
| [[A498 (line)]] | wt | 19.3 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +10.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.211× (z -12.0) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.293× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 16.0 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +10.6) | [[Harringtonine (drug)]] 0.5 µM 0.269× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 25.2 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.153× (z -11.3) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.210× (z -9.4) |
| [[A-172 (line)]] | wt | 34.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -12.6) |
| [[RKO (line)]] | wt | 19.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -12.1) |
| [[SNU-1 (line)]] | wt | 34.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0426× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0689× (z -14.8) |
| [[A-427 (line)]] | wt | 28.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.105× (z -15.5) |
| [[A549 (line)]] | wt | 15.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 27.8 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0917× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0561× (z -13.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 32.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.157× (z -10.3) ⚠ toxic |
| [[H4 (line)]] | wt | 7.19 | 0 | 1 | — | [[Tofacitinib (drug)]] 0.05 µM 0.0618× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.303× (z -9.2) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 17.5 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0324× (z -10.0) |
| [[HT-29 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.241× (z -9.2) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 8.15 | 0 | 1 | — | [[Proglumide (drug)]] 0.05 µM 0.0788× (z -8.7) |
| [[LoVo (line)]] | wt | 20.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -10.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 11.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.169× (z -9.4) |
| [[SW1417 (line)]] | alt | 23.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -9.3) |
| [[BT-474 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 733), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WIPI2]] | +0.70 | +0.41 / +0.75 | both halves | 4e-05 |  |
| [[ZER1]] | +0.69 | +0.48 / +0.76 | both halves | 2e-05 |  |
| [[SAP30L]] | +0.65 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[MAP3K3]] | +0.65 | +0.41 / +0.69 | both halves | 4e-05 |  |
| [[FBXL20]] | +0.63 | +0.34 / +0.71 | both halves | 1e-04 |  |
| [[SPSB3]] | +0.62 | +0.32 / +0.72 | both halves | 1e-04 | ⚠ same locus (1.9 kb, same strand: neighbours can correlate without regulation) |
| [[GATAD2B]] | +0.62 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[MXD4]] | +0.60 | +0.32 / +0.70 | both halves | 2e-04 |  |
| [[ULK1]] | +0.59 | +0.28 / +0.70 | both halves | 3e-04 |  |
| [[CSNK1G2]] | +0.59 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[CASTOR2]] | +0.58 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[SLC25A29]] | +0.58 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[WDTC1]] | +0.57 | +0.41 / +0.60 | both halves | 4e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GDAP1]] | -0.52 | -0.26 / -0.61 | both halves | 4e-04 |  |
| [[KICS2]] | -0.51 | -0.23 / -0.61 | both halves | 5e-04 |  |
| [[N6AMT1]] | -0.50 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[PYDC2-AS1]] | -0.49 | -0.24 / -0.51 | both halves | 5e-04 |  |
| [[DDX39B]] | -0.49 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[NBN]] | -0.48 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[GTF2H3]] | -0.47 | -0.29 / -0.56 | both halves | 2e-04 |  |
| [[HUS1]] | -0.47 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[NCR3LG1]] | -0.47 | -0.16 / -0.52 | ⚠ one half (not replicated) | 0.001 |  |
| [[PRRC2A]] | -0.47 | -0.24 / -0.57 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STEAP1]] | B | STEAP1 activity lowers HAGH's level | lines that do not express STEAP1 (11) vs lines expressing it (39) | 1.26× higher at baseline in the lines without STEAP1 | 0.071 | ⚠ within organs, on part of the lines; also absent: STEAP2-AS1, STEAP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.777). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.7, -43.1); signed map (-18.7, 12.4). **Vector** length 88.3, 20.3% of its response variance represented; |z| ≥ 3 in 955 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +3.8 | +5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +0.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.9 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | -0.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.5 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +1.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.3 | +1.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.1 | +2.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.1 | -12.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.0 | -7.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.4 | -5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -1.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | -4.1 | -3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.1 | -3.9 |
|  | [[EX229 (drug)]] 5 µM |  | -3.9 | -4.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.7 | -4.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.7 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | hydroxyacylglutathione hydrolase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:1,795,620-1,827,157 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GLO2, GLXII, HAGH1 |
| Gene groups (HGNC) | MBL domain containing glyoxalase 2 subfamily; Thioester hydrolases |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 2 pathways, smallest: Pyruvate metabolism; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16775](https://www.uniprot.org/uniprotkb/Q16775) (Hydroxyacylglutathione hydrolase, mitochondrial):

> Thiolesterase that catalyzes the hydrolysis of S-D-lactoyl-glutathione to form glutathione and D-lactic acid.

**Summary**, from NCBI Gene [3029](https://www.ncbi.nlm.nih.gov/gene/3029):

> The enzyme encoded by this gene is classified as a thiolesterase and is responsible for the hydrolysis of S-lactoyl-glutathione to reduced glutathione and D-lactate. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2013]

**Accessions** — [HGNC:4805](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4805) · Entrez [3029](https://www.ncbi.nlm.nih.gov/gene/3029) · UniProt [Q16775](https://www.uniprot.org/uniprotkb/Q16775) · Ensembl [ENSG00000063854](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000063854)

## Data

Gene col 733: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 733); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 733, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 733]; `tensor/DDL_lfc|DDL_z.npy` [733]; `embed/gene_vectors.npy` [733]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 733 or target_col == 733). Every well: [[HAGH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HAGH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
