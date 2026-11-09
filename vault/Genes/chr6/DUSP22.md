---
symbol: "DUSP22"
type: "gene"
col: 3393
ensembl_id: "ENSG00000112679"
name: "dual specificity phosphatase 22"
location: "6p25.3"
module: 126
arm: "+"
pooled_cpm: 21.66
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 20
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# DUSP22

*dual specificity phosphatase 22* — 6p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.33× (z +7.1, q 1e-09, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.468× (z -18.8, q 0e+00, down in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.557× (z -10.2, q 4e-22, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FCHO2]] (+0.63, fdr 7e-06), [[SLC41A3]] (+0.62, fdr 1e-05), [[TEAD3]] (+0.60, fdr 1e-05); moves opposite to [[KBTBD7]] (-0.55, fdr 1e-05), [[ABCF1]] (-0.50, fdr 3e-05), [[BMS1]] (-0.49, fdr 4e-05).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EVA1A-AS]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3393.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +7.1 | 1e-09 | 25/47 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.36×** | +5.3 | 3e-05 | 23/47 (NCI-H2030, SW480, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.37×** | +5.2 | 3e-05 | 20/47 (A-172, H4, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.19× | +4.3 | 0.002 | 14/48 (A-427, LOX-IMVI, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.011 | 18/47 (A498, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.22×** | +3.5 | 0.053 | 10/47 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.060 | 10/47 (HT-29, HCT15, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.21×** | +3.3 | 0.066 | 13/47 (A-172, SW48, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.066 | 7/47 (NCI-H2030, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.073 | 10/48 (CFPAC-1, H4, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.073 | 14/46 (CFPAC-1, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3393.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.468×** | -18.8 | 0e+00 | 43/47 (NCI-H1573, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.557×** | -10.2 | 4e-22 | 30/46 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.350×** | -9.6 | 1e-19 | 36/48 (SW480, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.583×** | -9.4 | 5e-19 | 37/47 (J82, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.595×** | -9.1 | 1e-17 | 37/47 (SW480, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.629×** | -8.1 | 5e-14 | 33/47 (A549, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.722×** | -5.7 | 1e-06 | 23/47 (NCI-H23, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.719×** | -5.5 | 2e-06 | 25/46 (NCI-H1573, HEC-1-A, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.601×** | -4.7 | 2e-04 | 20/46 (RPMI-7951, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.766×** | -4.6 | 2e-04 | 19/47 (NCI-H23, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.770×** | -4.4 | 6e-04 | 20/45 (NCI-H1573, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.629×** | -4.2 | 0.001 | 17/45 (NCI-H1792, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.809×** | -3.7 | 0.009 | 18/47 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.668×** | -3.7 | 0.009 | 11/46 (SW480, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.813×** | -3.6 | 0.011 | 14/47 (NCI-H1573, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.817×** | -3.5 | 0.015 | 14/47 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.822×** | -3.4 | 0.020 | 12/48 (HCT15, A-172, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.788×** | -3.0 | 0.082 | 6/48 (LOX-IMVI, C32, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3393. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 21.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -17.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.188× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 23.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0362× (z -20.6) |
| [[A-427 (line)]] | wt | 46.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -16.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.350× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 15.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -13.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.318× (z -9.0) |
| [[Hs 766T (line)]] | wt | 26.0 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.362× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 17.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0318× (z -22.3) |
| [[MIA PaCa-2 (line)]] | alt | 23.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -10.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Abemaciclib (drug)]] 5 µM 0.0782× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 37.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -12.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.285× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 28.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -14.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.242× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 31.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 23.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -10.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A498 (line)]] | wt | 11.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +9.0) | — |
| [[AsPC-1 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -10.0) ⚠ cell-cycle shift, explains ~35% of this change |
| [[CFPAC-1 (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -9.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[J82 (line)]] | alt | 25.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.293× (z -9.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[KATO III (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -9.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LoVo (line)]] | wt | 15.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[Panc 03.27 (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -13.0) ⚠ cell-cycle shift, explains ~35% of this change |
| [[RPMI-7951 (line)]] | alt | 11.1 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0976× (z -9.5) |
| [[A-172 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3393), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCHO2]] | +0.63 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[SLC41A3]] | +0.62 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[TEAD3]] | +0.60 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[SAP30L-AS1]] | +0.60 | +0.38 / +0.51 | both halves | 7e-05 |  |
| [[SGPP1]] | +0.57 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[PCBP4]] | +0.57 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[HECA]] | +0.55 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[SNHG22]] | +0.54 | +0.39 / +0.48 | both halves | 6e-05 |  |
| [[CERS2]] | +0.53 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[CMTM4]] | +0.53 | +0.61 / +0.39 | both halves | 5e-05 |  |
| [[UBE2Q2]] | +0.53 | +0.52 / +0.49 | both halves | 2e-05 |  |
| [[PCGF5]] | +0.53 | +0.46 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KBTBD7]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[ABCF1]] | -0.50 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[BMS1]] | -0.49 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[TRA2B]] | -0.49 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[MAGED1]] | -0.48 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[CWC22]] | -0.48 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[DDX1]] | -0.48 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[ZNF414]] | -0.48 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[KAT5]] | -0.47 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[KIF3B]] | -0.46 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[ODAD4]] | -0.46 | -0.51 / -0.37 | both halves | 7e-05 |  |
| [[TTC26]] | -0.46 | -0.45 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EVA1A-AS]] | B | EVA1A-AS activity lowers DUSP22's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 1.36× higher at baseline in the lines without EVA1A-AS | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.449). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.7, -1.8); signed map (-17.7, 20.8). **Vector** length 91.3, 19.5% of its response variance represented; |z| ≥ 3 in 966 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +7.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +3.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +0.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.3 | +5.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.2 | +4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +5.3 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.3 | +3.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -4.3 | -18.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -10.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.3 | -2.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.3 | -9.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -4.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.0 | -2.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -3.7 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -2.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | dual specificity phosphatase 22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.3 — chr6:291,630-351,355 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MKPX, JSP1, JKAP, VHX |
| Gene groups (HGNC) | Atypical dual specificity phosphatases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRW4](https://www.uniprot.org/uniprotkb/Q9NRW4) (Dual specificity protein phosphatase 22):

> Dual specificity phosphatase; can dephosphorylate both phosphotyrosine and phosphoserine or phosphothreonine residues. Activates the JNK signaling pathway. Inhibits T-cell receptor signaling and T-cell mediated immune responses, acting, at least in part, by inducing degradation of E3 ubiquitin ligase UBR2. Dephosphorylates and thereby induces 'Lys-48'-linked ubiquitination of UBR2, leading to proteasomal degradation of UBR2. Dephosphorylates and thereby inactivates tyrosine kinase LCK. Inhibits …

**Summary**, from NCBI Gene [56940](https://www.ncbi.nlm.nih.gov/gene/56940):

> Enables phosphoprotein phosphatase activity; protein tyrosine kinase binding activity; and protein tyrosine kinase inhibitor activity. Involved in several processes, including cellular response to epidermal growth factor stimulus; negative regulation of T cell receptor signaling pathway; and negative regulation of focal adhesion assembly. Acts upstream of or within negative regulation of transcription by RNA polymerase II. Located in cytoplasm and leading edge of lamellipodium. Part of …

**Accessions** — [HGNC:16077](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16077) · Entrez [56940](https://www.ncbi.nlm.nih.gov/gene/56940) · UniProt [Q9NRW4](https://www.uniprot.org/uniprotkb/Q9NRW4) · Ensembl [ENSG00000112679](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112679)

## Data

Gene col 3393: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3393); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3393, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3393]; `tensor/DDL_lfc|DDL_z.npy` [3393]; `embed/gene_vectors.npy` [3393]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3393 or target_col == 3393). Every well: [[DUSP22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUSP22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
