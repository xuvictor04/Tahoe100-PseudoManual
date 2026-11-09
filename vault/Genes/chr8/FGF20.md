---
symbol: "FGF20"
type: "gene"
col: 1225
ensembl_id: "ENSG00000078579"
name: "fibroblast growth factor 20"
location: "8p22"
module: 27
arm: "+"
pooled_cpm: 3.83
n_lines_expressing: 9
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 24
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# FGF20

*fibroblast growth factor 20* — 8p22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.61× (z +9.4, q 3e-18, up in 0 of 4 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 2 lines (SW480 0.0382×, A-427 0.203×); [[Panobinostat (drug)]] 5 µM in 1 line (A-427 0.0872×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (A-427 0.0907×); [[Belinostat (drug)]] 5 µM in 1 line (A-427 0.121×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APCDD1]] (+0.81, fdr 7e-06), [[JAKMIP2-AS1]] (+0.78, fdr 7e-06), [[NOTUM]] (+0.74, fdr 7e-06); moves opposite to [[PASD1]] (-0.50, fdr 5e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[GPR15]] → it (grade C ⚠); 24 go from it, the strongest it → [[PSD2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1225.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.61×** | +9.4 | 3e-18 | 0/4 | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.43×** | +9.3 | 5e-18 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.84×** | +6.4 | 2e-08 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.08×** | +5.8 | 8e-07 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.06×** | +5.3 | 1e-05 | 2/6 (A-427, NCI-H23) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.00×** | +5.1 | 4e-05 | 2/6 (NCI-H23, SW1417) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +4.7 | 2e-04 | 0/5 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +4.2 | 0.002 | 0/4 | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.04×** | +4.1 | 0.002 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +4.0 | 0.003 | 0/3 | top dose only | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +3.8 | 0.006 | 0/3 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.00×** | +3.6 | 0.016 | 0/3 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.58×** | +3.5 | 0.021 | 0/3 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.0 | 0.093 | 0/3 | top dose only |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.51×** | +3.0 | 0.097 | 0/5 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1225.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 2 lines (SW480 0.0382×, A-427 0.203×); [[Panobinostat (drug)]] 5 µM in 1 line (A-427 0.0872×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (A-427 0.0907×); [[Belinostat (drug)]] 5 µM in 1 line (A-427 0.121×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mebendazole (drug)]] 5 µM |  | 0.511× | -3.4 | 0.40 | 1/6 (NCI-H23) | top dose only | position effect removed |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.530× | -3.2 | 0.40 | 0/6 | rises with dose | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1225. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 129 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0872× (z -15.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0907× (z -15.7) |
| [[SW480 (line)]] | alt | 10.8 | 0 | 5 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0382× (z -14.2) |
| [[A-172 (line)]] | wt | 0.573 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.210 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.304 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.681 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.267 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.326 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.293 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.430 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.252 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.324 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.271 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.299 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.317 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.256 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.249 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.293 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.246 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.253 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.253 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.261 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.746 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.221 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.272 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.284 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.289 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.339 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1225), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APCDD1]] | +0.81 | +0.77 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[JAKMIP2-AS1]] | +0.78 | +0.79 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[NOTUM]] | +0.74 | +0.66 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[F10]] | +0.70 | +0.62 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[AXIN2]] | +0.69 | +0.61 / +0.66 | both halves | 7e-06 | STRING 435 |
| [[ST18]] | +0.68 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[B3GAT1-DT]] | +0.67 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[HS3ST5]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[PSD2]] | +0.66 | +0.64 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[SMOC2]] | +0.66 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[SERPINF1]] | +0.65 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[CHDH]] | +0.65 | +0.60 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PASD1]] | -0.50 | -0.47 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR15]] | C | GPR15 activity raises FGF20's level | lines that do not express GPR15 (46) vs lines expressing it (4) | 6.31× lower at baseline in the lines without GPR15 | 0.007 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GCG, APOB, BMP10; co-absent with the target |
| [[LINC02050]] | C | LINC02050 activity raises FGF20's level | lines that do not express LINC02050 (37) vs lines expressing it (13) | 2.16× lower at baseline in the lines without LINC02050 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000286329, ENSG00000242828, PASD1; co-absent with the target |
| [[NKD1]] | C | NKD1 activity raises FGF20's level | lines that do not express NKD1 (34) vs lines expressing it (16) | 2.04× lower at baseline in the lines without NKD1 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000265554, VSNL1, ENSG00000213981; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 8, C 16. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSD2]] | B | FGF20 activity raises PSD2's level | lines that do not express FGF20 (41) vs lines expressing it (9) | 1.97× lower at baseline in the lines without FGF20 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, HEPHL1, GCG |
| [[MYH7B]] | B | FGF20 activity raises MYH7B's level | lines that do not express FGF20 (41) vs lines expressing it (9) | 1.72× lower at baseline in the lines without FGF20 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, HEPHL1, GCG |
| [[LINC02981]] | B | FGF20 activity raises LINC02981's level | lines that do not express FGF20 (41) vs lines expressing it (9) | 2.89× lower at baseline in the lines without FGF20 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, HEPHL1, GCG |
| [[KSR2]] | B | FGF20 activity raises KSR2's level | lines that do not express FGF20 (41) vs lines expressing it (9) | 4.29× lower at baseline in the lines without FGF20 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, HEPHL1, GCG |
| [[CFAP298-TCP10L]] | B | FGF20 activity raises CFAP298-TCP10L's level | lines that do not express FGF20 (41) vs lines expressing it (9) | 1.53× lower at baseline in the lines without FGF20 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, HEPHL1, GCG |
| [[RDM1P5]] | B | FGF20 activity raises RDM1P5's level | lines that do not express FGF20 (41) vs lines expressing it (9) | 1.56× lower at baseline in the lines without FGF20 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, HEPHL1, GCG |
| [[F10]] | B | FGF20 activity raises F10's level | lines that do not express FGF20 (41) vs lines expressing it (9) | 1.94× lower at baseline in the lines without FGF20 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, HEPHL1, GCG |
| [[LINC00173]] | B | FGF20 activity raises LINC00173's level | lines that do not express FGF20 (41) vs lines expressing it (9) | 2.58× lower at baseline in the lines without FGF20 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, HEPHL1, GCG |
| [[AXIN2]] | C | FGF20 activity raises AXIN2's level | lines that do not express FGF20 (41) vs lines expressing it (9) | 6.53× lower at baseline in the lines without FGF20 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, HEPHL1, GCG; co-absent with the target |
| [[NOTUM]] | C | FGF20 activity raises NOTUM's level | lines that do not express FGF20 (41) vs lines expressing it (9) | 5.05× lower at baseline in the lines without FGF20 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, HEPHL1, GCG; co-absent with the target |
| [[SLC30A10]] | C | FGF20 activity raises SLC30A10's level | lines that do not express FGF20 (41) vs lines expressing it (9) | 3.03× lower at baseline in the lines without FGF20 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, HEPHL1, GCG; co-absent with the target |
| [[IGFL4]] | C | FGF20 activity raises IGFL4's level | lines that do not express FGF20 (41) vs lines expressing it (9) | 3.89× lower at baseline in the lines without FGF20 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, HEPHL1, GCG; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.759). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.0, 43.2); signed map (62.3, 16.7). **Vector** length 32.5, 13.9% of its response variance represented; |z| ≥ 3 in 231 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +5.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +2.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.5 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.5 | +5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.0 | +4.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.7 | +1.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.7 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.7 | +3.5 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | +0.6 | +2.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -0.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.7 | -1.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.7 | -0.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -0.7 | -1.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.6 | -2.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.6 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -0.6 | +0.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.6 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.5 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | fibroblast growth factor 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p22 — chr8:16,992,181-17,002,345 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Fibroblast growth factor family |
| Reactome | 65 pathways, smallest: FGFR3b ligand binding and activation; Signaling by activated point mutants of FGFR1; Activated point mutants of FGFR2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NP95](https://www.uniprot.org/uniprotkb/Q9NP95) (Fibroblast growth factor 20):

> Neurotrophic factor that regulates central nervous development and function.

**Summary**, from NCBI Gene [26281](https://www.ncbi.nlm.nih.gov/gene/26281):

> The protein encoded by this gene is a member of the fibroblast growth factor family. The fibroblast growth factors possess broad mitogenic and cell survival activities, and are involved in a variety of biological processes including embryonic development, cell growth, morphogenesis, tissue repair, tumor growth and invasion. This gene product is a secreted neurotrophic factor but lacks a typical signal peptide. It is expressed in normal brain, particularly the cerebellum, and may regulate …

**Accessions** — [HGNC:3677](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3677) · Entrez [26281](https://www.ncbi.nlm.nih.gov/gene/26281) · UniProt [Q9NP95](https://www.uniprot.org/uniprotkb/Q9NP95) · Ensembl [ENSG00000078579](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078579)

## Data

Gene col 1225: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1225); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1225, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1225]; `tensor/DDL_lfc|DDL_z.npy` [1225]; `embed/gene_vectors.npy` [1225]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1225 or target_col == 1225). Every well: [[FGF20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGF20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
