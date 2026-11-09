---
symbol: "GPR89B"
type: "gene"
col: 11975
ensembl_id: "ENSG00000188092"
name: "golgi pH regulator B"
location: "1q21.2"
module: 142
arm: "+"
pooled_cpm: 24.68
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 12
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# GPR89B

*golgi pH regulator B* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.78× (z +23.0, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.414× (z -15.3, q 0e+00, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.525× (z -5.9, q 6e-07, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPR89A]] (+0.88, fdr 7e-06), [[SLC30A6]] (+0.71, fdr 7e-06), [[ATG4B]] (+0.67, fdr 3e-05); moves opposite to [[RAP2C-AS1]] (-0.72, fdr 1e-05), [[HNRNPK]] (-0.69, fdr 3e-05), [[HNRNPH3]] (-0.68, fdr 3e-05).
> It is in [[Module 142]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PARD3B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11975.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.78×** | +23.0 | 0e+00 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.42×** | +21.3 | 0e+00 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.02×** | +19.1 | 0e+00 | 46/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.94×** | +11.5 | 2e-28 | 37/47 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.63×** | +8.0 | 1e-13 | 33/48 (SK-MEL-2, J82, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +8.0 | 1e-13 | 35/48 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.49×** | +6.6 | 3e-09 | 28/45 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.00×** | +6.3 | 3e-08 | 28/41 (RKO, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +6.1 | 7e-08 | 22/47 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.54×** | +5.2 | 1e-05 | 23/48 (RKO, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.66×** | +4.6 | 2e-04 | 18/48 (PANC-1, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.66×** | +4.6 | 2e-04 | 22/46 (Panc 03.27, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.31×** | +4.5 | 3e-04 | 23/46 (SW480, NCI-H23, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.30×** | +4.5 | 3e-04 | 18/48 (NCI-H2347, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.28×** | +4.3 | 7e-04 | 19/47 (RKO, KATO III, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.092 | 7/47 (A-172, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11975.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.414×** | -15.3 | 0e+00 | 40/44 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.517×** | -11.1 | 6e-26 | 24/34 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.510×** | -10.8 | 4e-25 | 30/38 (SW1417, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.525×** | -5.9 | 6e-07 | 25/48 (NCI-H1573, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.738×** | -5.3 | 1e-05 | 21/48 (A549, A498, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.729×** | -5.3 | 1e-05 | 21/45 (SW1417, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.765×** | -4.7 | 2e-04 | 21/46 (C32, PANC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~61% of this change | **0.785×** | -4.2 | 0.002 | 21/45 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.827×** | -3.3 | 0.053 | 8/48 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.825×** | -3.3 | 0.064 | 15/47 (A549, PANC-1, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.770×** | -3.2 | 0.074 | 13/44 (A549, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.876× | -3.2 | 0.074 | 11/48 (A-427, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.837× | -3.1 | 0.077 | 10/48 (A549, C32, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.833×** | -3.1 | 0.081 | 16/47 (A549, KATO III, …) | two highest doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11975. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 24.2 | 3 | 6 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 4.86× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.234× (z -14.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 36.0 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.61× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -20.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 25.2 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.68× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -11.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 20.5 | 4 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.33× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 20.8 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.57× (z +9.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.279× (z -9.1) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 33.5 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.52× (z +12.0) | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 34.7 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.95× (z +16.0) | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -14.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 24.1 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.25× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.0637× (z -19.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 28.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.70× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -13.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 28.0 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.22× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.114× (z -13.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 27.9 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.93× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.130× (z -17.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 39.2 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.22× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -13.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 19.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.75× (z +11.5) | — |
| [[AsPC-1 (line)]] | alt | 20.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.46× (z +11.7) | — |
| [[HT-29 (line)]] | alt | 32.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0894× (z -17.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 29.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.39× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 19.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.14× (z +11.1) | — |
| [[Panc 03.27 (line)]] | alt | 25.6 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.64× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -10.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 20.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.06× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 15.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.79× (z +9.5) | — |
| [[A498 (line)]] | wt | 14.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.37× (z +10.6) | — |
| [[A549 (line)]] | wt | 17.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.53× (z +10.1) | — |
| [[CFPAC-1 (line)]] | alt | 21.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.51× (z +9.3) | — |
| [[J82 (line)]] | alt | 24.2 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.09× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.219× (z -11.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 17.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.97× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 22.1 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.03× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.212× (z -9.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 27.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.12× (z +12.0) | — |
| [[NCI-H1573 (line)]] | alt | 23.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.274× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 47.3 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.17× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -8.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[Vortioxetine (drug)]] 5 µM 0.0728× (z -9.1) ⚠ toxic |
| [[C-33 A (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -8.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 21.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.202× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 31.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -10.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 12.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.07× (z +8.6) | — |
| [[RKO (line)]] | wt | 35.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.57× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.156× (z -10.2) ⚠ transcription drop; cell-cycle shift, explains ~61% of this change |
| [[SW48 (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -9.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11975), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR89A]] | +0.88 | +0.82 / +0.88 | both halves | 7e-06 | STRING 780 |
| [[SLC30A6]] | +0.71 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[ATG4B]] | +0.67 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[MPG]] | +0.66 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[QPCTL]] | +0.66 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[RBAK-RBAKDN]] | +0.66 | +0.37 / +0.68 | both halves | 8e-05 |  |
| [[HM13]] | +0.65 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ZCCHC17]] | +0.65 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[SS18L1]] | +0.65 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[BET1L]] | +0.64 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[SSR2]] | +0.64 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[DHDDS]] | +0.64 | +0.48 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAP2C-AS1]] | -0.72 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[HNRNPK]] | -0.69 | -0.44 / -0.70 | both halves | 3e-05 |  |
| [[HNRNPH3]] | -0.68 | -0.43 / -0.66 | both halves | 3e-05 |  |
| [[BMI1]] | -0.64 | -0.40 / -0.62 | both halves | 5e-05 |  |
| [[YWHAE]] | -0.62 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[TAF9B]] | -0.62 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[ATF7IP]] | -0.61 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[TBL1XR1]] | -0.59 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[CGGBP1]] | -0.59 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[NCOA4]] | -0.59 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[HMGN2]] | -0.58 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[TAFA2]] | -0.58 | -0.36 / -0.46 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARD3B]] | B | PARD3B activity lowers GPR89B's level | lines that do not express PARD3B (9) vs lines expressing it (41) | 1.12× higher at baseline in the lines without PARD3B | 0.089 | ⚠ within organs, on part of the lines; also absent: MRAS, LPCAT2, ZNF618 |
| [[RGS10]] | C | RGS10 activity lowers GPR89B's level | lines that do not express RGS10 (4) vs lines expressing it (46) | 1.39× higher at baseline in the lines without RGS10 | 0.092 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HOMER3, ARHGEF17, CHST3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction 0.712). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.3, -4.9); signed map (-44.6, 4.5). **Vector** length 94.9, 22.8% of its response variance represented; |z| ≥ 3 in 1,066 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.1 | +11.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.8 | +8.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | +3.8 | +6.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.7 | +6.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.4 | +21.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.7 | +5.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.4 | +4.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | +4.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.7 | +2.9 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.0 | -10.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.9 | -3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.4 | -15.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.9 | -11.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -4.7 | -5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.6 | -1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | golgi pH regulator B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:147,928,393-147,993,592 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GPHRB, SH120; previously GPR89, GPR89C, LINC02804, GPR89B |
| Gene groups (HGNC) | Golgi pH regulators |
| Matched by | ensembl_id |

**Function**, from UniProt [P0CG08](https://www.uniprot.org/uniprotkb/P0CG08) (Golgi pH regulator B):

> Voltage-gated channel that enables the transfer of anions such as iodide, chloride, bromide and fluoride which may function in counter-ion conductance and participates in Golgi acidification. Plays a role in lymphocyte development, probably by acting as a RABL3 effector in hematopoietic cells (By similarity). Essential for maintaining the acidic luminal pH of the Golgi apparatus in neurons, which is important for preserving Golgi structural integrity (By similarity). This integrity supports …

**Summary**, from NCBI Gene [51463](https://www.ncbi.nlm.nih.gov/gene/51463):

> Enables voltage-gated monoatomic anion channel activity. Involved in intracellular pH reduction. Located in Golgi cisterna membrane and Golgi-associated vesicle membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13840](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13840) · Entrez [51463](https://www.ncbi.nlm.nih.gov/gene/51463) · UniProt [P0CG08](https://www.uniprot.org/uniprotkb/P0CG08) · Ensembl [ENSG00000188092](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188092)

## Data

Gene col 11975: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11975); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11975, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11975]; `tensor/DDL_lfc|DDL_z.npy` [11975]; `embed/gene_vectors.npy` [11975]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11975 or target_col == 11975). Every well: [[GPR89B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPR89B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
