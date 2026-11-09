---
symbol: "FCRLA"
type: "gene"
col: 5283
ensembl_id: "ENSG00000132185"
name: "Fc receptor like A"
location: "1q23.3"
module: 87
arm: "+"
pooled_cpm: 2.83
n_lines_expressing: 9
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 27
direction_downstream: 39
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# FCRLA

*Fc receptor like A* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 10.6× (z +11.0, q 2e-25, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.35× (z +5.8, q 8e-07, up in 0 of 6 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Diphenhydramine (drug)]] 0.05 µM: 0.402× (z -4.1, q 0.023, down in 0 of 6 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AEBP1]] (+0.79, fdr 7e-06), [[A2M]] (+0.76, fdr 3e-05), [[TF]] (+0.69, fdr 4e-05); moves opposite to [[PYDC2-AS1]] (-0.51, fdr 2e-04).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[RHOJ]] → it (grade C ⚠); 39 go from it, the strongest it → [[DIRC3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5283.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **10.6×** | +11.0 | 2e-25 | 1/1 (C32) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.46×** | +9.7 | 8e-20 | 2/2 (C32, SK-MEL-2) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.68×** | +7.8 | 2e-12 | 1/2 (C32) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.35×** | +5.8 | 8e-07 | 0/6 | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **4.45×** | +4.7 | 3e-04 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.69×** | +4.6 | 4e-04 | 0/2 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.53×** | +4.5 | 6e-04 | 1/2 (SK-MEL-2) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.56×** | +4.4 | 9e-04 | 0/2 | top dose only | cell-cycle shift (explains ~3% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.38×** | +4.2 | 0.002 | 0/3 | top dose only | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **5.08×** | +4.1 | 0.002 | 1/2 (C32) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **2.22×** | +3.6 | 0.020 | 1/3 (RPMI-7951) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +3.5 | 0.022 | 0/3 | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **3.02×** | +3.5 | 0.023 | 0/2 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **2.02×** | +3.4 | 0.027 | 0/4 | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.64×** | +3.4 | 0.027 | 3/6 (C32, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.63×** | +3.3 | 0.031 | 0/6 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5283.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.402×** | -4.1 | 0.023 | 0/6 | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.521× | -3.0 | 0.47 | 0/5 | top dose only |  |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.510× | -3.0 | 0.47 | 0/6 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5283. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.169 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.441 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.186 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.229 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.194 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.294 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.223 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.473 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.234 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.276 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.212 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.322 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.217 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.237 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.432 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.219 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.212 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.187 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.198 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.207 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.200 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.177 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.288 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.348 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.161 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.185 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.297 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.194 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.289 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.208 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.285 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.205 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5283), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AEBP1]] | +0.79 | +0.84 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[A2M]] | +0.76 | +0.79 / +0.44 | both halves | 3e-05 | **novel candidate** |
| [[TF]] | +0.69 | +0.77 / +0.40 | both halves | 4e-05 | **novel candidate** |
| [[SOX10]] | +0.68 | +0.83 / +0.30 | both halves | 2e-04 |  |
| [[LHFPL3-AS1]] | +0.65 | +0.77 / +0.31 | both halves | 2e-04 |  |
| [[COL19A1]] | +0.65 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[FZD1]] | +0.64 | +0.53 / +0.44 | both halves | 3e-05 | **novel candidate** |
| [[MIR3681HG]] | +0.64 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[TIMP3]] | +0.63 | +0.56 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[PI15]] | +0.63 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[TYR]] | +0.62 | +0.81 / +0.25 | both halves | 4e-04 |  |
| [[C10orf90]] | +0.62 | +0.72 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PYDC2-AS1]] | -0.51 | -0.55 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 0, C 27. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHOJ]] | C | RHOJ activity raises FCRLA's level | lines that do not express RHOJ (33) vs lines expressing it (17) | 2.35× lower at baseline in the lines without RHOJ | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000203434, TF, LINC02240; co-absent with the target |
| [[COL19A1]] | C | COL19A1 activity raises FCRLA's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 2.93× lower at baseline in the lines without COL19A1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7; co-absent with the target |
| [[AEBP1]] | C | AEBP1 activity raises FCRLA's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 3.74× lower at baseline in the lines without AEBP1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[LHFPL3-AS1]] | C | LHFPL3-AS1 activity raises FCRLA's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 6.79× lower at baseline in the lines without LHFPL3-AS1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1; co-absent with the target |
| [[EDNRB]] | C | EDNRB activity raises FCRLA's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 2.57× lower at baseline in the lines without EDNRB | 0.011 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[TYR]] | C | TYR activity raises FCRLA's level | lines that do not express TYR (43) vs lines expressing it (7) | 6.53× lower at baseline in the lines without TYR | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |
| [[GDNF]] | C | GDNF activity raises FCRLA's level | lines that do not express GDNF (38) vs lines expressing it (12) | 3.33× lower at baseline in the lines without GDNF | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9; co-absent with the target |
| [[SPARC]] | C | SPARC activity raises FCRLA's level | lines that do not express SPARC (34) vs lines expressing it (16) | 2.64× lower at baseline in the lines without SPARC | 0.021 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032; co-absent with the target |
| [[A2M]] | C | A2M activity raises FCRLA's level | lines that do not express A2M (42) vs lines expressing it (8) | 5.14× lower at baseline in the lines without A2M | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |
| [[FKBP9P1-1]] | C | FKBP9P1-1 activity raises FCRLA's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 2.14× lower at baseline in the lines without FKBP9P1-1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent; co-absent with the target |
| [[IHO1]] | C | IHO1 activity raises FCRLA's level | lines that do not express IHO1 (36) vs lines expressing it (14) | 2.69× lower at baseline in the lines without IHO1 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DCT, TYR, ENSG00000253474; maybe low, not absent; co-absent with the target |
| [[TDRD9]] | C | TDRD9 activity raises FCRLA's level | lines that do not express TDRD9 (37) vs lines expressing it (13) | 2.80× lower at baseline in the lines without TDRD9 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GDNF, ITIH5, DCT; co-absent with the target |

### Downstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 3, C 36. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DIRC3]] | B | FCRLA activity raises DIRC3's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 5.00× lower at baseline in the lines without FCRLA | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474 |
| [[ZCCHC24]] | B | FCRLA activity raises ZCCHC24's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 2.78× lower at baseline in the lines without FCRLA | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474 |
| [[OBI1-AS1]] | B | FCRLA activity raises OBI1-AS1's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 2.11× lower at baseline in the lines without FCRLA | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474 |
| [[C10orf90]] | C | FCRLA activity raises C10orf90's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 5.45× lower at baseline in the lines without FCRLA | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474; co-absent with the target |
| [[CSPG4]] | C | FCRLA activity raises CSPG4's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 10.66× lower at baseline in the lines without FCRLA | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474; co-absent with the target |
| [[MOXD1]] | C | FCRLA activity raises MOXD1's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 5.13× lower at baseline in the lines without FCRLA | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474; co-absent with the target |
| [[A2M]] | C | FCRLA activity raises A2M's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 5.34× lower at baseline in the lines without FCRLA | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474; co-absent with the target |
| [[GDNF]] | C | FCRLA activity raises GDNF's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 7.41× lower at baseline in the lines without FCRLA | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474; co-absent with the target |
| [[SEMA5A]] | C | FCRLA activity raises SEMA5A's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 5.70× lower at baseline in the lines without FCRLA | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474; co-absent with the target |
| [[COL1A2]] | C | FCRLA activity raises COL1A2's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 23.44× lower at baseline in the lines without FCRLA | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474; co-absent with the target |
| [[COL19A1]] | C | FCRLA activity raises COL19A1's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 5.47× lower at baseline in the lines without FCRLA | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474; co-absent with the target |
| [[LHFPL3-AS1]] | C | FCRLA activity raises LHFPL3-AS1's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 6.33× lower at baseline in the lines without FCRLA | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.749). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (52.2, 28.3); signed map (29.2, 40.0). **Vector** length 16.5, 5.16% of its response variance represented; |z| ≥ 3 in 122 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.1 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.1 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.0 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +0.9 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +0.6 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +0.6 | +3.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.4 | +1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.4 | +0.9 |
|  | [[Berbamine (drug)]] 5 µM |  | +0.4 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.5 | -0.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -0.5 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.4 | +0.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.4 | -2.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -0.4 | -0.1 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -0.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | Fc receptor like A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:161,706,972-161,714,352 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4595, FCRLc2, FCRLb, FCRLc1, FCRLd, FCRLe, FCRL, FREB; previously FCRLM1 |
| Gene groups (HGNC) | Immunoglobulin like domain containing; Fc receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L513](https://www.uniprot.org/uniprotkb/Q7L513) (Fc receptor-like A):

> May be implicated in B-cell differentiation and lymphomagenesis.

**Summary**, from NCBI Gene [84824](https://www.ncbi.nlm.nih.gov/gene/84824):

> This gene encodes a protein similar to receptors for the Fc fragment of gamma immunoglobulin (IgG). These receptors, referred to as FCGRs, mediate the destruction of IgG-coated antigens and of cells induced by antibodies. This encoded protein is selectively expressed in B cells, and may be involved in their development. This protein may also be involved in the development of lymphomas. Multiple alternatively spliced transcript variants that encode different protein isoforms have been described …

**Accessions** — [HGNC:18504](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18504) · Entrez [84824](https://www.ncbi.nlm.nih.gov/gene/84824) · UniProt [Q7L513](https://www.uniprot.org/uniprotkb/Q7L513) · Ensembl [ENSG00000132185](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132185)

## Data

Gene col 5283: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5283); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5283, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5283]; `tensor/DDL_lfc|DDL_z.npy` [5283]; `embed/gene_vectors.npy` [5283]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5283 or target_col == 5283). Every well: [[FCRLA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FCRLA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
