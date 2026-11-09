---
symbol: "EMC7"
type: "gene"
col: 5518
ensembl_id: "ENSG00000134153"
name: "ER membrane protein complex subunit 7"
location: "15q14"
module: 183
arm: "+"
pooled_cpm: 34.19
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/183"]
generated_by: "tahoemap"
---

# EMC7

*ER membrane protein complex subunit 7* — 15q14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (19 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.66× (z +11.6, q 2e-28, up in 41 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.27× (z +7.8, q 1e-12, up in 43 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 2 lines (HepG2/C3A 0.202×, AN3 CA 0.0993×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.176×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.0998×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA9]] (+0.61, fdr 1e-05), [[MORN2]] (+0.58, fdr 2e-05), [[LSM1]] (+0.57, fdr 3e-05); moves opposite to [[LINC01399]] (-0.52, fdr 7e-05), [[SLC19A1]] (-0.51, fdr 2e-05), [[ABCA15P]] (-0.49, fdr 4e-05).
> It is in [[Module 183]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 19 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5518.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.66×** | +11.6 | 2e-28 | 41/45 (NCI-H1573, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.61×** | +11.6 | 2e-28 | 36/37 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.09×** | +9.3 | 4e-18 | 43/47 (SW480, NCI-H1573, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.27×** | +7.8 | 1e-12 | 43/49 (SW480, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.82×** | +7.5 | 7e-12 | 44/48 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +7.4 | 1e-11 | 33/48 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.73×** | +6.3 | 2e-08 | 32/40 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.42×** | +6.2 | 3e-08 | 30/47 (A-427, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.62×** | +5.8 | 4e-07 | 34/48 (LS 180, HEC-1-A, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +5.8 | 5e-07 | 38/46 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.0 | 3e-05 | 31/48 (HOP62, Hs 766T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.49×** | +5.0 | 3e-05 | 34/47 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **1.49×** | +5.0 | 3e-05 | 29/46 (HOP62, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.43×** | +4.5 | 2e-04 | 29/48 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.43×** | +4.5 | 2e-04 | 29/47 (HT-29, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +4.5 | 3e-04 | 31/47 (J82, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.94×** | +4.4 | 4e-04 | 29/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.0 | 0.059 | 17/48 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.068 | 14/48 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5518.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 2 lines (HepG2/C3A 0.202×, AN3 CA 0.0993×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.176×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.0998×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.812× | -3.7 | 0.12 | 25/48 (A498, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5518. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 42.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[SW480 (line)]] | alt | 29.5 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.17× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.80× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 34.8 | 0 | 2 | — | [[Verteporfin (drug)]] 5 µM 0.0993× (z -9.7) |
| [[HOP62 (line)]] | alt | 23.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.33× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[KATO III (line)]] | alt | 35.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.76× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H460 (line)]] | wt | 36.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.41× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A-427 (line)]] | wt | 18.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.65× (z +10.2) ⚠ cell-cycle shift, explains ~91% of this change | — |
| [[A498 (line)]] | wt | 54.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.67× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[CFPAC-1 (line)]] | alt | 42.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HepG2_C3A (line)]] | wt | 35.8 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.202× (z -9.7) |
| [[Hs 766T (line)]] | wt | 33.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[HS-578T (line)]] | alt | 34.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[J82 (line)]] | alt | 34.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.75× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 19.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.42× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H1573 (line)]] | alt | 31.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.00× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H1792 (line)]] | alt | 32.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H2030 (line)]] | alt | 51.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.53× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[PANC-1 (line)]] | alt | 34.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[RKO (line)]] | wt | 47.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SK-MEL-2 (line)]] | alt | 36.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.68× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[A-172 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5518), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA9]] | +0.61 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[MORN2]] | +0.58 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[LSM1]] | +0.57 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[ZHX1]] | +0.57 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[ZZEF1]] | +0.55 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[RMDN3]] | +0.55 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[ACOT8]] | +0.54 | +0.57 / +0.50 | both halves | 1e-05 | pathway: Protein localization |
| [[ITM2B]] | +0.54 | +0.39 / +0.53 | both halves | 5e-05 |  |
| [[COPS4]] | +0.52 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[CLPX]] | +0.52 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[FBXO8]] | +0.51 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[SMPD1]] | +0.50 | +0.48 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01399]] | -0.52 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[SLC19A1]] | -0.51 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[ABCA15P]] | -0.49 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[MPP3]] | -0.48 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[SACS]] | -0.47 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[PRR5-ARHGAP8]] | -0.47 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[POLR1E]] | -0.47 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[GNPNAT1]] | -0.46 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[AHCY]] | -0.46 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[IGSF9B]] | -0.46 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[PLEKHO2]] | -0.45 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[NEIL2]] | -0.45 | -0.49 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EMC7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 183]]; 21 genes; every member is in the + arm (projection on the module's main direction 0.288). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-25.4, -9.6); signed map (-9.2, -3.0). **Vector** length 58.6, 11.7% of its response variance represented; |z| ≥ 3 in 862 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +3.7 | +7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.2 | +3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +2.0 | +7.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +0.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +0.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.5 | +0.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.5 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -3.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~63% of this change | -3.0 | +4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -0.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | +0.6 |
|  | [[Auranofin (drug)]] 0.5 µM |  | -1.1 | -0.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.0 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | ER membrane protein complex subunit 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q14 — chr15:34,084,017-34,101,862 (-) |
| Ensembl biotype | protein_coding |
| Also known as | C11orf3; previously C15orf24 |
| Gene groups (HGNC) | ER membrane protein complex subunits |
| Reactome | 2 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPA0](https://www.uniprot.org/uniprotkb/Q9NPA0) (Endoplasmic reticulum membrane protein complex subunit 7):

> Part of the endoplasmic reticulum membrane protein complex (EMC) that enables the energy-independent insertion into endoplasmic reticulum membranes of newly synthesized membrane proteins. Preferentially accommodates proteins with transmembrane domains that are weakly hydrophobic or contain destabilizing features such as charged and aromatic residues. Involved in the cotranslational insertion of multi-pass membrane proteins in which stop-transfer membrane-anchor sequences become ER membrane …

**Summary**, from NCBI Gene [56851](https://www.ncbi.nlm.nih.gov/gene/56851):

> Contributes to membrane insertase activity. Involved in protein insertion into ER membrane by stop-transfer membrane-anchor sequence and tail-anchored membrane protein insertion into ER membrane. Located in endoplasmic reticulum membrane. Part of EMC complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24301](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24301) · Entrez [56851](https://www.ncbi.nlm.nih.gov/gene/56851) · UniProt [Q9NPA0](https://www.uniprot.org/uniprotkb/Q9NPA0) · Ensembl [ENSG00000134153](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134153)

## Data

Gene col 5518: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5518); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5518, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5518]; `tensor/DDL_lfc|DDL_z.npy` [5518]; `embed/gene_vectors.npy` [5518]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5518 or target_col == 5518). Every well: [[EMC7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EMC7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
