---
symbol: "ZBTB26"
type: "gene"
col: 10109
ensembl_id: "ENSG00000171448"
name: "zinc finger and BTB domain containing 26"
location: "9q33.2"
module: 15
arm: "+"
pooled_cpm: 12.67
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 13
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ZBTB26

*zinc finger and BTB domain containing 26* — 9q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.54× (z +9.2, q 2e-17, up in 34 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.89× (z +8.3, q 2e-14, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.575× (z -8.3, q 4e-14, down in 31 of 47 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.646× (z -6.1, q 2e-07, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DYNLT2]] (+0.72, fdr 1e-05), [[SPRYD4]] (+0.70, fdr 4e-05), [[HEXA]] (+0.69, fdr 7e-06); moves opposite to [[ZSWIM6]] (-0.56, fdr 2e-05), [[ADARB1]] (-0.52, fdr 6e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAFIP]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Hesperidin (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10109.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.54×** | +9.2 | 2e-17 | 34/48 (NCI-H460, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **2.89×** | +8.3 | 2e-14 | 33/48 (RKO, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +6.9 | 1e-09 | 15/31 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +5.5 | 4e-06 | 19/42 (NCI-H2030, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +5.1 | 4e-05 | 18/48 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.81×** | +4.7 | 3e-04 | 16/44 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.34×** | +4.4 | 9e-04 | 17/47 (SW480, RKO, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.029 | 15/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.3 | 0.051 | 0/48 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.079 | 12/47 (NCI-H1573, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.23×** | +3.1 | 0.100 | 14/46 (NCI-H1573, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10109.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.575×** | -8.3 | 4e-14 | 31/47 (SW480, NCI-H2347, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.615×** | -7.3 | 7e-11 | 27/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.625×** | -7.1 | 3e-10 | 28/48 (SW480, SW1417, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.646×** | -6.1 | 2e-07 | 24/48 (SW480, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.714×** | -5.1 | 4e-05 | 19/46 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.800×** | -4.7 | 2e-04 | 21/48 (BT-474, SHP-77, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.741×** | -4.5 | 5e-04 | 20/46 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **0.735×** | -4.5 | 5e-04 | 18/43 (A-427, NCI-H2347, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.735×** | -4.4 | 5e-04 | 19/46 (SW480, HCT15, …) | two highest doses | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | **0.750×** | -4.2 | 0.002 | 12/24 (NCI-H460, A-172, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.797×** | -3.4 | 0.033 | 15/38 (SHP-77, BT-474, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.802×** | -3.3 | 0.043 | 15/46 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.806×** | -3.3 | 0.050 | 8/47 (AN3 CA, CHP-212, …) | inconsistent across doses |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.868× | -3.0 | 0.10 | 6/48 (NCI-H1573, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10109. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 18.5 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.67× (z +9.2) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.387× (z -9.3) ⚠ cell-cycle shift, explains ~49% of this change |
| [[A-172 (line)]] | wt | 14.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[A-427 (line)]] | wt | 8.93 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.139× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~44% of this change |
| [[A549 (line)]] | wt | 13.1 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.205× (z -9.4) |
| [[BT-474 (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[NCI-H1792 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[NCI-H2347 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 14.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[SHP-77 (line)]] | alt | 24.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 16.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -9.0) ⚠ cell-cycle shift, explains ~75% of this change |
| [[SNU-423 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -10.5) ⚠ cell-cycle shift, explains ~58% of this change |
| [[A498 (line)]] | wt | 9.85 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10109), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYNLT2]] | +0.72 | +0.49 / +0.71 | both halves | 1e-05 |  |
| [[SPRYD4]] | +0.70 | +0.41 / +0.68 | both halves | 4e-05 |  |
| [[HEXA]] | +0.69 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[LINC00115]] | +0.69 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[ANKRD42-DT]] | +0.68 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[C1D]] | +0.67 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[MED28]] | +0.67 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[VPS13B-DT]] | +0.66 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[ZNF117]] | +0.65 | +0.37 / +0.65 | both halves | 8e-05 | same gene group |
| [[WASH2P-1]] | +0.65 | +0.37 / +0.57 | both halves | 7e-05 |  |
| [[ZNF12]] | +0.64 | +0.52 / +0.69 | both halves | 1e-05 | same gene group |
| [[SDHD]] | +0.64 | +0.52 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSWIM6]] | -0.56 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[ADARB1]] | -0.52 | -0.39 / -0.41 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAFIP]] | B | MAFIP activity raises ZBTB26's level | lines that do not express MAFIP (7) vs lines expressing it (43) | 1.28× lower at baseline in the lines without MAFIP | 0.071 | ⚠ within organs, on part of the lines |
| [[ZNF234]] | C | ZNF234 activity raises ZBTB26's level | lines that do not express ZNF234 (4) vs lines expressing it (46) | 1.31× lower at baseline in the lines without ZNF234 | 0.083 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF222, ZNF551, ZNF264 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Hesperidin (drug)]] 0.05 µM | C | ZBTB26's natural level lowers the cells' numbers under Hesperidin 0.05 µM (makes them more sensitive) | ZBTB26's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.63 | 0.403 over the table, 0.089 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.612). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-7.1, 23.0); signed map (-10.6, -18.7). **Vector** length 74.6, 12.8% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +8.1 | +9.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.3 | +5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +2.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +4.3 | +4.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +4.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.2 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +0.4 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | -3.1 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.7 | -5.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -2.5 | -4.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.3 | -6.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -1.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 26 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.2 — chr9:122,915,566-122,931,512 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ZNF481 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCK0](https://www.uniprot.org/uniprotkb/Q9HCK0) (Zinc finger and BTB domain-containing protein 26):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [57684](https://www.ncbi.nlm.nih.gov/gene/57684):

> Enables identical protein binding activity and sequence-specific double-stranded DNA binding activity. Predicted to be involved in negative regulation of transcription by RNA polymerase II; regulation of cytokine production; and regulation of immune system process. Predicted to be located in nucleus. Predicted to be active in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23383](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23383) · Entrez [57684](https://www.ncbi.nlm.nih.gov/gene/57684) · UniProt [Q9HCK0](https://www.uniprot.org/uniprotkb/Q9HCK0) · Ensembl [ENSG00000171448](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171448)

## Data

Gene col 10109: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10109); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10109, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10109]; `tensor/DDL_lfc|DDL_z.npy` [10109]; `embed/gene_vectors.npy` [10109]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10109 or target_col == 10109). Every well: [[ZBTB26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
