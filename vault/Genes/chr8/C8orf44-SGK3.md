---
symbol: "C8orf44-SGK3"
type: "gene"
col: 16363
ensembl_id: "ENSG00000288602"
name: "C8orf44-SGK3 readthrough"
location: "8q13.1"
module: 15
arm: "+"
pooled_cpm: 23.47
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 16
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# C8orf44-SGK3

*C8orf44-SGK3 readthrough* — 8q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.40× (z +9.4, q 4e-18, up in 28 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.71× (z +6.0, q 2e-07, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (12 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.390× (z -10.0, q 6e-21, down in 40 of 47 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 0.478× (z -4.3, q 0.001, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSTO1]] (+0.76, fdr 7e-06), [[ZNF213-AS1]] (+0.73, fdr 7e-06), [[GPALPP1]] (+0.73, fdr 7e-06); moves opposite to [[THEM6]] (-0.57, fdr 2e-04), [[MRPL17]] (-0.57, fdr 1e-04), [[CYC1]] (-0.57, fdr 3e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16363.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.40×** | +9.4 | 4e-18 | 28/33 (C32, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.10×** | +8.3 | 4e-14 | 30/41 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +7.4 | 3e-11 | 31/38 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.71×** | +6.0 | 2e-07 | 35/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +6.0 | 2e-07 | 32/48 (PANC-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.30×** | +4.2 | 0.003 | 26/48 (NCI-H2347, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.44×** | +4.1 | 0.003 | 24/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.006 | 22/48 (A498, A-427, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.47×** | +3.8 | 0.008 | 15/48 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.87×** | +3.7 | 0.014 | 20/48 (HOP62, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.26×** | +3.6 | 0.014 | 23/48 (SW480, H4, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.016 | 22/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.059 | 18/48 (SHP-77, SW 900, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.35×** | +3.1 | 0.064 | 16/48 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.064 | 19/47 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.089 | 15/48 (SW480, LS 180, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.30×** | +2.9 | 0.095 | 14/47 (LoVo, Hs 766T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 12 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16363.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.390×** | -10.0 | 6e-21 | 40/47 (A498, A549, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.433×** | -9.3 | 5e-18 | 41/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.538×** | -6.9 | 1e-09 | 37/47 (HepG2/C3A, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.644×** | -6.9 | 1e-09 | 31/47 (A549, AsPC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.542×** | -6.8 | 2e-09 | 38/48 (PANC-1, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.555×** | -6.5 | 7e-09 | 37/48 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.582×** | -6.0 | 2e-07 | 33/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | **0.609×** | -5.3 | 1e-05 | 28/46 (HepG2/C3A, SNU-423, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.626×** | -5.2 | 2e-05 | 31/47 (NCI-H460, A549, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.478×** | -4.3 | 0.001 | 27/48 (NCI-H1792, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **0.693×** | -4.0 | 0.003 | 24/48 (SW480, COLO 205, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **0.744×** | -3.2 | 0.056 | 23/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.739×** | -3.1 | 0.074 | 21/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.754×** | -3.1 | 0.077 | 21/48 (SW480, SNU-423, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.588×** | -3.1 | 0.082 | 18/46 (NCI-H460, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.590×** | -3.0 | 0.083 | 15/46 (MIA PaCa-2, COLO 205, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.47 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16363. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 24.6 | 1 | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +10.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -13.0) ⚠ cell-cycle shift, explains ~45% of this change |
| [[HOP62 (line)]] | alt | 36.8 | 3 (3 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.60× (z +11.6) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.233× (z -9.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H460 (line)]] | wt | 17.3 | 1 (1 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.02× (z +10.4) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 0.5 µM 0.280× (z -9.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 30.6 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -14.4) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A549 (line)]] | wt | 19.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -15.9) ⚠ cell-cycle shift, explains ~86% of this change |
| [[COLO 205 (line)]] | alt | 42.1 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.14× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -12.3) ⚠ cell-cycle shift, explains ~86% of this change |
| [[HepG2_C3A (line)]] | wt | 26.8 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0790× (z -14.0) ⚠ toxic; cell-cycle shift, explains ~53% of this change |
| [[LOX-IMVI (line)]] | wt | 30.4 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.161× (z -11.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A498 (line)]] | wt | 25.8 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.146× (z -14.3) ⚠ cell-cycle shift, explains ~36% of this change |
| [[C32 (line)]] | wt | 30.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.07× (z +12.9) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 18.9 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.97× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -10.0) ⚠ cell-cycle shift, explains ~86% of this change |
| [[H4 (line)]] | wt | 21.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 8.23× (z +9.0) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.131× (z -9.1) ⚠ cell-cycle shift, explains ~45% of this change |
| [[HEC-1-A (line)]] | alt | 28.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.52× (z +12.3) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 42.9 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0612× (z -10.6) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 23.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.179× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~53% of this change |
| [[SW 900 (line)]] | alt | 27.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.71× (z +14.0) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 19.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -12.4) ⚠ cell-cycle shift, explains ~86% of this change |
| [[HS-578T (line)]] | alt | 31.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.21× (z +8.9) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 26.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -10.4) ⚠ cell-cycle shift, explains ~86% of this change |
| [[KATO III (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.225× (z -9.8) ⚠ cell-cycle shift, explains ~45% of this change |
| [[LS 180 (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.193× (z -9.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H1573 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.197× (z -9.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H23 (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.199× (z -9.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H2347 (line)]] | alt | 19.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.25× (z +9.2) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 27.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.262× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[RPMI-7951 (line)]] | alt | 33.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.38× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16363), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSTO1]] | +0.76 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[ZNF213-AS1]] | +0.73 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[GPALPP1]] | +0.73 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[VPS13B-DT]] | +0.69 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[CCNY-AS1]] | +0.68 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[SNHG22]] | +0.68 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[ZNF596]] | +0.68 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[AMY2B]] | +0.67 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[PEX6]] | +0.66 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[RAD51-AS1]] | +0.66 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[NPIPB2]] | +0.66 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[GTF3C2-AS2]] | +0.65 | +0.54 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THEM6]] | -0.57 | -0.30 / -0.55 | both halves | 2e-04 |  |
| [[MRPL17]] | -0.57 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[CYC1]] | -0.57 | -0.28 / -0.58 | both halves | 3e-04 |  |
| [[JPT1]] | -0.56 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[TXNDC17]] | -0.55 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[PUSL1]] | -0.55 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[GALE]] | -0.54 | -0.44 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers C8orf44-SGK3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.682). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-6.0, 23.7); signed map (30.9, -16.4). **Vector** length 107, 28.7% of its response variance represented; |z| ≥ 3 in 1,056 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.8 | +7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.6 | +3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +6.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.1 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +3.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.5 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +0.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.2 | -6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -2.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | -4.5 | -4.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -4.2 | -10.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -3.7 | -6.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.7 | -4.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.7 | -2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -3.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | C8orf44-SGK3 readthrough |
| Locus type | readthrough (other) |
| Location | 8q13.1 — chr8:66,667,596-66,860,472 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100533105](https://www.ncbi.nlm.nih.gov/gene/100533105):

> This locus represents naturally occurring read-through transcription between the neighboring putative uncharacterized protein C8orf44 (GeneID 56260) and serine/threonine-protein kinase Sgk3 (GeneID 23678) genes on chromosome 8. The read-through transcript produces a protein that shares sequence identity with the downstream gene product. [provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:48354](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48354) · Entrez [100533105](https://www.ncbi.nlm.nih.gov/gene/100533105) · Ensembl [ENSG00000288602](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000288602)

## Data

Gene col 16363: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16363); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16363, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16363]; `tensor/DDL_lfc|DDL_z.npy` [16363]; `embed/gene_vectors.npy` [16363]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16363 or target_col == 16363). Every well: [[C8orf44-SGK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C8orf44-SGK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
