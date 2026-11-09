---
symbol: "GTF3C6"
type: "gene"
col: 7874
ensembl_id: "ENSG00000155115"
name: "general transcription factor IIIC subunit 6"
location: "6q21"
module: 137
arm: "+"
pooled_cpm: 14.15
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# GTF3C6

*general transcription factor IIIC subunit 6* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.73× (z +14.8, q 0e+00, up in 37 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.55× (z +3.6, q 0.031, up in 19 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (PANC-1 8.67×, NCI-H1792 12.3×, NCI-H460 8.29×, KATO III 9.49×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (PANC-1 7.44×, A498 8.70×, NCI-H1792 9.62×, LOX-IMVI 6.65×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.338× (z -9.1, q 3e-17, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A21]] (+0.78, fdr 1e-05), [[FAIM]] (+0.75, fdr 1e-05), [[MCCC2]] (+0.74, fdr 1e-05); moves opposite to [[DNAAF3]] (-0.72, fdr 3e-05), [[NDRG1]] (-0.67, fdr 1e-05), [[TMEM184B]] (-0.66, fdr 2e-05).
> It sits in the **+** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[CLMN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7874.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (PANC-1 8.67×, NCI-H1792 12.3×, NCI-H460 8.29×, KATO III 9.49×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (PANC-1 7.44×, A498 8.70×, NCI-H1792 9.62×, LOX-IMVI 6.65×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.73×** | +14.8 | 0e+00 | 37/38 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.74×** | +12.7 | 2e-34 | 27/29 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.19×** | +9.1 | 2e-17 | 30/32 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +6.0 | 2e-07 | 33/43 (HepG2/C3A, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.77×** | +4.9 | 1e-04 | 31/44 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.55×** | +3.6 | 0.031 | 19/46 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.049 | 17/48 (J82, C32, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **1.49×** | +3.2 | 0.082 | 20/45 (NCI-H1792, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7874.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.338×** | -9.1 | 3e-17 | 42/47 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.343×** | -9.0 | 6e-17 | 46/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.366×** | -8.5 | 5e-15 | 43/47 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.415×** | -7.4 | 2e-11 | 42/47 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.540×** | -5.2 | 2e-05 | 31/46 (AN3 CA, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.284×** | -4.9 | 1e-04 | 34/48 (SW48, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.684×** | -4.5 | 5e-04 | 30/48 (KATO III, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7874. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 16.2 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 6.58× (z +10.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.149× (z -10.5) |
| [[KATO III (line)]] | alt | 16.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 9.49× (z +11.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.138× (z -9.9) |
| [[SHP-77 (line)]] | alt | 24.4 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.175× (z -9.7) |
| [[A498 (line)]] | wt | 9.65 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.00× (z +11.0) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 8.13 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0550× (z -9.9) |
| [[HOP62 (line)]] | alt | 8.25 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.42× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 12.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.09× (z +9.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 19.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.65× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 11.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.3× (z +12.4) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 12.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.29× (z +11.4) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 23.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.67× (z +14.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 11.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.87× (z +9.8) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 13.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.21× (z +9.1) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 10.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HEC-1-A (line)]] | alt | 14.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.02× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 12.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.55× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 13.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.23× (z +8.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 22.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +8.7) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 15.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.43× (z +9.6) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 21.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.173× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 13.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.106× (z -10.7) |
| [[SW 900 (line)]] | alt | 12.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.92× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7874), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A21]] | +0.78 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[FAIM]] | +0.75 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[MCCC2]] | +0.74 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[MRPS7]] | +0.70 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[PBLD]] | +0.70 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[NFYC]] | +0.70 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[SENP6]] | +0.68 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[FIZ1]] | +0.68 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[RMDN2]] | +0.68 | +0.55 / +0.27 | both halves | 3e-04 |  |
| [[PHACTR2]] | +0.68 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[QTRT1]] | +0.68 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[ZFX]] | +0.68 | +0.65 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF3]] | -0.72 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[NDRG1]] | -0.67 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[TMEM184B]] | -0.66 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[YIF1B]] | -0.66 | -0.56 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[SLC27A1]] | -0.64 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[HEBP1]] | -0.64 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[GMCL1]] | -0.64 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[P4HB]] | -0.64 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[F11R]] | -0.63 | -0.63 / -0.34 | both halves | 1e-04 |  |
| [[ANKRD27]] | -0.63 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[PCMT1]] | -0.63 | -0.58 / -0.31 | both halves | 2e-04 |  |
| [[CARD19]] | -0.63 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[WIPI1]] | -0.61 | -0.57 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLMN]] | B | CLMN activity lowers GTF3C6's level | lines that do not express CLMN (7) vs lines expressing it (43) | 1.65× higher at baseline in the lines without CLMN | 0.015 | ⚠ within organs, on part of the lines; also absent: ITPR3, NABP1, HTATIP2; maybe low, not absent |
| [[NDRG1]] | B | NDRG1 activity lowers GTF3C6's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.73× higher at baseline in the lines without NDRG1 | 0.017 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[LINC00887]] | B | LINC00887 activity lowers GTF3C6's level | lines that do not express LINC00887 (8) vs lines expressing it (42) | 1.70× higher at baseline in the lines without LINC00887 | 0.040 | ⚠ within organs, on part of the lines; also absent: LINC02036, STAMBPL1, CFAP45; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises GTF3C6's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises GTF3C6's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CIB1]] | C | CIB1 activity lowers GTF3C6's level | lines that do not express CIB1 (4) vs lines expressing it (46) | 1.82× higher at baseline in the lines without CIB1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.858). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-5.3, 7.4); signed map (21.3, -31.4). **Vector** length 65.9, 14.7% of its response variance represented; |z| ≥ 3 in 730 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.2 | +3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +0.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +14.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +3.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +0.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.7 | +1.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.6 | +1.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.9 | -9.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.6 | -7.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.5 | -9.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.4 | -5.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.9 | -8.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -4.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.2 | -0.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.1 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | general transcription factor IIIC subunit 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:110,958,706-110,967,890 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA397G5.3, TFIIIC35; previously C6orf51 |
| Gene groups (HGNC) | General transcription factor IIIC complex subunits |
| Reactome | 5 pathways, smallest: RNA Polymerase III Transcription Initiation From Type 2 Promoter; RNA Polymerase III Transcription Initiation From Type 1 Promoter; RNA Polymerase III Transcription Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969F1](https://www.uniprot.org/uniprotkb/Q969F1) (General transcription factor 3C polypeptide 6):

> Involved in RNA polymerase III-mediated transcription. Integral, tightly associated component of the DNA-binding TFIIIC2 subcomplex that directly binds tRNA and virus-associated RNA promoters.

**Summary**, from NCBI Gene [112495](https://www.ncbi.nlm.nih.gov/gene/112495):

> RNA polymerases are unable to initiate RNA synthesis in the absence of additional proteins called general transcription factors (GTFs). GTFs assemble in a complex on the DNA promoter and recruit the RNA polymerase. GTF3C family proteins (e.g., GTF3C1, MIM 603246) are essential for RNA polymerase III to make a number of small nuclear and cytoplasmic RNAs, including 5S RNA (MIM 180420), tRNA, and adenovirus-associated (VA) RNA of both cellular and viral origin.[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:20872](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20872) · Entrez [112495](https://www.ncbi.nlm.nih.gov/gene/112495) · UniProt [Q969F1](https://www.uniprot.org/uniprotkb/Q969F1) · Ensembl [ENSG00000155115](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155115)

## Data

Gene col 7874: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7874); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7874, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7874]; `tensor/DDL_lfc|DDL_z.npy` [7874]; `embed/gene_vectors.npy` [7874]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7874 or target_col == 7874). Every well: [[GTF3C6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF3C6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
