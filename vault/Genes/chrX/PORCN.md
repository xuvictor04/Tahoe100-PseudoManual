---
symbol: "PORCN"
type: "gene"
col: 2237
ensembl_id: "ENSG00000102312"
name: "porcupine O-acyltransferase"
location: "Xp11.23"
module: 189
arm: "+"
pooled_cpm: 8.19
n_lines_expressing: 45
n_dd_up: 11
n_dd_down: 15
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 12
direction_downstream: 1
tags: ["gene", "module/189"]
generated_by: "tahoemap"
---

# PORCN

*porcupine O-acyltransferase* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.65× (z +5.8, q 5e-06, up in 16 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Verteporfin (drug)]] 5 µM: 0.577× (z -6.1, q 5e-07, down in 20 of 39 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLGAP4]] (+0.65, fdr 1e-05), [[EHD2]] (+0.62, fdr 1e-05), [[PLPPR2]] (+0.61, fdr 2e-04); moves opposite to [[ECHDC1]] (-0.57, fdr 4e-05), [[ANAPC1]] (-0.53, fdr 2e-05), [[NAF1]] (-0.53, fdr 1e-04).
> It is in [[Module 189]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[LINC02725]] → it (grade B ⚠); 1 goes from it, the strongest it → [[FSCN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2237.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.65×** | +5.8 | 5e-06 | 16/43 (KATO III, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.59×** | +5.4 | 2e-05 | 17/42 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +5.0 | 1e-04 | 8/26 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +4.8 | 3e-04 | 4/14 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.43×** | +3.9 | 0.010 | 8/34 (HS-578T, SW 1088, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.010 | 11/41 (MIA PaCa-2, Hs 766T, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.05 µM |  | **1.42×** | +3.8 | 0.010 | 6/37 (Hs 766T, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.6 | 0.019 | 7/27 (MIA PaCa-2, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.025 | 6/42 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +3.3 | 0.059 | 2/19 (AsPC-1, J82) | rises with dose | noisy plate (z scaled) |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.079 | 8/37 (H4, NCI-H1792, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2237.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.577×** | -6.1 | 5e-07 | 20/39 (NCI-H2030, SW 900, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.615×** | -5.6 | 5e-06 | 18/40 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.740×** | -4.9 | 1e-04 | 15/41 (HOP62, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.693×** | -4.3 | 0.003 | 17/43 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.708×** | -4.0 | 0.007 | 10/38 (HEC-1-A, NCI-H2030, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.726×** | -3.7 | 0.019 | 13/40 (HOP62, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.730×** | -3.6 | 0.022 | 14/41 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.738×** | -3.5 | 0.029 | 6/39 (C32, LoVo, …) | inconsistent across doses | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.808×** | -3.5 | 0.029 | 6/40 (SW 900, SW1417, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.751×** | -3.3 | 0.050 | 11/31 (HOP62, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.526×** | -3.3 | 0.051 | 11/36 (Hs 766T, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.754×** | -3.3 | 0.051 | 9/42 (NCI-H1792, A-172, …) | rises with dose |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **0.749×** | -3.2 | 0.051 | 5/41 (SW480, NCI-H2030, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.745×** | -3.2 | 0.051 | 14/38 (CFPAC-1, HOP62, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **0.833×** | -3.0 | 0.100 | 20/36 (NCI-H1792, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2237. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 18.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0772× (z -16.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -9.0) |
| [[Hs 766T (line)]] | wt | 22.6 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -11.7) ⚠ cell-cycle shift, explains ~4% of this change |
| [[NCI-H1792 (line)]] | alt | 19.1 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0985× (z -17.0) ⚠ cell-cycle shift, explains ~4% of this change |
| [[CFPAC-1 (line)]] | alt | 34.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -11.5) ⚠ cell-cycle shift, explains ~4% of this change |
| [[HOP62 (line)]] | alt | 9.29 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.214× (z -9.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H2030 (line)]] | alt | 4.45 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0583× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 4.22 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0648× (z -13.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.117× (z -8.8) ⚠ toxic |
| [[SW1417 (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -8.7) ⚠ cell-cycle shift, explains ~4% of this change |
| [[A-172 (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2237), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLGAP4]] | +0.65 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[EHD2]] | +0.62 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[PLPPR2]] | +0.61 | +0.61 / +0.31 | both halves | 2e-04 |  |
| [[GNAI2]] | +0.61 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[SLC9A3R2]] | +0.60 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[PDLIM7]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[TMEM184B]] | +0.58 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[RING1]] | +0.57 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[ACAP3]] | +0.57 | +0.39 / +0.44 | both halves | 5e-05 |  |
| [[LYPD3]] | +0.57 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[PLSCR3]] | +0.57 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[ELOVL1]] | +0.56 | +0.55 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECHDC1]] | -0.57 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[ANAPC1]] | -0.53 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[NAF1]] | -0.53 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[METTL4]] | -0.53 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[DPY19L1P1]] | -0.50 | -0.54 / -0.24 | both halves | 5e-04 |  |
| [[NSMAF]] | -0.49 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[RCC1L]] | -0.49 | -0.35 / -0.29 | both halves | 2e-04 |  |
| [[NUP107]] | -0.49 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[LAMTOR5-AS1]] | -0.49 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[PAXBP1]] | -0.49 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[VSIG10]] | -0.48 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[RNASEH2B]] | -0.48 | -0.47 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02725]] | B | LINC02725 activity raises PORCN's level | lines that do not express LINC02725 (35) vs lines expressing it (15) | 2.17× lower at baseline in the lines without LINC02725 | 0.003 | ⚠ within organs, on part of the lines; also absent: DHRS9, ENSG00000203434, LINC01425 |
| [[WNT7B]] | B | WNT7B activity raises PORCN's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 2.06× lower at baseline in the lines without WNT7B | 0.007 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[KRT81]] | B | KRT81 activity raises PORCN's level | lines that do not express KRT81 (34) vs lines expressing it (16) | 2.30× lower at baseline in the lines without KRT81 | 0.022 | ⚠ within organs, on part of the lines; also absent: CARD11, ANXA8, PSG9 |
| [[F3]] | B | F3 activity raises PORCN's level | lines that do not express F3 (24) vs lines expressing it (26) | 2.27× lower at baseline in the lines without F3 | 0.023 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[STRA6]] | B | STRA6 activity raises PORCN's level | lines that do not express STRA6 (26) vs lines expressing it (24) | 1.82× lower at baseline in the lines without STRA6 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000261543, CCDC33, ACKR3 |
| [[SMOX]] | B | SMOX activity raises PORCN's level | lines that do not express SMOX (6) vs lines expressing it (44) | 2.01× lower at baseline in the lines without SMOX | 0.049 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[ADAM8]] | B | ADAM8 activity raises PORCN's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 1.99× lower at baseline in the lines without ADAM8 | 0.060 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[WNT7B]] | B | WNT7B activity strengthens PORCN's drug response | lines that do not express WNT7B (18) vs lines expressing it (25) | the lines without WNT7B respond 0.70× as strongly (z diff +0.30); rises at some drug-doses, falls at others (32% from rises): Selinexor 5 µM: 0.97x vs 0.57x (z diff +3.3); Verteporfin 5 µM: 0.61x vs 0.45x (z diff +1.6); Thymol 0.5 µM: 1.16x vs 1.50x (z diff +1.1) | 0.087 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[NDRG1]] | B | NDRG1 activity raises PORCN's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.85× lower at baseline in the lines without NDRG1 | 0.088 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[LYPD3]] | B | LYPD3 activity raises PORCN's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 1.53× lower at baseline in the lines without LYPD3 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[TMEM92]] | B | TMEM92 activity raises PORCN's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.89× lower at baseline in the lines without TMEM92 | 0.093 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[FLNB]] | C | FLNB activity raises PORCN's level | lines that do not express FLNB (3) vs lines expressing it (47) | 2.15× lower at baseline in the lines without FLNB | 0.086 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYO1E, B4GALT1, SMOX; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSCN1]] | B | PORCN activity raises FSCN1's level | lines that do not express PORCN (5) vs lines expressing it (45) | 2.59× lower at baseline in the lines without PORCN | 0.029 | ⚠ within organs, on part of the lines; also absent: IQSEC2, APOBEC3F, CELSR1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 189]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.727). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.1, -1.4); signed map (-22.5, 25.1). **Vector** length 65.3, 11.6% of its response variance represented; |z| ≥ 3 in 752 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +5.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.7 | +5.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +3.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +4.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | +0.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.3 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.5 | -4.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.8 | -5.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -1.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -1.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | porcupine O-acyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:48,508,959-48,520,814 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MG61, PORC, PPN, por; previously DHOF |
| Gene groups (HGNC) | Membrane bound O-acyltransferase family |
| Reactome | 4 pathways, smallest: WNT ligand biogenesis and trafficking; Signaling by WNT in cancer; Signaling by WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H237](https://www.uniprot.org/uniprotkb/Q9H237) (Protein-serine O-palmitoleoyltransferase porcupine):

> Protein-serine O-palmitoleoyltransferase that acts as a key regulator of the Wnt signaling pathway by mediating the attachment of palmitoleate, a 16-carbon monounsaturated fatty acid (C16:1(9Z)), to Wnt proteins. Serine palmitoleoylation of WNT proteins is required for efficient binding to frizzled receptors.

**Summary**, from NCBI Gene [64840](https://www.ncbi.nlm.nih.gov/gene/64840):

> This gene belongs to the evolutionarily conserved porcupine (Porc) gene family. Genes of the porcupine family encode endoplasmic reticulum proteins with multiple transmembrane domains. Porcupine proteins are involved in the processing of Wnt (wingless and int homologue) proteins. Disruption of this gene is associated with focal dermal hypoplasia, and the encoded protein has been implicated in cancer. Multiple alternatively spliced transcript variants encoding distinct isoforms have been …

**Accessions** — [HGNC:17652](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17652) · Entrez [64840](https://www.ncbi.nlm.nih.gov/gene/64840) · UniProt [Q9H237](https://www.uniprot.org/uniprotkb/Q9H237) · Ensembl [ENSG00000102312](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102312)

## Data

Gene col 2237: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2237); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2237, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2237]; `tensor/DDL_lfc|DDL_z.npy` [2237]; `embed/gene_vectors.npy` [2237]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2237 or target_col == 2237). Every well: [[PORCN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PORCN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
