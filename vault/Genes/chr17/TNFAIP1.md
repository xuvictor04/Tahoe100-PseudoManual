---
symbol: "TNFAIP1"
type: "gene"
col: 3023
ensembl_id: "ENSG00000109079"
name: "TNF alpha induced protein 1"
location: "17q11.2"
module: 116
arm: "+"
pooled_cpm: 38.64
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 15
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# TNFAIP1

*TNF alpha induced protein 1* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 5 µM: 1.54× (z +8.2, q 9e-14, up in 29 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Peretinoin (drug)]] 5 µM: 1.53× (z +7.7, q 4e-12, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.634× (z -12.2, q 3e-31, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIC8A]] (+0.57, fdr 4e-05), [[SFN]] (+0.55, fdr 3e-05), [[ABL2]] (+0.54, fdr 1e-05); moves opposite to [[MATR3]] (-0.56, fdr 1e-05), [[DTWD2]] (-0.49, fdr 1e-04), [[EXOSC8]] (-0.47, fdr 4e-05).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MET]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3023.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.54×** | +8.2 | 9e-14 | 29/48 (HT-29, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.53×** | +7.7 | 4e-12 | 29/47 (HT-29, COLO 205, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.48×** | +7.5 | 2e-11 | 32/47 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.29×** | +6.8 | 2e-09 | 29/48 (HT-29, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.38×** | +6.1 | 1e-07 | 27/48 (HT-29, LS 180, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.31×** | +5.1 | 3e-05 | 22/47 (HT-29, COLO 205, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.05 µM |  | **1.31×** | +4.8 | 1e-04 | 21/48 (BT-474, SK-MEL-2, …) | all doses, flat |  |
| [[vincristine (drug)]] 5 µM |  | **1.61×** | +4.7 | 1e-04 | 22/44 (HT-29, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.27×** | +4.6 | 3e-04 | 21/47 (LS 180, LoVo, …) | rises with dose | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **1.40×** | +4.6 | 3e-04 | 24/48 (HT-29, NCI-H1573, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.27×** | +4.4 | 5e-04 | 23/47 (SK-MEL-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +4.1 | 0.002 | 13/48 (PANC-1, A498, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.2 | 0.053 | 13/39 (hTERT-HPNE, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.0 | 0.094 | 11/47 (PANC-1, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3023.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.634×** | -12.2 | 3e-31 | 35/47 (KATO III, HCT15, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.621×** | -9.0 | 6e-17 | 33/47 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.697×** | -6.6 | 1e-08 | 22/36 (LoVo, HCT15, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.710×** | -6.5 | 1e-08 | 34/48 (LOX-IMVI, NCI-H23, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.710×** | -6.2 | 5e-08 | 28/47 (NCI-H23, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.704×** | -6.1 | 8e-08 | 22/41 (HT-29, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[crizotinib (drug)]] 5 µM |  | **0.804×** | -4.0 | 0.006 | 15/48 (SNU-1, RKO, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.672×** | -3.9 | 0.006 | 14/34 (SW 900, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~11% of this change | **0.807×** | -3.9 | 0.006 | 19/47 (hTERT-HPNE, J82, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | **0.818×** | -3.8 | 0.008 | 20/47 (NCI-H1792, NCI-H661, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.812×** | -3.8 | 0.008 | 16/47 (A-427, SNU-423, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.824×** | -3.6 | 0.013 | 16/48 (A498, SW480, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.831×** | -3.5 | 0.019 | 16/48 (RKO, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.831×** | -3.5 | 0.019 | 20/47 (LoVo, HCT15, …) | rises with dose | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.710×** | -3.4 | 0.027 | 12/47 (SK-MEL-2, AN3 CA, …) | top dose only | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3023. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 35.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.529× (z -8.7) |
| [[HCT15 (line)]] | alt | 53.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -15.0) |
| [[HT-29 (line)]] | alt | 29.5 | 1 | 1 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.15× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -10.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 51.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -19.0) |
| [[LOX-IMVI (line)]] | wt | 80.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.463× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 36.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Daptomycin (drug)]] 0.5 µM 2.72× (z +8.6) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 33.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -13.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 38.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.418× (z -9.5) |
| [[AN3 CA (line)]] | alt | 24.2 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0733× (z -9.3) |
| [[BT-474 (line)]] | alt | 60.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -12.1) |
| [[C32 (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -9.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 39.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -13.9) |
| [[H4 (line)]] | wt | 42.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -8.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 57.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -11.1) |
| [[hTERT-HPNE (line)]] | wt | 42.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.230× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~11% of this change |
| [[J82 (line)]] | alt | 35.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.338× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~11% of this change |
| [[NCI-H1792 (line)]] | alt | 34.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.232× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[NCI-H2030 (line)]] | alt | 35.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 57.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.259× (z -13.3) |
| [[NCI-H2347 (line)]] | alt | 24.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 33.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -10.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -10.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 39.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3023), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIC8A]] | +0.57 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[SFN]] | +0.55 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[ABL2]] | +0.54 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[ORMDL2]] | +0.53 | +0.37 / +0.57 | both halves | 8e-05 |  |
| [[PLIN3]] | +0.53 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[TBC1D2]] | +0.53 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[ELOVL1]] | +0.51 | +0.39 / +0.60 | both halves | 6e-05 |  |
| [[TM2D2]] | +0.51 | +0.32 / +0.53 | both halves | 2e-04 |  |
| [[BTBD10]] | +0.51 | +0.50 / +0.50 | both halves | 1e-05 | same gene group; STRING 650 |
| [[LUZP1]] | +0.51 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[NABP1]] | +0.50 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[HRH1]] | +0.49 | +0.50 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MATR3]] | -0.56 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[DTWD2]] | -0.49 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[EXOSC8]] | -0.47 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[KCTD3]] | -0.47 | -0.37 / -0.49 | both halves | 8e-05 | same gene group |
| [[PPA2]] | -0.45 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[SLC25A40]] | -0.44 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[PHOSPHO2]] | -0.44 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[UBA5]] | -0.44 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[NFIA]] | -0.43 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[HADH]] | -0.43 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[SSRP1]] | -0.43 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[MANEA]] | -0.43 | -0.37 / -0.42 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MET]] | B | MET activity raises TNFAIP1's level | compounds that target MET: 3 of 4 lower it (Cabozantinib, Crizotinib / crizotinib, c-Kit-IN-1) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAST4]] | B | MAST4 activity raises TNFAIP1's level | lines that do not express MAST4 (11) vs lines expressing it (39) | 1.28× lower at baseline in the lines without MAST4 | 0.090 | ⚠ within organs, on part of the lines; also absent: TSPAN12, AHR, TLE4; maybe low, not absent |
| [[TBC1D2]] | C | TBC1D2 activity raises TNFAIP1's level | lines that do not express TBC1D2 (4) vs lines expressing it (46) | 1.68× lower at baseline in the lines without TBC1D2 | 0.023 | ⚠ few lines (4 vs 46); across organs; also absent: ARHGAP27; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.427). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-21.6, 35.6); signed map (-5.9, 41.9). **Vector** length 112, 28.0% of its response variance represented; |z| ≥ 3 in 1,042 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Peretinoin (drug)]] 5 µM |  | +7.0 | +7.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.8 | +6.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +6.4 | +8.2 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +6.3 | +7.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +5.8 | +5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +5.7 | +6.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +5.5 | +4.6 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -5.6 | -6.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.8 | -3.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.6 | -3.6 |
|  | [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.8 | -2.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | TNF alpha induced protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,335,602-28,347,009 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B61, B12, MGC2317, BTBD34; previously EDP1 |
| Gene groups (HGNC) | BTB domain containing |
| Reactome | 5 pathways, smallest: RND2 GTPase cycle; RND3 GTPase cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13829](https://www.uniprot.org/uniprotkb/Q13829) (BTB/POZ domain-containing adapter for CUL3-mediated RhoA degradation protein 2):

> Substrate-specific adapter of a BCR (BTB-CUL3-RBX1) E3 ubiquitin-protein ligase complex involved in regulation of cytoskeleton structure. The BCR(TNFAIP1) E3 ubiquitin ligase complex mediates the ubiquitination of RHOA, leading to its degradation by the proteasome, thereby regulating the actin cytoskeleton and cell migration. Its interaction with RHOB may regulate apoptosis. May enhance the PCNA-dependent DNA polymerase delta activity.

**Summary**, from NCBI Gene [7126](https://www.ncbi.nlm.nih.gov/gene/7126):

> This gene was identified as a gene whose expression can be induced by the tumor necrosis factor alpha (TNF) in umbilical vein endothelial cells. Studies of a similar gene in mouse suggest that the expression of this gene is developmentally regulated in a tissue-specific manner. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11894](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11894) · Entrez [7126](https://www.ncbi.nlm.nih.gov/gene/7126) · UniProt [Q13829](https://www.uniprot.org/uniprotkb/Q13829) · Ensembl [ENSG00000109079](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109079)

## Data

Gene col 3023: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3023); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3023, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3023]; `tensor/DDL_lfc|DDL_z.npy` [3023]; `embed/gene_vectors.npy` [3023]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3023 or target_col == 3023). Every well: [[TNFAIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFAIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
