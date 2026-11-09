---
symbol: "EVC"
type: "gene"
col: 1034
ensembl_id: "ENSG00000072840"
name: "EvC ciliary complex subunit 1"
location: "4p16.2"
module: 13
arm: "+"
pooled_cpm: 28.87
n_lines_expressing: 37
n_dd_up: 0
n_dd_down: 28
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 28
direction_downstream: 14
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# EVC

*EvC ciliary complex subunit 1* — 4p16.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (20 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.446× (z -14.8, q 0e+00, down in 27 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAMTS12]] (+0.65, fdr 1e-05), [[INSYN2B]] (+0.63, fdr 1e-05), [[AK5]] (+0.61, fdr 1e-05); moves opposite to [[SPATA6L]] (-0.49, fdr 3e-05), [[MUC1]] (-0.49, fdr 3e-05), [[RORC]] (-0.46, fdr 5e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[KIAA1549L]] → it (grade B ⚠); 14 go from it, the strongest it → [[RGMB]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 20 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1034.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.446×** | -14.8 | 0e+00 | 27/34 (LOX-IMVI, RKO, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.536×** | -11.4 | 1e-27 | 24/35 (hTERT-HPNE, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.582×** | -7.0 | 5e-10 | 25/35 (PANC-1, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.604×** | -6.5 | 1e-08 | 23/34 (PANC-1, NCI-H460, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.635×** | -5.3 | 1e-05 | 19/35 (hTERT-HPNE, RKO, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.647×** | -5.1 | 3e-05 | 19/34 (Panc 03.27, A-172, …) | top dose only | cell-cycle shift (explains ~25% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.651×** | -5.0 | 5e-05 | 19/35 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.663×** | -4.9 | 6e-05 | 16/30 (A549, hTERT-HPNE, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.689×** | -4.8 | 1e-04 | 20/35 (C-33 A, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.703×** | -4.5 | 3e-04 | 16/35 (PANC-1, H4, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.712×** | -4.4 | 6e-04 | 17/35 (SNU-423, RKO, …) | two highest doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.526×** | -4.3 | 7e-04 | 17/35 (C-33 A, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.694×** | -4.3 | 9e-04 | 19/32 (hTERT-HPNE, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.725×** | -4.1 | 0.001 | 15/35 (RPMI-7951, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **0.658×** | -4.1 | 0.001 | 14/34 (NCI-H460, A-172, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.561×** | -3.9 | 0.003 | 16/33 (RKO, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.615×** | -3.3 | 0.027 | 15/34 (RPMI-7951, SW 1271, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.712×** | -3.1 | 0.041 | 9/35 (A549, HS-578T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.632×** | -3.1 | 0.043 | 16/34 (C32, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | **0.780×** | -2.9 | 0.079 | 10/35 (A-427, SW 1271, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1034. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 122 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -16.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -12.5) |
| [[PANC-1 (line)]] | alt | 24.8 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -15.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -13.0) |
| [[A-172 (line)]] | wt | 50.0 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -11.1) |
| [[AN3 CA (line)]] | alt | 51.7 | 0 | 4 (3 ⚠) | — | [[Decitabine (drug)]] 0.05 µM 0.0926× (z -10.7) |
| [[C-33 A (line)]] | alt | 40.0 | 0 | 4 (2 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0392× (z -21.1) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Sonidegib (drug)]] 5 µM 0.0745× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 11.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0721× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[J82 (line)]] | alt | 23.4 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -11.4) |
| [[RKO (line)]] | wt | 50.4 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -16.3) |
| [[RPMI-7951 (line)]] | alt | 86.0 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -13.8) |
| [[SNU-1 (line)]] | wt | 33.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -11.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.189× (z -8.6) |
| [[A-427 (line)]] | wt | 40.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 74.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -12.2) |
| [[LOX-IMVI (line)]] | wt | 79.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -16.7) |
| [[NCI-H1792 (line)]] | alt | 30.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -11.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[Panc 03.27 (line)]] | alt | 22.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -15.3) |
| [[SNU-423 (line)]] | alt | 126 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -14.8) |
| [[A549 (line)]] | wt | 27.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0963× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[C32 (line)]] | wt | 19.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -9.9) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HOP62 (line)]] | alt | 72.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -13.9) |
| [[NCI-H23 (line)]] | alt | 37.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[SK-MEL-2 (line)]] | alt | 26.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -10.9) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW 1271 (line)]] | alt | 45.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.100× (z -9.9) |
| [[A498 (line)]] | wt | 65.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 68.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.26 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.06 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1034), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTS12]] | +0.65 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[INSYN2B]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[AK5]] | +0.61 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[AFF3]] | +0.61 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[MEG8]] | +0.60 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[SYT9]] | +0.58 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[STK32B]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[EVC2]] | +0.58 | +0.49 / +0.60 | both halves | 1e-05 | same gene group; pathway: Activation of SMO; STRING 999; ⚠ same locus (1.7 kb: neighbours can correlate without regulation) |
| [[MPDZ]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[ARHGAP22]] | +0.56 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[EML1]] | +0.56 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[BNC1]] | +0.56 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[RFTN1]] | +0.55 | +0.47 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA6L]] | -0.49 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[MUC1]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[RORC]] | -0.46 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[CASP10]] | -0.45 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[CDC42SE2]] | -0.45 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[UGP2]] | -0.44 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[FAAH2]] | -0.44 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[BCL2L15]] | -0.44 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[TC2N]] | -0.44 | -0.40 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 21, C 7. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIAA1549L]] | B | KIAA1549L activity raises EVC's level | lines that do not express KIAA1549L (20) vs lines expressing it (30) | 2.85× lower at baseline in the lines without KIAA1549L | 0.014 | ⚠ within organs, on part of the lines; also absent: NLRP3, PLPP4, PHACTR1 |
| [[ADAMTS6]] | B | ADAMTS6 activity raises EVC's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 3.50× lower at baseline in the lines without ADAMTS6 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2 |
| [[FAAH2]] | B | FAAH2 activity lowers EVC's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 3.87× higher at baseline in the lines without FAAH2 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[RORC]] | B | RORC activity lowers EVC's level | lines that do not express RORC (30) vs lines expressing it (20) | 2.92× higher at baseline in the lines without RORC | 0.027 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[COL5A1]] | B | COL5A1 activity raises EVC's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 3.63× lower at baseline in the lines without COL5A1 | 0.028 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R |
| [[KIRREL3]] | B | KIRREL3 activity raises EVC's level | lines that do not express KIRREL3 (36) vs lines expressing it (14) | 3.63× lower at baseline in the lines without KIRREL3 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN |
| [[CCNYL2]] | B | CCNYL2 activity raises EVC's level | lines that do not express CCNYL2 (29) vs lines expressing it (21) | 3.81× lower at baseline in the lines without CCNYL2 | 0.032 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1 |
| [[EVC2]] | B | EVC2 activity raises EVC's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 3.60× lower at baseline in the lines without EVC2 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7 |
| [[ARHGAP22]] | B | ARHGAP22 activity raises EVC's level | lines that do not express ARHGAP22 (21) vs lines expressing it (29) | 3.60× lower at baseline in the lines without ARHGAP22 | 0.034 | ⚠ within organs, on part of the lines; also absent: FAT4, TSHZ3, COL4A2 |
| [[APCDD1L-DT]] | B | APCDD1L-DT activity raises EVC's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 3.12× lower at baseline in the lines without APCDD1L-DT | 0.036 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |
| [[HHIP]] | B | HHIP activity raises EVC's level | lines that do not express HHIP (33) vs lines expressing it (17) | 2.88× lower at baseline in the lines without HHIP | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent |
| [[APCDD1L]] | B | APCDD1L activity raises EVC's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 3.70× lower at baseline in the lines without APCDD1L | 0.044 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1 |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 10, C 4. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGMB]] | B | EVC activity raises RGMB's level | lines that do not express EVC (13) vs lines expressing it (37) | 1.50× lower at baseline in the lines without EVC | 0.008 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: RNF150, PYGO1, EHD3 |
| [[ASAP1]] | B | EVC activity raises ASAP1's level | lines that do not express EVC (13) vs lines expressing it (37) | 1.53× lower at baseline in the lines without EVC | 0.044 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: RNF150, PYGO1, EHD3 |
| [[FRMD4A]] | B | EVC activity raises FRMD4A's level | lines that do not express EVC (13) vs lines expressing it (37) | 4.01× lower at baseline in the lines without EVC | 0.047 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: RNF150, PYGO1, EHD3 |
| [[BCL2L15]] | B | EVC activity lowers BCL2L15's level | lines that do not express EVC (13) vs lines expressing it (37) | 4.08× higher at baseline in the lines without EVC | 0.060 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: RNF150, PYGO1, EHD3 |
| [[C2CD2]] | B | EVC activity raises C2CD2's level | lines that do not express EVC (13) vs lines expressing it (37) | 1.16× lower at baseline in the lines without EVC | 0.069 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: RNF150, PYGO1, EHD3 |
| [[ARHGAP22]] | B | EVC activity raises ARHGAP22's level | lines that do not express EVC (13) vs lines expressing it (37) | 4.25× lower at baseline in the lines without EVC | 0.072 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: RNF150, PYGO1, EHD3 |
| [[ADAMTS6]] | B | EVC activity raises ADAMTS6's level | lines that do not express EVC (13) vs lines expressing it (37) | 3.79× lower at baseline in the lines without EVC | 0.083 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: RNF150, PYGO1, EHD3 |
| [[KIF7]] | B | EVC activity raises KIF7's level | lines that do not express EVC (13) vs lines expressing it (37) | 1.38× lower at baseline in the lines without EVC | 0.084 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: RNF150, PYGO1, EHD3 |
| [[UGP2]] | B | EVC activity lowers UGP2's level | lines that do not express EVC (13) vs lines expressing it (37) | 1.12× higher at baseline in the lines without EVC | 0.089 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: RNF150, PYGO1, EHD3 |
| [[TC2N]] | B | EVC activity lowers TC2N's level | lines that do not express EVC (13) vs lines expressing it (37) | 5.09× higher at baseline in the lines without EVC | 0.092 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: RNF150, PYGO1, EHD3 |
| [[FRMD6]] | C | EVC activity raises FRMD6's level | lines that do not express EVC (13) vs lines expressing it (37) | 5.28× lower at baseline in the lines without EVC | 0.003 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: RNF150, PYGO1, EHD3; co-absent with the target |
| [[BNC2]] | C | EVC activity raises BNC2's level | lines that do not express EVC (13) vs lines expressing it (37) | 7.38× lower at baseline in the lines without EVC | 0.006 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: RNF150, PYGO1, EHD3; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.599). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.8, 16.5); signed map (21.1, 46.9). **Vector** length 78.4, 18.5% of its response variance represented; |z| ≥ 3 in 864 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.2 | -3.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | +4.7 | -4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | +3.7 | -4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | -1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +1.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.9 | +1.1 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +0.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | +1.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.5 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -0.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | EvC ciliary complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.2 — chr4:5,711,201-5,814,305 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DWF-1, EVC1 |
| Gene groups (HGNC) | EvC complex subunits |
| Reactome | 3 pathways, smallest: Activation of SMO; Hedgehog 'on' state; Signaling by Hedgehog |
| Matched by | ensembl_id |

**Function**, from UniProt [P57679](https://www.uniprot.org/uniprotkb/P57679) (EvC complex member EVC):

> Component of the EvC complex that positively regulates ciliary Hedgehog (Hh) signaling. Involved in endochondral growth and skeletal development.

**Summary**, from NCBI Gene [2121](https://www.ncbi.nlm.nih.gov/gene/2121):

> This gene encodes a protein containing a leucine zipper and a transmembrane domain. This gene has been implicated in both Ellis-van Creveld syndrome (EvC) and Weyers acrodental dysostosis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3497](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3497) · Entrez [2121](https://www.ncbi.nlm.nih.gov/gene/2121) · UniProt [P57679](https://www.uniprot.org/uniprotkb/P57679) · Ensembl [ENSG00000072840](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072840)

## Data

Gene col 1034: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1034); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1034, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1034]; `tensor/DDL_lfc|DDL_z.npy` [1034]; `embed/gene_vectors.npy` [1034]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1034 or target_col == 1034). Every well: [[EVC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EVC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
