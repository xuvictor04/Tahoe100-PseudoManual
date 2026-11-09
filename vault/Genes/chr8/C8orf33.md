---
symbol: "C8orf33"
type: "gene"
col: 11270
ensembl_id: "ENSG00000182307"
name: "chromosome 8 open reading frame 33"
location: "8q24.3"
module: 148
arm: "+"
pooled_cpm: 27.45
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# C8orf33

*chromosome 8 open reading frame 33* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.67× (z +16.3, q 0e+00, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS52]] (+0.73, fdr 3e-05), [[PEF1]] (+0.73, fdr 6e-05), [[POLDIP2]] (+0.72, fdr 7e-06); moves opposite to [[HMGN3]] (-0.63, fdr 3e-05), [[PEDS1]] (-0.62, fdr 9e-05), [[RADX]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 148]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11270.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.67×** | +16.3 | 0e+00 | 47/48 (Panc 03.27, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.66×** | +15.3 | 0e+00 | 42/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.18×** | +13.1 | 7e-37 | 32/33 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.78×** | +11.2 | 1e-26 | 36/40 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.11×** | +8.5 | 3e-15 | 37/45 (NCI-H1573, RKO, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.98×** | +8.0 | 1e-13 | 40/48 (NCI-H2030, SW480, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.58×** | +7.6 | 2e-12 | 32/47 (NCI-H1792, NCI-H2030, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.88×** | +7.4 | 8e-12 | 42/48 (LOX-IMVI, MIA PaCa-2, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.85×** | +7.2 | 3e-11 | 34/47 (NCI-H1792, A549, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +6.7 | 1e-09 | 37/48 (A-172, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.64×** | +5.6 | 1e-06 | 34/47 (NCI-H2030, A498, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +5.5 | 1e-06 | 27/46 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.4 | 2e-06 | 31/48 (SW1417, Hs 766T, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.56×** | +4.8 | 6e-05 | 30/46 (NCI-H460, MIA PaCa-2, …) | all doses, flat | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.49×** | +4.7 | 1e-04 | 27/45 (PANC-1, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.006 | 25/47 (HOP62, SK-MEL-2, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.81×** | +3.6 | 0.009 | 22/48 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.015 | 22/48 (BT-474, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +2.9 | 0.079 | 15/47 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.29×** | +2.9 | 0.095 | 15/46 (HT-29, HCT15, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11270.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.733× | -3.7 | 0.12 | 24/47 (HOP62, SW 1271, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.821× | -3.3 | 0.25 | 22/48 (MIA PaCa-2, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11270. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 61.2 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +12.5) | — |
| [[HOP62 (line)]] | alt | 22.8 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +12.8) | — |
| [[NCI-H460 (line)]] | wt | 16.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.82× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +12.5) | — |
| [[SW480 (line)]] | alt | 28.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.19× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +10.4) | — |
| [[HEC-1-A (line)]] | alt | 30.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.74× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +10.6) | — |
| [[Hs 766T (line)]] | wt | 30.7 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +10.7) | — |
| [[HT-29 (line)]] | alt | 17.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.86× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +10.1) | — |
| [[KATO III (line)]] | alt | 38.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.35× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[LoVo (line)]] | wt | 18.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.06× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1792 (line)]] | alt | 15.7 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.15× (z +13.8) | — |
| [[NCI-H2030 (line)]] | alt | 28.4 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +12.5) | — |
| [[SW1417 (line)]] | alt | 42.9 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +12.9) | — |
| [[A549 (line)]] | wt | 28.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 38.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +13.2) | — |
| [[LOX-IMVI (line)]] | wt | 35.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 28.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.86× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 24.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 24.2 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.41× (z +10.4) ⚠ toxic | — |
| [[SNU-423 (line)]] | alt | 15.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.83× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +9.0) | — |
| [[A-172 (line)]] | wt | 18.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +11.3) | — |
| [[A-427 (line)]] | wt | 31.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.24× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[BT-474 (line)]] | alt | 33.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 14.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +10.2) | — |
| [[H4 (line)]] | wt | 22.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +9.1) | — |
| [[J82 (line)]] | alt | 32.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 26.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.47× (z +14.7) | — |
| [[PANC-1 (line)]] | alt | 24.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +11.9) | — |
| [[RKO (line)]] | wt | 51.0 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.31× (z +9.4) ⚠ toxic | — |
| [[RPMI-7951 (line)]] | alt | 27.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.97× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 43.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 25.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 17.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11270), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS52]] | +0.73 | +0.73 / +0.45 | both halves | 3e-05 |  |
| [[PEF1]] | +0.73 | +0.76 / +0.38 | both halves | 6e-05 |  |
| [[POLDIP2]] | +0.72 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[PSME3IP1]] | +0.70 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[MAPKAPK5]] | +0.70 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[MTHFSD]] | +0.68 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[ZNF621]] | +0.68 | +0.68 / +0.31 | both halves | 2e-04 |  |
| [[ANGEL2]] | +0.68 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[TRMT5]] | +0.68 | +0.75 / +0.46 | both halves | 3e-05 |  |
| [[ZNF543]] | +0.67 | +0.65 / +0.41 | both halves | 4e-05 |  |
| [[RPAP2]] | +0.67 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[PCBP1-AS1]] | +0.66 | +0.64 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGN3]] | -0.63 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[PEDS1]] | -0.62 | -0.57 / -0.36 | both halves | 9e-05 |  |
| [[RADX]] | -0.61 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[PCMT1]] | -0.61 | -0.61 / -0.25 | both halves | 4e-04 |  |
| [[GUSBP18]] | -0.60 | -0.57 / -0.29 | both halves | 2e-04 |  |
| [[COX6A1]] | -0.60 | -0.64 / -0.24 | both halves | 5e-04 |  |
| [[TNFAIP8L1]] | -0.60 | -0.53 / -0.29 | both halves | 2e-04 |  |
| [[FCHO1]] | -0.60 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[FAM118A]] | -0.59 | -0.59 / -0.24 | both halves | 5e-04 |  |
| [[CABLES2]] | -0.59 | -0.55 / -0.24 | both halves | 4e-04 |  |
| [[TSPAN33]] | -0.58 | -0.41 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers C8orf33's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ST3GAL5]] | B | ST3GAL5 activity lowers C8orf33's level | lines that do not express ST3GAL5 (7) vs lines expressing it (43) | 1.32× higher at baseline in the lines without ST3GAL5 | 0.048 | ⚠ within organs, on part of the lines; also absent: NR2F2-AS1; maybe low, not absent |
| [[PSME3IP1]] | C | PSME3IP1's natural level strengthens C8orf33's drug response | PSME3IP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64, reverse -0.08; direction not clear | 0.061 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **+** arm (projection on the module's main direction 0.816). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-10.7, 7.2); signed map (14.9, -25.8). **Vector** length 76.3, 17.8% of its response variance represented; |z| ≥ 3 in 924 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +16.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.3 | +7.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.1 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | +7.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +5.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.8 | +4.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -3.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.9 | -1.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.7 | -2.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -4.7 | -3.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.5 | +0.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.4 | -0.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 8 open reading frame 33 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:145,052,465-145,066,685 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20989 |
| Matched by | ensembl_id |

UniProt [Q9H7E9](https://www.uniprot.org/uniprotkb/Q9H7E9) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26104](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26104) · Entrez [65265](https://www.ncbi.nlm.nih.gov/gene/65265) · UniProt [Q9H7E9](https://www.uniprot.org/uniprotkb/Q9H7E9) · Ensembl [ENSG00000182307](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182307)

## Data

Gene col 11270: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11270); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11270, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11270]; `tensor/DDL_lfc|DDL_z.npy` [11270]; `embed/gene_vectors.npy` [11270]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11270 or target_col == 11270). Every well: [[C8orf33 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C8orf33.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
