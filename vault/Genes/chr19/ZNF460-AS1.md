---
symbol: "ZNF460-AS1"
type: "gene"
col: 15581
ensembl_id: "ENSG00000267871"
name: "ZNF460 antisense RNA 1"
location: "19q13.43"
module: 15
arm: "+"
pooled_cpm: 5.61
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 14
n_dd_up_clean: 12
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ZNF460-AS1

*ZNF460 antisense RNA 1* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.42× (z +21.8, q 0e+00, up in 39 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.284× (z -15.7, q 0e+00, down in 35 of 45 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A53]] (+0.80, fdr 7e-06), [[GARS1-DT]] (+0.79, fdr 7e-06), [[SEC24B-AS1]] (+0.77, fdr 7e-06); moves opposite to [[STUB1]] (-0.64, fdr 8e-04, ⚠ not reproduced), [[PAFAH1B3]] (-0.62, fdr 3e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15581.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.42×** | +21.8 | 0e+00 | 39/40 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.77×** | +12.8 | 9e-35 | 36/44 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.09×** | +8.8 | 2e-16 | 22/36 (HS-578T, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.05×** | +8.6 | 9e-16 | 19/30 (KATO III, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +7.9 | 4e-13 | 22/40 (BT-474, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.65×** | +6.2 | 4e-08 | 20/46 (KATO III, SW1417, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.6 | 1e-06 | 17/47 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +4.8 | 1e-04 | 13/47 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +4.8 | 1e-04 | 13/45 (SNU-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.28×** | +4.4 | 6e-04 | 8/46 (LoVo, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +4.0 | 0.003 | 3/43 (A-172, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +4.0 | 0.003 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **1.25×** | +3.9 | 0.004 | 8/47 (BT-474, SW1417, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +3.8 | 0.007 | 13/40 (RPMI-7951, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.045 | 9/44 (KATO III, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.052 | 6/44 (C32, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15581.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.284×** | -15.7 | 0e+00 | 35/45 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.297×** | -15.2 | 0e+00 | 43/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.319×** | -14.3 | 7e-44 | 39/46 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.403×** | -10.9 | 1e-25 | 31/45 (A549, Panc 03.27, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.473×** | -9.4 | 1e-18 | 29/47 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.564×** | -6.9 | 5e-10 | 16/33 (PANC-1, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.692×** | -6.5 | 7e-09 | 20/41 (HT-29, PANC-1, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.623×** | -5.9 | 2e-07 | 19/42 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.629×** | -5.8 | 4e-07 | 21/45 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.735×** | -5.4 | 3e-06 | 22/47 (HT-29, LS 180, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.468×** | -5.0 | 4e-05 | 15/43 (PANC-1, A-172, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.508×** | -4.4 | 5e-04 | 9/44 (PANC-1, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -4.4 | 6e-04 | 18/48 (A-172, HEC-1-A, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.722×** | -4.1 | 0.002 | 13/45 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.622×** | -3.1 | 0.074 | 11/39 (C-33 A, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15581. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 12.8 | 1 | 7 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.152× (z -15.9) |
| [[HEC-1-A (line)]] | alt | 6.88 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.75× (z +12.0) | — |
| [[LoVo (line)]] | wt | 7.19 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.115× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 5.44 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.48× (z +10.7) | [[Thymol (drug)]] 0.5 µM 0.106× (z -9.0) |
| [[SW480 (line)]] | alt | 5.78 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.0953× (z -12.4) |
| [[A-172 (line)]] | wt | 10.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +9.4) | — |
| [[A498 (line)]] | wt | 3.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.90× (z +10.1) | — |
| [[A549 (line)]] | wt | 3.90 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0803× (z -8.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[BT-474 (line)]] | alt | 5.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.36× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 7.87 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.0745× (z -9.0) |
| [[COLO 205 (line)]] | alt | 8.96 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0544× (z -10.1) |
| [[HS-578T (line)]] | alt | 6.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.38× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.163× (z -9.1) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 1.94 | 0 | 1 | — | [[Panobinostat (drug)]] 0.05 µM 0.0429× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 2.99 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0362× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 4.05 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0746× (z -11.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15581), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A53]] | +0.80 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[GARS1-DT]] | +0.79 | +0.61 / +0.80 | both halves | 7e-06 |  |
| [[SEC24B-AS1]] | +0.77 | +0.60 / +0.62 | both halves | 7e-06 | same gene group |
| [[ZNF213-AS1]] | +0.77 | +0.56 / +0.69 | both halves | 1e-05 | same gene group |
| [[MFF-DT]] | +0.76 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[SAP30L-AS1]] | +0.76 | +0.64 / +0.61 | both halves | 7e-06 | same gene group |
| [[NRSN2-AS1]] | +0.75 | +0.58 / +0.69 | both halves | 8e-06 | same gene group |
| [[BCL2L2-PABPN1]] | +0.74 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[DARS1-AS1]] | +0.74 | +0.65 / +0.56 | both halves | 1e-05 | same gene group |
| [[CASS4]] | +0.73 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[ANKRD17-DT]] | +0.72 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[ZFHX2-AS1]] | +0.72 | +0.43 / +0.54 | both halves | 3e-05 | same gene group |

## Genes that move opposite

*2 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STUB1]] | -0.64 | -0.33 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[PAFAH1B3]] | -0.62 | -0.27 / -0.33 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZNF460-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SGK2]] | B | SGK2 activity raises ZNF460-AS1's level | lines that do not express SGK2 (5) vs lines expressing it (45) | 1.21× lower at baseline in the lines without SGK2 | 0.087 | ⚠ within organs, on part of the lines; also absent: IGF2BP2, ADORA2B, ARSD; maybe low, not absent |
| [[SLC13A3]] | B | SLC13A3 activity lowers ZNF460-AS1's level | lines that do not express SLC13A3 (10) vs lines expressing it (40) | 1.09× higher at baseline in the lines without SLC13A3 | 0.096 | ⚠ within organs, on part of the lines; also absent: TLN2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.861). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-3.0, 22.4); signed map (18.9, -4.1). **Vector** length 92.5, 18.7% of its response variance represented; |z| ≥ 3 in 1,130 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.5 | +21.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.6 | +12.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +8.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.2 | +8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +5.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +6.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +2.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.9 | +2.6 |
| fall | [[Belinostat (drug)]] 5 µM |  | -6.0 | -14.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.2 | -15.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.2 | -9.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.1 | -15.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.0 | -5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -3.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.3 | -1.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ZNF460 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19q13.43 — chr19:57,267,211-57,280,334 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53774](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53774) · Entrez [105372476](https://www.ncbi.nlm.nih.gov/gene/105372476) · Ensembl [ENSG00000267871](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267871)

## Data

Gene col 15581: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15581); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15581, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15581]; `tensor/DDL_lfc|DDL_z.npy` [15581]; `embed/gene_vectors.npy` [15581]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15581 or target_col == 15581). Every well: [[ZNF460-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF460-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
