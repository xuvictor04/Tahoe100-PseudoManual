---
symbol: "C9orf40"
type: "gene"
col: 5638
ensembl_id: "ENSG00000135045"
name: "chromosome 9 open reading frame 40"
location: "9q21.13"
module: 71
arm: "+"
pooled_cpm: 7.68
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 11
direction_downstream: 1
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# C9orf40

*chromosome 9 open reading frame 40* — 9q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.03× (z +10.0, q 7e-21, up in 33 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.644× (z -4.2, q 0.019, down in 22 of 42 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.686× (z -3.8, q 0.036, down in 18 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FEN1]] (+0.76, fdr 7e-06), [[LRR1]] (+0.72, fdr 7e-06), [[ZNF367]] (+0.67, fdr 9e-06); moves opposite to [[ST13]] (-0.60, fdr 1e-05), [[CLIP3]] (-0.56, fdr 4e-05), [[VTI1B]] (-0.53, fdr 6e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5638.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +10.0 | 7e-21 | 33/42 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **1.83×** | +6.0 | 5e-07 | 16/28 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **1.85×** | +5.9 | 6e-07 | 9/14 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +5.8 | 1e-06 | 18/30 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.59×** | +4.5 | 8e-04 | 18/39 (SW480, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +4.3 | 0.002 | 15/46 (SW480, HT-29, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.32×** | +3.9 | 0.009 | 14/46 (PANC-1, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~61% of this change | **1.46×** | +3.8 | 0.011 | 10/30 (NCI-H2347, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.015 | 13/45 (HOP62, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | **1.44×** | +3.6 | 0.016 | 16/38 (SHP-77, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.39×** | +3.3 | 0.048 | 11/45 (H4, HEC-1-A, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.39×** | +3.2 | 0.066 | 12/41 (SW480, HOP62, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **1.81×** | +3.1 | 0.086 | 3/26 (HOP62, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5638.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.644×** | -4.2 | 0.019 | 22/42 (HEC-1-A, Panc 03.27, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.686×** | -3.8 | 0.036 | 18/46 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.771×** | -3.7 | 0.036 | 9/46 (CFPAC-1, A-427, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.496×** | -3.7 | 0.036 | 13/43 (PANC-1, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | **0.779×** | -3.5 | 0.048 | 8/47 (Panc 03.27, J82, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.727× | -3.2 | 0.13 | 10/45 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.547× | -3.1 | 0.13 | 13/40 (A-172, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.736× | -3.1 | 0.15 | 7/47 (SNU-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.808× | -3.0 | 0.16 | 17/42 (A-172, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5638. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 10.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -11.2) |
| [[PANC-1 (line)]] | alt | 9.58 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -8.9) |
| [[A-427 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.70 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5638), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FEN1]] | +0.76 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[LRR1]] | +0.72 | +0.69 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[ZNF367]] | +0.67 | +0.71 / +0.57 | both halves | 9e-06 |  |
| [[MCM10]] | +0.66 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[CDC7]] | +0.66 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[RFWD3]] | +0.66 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[ASF1B]] | +0.65 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[DDIAS]] | +0.65 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[FANCC]] | +0.64 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[GINS1]] | +0.63 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[HMGB1P5]] ⚠ | +0.63 | +0.58 / +0.66 | both halves | 8e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[THSD4-AS1]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[PKMYT1]] | +0.63 | +0.58 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST13]] | -0.60 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[CLIP3]] | -0.56 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[VTI1B]] | -0.53 | -0.38 / -0.60 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 5, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises C9orf40's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.64× lower at baseline in the lines without E2F2 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises C9orf40's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.01× lower at baseline in the lines without CDC25A | 0.030 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises C9orf40's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DLX1]] | B | DLX1 activity raises C9orf40's level | lines that do not express DLX1 (13) vs lines expressing it (37) | 1.48× lower at baseline in the lines without DLX1 | 0.084 | ⚠ within organs, on part of the lines; also absent: TMEM145, GXYLT2, FSD1 |
| [[TOP2A]] | B | TOP2A activity lowers C9orf40's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CENPP]] | C | CENPP activity raises C9orf40's level | lines that do not express CENPP (4) vs lines expressing it (46) | 2.31× lower at baseline in the lines without CENPP | 0.010 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises C9orf40's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.04× lower at baseline in the lines without AURKB | 0.011 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[E2F1]] | C | E2F1 activity raises C9orf40's level | lines that do not express E2F1 (3) vs lines expressing it (47) | 2.35× lower at baseline in the lines without E2F1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p |
| [[MELK]] | C | MELK activity raises C9orf40's level | lines that do not express MELK (3) vs lines expressing it (47) | 2.12× lower at baseline in the lines without MELK | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[PKMYT1]] | C | PKMYT1 activity raises C9orf40's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 1.89× lower at baseline in the lines without PKMYT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent; its own permutation p |
| [[MCM10]] | C | MCM10 activity raises C9orf40's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.07× lower at baseline in the lines without MCM10 | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | C9orf40's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | C9orf40's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.59 | 0.491 over the table, 0.077 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.650). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.0, -48.6); signed map (-42.1, -44.9). **Vector** length 60.3, 10.0% of its response variance represented; |z| ≥ 3 in 750 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +10.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +3.1 | +4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +2.8 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +1.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +0.7 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | -3.8 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.8 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -3.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.4 | -1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.2 | -0.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 9 open reading frame 40 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.13 — chr9:74,946,583-74,952,912 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10110 |
| Matched by | ensembl_id |

UniProt [Q8IXQ3](https://www.uniprot.org/uniprotkb/Q8IXQ3) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:23433](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23433) · Entrez [55071](https://www.ncbi.nlm.nih.gov/gene/55071) · UniProt [Q8IXQ3](https://www.uniprot.org/uniprotkb/Q8IXQ3) · Ensembl [ENSG00000135045](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135045)

## Data

Gene col 5638: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5638); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5638, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5638]; `tensor/DDL_lfc|DDL_z.npy` [5638]; `embed/gene_vectors.npy` [5638]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5638 or target_col == 5638). Every well: [[C9orf40 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C9orf40.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
