---
symbol: "CCDC14"
type: "gene"
col: 10611
ensembl_id: "ENSG00000175455"
name: "coiled-coil domain containing 14"
location: "3q21.1"
module: 6
arm: "+"
pooled_cpm: 117.69
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 6
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CCDC14

*coiled-coil domain containing 14* — 3q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.35× (z +7.4, q 3e-11, up in 31 of 48 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 1 line (A-172 2.17×; ⚠ cell-cycle shift, would explain all of this change); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 1 line (MIA PaCa-2 2.58×; ⚠ cell-cycle shift, explains ~39% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 2.65×; ⚠ cell-cycle shift, explains ~36% of this change).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 0.511× (z -8.7, q 1e-15, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBC1D31]] (+0.69, fdr 7e-06), [[TIMELESS]] (+0.69, fdr 7e-06), [[RAD51AP1]] (+0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10611.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 1 line (A-172 2.17×; ⚠ cell-cycle shift, would explain all of this change); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 1 line (MIA PaCa-2 2.58×; ⚠ cell-cycle shift, explains ~39% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 2.65×; ⚠ cell-cycle shift, explains ~36% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.35×** | +7.4 | 3e-11 | 31/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.36×** | +7.4 | 3e-11 | 32/48 (MIA PaCa-2, SW 900, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.25×** | +5.7 | 3e-06 | 29/48 (RKO, HOP62, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.26×** | +5.6 | 3e-06 | 26/50 (SW 900, RKO, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~60% of this change | **1.22×** | +4.8 | 2e-04 | 22/47 (CFPAC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 1.18× | +4.1 | 0.004 | 18/48 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 1.18× | +4.1 | 0.004 | 19/48 (SW480, HOP62, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.1 | 0.004 | 20/47 (HS-578T, HOP62, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | 1.17× | +3.6 | 0.021 | 16/48 (LoVo, NCI-H460, …) | all doses, flat |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.11× | +3.6 | 0.021 | 5/48 (HOP62, A549, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.14× | +3.3 | 0.057 | 11/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | 1.14× | +3.2 | 0.066 | 19/49 (LS 180, HT-29, …) | two highest doses | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.084 | 14/48 (MIA PaCa-2, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10611.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.511×** | -8.7 | 1e-15 | 41/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.520×** | -8.5 | 4e-15 | 41/49 (PANC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.923× | -6.9 | 1e-09 | 1/50 (SW 1088) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.804×** | -5.4 | 8e-06 | 23/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.812×** | -5.2 | 3e-05 | 23/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.813×** | -5.1 | 3e-05 | 25/48 (H4, LoVo, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.843× | -4.2 | 0.002 | 20/48 (SNU-1, HT-29, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | 0.847× | -4.1 | 0.003 | 21/48 (A-172, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.892× | -4.0 | 0.004 | 20/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.860× | -3.8 | 0.010 | 21/48 (SHP-77, C-33 A, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.863× | -3.7 | 0.013 | 17/48 (SK-MEL-2, Panc 03.27, …) | two highest doses |  |
| [[Terfenadine (drug)]] 5 µM |  | 0.909× | -3.3 | 0.040 | 3/48 (NCI-H2030, SHP-77, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.788×** | -3.1 | 0.086 | 20/48 (SHP-77, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.917× | -3.0 | 0.097 | 8/49 (SK-MEL-2, H4, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10611. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 80.0 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.461× (z -10.8) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.488× (z -10.0) |
| [[SHP-77 (line)]] | alt | 154 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.439× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.500× (z -8.7) |
| [[SW480 (line)]] | alt | 131 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.506× (z -11.9) |
| [[PANC-1 (line)]] | alt | 164 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.488× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.503× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 219 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 254 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -13.0) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 155 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -15.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 138 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 116 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.559× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 88.3 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 2.58× (z +9.6) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[A-172 (line)]] | wt | 114 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.17× (z +9.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 131 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.438× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 68.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.30× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[KATO III (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.631× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 1271 (line)]] | alt | 178 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.194× (z -9.4) |
| [[SW48 (line)]] | wt | 115 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.350× (z -8.8) |
| [[A498 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 136 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 164 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 60.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 129 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 72.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 85.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 135 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 97.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 115 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10611), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D31]] | +0.69 | +0.72 / +0.63 | both halves | 7e-06 | same gene group; STRING 746 |
| [[TIMELESS]] | +0.69 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[RAD51AP1]] | +0.68 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[FANCI]] | +0.68 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[HELLS]] | +0.65 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[CDC7]] | +0.64 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[BRCA1]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[XRCC2]] | +0.64 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[ZNF726]] | +0.64 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[DNA2]] | +0.63 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[C1orf112]] | +0.63 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[CENPK]] | +0.63 | +0.56 / +0.75 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP1]] | B | TOP1 activity lowers CCDC14's level | compounds that target TOP1: 2 of 3 raise it (Doxorubicin, Topotecan) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DSCC1]] | C | DSCC1 activity raises CCDC14's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.00× lower at baseline in the lines without DSCC1 | 0.020 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.597). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-38.4, -45.1); signed map (-39.7, -48.3). **Vector** length 120, 33.5% of its response variance represented; |z| ≥ 3 in 1,129 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Homologous DNA Pairing and Strand Exchange* (reactome, mean cos +0.51 to 18); *Defective homologous recombination repair (HRR) due to BRCA2 loss of function* (reactome, mean cos +0.52 to 16); *Diseases of DNA Double-Strand Break Repair* (reactome, mean cos +0.52 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +6.1 | +7.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +5.4 | +7.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +5.1 | +5.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.8 | +4.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | +2.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.7 | +3.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.6 | +2.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.3 | +3.3 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +3.1 | +2.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.9 | +2.8 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -6.7 | -8.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.5 | -8.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -3.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | +0.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.4 | -6.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.4 | -2.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.0 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -2.1 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | -2.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.1 — chr3:123,897,305-123,961,408 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12892, DKFZp434L1050 |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q49A88](https://www.uniprot.org/uniprotkb/Q49A88) (Coiled-coil domain-containing protein 14):

> Negatively regulates centriole duplication. Negatively regulates CEP63 and CDK2 centrosomal localization.

**Summary**, from NCBI Gene [64770](https://www.ncbi.nlm.nih.gov/gene/64770):

> Involved in protein localization to centrosome. Located in centriolar satellite. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25766](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25766) · Entrez [64770](https://www.ncbi.nlm.nih.gov/gene/64770) · UniProt [Q49A88](https://www.uniprot.org/uniprotkb/Q49A88) · Ensembl [ENSG00000175455](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175455)

## Data

Gene col 10611: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10611); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10611, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10611]; `tensor/DDL_lfc|DDL_z.npy` [10611]; `embed/gene_vectors.npy` [10611]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10611 or target_col == 10611). Every well: [[CCDC14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
