---
symbol: "TXNL4B"
type: "gene"
col: 6452
ensembl_id: "ENSG00000140830"
name: "thioredoxin like 4B"
location: "16q22.2"
module: 41
arm: "+"
pooled_cpm: 17.68
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 1
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# TXNL4B

*thioredoxin like 4B* — 16q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.01× (z +30.9, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.764× (z -4.4, q 0.008, down in 16 of 29 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H460 0.192×, SW480 0.366×, A549 0.194×, HT-29 0.125×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A549 0.0959×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Monocrotaline (drug)]] 0.05 µM in 1 line (BT-474 0.0763×); [[Pravastatin (sodium) (drug)]] 0.05 µM in 1 line (SW48 0.0861×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF2B]] (+0.66, fdr 1e-05), [[RSRP1]] (+0.65, fdr 1e-05), [[POLR2A]] (+0.65, fdr 1e-05); moves opposite to [[KPNA1]] (-0.61, fdr 1e-05), [[G3BP1]] (-0.60, fdr 4e-05), [[DHX9]] (-0.60, fdr 4e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6452.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.01×** | +30.9 | 0e+00 | 45/47 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.05×** | +18.7 | 0e+00 | 43/46 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.11×** | +16.7 | 0e+00 | 41/47 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.59×** | +15.9 | 0e+00 | 44/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.27×** | +13.7 | 8e-41 | 46/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.09×** | +12.3 | 9e-33 | 40/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.03×** | +11.9 | 1e-30 | 43/48 (SW480, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.05×** | +11.6 | 4e-29 | 40/47 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +11.0 | 1e-26 | 35/44 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.81×** | +9.9 | 2e-21 | 35/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +9.4 | 3e-19 | 30/46 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +9.1 | 4e-18 | 36/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.64×** | +8.0 | 6e-14 | 30/48 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +7.6 | 1e-12 | 35/47 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.54×** | +7.3 | 2e-11 | 31/47 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.51×** | +6.5 | 3e-09 | 27/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +6.4 | 6e-09 | 26/48 (HOP62, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +6.3 | 1e-08 | 27/48 (J82, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +5.3 | 3e-06 | 23/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6452.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H460 0.192×, SW480 0.366×, A549 0.194×, HT-29 0.125×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A549 0.0959×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Monocrotaline (drug)]] 0.05 µM in 1 line (BT-474 0.0763×); [[Pravastatin (sodium) (drug)]] 0.05 µM in 1 line (SW48 0.0861×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.764×** | -4.4 | 0.008 | 16/29 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -4.1 | 0.010 | 1/48 (SW 1271) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.830× | -3.1 | 0.28 | 7/47 (hTERT-HPNE, HOP62, …) | top dose only |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.832× | -3.1 | 0.28 | 6/48 (HS-578T, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6452. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 36.5 | 9 (3 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +20.4) | [[Dinaciclib (drug)]] 5 µM 0.366× (z -11.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 21.6 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.59× (z +19.6) | — |
| [[A549 (line)]] | wt | 17.9 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.0959× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 19.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.60× (z +20.5) | — |
| [[LoVo (line)]] | wt | 11.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 11.6 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.192× (z -11.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 12.9 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +13.2) | — |
| [[BT-474 (line)]] | alt | 13.3 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.49× (z +12.3) | [[Monocrotaline (drug)]] 0.05 µM 0.0763× (z -11.9) |
| [[C32 (line)]] | wt | 13.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.75× (z +12.9) | — |
| [[NCI-H1573 (line)]] | alt | 18.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.60× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 19.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +14.5) | — |
| [[SK-MEL-2 (line)]] | alt | 18.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +12.2) | — |
| [[A-172 (line)]] | wt | 15.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +13.6) | — |
| [[AsPC-1 (line)]] | alt | 14.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +11.0) | — |
| [[CFPAC-1 (line)]] | alt | 15.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +14.5) | — |
| [[HEC-1-A (line)]] | alt | 17.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.23× (z +14.7) | — |
| [[HT-29 (line)]] | alt | 11.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.24× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.125× (z -10.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 15.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.01× (z +13.1) | — |
| [[LS 180 (line)]] | wt | 13.3 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.37× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 23.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +14.1) | — |
| [[A498 (line)]] | wt | 24.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 14.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.34× (z +10.9) | — |
| [[hTERT-HPNE (line)]] | wt | 14.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.26× (z +11.1) | — |
| [[J82 (line)]] | alt | 15.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.23× (z +14.3) | — |
| [[KATO III (line)]] | alt | 19.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 11.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +13.6) | — |
| [[Panc 03.27 (line)]] | alt | 13.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.86× (z +11.4) | — |
| [[RKO (line)]] | wt | 19.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.72× (z +14.9) | — |
| [[RPMI-7951 (line)]] | alt | 22.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +10.1) | — |
| [[SNU-423 (line)]] | alt | 17.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +12.1) | — |
| [[SW 900 (line)]] | alt | 13.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.71× (z +12.0) | — |
| [[SW1417 (line)]] | alt | 21.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +9.2) | — |
| [[SW48 (line)]] | wt | 13.0 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0861× (z -9.0) |
| [[A-427 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6452), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2B]] | +0.66 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[RSRP1]] | +0.65 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[POLR2A]] | +0.65 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[BTN2A1]] | +0.65 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[HMGCL]] | +0.64 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[BET1]] | +0.62 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[PMS2P4-1]] | +0.61 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[SNIP1]] | +0.60 | +0.57 / +0.38 | both halves | 6e-05 | STRING 434 |
| [[KLC4]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[IKZF4]] | +0.60 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[SYNRG]] | +0.60 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[ZRSR2]] | +0.60 | +0.58 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNA1]] | -0.61 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[G3BP1]] | -0.60 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[DHX9]] | -0.60 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[AGPS]] | -0.59 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[EXT2]] | -0.58 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[ADAMTSL5]] | -0.57 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[LBR]] | -0.56 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[RAB10]] | -0.55 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[GSK3B]] | -0.55 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[CHML]] | -0.55 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[UBE2E3]] | -0.55 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[NF2]] | -0.54 | -0.30 / -0.55 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TXNL4B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.626). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (6.1, -38.6); signed map (-3.4, 2.9). **Vector** length 57.8, 9.80% of its response variance represented; |z| ≥ 3 in 1,151 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +30.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.2 | +11.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.2 | +8.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +9.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.0 | +18.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +5.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | -0.3 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +1.2 | +0.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.1 | +1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.1 | +1.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.3 | +1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.2 | -4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.2 | -3.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.0 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -0.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | +2.4 |

## What is on record

|  |  |
|---|---|
| Name | thioredoxin like 4B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.2 — chr16:72,044,289-72,094,431 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20511, DLP, Dim2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NX01](https://www.uniprot.org/uniprotkb/Q9NX01) (Thioredoxin-like protein 4B):

> Essential role in pre-mRNA splicing. Required in cell cycle progression for S/G(2) transition.

**Summary**, from NCBI Gene [54957](https://www.ncbi.nlm.nih.gov/gene/54957):

> Predicted to be involved in spliceosomal tri-snRNP complex assembly and spliceosome conformational change to release U4 (or U4atac) and U1 (or U11). Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26041](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26041) · Entrez [54957](https://www.ncbi.nlm.nih.gov/gene/54957) · UniProt [Q9NX01](https://www.uniprot.org/uniprotkb/Q9NX01) · Ensembl [ENSG00000140830](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140830)

## Data

Gene col 6452: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6452); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6452, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6452]; `tensor/DDL_lfc|DDL_z.npy` [6452]; `embed/gene_vectors.npy` [6452]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6452 or target_col == 6452). Every well: [[TXNL4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TXNL4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
