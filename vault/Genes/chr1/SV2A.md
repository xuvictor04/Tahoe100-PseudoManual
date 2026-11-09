---
symbol: "SV2A"
type: "gene"
col: 8222
ensembl_id: "ENSG00000159164"
name: "synaptic vesicle glycoprotein 2A"
location: "1q21.2"
module: 47
arm: "+"
pooled_cpm: 6.5
n_lines_expressing: 33
n_dd_up: 31
n_dd_down: 6
n_dd_up_clean: 18
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# SV2A

*synaptic vesicle glycoprotein 2A* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.54× (z +13.6, q 3e-39, up in 7 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.55× (z +6.9, q 7e-10, up in 7 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.505× (z -7.6, q 1e-11, down in 20 of 28 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B4GAT1]] (+0.51, fdr 2e-05), [[TCEA2]] (+0.48, fdr 6e-05), [[ADIPOR2]] (+0.47, fdr 4e-05); moves opposite to [[NOTCH2NLB]] (-0.52, fdr 2e-04), [[ROR1-AS1]] (-0.43, fdr 2e-04), [[RGS5]] (-0.42, fdr 5e-04).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CFI]] → it (grade B ⚠); 2 go from it, the strongest it → [[POGLUT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8222.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.54×** | +13.6 | 3e-39 | 7/11 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.74×** | +11.3 | 6e-27 | 12/20 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.21×** | +8.5 | 2e-15 | 15/21 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +6.9 | 7e-10 | 7/26 (HEC-1-A, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.76×** | +6.3 | 3e-08 | 16/28 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +6.1 | 9e-08 | 12/30 (CFPAC-1, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.73×** | +6.1 | 9e-08 | 19/29 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.64×** | +5.5 | 2e-06 | 16/30 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.67×** | +5.3 | 6e-06 | 6/14 (A-172, J82, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.59×** | +5.2 | 1e-05 | 15/29 (SW480, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +5.1 | 2e-05 | 19/27 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +4.3 | 7e-04 | 13/27 (CFPAC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.3 | 8e-04 | 13/30 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.40×** | +3.7 | 0.007 | 4/26 (CHP-212, NCI-H1573, …) | two highest doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.007 | 8/28 (A-172, HepG2/C3A, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.008 | 9/29 (SW 900, H4, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.046 | 3/30 (HepG2/C3A, NCI-H2030, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.054 | 6/27 (SK-MEL-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.32×** | +3.1 | 0.057 | 8/28 (HOP62, SNU-423, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.47×** | +3.1 | 0.057 | 2/26 (NCI-H460, SW 900) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.060 | 2/28 (SK-MEL-2, C32) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.32×** | +3.0 | 0.060 | 6/29 (HOP62, A-172, …) | top dose only |  |
| [[Ritonavir (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.065 | 5/29 (SW 900, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8222.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.505×** | -7.6 | 1e-11 | 20/28 (NCI-H1573, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.649×** | -4.8 | 4e-04 | 20/31 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.681×** | -4.3 | 0.003 | 11/28 (NCI-H23, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.673×** | -4.2 | 0.003 | 14/28 (A-172, SW 900, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.710×** | -3.8 | 0.015 | 12/29 (A-172, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.711×** | -3.5 | 0.041 | 2/28 (NCI-H2030, RPMI-7951) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8222. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 29.7 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.52× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -20.9) |
| [[NCI-H23 (line)]] | alt | 7.86 | 0 | 3 | — | [[Bendamustine (drug)]] 5 µM 0.0768× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 23.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -11.1) |
| [[SW 900 (line)]] | alt | 23.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -12.7) |
| [[CHP-212 (line)]] | wt | 28.4 | 0 | 1 | — | [[Amsacrine (drug)]] 0.5 µM 0.0829× (z -9.6) |
| [[HS-578T (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.233× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.740 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.920 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.943 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.690 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.708 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.885 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.810 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.608 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.989 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8222), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B4GAT1]] | +0.51 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[TCEA2]] | +0.48 | +0.52 / +0.38 | both halves | 6e-05 |  |
| [[ADIPOR2]] | +0.47 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[ZNF883]] | +0.47 | +0.36 / +0.49 | both halves | 1e-04 |  |
| [[SLC22A17]] | +0.46 | +0.39 / +0.39 | both halves | 6e-05 | same gene group |
| [[DOK3]] | +0.46 | +0.47 / +0.36 | both halves | 9e-05 |  |
| [[ATP2A1]] | +0.46 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[ANO8]] | +0.45 | +0.42 / +0.38 | both halves | 6e-05 |  |
| [[RTL8A]] | +0.45 | +0.28 / +0.40 | both halves | 3e-04 |  |
| [[TTLL13]] | +0.44 | +0.40 / +0.35 | both halves | 1e-04 |  |
| [[LINC02133]] | +0.44 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[NPAS1]] | +0.44 | +0.37 / +0.40 | both halves | 8e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOTCH2NLB]] | -0.52 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[ROR1-AS1]] | -0.43 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[RGS5]] | -0.42 | -0.24 / -0.35 | both halves | 5e-04 |  |
| [[NOTCH2NLC]] | -0.42 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[DUS4L]] | -0.42 | -0.36 / -0.32 | both halves | 1e-04 |  |
| [[NEMP1]] | -0.41 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[CGGBP1]] | -0.41 | -0.19 / -0.38 | ⚠ not reproduced | 9e-04 |  |
| [[UEVLD]] | -0.41 | -0.27 / -0.35 | both halves | 3e-04 |  |
| [[MTR]] | -0.40 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[ITPA]] | -0.39 | -0.29 / -0.29 | both halves | 3e-04 |  |
| [[UBE3B]] | -0.39 | -0.13 / -0.44 | ⚠ not reproduced | 0.002 |  |
| [[TRAF3IP2-AS1]] | -0.39 | -0.20 / -0.36 | ⚠ not reproduced | 8e-04 |  |
| [[BAGE2]] | -0.38 | -0.29 / -0.27 | both halves | 3e-04 |  |
| [[CCDC15]] | -0.38 | -0.42 / -0.27 | both halves | 3e-04 |  |
| [[NLGN4Y]] | -0.38 | -0.29 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFI]] | B | CFI activity raises SV2A's level | lines that do not express CFI (31) vs lines expressing it (19) | 3.08× lower at baseline in the lines without CFI | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1 |
| [[SYNGR1]] | B | SYNGR1 activity raises SV2A's level | lines that do not express SYNGR1 (12) vs lines expressing it (38) | 2.63× lower at baseline in the lines without SYNGR1 | 0.078 | ⚠ within organs, on part of the lines; also absent: TTC7B, RASSF8, EML1 |
| [[ZNF883]] | C | ZNF883 activity raises SV2A's level | lines that do not express ZNF883 (22) vs lines expressing it (28) | 2.69× lower at baseline in the lines without ZNF883 | 0.041 | ⚠ within organs, on part of the lines; also absent: AK5, SOX5, GAP43; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POGLUT2]] | B | SV2A activity raises POGLUT2's level | lines that do not express SV2A (17) vs lines expressing it (33) | 1.54× lower at baseline in the lines without SV2A | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000268163, SYT11, SMARCA1; maybe low, not absent |
| [[SYNGR1]] | B | SV2A activity raises SYNGR1's level | lines that do not express SV2A (17) vs lines expressing it (33) | 2.41× lower at baseline in the lines without SV2A | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000268163, SYT11, SMARCA1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.336). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.5, -19.6); signed map (-47.3, 33.3). **Vector** length 51.7, 9.51% of its response variance represented; |z| ≥ 3 in 617 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +8.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.5 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +13.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.2 | +4.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +0.1 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.4 | +3.7 |
|  | [[EX229 (drug)]] 5 µM |  | +1.3 | +2.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +3.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -3.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.8 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.2 | -0.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -7.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.5 | -0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | synaptic vesicle glycoprotein 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:149,903,318-149,917,844 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SV2, KIAA0736, SLC22B1 |
| Gene groups (HGNC) | Solute carrier family 22 |
| Reactome | 5 pathways, smallest: Toxicity of botulinum toxin type D (botD); Toxicity of botulinum toxin type F (botF); Neurotoxicity of clostridium toxins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L0J3](https://www.uniprot.org/uniprotkb/Q7L0J3) (Synaptic vesicle glycoprotein 2A):

> Plays a role in the control of regulated secretion in neural and endocrine cells, enhancing selectively low-frequency neurotransmission. Positively regulates vesicle fusion by maintaining the readily releasable pool of secretory vesicles (By similarity).; (Microbial infection) Receptor for the C.botulinum neurotoxin type A2 (BoNT/A, botA); glycosylation is not essential but enhances the interaction. Probably also serves as a receptor for the closely related C.botulinum neurotoxin type A1.

**Summary**, from NCBI Gene [9900](https://www.ncbi.nlm.nih.gov/gene/9900):

> The protein encoded by this gene is one of three related synaptic vesicle proteins. The encoded protein may interact with synaptotagmin to enhance low frequency neurotransmission in quiescent neurons. [provided by RefSeq, Jun 2016]

**Accessions** — [HGNC:20566](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20566) · Entrez [9900](https://www.ncbi.nlm.nih.gov/gene/9900) · UniProt [Q7L0J3](https://www.uniprot.org/uniprotkb/Q7L0J3) · Ensembl [ENSG00000159164](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159164)

## Data

Gene col 8222: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8222); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8222, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8222]; `tensor/DDL_lfc|DDL_z.npy` [8222]; `embed/gene_vectors.npy` [8222]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8222 or target_col == 8222). Every well: [[SV2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SV2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
