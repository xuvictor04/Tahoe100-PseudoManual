---
symbol: "PHF10"
type: "gene"
col: 5017
ensembl_id: "ENSG00000130024"
name: "PHD finger protein 10"
location: "6q27"
module: 54
arm: "-"
pooled_cpm: 61.93
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 30
n_dd_up_clean: 1
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# PHF10

*PHD finger protein 10* — 6q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.19× (z +16.9, q 0e+00, up in 36 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.20× (z +4.2, q 0.004, up in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (SW480 2.70×, KATO III 3.41×, NCI-H1573 4.85×, PANC-1 2.30×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 2.43×, KATO III 2.91×, NCI-H460 2.32×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 2.01×).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.330× (z -24.7, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BTBD1]] (+0.57, fdr 3e-05), [[SEPTIN11]] (+0.55, fdr 3e-05), [[ALG10B]] (+0.55, fdr 1e-04); moves opposite to [[RPL36AL]] (-0.57, fdr 1e-04, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[SEC61B]] (-0.52, fdr 5e-05), [[EMC6]] (-0.52, fdr 2e-04), [[TRAPPC2B]] (-0.51, fdr 3e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TMPRSS4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5017.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (SW480 2.70×, KATO III 3.41×, NCI-H1573 4.85×, PANC-1 2.30×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 2.43×, KATO III 2.91×, NCI-H460 2.32×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 2.01×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +16.9 | 0e+00 | 36/43 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.91×** | +14.5 | 3e-45 | 37/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +8.8 | 2e-16 | 29/45 (Panc 03.27, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.20×** | +4.2 | 0.004 | 20/48 (BT-474, SHP-77, …) | top dose only |  |
| [[Roxadustat (drug)]] 5 µM |  | 1.17× | +3.5 | 0.055 | 12/47 (HOP62, PANC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~13% of this change | 1.16× | +3.4 | 0.055 | 13/47 (hTERT-HPNE, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.3 | 0.089 | 11/48 (PANC-1, MIA PaCa-2, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5017.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.330×** | -24.7 | 0e+00 | 45/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.346×** | -23.6 | 0e+00 | 46/48 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.438×** | -18.4 | 0e+00 | 43/48 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.593×** | -11.6 | 5e-29 | 34/48 (LOX-IMVI, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.613×** | -10.9 | 1e-25 | 32/47 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.718×** | -10.4 | 3e-23 | 30/48 (NCI-H23, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.726×** | -10.1 | 6e-22 | 31/49 (MIA PaCa-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.672×** | -8.8 | 7e-17 | 34/48 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.674×** | -8.8 | 1e-16 | 36/47 (HOP62, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.684×** | -8.0 | 8e-14 | 33/48 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.525×** | -7.5 | 3e-12 | 32/48 (AN3 CA, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.743×** | -6.6 | 2e-09 | 30/48 (HOP62, HepG2/C3A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.750×** | -6.4 | 8e-09 | 28/47 (HOP62, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.762×** | -6.0 | 7e-08 | 25/48 (NCI-H23, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.755×** | -6.0 | 8e-08 | 24/47 (RKO, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.780×** | -5.5 | 1e-06 | 25/48 (NCI-H23, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.649×** | -5.0 | 2e-05 | 29/49 (SNU-1, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5017. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 93.0 | 3 (3 ⚠) | 9 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +9.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.180× (z -20.8) |
| [[NCI-H23 (line)]] | alt | 93.2 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -27.0) |
| [[MIA PaCa-2 (line)]] | alt | 109 | 1 (1 ⚠) | 7 | [[Dinaciclib (drug)]] 5 µM 2.27× (z +9.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.124× (z -24.6) |
| [[NCI-H460 (line)]] | wt | 48.7 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +10.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.269× (z -15.9) |
| [[RKO (line)]] | wt | 112 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -24.2) |
| [[SK-MEL-2 (line)]] | alt | 78.6 | 0 | 7 | — | [[Panobinostat (drug)]] 0.5 µM 0.129× (z -17.3) |
| [[SW480 (line)]] | alt | 55.5 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +14.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.209× (z -22.8) |
| [[HepG2_C3A (line)]] | wt | 214 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.158× (z -19.5) |
| [[J82 (line)]] | alt | 92.2 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.240× (z -16.8) |
| [[Panc 03.27 (line)]] | alt | 39.3 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +10.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.219× (z -12.3) |
| [[PANC-1 (line)]] | alt | 112 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +12.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.309× (z -17.7) |
| [[HS-578T (line)]] | alt | 65.6 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.270× (z -11.6) |
| [[LoVo (line)]] | wt | 47.2 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.33× (z +9.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.379× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 49.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0818× (z -23.2) |
| [[LS 180 (line)]] | wt | 52.1 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +11.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.295× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 57.5 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -16.4) |
| [[SW 900 (line)]] | alt | 72.2 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.202× (z -14.8) |
| [[A-172 (line)]] | wt | 62.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.278× (z -13.8) |
| [[A-427 (line)]] | wt | 63.3 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +10.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.273× (z -12.4) |
| [[A549 (line)]] | wt | 62.6 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.166× (z -15.1) |
| [[AN3 CA (line)]] | alt | 130 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -14.9) |
| [[KATO III (line)]] | alt | 60.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +13.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.298× (z -12.8) |
| [[SNU-423 (line)]] | alt | 155 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.265× (z -12.6) |
| [[C-33 A (line)]] | alt | 92.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.298× (z -12.6) |
| [[C32 (line)]] | wt | 53.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.287× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 53.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -10.8) |
| [[SNU-1 (line)]] | wt | 81.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.262× (z -11.4) |
| [[A498 (line)]] | wt | 23.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 84.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -13.3) |
| [[HT-29 (line)]] | alt | 44.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +9.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.335× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 26.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +8.8) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 27.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 20.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +12.7) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 58.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.378× (z -9.1) |
| [[SW1417 (line)]] | alt | 47.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.415× (z -9.0) |
| [[SW48 (line)]] | wt | 51.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.199× (z -11.2) |
| [[BT-474 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 64.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 92.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5017), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTBD1]] | +0.57 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[SEPTIN11]] | +0.55 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[ALG10B]] | +0.55 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[YES1]] | +0.54 | +0.38 / +0.59 | both halves | 6e-05 |  |
| [[AKAP11]] | +0.54 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[IPO5]] | +0.53 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[STK26]] | +0.52 | +0.38 / +0.43 | both halves | 7e-05 |  |
| [[TOP2B]] | +0.52 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[MTR]] | +0.52 | +0.49 / +0.54 | both halves | 2e-05 |  |
| [[ZDHHC23]] | +0.52 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[HMGN1]] | +0.52 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[ALG10]] | +0.52 | +0.37 / +0.50 | both halves | 9e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 11 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL36AL]] ⚠ | -0.57 | -0.35 / -0.55 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[SEC61B]] | -0.52 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[EMC6]] | -0.52 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[SF3B5]] ⚠ | -0.52 | -0.28 / -0.54 | both halves | 3e-04 | pathway: ATP-dependent chromatin remodelers; ⚠ in the vector space only through flagged drug-doses |
| [[TRAPPC2B]] | -0.51 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[COX6B1]] | -0.51 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[RABAC1]] | -0.50 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[BLVRB]] | -0.50 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[RASSF7]] | -0.50 | -0.26 / -0.52 | both halves | 4e-04 |  |
| [[NDUFA11]] ⚠ | -0.49 | -0.42 / -0.47 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MTF1]] | -0.49 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[ROMO1]] | -0.49 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[DTX2P1-UPK3BP1-PMS2P11]] | -0.49 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[PRKD2]] | -0.49 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[DSG3]] | -0.49 | -0.38 / -0.49 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMPRSS4]] | B | TMPRSS4 activity lowers PHF10's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 1.65× higher at baseline in the lines without TMPRSS4 | 0.006 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[TMPRSS4]] | B | TMPRSS4 activity weakens PHF10's drug response | lines that do not express TMPRSS4 (33) vs lines expressing it (16) | the lines without TMPRSS4 respond 1.27× as strongly (z diff -1.23); strongest at Idarubicin (hydrochloride) 5 µM: 0.61x vs 0.88x (z diff -4.2) | 0.017 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; target measured in part of the lines; both ways; artifact flags |
| [[CRYBG2]] | B | CRYBG2 activity lowers PHF10's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 1.21× higher at baseline in the lines without CRYBG2 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[PRSS8]] | B | PRSS8 activity lowers PHF10's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 1.44× higher at baseline in the lines without PRSS8 | 0.030 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[S100P]] | B | S100P activity lowers PHF10's level | lines that do not express S100P (34) vs lines expressing it (16) | 1.41× higher at baseline in the lines without S100P | 0.038 | ⚠ within organs, on part of the lines; also absent: POF1B, ENSG00000287426, CEACAM6 |
| [[MYBL1]] | B | MYBL1 activity raises PHF10's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.36× lower at baseline in the lines without MYBL1 | 0.093 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.501). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-34.6, -16.5); signed map (13.3, -12.3). **Vector** length 97.0, 25.1% of its response variance represented; |z| ≥ 3 in 1,309 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.2 | +4.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +14.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +16.9 |
|  | [[Roxadustat (drug)]] 5 µM |  | +2.1 | +3.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | +1.8 | +1.3 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +1.7 | +0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +1.7 | +1.2 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -4.4 | -8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -10.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.5 | -8.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -6.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.3 | -2.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.1 | -3.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.6 | -4.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | PHD finger protein 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q27 — chr6:169,703,902-169,725,566 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10975, XAP135, BAF45a, SMARCG4 |
| Gene groups (HGNC) | PHD finger proteins; BAF complex subunits; PBAF complex subunits |
| Reactome | 6 pathways, smallest: Formation of the polybromo-BAF (pBAF) complex; Formation of the embryonic stem cell BAF (esBAF) complex; Formation of neuronal progenitor and neuronal BAF (npBAF and nBAF) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUB8](https://www.uniprot.org/uniprotkb/Q8WUB8) (PHD finger protein 10):

> Involved in transcription activity regulation by chromatin remodeling. Belongs to the neural progenitors-specific chromatin remodeling complex (npBAF complex) and is required for the proliferation of neural progenitors. During neural development a switch from a stem/progenitor to a post-mitotic chromatin remodeling mechanism occurs as neurons exit the cell cycle and become committed to their adult state. The transition from proliferating neural stem/progenitor cells to post-mitotic neurons …

**Summary**, from NCBI Gene [55274](https://www.ncbi.nlm.nih.gov/gene/55274):

> This gene contains a predicted ORF that encodes a protein with two zinc finger domains. The function of the encoded protein is not known. Sequence analysis suggests that multiple alternatively spliced transcript variants are derived from this gene but the full-length nature of only two of them is known. These two splice variants encode different isoforms. A pseudogene for this gene is located on Xq28. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18250](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18250) · Entrez [55274](https://www.ncbi.nlm.nih.gov/gene/55274) · UniProt [Q8WUB8](https://www.uniprot.org/uniprotkb/Q8WUB8) · Ensembl [ENSG00000130024](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130024)

## Data

Gene col 5017: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5017); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5017, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5017]; `tensor/DDL_lfc|DDL_z.npy` [5017]; `embed/gene_vectors.npy` [5017]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5017 or target_col == 5017). Every well: [[PHF10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHF10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
