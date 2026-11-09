---
symbol: "FLT3LG"
type: "gene"
col: 1628
ensembl_id: "ENSG00000090554"
name: "fms related receptor tyrosine kinase 3 ligand"
location: "19q13.33"
module: 70
arm: "+"
pooled_cpm: 3.25
n_lines_expressing: 48
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# FLT3LG

*fms related receptor tyrosine kinase 3 ligand* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.15× (z +7.0, q 1e-09, up in 23 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.574× (z -5.1, q 2e-04, down in 21 of 44 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (HS-578T 0.0696×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.238×); [[Panobinostat (drug)]] 0.5 µM in 1 line (A-172 0.147×; ⚠ cell-cycle shift, explains ~29% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HS-578T 0.213×); [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM in 1 line (Panc 03.27 0.0763×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APOL3]] (+0.70, fdr 7e-06), [[PARP10]] (+0.68, fdr 7e-06), [[PSME2]] (+0.66, fdr 7e-06); moves opposite to [[LDHB]] (-0.58, fdr 1e-05), [[ITGB1]] (-0.58, fdr 1e-05), [[IPO7]] (-0.55, fdr 1e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1628.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.15×** | +7.0 | 1e-09 | 23/42 (PANC-1, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +5.6 | 5e-06 | 9/18 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +5.5 | 6e-06 | 14/34 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +5.0 | 6e-05 | 12/26 (PANC-1, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +4.6 | 6e-04 | 11/33 (NCI-H460, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.64×** | +4.5 | 6e-04 | 10/44 (A549, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.95×** | +4.4 | 9e-04 | 8/20 (A-172, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +4.4 | 9e-04 | 7/45 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +4.1 | 0.002 | 0/5 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.53×** | +3.9 | 0.006 | 5/31 (SW1417, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.52×** | +3.8 | 0.006 | 14/39 (A-172, A549, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.49×** | +3.7 | 0.011 | 4/16 (HS-578T, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.014 | 9/33 (A549, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.68×** | +3.4 | 0.028 | 6/32 (H4, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.032 | 7/30 (HS-578T, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Pemigatinib (drug)]] 0.05 µM |  | **1.41×** | +3.0 | 0.091 | 3/37 (HS-578T, NCI-H1792, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1628.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (HS-578T 0.0696×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.238×); [[Panobinostat (drug)]] 0.5 µM in 1 line (A-172 0.147×; ⚠ cell-cycle shift, explains ~29% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HS-578T 0.213×); [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM in 1 line (Panc 03.27 0.0763×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.574×** | -5.1 | 2e-04 | 21/44 (HS-578T, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.607×** | -4.6 | 0.001 | 15/43 (HS-578T, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.650×** | -3.9 | 0.015 | 13/42 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | 0.697× | -3.3 | 0.11 | 9/42 (HEC-1-A, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.503× | -3.3 | 0.11 | 11/38 (HS-578T, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1628. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 10.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -10.8) |
| [[HS-578T (line)]] | alt | 12.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0696× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 4.58 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.0763× (z -8.6) |
| [[SW1417 (line)]] | alt | 4.31 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0811× (z -8.5) |
| [[A-427 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.828 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.767 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.766 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1628), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APOL3]] | +0.70 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[PARP10]] | +0.68 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[PSME2]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[PSMB9]] | +0.64 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[HLA-B]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[BTN2A1]] | +0.64 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[APOBEC3F]] | +0.63 | +0.45 / +0.75 | both halves | 3e-05 |  |
| [[DHX58]] | +0.63 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[CCL5]] | +0.63 | +0.58 / +0.59 | both halves | 7e-06 | STRING 579 |
| [[OGFR]] | +0.62 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[TRIM5]] | +0.62 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[ISG15]] | +0.62 | +0.57 / +0.66 | both halves | 1e-05 | STRING 578 |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LDHB]] | -0.58 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[ITGB1]] | -0.58 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[IPO7]] | -0.55 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[ASPH]] | -0.53 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[HSPD1]] | -0.53 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[PRKDC]] | -0.52 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[BLTP2]] | -0.52 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[OPA1]] | -0.52 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[LRPPRC]] | -0.51 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[LRBA]] | -0.51 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[GGCT]] | -0.51 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[CORO1C]] | -0.50 | -0.47 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MR1]] | B | MR1 activity raises FLT3LG's level | lines that do not express MR1 (5) vs lines expressing it (45) | 1.70× lower at baseline in the lines without MR1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: GGT7, AGK, TCTN1 |
| [[HDAC6]] | B | HDAC6 activity raises FLT3LG's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LMO2]] | B | LMO2 activity raises FLT3LG's level | lines that do not express LMO2 (24) vs lines expressing it (26) | 1.49× lower at baseline in the lines without LMO2 | 0.046 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent |
| [[SLC2A6]] | B | SLC2A6 activity raises FLT3LG's level | lines that do not express SLC2A6 (6) vs lines expressing it (44) | 1.42× lower at baseline in the lines without SLC2A6 | 0.068 | ⚠ within organs, on part of the lines; also absent: GFOD1, SOAT1, RGS9; maybe low, not absent |
| [[IL32]] | B | IL32 activity raises FLT3LG's level | lines that do not express IL32 (18) vs lines expressing it (32) | 1.50× lower at baseline in the lines without IL32 | 0.085 | ⚠ within organs, on part of the lines; also absent: PODXL, APOL1, F3 |
| [[IDO1]] | B | IDO1 activity raises FLT3LG's level | lines that do not express IDO1 (28) vs lines expressing it (22) | 1.42× lower at baseline in the lines without IDO1 | 0.089 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, DKK3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.648). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.7, 50.6); signed map (63.5, 28.4). **Vector** length 55.6, 7.62% of its response variance represented; |z| ≥ 3 in 987 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Antigen processing-Cross presentation* (reactome, mean cos +0.53 to 14); *Interferon gamma signaling* (reactome, mean cos +0.52 to 13); *Endosomal/Vacuolar pathway* (reactome, mean cos +0.52 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.4 | +5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.8 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.7 | +2.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.0 | -4.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.7 | -3.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.7 | -0.5 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.6 | -2.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | fms related receptor tyrosine kinase 3 ligand |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,474,207-49,486,231 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Receptor ligands |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 25 pathways, smallest: FLT3 signaling through SRC family kinases; FLT3 signaling by CBL mutants; STAT5 Activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P49771](https://www.uniprot.org/uniprotkb/P49771) (Fms-related tyrosine kinase 3 ligand):

> Stimulates the proliferation of early hematopoietic cells by activating FLT3. Synergizes well with a number of other colony stimulating factors and interleukins. Required for the development of B cells, and dendritic cells (DCs).

**Summary**, from NCBI Gene [2323](https://www.ncbi.nlm.nih.gov/gene/2323):

> Dendritic cells (DCs) provide the key link between innate and adaptive immunity by recognizing pathogens and priming pathogen-specific immune responses. FLT3LG controls the development of DCs and is particularly important for plasmacytoid DCs and CD8 (see MIM 186910)-positive classical DCs and their CD103 (ITGAE; MIM 604682)-positive tissue counterparts (summary by Sathaliyawala et al., 2010 [PubMed 20933441]).[supplied by OMIM, Jan 2011]

**Accessions** — [HGNC:3766](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3766) · Entrez [2323](https://www.ncbi.nlm.nih.gov/gene/2323) · UniProt [P49771](https://www.uniprot.org/uniprotkb/P49771) · Ensembl [ENSG00000090554](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090554)

## Data

Gene col 1628: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1628); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1628, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1628]; `tensor/DDL_lfc|DDL_z.npy` [1628]; `embed/gene_vectors.npy` [1628]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1628 or target_col == 1628). Every well: [[FLT3LG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FLT3LG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
