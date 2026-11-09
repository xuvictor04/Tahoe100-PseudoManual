---
symbol: "ENTPD1-AS1"
type: "gene"
col: 13548
ensembl_id: "ENSG00000226688"
name: "ENTPD1 antisense RNA 1"
location: "10q24.1"
module: 4
arm: "+"
pooled_cpm: 55.46
n_lines_expressing: 47
n_dd_up: 4
n_dd_down: 20
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 6
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# ENTPD1-AS1

*ENTPD1 antisense RNA 1* — 10q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.36× (z +4.2, q 0.008, up in 25 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (HT-29 3.44×).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.393× (z -12.9, q 2e-35, down in 42 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPH6]] (+0.63, fdr 1e-05), [[STX18-AS1]] (+0.61, fdr 1e-05), [[NAA15]] (+0.60, fdr 3e-05); moves opposite to [[WBP1]] (-0.55, fdr 9e-05), [[AAMDC]] (-0.51, fdr 1e-04), [[CDKL5]] (-0.48, fdr 2e-04).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 6 go from it, the strongest it → [[GBX2-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13548.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (HT-29 3.44×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +4.2 | 0.008 | 25/45 (NCI-H23, LS 180, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +4.2 | 0.008 | 25/45 (HT-29, RKO, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.32×** | +3.9 | 0.022 | 24/45 (PANC-1, RKO, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **1.31×** | +3.6 | 0.043 | 21/44 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.26× | +3.2 | 0.17 | 17/44 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.31× | +3.1 | 0.21 | 16/45 (A-172, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13548.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.393×** | -12.9 | 2e-35 | 42/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.448×** | -11.1 | 3e-26 | 40/45 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.435×** | -11.1 | 3e-26 | 41/45 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.261×** | -9.7 | 3e-20 | 44/46 (PANC-1, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.627×** | -9.2 | 6e-18 | 31/45 (PANC-1, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.553×** | -8.2 | 2e-14 | 37/45 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.342×** | -7.8 | 6e-13 | 38/45 (SW480, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.591×** | -7.3 | 2e-11 | 33/45 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.620×** | -6.6 | 2e-09 | 32/45 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.657×** | -5.8 | 4e-07 | 27/45 (PANC-1, A549, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.684×** | -5.1 | 2e-05 | 29/44 (COLO 205, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.685×** | -5.0 | 3e-05 | 32/45 (PANC-1, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.722×** | -4.5 | 3e-04 | 26/45 (SW48, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.726×** | -4.4 | 4e-04 | 25/45 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.727×** | -4.4 | 4e-04 | 26/45 (NCI-H2030, LoVo, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.744×** | -3.9 | 0.003 | 21/45 (SK-MEL-2, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.839× | -3.4 | 0.017 | 22/45 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.746×** | -2.9 | 0.097 | 15/45 (PANC-1, AN3 CA, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13548. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 82.8 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -23.7) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.326× (z -15.4) |
| [[A-172 (line)]] | wt | 64.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -10.7) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.289× (z -8.9) |
| [[HOP62 (line)]] | alt | 68.3 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.200× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 69.4 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.222× (z -15.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.282× (z -13.3) |
| [[A549 (line)]] | wt | 47.4 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -15.9) ⚠ cell-cycle shift, explains ~73% of this change |
| [[SHP-77 (line)]] | alt | 81.5 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.290× (z -10.8) |
| [[COLO 205 (line)]] | alt | 73.9 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.196× (z -12.5) |
| [[J82 (line)]] | alt | 34.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -11.6) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.285× (z -9.6) |
| [[LoVo (line)]] | wt | 57.8 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.366× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 51.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -19.9) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.347× (z -8.6) |
| [[RKO (line)]] | wt | 75.7 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.311× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -10.9) |
| [[SW480 (line)]] | alt | 71.7 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.310× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.324× (z -12.0) |
| [[A498 (line)]] | wt | 52.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -17.0) ⚠ cell-cycle shift, explains ~73% of this change |
| [[HepG2_C3A (line)]] | wt | 74.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.177× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.283× (z -9.0) |
| [[HT-29 (line)]] | alt | 34.6 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.44× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -9.6) ⚠ cell-cycle shift, explains ~73% of this change |
| [[NCI-H2030 (line)]] | alt | 60.0 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.290× (z -10.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H23 (line)]] | alt | 96.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 49.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -11.5) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.289× (z -9.4) |
| [[A-427 (line)]] | wt | 72.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -21.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 54.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.333× (z -8.7) |
| [[C-33 A (line)]] | alt | 169 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[CFPAC-1 (line)]] | alt | 58.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -10.2) ⚠ cell-cycle shift, explains ~73% of this change |
| [[H4 (line)]] | wt | 66.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -10.3) ⚠ cell-cycle shift, explains ~73% of this change |
| [[LOX-IMVI (line)]] | wt | 56.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.255× (z -12.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H1792 (line)]] | alt | 47.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.272× (z -9.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Panc 03.27 (line)]] | alt | 32.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.191× (z -10.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 77.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.209× (z -10.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SK-MEL-2 (line)]] | alt | 85.1 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -11.9) |
| [[SNU-1 (line)]] | wt | 87.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.325× (z -8.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 37.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -13.2) ⚠ cell-cycle shift, explains ~73% of this change |
| [[SW48 (line)]] | wt | 81.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.315× (z -8.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[AN3 CA (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.8 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.85 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 73.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13548), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPH6]] | +0.63 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[STX18-AS1]] | +0.61 | +0.68 / +0.53 | both halves | 1e-05 | same gene group |
| [[NAA15]] | +0.60 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[COX10]] | +0.57 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[TSEN2]] | +0.56 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[TCERG1]] | +0.56 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[METAP1D]] | +0.56 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[URB2]] | +0.55 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[LTV1]] | +0.55 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[PNO1]] | +0.55 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[LETM1]] | +0.55 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[TMEM33]] | +0.54 | +0.53 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WBP1]] | -0.55 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[AAMDC]] | -0.51 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[CDKL5]] | -0.48 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[HADHB]] | -0.48 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[ARID4A]] | -0.47 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[WDTC1]] | -0.47 | -0.36 / -0.52 | both halves | 9e-05 |  |
| [[KDM5B]] | -0.47 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[ACADSB]] | -0.47 | -0.29 / -0.36 | both halves | 3e-04 |  |
| [[TCP11L2]] | -0.46 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[PAIP2B]] | -0.46 | -0.19 / -0.37 | ⚠ not reproduced | 8e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBX2-AS1]] | C | ENTPD1-AS1 activity raises GBX2-AS1's level | lines that do not express ENTPD1-AS1 (3) vs lines expressing it (47) | 3.36× lower at baseline in the lines without ENTPD1-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRRIQ3, WDR35, ENSG00000287400; maybe low, not absent; its own permutation p |
| [[STX18-AS1]] | C | ENTPD1-AS1 activity raises STX18-AS1's level | lines that do not express ENTPD1-AS1 (3) vs lines expressing it (47) | 2.62× lower at baseline in the lines without ENTPD1-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRRIQ3, WDR35, ENSG00000287400; maybe low, not absent; its own permutation p |
| [[METAP1D]] | C | ENTPD1-AS1 activity raises METAP1D's level | lines that do not express ENTPD1-AS1 (3) vs lines expressing it (47) | 2.17× lower at baseline in the lines without ENTPD1-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRRIQ3, WDR35, ENSG00000287400; maybe low, not absent; its own permutation p |
| [[ACADSB]] | C | ENTPD1-AS1 activity raises ACADSB's level | lines that do not express ENTPD1-AS1 (3) vs lines expressing it (47) | 1.91× lower at baseline in the lines without ENTPD1-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRRIQ3, WDR35, ENSG00000287400; maybe low, not absent; its own permutation p |
| [[PUM3]] | C | ENTPD1-AS1 activity raises PUM3's level | lines that do not express ENTPD1-AS1 (3) vs lines expressing it (47) | 1.89× lower at baseline in the lines without ENTPD1-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRRIQ3, WDR35, ENSG00000287400; maybe low, not absent; its own permutation p |
| [[CDIN1]] | C | ENTPD1-AS1 activity raises CDIN1's level | lines that do not express ENTPD1-AS1 (3) vs lines expressing it (47) | 1.72× lower at baseline in the lines without ENTPD1-AS1 | 0.090 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRRIQ3, WDR35, ENSG00000287400; maybe low, not absent |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.557). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-11.9, -36.0); signed map (-5.8, -49.2). **Vector** length 77.4, 19.4% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.5 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | +5.1 | +3.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +1.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +0.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.4 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +1.5 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -3.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.9 | -11.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.2 | -3.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.0 | -4.4 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.6 | -0.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -0.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.5 | -0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | ENTPD1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10q24.1 — chr10:95,732,976-96,090,250 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:45203](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:45203) · Entrez [728558](https://www.ncbi.nlm.nih.gov/gene/728558) · Ensembl [ENSG00000226688](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226688)

## Data

Gene col 13548: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13548); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13548, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13548]; `tensor/DDL_lfc|DDL_z.npy` [13548]; `embed/gene_vectors.npy` [13548]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13548 or target_col == 13548). Every well: [[ENTPD1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENTPD1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
