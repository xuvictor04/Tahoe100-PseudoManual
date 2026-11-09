---
symbol: "LYPLAL1-DT"
type: "gene"
col: 13625
ensembl_id: "ENSG00000228063"
name: "LYPLAL1 divergent transcript"
location: "1q41"
module: 19
arm: "+"
pooled_cpm: 11.9
n_lines_expressing: 18
n_dd_up: 25
n_dd_down: 5
n_dd_up_clean: 21
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 9
direction_downstream: 11
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# LYPLAL1-DT

*LYPLAL1 divergent transcript* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.26× (z +10.2, q 1e-21, up in 3 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.95× (z +8.1, q 9e-14, up in 2 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.539× (z -5.4, q 5e-05, down in 9 of 15 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SIRLNT]] (+0.69, fdr 1e-05), [[C5orf46]] (+0.59, fdr 1e-05), [[COL4A5]] (+0.55, fdr 1e-05); moves opposite to [[NPTX2]] (-0.45, fdr 1e-04), [[PRELID2]] (-0.40, fdr 2e-04), [[RTN4RL1]] (-0.39, fdr 2e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 11 go from it, the strongest it → [[ENPEP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13625.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.26×** | +10.2 | 1e-21 | 3/9 (SW 900, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.94×** | +8.4 | 9e-15 | 1/7 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +8.1 | 9e-14 | 2/11 (NCI-H1792, C32) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.31×** | +6.6 | 4e-09 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.90×** | +6.4 | 2e-08 | 4/14 (NCI-H460, SW48, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.98×** | +6.0 | 2e-07 | 4/15 (NCI-H460, CHP-212, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **2.13×** | +5.9 | 3e-07 | 4/14 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | position effect removed |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.84×** | +5.0 | 5e-05 | 4/14 (NCI-H460, SK-MEL-2, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **1.67×** | +4.8 | 9e-05 | 5/15 (NCI-H460, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.49×** | +4.4 | 6e-04 | 3/14 (NCI-H460, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.65×** | +4.3 | 8e-04 | 3/14 (SNU-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +4.3 | 8e-04 | 5/15 (hTERT-HPNE, NCI-H1792, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **2.55×** | +4.2 | 0.001 | 1/9 (NCI-H460) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.62×** | +4.1 | 0.001 | 4/15 (NCI-H460, C32, …) | all doses, stronger at high dose | position effect removed |
| [[AZD-7648 (drug)]] 5 µM |  | **2.44×** | +4.0 | 0.002 | 1/9 (NCI-H460) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.39×** | +3.9 | 0.004 | 4/15 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.63×** | +3.8 | 0.005 | 3/13 (NCI-H460, C32, …) | all doses, stronger at high dose | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.50×** | +3.5 | 0.015 | 5/14 (NCI-H460, C32, …) | all doses, stronger at high dose | position effect removed |
| [[Alpelisib (drug)]] 5 µM |  | **2.13×** | +3.4 | 0.020 | 1/10 (NCI-H460) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13625.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.539×** | -5.4 | 5e-05 | 9/15 (NCI-H1573, HOP62, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.599×** | -4.4 | 0.003 | 10/15 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.637×** | -3.9 | 0.017 | 7/15 (NCI-H460, HS-578T, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.666×** | -3.5 | 0.062 | 6/13 (NCI-H460, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.679×** | -3.4 | 0.089 | 2/15 (C32, CHP-212) | all doses, flat | cell-cycle shift (explains ~19% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13625. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 133 | 3 | 6 (4 ⚠) | [[Trametinib (drug)]] 0.05 µM 6.55× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.0325× (z -17.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -10.3) |
| [[HOP62 (line)]] | alt | 56.1 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.84 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.74 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.03 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13625), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRLNT]] | +0.69 | +0.56 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[C5orf46]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[COL4A5]] | +0.55 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[NCKAP5]] | +0.55 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[LSAMP]] | +0.51 | +0.39 / +0.47 | both halves | 6e-05 |  |
| [[GLP2R]] | +0.51 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[EPGN]] | +0.50 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[STEAP1B-AS1]] | +0.50 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[ANXA10]] | +0.49 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[PAPPA2]] | +0.48 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[ADAM12]] | +0.47 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[ZNF804A]] | +0.47 | +0.34 / +0.45 | both halves | 1e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPTX2]] | -0.45 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[PRELID2]] | -0.40 | -0.39 / -0.31 | both halves | 2e-04 |  |
| [[RTN4RL1]] | -0.39 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[SNX8]] | -0.38 | -0.36 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 1, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers LYPLAL1-DT's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[IL6]] | C | IL6 activity raises LYPLAL1-DT's level | lines that do not express IL6 (32) vs lines expressing it (18) | 2.38× lower at baseline in the lines without IL6 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2; co-absent with the target |
| [[LINC02057]] | C | LINC02057 activity raises LYPLAL1-DT's level | lines that do not express LINC02057 (25) vs lines expressing it (25) | 1.93× lower at baseline in the lines without LINC02057 | 0.044 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6; co-absent with the target |
| [[ANXA10]] | C | ANXA10 activity raises LYPLAL1-DT's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 2.84× lower at baseline in the lines without ANXA10 | 0.045 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP; co-absent with the target |
| [[ADAM12]] | C | ADAM12 activity raises LYPLAL1-DT's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 2.41× lower at baseline in the lines without ADAM12 | 0.046 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1; co-absent with the target |
| [[STEAP1B-AS1]] | C | STEAP1B-AS1 activity raises LYPLAL1-DT's level | lines that do not express STEAP1B-AS1 (30) vs lines expressing it (20) | 2.19× lower at baseline in the lines without STEAP1B-AS1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, IL6, EFEMP1; co-absent with the target |
| [[TRPA1]] | C | TRPA1 activity raises LYPLAL1-DT's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 2.51× lower at baseline in the lines without TRPA1 | 0.064 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; co-absent with the target |
| [[C5orf46]] | C | C5orf46 activity raises LYPLAL1-DT's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 2.08× lower at baseline in the lines without C5orf46 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[NCKAP5-AS2]] | C | NCKAP5-AS2 activity raises LYPLAL1-DT's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 1.95× lower at baseline in the lines without NCKAP5-AS2 | 0.095 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 1, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENPEP]] | B | LYPLAL1-DT activity raises ENPEP's level | lines that do not express LYPLAL1-DT (32) vs lines expressing it (18) | 1.59× lower at baseline in the lines without LYPLAL1-DT | 0.057 | ⚠ within organs, on part of the lines; also absent: EBF1, ANXA10, IRF4; maybe low, not absent |
| [[TDO2]] | C | LYPLAL1-DT activity raises TDO2's level | lines that do not express LYPLAL1-DT (32) vs lines expressing it (18) | 2.35× lower at baseline in the lines without LYPLAL1-DT | 0.005 | ⚠ within organs, on part of the lines; also absent: EBF1, ANXA10, IRF4; maybe low, not absent; co-absent with the target |
| [[ADAM12]] | C | LYPLAL1-DT activity raises ADAM12's level | lines that do not express LYPLAL1-DT (32) vs lines expressing it (18) | 4.79× lower at baseline in the lines without LYPLAL1-DT | 0.018 | ⚠ within organs, on part of the lines; also absent: EBF1, ANXA10, IRF4; maybe low, not absent; co-absent with the target |
| [[IL6]] | C | LYPLAL1-DT activity raises IL6's level | lines that do not express LYPLAL1-DT (32) vs lines expressing it (18) | 5.56× lower at baseline in the lines without LYPLAL1-DT | 0.020 | ⚠ within organs, on part of the lines; also absent: EBF1, ANXA10, IRF4; maybe low, not absent; co-absent with the target |
| [[SETBP1]] | C | LYPLAL1-DT activity raises SETBP1's level | lines that do not express LYPLAL1-DT (32) vs lines expressing it (18) | 3.96× lower at baseline in the lines without LYPLAL1-DT | 0.025 | ⚠ within organs, on part of the lines; also absent: EBF1, ANXA10, IRF4; maybe low, not absent; co-absent with the target |
| [[MSC-AS1]] | C | LYPLAL1-DT activity raises MSC-AS1's level | lines that do not express LYPLAL1-DT (32) vs lines expressing it (18) | 4.78× lower at baseline in the lines without LYPLAL1-DT | 0.027 | ⚠ within organs, on part of the lines; also absent: EBF1, ANXA10, IRF4; maybe low, not absent; co-absent with the target |
| [[FBN1]] | C | LYPLAL1-DT activity raises FBN1's level | lines that do not express LYPLAL1-DT (32) vs lines expressing it (18) | 3.15× lower at baseline in the lines without LYPLAL1-DT | 0.070 | ⚠ within organs, on part of the lines; also absent: EBF1, ANXA10, IRF4; maybe low, not absent; co-absent with the target |
| [[GDNF]] | C | LYPLAL1-DT activity raises GDNF's level | lines that do not express LYPLAL1-DT (32) vs lines expressing it (18) | 2.82× lower at baseline in the lines without LYPLAL1-DT | 0.079 | ⚠ within organs, on part of the lines; also absent: EBF1, ANXA10, IRF4; maybe low, not absent; co-absent with the target |
| [[GDNF-AS1]] | C | LYPLAL1-DT activity raises GDNF-AS1's level | lines that do not express LYPLAL1-DT (32) vs lines expressing it (18) | 2.03× lower at baseline in the lines without LYPLAL1-DT | 0.083 | ⚠ within organs, on part of the lines; also absent: EBF1, ANXA10, IRF4; maybe low, not absent; co-absent with the target |
| [[STEAP1B-AS1]] | C | LYPLAL1-DT activity raises STEAP1B-AS1's level | lines that do not express LYPLAL1-DT (32) vs lines expressing it (18) | 2.56× lower at baseline in the lines without LYPLAL1-DT | 0.086 | ⚠ within organs, on part of the lines; also absent: EBF1, ANXA10, IRF4; maybe low, not absent; co-absent with the target |
| [[ANXA10]] | C | LYPLAL1-DT activity raises ANXA10's level | lines that do not express LYPLAL1-DT (32) vs lines expressing it (18) | 2.27× lower at baseline in the lines without LYPLAL1-DT | 0.099 | ⚠ within organs, on part of the lines; also absent: EBF1, ANXA10, IRF4; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.501). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.5, 32.9); signed map (39.5, 43.8). **Vector** length 44.1, 12.3% of its response variance represented; |z| ≥ 3 in 375 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +5.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.3 | +6.4 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -0.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -1.1 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.1 | -0.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.1 | -0.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | LYPLAL1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1q41 — chr1:218,976,672-219,173,961 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously LYPLAL1-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50560](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50560) · Entrez [643723](https://www.ncbi.nlm.nih.gov/gene/643723) · Ensembl [ENSG00000228063](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228063)

## Data

Gene col 13625: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13625); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13625, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13625]; `tensor/DDL_lfc|DDL_z.npy` [13625]; `embed/gene_vectors.npy` [13625]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13625 or target_col == 13625). Every well: [[LYPLAL1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LYPLAL1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
