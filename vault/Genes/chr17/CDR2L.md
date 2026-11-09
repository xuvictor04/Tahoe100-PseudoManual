---
symbol: "CDR2L"
type: "gene"
col: 3026
ensembl_id: "ENSG00000109089"
name: "cerebellar degeneration related protein 2 like"
location: "17q25.1"
module: 2
arm: "+"
pooled_cpm: 12.58
n_lines_expressing: 46
n_dd_up: 28
n_dd_down: 11
n_dd_up_clean: 16
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CDR2L

*cerebellar degeneration related protein 2 like* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.07× (z +14.9, q 0e+00, up in 30 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.457× (z -11.0, q 1e-25, down in 30 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM184B]] (+0.68, fdr 1e-05), [[TPST2]] (+0.65, fdr 1e-05), [[MYO9B]] (+0.64, fdr 1e-05); moves opposite to [[CASC9]] (-0.63, fdr 1e-05), [[DLEU1]] (-0.61, fdr 1e-05), [[RGS5]] (-0.60, fdr 2e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[KCNC4]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[AZD-7648 (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3026.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +14.9 | 0e+00 | 30/39 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.93×** | +9.5 | 4e-19 | 28/44 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.90×** | +9.3 | 3e-18 | 22/33 (SHP-77, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.83×** | +8.8 | 2e-16 | 28/43 (SW480, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.82×** | +8.7 | 3e-16 | 30/41 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.74×** | +8.1 | 7e-14 | 29/44 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.64×** | +6.9 | 5e-10 | 14/23 (KATO III, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +6.2 | 5e-08 | 22/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.43×** | +5.2 | 1e-05 | 16/42 (NCI-H460, A498, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +4.6 | 2e-04 | 13/42 (HEC-1-A, NCI-H460, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.92×** | +4.5 | 3e-04 | 4/41 (NCI-H460, A549, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +4.5 | 3e-04 | 16/44 (HT-29, SW1417, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.36×** | +4.3 | 8e-04 | 17/41 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.32×** | +4.0 | 0.002 | 14/41 (A-172, HOP62, …) | rises with dose | low cells (technical?) |
| [[Peretinoin (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.004 | 14/41 (NCI-H1792, A498, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.30×** | +3.7 | 0.007 | 13/43 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +3.3 | 0.024 | 10/44 (SHP-77, HepG2/C3A, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.024 | 5/44 (NCI-H2347, PANC-1, …) | all doses, flat |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.031 | 8/40 (SHP-77, RPMI-7951, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.26×** | +3.0 | 0.054 | 5/40 (A-427, RKO, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.061 | 11/41 (SW 900, MIA PaCa-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3026.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.457×** | -11.0 | 1e-25 | 30/43 (A-172, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.637×** | -9.4 | 2e-18 | 29/43 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.580×** | -8.0 | 3e-13 | 28/44 (hTERT-HPNE, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.591×** | -6.7 | 3e-09 | 22/40 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.645×** | -6.4 | 1e-08 | 23/42 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.663×** | -6.0 | 1e-07 | 22/42 (A-172, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.317×** | -5.7 | 8e-07 | 21/43 (A498, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.702×** | -5.2 | 1e-05 | 19/44 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.726×** | -4.7 | 2e-04 | 19/42 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.744×** | -4.2 | 0.002 | 16/40 (NCI-H1573, SNU-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.444×** | -4.1 | 0.002 | 16/39 (HS-578T, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3026. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 29.9 | 1 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -20.4) |
| [[SW480 (line)]] | alt | 8.86 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.10× (z +13.7) | — |
| [[hTERT-HPNE (line)]] | wt | 33.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0879× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.287× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 9.93 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.78× (z +15.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.174× (z -10.6) |
| [[A498 (line)]] | wt | 32.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +14.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.236× (z -11.6) |
| [[HOP62 (line)]] | alt | 16.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -10.5) |
| [[HS-578T (line)]] | alt | 21.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -10.8) |
| [[A-427 (line)]] | wt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.199× (z -8.8) |
| [[A549 (line)]] | wt | 14.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.80× (z +16.4) | — |
| [[C-33 A (line)]] | alt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0724× (z -8.7) |
| [[HCT15 (line)]] | alt | 10.5 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0901× (z -8.6) |
| [[J82 (line)]] | alt | 20.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -13.3) |
| [[KATO III (line)]] | alt | 33.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.77× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2030 (line)]] | alt | 7.58 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.120× (z -10.0) |
| [[RKO (line)]] | wt | 12.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.36× (z +11.5) | — |
| [[SNU-423 (line)]] | alt | 6.57 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -11.5) |
| [[SW48 (line)]] | wt | 11.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM 0.0776× (z -8.7) |
| [[AN3 CA (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3026), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM184B]] | +0.68 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[TPST2]] | +0.65 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[MYO9B]] | +0.64 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[ZFYVE21]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[SLC39A13]] | +0.61 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[SS18L1]] | +0.61 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[TSPAN17]] | +0.60 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[TESK1]] | +0.60 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[ZMYND19]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[LDLRAP1]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[SLC27A4]] | +0.59 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[SPRYD3]] | +0.58 | +0.54 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASC9]] | -0.63 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[DLEU1]] | -0.61 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[RGS5]] | -0.60 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[CRADD]] | -0.60 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[USP40]] | -0.58 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[LEKR1]] | -0.57 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[ATXN7L1]] | -0.56 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[NFYC]] | -0.56 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[CHIC1]] | -0.55 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[SLX4IP]] | -0.54 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[KCNMB2-AS1]] | -0.54 | -0.58 / -0.36 | both halves | 9e-05 |  |
| [[ZNF608]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNC4]] | B | KCNC4 activity raises CDR2L's level | lines that do not express KCNC4 (6) vs lines expressing it (44) | 1.50× lower at baseline in the lines without KCNC4 | 0.035 | ⚠ within organs, on part of the lines; also absent: CRTAP, FKBP7, SACS; maybe low, not absent |
| [[ZCCHC24]] | B | ZCCHC24 activity raises CDR2L's level | lines that do not express ZCCHC24 (5) vs lines expressing it (45) | 2.00× lower at baseline in the lines without ZCCHC24 | 0.059 | ⚠ within organs, on part of the lines; also absent: CNTNAP1, KIF17, SLC29A4; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[AZD-7648 (drug)]] 5 µM | C | CDR2L activity raises the cells' numbers under AZD-7648 5 µM (protects the cells) | lines that do not express CDR2L (4) vs lines expressing it (44) | the lines without CDR2L: 0.68× the cells of the other lines | 0.039 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: MTARC2, LRP5, HACD1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.658). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (2.5, 3.0); signed map (-44.1, -4.1). **Vector** length 80.8, 17.3% of its response variance represented; |z| ≥ 3 in 830 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +14.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +4.2 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +9.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.7 | +8.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.5 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.2 | +3.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.1 | +4.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.9 | +4.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.8 | +3.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.1 | -11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.6 | -9.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | -6.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.2 | -5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -1.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.8 | -0.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.8 | -1.1 |
|  | [[Encorafenib (drug)]] 5 µM |  | -1.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | cerebellar degeneration related protein 2 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:74,987,632-75,005,800 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HUMPPA |
| Matched by | ensembl_id |

UniProt [Q86X02](https://www.uniprot.org/uniprotkb/Q86X02) carries no function annotation.

**Summary**, from NCBI Gene [30850](https://www.ncbi.nlm.nih.gov/gene/30850):

> Enables identical protein binding activity. Predicted to be involved in Golgi to secretory granule transport and vesicle transport along microtubule. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29999](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29999) · Entrez [30850](https://www.ncbi.nlm.nih.gov/gene/30850) · UniProt [Q86X02](https://www.uniprot.org/uniprotkb/Q86X02) · Ensembl [ENSG00000109089](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109089)

## Data

Gene col 3026: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3026); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3026, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3026]; `tensor/DDL_lfc|DDL_z.npy` [3026]; `embed/gene_vectors.npy` [3026]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3026 or target_col == 3026). Every well: [[CDR2L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDR2L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
