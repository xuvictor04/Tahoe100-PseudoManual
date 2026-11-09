---
symbol: "TTF1"
type: "gene"
col: 4622
ensembl_id: "ENSG00000125482"
name: "transcription termination factor 1"
location: "9q34.13"
module: 149
arm: "+"
pooled_cpm: 53.63
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/149"]
generated_by: "tahoemap"
---

# TTF1

*transcription termination factor 1* — 9q34.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.65× (z +11.9, q 8e-30, up in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.73× (z +9.2, q 1e-17, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.665× (z -9.7, q 3e-19, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALKBH1]] (+0.79, fdr 7e-06), [[NKAPD1]] (+0.77, fdr 7e-06), [[BRAP]] (+0.75, fdr 7e-06); moves opposite to [[STT3B]] (-0.62, fdr 7e-06), [[TFRC]] (-0.61, fdr 1e-05), [[EMB]] (-0.60, fdr 1e-05).
> It is in [[Module 149]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4622.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.65×** | +11.9 | 8e-30 | 43/48 (PANC-1, NCI-H2030, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +9.2 | 1e-17 | 40/48 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.31×** | +7.3 | 5e-11 | 35/49 (RKO, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +6.8 | 1e-09 | 34/48 (BT-474, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +5.6 | 3e-06 | 35/47 (SNU-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +5.1 | 3e-05 | 32/48 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.36×** | +4.9 | 8e-05 | 29/48 (LOX-IMVI, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.29×** | +4.2 | 0.002 | 23/48 (PANC-1, NCI-H1573, …) | top dose only | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.1 | 0.003 | 16/48 (RKO, HT-29, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.9 | 0.005 | 22/44 (RKO, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.038 | 21/48 (HOP62, SW480, …) | rises with dose |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.069 | 9/49 (KATO III, LS 180, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.069 | 21/48 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.42×** | +3.1 | 0.082 | 15/47 (RKO, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4622.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.665×** | -9.7 | 3e-19 | 44/48 (SNU-423, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.561×** | -9.3 | 3e-18 | 33/43 (SHP-77, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.665×** | -6.8 | 2e-09 | 39/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.681×** | -6.4 | 2e-08 | 32/49 (COLO 205, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.689×** | -6.0 | 2e-07 | 32/47 (SHP-77, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.761×** | -4.6 | 5e-04 | 26/48 (CFPAC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.639×** | -3.9 | 0.007 | 27/48 (SK-MEL-2, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.804×** | -3.4 | 0.054 | 20/45 (SNU-423, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.870× | -3.3 | 0.062 | 12/48 (SW 1271, PANC-1, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.821×** | -3.2 | 0.085 | 22/49 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4622. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 81.4 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.3) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 5 µM 0.110× (z -21.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 62.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +15.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.69× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -9.8) ⚠ cell-cycle shift, explains ~17% of this change |
| [[COLO 205 (line)]] | alt | 86.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +12.4) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -11.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 72.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +13.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.62× (z +10.9) | [[Digitoxin (drug)]] 5 µM 0.433× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 35.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +17.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.32× (z +13.8) | — |
| [[NCI-H460 (line)]] | wt | 55.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.25× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.483× (z -8.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 42.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.20× (z +30.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.55× (z +21.9) | — |
| [[SNU-423 (line)]] | alt | 66.8 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.6) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.336× (z -9.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 50.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +19.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.49× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 54.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +12.3) ⚠ cell-cycle shift, explains ~17% of this change | [[Dinaciclib (drug)]] 5 µM 0.287× (z -12.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 36.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +10.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.86× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 32.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.10× (z +21.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.47× (z +14.5) | — |
| [[NCI-H23 (line)]] | alt | 63.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +15.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[AN3 CA (line)]] | alt | 70.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.189× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 94.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.62× (z +10.0) | — |
| [[C-33 A (line)]] | alt | 62.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -10.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 77.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0945× (z -18.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 40.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.324× (z -9.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 46.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +13.4) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[LS 180 (line)]] | wt | 45.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -8.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 61.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.382× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 39.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +10.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[Panc 03.27 (line)]] | alt | 59.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.299× (z -10.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 88.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -10.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 44.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -10.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 85.6 | 0 | 1 | — | [[Penfluridol (drug)]] 5 µM 0.144× (z -8.8) |
| [[SW 900 (line)]] | alt | 38.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0948× (z -17.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 61.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.426× (z -8.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 72.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +10.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 53.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 64.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 55.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 56.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4622), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALKBH1]] | +0.79 | +0.84 / +0.76 | both halves | 7e-06 |  |
| [[NKAPD1]] | +0.77 | +0.74 / +0.84 | both halves | 7e-06 |  |
| [[BRAP]] | +0.75 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[ALKBH4]] | +0.75 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.74 | +0.81 / +0.67 | both halves | 7e-06 |  |
| [[ZNF3]] | +0.73 | +0.81 / +0.63 | both halves | 7e-06 |  |
| [[TRAPPC2B]] | +0.73 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[SLC4A1AP]] | +0.71 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[ANKRD49]] | +0.70 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[MRPS18C]] | +0.70 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[TRIM4]] | +0.70 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[ZNF557]] | +0.69 | +0.75 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STT3B]] | -0.62 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[TFRC]] | -0.61 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[EMB]] | -0.60 | -0.61 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises TTF1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 149]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.857). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.9, 4.9); signed map (-7.9, -12.1). **Vector** length 128, 37.9% of its response variance represented; |z| ≥ 3 in 780 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +10.1 | +11.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.8 | +9.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.3 | +7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +6.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.1 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +1.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.9 | +2.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.7 | -9.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.2 | -9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.8 | -6.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.1 | -6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.5 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -3.9 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -2.0 | -2.5 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -2.0 | -2.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -2.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | transcription termination factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.13 — chr9:132,375,548-132,406,851 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Myb/SANT domain containing |
| Reactome | 9 pathways, smallest: Surfactant metabolism; ERCC6 (CSB) and EHMT2 (G9a) positively regulate rRNA expression; RNA Polymerase I Transcription Termination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15361](https://www.uniprot.org/uniprotkb/Q15361) (Transcription termination factor 1):

> Multifunctional nucleolar protein that terminates ribosomal gene transcription, mediates replication fork arrest and regulates RNA polymerase I transcription on chromatin. Plays a dual role in rDNA regulation, being involved in both activation and silencing of rDNA transcription. Interaction with BAZ2A/TIP5 recovers DNA-binding activity.

**Summary**, from NCBI Gene [7270](https://www.ncbi.nlm.nih.gov/gene/7270):

> This gene encodes a transcription termination factor that is localized to the nucleolus and plays a critical role in ribosomal gene transcription. The encoded protein mediates the termination of RNA polymerase I transcription by binding to Sal box terminator elements downstream of pre-rRNA coding regions. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. This gene shares the symbol/alias 'TFF1' with another gene, NK2 homeobox 1, also known as …

**Accessions** — [HGNC:12397](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12397) · Entrez [7270](https://www.ncbi.nlm.nih.gov/gene/7270) · UniProt [Q15361](https://www.uniprot.org/uniprotkb/Q15361) · Ensembl [ENSG00000125482](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125482)

## Data

Gene col 4622: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4622); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4622, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4622]; `tensor/DDL_lfc|DDL_z.npy` [4622]; `embed/gene_vectors.npy` [4622]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4622 or target_col == 4622). Every well: [[TTF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
