---
symbol: "TTC23L"
type: "gene"
col: 13017
ensembl_id: "ENSG00000205838"
name: "tetratricopeptide repeat domain 23 like"
location: "5p13.2"
module: 53
arm: "+"
pooled_cpm: 5.56
n_lines_expressing: 45
n_dd_up: 17
n_dd_down: 16
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# TTC23L

*tetratricopeptide repeat domain 23 like* — 5p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.13× (z +11.8, q 1e-29, up in 22 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.451× (z -8.9, q 4e-16, down in 26 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XG]] (+0.73, fdr 7e-06), [[DPYS]] (+0.69, fdr 7e-06), [[CCNP]] (+0.69, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ADAM7-AS1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[APH1B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13017.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +11.8 | 1e-29 | 22/34 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +8.6 | 2e-15 | 3/10 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.59×** | +7.3 | 7e-11 | 19/41 (A-427, HOP62, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **1.91×** | +7.2 | 1e-10 | 22/41 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +7.1 | 1e-10 | 19/37 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +6.9 | 4e-10 | 7/21 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +6.3 | 2e-08 | 17/42 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.73×** | +6.0 | 1e-07 | 17/36 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.71×** | +5.9 | 2e-07 | 17/42 (A498, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +5.3 | 6e-06 | 15/39 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +4.7 | 1e-04 | 12/41 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.54×** | +4.5 | 4e-04 | 14/39 (A498, A-172, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.002 | 11/33 (NCI-H2030, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +3.9 | 0.004 | 14/38 (A-172, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.5 | 0.015 | 13/28 (HOP62, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.055 | 11/34 (C-33 A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13017.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.451×** | -8.9 | 4e-16 | 26/41 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.614×** | -5.4 | 1e-05 | 18/38 (NCI-H1573, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.628×** | -5.2 | 4e-05 | 12/41 (NCI-H1573, H4, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.635×** | -5.1 | 6e-05 | 17/34 (LOX-IMVI, SW 900, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.661×** | -4.6 | 4e-04 | 15/38 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.677×** | -4.4 | 0.001 | 6/39 (Panc 03.27, HT-29, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.681×** | -4.3 | 0.001 | 13/39 (HEC-1-A, SK-MEL-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.686×** | -4.2 | 0.002 | 15/38 (NCI-H1573, LOX-IMVI, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.490×** | -4.2 | 0.002 | 15/37 (A498, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.705×** | -3.9 | 0.005 | 16/40 (RPMI-7951, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.708×** | -3.9 | 0.006 | 12/41 (HT-29, J82, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.518×** | -3.8 | 0.006 | 11/31 (HepG2/C3A, A498, …) | top dose only | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.704×** | -3.8 | 0.007 | 6/40 (SW48, HepG2/C3A, …) | top dose only | plate-row cell shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.813×** | -3.3 | 0.038 | 10/41 (Panc 03.27, NCI-H1573, …) | inconsistent across doses |  |
| [[LB-100 (drug)]] 0.05 µM |  | **0.746×** | -3.1 | 0.071 | 5/42 (AN3 CA, NCI-H23, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13017. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 14.2 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.184× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 15.8 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.5 µM 0.0943× (z -8.5) |
| [[HS-578T (line)]] | alt | 8.10 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0814× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 5.93 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0880× (z -9.3) |
| [[A-172 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.93 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.907 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13017), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XG]] | +0.73 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[DPYS]] | +0.69 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[CCNP]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[USP50]] | +0.69 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[PLCD4]] | +0.69 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[MIR9-1HG]] | +0.69 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[ARL9]] | +0.69 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[ADCY10P1]] | +0.68 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.67 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.67 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.67 | +0.67 / +0.57 | both halves | 8e-06 |  |
| [[CNBD2]] | +0.66 | +0.67 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM7-AS1]] | B | ADAM7-AS1 activity raises TTC23L's level | lines that do not express ADAM7-AS1 (23) vs lines expressing it (27) | 1.94× lower at baseline in the lines without ADAM7-AS1 | 0.057 | ⚠ within organs, on part of the lines; also absent: SETBP1, KCNMA1, STC1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APH1B]] | B | TTC23L activity raises APH1B's level | lines that do not express TTC23L (5) vs lines expressing it (45) | 3.20× lower at baseline in the lines without TTC23L | 0.089 | ⚠ within organs, on part of the lines; also absent: DNAJC18, NXPE3, TBKBP1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.698). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.0, -16.7); signed map (15.2, 9.7). **Vector** length 64.4, 10.4% of its response variance represented; |z| ≥ 3 in 1,030 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +3.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +6.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | +5.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +4.5 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.6 | +2.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -5.4 |
|  | [[NG25 (drug)]] 5 µM |  | -2.3 | -3.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -3.9 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.7 | -5.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.4 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 23 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.2 — chr5:34,838,833-34,900,511 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25439 |
| Matched by | ensembl_id |

UniProt [Q6PF05](https://www.uniprot.org/uniprotkb/Q6PF05) carries no function annotation.

**Summary**, from NCBI Gene [153657](https://www.ncbi.nlm.nih.gov/gene/153657):

> Predicted to be involved in response to endoplasmic reticulum stress. Predicted to be located in centrosome; midbody; and spindle. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26355](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26355) · Entrez [153657](https://www.ncbi.nlm.nih.gov/gene/153657) · UniProt [Q6PF05](https://www.uniprot.org/uniprotkb/Q6PF05) · Ensembl [ENSG00000205838](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205838)

## Data

Gene col 13017: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13017); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13017, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13017]; `tensor/DDL_lfc|DDL_z.npy` [13017]; `embed/gene_vectors.npy` [13017]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13017 or target_col == 13017). Every well: [[TTC23L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC23L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
