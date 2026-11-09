---
symbol: "HSPB1"
type: "gene"
col: 2729
ensembl_id: "ENSG00000106211"
name: "heat shock protein family B (small) member 1"
location: "7q11.23"
module: 60
arm: "+"
pooled_cpm: 92.2
n_lines_expressing: 48
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# HSPB1

*heat shock protein family B (small) member 1* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 7.40× (z +13.4, q 4e-38, up in 46 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SNU-1 0.189×); [[Canagliflozin (drug)]] 5 µM in 1 line (SW 1271 0.0595×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SOD1]] (+0.78, fdr 7e-06), [[CRYAB]] (+0.69, fdr 7e-06), [[HSPA1B]] (+0.69, fdr 7e-06); moves opposite to [[ENTR1]] (-0.60, fdr 1e-05), [[ODF2]] (-0.58, fdr 1e-05), [[NT5E]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CLU]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2729.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **7.40×** | +13.4 | 4e-38 | 46/46 (C32, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **6.52×** | +12.6 | 1e-33 | 46/46 (SW1417, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **6.14×** | +12.1 | 1e-31 | 46/46 (A-172, A498, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **4.76×** | +9.7 | 4e-20 | 46/46 (A498, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.20×** | +9.6 | 9e-20 | 44/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **10.0×** | +8.1 | 7e-14 | 43/43 (CFPAC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.38×** | +7.8 | 4e-13 | 37/41 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.45×** | +5.5 | 2e-06 | 34/43 (J82, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.36×** | +5.5 | 2e-06 | 38/45 (C32, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **4.28×** | +4.6 | 2e-04 | 39/47 (CFPAC-1, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.93×** | +4.4 | 5e-04 | 36/46 (SW1417, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **3.47×** | +4.3 | 6e-04 | 40/45 (KATO III, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | **1.69×** | +3.4 | 0.030 | 39/46 (SW 1088, SW480, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.63×** | +3.4 | 0.032 | 29/47 (NCI-H1573, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.69×** | +3.3 | 0.032 | 28/46 (NCI-H1573, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.65×** | +3.2 | 0.045 | 31/46 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.65×** | +3.1 | 0.058 | 28/46 (NCI-H23, BT-474, …) | all doses, flat | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.59×** | +3.0 | 0.079 | 25/45 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2729.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SNU-1 0.189×); [[Canagliflozin (drug)]] 5 µM in 1 line (SW 1271 0.0595×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sapanisertib (drug)]] 5 µM |  | 0.383× | -3.4 | 0.16 | 40/47 (LOX-IMVI, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.384× | -3.4 | 0.16 | 34/47 (NCI-H2030, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dabrafenib (drug)]] 5 µM |  | 0.389× | -3.3 | 0.16 | 36/47 (SNU-1, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | 0.395× | -3.2 | 0.16 | 38/46 (HCT15, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.62 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2729. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 96.9 | 6 | 0 | [[Auranofin (drug)]] 5 µM 14.9× (z +14.7) | — |
| [[A-172 (line)]] | wt | 246 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 18.1× (z +16.9) | — |
| [[A498 (line)]] | wt | 448 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 16.7× (z +15.7) | — |
| [[C32 (line)]] | wt | 158 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 38.4× (z +19.1) | — |
| [[CFPAC-1 (line)]] | alt | 73.0 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 11.8× (z +13.5) | — |
| [[HS-578T (line)]] | alt | 81.0 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 19.5× (z +14.6) | — |
| [[NCI-H2347 (line)]] | alt | 192 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.79× (z +14.3) | — |
| [[SHP-77 (line)]] | alt | 55.9 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 16.8× (z +13.5) | — |
| [[SW1417 (line)]] | alt | 62.7 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 18.1× (z +16.4) | — |
| [[A-427 (line)]] | wt | 260 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 12.3× (z +15.3) | — |
| [[AsPC-1 (line)]] | alt | 73.1 | 4 | 0 | [[Auranofin (drug)]] 5 µM 7.52× (z +11.2) | — |
| [[HOP62 (line)]] | alt | 33.3 | 4 | 0 | [[Auranofin (drug)]] 5 µM 26.8× (z +15.2) | — |
| [[J82 (line)]] | alt | 63.1 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.81× (z +10.3) | — |
| [[KATO III (line)]] | alt | 62.5 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 17.7× (z +14.6) | — |
| [[PANC-1 (line)]] | alt | 63.9 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.12× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 5.64× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 58.1 | 4 | 0 | [[Auranofin (drug)]] 5 µM 7.95× (z +10.6) | — |
| [[A549 (line)]] | wt | 63.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 9.11× (z +10.6) | — |
| [[HT-29 (line)]] | alt | 28.2 | 3 | 0 | [[Auranofin (drug)]] 5 µM 14.2× (z +12.5) | — |
| [[LOX-IMVI (line)]] | wt | 68.4 | 3 | 0 | [[Auranofin (drug)]] 5 µM 11.5× (z +12.4) | — |
| [[LS 180 (line)]] | wt | 30.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 17.4× (z +12.4) | — |
| [[Panc 03.27 (line)]] | alt | 32.6 | 3 | 0 | [[Auranofin (drug)]] 5 µM 9.12× (z +10.9) | — |
| [[SW480 (line)]] | alt | 58.8 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.10× (z +10.2) | — |
| [[COLO 205 (line)]] | alt | 37.8 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 10.7× (z +10.2) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 6.67× (z +8.5) | — |
| [[H4 (line)]] | wt | 59.5 | 2 | 0 | [[Auranofin (drug)]] 5 µM 16.9× (z +12.2) | — |
| [[hTERT-HPNE (line)]] | wt | 62.4 | 2 | 0 | [[Auranofin (drug)]] 5 µM 11.4× (z +10.6) | — |
| [[SNU-1 (line)]] | wt | 293 | 1 | 1 | [[Auranofin (drug)]] 5 µM 5.86× (z +11.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.189× (z -10.9) |
| [[SW 1271 (line)]] | alt | 72.1 | 1 | 1 | [[Auranofin (drug)]] 5 µM 17.7× (z +9.4) | [[Canagliflozin (drug)]] 5 µM 0.0595× (z -9.0) |
| [[SW 900 (line)]] | alt | 97.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 7.51× (z +12.1) | — |
| [[AN3 CA (line)]] | alt | 95.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.7× (z +9.9) | — |
| [[BT-474 (line)]] | alt | 80.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.37× (z +13.8) | — |
| [[C-33 A (line)]] | alt | 29.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.43× (z +8.8) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 56.4 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 13.6× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 108 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.18× (z +10.5) | — |
| [[NCI-H1573 (line)]] | alt | 33.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.01× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 58.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.03× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 91.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.34× (z +11.9) | — |
| [[NCI-H460 (line)]] | wt | 45.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.07× (z +10.0) | — |
| [[RKO (line)]] | wt | 61.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.85× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 37.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.64× (z +10.2) | — |
| [[SW 1088 (line)]] | alt | 83.1 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 40.8× (z +9.2) | — |
| [[SW48 (line)]] | wt | 67.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.35× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.3 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.27 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 82.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 185 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2729), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOD1]] | +0.78 | +0.76 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_APOPTOSIS; STRING 666 |
| [[CRYAB]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 | same gene group; pathway: Cellular response to heat stress; STRING 940 |
| [[HSPA1B]] | +0.69 | +0.67 / +0.70 | both halves | 7e-06 | pathway: Attenuation phase; STRING 939 |
| [[DNAJB4]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 | STRING 403 |
| [[UBB]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 | pathway: AUF1 (hnRNP D0) binds and destabilizes mRNA; STRING 772 |
| [[HSPA1A]] | +0.64 | +0.56 / +0.71 | both halves | 1e-05 | pathway: AUF1 (hnRNP D0) binds and destabilizes mRNA; STRING 977 |
| [[GABARAPL1]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[KIF1B]] | +0.60 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[PSMB4]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 | pathway: AUF1 (hnRNP D0) binds and destabilizes mRNA |
| [[HTATIP2]] | +0.59 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[OSBPL1A]] | +0.58 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[ST13]] | +0.58 | +0.64 / +0.57 | both halves | 1e-05 | pathway: Cellular response to heat stress |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENTR1]] | -0.60 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[ODF2]] | -0.58 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[NT5E]] | -0.53 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[TBCCD1]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[APEH]] | -0.50 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[FAM3C]] | -0.50 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[MSH5]] | -0.50 | -0.43 / -0.51 | both halves | 4e-05 |  |
| [[PPP3CB]] | -0.49 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[CTU2]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[SPRED1]] | -0.48 | -0.52 / -0.48 | both halves | 2e-05 | pathway: MAPK family signaling cascades |
| [[SEPTIN10]] | -0.48 | -0.55 / -0.36 | both halves | 9e-05 |  |
| [[DGUOK]] | -0.47 | -0.48 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLU]] | B | CLU activity strengthens HSPB1's drug response | lines that do not express CLU (10) vs lines expressing it (37) | the lines without CLU respond 1.13× as strongly (z diff -0.13); strongest at Dinaciclib 0.5 µM: 2.50x vs 4.27x (z diff +2.5) | 0.033 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[ALDH2]] | B | ALDH2 activity lowers HSPB1's level | lines that do not express ALDH2 (9) vs lines expressing it (41) | 2.02× higher at baseline in the lines without ALDH2 | 0.043 | ⚠ within organs, on part of the lines; also absent: MTARC2, SLC12A7; maybe low, not absent |
| [[ABCC2]] | B | ABCC2 activity weakens HSPB1's drug response | lines that do not express ABCC2 (22) vs lines expressing it (25) | the lines without ABCC2 respond 1.06× as strongly (z diff -0.19); strongest at Bortezomib 0.05 µM: 6.10x vs 4.63x (z diff -1.4) | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, NR0B1, DNAJC12; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.577). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-17.8, -10.8); signed map (-24.1, -27.5). **Vector** length 116, 44.3% of its response variance represented; |z| ≥ 3 in 1,070 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial unfolded protein response (UPRmt)* (reactome, mean cos +0.51 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +12.3 | +12.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +11.8 | +9.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +11.1 | +12.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.4 | +13.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +7.4 | +8.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.2 | +2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +6.1 | +3.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.9 | +4.6 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -2.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.4 | +9.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | -0.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.3 | -1.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.1 | -0.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.8 | +0.3 |
|  | [[EX229 (drug)]] 0.5 µM |  | -1.6 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | heat shock protein family B (small) member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:76,302,673-76,304,295 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSP27, HSP28, Hs.76067, Hsp25, CMT2F |
| Gene groups (HGNC) | Small heat shock proteins |
| Hallmark sets | APICAL_SURFACE, APOPTOSIS |
| Reactome | 18 pathways, smallest: Attenuation phase; HSF1 activation; HSF1-dependent transactivation |
| Matched by | ensembl_id |

**Function**, from UniProt [P04792](https://www.uniprot.org/uniprotkb/P04792) (Heat shock protein beta-1):

> Small heat shock protein which functions as a molecular chaperone probably maintaining denatured proteins in a folding-competent state. Plays a role in stress resistance and actin organization. Through its molecular chaperone activity may regulate numerous biological processes including the phosphorylation and the axonal transport of neurofilament proteins.

**Summary**, from NCBI Gene [3315](https://www.ncbi.nlm.nih.gov/gene/3315):

> This gene encodes a member of the small heat shock protein (HSP20) family of proteins. In response to environmental stress, the encoded protein translocates from the cytoplasm to the nucleus and functions as a molecular chaperone that promotes the correct folding of other proteins. This protein plays an important role in the differentiation of a wide variety of cell types. Expression of this gene is correlated with poor clinical outcome in multiple human cancers, and the encoded protein may …

**Accessions** — [HGNC:5246](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5246) · Entrez [3315](https://www.ncbi.nlm.nih.gov/gene/3315) · UniProt [P04792](https://www.uniprot.org/uniprotkb/P04792) · Ensembl [ENSG00000106211](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106211)

## Data

Gene col 2729: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2729); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2729, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2729]; `tensor/DDL_lfc|DDL_z.npy` [2729]; `embed/gene_vectors.npy` [2729]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2729 or target_col == 2729). Every well: [[HSPB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSPB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
