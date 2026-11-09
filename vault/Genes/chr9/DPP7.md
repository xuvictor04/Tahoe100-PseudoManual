---
symbol: "DPP7"
type: "gene"
col: 10775
ensembl_id: "ENSG00000176978"
name: "dipeptidyl peptidase 7"
location: "9q34.3"
module: 122
arm: "+"
pooled_cpm: 11.64
n_lines_expressing: 47
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 7
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# DPP7

*dipeptidyl peptidase 7* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.30× (z +13.2, q 4e-37, up in 21 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.23× (z +3.4, q 0.066, up in 13 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (LoVo 6.51×, NCI-H460 4.04×, PANC-1 3.84×, LS 180 4.97×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (LS 180 7.72×, A-172 3.29×, SW480 3.91×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-172 3.32×; ⚠ toxic; transcription drop).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LOX-IMVI 0.143×, MIA PaCa-2 0.231×); [[Procainamide (hydrochloride) (drug)]] 0.5 µM in 1 line (SNU-423 0.0526×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTPBP6]] (+0.59, fdr 1e-05), [[GLMP]] (+0.59, fdr 1e-05), [[GAA]] (+0.57, fdr 4e-05); moves opposite to [[ARHGAP29]] (-0.45, fdr 1e-04), [[H3-3B]] (-0.44, fdr 2e-04), [[YWHAB]] (-0.44, fdr 4e-04).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 7 go from it, the strongest it → [[UGT2B7]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10775.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (LoVo 6.51×, NCI-H460 4.04×, PANC-1 3.84×, LS 180 4.97×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (LS 180 7.72×, A-172 3.29×, SW480 3.91×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-172 3.32×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.30×** | +13.2 | 4e-37 | 21/23 (LS 180, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.07×** | +12.9 | 1e-35 | 29/31 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.59×** | +10.1 | 9e-22 | 24/27 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.65×** | +5.8 | 1e-06 | 20/37 (SNU-423, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +4.7 | 3e-04 | 24/40 (SW 900, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.066 | 13/42 (A-172, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10775.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LOX-IMVI 0.143×, MIA PaCa-2 0.231×); [[Procainamide (hydrochloride) (drug)]] 0.5 µM in 1 line (SNU-423 0.0526×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM |  | 0.728× | -3.7 | 0.14 | 13/43 (HT-29, NCI-H2347, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | 0.740× | -3.5 | 0.15 | 11/44 (MIA PaCa-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10775. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 30.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.29× (z +9.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 17.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.72× (z +11.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 11.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.51× (z +11.7) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 8.66 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 24.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.231× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 14.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +10.1) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 10.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 7.07 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.5 µM 0.0526× (z -13.0) |
| [[SW480 (line)]] | alt | 10.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.91× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.70 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10775), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTPBP6]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[GLMP]] | +0.59 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[GAA]] | +0.57 | +0.70 / +0.41 | both halves | 4e-05 |  |
| [[HEXA]] | +0.57 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[QTRT1]] | +0.57 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[EIF2D]] | +0.57 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[DVL2]] | +0.56 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[TPP1]] | +0.55 | +0.56 / +0.45 | both halves | 3e-05 | STRING 437 |
| [[TRAPPC2L]] | +0.55 | +0.49 / +0.57 | both halves | 2e-05 |  |
| [[GET3]] | +0.55 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[SLC39A1]] | +0.54 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[ABHD14B]] | +0.54 | +0.48 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP29]] | -0.45 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[H3-3B]] | -0.44 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[YWHAB]] | -0.44 | -0.25 / -0.50 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UGT2B7]] | C | DPP7 activity lowers UGT2B7's level | lines that do not express DPP7 (3) vs lines expressing it (47) | 9.24× higher at baseline in the lines without DPP7 | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: FAM89A, GALNT7, KLF2; maybe low, not absent |
| [[P4HTM]] | C | DPP7 activity raises P4HTM's level | lines that do not express DPP7 (3) vs lines expressing it (47) | 3.24× lower at baseline in the lines without DPP7 | 0.026 | ⚠ few lines (3 vs 47); across organs; also absent: FAM89A, GALNT7, KLF2; maybe low, not absent |
| cells under [[Digitoxin (drug)]] 5 µM | C | DPP7 activity lowers the cells' numbers under Digitoxin 5 µM (makes them more sensitive) | lines that do not express DPP7 (3) vs lines expressing it (45) | the lines without DPP7: 2.04× the cells of the other lines | 0.044 | ⚠ few lines (3 vs 47); across organs; also absent: FAM89A, GALNT7, KLF2; maybe low, not absent |
| cells under [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM | C | DPP7 activity raises the cells' numbers under Ropivacaine (hydrochloride monohydrate) 5 µM (protects the cells) | lines that do not express DPP7 (3) vs lines expressing it (45) | the lines without DPP7: 0.82× the cells of the other lines | 0.059 | ⚠ few lines (3 vs 47); across organs; also absent: FAM89A, GALNT7, KLF2; maybe low, not absent |
| cells under [[Ouabain (Octahydrate) (drug)]] 0.5 µM | C | DPP7 activity lowers the cells' numbers under Ouabain (Octahydrate) 0.5 µM (makes them more sensitive) | lines that do not express DPP7 (3) vs lines expressing it (45) | the lines without DPP7: 1.81× the cells of the other lines | 0.071 | ⚠ few lines (3 vs 47); across organs; also absent: FAM89A, GALNT7, KLF2; maybe low, not absent |
| cells under [[Ouabain (Octahydrate) (drug)]] 5 µM | C | DPP7 activity lowers the cells' numbers under Ouabain (Octahydrate) 5 µM (makes them more sensitive) | lines that do not express DPP7 (3) vs lines expressing it (45) | the lines without DPP7: 1.83× the cells of the other lines | 0.078 | ⚠ few lines (3 vs 47); across organs; also absent: FAM89A, GALNT7, KLF2; maybe low, not absent |
| cells under [[Digitoxin (drug)]] 0.5 µM | C | DPP7 activity lowers the cells' numbers under Digitoxin 0.5 µM (makes them more sensitive) | lines that do not express DPP7 (3) vs lines expressing it (45) | the lines without DPP7: 1.66× the cells of the other lines | 0.088 | ⚠ few lines (3 vs 47); across organs; also absent: FAM89A, GALNT7, KLF2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.666). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.5, -18.3); signed map (-16.9, -28.7). **Vector** length 46.9, 6.51% of its response variance represented; |z| ≥ 3 in 606 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +10.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +3.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +2.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.5 | +0.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.5 | +2.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.5 | +1.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.2 | -2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.0 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[Gallic acid (hydrate) (drug)]] 5 µM |  | -0.9 | -1.7 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | dipeptidyl peptidase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:137,110,542-137,118,309 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DPPII, DPP2 |
| Gene groups (HGNC) | DASH family |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHL4](https://www.uniprot.org/uniprotkb/Q9UHL4) (Dipeptidyl peptidase 2):

> Plays an important role in the degradation of some oligopeptides.

**Summary**, from NCBI Gene [29952](https://www.ncbi.nlm.nih.gov/gene/29952):

> The protein encoded by this gene is a post-proline cleaving aminopeptidase expressed in quiescent lymphocytes. The resting lymphocytes are maintained through suppression of apoptosis, a state which is disrupted by inhibition of this novel serine protease. The enzyme has strong sequence homology with prolylcarboxypeptidase and is active at both acidic and neutral pH. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14892](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14892) · Entrez [29952](https://www.ncbi.nlm.nih.gov/gene/29952) · UniProt [Q9UHL4](https://www.uniprot.org/uniprotkb/Q9UHL4) · Ensembl [ENSG00000176978](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176978)

## Data

Gene col 10775: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10775); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10775, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10775]; `tensor/DDL_lfc|DDL_z.npy` [10775]; `embed/gene_vectors.npy` [10775]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10775 or target_col == 10775). Every well: [[DPP7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPP7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
