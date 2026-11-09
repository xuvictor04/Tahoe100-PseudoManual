---
symbol: "EFCAB11"
type: "gene"
col: 6369
ensembl_id: "ENSG00000140025"
name: "EF-hand calcium binding domain 11"
location: "14q32.11"
module: 67
arm: "+"
pooled_cpm: 46.36
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 43
n_dd_up_clean: 3
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# EFCAB11

*EF-hand calcium binding domain 11* — 14q32.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.60× (z +8.7, q 1e-15, up in 38 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.24× (z +4.0, q 0.006, up in 20 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.261× (z -34.8, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTBP]] (+0.73, fdr 7e-06), [[CENPJ]] (+0.70, fdr 7e-06), [[FANCM]] (+0.70, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6369.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.60×** | +8.7 | 1e-15 | 38/48 (A498, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.48×** | +7.3 | 7e-11 | 33/48 (A498, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.46×** | +7.1 | 3e-10 | 30/48 (A498, A549, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.19× | +4.5 | 1e-03 | 22/48 (NCI-H1792, SW1417, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.006 | 20/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.20×** | +3.5 | 0.047 | 11/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.4 | 0.047 | 14/48 (C32, NCI-H1573, …) | top dose only |  |
| [[Irinotecan (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.094 | 5/48 (SW 900, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 1.13× | +3.1 | 0.11 | 16/48 (RKO, KATO III, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6369.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.261×** | -34.8 | 0e+00 | 47/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.251×** | -25.6 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.239×** | -25.5 | 0e+00 | 47/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.278×** | -23.7 | 0e+00 | 48/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.279×** | -23.7 | 0e+00 | 45/48 (H4, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.378×** | -18.0 | 0e+00 | 47/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.172×** | -17.1 | 0e+00 | 48/48 (SW480, H4, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.408×** | -16.6 | 0e+00 | 37/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.425×** | -15.9 | 0e+00 | 45/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.214×** | -14.9 | 0e+00 | 42/48 (A-427, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.598×** | -13.4 | 4e-39 | 46/48 (COLO 205, SW480, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.520×** | -12.1 | 5e-32 | 41/48 (PANC-1, SW1417, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.534×** | -11.6 | 2e-29 | 38/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.555×** | -10.5 | 4e-24 | 37/47 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.583×** | -10.0 | 7e-22 | 39/48 (COLO 205, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.614×** | -9.0 | 6e-18 | 33/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.637×** | -7.9 | 1e-13 | 34/48 (HEC-1-A, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.756×** | -7.2 | 1e-11 | 36/48 (CFPAC-1, A-427, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6369. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 72.6 | 0 | 18 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.128× (z -28.8) |
| [[NCI-H460 (line)]] | wt | 42.6 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -25.0) |
| [[PANC-1 (line)]] | alt | 52.9 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -33.6) |
| [[COLO 205 (line)]] | alt | 58.2 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0778× (z -26.7) |
| [[HOP62 (line)]] | alt | 49.4 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0955× (z -30.1) |
| [[NCI-H1573 (line)]] | alt | 44.8 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0919× (z -30.0) |
| [[MIA PaCa-2 (line)]] | alt | 43.1 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0526× (z -21.5) |
| [[CFPAC-1 (line)]] | alt | 53.7 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -21.5) |
| [[H4 (line)]] | wt | 71.3 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0192× (z -25.5) |
| [[HEC-1-A (line)]] | alt | 58.7 | 0 | 9 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -23.7) |
| [[SW 900 (line)]] | alt | 46.2 | 0 | 9 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0865× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.137× (z -16.2) |
| [[A-427 (line)]] | wt | 68.4 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -20.4) |
| [[A-172 (line)]] | wt | 52.9 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -21.6) |
| [[A498 (line)]] | wt | 42.2 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -27.4) |
| [[HCT15 (line)]] | alt | 67.4 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -14.5) |
| [[LOX-IMVI (line)]] | wt | 51.9 | 0 | 7 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.201× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.232× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 66.2 | 0 | 7 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0934× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.185× (z -13.9) |
| [[SNU-1 (line)]] | wt | 54.7 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -10.7) |
| [[J82 (line)]] | alt | 42.9 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -21.8) |
| [[KATO III (line)]] | alt | 37.3 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.127× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.275× (z -14.6) |
| [[LS 180 (line)]] | wt | 34.7 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -15.8) |
| [[NCI-H23 (line)]] | alt | 68.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -21.7) |
| [[SHP-77 (line)]] | alt | 43.2 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.214× (z -11.1) |
| [[AN3 CA (line)]] | alt | 70.7 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0643× (z -13.3) |
| [[hTERT-HPNE (line)]] | wt | 50.6 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.135× (z -14.7) |
| [[SK-MEL-2 (line)]] | alt | 52.9 | 0 | 5 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -16.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.274× (z -14.8) |
| [[SNU-423 (line)]] | alt | 39.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -14.7) |
| [[A549 (line)]] | wt | 32.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -19.8) |
| [[BT-474 (line)]] | alt | 37.8 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.110× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.268× (z -12.1) |
| [[HS-578T (line)]] | alt | 37.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -22.0) |
| [[LoVo (line)]] | wt | 34.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -13.7) |
| [[NCI-H2030 (line)]] | alt | 52.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -10.8) |
| [[SW1417 (line)]] | alt | 38.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -12.8) |
| [[AsPC-1 (line)]] | alt | 13.2 | 0 | 3 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0994× (z -11.6) ⚠ transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.251× (z -9.7) |
| [[Hs 766T (line)]] | wt | 27.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -13.7) |
| [[HT-29 (line)]] | alt | 26.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -11.7) |
| [[NCI-H1792 (line)]] | alt | 31.6 | 1 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +9.7) ⚠ cell-cycle shift, explains ~47% of this change | [[Harringtonine (drug)]] 5 µM 0.180× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 40.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -12.0) |
| [[C32 (line)]] | wt | 40.3 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.254× (z -9.7) |
| [[CHP-212 (line)]] | wt | 33.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0648× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.0686× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 24.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 36.3 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.160× (z -11.0) |
| [[SW48 (line)]] | wt | 36.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.141× (z -8.9) |
| [[C-33 A (line)]] | alt | 48.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -8.5) |
| [[RKO (line)]] | wt | 38.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -10.1) |
| [[SW 1271 (line)]] | alt | 88.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.120× (z -8.6) |
| [[NCI-H2122 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6369), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTBP]] | +0.73 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[CENPJ]] | +0.70 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[FANCM]] | +0.70 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[SPC25]] | +0.69 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[TRAIP]] | +0.69 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[CEP152]] | +0.68 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[CDCA5]] | +0.68 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[POC1A]] | +0.68 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[DSN1]] | +0.67 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[KIF22]] | +0.67 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[FANCI]] | +0.66 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[SHCBP1]] | +0.66 | +0.69 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers EFCAB11's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[AURKB]] | C | AURKB activity raises EFCAB11's level | lines that do not express AURKB (4) vs lines expressing it (46) | 1.74× lower at baseline in the lines without AURKB | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[C21orf58]] | C | C21orf58 activity raises EFCAB11's level | lines that do not express C21orf58 (3) vs lines expressing it (47) | 2.07× lower at baseline in the lines without C21orf58 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.692). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-33.8, -49.4); signed map (-42.1, -41.7). **Vector** length 104, 35.0% of its response variance represented; |z| ≥ 3 in 1,548 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.60 to 12); *G2/M checkpoint* (hallmark, mean cos +0.61 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.61 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.9 | +8.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.7 | +7.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | -2.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | -2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +2.9 | +7.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.6 | -1.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | +2.0 | +0.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.0 | +0.4 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | +1.9 | -0.8 |
|  | [[Methotrexate (drug)]] 5 µM |  | +1.6 | +1.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -16.2 | -13.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -13.7 | -10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.7 | -3.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.4 | -5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.7 | -5.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -4.7 | -5.1 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -3.8 | -2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.6 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | EF-hand calcium binding domain 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.11 — chr14:89,794,669-89,954,777 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C14orf143 |
| Gene groups (HGNC) | EF-hand domain containing |
| Matched by | ensembl_id |

UniProt [Q9BUY7](https://www.uniprot.org/uniprotkb/Q9BUY7) carries no function annotation.

**Summary**, from NCBI Gene [90141](https://www.ncbi.nlm.nih.gov/gene/90141):

> Predicted to enable calcium ion binding activity and enzyme regulator activity. Predicted to be involved in microtubule cytoskeleton organization. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20357](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20357) · Entrez [90141](https://www.ncbi.nlm.nih.gov/gene/90141) · UniProt [Q9BUY7](https://www.uniprot.org/uniprotkb/Q9BUY7) · Ensembl [ENSG00000140025](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140025)

## Data

Gene col 6369: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6369); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6369, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6369]; `tensor/DDL_lfc|DDL_z.npy` [6369]; `embed/gene_vectors.npy` [6369]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6369 or target_col == 6369). Every well: [[EFCAB11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFCAB11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
