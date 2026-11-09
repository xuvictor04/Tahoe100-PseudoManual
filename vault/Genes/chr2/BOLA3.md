---
symbol: "BOLA3"
type: "gene"
col: 8650
ensembl_id: "ENSG00000163170"
name: "bolA family member 3"
location: "2p13.1"
module: 138
arm: "+"
pooled_cpm: 15.98
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 3
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# BOLA3

*bolA family member 3* — 2p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.73× (z +10.9, q 5e-25, up in 30 of 31 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (NCI-H460 8.26×, NCI-H1792 9.42×, HOP62 6.85×, PANC-1 5.64×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H1792 13.4×, NCI-H460 8.32×, LoVo 11.7×, SW480 7.81×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (AsPC-1 5.20×, NCI-H2347 2.94×; ⚠ cell-cycle shift, explains ~29% of this change).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.587× (z -3.9, q 0.059, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OLA1]] (+0.58, fdr 5e-05), [[FAM104B]] (+0.57, fdr 3e-05), [[TFB1M]] (+0.56, fdr 3e-05); moves opposite to [[GIGYF1]] (-0.65, fdr 1e-05), [[CLCN7]] (-0.60, fdr 1e-05), [[DAZAP2]] (-0.56, fdr 1e-04).
> It is in [[Module 138]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PIK3CB]] → it (grade B ⚠); 1 goes from it, the strongest it → [[TEPSIN]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 10 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8650.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (NCI-H460 8.26×, NCI-H1792 9.42×, HOP62 6.85×, PANC-1 5.64×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H1792 13.4×, NCI-H460 8.32×, LoVo 11.7×, SW480 7.81×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (AsPC-1 5.20×, NCI-H2347 2.94×; ⚠ cell-cycle shift, explains ~29% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **4.73×** | +10.9 | 5e-25 | 30/31 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **6.02×** | +10.4 | 1e-22 | 38/38 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **3.76×** | +9.0 | 6e-17 | 32/34 (KATO III, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.78×** | +5.9 | 4e-07 | 30/46 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.95×** | +4.9 | 1e-04 | 29/43 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +4.8 | 2e-04 | 31/41 (MIA PaCa-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.87×** | +4.6 | 4e-04 | 34/47 (HT-29, COLO 205, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.76×** | +4.1 | 0.003 | 29/48 (HT-29, HOP62, …) | two highest doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.66×** | +3.6 | 0.023 | 25/47 (LOX-IMVI, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.58×** | +3.4 | 0.045 | 24/48 (COLO 205, HT-29, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8650.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.587×** | -3.9 | 0.059 | 27/47 (NCI-H1573, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.378×** | -3.5 | 0.088 | 23/46 (A-427, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.380×** | -3.5 | 0.088 | 29/47 (H4, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.631× | -3.4 | 0.11 | 25/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sapanisertib (drug)]] 5 µM |  | 0.408× | -3.2 | 0.13 | 23/48 (LoVo, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.577× | -3.0 | 0.22 | 23/48 (SK-MEL-2, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.77 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8650. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 18.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.94× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[LoVo (line)]] | wt | 14.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.7× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H1792 (line)]] | alt | 18.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.42× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H460 (line)]] | wt | 21.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.26× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SW480 (line)]] | alt | 15.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.93× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[AsPC-1 (line)]] | alt | 7.13 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.20× (z +9.1) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[HOP62 (line)]] | alt | 15.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.85× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[KATO III (line)]] | alt | 17.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.55× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H2347 (line)]] | alt | 14.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +8.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[PANC-1 (line)]] | alt | 22.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.64× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[A-172 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.97 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.00 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8650), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OLA1]] | +0.58 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[FAM104B]] | +0.57 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[TFB1M]] | +0.56 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[CHD1L]] | +0.55 | +0.41 / +0.39 | both halves | 5e-05 |  |
| [[MRPL17]] | +0.52 | +0.48 / +0.38 | both halves | 6e-05 |  |
| [[SLC25A11]] | +0.51 | +0.37 / +0.46 | both halves | 7e-05 |  |
| [[SDHAF3]] | +0.51 | +0.33 / +0.43 | both halves | 1e-04 | STRING 470 |
| [[MFSD3]] | +0.51 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[SERGEF]] | +0.51 | +0.24 / +0.37 | both halves | 4e-04 |  |
| [[NME1]] | +0.50 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[PDSS1]] | +0.50 | +0.41 / +0.39 | both halves | 6e-05 |  |
| [[IDH2]] | +0.49 | +0.24 / +0.47 | both halves | 4e-04 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GIGYF1]] | -0.65 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[CLCN7]] | -0.60 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[DAZAP2]] | -0.56 | -0.59 / -0.35 | both halves | 1e-04 |  |
| [[MLLT6]] | -0.54 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[ZFTRAF1]] | -0.53 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[RNF103]] | -0.53 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[C11orf54]] | -0.53 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[MAFG]] | -0.52 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[RRAGC-DT]] | -0.51 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[RXRB]] | -0.51 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[GABARAPL1]] | -0.51 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[N4BP2L2]] | -0.50 | -0.44 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIK3CB]] | B | PIK3CB activity raises BOLA3's level | compounds that target PIK3CB: 2 of 3 lower it (Bimiralisib, GSK1059615) | 67% of the class's compounds vs 0.8% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers BOLA3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PIK3CA]] | B | PIK3CA activity raises BOLA3's level | compounds that target PIK3CA: 2 of 4 lower it (Bimiralisib, GSK1059615) | 50% of the class's compounds vs 0.8% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TEPSIN]] | C | BOLA3's natural level strengthens TEPSIN's drug response | BOLA3's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.05; direction not clear | 0.048 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction -0.471). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.1, -21.6); signed map (-22.5, -3.6). **Vector** length 52.8, 11.4% of its response variance represented; |z| ≥ 3 in 605 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.3 | +1.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | +1.8 | +4.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.8 | +2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.7 | +0.5 |
|  | [[EX229 (drug)]] 5 µM |  | +1.7 | +1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +0.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | -3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | +0.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.3 | -1.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.0 | -3.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -3.5 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | bolA family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.1 — chr2:74,135,400-74,147,912 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Mitochondrial iron-sulfur assembly components |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53S33](https://www.uniprot.org/uniprotkb/Q53S33) (BolA-like protein 3):

> Acts as a mitochondrial iron-sulfur (Fe-S) cluster assembly factor that facilitates (Fe-S) cluster insertion into a subset of mitochondrial proteins. Probably acts together with NFU1.

**Summary**, from NCBI Gene [388962](https://www.ncbi.nlm.nih.gov/gene/388962):

> This gene encodes a protein that plays an essential role in the production of iron-sulfur (Fe-S) clusters for the normal maturation of lipoate-containing 2-oxoacid dehydrogenases, and for the assembly of the mitochondrial respiratory chain complexes. Mutation in this gene has been associated with multiple mitochondrial dysfunctions syndrome-2. Two alternatively spliced transcript variants encoding different isoforms with distinct subcellular localization have been reported for this gene …

**Accessions** — [HGNC:24415](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24415) · Entrez [388962](https://www.ncbi.nlm.nih.gov/gene/388962) · UniProt [Q53S33](https://www.uniprot.org/uniprotkb/Q53S33) · Ensembl [ENSG00000163170](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163170)

## Data

Gene col 8650: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8650); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8650, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8650]; `tensor/DDL_lfc|DDL_z.npy` [8650]; `embed/gene_vectors.npy` [8650]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8650 or target_col == 8650). Every well: [[BOLA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BOLA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
