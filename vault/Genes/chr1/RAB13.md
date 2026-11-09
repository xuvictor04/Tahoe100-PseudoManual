---
symbol: "RAB13"
type: "gene"
col: 6766
ensembl_id: "ENSG00000143545"
name: "RAB13, member RAS oncogene family"
location: "1q21.3"
module: 74
arm: "+"
pooled_cpm: 78.12
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# RAB13

*RAB13, member RAS oncogene family* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.03× (z +11.2, q 2e-26, up in 46 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Docetaxel (Trihydrate) (drug)]] 0.5 µM: 1.52× (z +4.3, q 0.002, up in 38 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (A-172 4.92×, NCI-H1573 4.45×, SW480 3.90×, LoVo 4.45×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 6 lines (A-172 3.74×, A549 3.37×, RKO 3.11×, A498 2.76×, …; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 4.82×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.627× (z -4.7, q 0.001, down in 38 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-901 (drug)]] 0.05 µM: 0.661× (z -3.9, q 0.019, down in 35 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBXN1]] (+0.68, fdr 7e-06), [[OGA]] (+0.62, fdr 1e-05), [[ABCA5]] (+0.61, fdr 1e-05); moves opposite to [[XXYLT1]] (-0.60, fdr 3e-05), [[SIGMAR1]] (-0.60, fdr 1e-05), [[NME1]] (-0.58, fdr 1e-05).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BASP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6766.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (A-172 4.92×, NCI-H1573 4.45×, SW480 3.90×, LoVo 4.45×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 6 lines (A-172 3.74×, A549 3.37×, RKO 3.11×, A498 2.76×, …; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 4.82×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.03×** | +11.2 | 2e-26 | 46/47 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.58×** | +9.2 | 1e-17 | 41/42 (SHP-77, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.28×** | +8.3 | 1e-14 | 46/46 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +6.0 | 2e-07 | 39/44 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.52×** | +4.3 | 0.002 | 38/47 (RKO, SNU-423, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.27×** | +3.5 | 0.052 | 34/47 (NCI-H2030, CHP-212, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6766.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.627×** | -4.7 | 0.001 | 38/47 (AsPC-1, NCI-H460, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.661×** | -3.9 | 0.019 | 35/46 (Panc 03.27, hTERT-HPNE, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.478×** | -3.9 | 0.019 | 35/47 (Hs 766T, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.507×** | -3.6 | 0.048 | 32/48 (LOX-IMVI, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.720× | -3.1 | 0.24 | 30/47 (NCI-H460, A-427, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.723× | -3.0 | 0.24 | 33/47 (HepG2/C3A, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6766. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 77.0 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +15.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[PANC-1 (line)]] | alt | 64.4 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 89.9 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +11.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 92.8 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +13.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 86.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +10.4) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.368× (z -8.7) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 120 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +10.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 66.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +9.6) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 74.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.20× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 64.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +11.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 126 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +10.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 96.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +11.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SHP-77 (line)]] | alt | 82.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.82× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 62.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 1088 (line)]] | alt | 102 | 0 | 2 | — | [[Vilanterol (drug)]] 0.05 µM 0.0823× (z -9.1) |
| [[A-427 (line)]] | wt | 93.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +10.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 73.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.343× (z -8.9) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 45.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +9.9) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 103 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 45.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +10.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 47.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.69× (z +9.2) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 89.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[KATO III (line)]] | alt | 46.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.18× (z +9.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 56.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +11.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 171 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 81.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +8.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 92.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +8.6) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -9.5) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SNU-423 (line)]] | alt | 88.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 55.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.96× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 43.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +11.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.00 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 62.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 96.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 68.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 158 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 102 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 94.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6766), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBXN1]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[OGA]] | +0.62 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[ABCA5]] | +0.61 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[ITSN2]] | +0.61 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[UBE2B]] | +0.60 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[UPF3B]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[WDR48]] | +0.59 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[ANKRD12]] | +0.59 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[PNRC1]] | +0.59 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[ZCRB1]] | +0.58 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[ZFYVE1]] | +0.57 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[CHMP4A]] | +0.57 | +0.55 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XXYLT1]] | -0.60 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[SIGMAR1]] | -0.60 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[NME1]] | -0.58 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[NSUN2]] | -0.58 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[EIF5A]] | -0.58 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[URB1]] | -0.57 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[DPAGT1]] | -0.56 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[TBRG4]] | -0.56 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[C1QBP]] | -0.56 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[TMEM109]] | -0.56 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[LRP8]] | -0.56 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[SLC25A10]] | -0.55 | -0.50 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BASP1]] | B | BASP1 activity raises RAB13's level | lines that do not express BASP1 (24) vs lines expressing it (26) | 1.55× lower at baseline in the lines without BASP1 | 0.067 | ⚠ within organs, on part of the lines; also absent: S1PR3, VEGFC, SRGN |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.692). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.5, -42.4); signed map (-15.2, 6.2). **Vector** length 90.2, 29.8% of its response variance represented; |z| ≥ 3 in 667 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.0 | +0.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | +2.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +1.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +1.5 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.8 | +0.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.5 | +1.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.4 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.4 | +4.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.1 | +1.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.1 | -4.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.0 | -1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.7 | -1.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.5 | -1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.2 | +0.3 |
|  | [[EX229 (drug)]] 5 µM |  | -3.0 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | RAB13, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:153,981,617-153,986,358 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 6 pathways, smallest: RAB geranylgeranylation; Translocation of SLC2A4 (GLUT4) to the plasma membrane; RAB GEFs exchange GTP for GDP on RABs |
| Matched by | ensembl_id |

**Function**, from UniProt [P51153](https://www.uniprot.org/uniprotkb/P51153) (Ras-related protein Rab-13):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. RAB13 is involved in endocytic recycling and regulates the transport to the plasma membrane of transmembrane proteins …

**Summary**, from NCBI Gene [5872](https://www.ncbi.nlm.nih.gov/gene/5872):

> This gene is a member of the Rab family of small G proteins and plays a role in regulating membrane trafficking between trans-Golgi network (TGN) and recycling endosomes (RE). The encoded protein is involved in the assembly of tight junctions, which are components of the apical junctional complex (AJC) of epithelial cells. The AJC plays a role in forming a barrier between luminal contents and the underlying tissue. Additional functions associated with the protein include endocytic recycling of …

**Accessions** — [HGNC:9762](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9762) · Entrez [5872](https://www.ncbi.nlm.nih.gov/gene/5872) · UniProt [P51153](https://www.uniprot.org/uniprotkb/P51153) · Ensembl [ENSG00000143545](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143545)

## Data

Gene col 6766: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6766); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6766, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6766]; `tensor/DDL_lfc|DDL_z.npy` [6766]; `embed/gene_vectors.npy` [6766]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6766 or target_col == 6766). Every well: [[RAB13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
