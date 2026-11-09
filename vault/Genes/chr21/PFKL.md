---
symbol: "PFKL"
type: "gene"
col: 6583
ensembl_id: "ENSG00000141959"
name: "phosphofructokinase, liver type"
location: "21q22.3"
module: 103
arm: "+"
pooled_cpm: 61.27
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 31
n_dd_up_clean: 0
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# PFKL

*phosphofructokinase, liver type* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.38× (z +5.2, q 1e-04, up in 29 of 49 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (LS 180 2.30×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.351× (z -24.1, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IDH3G]] (+0.65, fdr 7e-06), [[DDX41]] (+0.64, fdr 7e-06), [[MAPK7]] (+0.62, fdr 7e-06); moves opposite to [[SMIM30]] (-0.52, fdr 3e-05), [[JPX]] (-0.43, fdr 4e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Vinblastine (sulfate) (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6583.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (LS 180 2.30×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +5.2 | 1e-04 | 29/49 (LS 180, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.30× | +3.0 | 0.68 | 19/48 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6583.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.351×** | -24.1 | 0e+00 | 46/48 (MIA PaCa-2, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.389×** | -15.4 | 0e+00 | 47/48 (A-427, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.435×** | -13.6 | 1e-39 | 46/48 (NCI-H23, HCT15, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.449×** | -13.1 | 9e-37 | 47/48 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.510×** | -11.0 | 5e-26 | 44/48 (NCI-H23, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.552×** | -9.3 | 1e-18 | 39/48 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.682×** | -8.8 | 9e-17 | 40/48 (J82, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.614×** | -8.0 | 1e-13 | 42/48 (NCI-H2030, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.614×** | -7.9 | 1e-13 | 44/48 (SW480, C32, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.613×** | -7.7 | 1e-12 | 40/47 (HCT15, A-172, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.643×** | -7.2 | 3e-11 | 35/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.646×** | -7.1 | 5e-11 | 40/48 (LS 180, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.673×** | -6.5 | 5e-09 | 37/48 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.677×** | -6.4 | 8e-09 | 32/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.690×** | -6.0 | 6e-08 | 35/48 (LS 180, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.728×** | -5.2 | 8e-06 | 33/48 (A-427, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.710×** | -5.1 | 1e-05 | 34/48 (SK-MEL-2, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6583. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 111 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -19.0) |
| [[SW480 (line)]] | alt | 46.7 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -24.4) |
| [[NCI-H23 (line)]] | alt | 67.6 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -25.4) |
| [[SK-MEL-2 (line)]] | alt | 64.0 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -19.5) |
| [[C-33 A (line)]] | alt | 70.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -15.1) |
| [[C32 (line)]] | wt | 94.3 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -13.7) |
| [[HCT15 (line)]] | alt | 103 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -25.5) |
| [[NCI-H1573 (line)]] | alt | 98.0 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -24.8) |
| [[HEC-1-A (line)]] | alt | 107 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -16.2) |
| [[LOX-IMVI (line)]] | wt | 66.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -23.0) |
| [[LS 180 (line)]] | wt | 91.7 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -23.6) |
| [[NCI-H460 (line)]] | wt | 46.2 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -15.9) |
| [[LoVo (line)]] | wt | 52.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -22.4) |
| [[NCI-H2347 (line)]] | alt | 48.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -11.6) |
| [[A-427 (line)]] | wt | 52.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0816× (z -22.6) |
| [[A549 (line)]] | wt | 45.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 44.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -14.0) |
| [[CFPAC-1 (line)]] | alt | 74.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -9.5) |
| [[H4 (line)]] | wt | 88.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.128× (z -16.4) |
| [[HOP62 (line)]] | alt | 78.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -15.6) |
| [[HS-578T (line)]] | alt | 76.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -13.3) |
| [[J82 (line)]] | alt | 45.4 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.372× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 120 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -36.0) |
| [[Hs 766T (line)]] | wt | 53.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -12.6) |
| [[NCI-H2030 (line)]] | alt | 59.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -20.9) |
| [[NCI-H661 (line)]] | alt | 48.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -8.9) |
| [[PANC-1 (line)]] | alt | 42.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -16.1) |
| [[RKO (line)]] | wt | 39.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -12.6) |
| [[SW48 (line)]] | wt | 70.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -13.3) |
| [[AN3 CA (line)]] | alt | 73.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.175× (z -10.5) |
| [[HT-29 (line)]] | alt | 38.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -17.4) |
| [[hTERT-HPNE (line)]] | wt | 62.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.314× (z -8.9) ⚠ toxic |
| [[KATO III (line)]] | alt | 40.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -16.0) |
| [[NCI-H1792 (line)]] | alt | 53.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.374× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 58.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -9.1) |
| [[SNU-1 (line)]] | wt | 66.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -12.6) |
| [[SNU-423 (line)]] | alt | 63.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -13.2) |
| [[SW 1271 (line)]] | alt | 53.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -8.8) |
| [[SW 900 (line)]] | alt | 47.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -11.1) |
| [[A498 (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6583), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDH3G]] | +0.65 | +0.59 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_ADIPOGENESIS; STRING 517 |
| [[DDX41]] | +0.64 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[MAPK7]] | +0.62 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[GANAB]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[MAN1B1]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[PPFIA4]] | +0.57 | +0.70 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_HYPOXIA |
| [[SH3D21]] | +0.56 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[PLOD1]] | +0.54 | +0.68 / +0.40 | both halves | 4e-05 |  |
| [[SBF1]] | +0.54 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[ANAPC2]] | +0.54 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[TBC1D9B]] | +0.53 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[GAA]] | +0.53 | +0.47 / +0.43 | both halves | 3e-05 | pathway: HALLMARK_HYPOXIA |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM30]] | -0.52 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[JPX]] | -0.43 | -0.50 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Vinblastine (sulfate) (drug)]] 5 µM | C | PFKL's natural level raises the cells' numbers under Vinblastine (sulfate) 5 µM (protects the cells) | PFKL's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.68 | 0.285 over the table, 0.036 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.538). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.9, -22.4); signed map (-39.8, 26.4). **Vector** length 84.2, 22.1% of its response variance represented; |z| ≥ 3 in 1,114 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | -2.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.7 | +2.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -0.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +3.2 | -2.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.3 | -13.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.2 | +0.9 |
|  | [[Pentoxifylline (drug)]] 5 µM |  | +2.0 | +1.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.9 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +2.1 |
|  | [[Roxadustat (drug)]] 5 µM |  | +1.8 | +1.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.6 | -7.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.8 | -8.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.7 | -7.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.1 | -5.2 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.6 | -1.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.5 | -2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | -4.1 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -2.3 | -2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | phosphofructokinase, liver type |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:44,300,051-44,327,376 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phosphofructokinase family |
| Hallmark sets | HYPOXIA, ADIPOGENESIS, MTORC1_SIGNALING |
| Reactome | 5 pathways, smallest: Glycolysis; Glucose metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P17858](https://www.uniprot.org/uniprotkb/P17858) (ATP-dependent 6-phosphofructokinase, liver type):

> Catalyzes the phosphorylation of D-fructose 6-phosphate to fructose 1,6-bisphosphate by ATP, the first committing step of glycolysis. Negatively regulates the phagocyte oxidative burst in response to bacterial infection by controlling cellular NADPH biosynthesis and NADPH oxidase-derived reactive oxygen species. Upon macrophage activation, drives the metabolic switch toward glycolysis, thus preventing glucose turnover that produces NADPH via pentose phosphate pathway (By similarity).

**Summary**, from NCBI Gene [5211](https://www.ncbi.nlm.nih.gov/gene/5211):

> This gene encodes the liver (L) subunit of an enzyme that catalyzes the conversion of D-fructose 6-phosphate to D-fructose 1,6-bisphosphate, which is a key step in glucose metabolism (glycolysis). This enzyme is a tetramer that may be composed of different subunits encoded by distinct genes in different tissues. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:8876](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8876) · Entrez [5211](https://www.ncbi.nlm.nih.gov/gene/5211) · UniProt [P17858](https://www.uniprot.org/uniprotkb/P17858) · Ensembl [ENSG00000141959](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141959)

## Data

Gene col 6583: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6583); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6583, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6583]; `tensor/DDL_lfc|DDL_z.npy` [6583]; `embed/gene_vectors.npy` [6583]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6583 or target_col == 6583). Every well: [[PFKL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PFKL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
