---
symbol: "GMPR"
type: "gene"
col: 5983
ensembl_id: "ENSG00000137198"
name: "guanosine monophosphate reductase"
location: "6p22.3"
module: 32
arm: "+"
pooled_cpm: 8.14
n_lines_expressing: 36
n_dd_up: 23
n_dd_down: 24
n_dd_up_clean: 19
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 9
direction_downstream: 8
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# GMPR

*guanosine monophosphate reductase* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.05× (z +12.0, q 3e-30, up in 20 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.491× (z -8.3, q 4e-14, down in 25 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHFL]] (+0.70, fdr 1e-05), [[CYP2J2]] (+0.67, fdr 3e-05), [[BST2]] (+0.63, fdr 1e-05); moves opposite to [[DNAAF10]] (-0.49, fdr 1e-04).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[IFITM1]] → it (grade B ⚠); 8 go from it, the strongest it → [[SLC15A3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5983.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.05×** | +12.0 | 3e-30 | 20/33 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.55×** | +11.0 | 1e-25 | 27/32 (HOP62, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.40×** | +10.3 | 1e-22 | 23/31 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.17×** | +9.1 | 1e-17 | 17/33 (HOP62, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.12×** | +8.8 | 1e-16 | 17/31 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.00×** | +8.1 | 4e-14 | 13/31 (HOP62, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.38×** | +5.3 | 8e-06 | 8/31 (HOP62, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.51×** | +4.8 | 9e-05 | 13/29 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.50×** | +4.6 | 3e-04 | 14/30 (LoVo, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +4.6 | 3e-04 | 8/26 (C32, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.28×** | +3.9 | 0.005 | 9/31 (LoVo, A-172, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.011 | 8/32 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.011 | 12/31 (LoVo, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.36×** | +3.6 | 0.013 | 12/33 (H4, NCI-H2347, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.35×** | +3.5 | 0.015 | 4/33 (J82, LoVo, …) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.35×** | +3.5 | 0.015 | 6/31 (MIA PaCa-2, J82, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.020 | 4/32 (LoVo, SW48, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5983.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.491×** | -8.3 | 4e-14 | 25/33 (SNU-423, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.514×** | -7.8 | 2e-12 | 23/30 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.631×** | -5.4 | 1e-05 | 18/27 (RKO, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.457×** | -4.8 | 2e-04 | 17/29 (RKO, Panc 03.27, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.759×** | -4.6 | 5e-04 | 14/31 (A-172, Panc 03.27, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.677×** | -4.6 | 5e-04 | 17/31 (BT-474, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.669×** | -4.5 | 5e-04 | 11/32 (SNU-423, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.688×** | -4.4 | 9e-04 | 11/32 (LoVo, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.774×** | -4.2 | 0.001 | 18/32 (SNU-423, CHP-212, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.718×** | -3.9 | 0.006 | 12/26 (RKO, SK-MEL-2, …) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.721×** | -3.8 | 0.006 | 11/29 (RPMI-7951, Panc 03.27, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.794×** | -3.8 | 0.006 | 14/32 (A-172, SNU-423, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.721×** | -3.7 | 0.010 | 16/25 (SNU-423, KATO III, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.733×** | -3.6 | 0.011 | 12/27 (RPMI-7951, SK-MEL-2, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.743×** | -3.3 | 0.031 | 16/27 (SNU-423, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.753×** | -3.3 | 0.031 | 13/31 (SNU-423, RPMI-7951, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.755×** | -3.2 | 0.046 | 9/31 (COLO 205, SW480, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.767×** | -3.1 | 0.054 | 8/32 (SW480, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5983. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 30.2 | 0 | 11 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.104× (z -12.8) |
| [[RKO (line)]] | wt | 20.0 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0450× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.159× (z -13.9) |
| [[KATO III (line)]] | alt | 23.0 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -11.0) |
| [[HOP62 (line)]] | alt | 3.56 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 5.11× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.0911× (z -9.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 22.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.198× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.243× (z -8.9) |
| [[BT-474 (line)]] | alt | 10.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0487× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0968× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 6.27 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.107× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -8.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 25.6 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.182× (z -8.7) |
| [[A-172 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.719 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.69 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5983), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHFL]] | +0.70 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[CYP2J2]] | +0.67 | +0.44 / +0.73 | both halves | 3e-05 | **novel candidate** |
| [[BST2]] | +0.63 | +0.50 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[BATF2]] | +0.63 | +0.51 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFI44]] | +0.63 | +0.55 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[OAS1]] | +0.62 | +0.50 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFITM1]] | +0.62 | +0.51 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[STAT1]] | +0.61 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[TDRD7]] | +0.60 | +0.47 / +0.60 | both halves | 2e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[MX2]] | +0.60 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[UBE2L6]] | +0.60 | +0.49 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[MX1]] | +0.59 | +0.54 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 463 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF10]] | -0.49 | -0.34 / -0.38 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFITM1]] | B | IFITM1 activity raises GMPR's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 2.47× lower at baseline in the lines without IFITM1 | 0.032 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[IFI44L]] | B | IFI44L activity raises GMPR's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 2.34× lower at baseline in the lines without IFI44L | 0.046 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[SLC15A3]] | B | SLC15A3 activity raises GMPR's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 2.04× lower at baseline in the lines without SLC15A3 | 0.051 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |
| [[GBP4]] | B | GBP4 activity raises GMPR's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.04× lower at baseline in the lines without GBP4 | 0.053 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[LYPD5]] | B | LYPD5 activity raises GMPR's level | lines that do not express LYPD5 (16) vs lines expressing it (34) | 1.94× lower at baseline in the lines without LYPD5 | 0.055 | ⚠ within organs, on part of the lines; also absent: AGMAT, ZNF320, LIPG; maybe low, not absent |
| [[BST2]] | B | BST2 activity raises GMPR's level | lines that do not express BST2 (18) vs lines expressing it (32) | 2.29× lower at baseline in the lines without BST2 | 0.058 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |
| [[CYP2J2]] | B | CYP2J2 activity raises GMPR's level | lines that do not express CYP2J2 (12) vs lines expressing it (38) | 2.08× lower at baseline in the lines without CYP2J2 | 0.077 | ⚠ within organs, on part of the lines; also absent: CDK18 |
| [[MAP2K1]] | B | MAP2K1 activity lowers GMPR's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[EPSTI1]] | B | EPSTI1 activity raises GMPR's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 1.74× lower at baseline in the lines without EPSTI1 | 0.094 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC15A3]] | B | GMPR activity raises SLC15A3's level | lines that do not express GMPR (14) vs lines expressing it (36) | 2.08× lower at baseline in the lines without GMPR | 0.017 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[IFITM1]] | B | GMPR activity raises IFITM1's level | lines that do not express GMPR (14) vs lines expressing it (36) | 2.50× lower at baseline in the lines without GMPR | 0.031 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CMTR1]] | B | GMPR activity raises CMTR1's level | lines that do not express GMPR (14) vs lines expressing it (36) | 1.30× lower at baseline in the lines without GMPR | 0.040 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LY6E]] | B | GMPR activity raises LY6E's level | lines that do not express GMPR (14) vs lines expressing it (36) | 1.76× lower at baseline in the lines without GMPR | 0.052 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SAMHD1]] | B | GMPR activity raises SAMHD1's level | lines that do not express GMPR (14) vs lines expressing it (36) | 1.71× lower at baseline in the lines without GMPR | 0.076 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LYPD5]] | B | GMPR activity raises LYPD5's level | lines that do not express GMPR (14) vs lines expressing it (36) | 1.75× lower at baseline in the lines without GMPR | 0.076 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[RASSF4]] | B | GMPR activity raises RASSF4's level | lines that do not express GMPR (14) vs lines expressing it (36) | 1.40× lower at baseline in the lines without GMPR | 0.077 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[UBE2L6]] | B | GMPR activity raises UBE2L6's level | lines that do not express GMPR (14) vs lines expressing it (36) | 1.63× lower at baseline in the lines without GMPR | 0.084 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.580). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.0, 54.1); signed map (67.5, 31.4). **Vector** length 68.8, 14.4% of its response variance represented; |z| ≥ 3 in 802 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.55 to 23); *Interferon Signaling* (reactome, mean cos +0.53 to 45); *Interferon alpha/beta signaling* (reactome, mean cos +0.54 to 27).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +12.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +10.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.5 | +11.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +4.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +1.7 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +5.3 |
|  | [[Docetaxel (drug)]] 5 µM |  | +1.2 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -2.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.6 | -4.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.4 | -4.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -3.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.8 | -3.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.8 | -3.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.7 | -3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | guanosine monophosphate reductase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.3 — chr6:16,238,587-16,295,549 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GMPR1, hGMPR-I |
| Gene groups (HGNC) | Guanosine monophosphate reductase family |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE |
| Reactome | 6 pathways, smallest: Regulation of MITF-M dependent genes involved in invasion; Purine salvage; Nucleotide salvage |
| Matched by | ensembl_id |

**Function**, from UniProt [P36959](https://www.uniprot.org/uniprotkb/P36959) (GMP reductase 1):

> Catalyzes the irreversible NADPH-dependent deamination of GMP to IMP. It functions in the conversion of nucleobase, nucleoside and nucleotide derivatives of G to A nucleotides, and in maintaining the intracellular balance of A and G nucleotides.

**Summary**, from NCBI Gene [2766](https://www.ncbi.nlm.nih.gov/gene/2766):

> This gene encodes an enzyme that catalyzes the irreversible and NADPH-dependent reductive deamination of GMP to IMP. The protein also functions in the re-utilization of free intracellular bases and purine nucleosides.[provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:4376](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4376) · Entrez [2766](https://www.ncbi.nlm.nih.gov/gene/2766) · UniProt [P36959](https://www.uniprot.org/uniprotkb/P36959) · Ensembl [ENSG00000137198](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137198)

## Data

Gene col 5983: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5983); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5983, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5983]; `tensor/DDL_lfc|DDL_z.npy` [5983]; `embed/gene_vectors.npy` [5983]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5983 or target_col == 5983). Every well: [[GMPR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GMPR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
