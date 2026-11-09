---
symbol: "EXD2"
type: "gene"
col: 1311
ensembl_id: "ENSG00000081177"
name: "exonuclease 3'-5' domain containing 2"
location: "14q24.1"
module: 65
arm: "+"
pooled_cpm: 19.91
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 30
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# EXD2

*exonuclease 3'-5' domain containing 2* — 14q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.23× (z +5.1, q 2e-04, up in 19 of 47 measured lines) ⚠ cell-cycle shift, explains ~97% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.32× (z +4.8, q 3e-04, up in 13 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (19 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.346× (z -25.8, q 0e+00, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HEATR6]] (+0.72, fdr 7e-06), [[MRS2]] (+0.70, fdr 7e-06), [[MIGA1]] (+0.69, fdr 7e-06); moves opposite to [[PKNOX1]] (-0.59, fdr 1e-05), [[DDX5]] (-0.58, fdr 1e-05), [[TUT7]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1311.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.23×** | +5.1 | 2e-04 | 19/47 (A498, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.34×** | +5.0 | 2e-04 | 21/47 (NCI-H1792, SW480, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +4.8 | 3e-04 | 13/47 (KATO III, HOP62, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.021 | 9/44 (Panc 03.27, AN3 CA, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.23×** | +3.5 | 0.045 | 15/47 (Hs 766T, SK-MEL-2, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.15× | +3.4 | 0.074 | 12/47 (SW 900, A-172, …) | rises with dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.11 | 9/47 (Panc 03.27, HEC-1-A, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.11 | 4/46 (NCI-H2030, RKO, …) | rises with dose | low cells (technical?) |
| [[Bimiralisib (drug)]] 5 µM |  | 1.41× | +3.1 | 0.11 | 9/47 (SW480, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.0 | 0.13 | 5/47 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 1.21× | +3.0 | 0.13 | 8/47 (NCI-H23, SW480, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 21 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1311.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.346×** | -25.8 | 0e+00 | 41/46 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.293×** | -20.3 | 0e+00 | 42/46 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.363×** | -17.4 | 0e+00 | 47/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.384×** | -16.4 | 0e+00 | 40/45 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.466×** | -13.1 | 3e-37 | 41/47 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.600×** | -12.4 | 2e-33 | 34/46 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.510×** | -11.6 | 5e-29 | 39/46 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.554×** | -10.1 | 3e-22 | 32/45 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.569×** | -9.7 | 2e-20 | 32/46 (SNU-423, C-33 A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | **0.606×** | -8.6 | 4e-16 | 23/40 (A-427, NCI-H1573, …) | inconsistent across doses | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.648×** | -7.5 | 5e-12 | 29/46 (A-172, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.649×** | -7.4 | 6e-12 | 25/47 (HS-578T, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.644×** | -7.3 | 2e-11 | 29/47 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.645×** | -7.2 | 2e-11 | 27/45 (C32, NCI-H460, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **0.662×** | -6.8 | 4e-10 | 29/43 (LOX-IMVI, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.752×** | -4.9 | 3e-05 | 23/46 (CFPAC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.822×** | -4.7 | 5e-05 | 18/47 (HOP62, Hs 766T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.786×** | -4.1 | 8e-04 | 18/47 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.790×** | -3.8 | 0.003 | 16/46 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.765×** | -3.1 | 0.042 | 4/47 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Resveratrol (drug)]] 5 µM |  | 0.890× | -2.8 | 0.086 | 4/47 (HCT15, NCI-H1573, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.731×** | -2.8 | 0.086 | 10/43 (SHP-77, J82, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1311. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 22.1 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -23.4) |
| [[MIA PaCa-2 (line)]] | alt | 23.5 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -20.8) |
| [[NCI-H1573 (line)]] | alt | 22.9 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.127× (z -14.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.190× (z -11.3) |
| [[C32 (line)]] | wt | 18.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -10.0) |
| [[A549 (line)]] | wt | 21.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -17.1) |
| [[HOP62 (line)]] | alt | 14.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 15.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -15.5) |
| [[SW480 (line)]] | alt | 27.7 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.236× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.383× (z -9.6) |
| [[A-172 (line)]] | wt | 15.8 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0690× (z -17.3) |
| [[NCI-H1792 (line)]] | alt | 29.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -21.3) |
| [[NCI-H23 (line)]] | alt | 37.1 | 0 | 4 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -15.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.443× (z -9.0) |
| [[PANC-1 (line)]] | alt | 12.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -14.4) |
| [[SW 900 (line)]] | alt | 19.3 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0779× (z -14.4) |
| [[CFPAC-1 (line)]] | alt | 28.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -12.2) |
| [[NCI-H2030 (line)]] | alt | 44.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.214× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.292× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 17.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -14.8) |
| [[A-427 (line)]] | wt | 19.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.265× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 28.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -11.1) |
| [[HS-578T (line)]] | alt | 14.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -18.7) |
| [[J82 (line)]] | alt | 16.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -16.6) |
| [[LS 180 (line)]] | wt | 20.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[Panc 03.27 (line)]] | alt | 28.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -13.9) |
| [[RKO (line)]] | wt | 22.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -14.7) |
| [[SNU-423 (line)]] | alt | 11.9 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.111× (z -12.3) |
| [[SW48 (line)]] | wt | 40.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[A498 (line)]] | wt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -12.7) |
| [[BT-474 (line)]] | alt | 22.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -10.5) |
| [[C-33 A (line)]] | alt | 24.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.124× (z -11.7) |
| [[H4 (line)]] | wt | 10.7 | 0 | 1 | — | [[Tofacitinib (drug)]] 0.5 µM 0.0887× (z -8.6) |
| [[HCT15 (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 12.5 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.128× (z -8.9) |
| [[KATO III (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[RPMI-7951 (line)]] | alt | 18.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -14.0) |
| [[AN3 CA (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.81 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1311), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEATR6]] | +0.72 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[MRS2]] | +0.70 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[MIGA1]] | +0.69 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[ALG9]] | +0.68 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[SKIC3]] | +0.65 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[STX7]] | +0.65 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[MINDY3]] | +0.64 | +0.65 / +0.57 | both halves | 8e-06 |  |
| [[RAD17]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[TADA1]] | +0.63 | +0.74 / +0.48 | both halves | 2e-05 |  |
| [[AKTIP]] | +0.63 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[DDHD2]] | +0.62 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[ANAPC4]] | +0.62 | +0.65 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKNOX1]] | -0.59 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[DDX5]] | -0.58 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[TUT7]] | -0.57 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[SATB2]] | -0.56 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[BAZ1A]] | -0.55 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[DPH1-AS1]] | -0.54 | -0.62 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises EXD2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.719). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-6.8, -11.1); signed map (-31.6, -14.7). **Vector** length 73.7, 14.8% of its response variance represented; |z| ≥ 3 in 1,194 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | +5.9 | +5.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | +3.8 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +4.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +1.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.2 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | -0.6 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +0.2 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -4.7 | -16.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.3 | -11.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.2 | -20.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.0 | -25.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.9 | -17.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -4.7 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.8 | -1.5 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.8 | -2.1 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | exonuclease 3'-5' domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.1 — chr14:69,191,498-69,244,020 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10738; previously C14orf114, EXDL2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVH0](https://www.uniprot.org/uniprotkb/Q9NVH0) (Exonuclease 3'-5' domain-containing protein 2):

> Exonuclease that has both 3'-5' exoribonuclease and exodeoxyribonuclease activities, depending on the divalent metal cation used as cofactor. In presence of Mg(2+), only shows 3'-5' exoribonuclease activity, while it shows both exoribonuclease and exodeoxyribonuclease activities in presence of Mn(2+). Acts as an exoribonuclease in mitochondrion, possibly by regulating ATP production and mitochondrial translation. Also involved in the response to DNA damage. Acts as 3'-5' exodeoxyribonuclease …

**Summary**, from NCBI Gene [55218](https://www.ncbi.nlm.nih.gov/gene/55218):

> Enables 3'-5' exonuclease activity; metal ion binding activity; and protein homodimerization activity. Involved in DNA double-strand break processing; double-strand break repair via homologous recombination; and replication fork processing. Located in mitochondrial outer membrane and site of DNA damage. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20217](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20217) · Entrez [55218](https://www.ncbi.nlm.nih.gov/gene/55218) · UniProt [Q9NVH0](https://www.uniprot.org/uniprotkb/Q9NVH0) · Ensembl [ENSG00000081177](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081177)

## Data

Gene col 1311: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1311); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1311, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1311]; `tensor/DDL_lfc|DDL_z.npy` [1311]; `embed/gene_vectors.npy` [1311]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1311 or target_col == 1311). Every well: [[EXD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
