---
symbol: "TRPM2-AS"
type: "gene"
col: 13731
ensembl_id: "ENSG00000230061"
name: "TRPM2 antisense RNA"
location: "21q22.3"
module: 27
arm: "+"
pooled_cpm: 2.86
n_lines_expressing: 21
n_dd_up: 16
n_dd_down: 8
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 17
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# TRPM2-AS

*TRPM2 antisense RNA* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.19× (z +11.4, q 2e-27, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Thymol (drug)]] 0.5 µM: 1.61× (z +3.5, q 0.040, up in 2 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.399× (z -6.6, q 2e-08, down in 18 of 19 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.390× (z -6.5, q 2e-08, down in 18 of 19 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02050]] (+0.65, fdr 1e-05), [[DLX6-AS1]] (+0.59, fdr 1e-05), [[CIART]] (+0.58, fdr 1e-05); moves opposite to [[LAMA4]] (-0.38, fdr 5e-04), [[MXRA5]] (-0.37, fdr 5e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NIHCOLE]] → it (grade C ⚠); 17 go from it, the strongest it → [[RPH3AL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13731.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.19×** | +11.4 | 2e-27 | 1/1 (HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.07×** | +7.5 | 2e-11 | 1/6 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.60×** | +6.6 | 9e-09 | 0/7 | two highest doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.30×** | +6.0 | 3e-07 | 1/7 (LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.99×** | +5.0 | 8e-05 | 0/12 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +4.0 | 0.005 | 1/15 (BT-474) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.61×** | +3.5 | 0.040 | 2/12 (SW480, SHP-77) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.95×** | +3.5 | 0.040 | 3/10 (NCI-H1792, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.60×** | +3.4 | 0.043 | 3/12 (SW480, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.34×** | +3.2 | 0.073 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Imiquimod (maleate) (drug)]] 0.5 µM |  | **1.55×** | +3.2 | 0.073 | 1/17 (SNU-1) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.58×** | +3.2 | 0.073 | 2/15 (BT-474, KATO III) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +3.1 | 0.078 | 0/13 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.53×** | +3.1 | 0.080 | 6/18 (NCI-H23, BT-474, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.35×** | +3.0 | 0.087 | 5/19 (BT-474, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.091 | 0/19 | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13731.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.399×** | -6.6 | 2e-08 | 18/19 (COLO 205, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.390×** | -6.5 | 2e-08 | 18/19 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.417×** | -6.3 | 7e-08 | 16/19 (SHP-77, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.513×** | -4.8 | 2e-04 | 16/19 (NCI-H23, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.586×** | -3.8 | 0.015 | 10/19 (SNU-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.592×** | -3.8 | 0.016 | 5/19 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.609×** | -3.6 | 0.030 | 14/19 (NCI-H23, HCT15, …) | inconsistent across doses | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.611×** | -3.5 | 0.030 | 16/17 (HEC-1-A, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | 0.444× | -3.0 | 0.14 | 4/19 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13731. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 15.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0317× (z -20.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0934× (z -9.8) |
| [[SW480 (line)]] | alt | 5.97 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -13.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 15.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0922× (z -14.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0914× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 10.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0852× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -10.3) |
| [[A-427 (line)]] | wt | 11.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0452× (z -14.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 5.27 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0428× (z -9.7) |
| [[HCT15 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0636× (z -9.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 9.66 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -8.5) |
| [[SNU-1 (line)]] | wt | 6.95 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0485× (z -8.6) |
| [[A-172 (line)]] | wt | 0.241 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.202 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.264 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.218 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.209 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.343 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.294 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.206 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.264 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.324 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.335 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.203 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.262 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.325 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.172 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.201 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.188 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.196 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.183 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.248 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.265 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.523 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.228 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.324 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13731), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02050]] | +0.65 | +0.62 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[DLX6-AS1]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 | same gene group |
| [[CIART]] | +0.58 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[LINC01456]] | +0.58 | +0.58 / +0.49 | both halves | 2e-05 | **novel candidate** |
| [[MIR2052HG]] | +0.56 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[LINC02253]] | +0.54 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[CAPN14]] | +0.53 | +0.55 / +0.36 | both halves | 1e-04 | **novel candidate** |
| [[DMTN]] | +0.51 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[GABRG2]] | +0.50 | +0.53 / +0.39 | both halves | 6e-05 |  |
| [[PRR36]] | +0.48 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[RIMBP2]] | +0.48 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[AP1G2]] | +0.47 | +0.49 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMA4]] | -0.38 | -0.36 / -0.23 | both halves | 5e-04 |  |
| [[MXRA5]] | -0.37 | -0.37 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NIHCOLE]] | C | NIHCOLE activity raises TRPM2-AS's level | lines that do not express NIHCOLE (22) vs lines expressing it (28) | 1.93× lower at baseline in the lines without NIHCOLE | 0.025 | ⚠ within organs, on part of the lines; also absent: RORC, TSPAN1, VIL1; co-absent with the target |
| [[LINC01748]] | C | LINC01748 activity raises TRPM2-AS's level | lines that do not express LINC01748 (34) vs lines expressing it (16) | 2.04× lower at baseline in the lines without LINC01748 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CALB1, ATP10B, CLRN3; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 9, C 8. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPH3AL]] | B | TRPM2-AS activity raises RPH3AL's level | lines that do not express TRPM2-AS (29) vs lines expressing it (21) | 2.42× lower at baseline in the lines without TRPM2-AS | 0.020 | ⚠ within organs, on part of the lines; also absent: LINC03046, KLRC2, PCK1 |
| [[PPP1CB-DT]] | B | TRPM2-AS activity raises PPP1CB-DT's level | lines that do not express TRPM2-AS (29) vs lines expressing it (21) | 1.61× lower at baseline in the lines without TRPM2-AS | 0.026 | ⚠ within organs, on part of the lines; also absent: LINC03046, KLRC2, PCK1 |
| [[CAPN14]] | B | TRPM2-AS activity raises CAPN14's level | lines that do not express TRPM2-AS (29) vs lines expressing it (21) | 1.86× lower at baseline in the lines without TRPM2-AS | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC03046, KLRC2, PCK1 |
| [[HCN3]] | B | TRPM2-AS activity raises HCN3's level | lines that do not express TRPM2-AS (29) vs lines expressing it (21) | 1.38× lower at baseline in the lines without TRPM2-AS | 0.050 | ⚠ within organs, on part of the lines; also absent: LINC03046, KLRC2, PCK1 |
| [[ADAMTS13]] | B | TRPM2-AS activity raises ADAMTS13's level | lines that do not express TRPM2-AS (29) vs lines expressing it (21) | 1.35× lower at baseline in the lines without TRPM2-AS | 0.050 | ⚠ within organs, on part of the lines; also absent: LINC03046, KLRC2, PCK1 |
| cells under [[9-ING-41 (drug)]] 0.5 µM | B | TRPM2-AS activity lowers the cells' numbers under 9-ING-41 0.5 µM (makes them more sensitive) | lines that do not express TRPM2-AS (29) vs lines expressing it (19) | the lines without TRPM2-AS: 1.22× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: LINC03046, KLRC2, PCK1 |
| cells under [[Dinaciclib (drug)]] 5 µM | B | TRPM2-AS activity lowers the cells' numbers under Dinaciclib 5 µM (makes them more sensitive) | lines that do not express TRPM2-AS (29) vs lines expressing it (19) | the lines without TRPM2-AS: 2.42× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: LINC03046, KLRC2, PCK1 |
| [[DLX6-AS1]] | B | TRPM2-AS activity raises DLX6-AS1's level | lines that do not express TRPM2-AS (29) vs lines expressing it (21) | 2.00× lower at baseline in the lines without TRPM2-AS | 0.090 | ⚠ within organs, on part of the lines; also absent: LINC03046, KLRC2, PCK1 |
| [[RDM1P5]] | B | TRPM2-AS activity raises RDM1P5's level | lines that do not express TRPM2-AS (29) vs lines expressing it (21) | 1.57× lower at baseline in the lines without TRPM2-AS | 0.098 | ⚠ within organs, on part of the lines; also absent: LINC03046, KLRC2, PCK1 |
| [[NIHCOLE]] | C | TRPM2-AS activity raises NIHCOLE's level | lines that do not express TRPM2-AS (29) vs lines expressing it (21) | 3.03× lower at baseline in the lines without TRPM2-AS | 0.012 | ⚠ within organs, on part of the lines; also absent: LINC03046, KLRC2, PCK1; co-absent with the target |
| [[LINC01748]] | C | TRPM2-AS activity raises LINC01748's level | lines that do not express TRPM2-AS (29) vs lines expressing it (21) | 2.80× lower at baseline in the lines without TRPM2-AS | 0.012 | ⚠ within organs, on part of the lines; also absent: LINC03046, KLRC2, PCK1; co-absent with the target |
| [[SMOC2]] | C | TRPM2-AS activity raises SMOC2's level | lines that do not express TRPM2-AS (29) vs lines expressing it (21) | 2.42× lower at baseline in the lines without TRPM2-AS | 0.024 | ⚠ within organs, on part of the lines; also absent: LINC03046, KLRC2, PCK1; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.507). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.7, 41.0); signed map (49.6, 35.6). **Vector** length 44.2, 9.89% of its response variance represented; |z| ≥ 3 in 522 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +7.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.0 | +5.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | -0.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +1.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.1 | +1.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -4.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -0.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -1.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | TRPM2 antisense RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 21q22.3 — chr21:44,414,588-44,425,272 (-) |
| Ensembl biotype | lncRNA |
| Also known as | TRPM2-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50758](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50758) · Entrez [101928607](https://www.ncbi.nlm.nih.gov/gene/101928607) · Ensembl [ENSG00000230061](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000230061)

## Data

Gene col 13731: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13731); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13731, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13731]; `tensor/DDL_lfc|DDL_z.npy` [13731]; `embed/gene_vectors.npy` [13731]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13731 or target_col == 13731). Every well: [[TRPM2-AS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRPM2-AS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
