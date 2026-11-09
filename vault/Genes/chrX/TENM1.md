---
symbol: "TENM1"
type: "gene"
col: 188
ensembl_id: "ENSG00000009694"
name: "teneurin transmembrane protein 1"
location: "Xq25"
module: 19
arm: "+"
pooled_cpm: 41.81
n_lines_expressing: 21
n_dd_up: 34
n_dd_down: 2
n_dd_up_clean: 26
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 19
direction_downstream: 12
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# TENM1

*teneurin transmembrane protein 1* — Xq25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.18× (z +24.2, q 0e+00, up in 13 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.654× (z -5.1, q 2e-04, down in 10 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (SHP-77 0.203×, NCI-H460 0.141×; ⚠ toxic; cell-cycle shift, explains ~39% of this change); [[Bortezomib (drug)]] 0.05 µM in 2 lines (NCI-H460 0.132×, CHP-212 0.131×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (CHP-212 0.251×, SHP-77 0.459×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0679×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01885]] (+0.69, fdr 7e-06), [[LINC01035]] (+0.68, fdr 7e-06), [[LSAMP]] (+0.68, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[LINC01885]] → it (grade C ⚠); 12 go from it, the strongest it → [[SCUBE1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 188.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.18×** | +24.2 | 0e+00 | 13/19 (HS-578T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **6.77×** | +22.9 | 0e+00 | 16/19 (A-172, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.07×** | +19.0 | 0e+00 | 17/19 (KATO III, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.37×** | +17.7 | 0e+00 | 15/19 (KATO III, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.42×** | +14.7 | 0e+00 | 13/18 (KATO III, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.13×** | +13.7 | 2e-40 | 12/18 (HS-578T, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.58×** | +11.4 | 5e-28 | 3/16 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.51×** | +11.0 | 3e-26 | 15/18 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.34×** | +10.2 | 1e-22 | 9/19 (HS-578T, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.22×** | +9.6 | 6e-20 | 15/19 (KATO III, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.29×** | +9.5 | 8e-20 | 2/14 (KATO III, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +9.3 | 8e-19 | 3/19 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +6.3 | 1e-08 | 1/15 (A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.61×** | +6.0 | 8e-08 | 11/19 (SHP-77, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.58×** | +5.3 | 5e-06 | 6/18 (NCI-H23, SK-MEL-2, …) | top dose only | composition shift; position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.45×** | +4.4 | 3e-04 | 8/18 (KATO III, HS-578T, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.42×** | +4.2 | 8e-04 | 2/18 (HS-578T, KATO III) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +4.1 | 0.001 | 6/19 (HS-578T, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.013 | 10/17 (A-172, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 188.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (SHP-77 0.203×, NCI-H460 0.141×; ⚠ toxic; cell-cycle shift, explains ~39% of this change); [[Bortezomib (drug)]] 0.05 µM in 2 lines (NCI-H460 0.132×, CHP-212 0.131×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (CHP-212 0.251×, SHP-77 0.459×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0679×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.654×** | -5.1 | 2e-04 | 10/18 (SHP-77, KATO III, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.736×** | -3.7 | 0.063 | 3/18 (SHP-77, SK-MEL-2, …) | all doses, flat |  |
| [[Methylprednisolone succinate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.758× | -3.3 | 0.14 | 0/18 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.744× | -3.3 | 0.14 | 7/17 (SHP-77, SK-MEL-2, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.766× | -3.2 | 0.15 | 1/18 (NCI-H1792) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | 0.755× | -3.1 | 0.15 | 3/18 (SK-MEL-2, RPMI-7951, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.772× | -3.1 | 0.15 | 0/19 | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 0.777× | -3.0 | 0.16 | 3/19 (NCI-H1792, NCI-H661, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 188. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 64.1 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0679× (z -16.5) |
| [[HS-578T (line)]] | alt | 94.7 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 25.4× (z +17.8) | — |
| [[KATO III (line)]] | alt | 59.7 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 27.7× (z +19.3) | — |
| [[SHP-77 (line)]] | alt | 1,230 | 3 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.83× (z +16.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.203× (z -12.4) ⚠ toxic; cell-cycle shift, explains ~39% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.277× (z -10.4) |
| [[A-172 (line)]] | wt | 15.7 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 64.3× (z +19.7) | — |
| [[SW1417 (line)]] | alt | 19.9 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 13.2× (z +12.2) | — |
| [[CHP-212 (line)]] | wt | 129 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0845× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 75.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 12.7× (z +13.5) | — |
| [[NCI-H1792 (line)]] | alt | 46.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.47× (z +14.0) | — |
| [[RPMI-7951 (line)]] | alt | 42.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 29.8× (z +12.3) | — |
| [[H4 (line)]] | wt | 88.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.213× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 17.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.11× (z +10.2) | — |
| [[A-427 (line)]] | wt | 5.29 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.50 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.06 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.76 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.15 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.58 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.46 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.78 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.06 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.24 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.66 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.34 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.48 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.37 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.94 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.88 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.19 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.34 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.57 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.29 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.15 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.48 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.14 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.95 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.90 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 188), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01885]] | +0.69 | +0.64 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[LINC01035]] | +0.68 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[LSAMP]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[CDH7]] | +0.67 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[GREM2]] | +0.66 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[PCDH15]] | +0.65 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[LINC02506]] | +0.65 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[KCNK2]] | +0.65 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[BCHE]] | +0.65 | +0.63 / +0.58 | both halves | 8e-06 | **novel candidate** |
| [[MARCHF1]] | +0.65 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[COL4A6]] | +0.64 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[ST8SIA4]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 0, C 19. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01885]] | C | LINC01885 activity raises TENM1's level | lines that do not express LINC01885 (34) vs lines expressing it (16) | 5.60× lower at baseline in the lines without LINC01885 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287598, ZNF208, LINC00383; co-absent with the target |
| [[ZNF208]] | C | ZNF208 activity raises TENM1's level | lines that do not express ZNF208 (41) vs lines expressing it (9) | 7.65× lower at baseline in the lines without ZNF208 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000234426, LINC01029, ENSG00000287598; co-absent with the target |
| [[MIR4307HG]] | C | MIR4307HG activity raises TENM1's level | lines that do not express MIR4307HG (35) vs lines expressing it (15) | 4.08× lower at baseline in the lines without MIR4307HG | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000258081, MAGEB2, LINC02438; co-absent with the target |
| [[SLITRK4]] | C | SLITRK4 activity raises TENM1's level | lines that do not express SLITRK4 (36) vs lines expressing it (14) | 3.93× lower at baseline in the lines without SLITRK4 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AJAP1, ENSG00000238054, GLP2R; co-absent with the target |
| [[BCHE]] | C | BCHE activity raises TENM1's level | lines that do not express BCHE (35) vs lines expressing it (15) | 4.86× lower at baseline in the lines without BCHE | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[UBBP4-1]] | C | UBBP4-1 activity raises TENM1's level | lines that do not express UBBP4-1 (34) vs lines expressing it (16) | 3.75× lower at baseline in the lines without UBBP4-1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000253363, MIR548XHG, ENSG00000291025; co-absent with the target |
| [[RNF17]] | C | RNF17 activity raises TENM1's level | lines that do not express RNF17 (42) vs lines expressing it (8) | 3.82× lower at baseline in the lines without RNF17 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, APOD; co-absent with the target |
| [[CPED1]] | C | CPED1 activity raises TENM1's level | lines that do not express CPED1 (24) vs lines expressing it (26) | 3.63× lower at baseline in the lines without CPED1 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CCNYL2, LINC01885, ENSG00000291032; maybe low, not absent; co-absent with the target |
| [[MARCHF1]] | C | MARCHF1 activity raises TENM1's level | lines that do not express MARCHF1 (33) vs lines expressing it (17) | 3.44× lower at baseline in the lines without MARCHF1 | 0.049 | ⚠ within organs, on part of the lines; also absent: UNC5D, DSCAM, LINC01266; maybe low, not absent; co-absent with the target |
| [[CACNA2D3]] | C | CACNA2D3 activity raises TENM1's level | lines that do not express CACNA2D3 (36) vs lines expressing it (14) | 3.18× lower at baseline in the lines without CACNA2D3 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NCAM1, LINC01287, LINC00824; co-absent with the target |
| [[NKAIN2]] | C | NKAIN2 activity raises TENM1's level | lines that do not express NKAIN2 (32) vs lines expressing it (18) | 2.59× lower at baseline in the lines without NKAIN2 | 0.054 | ⚠ within organs, on part of the lines; also absent: GREM2, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[ENPP2]] | C | ENPP2 activity raises TENM1's level | lines that do not express ENPP2 (26) vs lines expressing it (24) | 3.28× lower at baseline in the lines without ENPP2 | 0.065 | ⚠ within organs, on part of the lines; also absent: SLC16A6, ITGA4, SNTG1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 2, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCUBE1]] | B | TENM1 activity raises SCUBE1's level | lines that do not express TENM1 (29) vs lines expressing it (21) | 1.88× lower at baseline in the lines without TENM1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, MIR4307HG |
| [[NCAM2]] | B | TENM1 activity raises NCAM2's level | lines that do not express TENM1 (29) vs lines expressing it (21) | 2.58× lower at baseline in the lines without TENM1 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, MIR4307HG |
| [[LINC01885]] | C | TENM1 activity raises LINC01885's level | lines that do not express TENM1 (29) vs lines expressing it (21) | 4.47× lower at baseline in the lines without TENM1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, MIR4307HG; co-absent with the target |
| [[MIR3171HG]] | C | TENM1 activity raises MIR3171HG's level | lines that do not express TENM1 (29) vs lines expressing it (21) | 4.37× lower at baseline in the lines without TENM1 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, MIR4307HG; co-absent with the target |
| [[ADGRB3]] | C | TENM1 activity raises ADGRB3's level | lines that do not express TENM1 (29) vs lines expressing it (21) | 2.48× lower at baseline in the lines without TENM1 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, MIR4307HG; co-absent with the target |
| [[NKAIN2]] | C | TENM1 activity raises NKAIN2's level | lines that do not express TENM1 (29) vs lines expressing it (21) | 1.97× lower at baseline in the lines without TENM1 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, MIR4307HG; co-absent with the target |
| [[MARCHF1]] | C | TENM1 activity raises MARCHF1's level | lines that do not express TENM1 (29) vs lines expressing it (21) | 2.63× lower at baseline in the lines without TENM1 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, MIR4307HG; co-absent with the target |
| [[DOK6]] | C | TENM1 activity raises DOK6's level | lines that do not express TENM1 (29) vs lines expressing it (21) | 2.38× lower at baseline in the lines without TENM1 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, MIR4307HG; co-absent with the target |
| [[SLITRK4]] | C | TENM1 activity raises SLITRK4's level | lines that do not express TENM1 (29) vs lines expressing it (21) | 1.83× lower at baseline in the lines without TENM1 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, MIR4307HG; co-absent with the target |
| [[MIR4307HG]] | C | TENM1 activity raises MIR4307HG's level | lines that do not express TENM1 (29) vs lines expressing it (21) | 2.55× lower at baseline in the lines without TENM1 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, MIR4307HG; co-absent with the target |
| [[LINC01035]] | C | TENM1 activity raises LINC01035's level | lines that do not express TENM1 (29) vs lines expressing it (21) | 2.07× lower at baseline in the lines without TENM1 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, MIR4307HG; co-absent with the target |
| [[ADARB2]] | C | TENM1 activity raises ADARB2's level | lines that do not express TENM1 (29) vs lines expressing it (21) | 2.09× lower at baseline in the lines without TENM1 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, MIR4307HG; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.726). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.6, 34.4); signed map (41.6, 39.4). **Vector** length 63.5, 17.8% of its response variance represented; |z| ≥ 3 in 508 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +19.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +9.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +13.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.7 | +4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +3.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.7 | -5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.8 | -0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -0.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -2.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.8 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | teneurin transmembrane protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq25 — chrX:124,375,903-125,204,312 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TEN-M1, TEN1; previously ODZ3, TNM, ODZ1 |
| Gene groups (HGNC) | Teneurin transmembrane protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKZ4](https://www.uniprot.org/uniprotkb/Q9UKZ4) (Teneurin-1):

> Involved in neural development, regulating the establishment of proper connectivity within the nervous system. May function as a cellular signal transducer (By similarity).; [Teneurin C-terminal-associated peptide]: Plays a role in the regulation of neuroplasticity in the limbic system. Mediates a rapid reorganization of actin- and tubulin-based cytoskeleton elements with an increase in dendritic arborization and spine density formation of neurons in the hippocampus and amygdala. Induces BDNF …

**Summary**, from NCBI Gene [10178](https://www.ncbi.nlm.nih.gov/gene/10178):

> The protein encoded by this gene belongs to the tenascin family and teneurin subfamily. It is expressed in the neurons and may function as a cellular signal transducer. Several alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:8117](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8117) · Entrez [10178](https://www.ncbi.nlm.nih.gov/gene/10178) · UniProt [Q9UKZ4](https://www.uniprot.org/uniprotkb/Q9UKZ4) · Ensembl [ENSG00000009694](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000009694)

## Data

Gene col 188: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 188); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 188, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 188]; `tensor/DDL_lfc|DDL_z.npy` [188]; `embed/gene_vectors.npy` [188]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 188 or target_col == 188). Every well: [[TENM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TENM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
