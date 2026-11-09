---
symbol: "FASTKD5"
type: "gene"
col: 13255
ensembl_id: "ENSG00000215251"
name: "FASTK mitochondrial RNA regulator 5"
location: "20p13"
module: 7
arm: "+"
pooled_cpm: 9.95
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# FASTKD5

*FASTK mitochondrial RNA regulator 5* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (14 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.02× (z +9.9, q 2e-20, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.586× (z -7.6, q 2e-11, down in 21 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.768× (z -5.3, q 4e-05, down in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (SW480 0.137×, NCI-H2347 0.234×, HS-578T 0.144×, AsPC-1 0.209×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2347 0.191×, LoVo 0.158×, AsPC-1 0.143×, SW480 0.261×; ⚠ toxic; transcription drop); [[Raltitrexed (drug)]] 0.5 µM in 1 line (Hs 766T 0.0654×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (SNU-1 0.0814×); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (SNU-1 0.115×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM115]] (+0.66, fdr 1e-05), [[BAG5]] (+0.65, fdr 1e-05), [[CLP1]] (+0.61, fdr 1e-05); moves opposite to [[TAF15]] (-0.58, fdr 1e-05), [[ACTR1B]] (-0.50, fdr 4e-05), [[CD83]] (-0.49, fdr 4e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → cells under [[Gemcitabine (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 16 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13255.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.02×** | +9.9 | 2e-20 | 40/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.56×** | +9.4 | 2e-18 | 37/47 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.79×** | +8.2 | 4e-14 | 36/47 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.78×** | +8.2 | 5e-14 | 31/47 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +8.0 | 1e-13 | 34/41 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +7.8 | 5e-13 | 26/45 (HOP62, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +7.2 | 5e-11 | 28/46 (SW480, COLO 205, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.67×** | +6.8 | 6e-10 | 29/44 (A498, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.62×** | +6.8 | 6e-10 | 23/47 (SW480, HT-29, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +6.4 | 7e-09 | 27/46 (SW480, HOP62, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +6.0 | 8e-08 | 23/44 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +6.0 | 8e-08 | 25/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.14×** | +5.6 | 9e-07 | 6/19 (SW480, PANC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.12×** | +5.5 | 1e-06 | 19/44 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.45×** | +5.3 | 5e-06 | 21/47 (Hs 766T, RPMI-7951, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.049 | 7/48 (SW480, RPMI-7951, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.24×** | +2.8 | 0.096 | 7/47 (SW48, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13255.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (SW480 0.137×, NCI-H2347 0.234×, HS-578T 0.144×, AsPC-1 0.209×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2347 0.191×, LoVo 0.158×, AsPC-1 0.143×, SW480 0.261×; ⚠ toxic; transcription drop); [[Raltitrexed (drug)]] 0.5 µM in 1 line (Hs 766T 0.0654×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (SNU-1 0.0814×); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (SNU-1 0.115×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.586×** | -7.6 | 2e-11 | 21/33 (LoVo, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.768×** | -5.3 | 4e-05 | 20/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.789× | -3.2 | 0.24 | 9/19 (SW480, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13255. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 16.4 | 0 | 3 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0814× (z -10.4) |
| [[SW480 (line)]] | alt | 14.9 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.25× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.137× (z -16.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 14.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 11.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -11.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 7.82 | 0 | 1 | — | [[Raltitrexed (drug)]] 0.5 µM 0.0654× (z -12.0) |
| [[HS-578T (line)]] | alt | 8.57 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -9.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 10.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -11.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 7.41 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13255), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM115]] | +0.66 | +0.55 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[BAG5]] | +0.65 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[CLP1]] | +0.61 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[YRDC]] | +0.59 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[TMEM127]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[GPATCH3]] | +0.58 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[CD2BP2]] | +0.57 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[PRCC]] | +0.57 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[ZDHHC5]] | +0.57 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[ATMIN]] | +0.56 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[MFSD5]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[DPH3]] | +0.56 | +0.57 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF15]] | -0.58 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[ACTR1B]] | -0.50 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[CD83]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[NKTR]] | -0.48 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[HADHB]] | -0.48 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[SEPTIN2]] | -0.48 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[ARHGAP12]] | -0.47 | -0.41 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Gemcitabine (drug)]] 5 µM | C | FASTKD5's natural level lowers the cells' numbers under Gemcitabine 5 µM (makes them more sensitive) | FASTKD5's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.268 over the table, 0.025 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[LY-2584702 (tosylate salt) (drug)]] 5 µM | C | FASTKD5's natural level lowers the cells' numbers under LY-2584702 (tosylate salt) 5 µM (makes them more sensitive) | FASTKD5's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.63 | 0.406 over the table, 0.087 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.592). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-28.8, -11.3); signed map (-7.8, -27.2). **Vector** length 59.0, 8.19% of its response variance represented; |z| ≥ 3 in 1,001 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.5 | +7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.3 | +8.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.6 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.6 | +8.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.5 | +6.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.5 | +2.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.4 | +0.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -5.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | +0.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.9 | -7.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.7 | -0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | FASTK mitochondrial RNA regulator 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:3,146,519-3,159,865 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13149 |
| Gene groups (HGNC) | FASTK mitochondrial RNA binding family |
| Reactome | 3 pathways, smallest: FASTK family proteins regulate processing and stability of mitochondrial RNAs; Mitochondrial RNA degradation; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L8L6](https://www.uniprot.org/uniprotkb/Q7L8L6) (Non-canonical pre-mRNAs endonuclease FASTKD5, mitochondrial):

> Required for the processing of non-canonical mitochondrial pre-mRNAs within the primary mitochondrial polycistronic transcript, i.e. pre-mRNA sequences that are not flanked by tRNA (tRNA punctuation). Has endoribonuclease activity and processes MT-CO1, MT-CO3 and MT-CYB pre-mRNAs, generating products with 3'/2'-phosphate or a 2',3'-cyclic phosphodiester at the 3'-end.

**Summary**, from NCBI Gene [60493](https://www.ncbi.nlm.nih.gov/gene/60493):

> Enables rRNA binding activity. Involved in mitochondrial RNA processing. Located in mitochondrial nucleoid and ribonucleoprotein granule. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25790](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25790) · Entrez [60493](https://www.ncbi.nlm.nih.gov/gene/60493) · UniProt [Q7L8L6](https://www.uniprot.org/uniprotkb/Q7L8L6) · Ensembl [ENSG00000215251](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215251)

## Data

Gene col 13255: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13255); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13255, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13255]; `tensor/DDL_lfc|DDL_z.npy` [13255]; `embed/gene_vectors.npy` [13255]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13255 or target_col == 13255). Every well: [[FASTKD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FASTKD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
