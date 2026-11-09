---
symbol: "AARS2"
type: "gene"
col: 4551
ensembl_id: "ENSG00000124608"
name: "alanyl-tRNA synthetase 2, mitochondrial"
location: "6p21.1"
module: 107
arm: "+"
pooled_cpm: 12.65
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 18
n_dd_up_clean: 2
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# AARS2

*alanyl-tRNA synthetase 2, mitochondrial* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.61× (z +7.7, q 7e-12, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.529× (z -10.3, q 7e-22, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR2C]] (+0.68, fdr 1e-05), [[PSMD3]] (+0.65, fdr 7e-06), [[ABCF3]] (+0.64, fdr 1e-05); moves opposite to [[LINC01208]] (-0.56, fdr 9e-05), [[RBM3]] (-0.55, fdr 3e-05), [[FAM81A]] (-0.54, fdr 2e-05).
> It is in [[Module 107]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4551.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +7.7 | 7e-12 | 29/47 (SNU-423, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.53×** | +6.9 | 1e-09 | 27/48 (LS 180, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.39×** | +5.3 | 2e-05 | 22/47 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +5.2 | 3e-05 | 20/48 (LOX-IMVI, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.35×** | +4.9 | 1e-04 | 17/47 (LS 180, A-427, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.5 | 0.037 | 7/35 (SNU-1, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~23% here); noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.23×** | +3.4 | 0.061 | 10/43 (hTERT-HPNE, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.23×** | +3.3 | 0.065 | 9/47 (RKO, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.17 | 12/47 (SW48, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4551.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.529×** | -10.3 | 7e-22 | 32/47 (KATO III, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.554×** | -9.5 | 4e-19 | 37/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -8.5 | 4e-15 | 33/46 (SNU-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.610×** | -8.0 | 2e-13 | 30/47 (SW48, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.633×** | -7.4 | 2e-11 | 27/46 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.629×** | -7.2 | 7e-11 | 26/48 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.436×** | -7.0 | 2e-10 | 30/48 (MIA PaCa-2, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.657×** | -6.5 | 6e-09 | 25/46 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.693×** | -5.9 | 2e-07 | 21/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.693×** | -5.7 | 8e-07 | 21/42 (NCI-H460, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.756×** | -4.5 | 4e-04 | 19/47 (SW480, NCI-H23, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.823×** | -4.4 | 5e-04 | 17/47 (H4, RPMI-7951, …) | rises with dose | composition shift |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.804×** | -3.5 | 0.020 | 10/47 (SW1417, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Tetracycline (hydrochloride) (drug)]] 0.5 µM |  | **0.806×** | -3.5 | 0.022 | 9/47 (SK-MEL-2, SW1417, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.669×** | -3.4 | 0.027 | 12/44 (LS 180, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **0.815×** | -3.1 | 0.058 | 7/47 (SW 1271, Panc 03.27, …) | top dose only |  |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | **0.830×** | -3.0 | 0.089 | 6/48 (HS-578T, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4551. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.12 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0676× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.198× (z -11.2) |
| [[KATO III (line)]] | alt | 19.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0755× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.293× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 14.5 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.165× (z -8.7) ⚠ transcription drop |
| [[AsPC-1 (line)]] | alt | 5.14 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0916× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0719× (z -10.3) ⚠ transcription drop |
| [[H4 (line)]] | wt | 26.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -9.0) ⚠ cell-cycle shift, explains ~76% of this change |
| [[HCT15 (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.206× (z -8.7) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 17.2 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 8.41 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0739× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 11.1 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0705× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 12.5 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0426× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 9.99 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 16.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -11.6) |
| [[SNU-1 (line)]] | wt | 18.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -10.3) |
| [[SW48 (line)]] | wt | 16.7 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0499× (z -13.2) |
| [[A-172 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4551), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2C]] | +0.68 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[PSMD3]] | +0.65 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[ABCF3]] | +0.64 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[MIER2]] | +0.63 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[TRMT2A]] | +0.61 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[OSBPL7]] | +0.61 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[NSFL1C]] | +0.60 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[FAHD2B]] | +0.59 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[WRAP73]] | +0.59 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[MKRN2]] | +0.59 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[BRF2]] | +0.59 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[HERC2P2]] | +0.58 | +0.48 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01208]] | -0.56 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[RBM3]] | -0.55 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[FAM81A]] | -0.54 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[SAXO1]] | -0.53 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[TBCE-1]] | -0.53 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[HCG17]] | -0.53 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[LINC02646]] | -0.52 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[H2AZ1-DT]] | -0.52 | -0.35 / -0.30 | both halves | 2e-04 |  |
| [[CASS4]] | -0.52 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[RNF170]] | -0.51 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[COLEC11]] | -0.51 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[LSMEM1]] | -0.51 | -0.33 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers AARS2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers AARS2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DAGLA]] | C | DAGLA activity raises AARS2's level | lines that do not express DAGLA (4) vs lines expressing it (46) | 1.74× lower at baseline in the lines without DAGLA | 0.046 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PLEKHF1, NBEAP2, C2orf27A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.458). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.8, -5.1); signed map (-23.5, -22.5). **Vector** length 76.7, 13.4% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +5.3 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +3.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.5 | +5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +3.3 | +3.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.7 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +1.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.3 | -8.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -7.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -4.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.1 | -5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | +0.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | alanyl-tRNA synthetase 2, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:44,298,731-44,313,347 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1270, bA444E17.1; previously AARSL |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class II |
| Reactome | 3 pathways, smallest: Mitochondrial tRNA aminoacylation; tRNA Aminoacylation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JTZ9](https://www.uniprot.org/uniprotkb/Q5JTZ9) (Alanine--tRNA ligase, mitochondrial):

> Catalyzes the attachment of alanine to tRNA(Ala) in a two-step reaction: alanine is first activated by ATP to form Ala-AMP and then transferred to the acceptor end of tRNA(Ala). Also edits incorrectly charged tRNA(Ala) via its editing domain. In presence of high levels of lactate, also acts as a protein lactyltransferase that mediates lactylation of lysine residues in target proteins, such as CGAS. Acts as an inhibitor of cGAS/STING signaling by catalyzing lactylation of CGAS, preventing the …

**Summary**, from NCBI Gene [57505](https://www.ncbi.nlm.nih.gov/gene/57505):

> The protein encoded by this gene belongs to the class-II aminoacyl-tRNA synthetase family. Aminoacyl-tRNA synthetases play critical roles in mRNA translation by charging tRNAs with their cognate amino acids. The encoded protein is a mitochondrial enzyme that specifically aminoacylates alanyl-tRNA. Mutations in this gene are a cause of combined oxidative phosphorylation deficiency 8. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:21022](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21022) · Entrez [57505](https://www.ncbi.nlm.nih.gov/gene/57505) · UniProt [Q5JTZ9](https://www.uniprot.org/uniprotkb/Q5JTZ9) · Ensembl [ENSG00000124608](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124608)

## Data

Gene col 4551: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4551); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4551, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4551]; `tensor/DDL_lfc|DDL_z.npy` [4551]; `embed/gene_vectors.npy` [4551]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4551 or target_col == 4551). Every well: [[AARS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AARS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
