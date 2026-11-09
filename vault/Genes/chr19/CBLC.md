---
symbol: "CBLC"
type: "gene"
col: 6613
ensembl_id: "ENSG00000142273"
name: "Cbl proto-oncogene C"
location: "19q13.32"
module: 31
arm: "+"
pooled_cpm: 10.21
n_lines_expressing: 19
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 54
direction_downstream: 77
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# CBLC

*Cbl proto-oncogene C* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.80× (z +9.0, q 1e-16, up in 0 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.82× (z +7.7, q 3e-12, up in 16 of 17 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 8 lines (HT-29 0.140×, LS 180 0.109×, HEC-1-A 0.279×, Panc 03.27 0.221×, …); [[Homoharringtonine (drug)]] 5 µM in 5 lines (LS 180 0.226×, LoVo 0.255×, HT-29 0.302×, NCI-H1573 0.211×, …); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW48 0.0806×, Panc 03.27 0.139×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LS 180 0.126×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPHA1]] (+0.68, fdr 1e-05), [[CRYBG2]] (+0.68, fdr 7e-06), [[ARHGAP8]] (+0.63, fdr 1e-05); moves opposite to [[EFCAB2]] (-0.56, fdr 3e-05), [[LMBRD2]] (-0.56, fdr 1e-05), [[IRAK4]] (-0.52, fdr 1e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 54 arrows point to it, the strongest [[B4GALNT3]] → it (grade B ⚠); 77 go from it, the strongest it → [[TMC6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6613.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.80×** | +9.0 | 1e-16 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.67×** | +8.9 | 2e-16 | 1/14 (HCT15) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.82×** | +7.7 | 3e-12 | 16/17 (PANC-1, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +6.4 | 3e-08 | 1/17 (AsPC-1) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.93×** | +6.0 | 3e-07 | 16/17 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.78×** | +5.3 | 1e-05 | 14/17 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +5.1 | 3e-05 | 7/16 (COLO 205, AsPC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.66×** | +4.6 | 3e-04 | 14/16 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.69×** | +4.4 | 7e-04 | 1/14 (PANC-1) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +4.3 | 9e-04 | 3/17 (SW1417, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.2 | 0.001 | 2/16 (KATO III, COLO 205) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.0 | 0.003 | 2/16 (COLO 205, HCT15) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +3.4 | 0.029 | 14/17 (CFPAC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.036 | 9/17 (HEC-1-A, SW1417, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.43×** | +3.3 | 0.039 | 9/17 (CFPAC-1, HCT15, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.045 | 5/17 (CFPAC-1, NCI-H1573, …) | top dose only |  |
| [[Decitabine (drug)]] 0.5 µM |  | **1.40×** | +3.0 | 0.072 | 1/17 (HepG2/C3A) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.59×** | +2.9 | 0.096 | 0/17 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Apalutamide (drug)]] 0.05 µM |  | **1.41×** | +2.9 | 0.096 | 3/17 (HCT15, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6613.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 8 lines (HT-29 0.140×, LS 180 0.109×, HEC-1-A 0.279×, Panc 03.27 0.221×, …); [[Homoharringtonine (drug)]] 5 µM in 5 lines (LS 180 0.226×, LoVo 0.255×, HT-29 0.302×, NCI-H1573 0.211×, …); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW48 0.0806×, Panc 03.27 0.139×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LS 180 0.126×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | 0.703× | -3.5 | 0.11 | 7/17 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.681× | -3.5 | 0.11 | 2/17 (HepG2/C3A, AsPC-1) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.684× | -3.4 | 0.11 | 0/17 | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.699× | -3.0 | 0.32 | 5/17 (AsPC-1, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6613. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 50.1 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -14.3) |
| [[HT-29 (line)]] | alt | 47.4 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.140× (z -20.4) |
| [[KATO III (line)]] | alt | 38.4 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -12.1) |
| [[LS 180 (line)]] | wt | 43.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -20.1) |
| [[Panc 03.27 (line)]] | alt | 40.5 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -13.6) |
| [[SW48 (line)]] | wt | 40.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0806× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -11.9) |
| [[LoVo (line)]] | wt | 28.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -13.1) |
| [[NCI-H1573 (line)]] | alt | 17.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -12.3) |
| [[SW1417 (line)]] | alt | 14.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 16.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -9.9) |
| [[COLO 205 (line)]] | alt | 11.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -10.1) |
| [[HCT15 (line)]] | alt | 17.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -11.3) |
| [[A-172 (line)]] | wt | 0.824 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.738 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.777 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.946 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.951 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.829 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.857 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.926 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.806 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.801 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.874 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.783 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.871 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.866 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.888 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.42 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6613), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPHA1]] | +0.68 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[CRYBG2]] | +0.68 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[ARHGAP8]] | +0.63 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[SH2D3A]] | +0.63 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[FA2H]] | +0.63 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[RASAL1]] | +0.62 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[TMC6]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[BAIAP2L1]] | +0.61 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[HS3ST1]] | +0.61 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[SLC5A1]] | +0.61 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[TMPRSS4]] | +0.60 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[TMEM92]] | +0.60 | +0.48 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB2]] | -0.56 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[LMBRD2]] | -0.56 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[IRAK4]] | -0.52 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[NEK11]] | -0.51 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[PAPOLA]] | -0.51 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[EIF4G2]] | -0.50 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[ATN1]] | -0.50 | -0.19 / -0.45 | ⚠ not reproduced | 9e-04 |  |
| [[ADI1]] | -0.50 | -0.29 / -0.46 | both halves | 2e-04 |  |
| [[PKN2-AS1]] | -0.50 | -0.41 / -0.26 | both halves | 4e-04 |  |
| [[PUS10]] | -0.50 | -0.52 / -0.29 | both halves | 2e-04 |  |
| [[PSME3IP1]] | -0.50 | -0.29 / -0.39 | both halves | 2e-04 |  |
| [[TOR1AIP1]] | -0.50 | -0.37 / -0.44 | both halves | 7e-05 |  |
| [[PCBP1-AS1]] | -0.49 | -0.41 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*54 arrows, 54 of them with an alert ⚠; grade A 0, B 7, C 47. Shown: the 12 strongest; 42 more arrows (42 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B4GALNT3]] | B | B4GALNT3 activity raises CBLC's level | lines that do not express B4GALNT3 (16) vs lines expressing it (34) | 3.42× lower at baseline in the lines without B4GALNT3 | 0.012 | ⚠ within organs, on part of the lines; also absent: MCF2L, EPHA1, PLEKHG6 |
| [[LMTK3]] | B | LMTK3 activity raises CBLC's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 3.68× lower at baseline in the lines without LMTK3 | 0.014 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[MYO1D]] | B | MYO1D activity raises CBLC's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 2.85× lower at baseline in the lines without MYO1D | 0.032 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[CDC42EP5]] | B | CDC42EP5 activity raises CBLC's level | lines that do not express CDC42EP5 (11) vs lines expressing it (39) | 3.13× lower at baseline in the lines without CDC42EP5 | 0.074 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LYPD3]] | B | LYPD3 activity raises CBLC's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 2.84× lower at baseline in the lines without LYPD3 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[TMC6]] | B | TMC6 activity raises CBLC's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 3.24× lower at baseline in the lines without TMC6 | 0.092 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[ACOT11]] | B | ACOT11 activity raises CBLC's level | lines that do not express ACOT11 (11) vs lines expressing it (39) | 3.14× lower at baseline in the lines without ACOT11 | 0.097 | ⚠ within organs, on part of the lines; also absent: GALM, GALNT6, MROH7; maybe low, not absent |
| [[S100A14]] | C | S100A14 activity raises CBLC's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 8.16× lower at baseline in the lines without S100A14 | 1e-05 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises CBLC's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 8.73× lower at baseline in the lines without TMPRSS4 | 1e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[BSPRY]] | C | BSPRY activity raises CBLC's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 6.52× lower at baseline in the lines without BSPRY | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25; co-absent with the target |
| [[ATP2C2]] | C | ATP2C2 activity raises CBLC's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 6.84× lower at baseline in the lines without ATP2C2 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14; co-absent with the target |
| [[ANKRD22]] | C | ANKRD22 activity raises CBLC's level | lines that do not express ANKRD22 (34) vs lines expressing it (16) | 6.39× lower at baseline in the lines without ANKRD22 | 3e-04 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25; co-absent with the target |

### Downstream of this gene

*77 arrows, 77 of them with an alert ⚠; grade A 0, B 34, C 43. Shown: the 12 strongest; 65 more arrows (65 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMC6]] | B | CBLC activity raises TMC6's level | lines that do not express CBLC (31) vs lines expressing it (19) | 4.40× lower at baseline in the lines without CBLC | 4e-04 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[LMTK3]] | B | CBLC activity raises LMTK3's level | lines that do not express CBLC (31) vs lines expressing it (19) | 3.71× lower at baseline in the lines without CBLC | 4e-04 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[ARHGEF16]] | B | CBLC activity raises ARHGEF16's level | lines that do not express CBLC (31) vs lines expressing it (19) | 3.47× lower at baseline in the lines without CBLC | 5e-04 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[ACOT11]] | B | CBLC activity raises ACOT11's level | lines that do not express CBLC (31) vs lines expressing it (19) | 3.40× lower at baseline in the lines without CBLC | 0.001 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[BAIAP2L1]] | B | CBLC activity raises BAIAP2L1's level | lines that do not express CBLC (31) vs lines expressing it (19) | 3.01× lower at baseline in the lines without CBLC | 0.001 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[RDH13]] | B | CBLC activity raises RDH13's level | lines that do not express CBLC (31) vs lines expressing it (19) | 2.26× lower at baseline in the lines without CBLC | 0.002 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[MYO1D]] | B | CBLC activity raises MYO1D's level | lines that do not express CBLC (31) vs lines expressing it (19) | 3.27× lower at baseline in the lines without CBLC | 0.003 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[AMN]] | B | CBLC activity raises AMN's level | lines that do not express CBLC (31) vs lines expressing it (19) | 2.33× lower at baseline in the lines without CBLC | 0.004 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[PTK2B]] | B | CBLC activity raises PTK2B's level | lines that do not express CBLC (31) vs lines expressing it (19) | 2.98× lower at baseline in the lines without CBLC | 0.004 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[VILL]] | B | CBLC activity raises VILL's level | lines that do not express CBLC (31) vs lines expressing it (19) | 2.28× lower at baseline in the lines without CBLC | 0.010 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[B4GALNT3]] | B | CBLC activity raises B4GALNT3's level | lines that do not express CBLC (31) vs lines expressing it (19) | 3.22× lower at baseline in the lines without CBLC | 0.016 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | CBLC activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express CBLC (31) vs lines expressing it (17) | the lines without CBLC: 1.19× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.652). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.8, 55.2); signed map (-1.4, 38.9). **Vector** length 63.7, 22.1% of its response variance represented; |z| ≥ 3 in 369 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +7.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +6.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.8 | +3.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.8 | +4.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +2.3 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +2.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +3.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.7 | +1.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.8 | -2.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -2.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -0.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.7 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | Cbl proto-oncogene C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:44,777,869-44,800,652 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CBL-3, CBL-SL, RNF57 |
| Gene groups (HGNC) | Ring finger proteins; Cbl proto-oncogene family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULV8](https://www.uniprot.org/uniprotkb/Q9ULV8) (E3 ubiquitin-protein ligase CBL-C):

> Acts as an E3 ubiquitin-protein ligase, which accepts ubiquitin from specific E2 ubiquitin-conjugating enzymes, and then transfers it to substrates promoting their degradation by the proteasome. Functionally coupled with the E2 ubiquitin-protein ligases UB2D1, UB2D2 and UB2D3. Regulator of EGFR mediated signal transduction; upon EGF activation, ubiquitinates EGFR. Isoform 1, but not isoform 2, inhibits EGF stimulated MAPK1 activation. Promotes ubiquitination of SRC phosphorylated at 'Tyr-419'. …

**Summary**, from NCBI Gene [23624](https://www.ncbi.nlm.nih.gov/gene/23624):

> This gene encodes a member of the Cbl family of E3 ubiquitin ligases. Cbl proteins play important roles in cell signaling through the ubiquitination and subsequent downregulation of tyrosine kinases. Expression of this gene may be restricted to epithelial cells, and alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:15961](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15961) · Entrez [23624](https://www.ncbi.nlm.nih.gov/gene/23624) · UniProt [Q9ULV8](https://www.uniprot.org/uniprotkb/Q9ULV8) · Ensembl [ENSG00000142273](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142273)

## Data

Gene col 6613: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6613); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6613, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6613]; `tensor/DDL_lfc|DDL_z.npy` [6613]; `embed/gene_vectors.npy` [6613]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6613 or target_col == 6613). Every well: [[CBLC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CBLC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
