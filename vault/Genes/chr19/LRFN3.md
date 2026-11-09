---
symbol: "LRFN3"
type: "gene"
col: 4724
ensembl_id: "ENSG00000126243"
name: "leucine rich repeat and fibronectin type III domain containing 3"
location: "19q13.12"
module: 199
arm: "+"
pooled_cpm: 4.44
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 19
n_dd_up_clean: 8
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/199"]
generated_by: "tahoemap"
---

# LRFN3

*leucine rich repeat and fibronectin type III domain containing 3* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.34× (z +10.6, q 2e-23, up in 33 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.582× (z -9.5, q 9e-19, down in 25 of 39 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.476× (z -9.2, q 7e-18, down in 24 of 37 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP35]] (+0.73, fdr 7e-06), [[SEMA4F]] (+0.72, fdr 1e-05), [[GTF2E2]] (+0.72, fdr 1e-05); moves opposite to [[LINC01004]] (-0.74, fdr 2e-05), [[PPP1R12A-AS2]] (-0.71, fdr 2e-04), [[MMADHC-DT]] (-0.69, fdr 4e-04).
> It is in [[Module 199]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[THRB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4724.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.34×** | +10.6 | 2e-23 | 33/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.31×** | +10.4 | 7e-23 | 34/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.26×** | +10.1 | 8e-22 | 35/45 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +6.5 | 1e-08 | 1/5 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.67×** | +6.4 | 2e-08 | 18/39 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +5.3 | 1e-05 | 15/46 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +5.1 | 3e-05 | 14/45 (HT-29, SW480, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +4.8 | 9e-05 | 1/11 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.89×** | +4.1 | 0.002 | 2/41 (PANC-1, MIA PaCa-2) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +3.8 | 0.007 | 7/44 (HT-29, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.34×** | +3.7 | 0.012 | 6/23 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +3.4 | 0.033 | 7/27 (HOP62, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4724.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.582×** | -9.5 | 9e-19 | 25/39 (A-172, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.476×** | -9.2 | 7e-18 | 24/37 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.486×** | -9.0 | 6e-17 | 27/45 (H4, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.488×** | -8.6 | 1e-15 | 24/44 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.619×** | -8.4 | 4e-15 | 22/37 (SHP-77, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.567×** | -7.1 | 2e-10 | 20/39 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.576×** | -6.9 | 5e-10 | 24/47 (SNU-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.583×** | -6.7 | 1e-09 | 18/46 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.622×** | -5.7 | 9e-07 | 17/40 (LOX-IMVI, H4, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.657×** | -5.2 | 9e-06 | 15/46 (SK-MEL-2, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.666×** | -5.0 | 2e-05 | 16/45 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.693×** | -4.4 | 6e-04 | 11/35 (LOX-IMVI, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.715×** | -4.2 | 0.001 | 12/45 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.724×** | -4.0 | 0.002 | 7/46 (HS-578T, COLO 205, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.726×** | -4.0 | 0.003 | 8/46 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.767×** | -3.2 | 0.049 | 7/43 (NCI-H1573, LOX-IMVI, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.766×** | -3.1 | 0.063 | 14/36 (Panc 03.27, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Sulfisoxazole (drug)]] 5 µM |  | 0.840× | -3.1 | 0.063 | 2/45 (NCI-H661, LOX-IMVI) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4724. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 6.24 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -10.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.135× (z -8.7) |
| [[KATO III (line)]] | alt | 4.79 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0904× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 4.51 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -10.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.163× (z -8.5) |
| [[PANC-1 (line)]] | alt | 4.00 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0792× (z -12.2) |
| [[A-427 (line)]] | wt | 9.42 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.149× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~68% of this change |
| [[HOP62 (line)]] | alt | 5.05 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -8.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LOX-IMVI (line)]] | wt | 6.27 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 6.41 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0777× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 2.16 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0536× (z -9.5) |
| [[SHP-77 (line)]] | alt | 5.23 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -8.6) |
| [[SW 900 (line)]] | alt | 4.06 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -8.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4724), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP35]] | +0.73 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[SEMA4F]] | +0.72 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[GTF2E2]] | +0.72 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[MYPOP]] | +0.72 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[MAST3]] | +0.71 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[ANKRD27]] | +0.69 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[PIK3R2]] | +0.69 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[ZNF71]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[POMGNT2]] | +0.69 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[WASF3]] | +0.68 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[INTS11]] | +0.68 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[GPRIN1]] | +0.67 | +0.49 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01004]] | -0.74 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[PPP1R12A-AS2]] | -0.71 | -0.65 / -0.30 | both halves | 2e-04 |  |
| [[MMADHC-DT]] | -0.69 | -0.64 / -0.26 | both halves | 4e-04 |  |
| [[THAP2]] | -0.68 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[EFCAB2]] | -0.67 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[PKN2-AS1]] | -0.67 | -0.60 / -0.29 | both halves | 2e-04 |  |
| [[BAZ2B]] | -0.67 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[TSGA10]] | -0.66 | -0.68 / -0.23 | both halves | 5e-04 |  |
| [[RFX3-DT]] | -0.66 | -0.59 / -0.27 | both halves | 3e-04 |  |
| [[KRBOX5]] | -0.66 | -0.62 / -0.30 | both halves | 2e-04 |  |
| [[LINC00869-1]] | -0.66 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[CCDC90B-AS1]] | -0.66 | -0.59 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[WARS2-AS1]] | -0.65 | -0.53 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THRB]] | B | THRB activity lowers LRFN3's level | lines that do not express THRB (21) vs lines expressing it (29) | 1.49× higher at baseline in the lines without THRB | 0.013 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[GNAZ]] | B | GNAZ activity raises LRFN3's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.55× lower at baseline in the lines without GNAZ | 0.032 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[SNTA1]] | B | SNTA1 activity raises LRFN3's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.35× lower at baseline in the lines without SNTA1 | 0.033 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[RIMS3]] | B | RIMS3 activity raises LRFN3's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 1.41× lower at baseline in the lines without RIMS3 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity lowers LRFN3's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.45× higher at baseline in the lines without ZNF341-AS1 | 0.066 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[ZHX2]] | B | ZHX2 activity lowers LRFN3's level | lines that do not express ZHX2 (7) vs lines expressing it (43) | 1.52× higher at baseline in the lines without ZHX2 | 0.077 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers LRFN3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers LRFN3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises LRFN3's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC00944]] | B | LINC00944 activity lowers LRFN3's level | lines that do not express LINC00944 (20) vs lines expressing it (30) | 1.33× higher at baseline in the lines without LINC00944 | 0.095 | ⚠ within organs, on part of the lines; also absent: RDUR, ENSG00000289600, LINC02405 |
| [[SMARCD3]] | C | SMARCD3 activity raises LRFN3's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 2.04× lower at baseline in the lines without SMARCD3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 199]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.781). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.9, -0.8); signed map (-39.5, -7.4). **Vector** length 61.4, 8.52% of its response variance represented; |z| ≥ 3 in 1,084 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.0 | +10.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.9 | +6.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.8 | +10.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.6 | +10.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.9 | +5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.4 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.4 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.8 | -9.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.4 | -8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.7 | -9.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -9.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -5.2 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.2 | -0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat and fibronectin type III domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:35,935,358-35,946,624 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2656, SALM4, FIGLER1 |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; Ig-like cell adhesion molecule family |
| Reactome | 3 pathways, smallest: Synaptic adhesion-like molecules; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTN0](https://www.uniprot.org/uniprotkb/Q9BTN0) (Leucine-rich repeat and fibronectin type-III domain-containing protein 3):

> Cell adhesion molecule that mediates homophilic cell-cell adhesion in a Ca(2+)-independent manner. Promotes neurite outgrowth in hippocampal neurons (By similarity).

**Summary**, from NCBI Gene [79414](https://www.ncbi.nlm.nih.gov/gene/79414):

> Predicted to be involved in regulation of presynapse assembly; regulation of synaptic membrane adhesion; and synaptic membrane adhesion. Predicted to be located in plasma membrane. Predicted to be active in cell surface and presynaptic active zone membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28370](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28370) · Entrez [79414](https://www.ncbi.nlm.nih.gov/gene/79414) · UniProt [Q9BTN0](https://www.uniprot.org/uniprotkb/Q9BTN0) · Ensembl [ENSG00000126243](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126243)

## Data

Gene col 4724: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4724); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4724, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4724]; `tensor/DDL_lfc|DDL_z.npy` [4724]; `embed/gene_vectors.npy` [4724]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4724 or target_col == 4724). Every well: [[LRFN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRFN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
