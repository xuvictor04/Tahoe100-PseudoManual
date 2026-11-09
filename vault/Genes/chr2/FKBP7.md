---
symbol: "FKBP7"
type: "gene"
col: 1242
ensembl_id: "ENSG00000079150"
name: "FKBP prolyl isomerase 7"
location: "2q31.2"
module: 45
arm: "+"
pooled_cpm: 2.58
n_lines_expressing: 43
n_dd_up: 22
n_dd_down: 10
n_dd_up_clean: 15
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 13
direction_downstream: 5
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# FKBP7

*FKBP prolyl isomerase 7* — 2q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.50× (z +15.4, q 0e+00, up in 14 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.35× (z +10.9, q 2e-25, up in 29 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[5-Azacytidine (drug)]] 5 µM: 0.536× (z -5.7, q 4e-06, down in 16 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTSF]] (+0.65, fdr 9e-06), [[HMGN3]] (+0.64, fdr 1e-05), [[SMIM10]] (+0.62, fdr 1e-05); moves opposite to [[BCL2L13]] (-0.50, fdr 9e-05), [[SLC66A1]] (-0.49, fdr 4e-05), [[MICALL1]] (-0.48, fdr 3e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[ENPP2]] → it (grade B ⚠); 5 go from it, the strongest it → [[GSTM4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1242.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.50×** | +15.4 | 0e+00 | 14/14 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.42×** | +14.7 | 0e+00 | 5/5 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.80×** | +13.1 | 8e-37 | 4/5 (A498, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.35×** | +10.9 | 2e-25 | 29/39 (A498, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.77×** | +9.2 | 6e-18 | 27/40 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.51×** | +8.3 | 1e-14 | 26/37 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.50×** | +8.2 | 1e-14 | 23/38 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.26×** | +7.3 | 2e-11 | 25/40 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.11×** | +6.7 | 1e-09 | 23/34 (SW1417, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +6.6 | 2e-09 | 13/26 (SNU-423, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.68×** | +6.6 | 3e-09 | 14/39 (A498, SW48, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +5.7 | 6e-07 | 4/14 (NCI-H2347, SW480, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.70×** | +4.8 | 8e-05 | 11/38 (A-172, PANC-1, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.52×** | +4.3 | 6e-04 | 4/34 (A498, HS-578T, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +3.8 | 0.005 | 5/11 (NCI-H460, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.50×** | +3.6 | 0.010 | 10/24 (NCI-H2030, C32, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.017 | 6/33 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | **1.47×** | +3.3 | 0.028 | 3/31 (SW480, LoVo, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.62×** | +3.1 | 0.059 | 1/10 (NCI-H2030) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +2.9 | 0.088 | 3/21 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1242.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[5-Azacytidine (drug)]] 5 µM |  | **0.536×** | -5.7 | 4e-06 | 16/38 (NCI-H2030, hTERT-HPNE, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.538×** | -5.6 | 4e-06 | 22/38 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.538×** | -5.6 | 4e-06 | 16/29 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.557×** | -5.3 | 2e-05 | 17/32 (C32, NCI-H2030, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.637×** | -3.9 | 0.011 | 16/31 (HS-578T, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.654×** | -3.9 | 0.011 | 14/32 (NCI-H2030, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.658×** | -3.8 | 0.012 | 13/36 (NCI-H460, SHP-77, …) | all doses, flat |  |
| [[Hexylresorcinol (drug)]] 5 µM |  | **0.762×** | -3.5 | 0.033 | 12/40 (A498, SW48, …) | top dose only |  |
| [[Furosemide (drug)]] 0.05 µM |  | **0.691×** | -3.4 | 0.048 | 3/36 (RKO, LOX-IMVI, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.698×** | -3.3 | 0.062 | 9/37 (A498, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1242. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 6.86 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 3.86 | 0 | 1 | — | [[5-Azacytidine (drug)]] 5 µM 0.0473× (z -10.7) |
| [[A-172 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.886 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.747 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.470 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.835 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.578 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.613 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.825 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.896 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.615 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1242), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSF]] | +0.65 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[HMGN3]] | +0.64 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[SMIM10]] | +0.62 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[NME4]] | +0.60 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[SPARC]] | +0.60 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[OLFML2A]] | +0.59 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[NID2]] | +0.59 | +0.65 / +0.40 | both halves | 5e-05 |  |
| [[COL3A1]] | +0.58 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[CXADR]] | +0.58 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[TMEM14A]] | +0.56 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[LDOC1]] | +0.56 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[CD302]] | +0.55 | +0.49 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL2L13]] | -0.50 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[SLC66A1]] | -0.49 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[MICALL1]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[CEP164]] | -0.48 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[CSRNP2]] | -0.48 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[AP4E1]] | -0.47 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[TTC4]] | -0.47 | -0.51 / -0.31 | both halves | 2e-04 |  |
| [[ADRM1]] | -0.47 | -0.62 / -0.26 | both halves | 4e-04 |  |
| [[ENOX2]] | -0.47 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[FBF1]] | -0.46 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[RFFL]] | -0.46 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[MRPL45P2]] | -0.46 | -0.43 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENPP2]] | B | ENPP2 activity raises FKBP7's level | lines that do not express ENPP2 (26) vs lines expressing it (24) | 2.17× lower at baseline in the lines without ENPP2 | 0.008 | ⚠ within organs, on part of the lines; also absent: SLC16A6, ITGA4, SNTG1; maybe low, not absent |
| [[P3H3]] | B | P3H3 activity raises FKBP7's level | lines that do not express P3H3 (10) vs lines expressing it (40) | 2.11× lower at baseline in the lines without P3H3 | 0.025 | ⚠ within organs, on part of the lines; also absent: STARD9, GSTA4, CTXN1 |
| [[SMIM10]] | B | SMIM10 activity raises FKBP7's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 1.82× lower at baseline in the lines without SMIM10 | 0.031 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365 |
| [[COL3A1]] | B | COL3A1 activity raises FKBP7's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 2.03× lower at baseline in the lines without COL3A1 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677 |
| [[SPARC]] | B | SPARC activity raises FKBP7's level | lines that do not express SPARC (34) vs lines expressing it (16) | 2.13× lower at baseline in the lines without SPARC | 0.048 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032 |
| [[PTN]] | B | PTN activity raises FKBP7's level | lines that do not express PTN (28) vs lines expressing it (22) | 2.02× lower at baseline in the lines without PTN | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, SPARC, BAALC |
| [[CHRDL1]] | B | CHRDL1 activity raises FKBP7's level | lines that do not express CHRDL1 (37) vs lines expressing it (13) | 1.55× lower at baseline in the lines without CHRDL1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01592, PAX3, LINC01035 |
| [[LDOC1]] | B | LDOC1 activity raises FKBP7's level | lines that do not express LDOC1 (21) vs lines expressing it (29) | 1.72× lower at baseline in the lines without LDOC1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SPANXA2-OT1, S1PR3, SNAP91; its own permutation p |
| [[ITGA4]] | B | ITGA4 activity raises FKBP7's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 2.05× lower at baseline in the lines without ITGA4 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411 |
| [[DKK3]] | B | DKK3 activity raises FKBP7's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 1.79× lower at baseline in the lines without DKK3 | 0.074 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1 |
| [[ZNF883]] | B | ZNF883 activity raises FKBP7's level | lines that do not express ZNF883 (22) vs lines expressing it (28) | 1.81× lower at baseline in the lines without ZNF883 | 0.074 | ⚠ within organs, on part of the lines; also absent: AK5, SOX5, GAP43 |
| [[MGP]] | B | MGP activity raises FKBP7's level | lines that do not express MGP (35) vs lines expressing it (15) | 1.97× lower at baseline in the lines without MGP | 0.081 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TIMP3, HTR1F, AEBP1 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GSTM4]] | B | FKBP7 activity raises GSTM4's level | lines that do not express FKBP7 (7) vs lines expressing it (43) | 1.75× lower at baseline in the lines without FKBP7 | 0.073 | ⚠ within organs, on part of the lines; also absent: C12orf75, KCNC4, MXRA7; maybe low, not absent |
| [[B4GAT1]] | B | FKBP7 activity raises B4GAT1's level | lines that do not express FKBP7 (7) vs lines expressing it (43) | 1.48× lower at baseline in the lines without FKBP7 | 0.078 | ⚠ within organs, on part of the lines; also absent: C12orf75, KCNC4, MXRA7; maybe low, not absent |
| [[METRN]] | B | FKBP7 activity raises METRN's level | lines that do not express FKBP7 (7) vs lines expressing it (43) | 1.66× lower at baseline in the lines without FKBP7 | 0.078 | ⚠ within organs, on part of the lines; also absent: C12orf75, KCNC4, MXRA7; maybe low, not absent |
| cells under [[Vemurafenib (drug)]] 5 µM | B | FKBP7 activity raises the cells' numbers under Vemurafenib 5 µM (protects the cells) | lines that do not express FKBP7 (7) vs lines expressing it (41) | the lines without FKBP7: 0.84× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: C12orf75, KCNC4, MXRA7; maybe low, not absent |
| [[CTSF]] | B | FKBP7 activity raises CTSF's level | lines that do not express FKBP7 (7) vs lines expressing it (43) | 2.74× lower at baseline in the lines without FKBP7 | 0.097 | ⚠ within organs, on part of the lines; also absent: C12orf75, KCNC4, MXRA7; maybe low, not absent |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.597). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (10.0, 5.2); signed map (23.2, 40.8). **Vector** length 49.0, 7.03% of its response variance represented; |z| ≥ 3 in 907 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +13.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +15.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +6.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +4.8 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.5 | -5.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -5.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.2 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -3.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | FKBP prolyl isomerase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.2 — chr2:178,463,664-178,478,600 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FKBP23 |
| Gene groups (HGNC) | EF-hand domain containing; FKBP prolyl isomerase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y680](https://www.uniprot.org/uniprotkb/Q9Y680) (Peptidyl-prolyl cis-trans isomerase FKBP7):

> PPIases accelerate the folding of proteins during protein synthesis.

**Summary**, from NCBI Gene [51661](https://www.ncbi.nlm.nih.gov/gene/51661):

> The protein encoded by this gene belongs to the FKBP-type peptidyl-prolyl cis/trans isomerase (PPIase) family. Members of this family exhibit PPIase activity and function as molecular chaperones. A similar protein in mouse is located in the endoplasmic reticulum and binds calcium. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3723](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3723) · Entrez [51661](https://www.ncbi.nlm.nih.gov/gene/51661) · UniProt [Q9Y680](https://www.uniprot.org/uniprotkb/Q9Y680) · Ensembl [ENSG00000079150](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079150)

## Data

Gene col 1242: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1242); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1242, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1242]; `tensor/DDL_lfc|DDL_z.npy` [1242]; `embed/gene_vectors.npy` [1242]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1242 or target_col == 1242). Every well: [[FKBP7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FKBP7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
