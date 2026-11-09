---
symbol: "VPS51"
type: "gene"
col: 7413
ensembl_id: "ENSG00000149823"
name: "VPS51 subunit of GARP complex"
location: "11q13.1"
module: 156
arm: "+"
pooled_cpm: 28.73
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 19
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/156"]
generated_by: "tahoemap"
---

# VPS51

*VPS51 subunit of GARP complex* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.57× (z +5.9, q 2e-06, up in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 5.15×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 2.28×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.518× (z -16.4, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ING5]] (+0.68, fdr 1e-05), [[QRICH1]] (+0.66, fdr 7e-06), [[RBM14-RBM4]] (+0.64, fdr 1e-05); moves opposite to [[PICALM]] (-0.52, fdr 7e-04), [[AFDN]] (-0.51, fdr 8e-04, ⚠ one half only (not replicated)), [[HMSD]] (-0.51, fdr 5e-05).
> It is in [[Module 156]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7413.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 5.15×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 2.28×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.57×** | +5.9 | 2e-06 | 19/48 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.37×** | +4.1 | 0.010 | 16/47 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.3 | 0.21 | 13/47 (PANC-1, A-427, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.13× | +3.0 | 0.36 | 2/48 (NCI-H2347, BT-474) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7413.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.518×** | -16.4 | 0e+00 | 44/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.550×** | -14.9 | 0e+00 | 45/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.559×** | -14.5 | 1e-45 | 43/48 (A498, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.678×** | -13.7 | 1e-40 | 39/48 (Hs 766T, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.682×** | -13.5 | 1e-39 | 31/47 (AsPC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.575×** | -13.3 | 3e-38 | 38/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.646×** | -10.9 | 9e-26 | 40/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.688×** | -9.4 | 6e-19 | 31/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.686×** | -9.1 | 7e-18 | 28/47 (A-172, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~23% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.707×** | -8.7 | 3e-16 | 30/48 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.715×** | -8.1 | 3e-14 | 27/47 (COLO 205, C-33 A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.728×** | -7.9 | 1e-13 | 27/47 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.559×** | -7.6 | 1e-12 | 30/48 (SW480, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.731×** | -7.5 | 2e-12 | 30/48 (HOP62, A-172, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.813×** | -7.3 | 1e-11 | 24/48 (LOX-IMVI, RPMI-7951, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.826×** | -4.8 | 5e-05 | 17/48 (HOP62, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.825×** | -4.5 | 2e-04 | 20/47 (C-33 A, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Terfenadine (drug)]] 0.5 µM |  | 0.881× | -3.2 | 0.040 | 12/48 (SW480, CFPAC-1, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.847× | -3.0 | 0.073 | 10/45 (NCI-H23, AN3 CA, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7413. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 36.5 | 0 | 4 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.236× (z -10.4) ⚠ toxic · without an alert: [[Tucidinostat (drug)]] 5 µM 0.624× (z -9.1) |
| [[A-427 (line)]] | wt | 35.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.364× (z -9.6) |
| [[C-33 A (line)]] | alt | 22.1 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.189× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[PANC-1 (line)]] | alt | 41.7 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.466× (z -9.5) |
| [[A-172 (line)]] | wt | 17.5 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -9.2) |
| [[AN3 CA (line)]] | alt | 23.6 | 0 | 2 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0734× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 24.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -12.2) |
| [[LoVo (line)]] | wt | 34.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.15× (z +16.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 22.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -15.8) |
| [[A498 (line)]] | wt | 17.4 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.367× (z -8.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[BT-474 (line)]] | alt | 52.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -11.5) |
| [[COLO 205 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.170× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[HCT15 (line)]] | alt | 41.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.292× (z -8.7) |
| [[HOP62 (line)]] | alt | 37.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.555× (z -8.6) |
| [[Hs 766T (line)]] | wt | 24.1 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.368× (z -10.2) |
| [[HS-578T (line)]] | alt | 41.9 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.112× (z -11.4) ⚠ toxic |
| [[HT-29 (line)]] | alt | 33.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 24.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -11.7) |
| [[J82 (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.445× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.323× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 29.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -9.9) ⚠ cell-cycle shift, explains ~24% of this change |
| [[NCI-H23 (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.334× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[RPMI-7951 (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.104× (z -15.7) ⚠ transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SHP-77 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 27.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0947× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7413), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ING5]] | +0.68 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[QRICH1]] | +0.66 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[RBM14-RBM4]] | +0.64 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[LRRC41]] | +0.64 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[TMEM87A]] | +0.63 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[ACO2]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[TMX2]] | +0.62 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[TRMT44]] | +0.61 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[DDX49]] | +0.60 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[DIDO1]] | +0.60 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[PRPF40B]] | +0.59 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[PEX6]] | +0.59 | +0.31 / +0.56 | both halves | 2e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PICALM]] | -0.52 | -0.21 / -0.48 | both halves | 7e-04 |  |
| [[AFDN]] | -0.51 | -0.20 / -0.52 | ⚠ one half (not replicated) | 8e-04 |  |
| [[HMSD]] | -0.51 | -0.39 / -0.58 | both halves | 5e-05 |  |
| [[RYBP]] | -0.49 | -0.17 / -0.57 | ⚠ one half (not replicated) | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises VPS51's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 156]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.635). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-25.1, -11.5); signed map (-32.3, -29.5). **Vector** length 74.8, 13.5% of its response variance represented; |z| ≥ 3 in 1,045 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.0 | +1.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.6 | +5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +4.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.9 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.7 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | -0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.5 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +1.7 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +0.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.5 | -13.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.5 | -9.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.5 | -8.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | -3.7 | -8.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.5 | -10.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -7.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | VPS51 subunit of GARP complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,089,324-65,111,862 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ANG2, ANG3, FFR; previously C11orf3, C11orf2 |
| Gene groups (HGNC) | Endosome-associated recycling protein (EARP) complex; Golgi associated retrograde protein (GARP) complex |
| Reactome | 4 pathways, smallest: Retrograde transport at the Trans-Golgi-Network; Intra-Golgi and retrograde Golgi-to-ER traffic; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UID3](https://www.uniprot.org/uniprotkb/Q9UID3) (Vacuolar protein sorting-associated protein 51 homolog):

> Acts as a component of the GARP complex that is involved in retrograde transport from early and late endosomes to the trans-Golgi network (TGN). The GARP complex is required for the maintenance of protein retrieval from endosomes to the TGN, acid hydrolase sorting, lysosome function, endosomal cholesterol traffic and autophagy. VPS51 participates in retrograde transport of acid hydrolase receptors, likely by promoting tethering and SNARE-dependent fusion of endosome-derived carriers to the TGN. …

**Summary**, from NCBI Gene [738](https://www.ncbi.nlm.nih.gov/gene/738):

> This gene encodes a member of the vacuolar protein sorting-associated protein 51 family. The encoded protein is a component of the Golgi-associated retrograde protein complex which acts as a tethering factor for carriers in retrograde transport from the early and late endosomes to the trans-Golgi network. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:1172](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1172) · Entrez [738](https://www.ncbi.nlm.nih.gov/gene/738) · UniProt [Q9UID3](https://www.uniprot.org/uniprotkb/Q9UID3) · Ensembl [ENSG00000149823](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149823)

## Data

Gene col 7413: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7413); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7413, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7413]; `tensor/DDL_lfc|DDL_z.npy` [7413]; `embed/gene_vectors.npy` [7413]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7413 or target_col == 7413). Every well: [[VPS51 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS51.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
