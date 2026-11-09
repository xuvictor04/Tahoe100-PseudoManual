---
symbol: "NLRC5"
type: "gene"
col: 6456
ensembl_id: "ENSG00000140853"
name: "NLR family CARD domain containing 5"
location: "16q13"
module: 32
arm: "+"
pooled_cpm: 35.1
n_lines_expressing: 45
n_dd_up: 30
n_dd_down: 48
n_dd_up_clean: 28
n_dd_down_clean: 36
in_vector_space: true
direction_upstream: 55
direction_downstream: 40
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# NLRC5

*NLR family CARD domain containing 5* — 16q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (2 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.79× (z +7.4, q 1e-10, up in 32 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 48 drug-doses (12 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.532× (z -11.7, q 6e-29, down in 31 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PARP12]] (+0.81, fdr 7e-06), [[SLC15A3]] (+0.81, fdr 7e-06), [[OAS1]] (+0.81, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 55 arrows point to it, the strongest [[GBP1]] → it (grade B ⚠); 40 go from it, the strongest it → [[SP100]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6456.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.79×** | +7.4 | 1e-10 | 32/41 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.61×** | +6.5 | 3e-08 | 28/43 (NCI-H460, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.38×** | +5.8 | 9e-07 | 29/43 (AsPC-1, NCI-H460, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.55×** | +5.7 | 2e-06 | 28/43 (NCI-H460, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.56×** | +5.6 | 2e-06 | 26/41 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +5.6 | 2e-06 | 23/42 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.52×** | +5.5 | 2e-06 | 29/43 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.38×** | +5.4 | 5e-06 | 24/43 (NCI-H460, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.39×** | +5.4 | 5e-06 | 26/43 (NCI-H460, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +5.3 | 6e-06 | 21/43 (HT-29, Hs 766T, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.49×** | +5.3 | 7e-06 | 24/42 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.48×** | +5.1 | 1e-05 | 23/43 (HT-29, SW1417, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +5.1 | 2e-05 | 20/42 (SW480, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.31×** | +4.9 | 3e-05 | 24/43 (AsPC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.38×** | +4.2 | 8e-04 | 19/43 (HS-578T, RPMI-7951, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.40×** | +4.2 | 1e-03 | 18/43 (AsPC-1, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 48 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6456.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.532×** | -11.7 | 6e-29 | 31/43 (LoVo, A549, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.533×** | -11.7 | 6e-29 | 34/43 (SW1417, HS-578T, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.438×** | -10.4 | 4e-23 | 22/31 (Panc 03.27, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.466×** | -10.0 | 2e-21 | 28/39 (LoVo, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.515×** | -8.7 | 4e-16 | 32/42 (LoVo, A498, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.537×** | -8.2 | 3e-14 | 29/42 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.650×** | -8.0 | 1e-13 | 31/43 (LoVo, A549, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.556×** | -7.7 | 1e-12 | 33/43 (LoVo, A549, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.591×** | -6.6 | 2e-09 | 21/39 (LoVo, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.602×** | -6.3 | 2e-08 | 24/42 (SNU-423, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.637×** | -5.9 | 2e-07 | 21/43 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.743×** | -5.5 | 2e-06 | 25/43 (A549, LoVo, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.451×** | -5.5 | 2e-06 | 26/41 (LoVo, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.674×** | -5.2 | 1e-05 | 20/43 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.681×** | -5.0 | 2e-05 | 22/41 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.688×** | -4.9 | 4e-05 | 19/42 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.495×** | -4.8 | 5e-05 | 24/42 (LoVo, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.698×** | -4.7 | 8e-05 | 20/43 (NCI-H2347, HS-578T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6456. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 123 | 0 | 17 (8 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.102× (z -18.3) ⚠ toxic · without an alert: [[Tofacitinib (drug)]] 5 µM 0.246× (z -16.6) |
| [[A549 (line)]] | wt | 57.3 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0714× (z -18.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.164× (z -12.4) |
| [[A498 (line)]] | wt | 43.9 | 0 | 9 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.179× (z -12.7) ⚠ toxic · without an alert: [[Tofacitinib (drug)]] 5 µM 0.356× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 30.5 | 0 | 9 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0640× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.0996× (z -10.2) |
| [[A-172 (line)]] | wt | 52.0 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -9.7) |
| [[HS-578T (line)]] | alt | 67.3 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -13.7) |
| [[NCI-H460 (line)]] | wt | 35.1 | 1 | 4 (4 ⚠) | [[Auranofin (drug)]] 5 µM 7.10× (z +15.9) | [[Digitoxin (drug)]] 5 µM 0.245× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 108 | 1 (1 ⚠) | 3 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.31× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.0941× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.250× (z -11.2) |
| [[SNU-423 (line)]] | alt | 74.3 | 0 | 4 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -10.5) |
| [[SW1417 (line)]] | alt | 82.6 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -15.3) |
| [[Panc 03.27 (line)]] | alt | 46.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0819× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -12.0) |
| [[HT-29 (line)]] | alt | 21.9 | 2 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 5.98× (z +10.0) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 3.28× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 50.2 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.93× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 30.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H2347 (line)]] | alt | 34.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.23× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[RKO (line)]] | wt | 31.2 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0518× (z -14.9) |
| [[SNU-1 (line)]] | wt | 32.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 13.5 | 0 | 1 | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.0805× (z -8.5) |
| [[H4 (line)]] | wt | 16.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.7× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 38.4 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.112× (z -9.4) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 56.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -13.0) |
| [[hTERT-HPNE (line)]] | wt | 16.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 11.0× (z +10.0) | — |
| [[NCI-H2030 (line)]] | alt | 15.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.20× (z +15.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 57.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -8.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 20.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0800× (z -12.9) ⚠ toxic |
| [[SW 900 (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW480 (line)]] | alt | 11.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.14× (z +12.5) | — |
| [[A-427 (line)]] | wt | 5.84 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.07 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.19 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.14 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6456), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARP12]] | +0.81 | +0.72 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[SLC15A3]] | +0.81 | +0.75 / +0.81 | both halves | 7e-06 |  |
| [[OAS1]] | +0.81 | +0.77 / +0.81 | both halves | 7e-06 | STRING 405 |
| [[IFI35]] | +0.80 | +0.74 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 419 |
| [[PARP9]] | +0.80 | +0.76 / +0.80 | both halves | 7e-06 | STRING 546 |
| [[EIF2AK2]] | +0.79 | +0.73 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[RSAD2]] | +0.79 | +0.74 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 412 |
| [[SAMD9L]] | +0.78 | +0.74 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[MX1]] | +0.77 | +0.69 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 455 |
| [[XAF1]] | +0.77 | +0.67 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[MX2]] | +0.77 | +0.68 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[DDX60L]] | +0.77 | +0.74 / +0.78 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*55 arrows, 55 of them with an alert ⚠; grade A 0, B 43, C 12. Shown: the 12 strongest; 43 more arrows (43 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP1]] | B | GBP1 activity raises NLRC5's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.33× lower at baseline in the lines without GBP1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[OAS1]] | B | OAS1 activity raises NLRC5's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.53× lower at baseline in the lines without OAS1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[SAMD9L]] | B | SAMD9L activity raises NLRC5's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 2.23× lower at baseline in the lines without SAMD9L | 6e-04 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[TRIM22]] | B | TRIM22 activity raises NLRC5's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 2.51× lower at baseline in the lines without TRIM22 | 6e-04 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[RSAD2]] | B | RSAD2 activity raises NLRC5's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.59× lower at baseline in the lines without RSAD2 | 8e-04 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[GBP4]] | B | GBP4 activity raises NLRC5's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.00× lower at baseline in the lines without GBP4 | 1e-03 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[OAS2]] | B | OAS2 activity raises NLRC5's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.21× lower at baseline in the lines without OAS2 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[CD5L]] | B | CD5L activity raises NLRC5's level | lines that do not express CD5L (23) vs lines expressing it (27) | 2.12× lower at baseline in the lines without CD5L | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[NRIR]] | B | NRIR activity raises NLRC5's level | lines that do not express NRIR (14) vs lines expressing it (36) | 2.09× lower at baseline in the lines without NRIR | 0.002 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[HERC6]] | B | HERC6 activity raises NLRC5's level | lines that do not express HERC6 (5) vs lines expressing it (45) | 3.20× lower at baseline in the lines without HERC6 | 0.003 | ⚠ within organs, on part of the lines; also absent: IFIH1, IFI35, PARP9; maybe low, not absent |
| [[CMPK2]] | B | CMPK2 activity raises NLRC5's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.32× lower at baseline in the lines without CMPK2 | 0.003 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[IFI44]] | B | IFI44 activity raises NLRC5's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.19× lower at baseline in the lines without IFI44 | 0.003 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |

### Downstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 37, C 3. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SP100]] | B | NLRC5 activity raises SP100's level | lines that do not express NLRC5 (5) vs lines expressing it (45) | 3.53× lower at baseline in the lines without NLRC5 | 0.003 | ⚠ within organs, on part of the lines; also absent: NDRG1, APOL6, S100A13; maybe low, not absent |
| [[IFI44]] | B | NLRC5 activity raises IFI44's level | lines that do not express NLRC5 (5) vs lines expressing it (45) | 4.62× lower at baseline in the lines without NLRC5 | 0.004 | ⚠ within organs, on part of the lines; also absent: NDRG1, APOL6, S100A13; maybe low, not absent |
| [[SAMD9]] | B | NLRC5 activity raises SAMD9's level | lines that do not express NLRC5 (5) vs lines expressing it (45) | 4.80× lower at baseline in the lines without NLRC5 | 0.004 | ⚠ within organs, on part of the lines; also absent: NDRG1, APOL6, S100A13; maybe low, not absent |
| [[GBP2]] | B | NLRC5 activity raises GBP2's level | lines that do not express NLRC5 (5) vs lines expressing it (45) | 5.17× lower at baseline in the lines without NLRC5 | 0.006 | ⚠ within organs, on part of the lines; also absent: NDRG1, APOL6, S100A13; maybe low, not absent |
| [[RSAD2]] | B | NLRC5 activity raises RSAD2's level | lines that do not express NLRC5 (5) vs lines expressing it (45) | 5.56× lower at baseline in the lines without NLRC5 | 0.007 | ⚠ within organs, on part of the lines; also absent: NDRG1, APOL6, S100A13; maybe low, not absent |
| [[SAMD9L]] | B | NLRC5 activity raises SAMD9L's level | lines that do not express NLRC5 (5) vs lines expressing it (45) | 5.19× lower at baseline in the lines without NLRC5 | 0.007 | ⚠ within organs, on part of the lines; also absent: NDRG1, APOL6, S100A13; maybe low, not absent |
| [[TRIM38]] | B | NLRC5 activity raises TRIM38's level | lines that do not express NLRC5 (5) vs lines expressing it (45) | 4.22× lower at baseline in the lines without NLRC5 | 0.008 | ⚠ within organs, on part of the lines; also absent: NDRG1, APOL6, S100A13; maybe low, not absent |
| [[GBP1]] | B | NLRC5 activity raises GBP1's level | lines that do not express NLRC5 (5) vs lines expressing it (45) | 4.65× lower at baseline in the lines without NLRC5 | 0.014 | ⚠ within organs, on part of the lines; also absent: NDRG1, APOL6, S100A13; maybe low, not absent |
| [[DDX60]] | B | NLRC5 activity raises DDX60's level | lines that do not express NLRC5 (5) vs lines expressing it (45) | 2.59× lower at baseline in the lines without NLRC5 | 0.014 | ⚠ within organs, on part of the lines; also absent: NDRG1, APOL6, S100A13; maybe low, not absent |
| [[IFIT3]] | B | NLRC5 activity raises IFIT3's level | lines that do not express NLRC5 (5) vs lines expressing it (45) | 3.78× lower at baseline in the lines without NLRC5 | 0.014 | ⚠ within organs, on part of the lines; also absent: NDRG1, APOL6, S100A13; maybe low, not absent |
| [[ISG20]] | B | NLRC5 activity raises ISG20's level | lines that do not express NLRC5 (5) vs lines expressing it (45) | 2.00× lower at baseline in the lines without NLRC5 | 0.015 | ⚠ within organs, on part of the lines; also absent: NDRG1, APOL6, S100A13; maybe low, not absent |
| [[HERC6]] | B | NLRC5 activity raises HERC6's level | lines that do not express NLRC5 (5) vs lines expressing it (45) | 2.98× lower at baseline in the lines without NLRC5 | 0.016 | ⚠ within organs, on part of the lines; also absent: NDRG1, APOL6, S100A13; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.809). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.8, 54.8); signed map (64.2, 32.8). **Vector** length 139, 44.7% of its response variance represented; |z| ≥ 3 in 1,437 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.67 to 56); *interferon* (control, mean cos +0.73 to 23); *Interferon Signaling* (reactome, mean cos +0.69 to 45).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.0 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.9 | +7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.9 | +5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.6 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +1.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.1 | +5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.9 | +5.6 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -7.7 | -11.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -7.0 | -8.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -7.0 | -7.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -6.6 | -8.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -6.3 | -8.7 |

## What is on record

|  |  |
|---|---|
| Name | NLR family CARD domain containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q13 — chr16:56,989,485-57,083,531 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NOD27, CLR16.1, FLJ21709 |
| Gene groups (HGNC) | NLR family |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Reactome | 25 pathways, smallest: Regulation of NF-kappa B signaling; Negative regulators of DDX58/IFIH1 signaling; TAK1-dependent IKK and NF-kappa-B activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86WI3](https://www.uniprot.org/uniprotkb/Q86WI3) (Protein NLRC5):

> Probable regulator of the NF-kappa-B and type I interferon signaling pathways. May also regulate the type II interferon signaling pathway. Plays a role in homeostatic control of innate immunity and in antiviral defense mechanisms.

**Summary**, from NCBI Gene [84166](https://www.ncbi.nlm.nih.gov/gene/84166):

> This gene encodes a member of the caspase recruitment domain-containing NLR family. This gene plays a role in cytokine response and antiviral immunity through its inhibition of NF-kappa-B activation and negative regulation of type I interferon signaling pathways. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:29933](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29933) · Entrez [84166](https://www.ncbi.nlm.nih.gov/gene/84166) · UniProt [Q86WI3](https://www.uniprot.org/uniprotkb/Q86WI3) · Ensembl [ENSG00000140853](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140853)

## Data

Gene col 6456: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6456); `tables/drug_effects.parquet` (83 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6456, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6456]; `tensor/DDL_lfc|DDL_z.npy` [6456]; `embed/gene_vectors.npy` [6456]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6456 or target_col == 6456). Every well: [[NLRC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NLRC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
