---
symbol: "PEX13"
type: "gene"
col: 8601
ensembl_id: "ENSG00000162928"
name: "peroxisomal biogenesis factor 13"
location: "2p15"
module: 41
arm: "+"
pooled_cpm: 53.78
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# PEX13

*peroxisomal biogenesis factor 13* — 2p15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 3.34× (z +14.5, q 7e-45, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.568× (z -13.0, q 5e-36, down in 35 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.733× (z -6.9, q 1e-09, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTI2]] (+0.65, fdr 1e-05), [[KLHL28]] (+0.65, fdr 7e-06), [[ZNF230]] (+0.63, fdr 7e-06); moves opposite to [[DOCK1]] (-0.59, fdr 1e-05), [[HLCS]] (-0.59, fdr 1e-05), [[CCT5]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8601.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.34×** | +14.5 | 7e-45 | 43/49 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +6.7 | 5e-09 | 24/48 (SK-MEL-2, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.29×** | +5.8 | 2e-06 | 25/48 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +5.7 | 2e-06 | 22/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.26×** | +5.3 | 1e-05 | 24/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.24×** | +5.0 | 5e-05 | 22/48 (BT-474, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.24×** | +5.0 | 6e-05 | 21/48 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.6 | 4e-04 | 19/49 (PANC-1, SW1417, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.21×** | +4.3 | 1e-03 | 21/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.10× | +3.1 | 0.11 | 6/48 (HT-29, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8601.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.568×** | -13.0 | 5e-36 | 35/49 (A-427, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.600×** | -11.3 | 4e-27 | 30/40 (NCI-H1573, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.733×** | -6.9 | 1e-09 | 33/48 (NCI-H1573, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.730×** | -6.7 | 3e-09 | 31/43 (CFPAC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.770×** | -5.8 | 8e-07 | 25/47 (A-427, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.811×** | -4.8 | 1e-04 | 20/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.811×** | -4.7 | 3e-04 | 22/47 (NCI-H460, A549, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.825×** | -4.4 | 7e-04 | 19/48 (HT-29, NCI-H1573, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **0.827×** | -4.4 | 7e-04 | 18/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.828×** | -4.4 | 8e-04 | 22/48 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.829×** | -4.3 | 8e-04 | 17/48 (NCI-H1792, C32, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.840× | -4.0 | 0.003 | 15/47 (CFPAC-1, SW 1271, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.787×** | -3.9 | 0.004 | 20/48 (SW 900, HOP62, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.897× | -3.5 | 0.022 | 8/48 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.899× | -3.4 | 0.029 | 13/48 (SW480, LS 180, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.871× | -3.2 | 0.049 | 14/47 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.872× | -3.2 | 0.051 | 13/48 (NCI-H1573, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8601. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 79.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -18.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 56.8 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.29× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 77.6 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0837× (z -25.2) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.383× (z -9.8) |
| [[HOP62 (line)]] | alt | 58.4 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -11.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 61.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.39× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 57.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.319× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 60.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -15.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 60.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.567× (z -8.6) |
| [[PANC-1 (line)]] | alt | 44.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.78× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 72.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -10.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 50.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.38× (z +10.9) | — |
| [[A549 (line)]] | wt | 54.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -10.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 79.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.544× (z -9.3) |
| [[HCT15 (line)]] | alt | 68.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0887× (z -17.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 77.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 49.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.75× (z +8.5) | — |
| [[LoVo (line)]] | wt | 31.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.13× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 47.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.60× (z +10.4) | — |
| [[NCI-H1792 (line)]] | alt | 118 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.22× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 43.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.450× (z -10.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 52.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -14.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 37.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.8) | — |
| [[SW 1271 (line)]] | alt | 63.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 55.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 69.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8601), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTI2]] | +0.65 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[KLHL28]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ZNF230]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[MMUT]] | +0.62 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[ERCC5]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[RSPRY1]] | +0.60 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[YY1AP1]] | +0.59 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[APPBP2]] | +0.59 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[CIR1]] | +0.58 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[ZSWIM8]] | +0.58 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[BCKDHA]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[TTC9C]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOCK1]] | -0.59 | -0.59 / -0.52 | both halves | 1e-05 | same gene group |
| [[HLCS]] | -0.59 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[CCT5]] | -0.57 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[SLFNL1-AS1]] | -0.55 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[SACS]] | -0.55 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[HERC2P9-1]] | -0.55 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[GALNT10]] | -0.54 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[ASAP1]] | -0.54 | -0.42 / -0.61 | both halves | 4e-05 | same gene group |
| [[TBILA]] | -0.54 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[CHCHD3]] | -0.53 | -0.51 / -0.53 | both halves | 1e-05 | pathway: Protein localization |
| [[UGGT2]] | -0.53 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[IPO7]] | -0.53 | -0.51 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers PEX13's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.620). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (4.6, -34.9); signed map (-12.6, 3.0). **Vector** length 90.5, 19.6% of its response variance represented; |z| ≥ 3 in 898 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.2 | +14.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.3 | +4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +5.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +1.8 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | +2.1 | +1.6 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +2.1 | +1.6 |
|  | [[Entrectinib (drug)]] 0.5 µM |  | +1.6 | +2.0 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | +1.5 | +2.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.7 | -5.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.5 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | -4.4 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | -4.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.2 | -4.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.1 | -4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | peroxisomal biogenesis factor 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p15 — chr2:61,017,225-61,051,990 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Peroxins; SH3 domain containing |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME |
| Reactome | 5 pathways, smallest: Class I peroxisomal membrane protein import; E3 ubiquitin ligases ubiquitinate target proteins; Peroxisomal protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92968](https://www.uniprot.org/uniprotkb/Q92968) (Peroxisomal membrane protein PEX13):

> Component of the PEX13-PEX14 docking complex, a translocon channel that specifically mediates the import of peroxisomal cargo proteins bound to PEX5 receptor. The PEX13-PEX14 docking complex forms a large import pore which can be opened to a diameter of about 9 nm (By similarity). Mechanistically, PEX5 receptor along with cargo proteins associates with the PEX14 subunit of the PEX13-PEX14 docking complex in the cytosol, leading to the insertion of the receptor into the organelle membrane with …

**Summary**, from NCBI Gene [5194](https://www.ncbi.nlm.nih.gov/gene/5194):

> This gene encodes a peroxisomal membrane protein that binds the type 1 peroxisomal targeting signal receptor via a SH3 domain located in the cytoplasm. Mutations and deficiencies in peroxisomal protein importing and peroxisome assembly lead to peroxisomal biogenesis disorders, an example of which is Zellweger syndrome. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:8855](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8855) · Entrez [5194](https://www.ncbi.nlm.nih.gov/gene/5194) · UniProt [Q92968](https://www.uniprot.org/uniprotkb/Q92968) · Ensembl [ENSG00000162928](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162928)

## Data

Gene col 8601: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8601); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8601, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8601]; `tensor/DDL_lfc|DDL_z.npy` [8601]; `embed/gene_vectors.npy` [8601]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8601 or target_col == 8601). Every well: [[PEX13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEX13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
