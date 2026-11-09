---
symbol: "CCT6P1"
type: "gene"
col: 13641
ensembl_id: "ENSG00000228409"
name: "chaperonin containing TCP1 family member 6A2, pseudogene"
location: "7q11.21"
module: 107
arm: "+"
pooled_cpm: 9.02
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# CCT6P1

*chaperonin containing TCP1 family member 6A2, pseudogene* — 7q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.24× (z +15.4, q 0e+00, up in 35 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.828× (z -3.6, q 0.098, down in 13 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 2 lines (NCI-H1792 0.101×, HT-29 0.0892×); [[Fluvoxamine (drug)]] 5 µM in 1 line (RPMI-7951 0.0550×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-172 0.143×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Eplerenone (drug)]] 0.05 µM in 1 line (C32 0.0626×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCT6P3]] (+0.63, fdr 1e-05), [[QTRT2]] (+0.61, fdr 1e-05), [[ZNF777]] (+0.61, fdr 4e-05); moves opposite to [[C4orf3]] (-0.62, fdr 1e-05), [[SLC35B2]] (-0.61, fdr 3e-05), [[NPTN]] (-0.56, fdr 5e-05).
> It is in [[Module 107]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CCDC88A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13641.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.24×** | +15.4 | 0e+00 | 35/46 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.42×** | +11.5 | 4e-28 | 37/46 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.64×** | +11.3 | 3e-27 | 37/44 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.17×** | +10.5 | 2e-23 | 33/47 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.16×** | +9.9 | 7e-21 | 31/46 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.91×** | +9.6 | 5e-20 | 30/42 (SW480, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.79×** | +7.8 | 3e-13 | 28/47 (SW480, A498, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.74×** | +7.1 | 7e-11 | 23/47 (SW480, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +6.4 | 1e-08 | 21/43 (NCI-H2030, HT-29, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +6.2 | 3e-08 | 19/36 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.34×** | +6.0 | 1e-07 | 20/30 (SW1417, SW480, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.22×** | +5.6 | 9e-07 | 23/46 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +5.4 | 3e-06 | 21/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.4 | 3e-06 | 17/44 (RPMI-7951, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.0 | 2e-05 | 16/45 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.61×** | +4.6 | 2e-04 | 11/48 (MIA PaCa-2, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.015 | 11/46 (C32, HOP62, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13641.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 2 lines (NCI-H1792 0.101×, HT-29 0.0892×); [[Fluvoxamine (drug)]] 5 µM in 1 line (RPMI-7951 0.0550×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-172 0.143×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Eplerenone (drug)]] 0.05 µM in 1 line (C32 0.0626×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.828×** | -3.6 | 0.098 | 13/48 (A498, HEC-1-A, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.691×** | -3.6 | 0.098 | 12/44 (SW48, KATO III, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | 0.771× | -3.3 | 0.20 | 8/40 (RKO, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13641. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 15.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.3) | — |
| [[AsPC-1 (line)]] | alt | 6.08 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.122× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Irinotecan (hydrochloride) (drug)]] 0.05 µM 0.107× (z -8.5) |
| [[HT-29 (line)]] | alt | 5.63 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +8.9) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0892× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 8.98 | 0 | 2 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.101× (z -10.1) |
| [[A-172 (line)]] | wt | 9.39 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 6.01 | 0 | 1 | — | [[Eplerenone (drug)]] 0.05 µM 0.0626× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 11.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +9.1) | — |
| [[KATO III (line)]] | alt | 9.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.16× (z +11.7) | — |
| [[LoVo (line)]] | wt | 8.26 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.26× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 3.21 | 0 | 1 (1 ⚠) | — | [[Vortioxetine (drug)]] 5 µM 0.0654× (z -8.5) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 6.85 | 0 | 1 | — | [[Fluvoxamine (drug)]] 5 µM 0.0550× (z -10.3) |
| [[A-427 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.23 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.83 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13641), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT6P3]] | +0.63 | +0.65 / +0.56 | both halves | 1e-05 | same gene group |
| [[QTRT2]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ZNF777]] | +0.61 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[NADK2]] | +0.60 | +0.67 / +0.32 | both halves | 2e-04 |  |
| [[C8orf33]] | +0.60 | +0.65 / +0.23 | both halves | 5e-04 |  |
| [[SLC25A38]] | +0.59 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[PRR3]] | +0.59 | +0.59 / +0.32 | both halves | 2e-04 |  |
| [[SRSF8]] | +0.59 | +0.60 / +0.36 | both halves | 1e-04 |  |
| [[ZNF343]] | +0.58 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[NUDT19]] | +0.58 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[ZFR]] | +0.57 | +0.66 / +0.36 | both halves | 1e-04 |  |
| [[MAPKAPK5]] | +0.57 | +0.52 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C4orf3]] | -0.62 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[SLC35B2]] | -0.61 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[NPTN]] | -0.56 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[ALDOA]] | -0.54 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[JPT1]] | -0.52 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[NXPH4]] | -0.51 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[C1QL1]] | -0.51 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[SH3BGRL3]] | -0.51 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[TXNDC17]] | -0.50 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[PPP1R13B]] | -0.50 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[BRK1]] | -0.50 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[RCOR1]] | -0.49 | -0.50 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC88A]] | B | CCDC88A activity raises CCT6P1's level | lines that do not express CCDC88A (8) vs lines expressing it (42) | 1.28× lower at baseline in the lines without CCDC88A | 0.025 | ⚠ within organs, on part of the lines; also absent: LIX1L, HEG1, CHROMR |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.557). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.9, 18.3); signed map (-3.2, -34.4). **Vector** length 70.3, 11.5% of its response variance represented; |z| ≥ 3 in 1,014 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.8 | +11.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.7 | +9.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.6 | +10.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.0 | +11.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +7.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +9.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.3 | +5.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.4 | +4.6 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.7 | -0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -3.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -1.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.1 | -3.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | chaperonin containing TCP1 family member 6A2, pseudogene |
| Locus type | pseudogene |
| Location | 7q11.21 — chr7:65,751,142-65,763,336 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously CCT6AP1, CCT6P1 |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:33094](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33094) · Entrez [643253](https://www.ncbi.nlm.nih.gov/gene/643253) · Ensembl [ENSG00000228409](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228409)

## Data

Gene col 13641: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13641); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13641, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13641]; `tensor/DDL_lfc|DDL_z.npy` [13641]; `embed/gene_vectors.npy` [13641]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13641 or target_col == 13641). Every well: [[CCT6P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCT6P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
