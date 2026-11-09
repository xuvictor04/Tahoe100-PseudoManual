---
symbol: "PRELID2"
type: "gene"
col: 11804
ensembl_id: "ENSG00000186314"
name: "PRELI domain containing 2"
location: "5q32"
module: 144
arm: "+"
pooled_cpm: 475.05
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 44
n_dd_up_clean: 2
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# PRELID2

*PRELI domain containing 2* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.40× (z +4.4, q 0.005, up in 33 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 44 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.104× (z -43.9, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIAS2]] (+0.64, fdr 1e-05), [[BCKDHB]] (+0.63, fdr 7e-06), [[YEATS2]] (+0.62, fdr 7e-06); moves opposite to [[CAMSAP1-DT]] (-0.49, fdr 3e-05), [[UBE2Q2P1-1]] (-0.48, fdr 6e-05), [[CDYL2]] (-0.48, fdr 1e-04).
> It is in [[Module 144]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11804.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +4.4 | 0.005 | 33/46 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.089 | 31/47 (KATO III, AsPC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.26× | +3.3 | 0.18 | 27/47 (KATO III, A-172, …) | rises with dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.26× | +3.2 | 0.18 | 31/47 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.26× | +3.2 | 0.18 | 24/46 (AsPC-1, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 22 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 44 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11804.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.104×** | -43.9 | 0e+00 | 47/47 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.138×** | -26.2 | 0e+00 | 47/47 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.200×** | -22.1 | 0e+00 | 47/47 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.254×** | -18.1 | 0e+00 | 45/46 (SNU-423, C32, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.329×** | -15.3 | 0e+00 | 47/47 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.315×** | -15.2 | 0e+00 | 46/46 (HCT15, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.338×** | -14.9 | 0e+00 | 45/48 (SK-MEL-2, C32, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.354×** | -14.2 | 3e-44 | 47/47 (LS 180, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.342×** | -14.2 | 7e-44 | 40/43 (NCI-H23, C32, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.395×** | -12.8 | 2e-35 | 46/47 (C32, H4, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.585×** | -10.4 | 1e-23 | 38/48 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.474×** | -10.2 | 6e-23 | 42/47 (HCT15, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.476×** | -10.2 | 9e-23 | 42/47 (HCT15, C32, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.481×** | -10.0 | 4e-22 | 47/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.486×** | -9.9 | 2e-21 | 46/47 (C32, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.499×** | -9.5 | 5e-20 | 44/47 (HCT15, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.300×** | -8.6 | 1e-16 | 41/48 (KATO III, C32, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.550×** | -8.2 | 6e-15 | 43/47 (HT-29, HCT15, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.362×** | -7.3 | 7e-12 | 40/47 (C32, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.598×** | -7.0 | 5e-11 | 44/47 (NCI-H1792, A549, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.604×** | -6.9 | 1e-10 | 35/47 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.591×** | -6.7 | 4e-10 | 39/47 (HT-29, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.789×** | -4.6 | 9e-05 | 28/48 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.724×** | -4.4 | 2e-04 | 38/47 (CFPAC-1, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11804. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 1,275 | 0 | 26 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0346× (z -50.3) |
| [[LS 180 (line)]] | wt | 677 | 0 | 22 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -31.9) |
| [[SNU-423 (line)]] | alt | 584 | 0 | 22 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0572× (z -50.4) |
| [[H4 (line)]] | wt | 478 | 0 | 21 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0444× (z -42.7) |
| [[SW480 (line)]] | alt | 278 | 0 | 21 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -28.5) |
| [[SNU-1 (line)]] | wt | 735 | 0 | 20 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -30.6) |
| [[AN3 CA (line)]] | alt | 663 | 0 | 19 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -20.7) |
| [[HCT15 (line)]] | alt | 973 | 0 | 19 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0733× (z -35.1) |
| [[HEC-1-A (line)]] | alt | 1,210 | 0 | 19 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0652× (z -38.8) |
| [[NCI-H460 (line)]] | wt | 529 | 0 | 19 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0590× (z -47.8) |
| [[A-172 (line)]] | wt | 601 | 0 | 18 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0937× (z -36.1) |
| [[COLO 205 (line)]] | alt | 541 | 0 | 18 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0770× (z -37.3) |
| [[HOP62 (line)]] | alt | 708 | 0 | 18 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0575× (z -43.9) |
| [[KATO III (line)]] | alt | 417 | 0 | 18 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -35.3) |
| [[PANC-1 (line)]] | alt | 436 | 0 | 18 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0705× (z -49.0) |
| [[SW 900 (line)]] | alt | 450 | 0 | 18 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0772× (z -36.2) |
| [[LOX-IMVI (line)]] | wt | 368 | 0 | 17 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -35.9) |
| [[NCI-H1792 (line)]] | alt | 786 | 0 | 16 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0276× (z -58.3) |
| [[A549 (line)]] | wt | 357 | 0 | 15 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0779× (z -44.4) |
| [[BT-474 (line)]] | alt | 256 | 0 | 15 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -29.7) |
| [[CFPAC-1 (line)]] | alt | 365 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0852× (z -35.0) |
| [[Hs 766T (line)]] | wt | 601 | 0 | 15 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0880× (z -33.8) |
| [[LoVo (line)]] | wt | 737 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0966× (z -38.7) |
| [[MIA PaCa-2 (line)]] | alt | 448 | 0 | 15 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0652× (z -37.1) |
| [[HT-29 (line)]] | alt | 532 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -32.5) |
| [[SK-MEL-2 (line)]] | alt | 700 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0913× (z -42.7) |
| [[J82 (line)]] | alt | 394 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -28.1) |
| [[SW1417 (line)]] | alt | 523 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -29.7) |
| [[SW48 (line)]] | wt | 467 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -22.6) |
| [[Panc 03.27 (line)]] | alt | 331 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -21.9) |
| [[HepG2_C3A (line)]] | wt | 299 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -25.6) |
| [[HS-578T (line)]] | alt | 783 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0568× (z -36.6) |
| [[hTERT-HPNE (line)]] | wt | 385 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -29.8) |
| [[NCI-H1573 (line)]] | alt | 242 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -33.2) |
| [[NCI-H23 (line)]] | alt | 402 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0764× (z -37.8) |
| [[C-33 A (line)]] | alt | 224 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -13.8) |
| [[SW 1271 (line)]] | alt | 468 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -21.6) |
| [[A-427 (line)]] | wt | 205 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.185× (z -18.8) |
| [[SHP-77 (line)]] | alt | 165 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -14.0) |
| [[AsPC-1 (line)]] | alt | 495 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -23.9) |
| [[NCI-H2030 (line)]] | alt | 214 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -21.5) |
| [[RKO (line)]] | wt | 269 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -18.8) |
| [[A498 (line)]] | wt | 121 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -23.6) |
| [[NCI-H2347 (line)]] | alt | 193 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -27.9) |
| [[SW 1088 (line)]] | alt | 722 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0769× (z -20.4) |
| [[RPMI-7951 (line)]] | alt | 126 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -28.3) |
| [[CHP-212 (line)]] | wt | 56.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 410 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 480 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 427 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11804), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIAS2]] | +0.64 | +0.57 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[BCKDHB]] | +0.63 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[YEATS2]] | +0.62 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[METTL15]] | +0.60 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[ZNF395]] | +0.57 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[CABIN1]] | +0.56 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[PLEKHA2]] | +0.56 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[PFKFB4]] | +0.56 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[FAM216A]] | +0.54 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[PDK3]] | +0.53 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[PRDX2]] | +0.52 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[BNIP3]] | +0.52 | +0.54 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMSAP1-DT]] | -0.49 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[UBE2Q2P1-1]] | -0.48 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[CDYL2]] | -0.48 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[MICAL1]] | -0.47 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[IGDCC4]] | -0.46 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[ZNF83]] | -0.45 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[NGRN]] | -0.45 | -0.37 / -0.48 | both halves | 9e-05 |  |
| [[CLCF1]] | -0.44 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[MDGA1]] | -0.43 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[BMAL2]] | -0.43 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[SNX21]] | -0.43 | -0.28 / -0.41 | both halves | 3e-04 |  |
| [[MAP3K10]] | -0.42 | -0.35 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PRELID2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.493). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.5, -17.4); signed map (-37.6, 24.3). **Vector** length 91.1, 44.8% of its response variance represented; |z| ≥ 3 in 2,042 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.0 | +0.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.8 | -0.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.5 | +0.9 |
|  | [[EX229 (drug)]] 5 µM |  | +4.0 | +0.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.6 | -0.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.6 | +0.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.5 | -15.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -7.0 | -9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -5.2 | -14.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -4.3 | -1.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -4.1 | -14.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -3.8 | -2.0 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -3.7 | -0.9 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -3.6 | -1.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.3 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | PRELI domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:145,471,799-145,835,369 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC21644, FLJ38376 |
| Gene groups (HGNC) | PRELI domain containing |
| Matched by | ensembl_id |

UniProt [Q8N945](https://www.uniprot.org/uniprotkb/Q8N945) carries no function annotation.

**Summary**, from NCBI Gene [153768](https://www.ncbi.nlm.nih.gov/gene/153768):

> Predicted to enable phosphatidic acid transfer activity. Predicted to be involved in phospholipid transport. Predicted to be active in mitochondrial intermembrane space. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28306](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28306) · Entrez [153768](https://www.ncbi.nlm.nih.gov/gene/153768) · UniProt [Q8N945](https://www.uniprot.org/uniprotkb/Q8N945) · Ensembl [ENSG00000186314](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186314)

## Data

Gene col 11804: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11804); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11804, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11804]; `tensor/DDL_lfc|DDL_z.npy` [11804]; `embed/gene_vectors.npy` [11804]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11804 or target_col == 11804). Every well: [[PRELID2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRELID2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
