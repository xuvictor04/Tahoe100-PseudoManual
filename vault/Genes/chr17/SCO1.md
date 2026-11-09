---
symbol: "SCO1"
type: "gene"
col: 5405
ensembl_id: "ENSG00000133028"
name: "synthesis of cytochrome C oxidase 1"
location: "17p13.1"
module: 1
arm: "+"
pooled_cpm: 22.55
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# SCO1

*synthesis of cytochrome C oxidase 1* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.86× (z +11.7, q 9e-29, up in 38 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.352×); [[Dinaciclib (drug)]] 5 µM in 1 line (SW 900 0.195×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (CHP-212 0.116×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UTP15]] (+0.79, fdr 7e-06), [[RRS1]] (+0.75, fdr 7e-06), [[LTV1]] (+0.75, fdr 7e-06); moves opposite to [[PHF1]] (-0.67, fdr 7e-06), [[SIRT2]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5405.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.86×** | +11.7 | 9e-29 | 38/47 (A549, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +10.6 | 1e-23 | 42/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.72×** | +10.3 | 2e-22 | 37/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.68×** | +9.0 | 2e-17 | 26/39 (SNU-423, SW480, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.58×** | +8.6 | 6e-16 | 35/47 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +7.8 | 5e-13 | 30/48 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.34×** | +7.7 | 9e-13 | 30/48 (NCI-H1792, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +7.4 | 1e-11 | 28/48 (MIA PaCa-2, LoVo, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.47×** | +7.3 | 2e-11 | 26/48 (LS 180, SW 900, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.09×** | +7.2 | 2e-11 | 23/46 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +6.8 | 7e-10 | 23/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.94×** | +6.5 | 3e-09 | 22/48 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.39×** | +6.2 | 3e-08 | 23/48 (LS 180, SW 900, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +5.9 | 2e-07 | 24/47 (A549, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **1.36×** | +5.8 | 3e-07 | 20/43 (NCI-H23, LS 180, …) | all doses, flat | composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.62×** | +4.7 | 6e-05 | 15/47 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.29×** | +4.4 | 2e-04 | 14/47 (NCI-H460, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.54×** | +4.3 | 5e-04 | 14/46 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.48×** | +3.9 | 0.002 | 11/48 (A498, A549, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.003 | 10/47 (PANC-1, A498, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.006 | 13/47 (A498, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.011 | 13/48 (A-172, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5405.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.352×); [[Dinaciclib (drug)]] 5 µM in 1 line (SW 900 0.195×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (CHP-212 0.116×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PF-06260933 (drug)]] 5 µM |  | 0.719× | -3.3 | 0.49 | 13/46 (BT-474, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Methotrexate (drug)]] 0.5 µM |  | 0.847× | -3.1 | 0.49 | 10/48 (NCI-H460, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5405. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 38.1 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.44× (z +9.4) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.07× (z +8.8) | — |
| [[CHP-212 (line)]] | wt | 28.1 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.116× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 9.54 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.15× (z +9.4) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H23 (line)]] | alt | 46.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | — |
| [[RKO (line)]] | wt | 35.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -10.9) |
| [[SW 900 (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change |
| [[A-172 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5405), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP15]] | +0.79 | +0.82 / +0.69 | both halves | 7e-06 |  |
| [[RRS1]] | +0.75 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[LTV1]] | +0.75 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[CIAPIN1]] | +0.74 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[ZNF239]] | +0.73 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[BYSL]] | +0.73 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[PPIL1]] | +0.73 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[MAPKAPK5]] | +0.73 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[NOL9]] | +0.72 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[WDR4]] | +0.72 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[MRTO4]] | +0.72 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[DHX33]] | +0.71 | +0.61 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF1]] | -0.67 | -0.69 / -0.60 | both halves | 7e-06 |  |
| [[SIRT2]] | -0.64 | -0.64 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SCO1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SESN3]] | B | SESN3 activity lowers SCO1's level | lines that do not express SESN3 (20) vs lines expressing it (30) | 1.21× higher at baseline in the lines without SESN3 | 0.094 | ⚠ within organs, on part of the lines; also absent: EPHA4, GNG2, ST6GALNAC5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.781). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.8, -36.6); signed map (-0.6, -43.4). **Vector** length 82.4, 16.4% of its response variance represented; |z| ≥ 3 in 894 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.52 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.54 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.54 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.2 | +8.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.7 | +10.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +11.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +10.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +7.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +2.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.0 | +4.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | +0.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.8 | +1.5 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.8 | -1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -3.3 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | synthesis of cytochrome C oxidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:10,672,474-10,698,375 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SCOD1 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Complex IV assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O75880](https://www.uniprot.org/uniprotkb/O75880) (Cytochrome c oxidase assembly factor SCO1):

> Copper metallochaperone essential for the maturation of cytochrome c oxidase subunit II (MT-CO2/COX2). Together with SCO2, involved in delivering copper to the Cu(A) site on MT-CO2/COX2. Plays an important role in the regulation of copper homeostasis by controlling the abundance and cell membrane localization of copper transporter CTR1 (By similarity).

**Summary**, from NCBI Gene [6341](https://www.ncbi.nlm.nih.gov/gene/6341):

> Mammalian cytochrome c oxidase (COX) catalyzes the transfer of reducing equivalents from cytochrome c to molecular oxygen and pumps protons across the inner mitochondrial membrane. In yeast, 2 related COX assembly genes, SCO1 and SCO2 (synthesis of cytochrome c oxidase), enable subunits 1 and 2 to be incorporated into the holoprotein. This gene is the human homolog to the yeast SCO1 gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10603](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10603) · Entrez [6341](https://www.ncbi.nlm.nih.gov/gene/6341) · UniProt [O75880](https://www.uniprot.org/uniprotkb/O75880) · Ensembl [ENSG00000133028](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133028)

## Data

Gene col 5405: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5405); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5405, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5405]; `tensor/DDL_lfc|DDL_z.npy` [5405]; `embed/gene_vectors.npy` [5405]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5405 or target_col == 5405). Every well: [[SCO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
