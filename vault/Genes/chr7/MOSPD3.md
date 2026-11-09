---
symbol: "MOSPD3"
type: "gene"
col: 2744
ensembl_id: "ENSG00000106330"
name: "motile sperm domain containing 3"
location: "7q22.1"
module: 76
arm: "+"
pooled_cpm: 6.75
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 17
n_dd_up_clean: 6
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# MOSPD3

*motile sperm domain containing 3* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.08× (z +7.4, q 8e-11, up in 20 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.44× (z +5.3, q 3e-05, up in 21 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.309× (z -16.7, q 0e+00, down in 39 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GMCL1]] (+0.80, fdr 7e-06), [[IGSF8]] (+0.78, fdr 7e-06), [[CBFA2T2]] (+0.76, fdr 7e-06); moves opposite to [[ST7L]] (-0.83, fdr 7e-06), [[GPATCH4]] (-0.75, fdr 7e-06), [[DNAJC11]] (-0.73, fdr 7e-06).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF649]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2744.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.08×** | +7.4 | 8e-11 | 20/30 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +5.9 | 8e-07 | 6/14 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +5.3 | 3e-05 | 21/47 (A498, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +4.9 | 2e-04 | 24/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +4.8 | 2e-04 | 17/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +4.2 | 0.003 | 8/19 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.009 | 15/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.012 | 18/43 (A498, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.82×** | +3.3 | 0.072 | 8/42 (A498, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.37×** | +3.2 | 0.081 | 9/37 (NCI-H2030, SHP-77, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2744.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.309×** | -16.7 | 0e+00 | 39/43 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.230×** | -14.8 | 0e+00 | 39/41 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.292×** | -11.9 | 2e-30 | 38/47 (SW 900, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.416×** | -8.8 | 1e-16 | 36/48 (SW 900, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.462×** | -7.8 | 9e-13 | 33/47 (SW 900, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.499×** | -7.0 | 3e-10 | 33/46 (SW 900, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.516×** | -6.6 | 2e-09 | 33/47 (MIA PaCa-2, PANC-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.549×** | -6.0 | 1e-07 | 24/44 (H4, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.574×** | -5.6 | 2e-06 | 23/42 (A549, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.575×** | -5.6 | 2e-06 | 22/46 (NCI-H2030, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.666×** | -4.1 | 0.002 | 22/46 (H4, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.490×** | -3.8 | 0.008 | 13/39 (HOP62, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.698×** | -3.6 | 0.013 | 13/47 (Panc 03.27, C-33 A, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[EX229 (drug)]] 5 µM |  | **0.536×** | -3.3 | 0.041 | 11/40 (Hs 766T, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.722×** | -3.3 | 0.041 | 9/47 (HT-29, H4, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.546×** | -3.2 | 0.052 | 13/45 (NCI-H1792, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ivermectin (drug)]] 5 µM |  | **0.743×** | -3.0 | 0.096 | 3/48 (J82, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2744. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 6.70 | 0 | 5 | — | [[Harringtonine (drug)]] 5 µM 0.0377× (z -12.0) |
| [[Hs 766T (line)]] | wt | 7.96 | 0 | 3 (1 ⚠) | — | [[Saquinavir (drug)]] 0.5 µM 0.0744× (z -10.4) |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0385× (z -16.0) |
| [[CFPAC-1 (line)]] | alt | 8.09 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -11.4) |
| [[HT-29 (line)]] | alt | 5.61 | 0 | 2 | — | [[Canagliflozin (drug)]] 5 µM 0.0642× (z -9.7) |
| [[LS 180 (line)]] | wt | 7.11 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0292× (z -14.9) |
| [[NCI-H2347 (line)]] | alt | 7.29 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0469× (z -16.7) |
| [[Panc 03.27 (line)]] | alt | 6.32 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -11.4) |
| [[PANC-1 (line)]] | alt | 6.62 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.178× (z -9.9) |
| [[SW480 (line)]] | alt | 6.85 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -11.7) |
| [[A-172 (line)]] | wt | 9.75 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -12.7) |
| [[A498 (line)]] | wt | 7.92 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 5.64 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -10.0) |
| [[HOP62 (line)]] | alt | 7.86 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -14.2) |
| [[J82 (line)]] | alt | 5.33 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 7.43 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 8.19 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.118× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 7.72 | 0 | 1 | — | [[Ligustrazine (drug)]] 5 µM 0.0634× (z -9.1) |
| [[SNU-423 (line)]] | alt | 7.50 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -9.0) |
| [[A-427 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2744), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMCL1]] | +0.80 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[IGSF8]] | +0.78 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[CBFA2T2]] | +0.76 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[ARL3]] | +0.76 | +0.73 / +0.57 | both halves | 1e-05 |  |
| [[NTAN1]] | +0.75 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[SEZ6L2]] | +0.74 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[KLHL7]] | +0.74 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[GNB2]] | +0.72 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[ANG]] | +0.72 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[LMBR1L]] | +0.72 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[PLA2G15]] | +0.71 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[ADIPOR1]] | +0.71 | +0.67 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST7L]] | -0.83 | -0.80 / -0.73 | both halves | 7e-06 |  |
| [[GPATCH4]] | -0.75 | -0.80 / -0.64 | both halves | 7e-06 |  |
| [[DNAJC11]] | -0.73 | -0.73 / -0.60 | both halves | 7e-06 |  |
| [[POGLUT1]] | -0.73 | -0.73 / -0.61 | both halves | 7e-06 |  |
| [[CPSF2]] | -0.72 | -0.74 / -0.55 | both halves | 1e-05 |  |
| [[ANAPC7]] | -0.71 | -0.68 / -0.76 | both halves | 7e-06 |  |
| [[GCFC2]] | -0.70 | -0.71 / -0.58 | both halves | 8e-06 |  |
| [[ANKRD18A]] | -0.69 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[FKRP]] | -0.68 | -0.68 / -0.53 | both halves | 1e-05 |  |
| [[ZC3H7B]] | -0.68 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | -0.68 | -0.68 / -0.44 | both halves | 3e-05 |  |
| [[NEPRO-AS1]] | -0.67 | -0.66 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF649]] | B | ZNF649 activity raises MOSPD3's level | lines that do not express ZNF649 (13) vs lines expressing it (37) | 1.30× lower at baseline in the lines without ZNF649 | 0.006 | ⚠ within organs, on part of the lines; also absent: ZNF577, ZNF681, RPSAP58 |
| [[SNHG18]] | B | SNHG18 activity raises MOSPD3's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.32× lower at baseline in the lines without SNHG18 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |
| [[HDAC6]] | B | HDAC6 activity lowers MOSPD3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.774). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.4, -14.3); signed map (-34.8, 14.0). **Vector** length 71.2, 13.4% of its response variance represented; |z| ≥ 3 in 815 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.1 | +4.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.8 | +4.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.7 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +3.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.8 | +5.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +2.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.3 | +3.3 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.2 | +1.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.1 | +0.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.9 | -14.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.1 | -7.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.5 | -11.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.9 | -16.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | motile sperm domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,612,102-100,615,384 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CDS3, NET30 |
| Gene groups (HGNC) | Motile sperm domain containing |
| Matched by | ensembl_id |

UniProt [O75425](https://www.uniprot.org/uniprotkb/O75425) carries no function annotation.

**Summary**, from NCBI Gene [64598](https://www.ncbi.nlm.nih.gov/gene/64598):

> This gene encodes a multi-pass membrane protein with a major sperm protein (MSP) domain. The deletion of a similar mouse gene is associated with defective cardiac development and neonatal lethality. Alternate transcriptional splice variants, encoding different isoforms, have been described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:25078](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25078) · Entrez [64598](https://www.ncbi.nlm.nih.gov/gene/64598) · UniProt [O75425](https://www.uniprot.org/uniprotkb/O75425) · Ensembl [ENSG00000106330](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106330)

## Data

Gene col 2744: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2744); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2744, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2744]; `tensor/DDL_lfc|DDL_z.npy` [2744]; `embed/gene_vectors.npy` [2744]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2744 or target_col == 2744). Every well: [[MOSPD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MOSPD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
