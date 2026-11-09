---
symbol: "MIR3659HG"
type: "gene"
col: 13406
ensembl_id: "ENSG00000224592"
name: "MIR3659 host gene"
location: "1p34.3"
module: 62
arm: "+"
pooled_cpm: 3.45
n_lines_expressing: 45
n_dd_up: 32
n_dd_down: 11
n_dd_up_clean: 24
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# MIR3659HG

*MIR3659 host gene* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.70× (z +21.0, q 0e+00, up in 27 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Gallic acid (hydrate) (drug)]] 0.05 µM: 0.561× (z -4.9, q 4e-04, down in 13 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF423]] (+0.66, fdr 1e-05), [[INKA2]] (+0.65, fdr 1e-05), [[GRIN2C]] (+0.61, fdr 1e-05); moves opposite to [[YTHDC2]] (-0.50, fdr 7e-05), [[NEK1]] (-0.49, fdr 1e-04), [[DCLRE1A]] (-0.47, fdr 1e-04).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[EDA2R]] → it (grade B ⚠); 4 go from it, the strongest it → [[SEPTIN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13406.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.70×** | +21.0 | 0e+00 | 27/27 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **5.83×** | +15.0 | 0e+00 | 24/33 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **5.80×** | +14.4 | 8e-45 | 20/26 (NCI-H460, A498, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **5.38×** | +14.4 | 1e-44 | 38/40 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.10×** | +13.9 | 7e-42 | 37/38 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.02×** | +13.3 | 2e-38 | 24/28 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **16.8×** | +12.6 | 2e-34 | 32/32 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.97×** | +11.3 | 8e-28 | 20/30 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.50×** | +10.7 | 8e-25 | 30/40 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **9.47×** | +10.0 | 7e-22 | 21/25 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.22×** | +9.6 | 4e-20 | 17/39 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.59×** | +7.8 | 3e-13 | 6/14 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.40×** | +7.5 | 4e-12 | 10/24 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.28×** | +7.0 | 9e-11 | 17/40 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.28×** | +7.0 | 9e-11 | 17/36 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.11×** | +6.4 | 7e-09 | 21/41 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.10×** | +6.3 | 9e-09 | 15/35 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13406.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.561×** | -4.9 | 4e-04 | 13/39 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.710×** | -4.1 | 0.010 | 11/40 (NCI-H2030, SHP-77, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.628×** | -4.0 | 0.013 | 15/39 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.648×** | -3.7 | 0.029 | 8/39 (NCI-H2030, A-172, …) | inconsistent across doses | position effect removed |
| [[Thymol (drug)]] 5 µM |  | **0.749×** | -3.5 | 0.048 | 12/38 (HS-578T, HCT15, …) | top dose only | position effect removed |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.666×** | -3.5 | 0.048 | 10/39 (NCI-H1792, SHP-77, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.671×** | -3.4 | 0.051 | 7/39 (HEC-1-A, A498, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.684×** | -3.3 | 0.074 | 5/39 (SK-MEL-2, Hs 766T, …) | top dose only |  |
| [[Erlotinib (drug)]] 5 µM |  | **0.674×** | -3.2 | 0.074 | 9/31 (NCI-H23, Panc 03.27, …) | top dose only | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.689×** | -3.2 | 0.078 | 4/41 (SW48, C-33 A, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.690×** | -3.2 | 0.078 | 6/40 (SHP-77, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13406. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 13.0 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.44× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.0186× (z -20.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 2.39 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.6× (z +13.3) | — |
| [[HepG2_C3A (line)]] | wt | 2.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.6× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 5.38 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0671× (z -9.1) |
| [[LoVo (line)]] | wt | 10.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.49× (z +12.5) | — |
| [[PANC-1 (line)]] | alt | 3.19 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0898× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 2.92 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.14× (z +8.5) | — |
| [[A-172 (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.688 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.783 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.865 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.736 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.953 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.970 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.829 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.889 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13406), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF423]] | +0.66 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[INKA2]] | +0.65 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[GRIN2C]] | +0.61 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[SPATA18]] | +0.60 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[ADGRA2]] | +0.58 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[ZMAT3]] | +0.57 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[ADAMTS7]] | +0.57 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[CD247]] | +0.56 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[DNAI3]] | +0.56 | +0.37 / +0.67 | both halves | 7e-05 |  |
| [[PINCR]] | +0.56 | +0.39 / +0.62 | both halves | 5e-05 |  |
| [[FDXR]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[LGI4]] | +0.55 | +0.37 / +0.57 | both halves | 9e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YTHDC2]] | -0.50 | -0.37 / -0.44 | both halves | 7e-05 |  |
| [[NEK1]] | -0.49 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[DCLRE1A]] | -0.47 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[FKTN]] | -0.47 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[MRPS10]] | -0.47 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[PTCD2]] | -0.46 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[DNM1L]] | -0.45 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[ASF1A]] | -0.44 | -0.29 / -0.42 | both halves | 2e-04 |  |
| [[CEP162]] | -0.44 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[APOOL]] | -0.44 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[TRIM16L-1]] | -0.44 | -0.34 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EDA2R]] | B | EDA2R activity raises MIR3659HG's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.34× lower at baseline in the lines without EDA2R | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[ADAMTS7]] | B | ADAMTS7 activity raises MIR3659HG's level | lines that do not express ADAMTS7 (17) vs lines expressing it (33) | 1.57× lower at baseline in the lines without ADAMTS7 | 0.031 | ⚠ within organs, on part of the lines; also absent: VASH1, FHL1, ANTXR1; maybe low, not absent |
| [[PURPL]] | B | PURPL activity raises MIR3659HG's level | lines that do not express PURPL (25) vs lines expressing it (25) | 1.51× lower at baseline in the lines without PURPL | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MIR99AHG, ENSG00000286385, RPS4Y1 |
| [[TOP2A]] | B | TOP2A activity lowers MIR3659HG's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEPTIN1]] | B | MIR3659HG activity raises SEPTIN1's level | lines that do not express MIR3659HG (5) vs lines expressing it (45) | 1.48× lower at baseline in the lines without MIR3659HG | 0.033 | ⚠ within organs, on part of the lines; also absent: USP31, ZNF594, WHRN; maybe low, not absent |
| [[DNM1L]] | B | MIR3659HG activity raises DNM1L's level | lines that do not express MIR3659HG (5) vs lines expressing it (45) | 1.70× lower at baseline in the lines without MIR3659HG | 0.036 | ⚠ within organs, on part of the lines; also absent: USP31, ZNF594, WHRN; maybe low, not absent |
| [[ADAMTS7]] | B | MIR3659HG activity raises ADAMTS7's level | lines that do not express MIR3659HG (5) vs lines expressing it (45) | 2.30× lower at baseline in the lines without MIR3659HG | 0.094 | ⚠ within organs, on part of the lines; also absent: USP31, ZNF594, WHRN; maybe low, not absent |
| cells under [[Pravastatin (sodium) (drug)]] 5 µM | B | MIR3659HG activity raises the cells' numbers under Pravastatin (sodium) 5 µM (protects the cells) | lines that do not express MIR3659HG (5) vs lines expressing it (43) | the lines without MIR3659HG: 0.82× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: USP31, ZNF594, WHRN; maybe low, not absent |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.606). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.3, 37.2); signed map (44.0, -23.6). **Vector** length 67.7, 12.0% of its response variance represented; |z| ≥ 3 in 1,215 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +21.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +4.9 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +15.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | +4.2 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +9.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +10.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +0.9 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -2.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -0.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.1 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.4 | -2.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | MIR3659 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p34.3 — chr1:38,047,314-38,119,025 (+) |
| Ensembl biotype | lncRNA |
| Also known as | uc.15 |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54306](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54306) · Entrez [105378653](https://www.ncbi.nlm.nih.gov/gene/105378653) · Ensembl [ENSG00000224592](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224592)

## Data

Gene col 13406: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13406); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13406, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13406]; `tensor/DDL_lfc|DDL_z.npy` [13406]; `embed/gene_vectors.npy` [13406]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13406 or target_col == 13406). Every well: [[MIR3659HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR3659HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
