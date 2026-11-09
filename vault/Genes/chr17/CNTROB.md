---
symbol: "CNTROB"
type: "gene"
col: 9897
ensembl_id: "ENSG00000170037"
name: "centrobin, centriole duplication and spindle assembly protein"
location: "17p13.1"
module: 67
arm: "+"
pooled_cpm: 34.36
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# CNTROB

*centrobin, centriole duplication and spindle assembly protein* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.79× (z +15.4, q 0e+00, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.742× (z -5.3, q 5e-05, down in 26 of 46 measured lines) ⚠ toxic; cell-cycle shift, explains ~24% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.756× (z -5.0, q 1e-04, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A549 0.253×, C-33 A 0.224×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.289×; ⚠ toxic; cell-cycle shift, explains ~24% of this change); [[AZD2858 (drug)]] 0.5 µM in 1 line (Hs 766T 0.113×; ⚠ toxic); [[4EGI-1 (drug)]] 0.05 µM in 1 line (NCI-H661 0.0863×); [[olaparib (drug)]] 5 µM in 1 line (Hs 766T 0.0960×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP33]] (+0.69, fdr 7e-06), [[SUN2]] (+0.62, fdr 1e-05), [[RACGAP1]] (+0.62, fdr 8e-06); moves opposite to [[PSMA1]] (-0.47, fdr 6e-05), [[CDC123]] (-0.45, fdr 2e-04), [[SPR]] (-0.44, fdr 4e-04).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LIX1L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9897.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.79×** | +15.4 | 0e+00 | 39/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.68×** | +9.7 | 7e-20 | 35/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +8.7 | 5e-16 | 35/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +6.5 | 1e-08 | 27/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +6.4 | 1e-08 | 27/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.27×** | +4.0 | 0.005 | 19/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **1.21×** | +3.4 | 0.060 | 13/47 (A-172, LOX-IMVI, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.3 | 0.062 | 8/48 (HepG2/C3A, NCI-H460, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.18× | +3.0 | 0.15 | 11/48 (A498, HepG2/C3A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9897.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A549 0.253×, C-33 A 0.224×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.289×; ⚠ toxic; cell-cycle shift, explains ~24% of this change); [[AZD2858 (drug)]] 0.5 µM in 1 line (Hs 766T 0.113×; ⚠ toxic); [[4EGI-1 (drug)]] 0.05 µM in 1 line (NCI-H661 0.0863×); [[olaparib (drug)]] 5 µM in 1 line (Hs 766T 0.0960×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.742×** | -5.3 | 5e-05 | 26/46 (MIA PaCa-2, NCI-H2030, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.752×** | -5.0 | 1e-04 | 28/48 (SK-MEL-2, HOP62, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.756×** | -5.0 | 1e-04 | 27/48 (NCI-H2030, C-33 A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.765×** | -4.8 | 2e-04 | 22/48 (SW 1271, A549, …) | top dose only | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.791×** | -4.4 | 0.001 | 18/48 (HCT15, NCI-H460, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.847× | -4.4 | 0.001 | 19/48 (H4, A498, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.647×** | -4.2 | 0.002 | 21/48 (MIA PaCa-2, AN3 CA, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.808×** | -4.0 | 0.005 | 15/48 (SW 1088, SW1417, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.810×** | -3.9 | 0.006 | 21/48 (LOX-IMVI, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -3.3 | 0.052 | 14/48 (SW480, RPMI-7951, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.838× | -3.3 | 0.052 | 16/48 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.843× | -3.2 | 0.070 | 19/48 (BT-474, HOP62, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **0.723×** | -3.2 | 0.070 | 12/42 (HOP62, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Larotrectinib (drug)]] 5 µM |  | 0.889× | -3.1 | 0.078 | 6/48 (LS 180, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9897. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.1 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +22.3) | — |
| [[PANC-1 (line)]] | alt | 37.1 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +15.6) | — |
| [[A549 (line)]] | wt | 43.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[HOP62 (line)]] | alt | 43.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +11.6) | — |
| [[Hs 766T (line)]] | wt | 24.1 | 0 | 2 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.113× (z -10.7) ⚠ toxic · without an alert: [[olaparib (drug)]] 5 µM 0.0960× (z -8.5) |
| [[LoVo (line)]] | wt | 18.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +11.4) | — |
| [[NCI-H1573 (line)]] | alt | 14.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +15.2) | — |
| [[NCI-H23 (line)]] | alt | 61.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.7) | — |
| [[A498 (line)]] | wt | 42.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +13.4) | — |
| [[C-33 A (line)]] | alt | 56.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[HS-578T (line)]] | alt | 49.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.3) | — |
| [[hTERT-HPNE (line)]] | wt | 35.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +8.7) | — |
| [[LOX-IMVI (line)]] | wt | 36.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 59.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.289× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~24% of this change |
| [[NCI-H1792 (line)]] | alt | 19.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +13.8) | — |
| [[NCI-H2030 (line)]] | alt | 49.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +10.7) | — |
| [[NCI-H661 (line)]] | alt | 46.2 | 0 | 1 | — | [[4EGI-1 (drug)]] 0.05 µM 0.0863× (z -8.6) |
| [[RKO (line)]] | wt | 30.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +12.5) | — |
| [[RPMI-7951 (line)]] | alt | 54.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +13.1) | — |
| [[SHP-77 (line)]] | alt | 55.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.315× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 19.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +12.2) | — |
| [[SNU-1 (line)]] | wt | 42.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 53.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0613× (z -9.1) ⚠ cell-cycle shift, explains ~20% of this change |
| [[A-172 (line)]] | wt | 57.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 43.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9897), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP33]] | +0.69 | +0.72 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[SUN2]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[RACGAP1]] | +0.62 | +0.63 / +0.58 | both halves | 8e-06 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[IQGAP3]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[SPAG5]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[UBE2C]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[IFT122]] | +0.56 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[ESPL1]] | +0.56 | +0.56 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[ARHGAP11B]] | +0.54 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[TROAP]] | +0.54 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[AURKB]] | +0.54 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[KIF2C]] | +0.54 | +0.55 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMA1]] | -0.47 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[CDC123]] | -0.45 | -0.52 / -0.29 | both halves | 2e-04 |  |
| [[SPR]] | -0.44 | -0.49 / -0.26 | both halves | 4e-04 |  |
| [[SMIM10L1]] | -0.44 | -0.53 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LIX1L]] | B | LIX1L activity raises CNTROB's level | lines that do not express LIX1L (10) vs lines expressing it (38) | 1.59× lower at baseline in the lines without LIX1L | 0.035 | ⚠ within organs, on part of the lines; also absent: CCDC88A, GIHCG, BOLA3-DT |
| [[PIMREG]] | B | PIMREG activity raises CNTROB's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.76× lower at baseline in the lines without PIMREG | 0.086 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises CNTROB's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.06× lower at baseline in the lines without AURKB | 0.025 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.481). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-35.3, -54.9); signed map (-48.1, -41.5). **Vector** length 101, 23.0% of its response variance represented; |z| ≥ 3 in 884 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.5 | +15.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | +5.5 | -0.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.3 | +2.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.1 | +2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.9 | +9.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.8 | +2.5 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.7 | -0.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.7 | +0.8 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +1.7 | +1.6 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | -4.8 | -5.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.7 | -4.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | -4.3 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -3.6 | -3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | centrobin, centriole duplication and spindle assembly protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,932,101-7,949,920 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LIP8, PP1221 |
| Hallmark sets | MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N137](https://www.uniprot.org/uniprotkb/Q8N137) (Centrobin):

> Required for centriole duplication. Inhibition of centriole duplication leading to defects in cytokinesis.

**Summary**, from NCBI Gene [116840](https://www.ncbi.nlm.nih.gov/gene/116840):

> This gene encodes a centrosomal protein that interacts with BRCA2, and is required for centriole duplication and cytokinesis. Alternatively spliced transcript variants encoding different isoforms have been described for this gene. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:29616](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29616) · Entrez [116840](https://www.ncbi.nlm.nih.gov/gene/116840) · UniProt [Q8N137](https://www.uniprot.org/uniprotkb/Q8N137) · Ensembl [ENSG00000170037](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170037)

## Data

Gene col 9897: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9897); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9897, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9897]; `tensor/DDL_lfc|DDL_z.npy` [9897]; `embed/gene_vectors.npy` [9897]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9897 or target_col == 9897). Every well: [[CNTROB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNTROB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
