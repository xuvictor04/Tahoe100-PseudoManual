---
symbol: "NHS"
type: "gene"
col: 11981
ensembl_id: "ENSG00000188158"
name: "NHS actin remodeling regulator"
location: "Xp22.2-p22.13"
module: 34
arm: "+"
pooled_cpm: 175.69
n_lines_expressing: 33
n_dd_up: 3
n_dd_down: 43
n_dd_up_clean: 3
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 21
direction_downstream: 11
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# NHS

*NHS actin remodeling regulator* — Xp22.2-p22.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.41× (z +7.0, q 2e-09, up in 21 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.622× (z -9.5, q 2e-18, down in 24 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GJA1]] (+0.66, fdr 1e-05), [[EDIL3]] (+0.63, fdr 1e-05), [[FAM107B]] (+0.60, fdr 1e-05); moves opposite to [[MAOA]] (-0.53, fdr 2e-05), [[ADGRG2]] (-0.47, fdr 5e-05), [[ACSL1]] (-0.46, fdr 4e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[RAB27B]] → it (grade B ⚠); 11 go from it, the strongest it → [[NR3C1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11981.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +7.0 | 2e-09 | 21/31 (SW480, SW1417, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.025 | 17/31 (HOP62, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.025 | 19/32 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.2 | 0.19 | 12/31 (NCI-H1573, Panc 03.27, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.24× | +3.1 | 0.21 | 15/31 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11981.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.622×** | -9.5 | 2e-18 | 24/32 (HS-578T, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.501×** | -9.4 | 2e-18 | 26/30 (A-172, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.540×** | -8.4 | 1e-14 | 23/31 (Hs 766T, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.542×** | -8.3 | 1e-14 | 27/30 (HT-29, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.694×** | -7.3 | 4e-11 | 19/31 (Hs 766T, NCI-H2030, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.529×** | -7.2 | 5e-11 | 25/32 (A-172, NCI-H1792, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.699×** | -7.1 | 9e-11 | 21/31 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.584×** | -7.0 | 2e-10 | 22/30 (A-172, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.609×** | -7.0 | 2e-10 | 20/31 (NCI-H23, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.627×** | -6.6 | 3e-09 | 22/31 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **0.637×** | -6.3 | 1e-08 | 24/31 (HT-29, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.621×** | -6.3 | 1e-08 | 24/31 (HT-29, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.636×** | -6.1 | 4e-08 | 23/32 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.651×** | -6.0 | 6e-08 | 24/31 (Hs 766T, NCI-H1573, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.654×** | -6.0 | 8e-08 | 23/31 (RPMI-7951, A-172, …) | two highest doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.669×** | -5.7 | 5e-07 | 20/31 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.687×** | -5.3 | 4e-06 | 22/31 (A-172, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.633×** | -5.2 | 7e-06 | 19/31 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.708×** | -4.9 | 3e-05 | 20/31 (NCI-H1573, Hs 766T, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.717×** | -4.7 | 8e-05 | 19/31 (Hs 766T, RPMI-7951, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.664×** | -4.6 | 1e-04 | 20/31 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11981. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 211 | 0 | 29 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -22.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.173× (z -15.1) |
| [[NCI-H1573 (line)]] | alt | 210 | 0 | 21 (1 ⚠) | — | [[Triamcinolone (drug)]] 0.5 µM 0.112× (z -14.3) |
| [[A-172 (line)]] | wt | 427 | 0 | 15 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -12.5) |
| [[NCI-H1792 (line)]] | alt | 909 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -21.5) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -18.5) |
| [[HS-578T (line)]] | alt | 258 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -20.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -19.5) |
| [[SNU-423 (line)]] | alt | 551 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -14.4) |
| [[NCI-H460 (line)]] | wt | 442 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -18.4) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -9.4) |
| [[HT-29 (line)]] | alt | 305 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.153× (z -17.4) ⚠ toxic · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.285× (z -11.4) |
| [[LoVo (line)]] | wt | 141 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +18.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.25× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.408× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H2030 (line)]] | alt | 283 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -22.6) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -12.5) |
| [[SW 900 (line)]] | alt | 284 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -13.5) |
| [[CFPAC-1 (line)]] | alt | 489 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.205× (z -13.2) ⚠ toxic · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.348× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 176 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -12.5) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.446× (z -9.3) |
| [[J82 (line)]] | alt | 137 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 305 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -13.1) |
| [[SW480 (line)]] | alt | 52.5 | 2 | 1 | [[Tucidinostat (drug)]] 5 µM 2.81× (z +13.5) | [[Harringtonine (drug)]] 5 µM 0.378× (z -8.7) |
| [[A498 (line)]] | wt | 66.9 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.380× (z -9.7) |
| [[A549 (line)]] | wt | 281 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -13.3) |
| [[CHP-212 (line)]] | wt | 91.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0447× (z -13.5) |
| [[NCI-H2347 (line)]] | alt | 153 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -14.0) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -13.6) |
| [[Panc 03.27 (line)]] | alt | 233 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.368× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 210 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.346× (z -9.9) |
| [[SW1417 (line)]] | alt | 110 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.54× (z +12.4) | [[Dinaciclib (drug)]] 0.05 µM 0.375× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 54.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -9.1) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SHP-77 (line)]] | alt | 150 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.388× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 24.4 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.3 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 13.2 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.7 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.8 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 18.6 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 15.5 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 37.5 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.38 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 27.2 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 14.0 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 26.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.8 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 72.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11981), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GJA1]] | +0.66 | +0.70 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[EDIL3]] | +0.63 | +0.71 / +0.50 | both halves | 1e-05 | **novel candidate** |
| [[FAM107B]] | +0.60 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[AADACP1]] | +0.57 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[BMPER]] | +0.56 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[IGFBP3]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[VEGFC]] | +0.55 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[FRMD5]] | +0.55 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[SYNJ2]] | +0.54 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[PTHLH]] | +0.54 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[C6orf141]] | +0.54 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[WNT7B]] | +0.53 | +0.57 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAOA]] | -0.53 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[ADGRG2]] | -0.47 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[ACSL1]] | -0.46 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[KLF9]] | -0.46 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[COPS8]] | -0.45 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[RILPL2]] | -0.45 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[LTBR]] | -0.44 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[MT1M]] | -0.44 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[SLC26A2]] | -0.44 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[SH3TC1]] | -0.43 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[BATF]] | -0.43 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[EDN2]] | -0.43 | -0.43 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 18, C 3. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB27B]] | B | RAB27B activity raises NHS's level | lines that do not express RAB27B (15) vs lines expressing it (35) | 4.40× lower at baseline in the lines without RAB27B | 0.010 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3 |
| [[FAM107B]] | B | FAM107B activity raises NHS's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 3.14× lower at baseline in the lines without FAM107B | 0.023 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[EDIL3-DT]] | B | EDIL3-DT activity raises NHS's level | lines that do not express EDIL3-DT (25) vs lines expressing it (25) | 3.76× lower at baseline in the lines without EDIL3-DT | 0.024 | ⚠ within organs, on part of the lines; also absent: EDIL3, NALCN, DTNA |
| [[SRPX2]] | B | SRPX2 activity raises NHS's level | lines that do not express SRPX2 (24) vs lines expressing it (26) | 2.95× lower at baseline in the lines without SRPX2 | 0.043 | ⚠ within organs, on part of the lines; also absent: TGFBI, GBP5, FN1 |
| [[STAC]] | B | STAC activity raises NHS's level | lines that do not express STAC (25) vs lines expressing it (25) | 3.73× lower at baseline in the lines without STAC | 0.043 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11 |
| [[ANXA10]] | B | ANXA10 activity raises NHS's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 3.43× lower at baseline in the lines without ANXA10 | 0.045 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP |
| [[GPR39]] | B | GPR39 activity raises NHS's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 3.55× lower at baseline in the lines without GPR39 | 0.059 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[ARHGAP42]] | B | ARHGAP42 activity raises NHS's level | lines that do not express ARHGAP42 (13) vs lines expressing it (37) | 2.89× lower at baseline in the lines without ARHGAP42 | 0.062 | ⚠ within organs, on part of the lines; also absent: C6orf141, BACE2, LINC01348; maybe low, not absent |
| [[AHR]] | B | AHR activity raises NHS's level | lines that do not express AHR (7) vs lines expressing it (43) | 3.63× lower at baseline in the lines without AHR | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[NALCN]] | B | NALCN activity raises NHS's level | lines that do not express NALCN (22) vs lines expressing it (28) | 3.12× lower at baseline in the lines without NALCN | 0.072 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229 |
| [[PRKCA]] | B | PRKCA activity raises NHS's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 4.52× lower at baseline in the lines without PRKCA | 0.081 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[PTHLH]] | B | PTHLH activity raises NHS's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 3.53× lower at baseline in the lines without PTHLH | 0.083 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1 |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 9, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NHS activity raises NR3C1's level | lines that do not express NHS (17) vs lines expressing it (33) | 2.67× lower at baseline in the lines without NHS | 0.009 | ⚠ within organs, on part of the lines; also absent: ANKRD29, WNT7B, ABCC3 |
| [[ARHGAP42]] | B | NHS activity raises ARHGAP42's level | lines that do not express NHS (17) vs lines expressing it (33) | 2.40× lower at baseline in the lines without NHS | 0.015 | ⚠ within organs, on part of the lines; also absent: ANKRD29, WNT7B, ABCC3 |
| [[FAM107B]] | B | NHS activity raises FAM107B's level | lines that do not express NHS (17) vs lines expressing it (33) | 3.10× lower at baseline in the lines without NHS | 0.021 | ⚠ within organs, on part of the lines; also absent: ANKRD29, WNT7B, ABCC3 |
| [[SMAD3]] | B | NHS activity raises SMAD3's level | lines that do not express NHS (17) vs lines expressing it (33) | 1.77× lower at baseline in the lines without NHS | 0.040 | ⚠ within organs, on part of the lines; also absent: ANKRD29, WNT7B, ABCC3 |
| [[GPR39]] | B | NHS activity raises GPR39's level | lines that do not express NHS (17) vs lines expressing it (33) | 2.46× lower at baseline in the lines without NHS | 0.065 | ⚠ within organs, on part of the lines; also absent: ANKRD29, WNT7B, ABCC3 |
| [[SH3TC1]] | B | NHS activity raises SH3TC1's level | lines that do not express NHS (17) vs lines expressing it (33) | 1.81× lower at baseline in the lines without NHS | 0.079 | ⚠ within organs, on part of the lines; also absent: ANKRD29, WNT7B, ABCC3 |
| [[MXRA5]] | B | NHS activity raises MXRA5's level | lines that do not express NHS (17) vs lines expressing it (33) | 2.68× lower at baseline in the lines without NHS | 0.087 | ⚠ within organs, on part of the lines; also absent: ANKRD29, WNT7B, ABCC3 |
| [[IGFBP3]] | B | NHS activity raises IGFBP3's level | lines that do not express NHS (17) vs lines expressing it (33) | 3.73× lower at baseline in the lines without NHS | 0.095 | ⚠ within organs, on part of the lines; also absent: ANKRD29, WNT7B, ABCC3 |
| [[C6orf141]] | B | NHS activity raises C6orf141's level | lines that do not express NHS (17) vs lines expressing it (33) | 2.20× lower at baseline in the lines without NHS | 0.096 | ⚠ within organs, on part of the lines; also absent: ANKRD29, WNT7B, ABCC3 |
| [[WNT7B]] | C | NHS activity raises WNT7B's level | lines that do not express NHS (17) vs lines expressing it (33) | 4.08× lower at baseline in the lines without NHS | 0.002 | ⚠ within organs, on part of the lines; also absent: ANKRD29, WNT7B, ABCC3; co-absent with the target |
| [[EDN2]] | C | NHS activity raises EDN2's level | lines that do not express NHS (17) vs lines expressing it (33) | 2.07× lower at baseline in the lines without NHS | 0.068 | ⚠ within organs, on part of the lines; also absent: ANKRD29, WNT7B, ABCC3; co-absent with the target |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.338). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.7, 22.0); signed map (37.3, 46.4). **Vector** length 118, 36.0% of its response variance represented; |z| ≥ 3 in 1,250 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.6 | +7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.6 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.6 | +3.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.6 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +3.0 | -7.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +3.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.1 | +2.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -5.1 | -4.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.9 | -7.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -4.8 | -6.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.8 | -4.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.7 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | NHS actin remodeling regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2-p22.13 — chrX:17,375,200-17,735,994 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MicroRNA protein coding host genes; NHS family |
| Reactome | 6 pathways, smallest: RAC2 GTPase cycle; RAC3 GTPase cycle; RAC1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6T4R5](https://www.uniprot.org/uniprotkb/Q6T4R5) (Actin remodeling regulator NHS):

> May function in cell morphology by maintaining the integrity of the circumferential actin ring and controlling lamellipod formation. Involved in the regulation eye, tooth, brain and craniofacial development.

**Summary**, from NCBI Gene [4810](https://www.ncbi.nlm.nih.gov/gene/4810):

> This gene encodes a protein containing four conserved nuclear localization signals. The encoded protein functions in eye, tooth, craniofacial and brain development, and it can regulate actin remodeling and cell morphology. Mutations in this gene have been shown to cause Nance-Horan syndrome, and also X-linked cataract-40. Alternatively spliced transcript variants encoding different isoforms have been described for this gene. [provided by RefSeq, May 2014]

**Accessions** — [HGNC:7820](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7820) · Entrez [4810](https://www.ncbi.nlm.nih.gov/gene/4810) · UniProt [Q6T4R5](https://www.uniprot.org/uniprotkb/Q6T4R5) · Ensembl [ENSG00000188158](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188158)

## Data

Gene col 11981: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11981); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11981, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11981]; `tensor/DDL_lfc|DDL_z.npy` [11981]; `embed/gene_vectors.npy` [11981]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11981 or target_col == 11981). Every well: [[NHS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NHS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
