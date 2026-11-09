---
symbol: "CMKLR2"
type: "gene"
col: 11434
ensembl_id: "ENSG00000183671"
name: "chemerin chemokine-like receptor 2"
location: "2q33.3"
module: 63
arm: "+"
pooled_cpm: 2.34
n_lines_expressing: 34
n_dd_up: 32
n_dd_down: 1
n_dd_up_clean: 23
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 7
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# CMKLR2

*chemerin chemokine-like receptor 2* — 2q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.03× (z +7.7, q 6e-12, up in 1 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 2.58× (z +6.6, q 5e-09, up in 17 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.554× (z -4.1, q 0.021, down in 9 of 24 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 0.119×); [[Harringtonine (drug)]] 5 µM in 1 line (A498 0.1000×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TOM1L1]] (+0.64, fdr 1e-05), [[SLC22A15]] (+0.62, fdr 1e-05), [[LINC00662]] (+0.55, fdr 2e-05); moves opposite to [[CD82]] (-0.58, fdr 1e-05), [[ANTXR2]] (-0.56, fdr 1e-05), [[NT5E]] (-0.56, fdr 1e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC16A6]] → it (grade B ⚠); 7 go from it, the strongest it → [[VEGFC]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11434.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.03×** | +7.7 | 6e-12 | 1/10 (HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.99×** | +7.4 | 4e-11 | 0/4 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.12×** | +7.3 | 4e-11 | 0/5 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.58×** | +6.6 | 5e-09 | 17/27 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.25×** | +5.7 | 2e-06 | 13/22 (SW480, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +5.4 | 4e-06 | 2/18 (KATO III, LoVo) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.28×** | +5.4 | 4e-06 | 14/20 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.73×** | +5.4 | 4e-06 | 5/27 (A498, LOX-IMVI, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +5.1 | 2e-05 | 2/7 (SW480, NCI-H460) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +4.9 | 5e-05 | 10/26 (SW1417, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **2.01×** | +4.9 | 5e-05 | 13/28 (SW480, H4, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.81×** | +4.1 | 0.002 | 9/19 (SW1417, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.79×** | +4.1 | 0.002 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +4.0 | 0.002 | 7/20 (A498, HS-578T, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.48×** | +3.9 | 0.004 | 7/26 (LS 180, HS-578T, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.54×** | +3.7 | 0.007 | 7/25 (NCI-H460, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **2.62×** | +3.5 | 0.013 | 8/12 (NCI-H460, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.66×** | +3.4 | 0.018 | 10/19 (NCI-H460, SW480, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.61×** | +3.3 | 0.025 | 6/25 (SW480, NCI-H1792, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.63×** | +3.3 | 0.027 | 1/15 (SW1417) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11434.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 0.119×); [[Harringtonine (drug)]] 5 µM in 1 line (A498 0.1000×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.554×** | -4.1 | 0.021 | 9/24 (SW480, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Vilanterol (drug)]] 5 µM |  | 0.706× | -3.4 | 0.14 | 3/24 (NCI-H1792, NCI-H460, …) | rises with dose | position effect removed |
| [[BAY1125976 (drug)]] 5 µM |  | 0.403× | -3.3 | 0.14 | 4/27 (HOP62, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.624× | -3.3 | 0.14 | 8/29 (SW480, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.631× | -3.2 | 0.14 | 7/19 (J82, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11434. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 11.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.1000× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 7.24 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.119× (z -10.1) |
| [[A-172 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.454 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.644 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.475 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.761 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.457 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.551 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.822 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.476 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.690 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.620 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.642 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.785 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.570 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.427 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.432 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.696 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.613 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11434), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOM1L1]] | +0.64 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[SLC22A15]] | +0.62 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[LINC00662]] | +0.55 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[EIF2S2]] | +0.54 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[MAP2]] | +0.53 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[LINC01012]] | +0.53 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[MIA2]] | +0.52 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[PYROXD1]] | +0.52 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[XPOT]] | +0.52 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[DMGDH]] | +0.52 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[HECW1]] | +0.52 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[TSC22D3]] | +0.51 | +0.47 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD82]] | -0.58 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[ANTXR2]] | -0.56 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[NT5E]] | -0.56 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[ATP13A3]] | -0.56 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[LIF]] | -0.55 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[SYNJ2]] | -0.52 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[SHB]] | -0.52 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[WWTR1]] | -0.51 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[IL11]] | -0.51 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[SMAD3]] | -0.51 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[TFPI2]] | -0.50 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[VEGFC]] | -0.50 | -0.44 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A6]] | B | SLC16A6 activity raises CMKLR2's level | lines that do not express SLC16A6 (27) vs lines expressing it (23) | 1.57× lower at baseline in the lines without SLC16A6 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENPP2, TMEM47, IGFBP7 |
| [[SYNJ2]] | C | SYNJ2 activity lowers CMKLR2's level | lines that do not express SYNJ2 (4) vs lines expressing it (46) | 2.31× higher at baseline in the lines without SYNJ2 | 0.017 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF827, LINC01277, ITGA2-AS1; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VEGFC]] | B | CMKLR2 activity raises VEGFC's level | lines that do not express CMKLR2 (16) vs lines expressing it (34) | 2.08× lower at baseline in the lines without CMKLR2 | 0.058 | ⚠ within organs, on part of the lines; also absent: SATB1-AS1, ENSG00000231772, NYAP2; maybe low, not absent |
| [[TMEM200A]] | B | CMKLR2 activity raises TMEM200A's level | lines that do not express CMKLR2 (16) vs lines expressing it (34) | 2.66× lower at baseline in the lines without CMKLR2 | 0.059 | ⚠ within organs, on part of the lines; also absent: SATB1-AS1, ENSG00000231772, NYAP2; maybe low, not absent |
| [[TMTC1]] | B | CMKLR2 activity raises TMTC1's level | lines that do not express CMKLR2 (16) vs lines expressing it (34) | 2.48× lower at baseline in the lines without CMKLR2 | 0.059 | ⚠ within organs, on part of the lines; also absent: SATB1-AS1, ENSG00000231772, NYAP2; maybe low, not absent |
| [[SAMD3]] | B | CMKLR2 activity raises SAMD3's level | lines that do not express CMKLR2 (16) vs lines expressing it (34) | 2.73× lower at baseline in the lines without CMKLR2 | 0.064 | ⚠ within organs, on part of the lines; also absent: SATB1-AS1, ENSG00000231772, NYAP2; maybe low, not absent |
| [[IL1B]] | B | CMKLR2 activity raises IL1B's level | lines that do not express CMKLR2 (16) vs lines expressing it (34) | 2.65× lower at baseline in the lines without CMKLR2 | 0.067 | ⚠ within organs, on part of the lines; also absent: SATB1-AS1, ENSG00000231772, NYAP2; maybe low, not absent |
| [[LFNG]] | B | CMKLR2 activity raises LFNG's level | lines that do not express CMKLR2 (16) vs lines expressing it (34) | 1.57× lower at baseline in the lines without CMKLR2 | 0.092 | ⚠ within organs, on part of the lines; also absent: SATB1-AS1, ENSG00000231772, NYAP2; maybe low, not absent |
| [[PODXL]] | B | CMKLR2 activity raises PODXL's level | lines that do not express CMKLR2 (16) vs lines expressing it (34) | 2.10× lower at baseline in the lines without CMKLR2 | 0.097 | ⚠ within organs, on part of the lines; also absent: SATB1-AS1, ENSG00000231772, NYAP2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.514). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.9, 49.5); signed map (-9.9, 25.9). **Vector** length 54.1, 12.1% of its response variance represented; |z| ≥ 3 in 665 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +3.4 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.3 | +6.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.2 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +4.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +3.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -4.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -1.4 | -3.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.1 | +0.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.8 | -0.5 |
|  | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | -0.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | chemerin chemokine-like receptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.3 — chr2:206,175,316-206,218,047 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GPR1 |
| Gene groups (HGNC) | Chemerin receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [P46091](https://www.uniprot.org/uniprotkb/P46091) (Chemerin-like receptor 2):

> Receptor for chemoattractant adipokine chemerin/RARRES2 suggesting a role for this receptor in the regulation of inflammation and energy homesotasis. Signals mainly via beta-arrestin pathway. Binding of RARRES2 activates weakly G proteins, calcium mobilization and MAPK1/MAPK3 (ERK1/2) phosphorylation too. Also acts as a receptor for TAFA1, mediates its effects on neuronal stem-cell proliferation and differentiation via the activation of ROCK/ERK and ROCK/STAT3 signaling pathway (By …

**Summary**, from NCBI Gene [2825](https://www.ncbi.nlm.nih.gov/gene/2825):

> Enables adipokinetic hormone binding activity and adipokinetic hormone receptor activity. Predicted to be involved in glucose homeostasis and neuropeptide signaling pathway. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:4463](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4463) · Entrez [2825](https://www.ncbi.nlm.nih.gov/gene/2825) · UniProt [P46091](https://www.uniprot.org/uniprotkb/P46091) · Ensembl [ENSG00000183671](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183671)

## Data

Gene col 11434: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11434); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11434, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11434]; `tensor/DDL_lfc|DDL_z.npy` [11434]; `embed/gene_vectors.npy` [11434]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11434 or target_col == 11434). Every well: [[CMKLR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CMKLR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
