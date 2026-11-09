---
symbol: "ZMYM1"
type: "gene"
col: 12332
ensembl_id: "ENSG00000197056"
name: "zinc finger MYM-type containing 1"
location: "1p34.3"
module: 22
arm: "+"
pooled_cpm: 44.49
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 15
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# ZMYM1

*zinc finger MYM-type containing 1* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.40× (z +6.6, q 3e-08, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.613× (z -13.7, q 7e-40, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP295]] (+0.66, fdr 7e-06), [[DEPDC1]] (+0.66, fdr 7e-06), [[CENPE]] (+0.66, fdr 7e-06); moves opposite to [[MED26]] (-0.52, fdr 1e-05), [[DNAJC4]] (-0.52, fdr 3e-05), [[SPAG4]] (-0.52, fdr 7e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12332.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +6.6 | 3e-08 | 30/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +6.0 | 6e-07 | 27/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.21×** | +5.5 | 9e-06 | 25/48 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.25×** | +4.5 | 9e-04 | 24/47 (AsPC-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.24×** | +4.3 | 0.001 | 22/48 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.24×** | +4.3 | 0.001 | 21/48 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +4.2 | 0.002 | 22/48 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.005 | 19/48 (LoVo, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.6 | 0.022 | 15/48 (SK-MEL-2, KATO III, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.2 | 0.076 | 13/48 (AsPC-1, HT-29, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.0 | 0.13 | 12/47 (NCI-H23, SW48, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12332.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.613×** | -13.7 | 7e-40 | 44/47 (H4, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.572×** | -10.6 | 6e-24 | 35/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.604×** | -9.6 | 1e-19 | 36/48 (A-427, RKO, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.444×** | -8.4 | 6e-15 | 35/48 (PANC-1, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.698×** | -6.4 | 2e-08 | 25/44 (C32, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.741×** | -5.9 | 3e-07 | 31/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.796×** | -4.5 | 6e-04 | 25/48 (NCI-H460, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.795×** | -4.4 | 9e-04 | 22/48 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.663×** | -4.3 | 0.001 | 18/48 (SK-MEL-2, A-427, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.811×** | -4.2 | 0.002 | 23/48 (MIA PaCa-2, SW48, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.758×** | -3.9 | 0.005 | 15/48 (PANC-1, J82, …) | all doses, flat | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.760×** | -3.9 | 0.005 | 17/48 (NCI-H2030, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.695×** | -3.8 | 0.008 | 14/33 (HEC-1-A, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.880× | -3.6 | 0.015 | 16/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.721×** | -3.4 | 0.027 | 18/48 (RPMI-7951, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Pimitespib (drug)]] 5 µM |  | **0.744×** | -3.1 | 0.071 | 12/46 (hTERT-HPNE, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12332. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 71.1 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +11.8) ⚠ cell-cycle shift, explains ~31% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.346× (z -14.1) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.267× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 39.4 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.344× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -11.1) |
| [[H4 (line)]] | wt | 31.7 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.212× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 67.8 | 0 | 3 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0731× (z -17.3) ⚠ toxic · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -10.0) |
| [[HOP62 (line)]] | alt | 51.5 | 0 | 3 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.426× (z -13.3) |
| [[LS 180 (line)]] | wt | 34.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.311× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 77.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -23.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[RKO (line)]] | wt | 45.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.08× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -13.0) |
| [[SNU-1 (line)]] | wt | 58.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -10.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 63.2 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -15.9) |
| [[HCT15 (line)]] | alt | 64.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[J82 (line)]] | alt | 47.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -10.4) |
| [[LoVo (line)]] | wt | 32.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 87.8 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -13.3) ⚠ cell-cycle shift, explains ~22% of this change |
| [[SW480 (line)]] | alt | 42.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.435× (z -9.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 30.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -12.9) ⚠ cell-cycle shift, explains ~22% of this change |
| [[A498 (line)]] | wt | 39.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.353× (z -9.4) ⚠ toxic |
| [[A549 (line)]] | wt | 39.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -10.7) |
| [[BT-474 (line)]] | alt | 43.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.316× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 79.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[C32 (line)]] | wt | 21.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.157× (z -10.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 34.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.248× (z -8.6) ⚠ toxic |
| [[KATO III (line)]] | alt | 41.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 42.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 31.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -16.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H2030 (line)]] | alt | 39.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +12.4) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2347 (line)]] | alt | 31.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 33.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 49.4 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.119× (z -10.3) |
| [[SW 1271 (line)]] | alt | 55.8 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0708× (z -10.1) |
| [[SW48 (line)]] | wt | 43.6 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -11.6) ⚠ cell-cycle shift, explains ~22% of this change |
| [[AN3 CA (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12332), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP295]] | +0.66 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[DEPDC1]] | +0.66 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[CENPE]] | +0.66 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[HYLS1]] | +0.65 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[CKAP2]] | +0.61 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[CENPF]] | +0.61 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[KLHL9]] | +0.61 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[HUS1]] | +0.60 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[MSL3P1]] | +0.60 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[ARHGAP11A]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[THAP5]] | +0.60 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[MDC1]] | +0.59 | +0.54 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED26]] | -0.52 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[DNAJC4]] | -0.52 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[SPAG4]] | -0.52 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[KDELR1]] | -0.52 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[CD27-AS1]] | -0.52 | -0.23 / -0.57 | both halves | 5e-04 |  |
| [[CCNO-DT]] | -0.51 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[CSNK1G2]] | -0.51 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[UBOX5-AS1]] | -0.50 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[VSIG10L]] | -0.50 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[PBXIP1]] | -0.49 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[OXR1-AS1]] | -0.49 | -0.22 / -0.51 | both halves | 6e-04 |  |
| [[CATSPER2P1-1]] | -0.49 | -0.35 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ZMYM1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | ZMYM1's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | ZMYM1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.56 | 0.529 over the table, 0.099 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.502). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.3, -57.6); signed map (-52.2, -45.1). **Vector** length 104, 24.9% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.5 | +6.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.4 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +5.9 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.6 | +4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +4.0 | +5.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.0 | +2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.6 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +2.0 | +1.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.6 | -13.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -9.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -6.9 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -3.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.4 | -10.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -3.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -3.4 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -2.2 | -0.9 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -2.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger MYM-type containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:35,032,172-35,115,859 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23151, MYM |
| Gene groups (HGNC) | Zinc fingers MYM-type |
| Matched by | ensembl_id |

UniProt [Q5SVZ6](https://www.uniprot.org/uniprotkb/Q5SVZ6) carries no function annotation.

**Summary**, from NCBI Gene [79830](https://www.ncbi.nlm.nih.gov/gene/79830):

> Predicted to enable protein dimerization activity and zinc ion binding activity. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26253](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26253) · Entrez [79830](https://www.ncbi.nlm.nih.gov/gene/79830) · UniProt [Q5SVZ6](https://www.uniprot.org/uniprotkb/Q5SVZ6) · Ensembl [ENSG00000197056](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197056)

## Data

Gene col 12332: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12332); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12332, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12332]; `tensor/DDL_lfc|DDL_z.npy` [12332]; `embed/gene_vectors.npy` [12332]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12332 or target_col == 12332). Every well: [[ZMYM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZMYM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
