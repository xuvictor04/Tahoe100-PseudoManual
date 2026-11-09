---
symbol: "ZBTB49"
type: "gene"
col: 9707
ensembl_id: "ENSG00000168826"
name: "zinc finger and BTB domain containing 49"
location: "4p16.3"
module: 142
arm: "+"
pooled_cpm: 8.89
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# ZBTB49

*zinc finger and BTB domain containing 49* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.51× (z +11.3, q 6e-27, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.425× (z -10.6, q 1e-23, down in 25 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.763× (z -4.8, q 3e-04, down in 20 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (CFPAC-1 0.102×, HOP62 0.159×, NCI-H1573 0.127×, NCI-H2030 0.107×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HOP62 0.0567×, AsPC-1 0.0795×, NCI-H1573 0.146×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (PANC-1 0.0793×, HOP62 0.175×; ⚠ toxic; transcription drop); [[Orlistat (drug)]] 0.05 µM in 1 line (CFPAC-1 0.119×); [[Saquinavir (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.103×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0766×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CWF19L1]] (+0.69, fdr 7e-06), [[SLC30A6]] (+0.68, fdr 7e-06), [[UBOX5]] (+0.67, fdr 8e-06); moves opposite to [[TBL1XR1]] (-0.60, fdr 1e-05), [[RFK]] (-0.58, fdr 3e-05), [[MBNL1]] (-0.54, fdr 5e-05).
> It is in [[Module 142]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PEG10]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9707.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.51×** | +11.3 | 6e-27 | 44/47 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.11×** | +9.2 | 1e-17 | 41/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.18×** | +9.0 | 6e-17 | 39/47 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.89×** | +7.4 | 2e-11 | 27/44 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.80×** | +7.2 | 5e-11 | 30/47 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.92×** | +6.9 | 5e-10 | 27/43 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.69×** | +6.4 | 2e-08 | 25/47 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +6.0 | 2e-07 | 22/42 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +5.2 | 1e-05 | 18/44 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +4.4 | 6e-04 | 15/46 (HOP62, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +4.3 | 1e-03 | 20/45 (KATO III, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.3 | 0.001 | 17/44 (LOX-IMVI, A498, …) | top dose only | cell-cycle shift (explains ~8% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9707.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (CFPAC-1 0.102×, HOP62 0.159×, NCI-H1573 0.127×, NCI-H2030 0.107×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HOP62 0.0567×, AsPC-1 0.0795×, NCI-H1573 0.146×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (PANC-1 0.0793×, HOP62 0.175×; ⚠ toxic; transcription drop); [[Orlistat (drug)]] 0.05 µM in 1 line (CFPAC-1 0.119×); [[Saquinavir (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.103×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0766×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.425×** | -10.6 | 1e-23 | 25/33 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.505×** | -8.2 | 1e-13 | 11/15 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.647×** | -5.0 | 1e-04 | 16/25 (HOP62, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.763×** | -4.8 | 3e-04 | 20/47 (A498, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.735×** | -3.8 | 0.014 | 20/45 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9707. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 12.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0567× (z -16.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 9.92 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Orlistat (drug)]] 0.05 µM 0.119× (z -11.0) |
| [[hTERT-HPNE (line)]] | wt | 9.27 | 0 | 2 (1 ⚠) | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0766× (z -9.5) |
| [[J82 (line)]] | alt | 7.99 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -9.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 6.35 | 0 | 2 (1 ⚠) | — | [[Saquinavir (drug)]] 0.05 µM 0.103× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 13.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -11.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 8.69 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0793× (z -16.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 9.62 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0795× (z -11.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 5.72 | 0 | 1 | — | [[Pentagastrin (drug)]] 0.5 µM 0.0751× (z -8.7) |
| [[Hs 766T (line)]] | wt | 8.15 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0878× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 7.23 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -10.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 10.00 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.107× (z -9.1) |
| [[SW480 (line)]] | alt | 9.89 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.27× (z +8.6) | — |
| [[A-172 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.91 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9707), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CWF19L1]] | +0.69 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[SLC30A6]] | +0.68 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[UBOX5]] | +0.67 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[BRAP]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[SHARPIN]] | +0.65 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[ZNF500]] | +0.65 | +0.54 / +0.65 | both halves | 1e-05 | same gene group |
| [[ZNF7]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 | same gene group |
| [[USP20]] | +0.64 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[LCMT1]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[PARL]] | +0.64 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[C1orf52]] | +0.62 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[ARHGAP1]] | +0.62 | +0.60 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBL1XR1]] | -0.60 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[RFK]] | -0.58 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[MBNL1]] | -0.54 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[RHOBTB3]] | -0.53 | -0.46 / -0.42 | both halves | 4e-05 | same gene group |
| [[RFX3]] | -0.53 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[DDX3X]] | -0.53 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[PEAK1]] | -0.53 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[ATF7IP]] | -0.53 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[STIM2]] | -0.52 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[ALCAM]] | -0.52 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[CHD4]] | -0.51 | -0.46 / -0.46 | both halves | 2e-05 |  |
| [[GDF11]] | -0.51 | -0.55 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PEG10]] | B | PEG10 activity raises ZBTB49's level | lines that do not express PEG10 (17) vs lines expressing it (33) | 1.24× lower at baseline in the lines without PEG10 | 0.029 | ⚠ within organs, on part of the lines; also absent: ZNF569, ZNF570, MAP1B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction 0.723). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.7, -4.1); signed map (-45.6, 4.7). **Vector** length 66.9, 10.8% of its response variance represented; |z| ≥ 3 in 962 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +3.8 | +7.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +6.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.0 | +7.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.8 | +6.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.4 | +9.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +4.4 |
|  | [[Fulvestrant (drug)]] 0.5 µM |  | +1.4 | +1.3 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | +1.4 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +0.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.8 | -3.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.5 | -10.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.4 | -2.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.1 | -8.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -1.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | +2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 49 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:4,290,251-4,321,786 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38559; previously ZNF509 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZSB9](https://www.uniprot.org/uniprotkb/Q6ZSB9) (Zinc finger and BTB domain-containing protein 49):

> Transcription factor. Inhibits cell proliferation by activating either CDKN1A/p21 transcription or RB1 transcription.; [Isoform 1]: Binds CDKN1A promoter and activates its transcription; this activity is further potentiated in the presence of EP300 (synergistic) and ZBTB17/Miz-1 (additive).; [Isoform 3]: Activates RB1 transcription most probably by antagonizing ZBTB17 repression of RB1. Does not bind directly RB1 promoter.

**Summary**, from NCBI Gene [166793](https://www.ncbi.nlm.nih.gov/gene/166793):

> Enables DNA-binding transcription factor binding activity; sequence-specific DNA binding activity; and transcription coactivator binding activity. Involved in negative regulation of cell population proliferation; positive regulation of transcription by RNA polymerase II; and regulation of cell cycle. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19883](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19883) · Entrez [166793](https://www.ncbi.nlm.nih.gov/gene/166793) · UniProt [Q6ZSB9](https://www.uniprot.org/uniprotkb/Q6ZSB9) · Ensembl [ENSG00000168826](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168826)

## Data

Gene col 9707: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9707); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9707, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9707]; `tensor/DDL_lfc|DDL_z.npy` [9707]; `embed/gene_vectors.npy` [9707]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9707 or target_col == 9707). Every well: [[ZBTB49 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB49.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
