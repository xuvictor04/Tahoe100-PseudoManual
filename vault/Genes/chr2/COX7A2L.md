---
symbol: "COX7A2L"
type: "gene"
col: 3740
ensembl_id: "ENSG00000115944"
name: "cytochrome c oxidase subunit 7A2 like"
location: "2p21"
module: 40
arm: "+"
pooled_cpm: 51.57
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# COX7A2L

*cytochrome c oxidase subunit 7A2 like* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.31× (z +12.7, q 2e-34, up in 46 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.45× (z +7.9, q 4e-13, up in 37 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (AsPC-1 0.379×, A498 0.533×, A-427 0.583×; ⚠ cell-cycle shift, explains ~0% of this change); [[OTS514 (drug)]] 5 µM in 1 line (COLO 205 0.0570×); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.427×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERP1]] (+0.73, fdr 7e-06), [[SLC33A1]] (+0.70, fdr 7e-06), [[YIPF2]] (+0.69, fdr 7e-06); moves opposite to [[RIF1]] (-0.65, fdr 1e-05), [[TFAM]] (-0.60, fdr 1e-05), [[ATF7IP]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[IARS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3740.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.31×** | +12.7 | 2e-34 | 46/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +9.0 | 9e-17 | 35/40 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +7.9 | 4e-13 | 37/48 (NCI-H1792, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +6.4 | 3e-08 | 37/48 (NCI-H23, LoVo, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.46×** | +5.7 | 1e-06 | 34/47 (Panc 03.27, C32, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +5.2 | 2e-05 | 34/48 (CFPAC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +5.1 | 3e-05 | 29/43 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.39×** | +5.0 | 4e-05 | 32/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.006 | 24/48 (A-172, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.28×** | +3.7 | 0.010 | 23/48 (SNU-423, HEC-1-A, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.25×** | +3.3 | 0.042 | 23/48 (HEC-1-A, Panc 03.27, …) | all doses, flat |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.098 | 15/48 (NCI-H1573, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3740.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (AsPC-1 0.379×, A498 0.533×, A-427 0.583×; ⚠ cell-cycle shift, explains ~0% of this change); [[OTS514 (drug)]] 5 µM in 1 line (COLO 205 0.0570×); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.427×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | 0.784× | -3.5 | 0.27 | 20/47 (LOX-IMVI, RKO, …) | inconsistent across doses |  |
| [[Relugolix (drug)]] 5 µM |  | 0.860× | -3.3 | 0.32 | 7/49 (RPMI-7951, PANC-1, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.867× | -3.1 | 0.40 | 20/48 (AsPC-1, A498, …) | inconsistent across doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3740. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 47.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +11.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 87.9 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.427× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 64.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.62× (z +11.2) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 36.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +8.7) ⚠ toxic; transcription drop | [[OTS514 (drug)]] 5 µM 0.0570× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 40.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +10.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 48.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.88× (z +11.3) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 70.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 39.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.50× (z +9.2) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.320× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 44.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.61× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 76.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 47.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 41.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 64.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 46.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +9.3) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 50.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +8.5) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 39.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.41× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 62.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +16.1) | — |
| [[NCI-H2030 (line)]] | alt | 55.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 80.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 46.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 47.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +9.4) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 45.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 52.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 43.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +8.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 53.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3740), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERP1]] | +0.73 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[SLC33A1]] | +0.70 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.69 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[OSTC]] | +0.68 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[GPR107]] | +0.68 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[CDC26]] | +0.66 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[WIPI1]] | +0.66 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[IFT20]] | +0.66 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[SLC31A1]] | +0.66 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[GFPT1]] | +0.65 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[SEC61B]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[DNAJC25]] | +0.65 | +0.61 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIF1]] | -0.65 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[TFAM]] | -0.60 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[ATF7IP]] | -0.59 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[PNRC2]] | -0.57 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[DCLRE1A]] | -0.55 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[H2AX]] | -0.55 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[CSTF2T]] | -0.55 | -0.37 / -0.66 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IARS1]] | C | COX7A2L's natural level weakens IARS1's drug response | COX7A2L's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.64, reverse -0.12; direction not clear | 0.046 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.668). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (14.3, -36.1); signed map (-48.3, 10.9). **Vector** length 86.8, 21.8% of its response variance represented; |z| ≥ 3 in 688 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.1 | +6.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +2.8 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +2.5 | +0.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +2.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.1 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +1.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -2.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.3 | -3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -1.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.5 | -0.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase subunit 7A2 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:42,333,546-42,425,088 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EB1, COX7RP, COX7AR, SIG81, SCAF1, SCAFI |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 9 pathways, smallest: Complex IV assembly; Cytoprotection by HMOX1; TP53 Regulates Metabolic Genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O14548](https://www.uniprot.org/uniprotkb/O14548) (Cytochrome c oxidase subunit 7A2-like, mitochondrial):

> Assembly factor that mediates the formation of some mitochondrial respiratory supercomplexes (respirasomes), thereby promoting oxidative phosphorylation and energy metabolism. Acts as a molecular adapter that associates with both mitochondrial respiratory complexes III (CIII) and IV (CIV), promoting their association. Mediates the formation of various mitochondrial respiratory supercomplexes, such as MCIII(2)IV(2), composed of two CIII and two CIV, and the CS-respirasome (MCI(1)III(2)IV(2)), …

**Summary**, from NCBI Gene [9167](https://www.ncbi.nlm.nih.gov/gene/9167):

> Cytochrome c oxidase (COX), the terminal component of the mitochondrial respiratory chain, catalyzes the electron transfer from reduced cytochrome c to oxygen. This component is a heteromeric complex consisting of 3 catalytic subunits encoded by mitochondrial genes and multiple structural subunits encoded by nuclear genes. The mitochondrially-encoded subunits function in electron transfer, and the nuclear-encoded subunits may function in the regulation and assembly of the complex. This nuclear …

**Accessions** — [HGNC:2289](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2289) · Entrez [9167](https://www.ncbi.nlm.nih.gov/gene/9167) · UniProt [O14548](https://www.uniprot.org/uniprotkb/O14548) · Ensembl [ENSG00000115944](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115944)

## Data

Gene col 3740: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3740); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3740, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3740]; `tensor/DDL_lfc|DDL_z.npy` [3740]; `embed/gene_vectors.npy` [3740]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3740 or target_col == 3740). Every well: [[COX7A2L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COX7A2L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
