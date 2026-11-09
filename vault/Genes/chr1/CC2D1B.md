---
symbol: "CC2D1B"
type: "gene"
col: 7785
ensembl_id: "ENSG00000154222"
name: "coiled-coil and C2 domain containing 1B"
location: "1p32.3"
module: 7
arm: "+"
pooled_cpm: 19.78
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# CC2D1B

*coiled-coil and C2 domain containing 1B* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Sapanisertib (drug)]] 0.05 µM: 1.33× (z +3.9, q 0.034, up in 15 of 48 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.41× (z +3.8, q 0.034, up in 13 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 2.62×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 3.71×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.444× (z -6.2, q 3e-07, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC66A1]] (+0.67, fdr 1e-05), [[SLC12A4]] (+0.63, fdr 7e-06), [[TAOK2]] (+0.60, fdr 1e-05); moves opposite to [[FAM117B]] (-0.56, fdr 1e-05), [[LRRC1]] (-0.55, fdr 5e-05), [[ATP8A1]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7785.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 2.62×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 3.71×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.33×** | +3.9 | 0.034 | 15/48 (Hs 766T, SW480, …) | inconsistent across doses | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.034 | 13/47 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.039 | 13/47 (HEC-1-A, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.26× | +3.2 | 0.22 | 13/48 (SW480, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7785.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.444×** | -6.2 | 3e-07 | 33/48 (Hs 766T, Panc 03.27, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.691×** | -5.4 | 2e-05 | 25/48 (HS-578T, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.501×** | -5.3 | 2e-05 | 28/41 (Panc 03.27, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.712×** | -5.0 | 1e-04 | 23/47 (A-172, LOX-IMVI, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **0.735×** | -4.5 | 7e-04 | 22/47 (KATO III, SW480, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.673×** | -4.5 | 7e-04 | 20/44 (NCI-H1792, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.740×** | -4.4 | 9e-04 | 22/48 (A-172, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.574×** | -4.2 | 0.002 | 16/45 (LoVo, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.775×** | -3.7 | 0.013 | 19/47 (MIA PaCa-2, RPMI-7951, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.659×** | -3.2 | 0.083 | 12/46 (MIA PaCa-2, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.806×** | -3.2 | 0.083 | 18/47 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~67% of this change | 0.813× | -3.0 | 0.12 | 14/48 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7785. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 26.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 22.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.71× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A549 (line)]] | wt | 22.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 14.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.171× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 19.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.219× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 21.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.227× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 15.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0814× (z -8.9) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 20.6 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.05 µM 0.0657× (z -12.6) |
| [[SW48 (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0799× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7785), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC66A1]] | +0.67 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[SLC12A4]] | +0.63 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[TAOK2]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[CD2BP2]] | +0.59 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[LCAT]] | +0.58 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[KHNYN]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[TFE3]] | +0.57 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[ZNF674]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[BLOC1S3]] | +0.56 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[WSB2]] | +0.56 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[FAM50A]] | +0.56 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[DMWD]] | +0.55 | +0.52 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM117B]] | -0.56 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[LRRC1]] | -0.55 | -0.60 / -0.39 | both halves | 5e-05 |  |
| [[ATP8A1]] | -0.54 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[USP3]] | -0.53 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[RAB20]] | -0.53 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[PPAT]] | -0.52 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[TRERF1]] | -0.52 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[LDHB]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[CNOT6L]] | -0.52 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[MTF2]] | -0.51 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[NFIA]] | -0.51 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[ORC4]] | -0.51 | -0.51 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | CC2D1B's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | CC2D1B's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.268 over the table, 0.017 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | CC2D1B's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | CC2D1B's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64 | 0.390 over the table, 0.052 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | CC2D1B's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | CC2D1B's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.57 | 0.509 over the table, 0.093 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.361). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-8.7, -0.6); signed map (1.9, -9.6). **Vector** length 76.6, 14.4% of its response variance represented; |z| ≥ 3 in 843 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +1.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.8 | +2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +2.8 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.6 | +1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.5 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.5 | +1.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.5 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.8 | -0.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.8 | +1.8 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.7 | -1.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | -2.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | -2.5 | -4.5 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil and C2 domain containing 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:52,345,723-52,366,205 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1836, Freud-2, Lgd1 |
| Gene groups (HGNC) | C2 domain containing |
| Reactome | 7 pathways, smallest: Sealing of the nuclear envelope (NE) by ESCRT-III; Nuclear Envelope (NE) Reassembly; Mitotic Anaphase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T0F9](https://www.uniprot.org/uniprotkb/Q5T0F9) (Coiled-coil and C2 domain-containing protein 1B):

> Transcription factor that binds specifically to the DRE (dual repressor element) and represses HTR1A gene transcription in neuronal cells.

**Summary**, from NCBI Gene [200014](https://www.ncbi.nlm.nih.gov/gene/200014):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to act upstream of or within negative regulation of transcription by RNA polymerase II. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29386](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29386) · Entrez [200014](https://www.ncbi.nlm.nih.gov/gene/200014) · UniProt [Q5T0F9](https://www.uniprot.org/uniprotkb/Q5T0F9) · Ensembl [ENSG00000154222](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154222)

## Data

Gene col 7785: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7785); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7785, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7785]; `tensor/DDL_lfc|DDL_z.npy` [7785]; `embed/gene_vectors.npy` [7785]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7785 or target_col == 7785). Every well: [[CC2D1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CC2D1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
