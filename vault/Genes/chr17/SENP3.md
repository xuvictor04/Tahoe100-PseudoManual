---
symbol: "SENP3"
type: "gene"
col: 8463
ensembl_id: "ENSG00000161956"
name: "SUMO specific peptidase 3"
location: "17p13"
module: 5
arm: "+"
pooled_cpm: 19.73
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# SENP3

*SUMO specific peptidase 3* — 17p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.25× (z +14.1, q 2e-42, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.800× (z -5.6, q 2e-05, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Tofacitinib (drug)]] 0.5 µM in 1 line (H4 0.0501×); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.236×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Rapamycin (drug)]] 0.5 µM in 1 line (H4 0.0858×); [[Decitabine (drug)]] 0.5 µM in 1 line (BT-474 0.191×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NADK]] (+0.73, fdr 7e-06), [[SMPD4]] (+0.69, fdr 7e-06), [[DIDO1]] (+0.69, fdr 7e-06); moves opposite to [[BTG1]] (-0.66, fdr 1e-05), [[SNAPIN]] (-0.61, fdr 1e-05), [[AKAP9]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NEDD9]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Rutin (trihydrate) (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8463.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.25×** | +14.1 | 2e-42 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +12.3 | 2e-32 | 44/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +12.0 | 4e-31 | 37/47 (NCI-H2030, SW 900, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.99×** | +12.0 | 6e-31 | 41/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.65×** | +11.8 | 5e-30 | 39/48 (PANC-1, KATO III, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +10.1 | 4e-22 | 38/47 (SW480, HOP62, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +9.7 | 2e-20 | 31/43 (SW480, SW 900, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.70×** | +9.2 | 4e-18 | 28/42 (A-172, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.69×** | +9.1 | 5e-18 | 38/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.71×** | +9.0 | 2e-17 | 21/33 (HT-29, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.66×** | +8.8 | 1e-16 | 37/47 (Hs 766T, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +8.6 | 4e-16 | 31/46 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.53×** | +8.4 | 1e-15 | 33/45 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.28×** | +7.5 | 3e-12 | 14/24 (NCI-H2030, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.55×** | +7.0 | 9e-11 | 22/37 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +5.1 | 1e-05 | 17/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.65×** | +4.6 | 2e-04 | 10/44 (Hs 766T, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 0.5 µM |  | **1.30×** | +4.5 | 2e-04 | 18/48 (SW480, KATO III, …) | two highest doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +4.2 | 7e-04 | 11/48 (HOP62, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.55×** | +3.9 | 0.002 | 8/46 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.002 | 13/47 (PANC-1, LoVo, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.48×** | +3.6 | 0.008 | 10/46 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.1 | 0.041 | 12/48 (HOP62, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8463.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Tofacitinib (drug)]] 0.5 µM in 1 line (H4 0.0501×); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.236×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Rapamycin (drug)]] 0.5 µM in 1 line (H4 0.0858×); [[Decitabine (drug)]] 0.5 µM in 1 line (BT-474 0.191×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.800×** | -5.6 | 2e-05 | 23/48 (A498, SW1417, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.850× | -4.1 | 0.013 | 14/48 (J82, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | 0.825× | -3.4 | 0.11 | 6/48 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.829× | -3.3 | 0.11 | 9/48 (H4, COLO 205, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.829× | -3.3 | 0.11 | 16/47 (CHP-212, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.841× | -3.0 | 0.22 | 7/48 (LS 180, Hs 766T, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8463. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 26.7 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.73× (z +14.1) | — |
| [[NCI-H460 (line)]] | wt | 23.6 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.02× (z +9.9) | — |
| [[PANC-1 (line)]] | alt | 19.9 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.30× (z +12.2) | — |
| [[H4 (line)]] | wt | 11.7 | 0 | 2 | — | [[Tofacitinib (drug)]] 0.5 µM 0.0501× (z -11.1) |
| [[LoVo (line)]] | wt | 17.3 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.75× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.236× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 18.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[BT-474 (line)]] | alt | 16.3 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.191× (z -8.9) |
| [[HOP62 (line)]] | alt | 12.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +10.2) | — |
| [[KATO III (line)]] | alt | 16.4 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.11× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 20.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +9.8) | — |
| [[LS 180 (line)]] | wt | 14.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.76× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 30.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +10.9) | — |
| [[SW 900 (line)]] | alt | 23.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +10.8) | — |
| [[A-427 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.00 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8463), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NADK]] | +0.73 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[SMPD4]] | +0.69 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[DIDO1]] | +0.69 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[ELAVL1]] | +0.67 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[TMEM248]] | +0.66 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[TMEM138]] | +0.66 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[UBE2G2]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[PEX26]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[NUDT3]] | +0.64 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[NIPA2]] | +0.64 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[PRDM15]] | +0.63 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[THAP4]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTG1]] | -0.66 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[SNAPIN]] | -0.61 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[AKAP9]] | -0.59 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[GOLGB1]] | -0.57 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[TCAF1]] | -0.56 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[H3-3B]] | -0.56 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[CTR9]] | -0.56 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[TPR]] | -0.54 | -0.48 / -0.45 | both halves | 3e-05 | STRING 439 |
| [[CHMP2B]] | -0.54 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[UBE2B]] | -0.54 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[PITPNA-AS1]] | -0.53 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[MMADHC]] | -0.53 | -0.60 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEDD9]] | B | NEDD9 activity lowers SENP3's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 1.33× higher at baseline in the lines without NEDD9 | 0.055 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Rutin (trihydrate) (drug)]] 0.05 µM | C | SENP3's natural level raises the cells' numbers under Rutin (trihydrate) 0.05 µM (protects the cells) | SENP3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67 | 0.317 over the table, 0.065 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.563). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-17.9, -29.8); signed map (-9.0, -42.0). **Vector** length 78.8, 15.6% of its response variance represented; |z| ≥ 3 in 977 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +12.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.5 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +5.2 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +5.1 | +9.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +3.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +4.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -1.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -2.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | +1.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -3.0 | +2.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -2.2 | -4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -5.6 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.7 | -2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Methotrexate (drug)]] 0.5 µM |  | -1.4 | -0.7 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.4 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | SUMO specific peptidase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13 — chr17:7,561,919-7,571,969 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP586K0919, SSP3, DKFZp762A152, SMT3IP1, Ulp1 |
| Gene groups (HGNC) | SUMO specific peptidases; Large ribosomal subunit biogenesis complex |
| Reactome | 4 pathways, smallest: Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4L4](https://www.uniprot.org/uniprotkb/Q9H4L4) (Sentrin-specific protease 3):

> Protease that releases SUMO2 and SUMO3 monomers from sumoylated substrates, but has only weak activity against SUMO1 conjugates. Deconjugates SUMO2 from MEF2D, which increases its transcriptional activation capability. Deconjugates SUMO2 and SUMO3 from CDCA8. Redox sensor that, when redistributed into nucleoplasm, can act as an effector to enhance HIF1A transcriptional activity by desumoylating EP300. Required for rRNA processing through deconjugation of SUMO2 and SUMO3 from nucleophosmin, …

**Summary**, from NCBI Gene [26168](https://www.ncbi.nlm.nih.gov/gene/26168):

> The reversible posttranslational modification of proteins by the addition of small ubiquitin-like SUMO proteins (see SUMO1; MIM 601912) is required for numerous biologic processes. SUMO-specific proteases, such as SENP3, are responsible for the initial processing of SUMO precursors to generate a C-terminal diglycine motif required for the conjugation reaction. They also have isopeptidase activity for the removal of SUMO from high molecular mass SUMO conjugates (Di Bacco et al., 2006 [PubMed …

**Accessions** — [HGNC:17862](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17862) · Entrez [26168](https://www.ncbi.nlm.nih.gov/gene/26168) · UniProt [Q9H4L4](https://www.uniprot.org/uniprotkb/Q9H4L4) · Ensembl [ENSG00000161956](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161956)

## Data

Gene col 8463: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8463); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8463, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8463]; `tensor/DDL_lfc|DDL_z.npy` [8463]; `embed/gene_vectors.npy` [8463]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8463 or target_col == 8463). Every well: [[SENP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SENP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
