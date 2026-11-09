---
symbol: "SLC4A8"
type: "gene"
col: 567
ensembl_id: "ENSG00000050438"
name: "solute carrier family 4 member 8"
location: "12q13.13"
module: 115
arm: "+"
pooled_cpm: 11.76
n_lines_expressing: 39
n_dd_up: 23
n_dd_down: 17
n_dd_up_clean: 20
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 5
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# SLC4A8

*solute carrier family 4 member 8* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 4.77× (z +23.8, q 0e+00, up in 32 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.496× (z -10.7, q 8e-24, down in 22 of 36 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APBA1]] (+0.59, fdr 5e-05), [[ACBD7]] (+0.57, fdr 2e-05), [[CACNA1A]] (+0.54, fdr 5e-05); moves opposite to [[LINC00278]] (-0.44, fdr 2e-04), [[ZNF736P9Y]] (-0.42, fdr 2e-04), [[POLR1F]] (-0.40, fdr 7e-04).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 5 go from it, the strongest it → [[SCN8A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 567.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **4.77×** | +23.8 | 0e+00 | 32/36 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.50×** | +22.9 | 0e+00 | 31/36 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.60×** | +20.6 | 0e+00 | 30/37 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +18.3 | 0e+00 | 24/35 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.24×** | +17.9 | 0e+00 | 30/36 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.17×** | +17.6 | 0e+00 | 27/35 (LoVo, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.82×** | +15.8 | 0e+00 | 30/36 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.54×** | +14.2 | 7e-44 | 30/36 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.38×** | +9.7 | 2e-20 | 25/37 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +7.5 | 5e-12 | 17/33 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +6.6 | 2e-09 | 10/27 (MIA PaCa-2, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **2.08×** | +5.8 | 2e-07 | 13/36 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +5.7 | 4e-07 | 4/17 (J82, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.8 | 5e-05 | 9/37 (SW480, Panc 03.27, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.19× | +3.8 | 0.006 | 7/36 (SHP-77, CFPAC-1, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.29×** | +3.7 | 0.008 | 8/35 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.013 | 6/35 (SHP-77, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 567.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.496×** | -10.7 | 8e-24 | 22/36 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.520×** | -10.0 | 6e-21 | 24/36 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.581×** | -8.3 | 3e-14 | 21/36 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.588×** | -8.1 | 1e-13 | 24/34 (PANC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.634×** | -6.9 | 5e-10 | 18/36 (PANC-1, RKO, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.626×** | -6.9 | 7e-10 | 21/36 (H4, A-427, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.651×** | -6.5 | 5e-09 | 16/36 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.545×** | -4.8 | 9e-05 | 10/33 (RKO, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.755×** | -4.3 | 0.001 | 17/36 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.757×** | -4.2 | 0.001 | 13/36 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.746×** | -4.2 | 0.001 | 17/35 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.752×** | -4.2 | 0.001 | 12/35 (A-427, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.759×** | -4.0 | 0.003 | 15/36 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.613×** | -3.9 | 0.004 | 13/36 (NCI-H23, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.793×** | -3.4 | 0.027 | 12/35 (Panc 03.27, HOP62, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **0.806×** | -3.2 | 0.056 | 6/35 (SW 1271, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 567. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 53.0 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0843× (z -20.6) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.366× (z -11.9) |
| [[PANC-1 (line)]] | alt | 16.9 | 5 | 4 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.97× (z +11.1) | [[Digitoxin (drug)]] 5 µM 0.216× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.262× (z -9.4) |
| [[SW480 (line)]] | alt | 18.4 | 7 | 2 | [[Panobinostat (drug)]] 0.5 µM 6.24× (z +13.3) | [[Ixazomib citrate (drug)]] 5 µM 0.275× (z -9.3) |
| [[RKO (line)]] | wt | 74.5 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -13.0) |
| [[A549 (line)]] | wt | 3.30 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 8.67× (z +9.0) | — |
| [[J82 (line)]] | alt | 5.32 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 12.0× (z +9.5) | — |
| [[H4 (line)]] | wt | 16.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.103× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 8.64 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0890× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Cepharanthine (drug)]] 0.5 µM 0.0927× (z -8.8) |
| [[LoVo (line)]] | wt | 8.98 | 2 | 0 | [[Auranofin (drug)]] 5 µM 14.1× (z +14.2) | — |
| [[LOX-IMVI (line)]] | wt | 17.1 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.168× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 20.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 25.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -13.2) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0791× (z -8.9) |
| [[A-172 (line)]] | wt | 8.37 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.27× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 31.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 8.73 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.69× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 3.30 | 1 | 0 | [[Auranofin (drug)]] 5 µM 12.0× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.55 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.103× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 6.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.69× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 59.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -13.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 7.20 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0818× (z -8.9) |
| [[A498 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.52 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 567), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APBA1]] | +0.59 | +0.40 / +0.66 | both halves | 5e-05 |  |
| [[ACBD7]] | +0.57 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[CACNA1A]] | +0.54 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[VAT1L]] | +0.54 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[STARD8]] | +0.52 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[SPTB]] | +0.51 | +0.36 / +0.56 | both halves | 9e-05 |  |
| [[SLC7A8]] | +0.49 | +0.43 / +0.58 | both halves | 3e-05 | pathway: SLC-mediated transmembrane transport |
| [[LRRC36]] | +0.49 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[PDE4DIP]] | +0.49 | +0.35 / +0.46 | both halves | 1e-04 |  |
| [[OTUD7A]] | +0.48 | +0.25 / +0.60 | both halves | 4e-04 |  |
| [[CTNNA2]] | +0.48 | +0.37 / +0.43 | both halves | 7e-05 |  |
| [[SUSD4]] | +0.48 | +0.38 / +0.56 | both halves | 7e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00278]] | -0.44 | -0.31 / -0.32 | both halves | 2e-04 |  |
| [[ZNF736P9Y]] | -0.42 | -0.32 / -0.33 | both halves | 2e-04 |  |
| [[POLR1F]] | -0.40 | -0.20 / -0.37 | both halves | 7e-04 |  |
| [[NFX1]] | -0.39 | -0.27 / -0.36 | both halves | 3e-04 |  |
| [[FASTKD2]] | -0.39 | -0.19 / -0.43 | ⚠ not reproduced | 8e-04 |  |
| [[FAM185A]] | -0.39 | -0.21 / -0.33 | both halves | 7e-04 |  |
| [[CDK12]] | -0.39 | -0.14 / -0.48 | ⚠ not reproduced | 0.002 |  |
| [[PALB2]] | -0.39 | -0.23 / -0.42 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCN8A]] | B | SLC4A8 activity raises SCN8A's level | lines that do not express SLC4A8 (11) vs lines expressing it (39) | 3.61× lower at baseline in the lines without SLC4A8 | 0.019 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[SGSM1]] | B | SLC4A8 activity raises SGSM1's level | lines that do not express SLC4A8 (11) vs lines expressing it (39) | 1.68× lower at baseline in the lines without SLC4A8 | 0.040 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[SLAIN1]] | B | SLC4A8 activity raises SLAIN1's level | lines that do not express SLC4A8 (11) vs lines expressing it (39) | 2.38× lower at baseline in the lines without SLC4A8 | 0.058 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[FAM185A]] | B | SLC4A8 activity raises FAM185A's level | lines that do not express SLC4A8 (11) vs lines expressing it (39) | 1.30× lower at baseline in the lines without SLC4A8 | 0.074 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[CDK12]] | B | SLC4A8 activity raises CDK12's level | lines that do not express SLC4A8 (11) vs lines expressing it (39) | 1.31× lower at baseline in the lines without SLC4A8 | 0.078 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.407). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (58.0, 11.9); signed map (31.9, 27.3). **Vector** length 78.9, 15.2% of its response variance represented; |z| ≥ 3 in 1,155 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +20.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.0 | +17.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +14.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +6.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +9.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +2.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -0.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.3 | -4.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.8 | -10.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -8.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.4 | -3.4 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | -1.2 | -1.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.2 | -0.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 4 member 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:51,391,317-51,515,763 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NBC3 |
| Gene groups (HGNC) | Solute carrier family 4 |
| Reactome | 4 pathways, smallest: Bicarbonate transporters; SLC-mediated transport of inorganic anions; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2Y0W8](https://www.uniprot.org/uniprotkb/Q2Y0W8) (Electroneutral sodium bicarbonate exchanger 1):

> Mediates electroneutral sodium- and carbonate-dependent chloride-HCO3(-) exchange with a Na(+):HCO3(-) stoichiometry of 2:1. Plays a major role in pH regulation in neurons (By similarity). Mediates sodium reabsorption in the renal cortical collecting ducts (By similarity).

**Summary**, from NCBI Gene [9498](https://www.ncbi.nlm.nih.gov/gene/9498):

> The protein encoded by this gene is a membrane protein that functions to transport sodium and bicarbonate ions across the cell membrane. The encoded protein is important for pH regulation in neurons. The activity of this protein can be inhibited by 4,4'-Di-isothiocyanatostilbene-2,2'-disulfonic acid (DIDS). Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012]

**Accessions** — [HGNC:11034](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11034) · Entrez [9498](https://www.ncbi.nlm.nih.gov/gene/9498) · UniProt [Q2Y0W8](https://www.uniprot.org/uniprotkb/Q2Y0W8) · Ensembl [ENSG00000050438](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000050438)

## Data

Gene col 567: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 567); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 567, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 567]; `tensor/DDL_lfc|DDL_z.npy` [567]; `embed/gene_vectors.npy` [567]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 567 or target_col == 567). Every well: [[SLC4A8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC4A8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
