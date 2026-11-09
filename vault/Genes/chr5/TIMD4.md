---
symbol: "TIMD4"
type: "gene"
col: 7033
ensembl_id: "ENSG00000145850"
name: "T cell immunoglobulin and mucin domain containing 4"
location: "5q33.3"
module: 8
arm: "+"
pooled_cpm: 2.28
n_lines_expressing: 10
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 23
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# TIMD4

*T cell immunoglobulin and mucin domain containing 4* — 5q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.70× (z +11.3, q 5e-27, up in 1 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A549 0.149×, CFPAC-1 0.112×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A549 0.0704×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 1 line (A549 0.0851×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HAVCR1]] (+0.80, fdr 7e-06), [[RHEX]] (+0.77, fdr 7e-06), [[PREX2]] (+0.70, fdr 7e-06); moves opposite to [[NEFM]] (-0.41, fdr 3e-04), [[SH3PXD2A]] (-0.41, fdr 2e-04), [[SPRY4]] (-0.38, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[HAVCR1]] → it (grade C ⚠); 23 go from it, the strongest it → [[GAL3ST1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7033.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.70×** | +11.3 | 5e-27 | 1/6 (LoVo) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.05×** | +11.0 | 8e-26 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.58×** | +10.9 | 4e-25 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.02×** | +9.1 | 9e-18 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.60×** | +8.3 | 1e-14 | 1/7 (HepG2/C3A) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.95×** | +6.6 | 3e-09 | 1/6 (LoVo) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.51×** | +5.6 | 1e-06 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.46×** | +5.4 | 4e-06 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.92×** | +5.4 | 4e-06 | 1/5 (HEC-1-A) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.53×** | +4.7 | 2e-04 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.70×** | +4.2 | 0.001 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +3.9 | 0.005 | 0/5 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +3.8 | 0.007 | 0/6 | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.64×** | +3.7 | 0.009 | 6/6 (HEC-1-A, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.23×** | +3.5 | 0.017 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.3 | 0.035 | 1/7 (A498) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +3.3 | 0.035 | 0/6 | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.66×** | +3.1 | 0.060 | 0/5 | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +3.0 | 0.079 | 0/5 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.62×** | +2.9 | 0.082 | 0/5 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.68×** | +2.9 | 0.082 | 0/5 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7033.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A549 0.149×, CFPAC-1 0.112×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A549 0.0704×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 1 line (A549 0.0851×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Erlotinib (drug)]] 0.05 µM |  | 0.530× | -3.6 | 0.13 | 0/7 | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.541× | -3.5 | 0.13 | 0/7 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7033. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 21.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 3.52 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -8.9) |
| [[A-172 (line)]] | wt | 0.285 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.217 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.261 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.275 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.303 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.261 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.595 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.295 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.305 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.330 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.238 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.275 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.947 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.293 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.278 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.204 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.274 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.269 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 0.997 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.246 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.280 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.281 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.262 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.346 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.378 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.289 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.291 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.299 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.297 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7033), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HAVCR1]] | +0.80 | +0.88 / +0.65 | both halves | 7e-06 | same gene group; pathway: Dengue Virus Attachment and Entry; STRING 857 |
| [[RHEX]] | +0.77 | +0.74 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[PREX2]] | +0.70 | +0.61 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[CP]] | +0.68 | +0.59 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[POU5F1]] | +0.66 | +0.67 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[FGA]] | +0.63 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[DSCAML1]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 | same gene group |
| [[SLC4A4]] | +0.62 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[ITIH2]] | +0.58 | +0.57 / +0.45 | both halves | 3e-05 | **novel candidate** |
| [[CYP24A1]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[CD38]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[IGFBP1]] | +0.56 | +0.47 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEFM]] | -0.41 | -0.32 / -0.29 | both halves | 3e-04 |  |
| [[SH3PXD2A]] | -0.41 | -0.29 / -0.37 | both halves | 2e-04 |  |
| [[SPRY4]] | -0.38 | -0.36 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HAVCR1]] | C | HAVCR1 activity raises TIMD4's level | lines that do not express HAVCR1 (39) vs lines expressing it (11) | 3.26× lower at baseline in the lines without HAVCR1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TIMD4, RHEX, FGA; co-absent with the target |
| [[FGA]] | C | FGA activity raises TIMD4's level | lines that do not express FGA (43) vs lines expressing it (7) | 2.31× lower at baseline in the lines without FGA | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG; co-absent with the target |
| [[LINC00278]] | C | LINC00278 activity raises TIMD4's level | lines that do not express LINC00278 (32) vs lines expressing it (18) | 1.31× lower at baseline in the lines without LINC00278 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZFY, PRKY, RPS4Y1; co-absent with the target |
| [[FGG]] | C | FGG activity raises TIMD4's level | lines that do not express FGG (42) vs lines expressing it (8) | 2.03× lower at baseline in the lines without FGG | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB; co-absent with the target |
| [[FXYD2]] | C | FXYD2 activity raises TIMD4's level | lines that do not express FXYD2 (38) vs lines expressing it (12) | 1.86× lower at baseline in the lines without FXYD2 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSCAML1, ITIH2, FGA; co-absent with the target |
| [[IGFBP1]] | C | IGFBP1 activity raises TIMD4's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 1.59× lower at baseline in the lines without IGFBP1 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2; co-absent with the target |
| [[SLCO1B1]] | C | SLCO1B1 activity raises TIMD4's level | lines that do not express SLCO1B1 (28) vs lines expressing it (22) | 1.47× lower at baseline in the lines without SLCO1B1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000257062, SLCO1B3, SLCO1B3-SLCO1B7; co-absent with the target |
| [[SLCO1B3-SLCO1B7]] | C | SLCO1B3-SLCO1B7 activity raises TIMD4's level | lines that do not express SLCO1B3-SLCO1B7 (27) vs lines expressing it (23) | 1.43× lower at baseline in the lines without SLCO1B3-SLCO1B7 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000257062, SLCO1B3, SLCO1B1; co-absent with the target |
| [[POU5F1]] | C | POU5F1 activity raises TIMD4's level | lines that do not express POU5F1 (27) vs lines expressing it (23) | 1.74× lower at baseline in the lines without POU5F1 | 0.084 | ⚠ within organs, on part of the lines; also absent: P2RY2, C4BPB, UGT1A6; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 3, C 20. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GAL3ST1]] | B | TIMD4 activity raises GAL3ST1's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 2.46× lower at baseline in the lines without TIMD4 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA |
| [[KMO]] | B | TIMD4 activity raises KMO's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 1.66× lower at baseline in the lines without TIMD4 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA |
| [[CHST9]] | B | TIMD4 activity raises CHST9's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 2.31× lower at baseline in the lines without TIMD4 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA |
| [[HAVCR1]] | C | TIMD4 activity raises HAVCR1's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 6.84× lower at baseline in the lines without TIMD4 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA; co-absent with the target |
| [[POU5F1]] | C | TIMD4 activity raises POU5F1's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 7.78× lower at baseline in the lines without TIMD4 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA; co-absent with the target |
| [[LINC00278]] | C | TIMD4 activity raises LINC00278's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 3.74× lower at baseline in the lines without TIMD4 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA; co-absent with the target |
| [[SLCO1B1]] | C | TIMD4 activity raises SLCO1B1's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 2.44× lower at baseline in the lines without TIMD4 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA; co-absent with the target |
| [[FGA]] | C | TIMD4 activity raises FGA's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 4.16× lower at baseline in the lines without TIMD4 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA; co-absent with the target |
| [[SLCO1B3-SLCO1B7]] | C | TIMD4 activity raises SLCO1B3-SLCO1B7's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 3.37× lower at baseline in the lines without TIMD4 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA; co-absent with the target |
| [[DCDC2]] | C | TIMD4 activity raises DCDC2's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 5.11× lower at baseline in the lines without TIMD4 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA; co-absent with the target |
| [[IGFBP1]] | C | TIMD4 activity raises IGFBP1's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 4.76× lower at baseline in the lines without TIMD4 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA; co-absent with the target |
| [[RHEX]] | C | TIMD4 activity raises RHEX's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 5.77× lower at baseline in the lines without TIMD4 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.378). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.8, 44.4); signed map (52.0, 26.9). **Vector** length 32.9, 15.3% of its response variance represented; |z| ≥ 3 in 185 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +10.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.6 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.5 | +11.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.1 | +2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.0 | +3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.0 | +2.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.9 | -1.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -2.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.7 | -0.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.7 | -1.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.7 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | T cell immunoglobulin and mucin domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.3 — chr5:156,919,292-156,963,226 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TIM4 |
| Gene groups (HGNC) | V-set domain containing |
| Reactome | 3 pathways, smallest: Dengue Virus Attachment and Entry; Dengue Virus Infection; Viral Infection Pathways |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96H15](https://www.uniprot.org/uniprotkb/Q96H15) (T-cell immunoglobulin and mucin domain-containing protein 4):

> Phosphatidylserine receptor that plays different role in immune response including phagocytosis of apoptotic cells and T-cell regulation. Involved in efferocytosis, the process by which apoptotic cells are removed by phagocytic cells by promoting the engulfment of apoptotic cells or exogenous particles. Mechanistically, acts by securing apoptotic cells to phagocytes through direct binding to phosphatidylserine present on apoptotic cells, while other engulfment receptors such as MERTK …

**Summary**, from NCBI Gene [91937](https://www.ncbi.nlm.nih.gov/gene/91937):

> Enables phosphatidylserine binding activity. Involved in apoptotic cell clearance. Is active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25132](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25132) · Entrez [91937](https://www.ncbi.nlm.nih.gov/gene/91937) · UniProt [Q96H15](https://www.uniprot.org/uniprotkb/Q96H15) · Ensembl [ENSG00000145850](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145850)

## Data

Gene col 7033: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7033); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7033, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7033]; `tensor/DDL_lfc|DDL_z.npy` [7033]; `embed/gene_vectors.npy` [7033]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7033 or target_col == 7033). Every well: [[TIMD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIMD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
