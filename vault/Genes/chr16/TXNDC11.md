---
symbol: "TXNDC11"
type: "gene"
col: 7686
ensembl_id: "ENSG00000153066"
name: "thioredoxin domain containing 11"
location: "16p13.13"
module: 56
arm: "+"
pooled_cpm: 89.1
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 40
n_dd_up_clean: 1
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# TXNDC11

*thioredoxin domain containing 11* — 16p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 1.82× (z +4.2, q 0.014, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.261× (z -18.0, q 0e+00, down in 47 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.460× (z -10.0, q 2e-21, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF2AK3]] (+0.86, fdr 7e-06), [[PDIA5]] (+0.80, fdr 7e-06), [[TMEM39A]] (+0.80, fdr 7e-06); moves opposite to [[ZNF462]] (-0.63, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MPDZ]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7686.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **1.82×** | +4.2 | 0.014 | 30/48 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.2 | 0.42 | 0/50 | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7686.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.261×** | -18.0 | 0e+00 | 47/48 (AsPC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.269×** | -16.2 | 0e+00 | 43/45 (A498, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.294×** | -15.8 | 0e+00 | 41/43 (NCI-H1573, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.494×** | -12.5 | 1e-33 | 44/48 (A-172, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.460×** | -10.0 | 2e-21 | 43/48 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.628×** | -8.4 | 3e-15 | 43/48 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.556×** | -7.8 | 4e-13 | 35/48 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.612×** | -6.3 | 2e-08 | 37/47 (NCI-H2030, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.624×** | -6.3 | 2e-08 | 32/48 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.637×** | -5.8 | 4e-07 | 36/48 (SK-MEL-2, NCI-H1792, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.727×** | -5.7 | 7e-07 | 33/48 (AsPC-1, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.700×** | -4.8 | 9e-05 | 30/48 (AsPC-1, LoVo, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.705×** | -4.7 | 1e-04 | 32/48 (A549, A-172, …) | all doses, stronger at high dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.725×** | -4.3 | 7e-04 | 34/48 (HT-29, LS 180, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.727×** | -4.3 | 8e-04 | 28/48 (NCI-H1573, HOP62, …) | two highest doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.751×** | -3.8 | 0.004 | 29/48 (HT-29, A498, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.758×** | -3.7 | 0.006 | 26/49 (C32, HT-29, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.763×** | -3.6 | 0.009 | 28/48 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.769×** | -3.5 | 0.011 | 26/48 (SW1417, HT-29, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.775×** | -3.4 | 0.016 | 27/49 (HT-29, SW 1088, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.776×** | -3.4 | 0.016 | 24/48 (A-427, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7686. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 97.5 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -22.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.228× (z -15.0) |
| [[NCI-H2347 (line)]] | alt | 63.5 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.293× (z -12.5) |
| [[AsPC-1 (line)]] | alt | 266 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -25.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.392× (z -10.6) |
| [[A549 (line)]] | wt | 106 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -18.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.221× (z -16.1) |
| [[HS-578T (line)]] | alt | 106 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.187× (z -14.5) |
| [[NCI-H1573 (line)]] | alt | 138 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0453× (z -28.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.308× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 90.9 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.292× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 62.7 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.332× (z -8.8) |
| [[A498 (line)]] | wt | 158 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.383× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 87.0 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -13.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 71.9 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -16.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 90.6 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0678× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.242× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 70.9 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -12.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[PANC-1 (line)]] | alt | 50.9 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.326× (z -11.3) |
| [[SNU-423 (line)]] | alt | 66.4 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0863× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.298× (z -9.5) |
| [[Hs 766T (line)]] | wt | 160 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.452× (z -9.9) |
| [[J82 (line)]] | alt | 98.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -16.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 114 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -13.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 90.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -13.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 80.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -12.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 91.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -9.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 113 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -16.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 105 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -11.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 88.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -10.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 97.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.343× (z -8.6) |
| [[SW480 (line)]] | alt | 62.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -16.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 43.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.210× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.339× (z -8.6) |
| [[H4 (line)]] | wt | 114 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0844× (z -16.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 71.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.238× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 37.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -11.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 67.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -11.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 63.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -14.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 90.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -11.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 105 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -10.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 68.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -13.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 49.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -12.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 81.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -10.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -10.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 76.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -8.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 44.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -17.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H460 (line)]] | wt | 70.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -9.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 72.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 94.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 73.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 98.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7686), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2AK3]] | +0.86 | +0.82 / +0.84 | both halves | 7e-06 |  |
| [[PDIA5]] | +0.80 | +0.83 / +0.71 | both halves | 7e-06 |  |
| [[TMEM39A]] | +0.80 | +0.84 / +0.75 | both halves | 7e-06 |  |
| [[NDEL1]] | +0.80 | +0.79 / +0.78 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.78 | +0.79 / +0.72 | both halves | 7e-06 |  |
| [[PDXDC2P]] | +0.78 | +0.78 / +0.73 | both halves | 7e-06 |  |
| [[SEC31A]] | +0.77 | +0.79 / +0.72 | both halves | 7e-06 |  |
| [[COPA]] | +0.77 | +0.82 / +0.69 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.77 | +0.78 / +0.74 | both halves | 7e-06 |  |
| [[DNAJC25]] | +0.77 | +0.70 / +0.82 | both halves | 7e-06 |  |
| [[SSR2]] | +0.77 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[SEC23A]] | +0.76 | +0.81 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF462]] | -0.63 | -0.65 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPDZ]] | B | MPDZ activity lowers TXNDC11's level | lines that do not express MPDZ (17) vs lines expressing it (33) | 1.31× higher at baseline in the lines without MPDZ | 0.073 | ⚠ within organs, on part of the lines; also absent: GNB4, BVES, BVES-AS1 |
| [[LINC01881]] | C | LINC01881's natural level strengthens TXNDC11's drug response | LINC01881's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.61, reverse +0.09; direction not clear | 0.091 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.841). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.6, -33.2); signed map (-50.4, 10.0). **Vector** length 119, 42.2% of its response variance represented; |z| ≥ 3 in 1,105 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.68 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.68 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.68 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +5.6 | -3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | +5.2 | -3.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +4.6 | -4.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +4.3 | -3.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +3.6 | -3.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.9 | +0.7 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.7 | +1.4 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.7 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +0.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.7 | +0.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.2 | -10.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.8 | -6.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -7.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.1 | -12.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -8.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -4.3 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -3.2 | -3.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.0 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | thioredoxin domain containing 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.13 — chr16:11,679,083-11,742,857 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EFP1 |
| Gene groups (HGNC) | Thioredoxin domain containing |
| Reactome | 3 pathways, smallest: Metabolism of amine-derived hormones; Thyroxine biosynthesis; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PKC3](https://www.uniprot.org/uniprotkb/Q6PKC3) (Thioredoxin domain-containing protein 11):

> May act as a redox regulator involved in DUOX proteins folding. The interaction with DUOX1 and DUOX2 suggest that it belongs to a multiprotein complex constituting the thyroid H(2)O(2) generating system. It is however not sufficient to assist DUOX1 and DUOX2 in H(2)O(2) generation.

**Summary**, from NCBI Gene [51061](https://www.ncbi.nlm.nih.gov/gene/51061):

> Located in cytosol and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28030](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28030) · Entrez [51061](https://www.ncbi.nlm.nih.gov/gene/51061) · UniProt [Q6PKC3](https://www.uniprot.org/uniprotkb/Q6PKC3) · Ensembl [ENSG00000153066](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153066)

## Data

Gene col 7686: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7686); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7686, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7686]; `tensor/DDL_lfc|DDL_z.npy` [7686]; `embed/gene_vectors.npy` [7686]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7686 or target_col == 7686). Every well: [[TXNDC11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TXNDC11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
