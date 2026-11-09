---
symbol: "CAPN1"
type: "gene"
col: 286
ensembl_id: "ENSG00000014216"
name: "calpain 1"
location: "11q13.1"
module: 2
arm: "+"
pooled_cpm: 42.06
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 22
n_dd_up_clean: 2
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CAPN1

*calpain 1* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.92× (z +12.8, q 1e-34, up in 35 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.26× (z +4.5, q 9e-04, up in 20 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 7 lines (KATO III 4.57×, LoVo 3.13×, A498 3.42×, PANC-1 2.99×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A498 3.34×, J82 3.05×, PANC-1 2.67×, A-427 2.73×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2030 3.20×, A-172 2.93×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.263× (z -37.1, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAN2B2]] (+0.70, fdr 7e-06), [[LLGL1]] (+0.68, fdr 7e-06), [[NRBP2]] (+0.67, fdr 1e-05); moves opposite to [[PIGBOS1]] (-0.61, fdr 1e-05), [[CEBPZ]] (-0.59, fdr 1e-05), [[TOPORS]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[EPS8L2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 286.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 7 lines (KATO III 4.57×, LoVo 3.13×, A498 3.42×, PANC-1 2.99×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A498 3.34×, J82 3.05×, PANC-1 2.67×, A-427 2.73×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2030 3.20×, A-172 2.93×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.92×** | +12.8 | 1e-34 | 35/42 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +12.3 | 3e-32 | 29/36 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +8.6 | 1e-15 | 27/38 (NCI-H2030, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +4.5 | 9e-04 | 20/47 (NCI-H2030, HOP62, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.25×** | +4.2 | 0.003 | 17/47 (HOP62, H4, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.23×** | +4.0 | 0.006 | 14/48 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.15× | +3.9 | 0.009 | 14/48 (HT-29, RKO, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.19× | +3.2 | 0.11 | 13/48 (SW480, AsPC-1, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.17× | +3.1 | 0.13 | 5/48 (A-427, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 286.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.263×** | -37.1 | 0e+00 | 43/47 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.282×** | -24.9 | 0e+00 | 43/46 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.370×** | -18.8 | 0e+00 | 46/48 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.467×** | -15.0 | 0e+00 | 41/48 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.485×** | -14.2 | 1e-43 | 42/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.504×** | -13.4 | 4e-39 | 40/48 (HEC-1-A, SNU-423, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.649×** | -12.0 | 3e-31 | 31/46 (HEC-1-A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.617×** | -9.5 | 2e-19 | 36/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.644×** | -8.6 | 4e-16 | 35/48 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.666×** | -8.0 | 1e-13 | 32/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.759×** | -7.7 | 1e-12 | 28/48 (NCI-H2347, SW480, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.685×** | -7.4 | 6e-12 | 30/46 (BT-474, NCI-H460, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.575×** | -5.7 | 6e-07 | 26/48 (HEC-1-A, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.751×** | -5.6 | 8e-07 | 26/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.780×** | -4.7 | 1e-04 | 22/45 (NCI-H1573, HEC-1-A, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.788×** | -4.7 | 1e-04 | 23/48 (H4, NCI-H2347, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.817×** | -4.0 | 0.002 | 17/47 (HEC-1-A, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.873× | -3.8 | 0.005 | 18/48 (CFPAC-1, HEC-1-A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 286. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 42.4 | 1 (1 ⚠) | 9 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.10× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -26.2) |
| [[HEC-1-A (line)]] | alt | 110 | 0 | 8 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -15.8) |
| [[NCI-H1573 (line)]] | alt | 22.6 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -15.5) |
| [[AsPC-1 (line)]] | alt | 61.3 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -28.8) |
| [[BT-474 (line)]] | alt | 62.7 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -23.8) |
| [[HT-29 (line)]] | alt | 50.1 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -21.5) |
| [[LoVo (line)]] | wt | 36.2 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 3.13× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -18.7) |
| [[NCI-H2347 (line)]] | alt | 112 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -27.9) |
| [[SW1417 (line)]] | alt | 103 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -21.4) |
| [[CFPAC-1 (line)]] | alt | 64.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -25.5) |
| [[HOP62 (line)]] | alt | 40.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -26.7) |
| [[HS-578T (line)]] | alt | 27.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -14.2) |
| [[MIA PaCa-2 (line)]] | alt | 37.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -21.0) |
| [[NCI-H2030 (line)]] | alt | 25.0 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.20× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -25.9) |
| [[NCI-H460 (line)]] | wt | 19.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -22.0) |
| [[PANC-1 (line)]] | alt | 27.5 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -18.8) |
| [[SNU-423 (line)]] | alt | 32.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -25.0) |
| [[A-172 (line)]] | wt | 36.5 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 2.93× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -15.6) |
| [[A549 (line)]] | wt | 32.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -19.4) |
| [[Hs 766T (line)]] | wt | 61.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -25.4) |
| [[J82 (line)]] | alt | 33.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -16.6) |
| [[KATO III (line)]] | alt | 48.5 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.57× (z +14.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -19.6) |
| [[LS 180 (line)]] | wt | 64.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -23.7) |
| [[LOX-IMVI (line)]] | wt | 26.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -14.5) |
| [[A498 (line)]] | wt | 21.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +11.1) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 21.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -12.4) |
| [[COLO 205 (line)]] | alt | 39.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -13.6) |
| [[H4 (line)]] | wt | 29.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0870× (z -18.7) |
| [[HCT15 (line)]] | alt | 52.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -17.6) |
| [[hTERT-HPNE (line)]] | wt | 27.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -13.5) |
| [[Panc 03.27 (line)]] | alt | 88.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -16.2) |
| [[RPMI-7951 (line)]] | alt | 24.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -14.9) |
| [[SW 900 (line)]] | alt | 26.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -14.7) |
| [[A-427 (line)]] | wt | 43.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +9.1) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 17.0 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.05 µM 0.0733× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 22.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -12.0) |
| [[NCI-H23 (line)]] | alt | 18.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.242× (z -8.8) |
| [[RKO (line)]] | wt | 36.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -16.2) |
| [[SNU-1 (line)]] | wt | 12.7 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0564× (z -11.2) |
| [[SW48 (line)]] | wt | 52.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -12.5) |
| [[AN3 CA (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 286), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAN2B2]] | +0.70 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[LLGL1]] | +0.68 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[NRBP2]] | +0.67 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[AKT1]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 | STRING 597 |
| [[PLBD2]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[SBF1]] | +0.66 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[CTSZ]] | +0.66 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[ESYT1]] | +0.66 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[DLST]] | +0.65 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[SH3GLB2]] | +0.64 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[HECTD3]] | +0.64 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[DCTN1]] | +0.63 | +0.51 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGBOS1]] | -0.61 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[CEBPZ]] | -0.59 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[TOPORS]] | -0.59 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[MRPS18B]] | -0.58 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[KRTCAP2]] | -0.58 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[BTG1]] | -0.58 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[METTL23]] | -0.56 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[ERVK3-1]] | -0.56 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[FOXA2]] | -0.55 | -0.40 / -0.60 | both halves | 4e-05 |  |
| [[MRPL36]] | -0.55 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[MED19]] | -0.55 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[LINC01473]] | -0.55 | -0.67 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L2]] | B | EPS8L2 activity raises CAPN1's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 1.95× lower at baseline in the lines without EPS8L2 | 0.009 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[SEPTIN5]] | B | SEPTIN5 activity lowers CAPN1's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 1.79× higher at baseline in the lines without SEPTIN5 | 0.036 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[ZSWIM5]] | B | ZSWIM5 activity lowers CAPN1's level | lines that do not express ZSWIM5 (5) vs lines expressing it (45) | 1.69× higher at baseline in the lines without ZSWIM5 | 0.060 | ⚠ within organs, on part of the lines; also absent: DLGAP1, ABHD12B, TTN; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.638). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-8.3, -22.2); signed map (-46.6, -10.6). **Vector** length 92.0, 23.1% of its response variance represented; |z| ≥ 3 in 1,172 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.0 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.2 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.6 | +8.6 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +3.0 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.0 | +1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +1.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.0 | +1.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.0 | -9.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.9 | -18.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -24.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.1 | -37.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.5 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -7.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -1.3 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.8 | -2.0 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | calpain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,180,566-65,212,006 (+) |
| Ensembl biotype | protein_coding |
| Also known as | muCANP, muCL, CANP, CANPL1 |
| Gene groups (HGNC) | EF-hand domain containing; Calpains |
| Reactome | 10 pathways, smallest: Deregulated CDK5 triggers multiple neurodegenerative pathways in Alzheimer's disease models; Neurodegenerative Diseases; Defective Intrinsic Pathway for Apoptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [P07384](https://www.uniprot.org/uniprotkb/P07384) (Calpain-1 catalytic subunit):

> Calcium-regulated non-lysosomal thiol-protease which catalyzes limited proteolysis of substrates involved in cytoskeletal remodeling and signal transduction. Proteolytically cleaves CTBP1 at 'Asn-375', 'Gly-387' and 'His-409'. Cleaves and activates caspase-7 (CASP7).

**Summary**, from NCBI Gene [823](https://www.ncbi.nlm.nih.gov/gene/823):

> The calpains, calcium-activated neutral proteases, are nonlysosomal, intracellular cysteine proteases. The mammalian calpains include ubiquitous, stomach-specific, and muscle-specific proteins. The ubiquitous enzymes consist of heterodimers with distinct large, catalytic subunits associated with a common small, regulatory subunit. This gene encodes the large subunit of the ubiquitous enzyme, calpain 1. Several transcript variants encoding two different isoforms have been found for this gene. …

**Accessions** — [HGNC:1476](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1476) · Entrez [823](https://www.ncbi.nlm.nih.gov/gene/823) · UniProt [P07384](https://www.uniprot.org/uniprotkb/P07384) · Ensembl [ENSG00000014216](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000014216)

## Data

Gene col 286: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 286); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 286, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 286]; `tensor/DDL_lfc|DDL_z.npy` [286]; `embed/gene_vectors.npy` [286]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 286 or target_col == 286). Every well: [[CAPN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAPN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
