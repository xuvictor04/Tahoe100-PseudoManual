---
symbol: "NUP85"
type: "gene"
col: 4616
ensembl_id: "ENSG00000125450"
name: "nucleoporin 85"
location: "17q25.1"
module: 71
arm: "+"
pooled_cpm: 42.18
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# NUP85

*nucleoporin 85* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.35× (z +6.5, q 5e-08, up in 30 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Sapanisertib (drug)]] 0.5 µM: 1.23× (z +3.2, q 0.093, up in 9 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.601× (z -15.4, q 0e+00, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPIH]] (+0.79, fdr 7e-06), [[RAD51]] (+0.74, fdr 7e-06), [[RBL1]] (+0.73, fdr 7e-06); moves opposite to [[DNAH12]] (-0.61, fdr 2e-05), [[TSPAN31]] (-0.60, fdr 1e-05), [[MMRN2]] (-0.60, fdr 1e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DSCC1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4616.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +6.5 | 5e-08 | 30/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.31×** | +5.9 | 1e-06 | 29/47 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.28×** | +5.3 | 2e-05 | 26/48 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +5.2 | 3e-05 | 1/48 (NCI-H2030) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.27×** | +5.1 | 3e-05 | 22/48 (PANC-1, KATO III, …) | rises with dose | composition shift |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.20× | +3.9 | 0.011 | 14/48 (SNU-1, LS 180, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.17× | +3.4 | 0.058 | 14/48 (PANC-1, C-33 A, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.093 | 9/48 (PANC-1, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.16× | +3.2 | 0.093 | 14/48 (LoVo, NCI-H1792, …) | top dose only | position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.093 | 9/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.093 | 9/48 (C32, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.095 | 8/48 (PANC-1, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4616.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.601×** | -15.4 | 0e+00 | 41/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.577×** | -11.3 | 1e-27 | 38/48 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.589×** | -11.3 | 1e-27 | 39/47 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.730×** | -9.5 | 2e-19 | 30/48 (HOP62, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.745×** | -8.9 | 5e-17 | 37/48 (HOP62, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.685×** | -8.1 | 4e-14 | 35/48 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.711×** | -7.3 | 2e-11 | 30/48 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.737×** | -6.5 | 4e-09 | 25/48 (A-172, A-427, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.813×** | -6.3 | 2e-08 | 26/48 (A498, SNU-1, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.766×** | -5.7 | 6e-07 | 23/47 (HEC-1-A, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.790×** | -5.1 | 2e-05 | 24/48 (HOP62, C-33 A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.793×** | -4.8 | 8e-05 | 21/40 (PANC-1, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.835× | -3.9 | 0.005 | 14/48 (LS 180, A-427, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.846× | -3.6 | 0.013 | 17/48 (A-172, NCI-H2347, …) | top dose only |  |
| [[Erlotinib (drug)]] 0.5 µM |  | 0.868× | -3.1 | 0.082 | 3/48 (AsPC-1, NCI-H460, …) | rises with dose | position effect removed |
| [[Erlotinib (drug)]] 5 µM |  | 0.863× | -3.0 | 0.082 | 12/47 (HS-578T, HCT15, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4616. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 47.4 | 0 | 7 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.257× (z -14.8) |
| [[A-172 (line)]] | wt | 46.9 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -16.2) |
| [[PANC-1 (line)]] | alt | 46.9 | 4 (4 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +10.0) ⚠ cell-cycle shift, explains ~46% of this change | [[Dinaciclib (drug)]] 5 µM 0.452× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.499× (z -9.2) |
| [[A498 (line)]] | wt | 45.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -18.0) |
| [[NCI-H2347 (line)]] | alt | 42.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.319× (z -13.2) |
| [[A-427 (line)]] | wt | 60.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -10.5) |
| [[SNU-1 (line)]] | wt | 32.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.115× (z -12.6) |
| [[HEC-1-A (line)]] | alt | 52.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -12.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 28.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -11.6) |
| [[SHP-77 (line)]] | alt | 69.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -11.9) |
| [[SNU-423 (line)]] | alt | 51.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -13.0) |
| [[AsPC-1 (line)]] | alt | 28.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -9.4) |
| [[COLO 205 (line)]] | alt | 36.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.260× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 46.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 38.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.206× (z -14.2) |
| [[NCI-H23 (line)]] | alt | 57.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 36.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.580× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 31.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 42.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -9.1) |
| [[SW1417 (line)]] | alt | 38.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.403× (z -8.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 56.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4616), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIH]] | +0.79 | +0.75 / +0.78 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[RAD51]] | +0.74 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[RBL1]] | +0.73 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[SLF1]] | +0.72 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[SMYD4]] | +0.71 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[BLM]] | +0.71 | +0.68 / +0.63 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[RFC4]] | +0.71 | +0.68 / +0.66 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 402 |
| [[RAD54L]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[TRAIP]] | +0.70 | +0.57 / +0.70 | both halves | 8e-06 |  |
| [[FANCA]] | +0.69 | +0.70 / +0.64 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[DSCC1]] | +0.69 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[MMS22L]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAH12]] | -0.61 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[TSPAN31]] | -0.60 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[MMRN2]] | -0.60 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[LINC01933]] | -0.60 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[TSGA10]] | -0.58 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[AK9]] | -0.58 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[ZBED9]] | -0.58 | -0.64 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DSCC1]] | C | DSCC1 activity raises NUP85's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.51× lower at baseline in the lines without DSCC1 | 0.071 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.684). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-32.9, -46.7); signed map (-39.6, -41.0). **Vector** length 116, 29.9% of its response variance represented; |z| ≥ 3 in 810 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.0 | +3.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +0.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +1.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.1 | +6.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.6 | +3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.1 | +2.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -9.0 | -11.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.9 | -15.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.1 | -11.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.5 | -8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.2 | -8.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -6.5 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -2.3 | -0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -3.6 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | nucleoporin 85 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:75,205,659-75,235,758 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NUP75, FLJ12549 |
| Gene groups (HGNC) | Nucleoporins |
| Reactome | 85 pathways, smallest: Postmitotic nuclear pore complex (NPC) reformation; IP3 and IP4 transport between cytosol and nucleus; IP6 and IP7 transport between cytosol and nucleus |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BW27](https://www.uniprot.org/uniprotkb/Q9BW27) (Nuclear pore complex protein Nup85):

> Essential component of the nuclear pore complex (NPC) that seems to be required for NPC assembly and maintenance. As part of the NPC Nup107-160 subcomplex plays a role in RNA export and in tethering NUP96/Nup98 and NUP153 to the nucleus. The Nup107-160 complex seems to be required for spindle assembly during mitosis. NUP85 is required for membrane clustering of CCL2-activated CCR2. Seems to be involved in CCR2-mediated chemotaxis of monocytes and may link activated CCR2 to the …

**Summary**, from NCBI Gene [79902](https://www.ncbi.nlm.nih.gov/gene/79902):

> This gene encodes a protein component of the Nup107-160 subunit of the nuclear pore complex. Nuclear pore complexes are embedded in the nuclear envelope and promote bidirectional transport of macromolecules between the cytoplasm and nucleus. The encoded protein can also bind to the C-terminus of chemokine (C-C motif) receptor 2 (CCR2) and promote chemotaxis of monocytes, thereby participating in the inflammatory response. Alternative splicing results in multiple transcript variants. [provided …

**Accessions** — [HGNC:8734](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8734) · Entrez [79902](https://www.ncbi.nlm.nih.gov/gene/79902) · UniProt [Q9BW27](https://www.uniprot.org/uniprotkb/Q9BW27) · Ensembl [ENSG00000125450](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125450)

## Data

Gene col 4616: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4616); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4616, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4616]; `tensor/DDL_lfc|DDL_z.npy` [4616]; `embed/gene_vectors.npy` [4616]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4616 or target_col == 4616). Every well: [[NUP85 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUP85.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
