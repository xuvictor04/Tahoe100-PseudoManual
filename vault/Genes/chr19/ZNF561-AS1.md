---
symbol: "ZNF561-AS1"
type: "gene"
col: 15522
ensembl_id: "ENSG00000267106"
name: "ZNF561 antisense RNA 1"
location: "19p13.2"
module: 35
arm: "+"
pooled_cpm: 10.01
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# ZNF561-AS1

*ZNF561 antisense RNA 1* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.77× (z +11.7, q 1e-28, up in 33 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.696× (z -5.3, q 8e-05, down in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H23 0.0986×, C32 0.142×; ⚠ toxic; cell-cycle shift, explains ~33% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (SNU-423 0.117×, hTERT-HPNE 0.0884×; ⚠ toxic; cell-cycle shift, explains ~30% of this change); [[Macitentan (drug)]] 5 µM in 1 line (HepG2/C3A 0.0916×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (BT-474 0.117×); [[Ligustrazine (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0880×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INKA2]] (+0.65, fdr 7e-06), [[TMLHE-AS1]] (+0.65, fdr 3e-05), [[PSMD14-DT]] (+0.64, fdr 3e-05); moves opposite to [[L2HGDH]] (-0.57, fdr 2e-04), [[THEM6]] (-0.56, fdr 1e-04), [[EFNA4]] (-0.55, fdr 2e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15522.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +11.7 | 1e-28 | 33/44 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.25×** | +10.9 | 5e-25 | 26/29 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.08×** | +10.6 | 4e-24 | 31/37 (C32, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +8.9 | 6e-17 | 17/24 (A498, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +7.5 | 8e-12 | 30/48 (A498, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.36×** | +6.3 | 4e-08 | 22/48 (LOX-IMVI, LS 180, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +5.7 | 1e-06 | 20/45 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +5.4 | 5e-06 | 20/44 (LoVo, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +4.4 | 8e-04 | 19/46 (HCT15, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.35×** | +4.3 | 1e-03 | 13/48 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.004 | 13/46 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.004 | 14/48 (A-172, RKO, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.27×** | +3.5 | 0.021 | 12/47 (A-172, LS 180, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.27×** | +3.4 | 0.026 | 12/47 (A-172, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.26×** | +3.2 | 0.047 | 14/40 (A-427, LS 180, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.091 | 5/48 (LS 180, C32, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.091 | 3/46 (SNU-423, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15522.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H23 0.0986×, C32 0.142×; ⚠ toxic; cell-cycle shift, explains ~33% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (SNU-423 0.117×, hTERT-HPNE 0.0884×; ⚠ toxic; cell-cycle shift, explains ~30% of this change); [[Macitentan (drug)]] 5 µM in 1 line (HepG2/C3A 0.0916×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (BT-474 0.117×); [[Ligustrazine (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0880×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.696×** | -5.3 | 8e-05 | 21/48 (A-427, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.780×** | -3.6 | 0.090 | 12/46 (H4, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.798× | -3.3 | 0.20 | 8/48 (PANC-1, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15522. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 8.10 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +9.8) | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 2 | — | [[Macitentan (drug)]] 5 µM 0.0916× (z -8.7) |
| [[BT-474 (line)]] | alt | 9.44 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.117× (z -8.7) |
| [[C32 (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.142× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[hTERT-HPNE (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0884× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[LoVo (line)]] | wt | 12.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 7.94 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0986× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[NCI-H460 (line)]] | wt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.117× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15522), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INKA2]] | +0.65 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[TMLHE-AS1]] | +0.65 | +0.60 / +0.44 | both halves | 3e-05 | same gene group |
| [[PSMD14-DT]] | +0.64 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[IDNK]] | +0.64 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[ACTA2]] | +0.64 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[FAM227B]] | +0.64 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[APPBP2-DT]] | +0.64 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[BDNF-AS]] | +0.64 | +0.70 / +0.42 | both halves | 4e-05 | same gene group |
| [[ATE1OSP]] | +0.63 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[ZKSCAN7-AS1]] | +0.63 | +0.71 / +0.42 | both halves | 4e-05 | same gene group |
| [[BAX]] | +0.63 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[LINC01090]] | +0.63 | +0.58 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[L2HGDH]] | -0.57 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[THEM6]] | -0.56 | -0.32 / -0.44 | both halves | 1e-04 |  |
| [[EFNA4]] | -0.55 | -0.52 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZNF561-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PINCR]] | B | PINCR activity strengthens ZNF561-AS1's drug response | lines that do not express PINCR (29) vs lines expressing it (19) | the lines without PINCR respond 0.68× as strongly (z diff +0.86); strongest at Idarubicin (hydrochloride) 5 µM: 1.38x vs 2.17x (z diff +3.3) | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[TP53]] | C | TP53 activity strengthens ZNF561-AS1's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 0.74× as strongly (z diff +0.70); strongest at Idarubicin (hydrochloride) 5 µM: 1.45x vs 2.08x (z diff +2.7) | 0.709 over the table, 0.044 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.624). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (8.0, 23.4); signed map (31.9, -5.0). **Vector** length 65.1, 9.89% of its response variance represented; |z| ≥ 3 in 885 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.5 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +10.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +8.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +4.4 | +3.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +11.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +2.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.0 | +2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +2.4 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +1.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -1.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | +0.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -1.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +0.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -2.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.3 | -0.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ZNF561 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19p13.2 — chr19:9,621,249-9,674,662 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously C19orf82 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

UniProt [K7EIQ3](https://www.uniprot.org/uniprotkb/K7EIQ3) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27613](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27613) · Entrez [284385](https://www.ncbi.nlm.nih.gov/gene/284385) · UniProt [K7EIQ3](https://www.uniprot.org/uniprotkb/K7EIQ3) · Ensembl [ENSG00000267106](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267106)

## Data

Gene col 15522: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15522); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15522, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15522]; `tensor/DDL_lfc|DDL_z.npy` [15522]; `embed/gene_vectors.npy` [15522]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15522 or target_col == 15522). Every well: [[ZNF561-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF561-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
