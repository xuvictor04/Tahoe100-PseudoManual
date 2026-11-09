---
symbol: "LAPTM5"
type: "gene"
col: 8524
ensembl_id: "ENSG00000162511"
name: "lysosomal protein transmembrane 5"
location: "1p35.2"
module: 196
arm: "+"
pooled_cpm: 2.21
n_lines_expressing: 19
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 10
direction_downstream: 19
tags: ["gene", "module/196"]
generated_by: "tahoemap"
---

# LAPTM5

*lysosomal protein transmembrane 5* — 1p35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.32× (z +11.4, q 2e-27, up in 3 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.00× (z +6.3, q 4e-08, up in 0 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Trametinib (drug)]] 5 µM: 0.490× (z -4.5, q 0.003, down in 10 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HOP62 0.251×; ⚠ cell-cycle shift, explains ~31% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0676×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR4280HG]] (+0.62, fdr 1e-05), [[CACNA2D4]] (+0.61, fdr 1e-05), [[PAEP]] (+0.61, fdr 1e-05); moves opposite to [[KIF13A]] (-0.47, fdr 2e-04), [[MIR4307HG]] (-0.44, fdr 1e-04), [[RAB32]] (-0.43, fdr 6e-05).
> It is in [[Module 196]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[LINC02970]] → it (grade B ⚠); 19 go from it, the strongest it → [[PTPRU]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8524.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.32×** | +11.4 | 2e-27 | 3/4 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.65×** | +9.9 | 1e-20 | 4/6 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.32×** | +8.7 | 5e-16 | 3/6 (RPMI-7951, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +6.3 | 4e-08 | 0/10 | top dose only | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.45×** | +5.8 | 9e-07 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.81×** | +5.4 | 8e-06 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.18×** | +4.8 | 1e-04 | 1/8 (Hs 766T) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.11×** | +4.8 | 1e-04 | 0/10 | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.51×** | +4.2 | 0.002 | 1/3 (HOP62) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +4.1 | 0.003 | 3/15 (SW480, Hs 766T, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.86×** | +4.0 | 0.003 | 3/9 (SW480, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +3.5 | 0.026 | 1/9 (NCI-H1792) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Trifluridine (drug)]] 5 µM |  | **1.46×** | +3.4 | 0.029 | 2/14 (HOP62, NCI-H2347) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +3.4 | 0.029 | 0/14 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.61×** | +3.2 | 0.047 | 1/2 (HOP62) | rises with dose | noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.61×** | +3.0 | 0.079 | 0/10 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.59×** | +3.0 | 0.095 | 1/10 (SW480) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8524.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HOP62 0.251×; ⚠ cell-cycle shift, explains ~31% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0676×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.490×** | -4.5 | 0.003 | 10/15 (NCI-H1792, HOP62, …) | top dose only | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.542×** | -3.7 | 0.063 | 4/15 (SK-MEL-2, HEC-1-A, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.384× | -3.2 | 0.17 | 6/15 (HOP62, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.608× | -3.2 | 0.17 | 6/15 (SK-MEL-2, Hs 766T, …) | inconsistent across doses |  |
| [[Vemurafenib (drug)]] 5 µM |  | 0.402× | -3.1 | 0.22 | 1/14 (NCI-H1792) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8524. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 29.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -11.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0676× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.279 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.159 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.174 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.500 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.290 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.163 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.147 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.174 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.257 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.343 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.212 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.200 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.240 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.248 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.140 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.365 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.216 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.261 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.180 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.203 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.794 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.255 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.497 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.724 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.155 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.182 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.206 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.212 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8524), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR4280HG]] | +0.62 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[CACNA2D4]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[PAEP]] | +0.61 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[PTGS1]] | +0.61 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[ETV1]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[STMN3]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[LINC02813]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[LINC01844]] | +0.58 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[MILR1]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[TSPAN4]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[SPRY4]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[IL19]] | +0.55 | +0.44 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF13A]] | -0.47 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[MIR4307HG]] | -0.44 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[RAB32]] | -0.43 | -0.39 / -0.46 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 3, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02970]] | B | LINC02970 activity raises LAPTM5's level | lines that do not express LINC02970 (24) vs lines expressing it (26) | 1.62× lower at baseline in the lines without LINC02970 | 0.036 | ⚠ within organs, on part of the lines; also absent: TOX, MXRA5, ENSG00000255595 |
| [[CCDC33]] | B | CCDC33 activity raises LAPTM5's level | lines that do not express CCDC33 (24) vs lines expressing it (26) | 1.58× lower at baseline in the lines without CCDC33 | 0.045 | ⚠ within organs, on part of the lines; also absent: STRA6, ENSG00000261543, KLF8 |
| [[TGFA]] | B | TGFA activity raises LAPTM5's level | lines that do not express TGFA (17) vs lines expressing it (33) | 1.54× lower at baseline in the lines without TGFA | 0.078 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[NES]] | C | NES activity raises LAPTM5's level | lines that do not express NES (26) vs lines expressing it (24) | 2.07× lower at baseline in the lines without NES | 0.051 | ⚠ within organs, on part of the lines; also absent: LAPTM5, CSPG4, ENSG00000230490; co-absent with the target |
| [[MIR3681HG]] | C | MIR3681HG activity raises LAPTM5's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 1.90× lower at baseline in the lines without MIR3681HG | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent; co-absent with the target |
| [[SHROOM4]] | C | SHROOM4 activity raises LAPTM5's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 1.95× lower at baseline in the lines without SHROOM4 | 0.057 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539; co-absent with the target |
| [[MANCR]] | C | MANCR activity raises LAPTM5's level | lines that do not express MANCR (20) vs lines expressing it (30) | 1.79× lower at baseline in the lines without MANCR | 0.066 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2; co-absent with the target |
| [[STRA6]] | C | STRA6 activity raises LAPTM5's level | lines that do not express STRA6 (26) vs lines expressing it (24) | 1.70× lower at baseline in the lines without STRA6 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000261543, CCDC33, ACKR3; co-absent with the target |
| [[LINC02813]] | C | LINC02813 activity raises LAPTM5's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 2.03× lower at baseline in the lines without LINC02813 | 0.094 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN; co-absent with the target |
| [[MILR1]] | C | MILR1 activity raises LAPTM5's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 1.79× lower at baseline in the lines without MILR1 | 0.095 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 8, C 11. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRU]] | B | LAPTM5 activity raises PTPRU's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 1.84× lower at baseline in the lines without LAPTM5 | 0.023 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2 |
| [[RAB17]] | B | LAPTM5 activity raises RAB17's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 1.88× lower at baseline in the lines without LAPTM5 | 0.027 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2 |
| [[TGFA]] | B | LAPTM5 activity raises TGFA's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 1.99× lower at baseline in the lines without LAPTM5 | 0.032 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2 |
| [[HPCAL1]] | B | LAPTM5 activity raises HPCAL1's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 1.78× lower at baseline in the lines without LAPTM5 | 0.045 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2 |
| [[PLP2]] | B | LAPTM5 activity raises PLP2's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 1.71× lower at baseline in the lines without LAPTM5 | 0.062 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2 |
| [[SH3TC2]] | B | LAPTM5 activity raises SH3TC2's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 2.16× lower at baseline in the lines without LAPTM5 | 0.068 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2 |
| [[GALNT18]] | B | LAPTM5 activity raises GALNT18's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 2.15× lower at baseline in the lines without LAPTM5 | 0.088 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2 |
| [[ANKH]] | B | LAPTM5 activity raises ANKH's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 1.53× lower at baseline in the lines without LAPTM5 | 0.099 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2 |
| [[MILR1]] | C | LAPTM5 activity raises MILR1's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 2.27× lower at baseline in the lines without LAPTM5 | 0.006 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2; co-absent with the target |
| [[LOXL4]] | C | LAPTM5 activity raises LOXL4's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 2.73× lower at baseline in the lines without LAPTM5 | 0.019 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2; co-absent with the target |
| [[MANCR]] | C | LAPTM5 activity raises MANCR's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 2.31× lower at baseline in the lines without LAPTM5 | 0.033 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2; co-absent with the target |
| [[SHROOM4]] | C | LAPTM5 activity raises SHROOM4's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 2.67× lower at baseline in the lines without LAPTM5 | 0.039 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2; co-absent with the target |

## Where it sits

- **Module**: [[Module 196]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.683). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (51.2, 8.2); signed map (9.4, 52.3). **Vector** length 32.0, 7.75% of its response variance represented; |z| ≥ 3 in 322 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +8.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.6 | +9.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.2 | +1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.6 | +0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.6 | +2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +0.6 | +1.4 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +0.4 | +0.6 |
| fall | [[Trametinib (drug)]] 5 µM |  | -1.7 | -4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.4 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.3 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.3 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | lysosomal protein transmembrane 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.2 — chr1:30,732,469-30,757,774 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Lysosomal protein transmembrane family |
| Hallmark sets | KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13571](https://www.uniprot.org/uniprotkb/Q13571) (Lysosomal-associated transmembrane protein 5):

> May have a special functional role during embryogenesis and in adult hematopoietic cells.

**Summary**, from NCBI Gene [7805](https://www.ncbi.nlm.nih.gov/gene/7805):

> This gene encodes a transmembrane receptor that is associated with lysosomes. The encoded protein, also known as E3 protein, may play a role in hematopoiesis. [provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:29612](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29612) · Entrez [7805](https://www.ncbi.nlm.nih.gov/gene/7805) · UniProt [Q13571](https://www.uniprot.org/uniprotkb/Q13571) · Ensembl [ENSG00000162511](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162511)

## Data

Gene col 8524: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8524); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8524, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8524]; `tensor/DDL_lfc|DDL_z.npy` [8524]; `embed/gene_vectors.npy` [8524]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8524 or target_col == 8524). Every well: [[LAPTM5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAPTM5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
