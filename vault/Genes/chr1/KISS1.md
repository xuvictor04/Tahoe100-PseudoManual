---
symbol: "KISS1"
type: "gene"
col: 9963
ensembl_id: "ENSG00000170498"
name: "KiSS-1 metastasis suppressor"
location: "1q32.1"
module: 34
arm: "+"
pooled_cpm: 7.2
n_lines_expressing: 15
n_dd_up: 12
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 8
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# KISS1

*KiSS-1 metastasis suppressor* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.51× (z +10.9, q 4e-25, up in 5 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.91× (z +5.9, q 4e-07, up in 2 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.417× (z -5.2, q 1e-04, down in 8 of 13 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (Hs 766T 0.133×, LOX-IMVI 0.131×, AsPC-1 0.119×; ⚠ cell-cycle shift, explains ~39% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LOX-IMVI 0.0701×, AsPC-1 0.0428×; ⚠ cell-cycle shift, explains ~49% of this change); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (AsPC-1 0.0307×); [[Trametinib (drug)]] 0.05 µM in 1 line (AsPC-1 0.105×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEAR1]] (+0.61, fdr 8e-06), [[SLC14A1]] (+0.60, fdr 1e-05), [[ECSCR]] (+0.57, fdr 1e-05); moves opposite to [[KRT5]] (-0.52, fdr 1e-04), [[APOOL]] (-0.42, fdr 6e-05), [[CEP126]] (-0.40, fdr 3e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MIR31HG]] → it (grade B ⚠); 8 go from it, the strongest it → [[SCHIP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9963.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.51×** | +10.9 | 4e-25 | 5/7 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.81×** | +9.7 | 9e-20 | 3/5 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.64×** | +8.8 | 3e-16 | 2/13 (HepG2/C3A, COLO 205) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.36×** | +7.2 | 1e-10 | 3/6 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.64×** | +6.2 | 6e-08 | 7/11 (SNU-423, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~23% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +5.9 | 4e-07 | 2/13 (SNU-423, Panc 03.27) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +4.5 | 7e-04 | 3/9 (SNU-423, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +4.3 | 0.001 | 2/11 (SNU-423, Panc 03.27) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.87×** | +4.0 | 0.004 | 3/8 (J82, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.79×** | +3.7 | 0.012 | 4/11 (Panc 03.27, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +3.2 | 0.065 | 2/13 (SW480, SNU-423) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.68×** | +3.2 | 0.069 | 3/11 (Panc 03.27, SNU-423, …) | top dose only |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.61× | +3.0 | 0.11 | 3/11 (LOX-IMVI, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9963.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (Hs 766T 0.133×, LOX-IMVI 0.131×, AsPC-1 0.119×; ⚠ cell-cycle shift, explains ~39% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LOX-IMVI 0.0701×, AsPC-1 0.0428×; ⚠ cell-cycle shift, explains ~49% of this change); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (AsPC-1 0.0307×); [[Trametinib (drug)]] 0.05 µM in 1 line (AsPC-1 0.105×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.417×** | -5.2 | 1e-04 | 8/13 (AsPC-1, Hs 766T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | 0.597× | -3.3 | 0.22 | 6/13 (LOX-IMVI, AsPC-1, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | 0.558× | -3.2 | 0.22 | 7/13 (Hs 766T, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Encorafenib (drug)]] 5 µM |  | 0.393× | -3.2 | 0.22 | 4/13 (LOX-IMVI, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.606× | -3.0 | 0.24 | 1/13 (NCI-H2030) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9963. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 10.3 | 0 | 4 (2 ⚠) | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0307× (z -9.9) |
| [[Hs 766T (line)]] | wt | 92.6 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -12.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[LOX-IMVI (line)]] | wt | 137 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -11.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SNU-423 (line)]] | alt | 23.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.5× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 0.686 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.459 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.000 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.623 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.509 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.901 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.691 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.736 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.523 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.931 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.763 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.517 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.620 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.485 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.592 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.889 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.939 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.908 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.795 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9963), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEAR1]] | +0.61 | +0.57 / +0.61 | both halves | 8e-06 |  |
| [[SLC14A1]] | +0.60 | +0.63 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[ECSCR]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[FST]] | +0.55 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[CNST]] | +0.54 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[PLEKHG5]] | +0.54 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[ESAM]] | +0.53 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[LINC01610]] | +0.51 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[MMP1]] | +0.50 | +0.43 / +0.54 | both halves | 4e-05 |  |
| [[ADAMTSL3]] | +0.50 | +0.38 / +0.44 | both halves | 6e-05 |  |
| [[SIGIRR]] | +0.49 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[TM4SF1]] | +0.49 | +0.44 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRT5]] | -0.52 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[APOOL]] | -0.42 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[CEP126]] | -0.40 | -0.39 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR31HG]] | B | MIR31HG activity raises KISS1's level | lines that do not express MIR31HG (16) vs lines expressing it (34) | 1.82× lower at baseline in the lines without MIR31HG | 0.082 | ⚠ within organs, on part of the lines; also absent: SMCO2, POU5F1, PLA2R1 |
| [[KRT5]] | C | KRT5 activity raises KISS1's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 3.74× lower at baseline in the lines without KRT5 | 0.013 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[SFTA1P]] | C | SFTA1P activity raises KISS1's level | lines that do not express SFTA1P (32) vs lines expressing it (18) | 2.10× lower at baseline in the lines without SFTA1P | 0.019 | ⚠ within organs, on part of the lines; also absent: SUN3, SIM1, MMRN1; co-absent with the target |
| [[DSCAM]] | C | DSCAM activity raises KISS1's level | lines that do not express DSCAM (37) vs lines expressing it (13) | 1.68× lower at baseline in the lines without DSCAM | 0.047 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent; co-absent with the target |
| [[TFF2]] | C | TFF2 activity raises KISS1's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 2.12× lower at baseline in the lines without TFF2 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31; co-absent with the target |
| [[CCDC190]] | C | CCDC190 activity raises KISS1's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 2.72× lower at baseline in the lines without CCDC190 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCHIP1]] | B | KISS1 activity strengthens SCHIP1's drug response | lines that do not express KISS1 (31) vs lines expressing it (10) | the lines without KISS1 respond 0.56× as strongly (z diff +1.83); strongest at Topotecan (hydrochloride) 5 µM: 0.64x vs 0.32x (z diff +4.1) | 0.036 | ⚠ within organs, on part of the lines; also absent: SIM1, CALB1, PSG1; target measured in part of the lines; artifact flags |
| [[ARHGAP27P1-BPTFP1-KPNA2P3]] | B | KISS1 activity raises ARHGAP27P1-BPTFP1-KPNA2P3's level | lines that do not express KISS1 (35) vs lines expressing it (15) | 1.54× lower at baseline in the lines without KISS1 | 0.057 | ⚠ within organs, on part of the lines; also absent: SIM1, CALB1, PSG1 |
| [[PLEK2]] | B | KISS1 activity raises PLEK2's level | lines that do not express KISS1 (35) vs lines expressing it (15) | 2.40× lower at baseline in the lines without KISS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: SIM1, CALB1, PSG1 |
| [[KPNA2P3]] | B | KISS1 activity raises KPNA2P3's level | lines that do not express KISS1 (35) vs lines expressing it (15) | 1.46× lower at baseline in the lines without KISS1 | 0.074 | ⚠ within organs, on part of the lines; also absent: SIM1, CALB1, PSG1 |
| [[BMAL2-AS1]] | B | KISS1 activity raises BMAL2-AS1's level | lines that do not express KISS1 (35) vs lines expressing it (15) | 1.18× lower at baseline in the lines without KISS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: SIM1, CALB1, PSG1 |
| [[PEAR1]] | C | KISS1 activity raises PEAR1's level | lines that do not express KISS1 (35) vs lines expressing it (15) | 2.02× lower at baseline in the lines without KISS1 | 0.052 | ⚠ within organs, on part of the lines; also absent: SIM1, CALB1, PSG1; co-absent with the target |
| [[PRSS3]] | C | KISS1 activity raises PRSS3's level | lines that do not express KISS1 (35) vs lines expressing it (15) | 2.13× lower at baseline in the lines without KISS1 | 0.075 | ⚠ within organs, on part of the lines; also absent: SIM1, CALB1, PSG1; co-absent with the target |
| [[KRT5]] | C | KISS1 activity raises KRT5's level | lines that do not express KISS1 (35) vs lines expressing it (15) | 2.07× lower at baseline in the lines without KISS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: SIM1, CALB1, PSG1; co-absent with the target |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.501). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.9, 18.9); signed map (16.7, 50.9). **Vector** length 40.7, 11.7% of its response variance represented; |z| ≥ 3 in 369 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +1.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.1 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.0 | +2.3 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -1.5 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -0.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -0.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.2 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -5.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.0 | -0.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -1.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.9 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | KiSS-1 metastasis suppressor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:204,190,341-204,196,491 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Neuropeptides |
| Reactome | 6 pathways, smallest: Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors); G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15726](https://www.uniprot.org/uniprotkb/Q15726) (Metastasis-suppressor KiSS-1):

> Kisspeptins are ligands for the G protein-coupled receptor KISS1R/GPR54. The hypothalamic KISS1/KISS1R signaling system plays a central role in the regulation of the hypothalamic-pituitary-gonadal reproductive axis by modulating the secretion of gonadotropin-releasing hormone (GnRH) from GnRH neurons. In these neurons, kisspeptin binding to its receptor activates G(q)-dependent signaling, leading to phospholipase C (PLC) activation, and hydrolysis of phosphatidylinositol 4,5-bisphosphate …

**Summary**, from NCBI Gene [3814](https://www.ncbi.nlm.nih.gov/gene/3814):

> This gene is a metastasis suppressor gene that suppresses metastases of melanomas and breast carcinomas without affecting tumorigenicity. The encoded protein may inhibit chemotaxis and invasion and thereby attenuate metastasis in malignant melanomas. Studies suggest a putative role in the regulation of events downstream of cell-matrix adhesion, perhaps involving cytoskeletal reorganization. A protein product of this gene, kisspeptin, stimulates gonadotropin-releasing hormone (GnRH)-induced …

**Accessions** — [HGNC:6341](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6341) · Entrez [3814](https://www.ncbi.nlm.nih.gov/gene/3814) · UniProt [Q15726](https://www.uniprot.org/uniprotkb/Q15726) · Ensembl [ENSG00000170498](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170498)

## Data

Gene col 9963: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9963); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9963, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9963]; `tensor/DDL_lfc|DDL_z.npy` [9963]; `embed/gene_vectors.npy` [9963]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9963 or target_col == 9963). Every well: [[KISS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KISS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
