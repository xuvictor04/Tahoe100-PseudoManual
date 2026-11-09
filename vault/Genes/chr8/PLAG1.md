---
symbol: "PLAG1"
type: "gene"
col: 11206
ensembl_id: "ENSG00000181690"
name: "PLAG1 zinc finger"
location: "8q12.1"
module: 1
arm: "-"
pooled_cpm: 55.64
n_lines_expressing: 41
n_dd_up: 10
n_dd_down: 36
n_dd_up_clean: 10
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 2
direction_downstream: 10
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PLAG1

*PLAG1 zinc finger* — 8q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.29× (z +15.0, q 0e+00, up in 31 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.302× (z -21.6, q 0e+00, down in 29 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.549× (z -10.8, q 3e-25, down in 32 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MINDY2]] (+0.73, fdr 7e-06), [[ARID4A]] (+0.73, fdr 7e-06), [[UBXN7]] (+0.71, fdr 7e-06); moves opposite to [[CCT5]] (-0.67, fdr 7e-06), [[CLPB]] (-0.64, fdr 7e-06), [[ZNF195]] (-0.64, fdr 1e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC12A8]] → it (grade B ⚠); 10 go from it, the strongest it → [[AAMDC]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11206.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.29×** | +15.0 | 0e+00 | 31/39 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.90×** | +11.6 | 1e-28 | 29/39 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.80×** | +10.7 | 3e-24 | 26/39 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +7.3 | 6e-11 | 19/40 (SW1417, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +6.8 | 1e-09 | 20/39 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.29×** | +4.6 | 4e-04 | 13/40 (MIA PaCa-2, RKO, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +4.1 | 0.003 | 16/40 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.9 | 0.006 | 14/39 (KATO III, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.008 | 17/39 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.044 | 9/38 (RKO, LoVo, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.086 | 15/37 (AsPC-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.19× | +3.1 | 0.098 | 8/39 (A-427, HepG2/C3A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11206.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.302×** | -21.6 | 0e+00 | 29/36 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.382×** | -16.7 | 0e+00 | 24/28 (AsPC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.416×** | -15.8 | 0e+00 | 37/39 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.459×** | -13.0 | 1e-36 | 27/33 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.549×** | -10.8 | 3e-25 | 32/39 (Hs 766T, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.595×** | -9.4 | 7e-19 | 30/39 (SW480, AsPC-1, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.372×** | -9.3 | 8e-19 | 35/38 (AsPC-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.603×** | -9.1 | 5e-18 | 35/39 (HOP62, AsPC-1, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.386×** | -9.0 | 1e-17 | 33/38 (AsPC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.616×** | -8.7 | 1e-16 | 27/39 (AsPC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.441×** | -7.7 | 6e-13 | 32/38 (AsPC-1, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.450×** | -7.6 | 2e-12 | 28/39 (AsPC-1, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.672×** | -6.8 | 6e-10 | 31/39 (AsPC-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.499×** | -6.6 | 2e-09 | 26/36 (AsPC-1, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.702×** | -6.4 | 6e-09 | 23/39 (AsPC-1, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.741×** | -5.4 | 2e-06 | 24/39 (AsPC-1, NCI-H23, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.744×** | -5.3 | 3e-06 | 25/39 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.812×** | -5.3 | 3e-06 | 20/39 (NCI-H2347, AsPC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.765×** | -4.8 | 4e-05 | 16/39 (SW480, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11206. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 143 | 0 | 18 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -21.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -17.8) |
| [[HOP62 (line)]] | alt | 117 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -16.6) |
| [[CFPAC-1 (line)]] | alt | 97.8 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.316× (z -13.3) |
| [[HS-578T (line)]] | alt | 87.7 | 1 | 9 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.51× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -14.4) ⚠ cell-cycle shift, explains ~88% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.301× (z -12.0) |
| [[RKO (line)]] | wt | 111 | 6 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +13.9) ⚠ cell-cycle shift, explains ~88% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.82× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.153× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 92.7 | 0 | 8 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.142× (z -21.2) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.313× (z -12.6) |
| [[SW480 (line)]] | alt | 96.2 | 1 | 6 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.408× (z -10.8) |
| [[HT-29 (line)]] | alt | 99.4 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.394× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 67.1 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.247× (z -8.6) |
| [[PANC-1 (line)]] | alt | 27.3 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.23× (z +13.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.302× (z -11.4) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.371× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 131 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.342× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 76.9 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -14.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 67.0 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.217× (z -13.0) |
| [[LoVo (line)]] | wt | 22.0 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.00× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -8.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 137 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.447× (z -8.7) |
| [[SNU-423 (line)]] | alt | 90.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.110× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.366× (z -10.1) |
| [[SW 900 (line)]] | alt | 133 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -17.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 49.6 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +11.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.276× (z -10.9) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 17.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.90× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 134 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -19.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 19.7 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 4.30× (z +10.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -11.5) |
| [[NCI-H23 (line)]] | alt | 28.5 | 1 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 4.03× (z +9.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.209× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~47% of this change |
| [[Panc 03.27 (line)]] | alt | 101 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -20.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 55.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -13.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 72.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -11.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 65.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -13.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 22.4 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.53× (z +9.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.205× (z -9.9) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 20.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.57× (z +8.6) | — |
| [[KATO III (line)]] | alt | 39.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -9.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 74.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -10.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 68.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -13.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 6.48 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.43 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 84.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.30 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.96 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11206), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MINDY2]] | +0.73 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[ARID4A]] | +0.73 | +0.58 / +0.74 | both halves | 7e-06 |  |
| [[UBXN7]] | +0.71 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[AAMDC]] | +0.67 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[ARL3]] | +0.66 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[NDUFA2]] | +0.66 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ALDH6A1]] | +0.65 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[GABARAP]] ⚠ | +0.65 | +0.58 / +0.61 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[FBXL20]] | +0.64 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[PAIP2B]] | +0.64 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[YPEL3]] | +0.64 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[ZNF654]] | +0.64 | +0.67 / +0.64 | both halves | 7e-06 | same gene group |
| [[KBTBD3]] | +0.64 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT5]] | -0.67 | -0.68 / -0.60 | both halves | 7e-06 |  |
| [[CLPB]] | -0.64 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[ZNF195]] | -0.64 | -0.65 / -0.52 | both halves | 1e-05 | same gene group |
| [[NAA15]] | -0.63 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[PTPN11]] | -0.62 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[DHX37]] | -0.62 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[CCT7]] | -0.61 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[GTPBP4]] | -0.61 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[POGK]] | -0.61 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[PSMD1]] | -0.61 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[DNAJC11]] | -0.60 | -0.66 / -0.46 | both halves | 2e-05 |  |
| [[UTP20]] | -0.60 | -0.59 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC12A8]] | B | SLC12A8 activity raises PLAG1's level | lines that do not express SLC12A8 (17) vs lines expressing it (33) | 1.20× lower at baseline in the lines without SLC12A8 | 0.076 | ⚠ within organs, on part of the lines; also absent: ANK3, LYPD6B, SAMD12-AS1; maybe low, not absent |
| [[PRKAR1B]] | B | PRKAR1B activity lowers PLAG1's level | lines that do not express PRKAR1B (6) vs lines expressing it (44) | 3.28× higher at baseline in the lines without PRKAR1B | 0.098 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AAMDC]] | B | PLAG1 activity raises AAMDC's level | lines that do not express PLAG1 (9) vs lines expressing it (41) | 1.38× lower at baseline in the lines without PLAG1 | 0.058 | ⚠ within organs, on part of the lines; also absent: FCGRT; maybe low, not absent |
| [[CCT3]] | B | PLAG1 activity lowers CCT3's level | lines that do not express PLAG1 (9) vs lines expressing it (41) | 1.43× higher at baseline in the lines without PLAG1 | 0.065 | ⚠ within organs, on part of the lines; also absent: FCGRT; maybe low, not absent |
| [[MPC2]] | B | PLAG1 activity lowers MPC2's level | lines that do not express PLAG1 (9) vs lines expressing it (41) | 1.48× higher at baseline in the lines without PLAG1 | 0.068 | ⚠ within organs, on part of the lines; also absent: FCGRT; maybe low, not absent |
| [[HERC2P9-1]] | B | PLAG1 activity lowers HERC2P9-1's level | lines that do not express PLAG1 (9) vs lines expressing it (41) | 1.21× higher at baseline in the lines without PLAG1 | 0.074 | ⚠ within organs, on part of the lines; also absent: FCGRT; maybe low, not absent |
| [[KIAA1549]] | B | PLAG1 activity lowers KIAA1549's level | lines that do not express PLAG1 (9) vs lines expressing it (41) | 1.46× higher at baseline in the lines without PLAG1 | 0.074 | ⚠ within organs, on part of the lines; also absent: FCGRT; maybe low, not absent |
| [[OXR1]] | B | PLAG1 activity raises OXR1's level | lines that do not express PLAG1 (9) vs lines expressing it (41) | 1.76× lower at baseline in the lines without PLAG1 | 0.079 | ⚠ within organs, on part of the lines; also absent: FCGRT; maybe low, not absent |
| [[MVB12B]] | B | PLAG1 activity lowers MVB12B's level | lines that do not express PLAG1 (9) vs lines expressing it (41) | 1.91× higher at baseline in the lines without PLAG1 | 0.086 | ⚠ within organs, on part of the lines; also absent: FCGRT; maybe low, not absent |
| [[KBTBD3]] | B | PLAG1 activity raises KBTBD3's level | lines that do not express PLAG1 (9) vs lines expressing it (41) | 1.50× lower at baseline in the lines without PLAG1 | 0.086 | ⚠ within organs, on part of the lines; also absent: FCGRT; maybe low, not absent |
| [[TCERG1]] | B | PLAG1 activity lowers TCERG1's level | lines that do not express PLAG1 (9) vs lines expressing it (41) | 1.22× higher at baseline in the lines without PLAG1 | 0.091 | ⚠ within organs, on part of the lines; also absent: FCGRT; maybe low, not absent |
| [[AP3S1]] | B | PLAG1 activity raises AP3S1's level | lines that do not express PLAG1 (9) vs lines expressing it (41) | 1.38× lower at baseline in the lines without PLAG1 | 0.097 | ⚠ within organs, on part of the lines; also absent: FCGRT; maybe low, not absent |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.576). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-3.0, -43.6); signed map (-13.0, 8.5). **Vector** length 116, 32.9% of its response variance represented; |z| ≥ 3 in 1,226 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.6 | +10.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.0 | +11.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.8 | +15.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.3 | +1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +2.8 | +3.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.4 | +4.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.2 | +2.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.1 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.0 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.4 | -15.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -7.9 | -10.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.5 | -6.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.2 | -9.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.8 | -9.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.8 | -9.3 |
|  | [[EX229 (drug)]] 5 µM |  | -5.7 | -7.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.9 | -6.6 |

## What is on record

|  |  |
|---|---|
| Name | PLAG1 zinc finger |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q12.1 — chr8:56,160,909-56,211,324 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF912 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Hallmark sets | KRAS_SIGNALING_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6DJT9](https://www.uniprot.org/uniprotkb/Q6DJT9) (Zinc finger protein PLAG1):

> Transcription factor whose activation results in up-regulation of target genes, such as IGFII, leading to uncontrolled cell proliferation: when overexpressed in cultured cells, higher proliferation rate and transformation are observed. Other target genes such as CRLF1, CRABP2, CRIP2, PIGF are strongly induced in cells with PLAG1 induction. Proto-oncogene whose ectopic expression can trigger the development of pleomorphic adenomas of the salivary gland and lipoblastomas. Overexpression is …

**Summary**, from NCBI Gene [5324](https://www.ncbi.nlm.nih.gov/gene/5324):

> Pleomorphic adenoma gene 1 encodes a zinc finger protein with 2 putative nuclear localization signals. PLAG1, which is developmentally regulated, has been shown to be consistently rearranged in pleomorphic adenomas of the salivary glands. PLAG1 is activated by the reciprocal chromosomal translocations involving 8q12 in a subset of salivary gland pleomorphic adenomas. Three transcript variants encoding two different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9045](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9045) · Entrez [5324](https://www.ncbi.nlm.nih.gov/gene/5324) · UniProt [Q6DJT9](https://www.uniprot.org/uniprotkb/Q6DJT9) · Ensembl [ENSG00000181690](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181690)

## Data

Gene col 11206: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11206); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11206, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11206]; `tensor/DDL_lfc|DDL_z.npy` [11206]; `embed/gene_vectors.npy` [11206]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11206 or target_col == 11206). Every well: [[PLAG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLAG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
