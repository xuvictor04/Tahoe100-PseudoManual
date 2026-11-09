---
symbol: "NPM1"
type: "gene"
col: 11170
ensembl_id: "ENSG00000181163"
name: "nucleophosmin 1"
location: "5q35.1"
module: 43
arm: "+"
pooled_cpm: 505.12
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# NPM1

*nucleophosmin 1* — 5q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.14× (z +13.6, q 3e-39, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.48× (z +4.7, q 2e-04, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Carbidopa (monohydrate) (drug)]] 0.05 µM: 0.706× (z -4.2, q 0.016, down in 48 of 49 measured lines) ⚠ unreliable plate only; position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.480×; ⚠ cell-cycle shift, explains ~89% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.568×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNRNPA1]] (+0.74, fdr 7e-06), [[RPL14]] (+0.73, fdr 7e-06), [[EEF2]] (+0.72, fdr 7e-06); moves opposite to [[DCAF15]] (-0.52, fdr 1e-05), [[PCSK7]] (-0.48, fdr 1e-04), [[TMED1]] (-0.47, fdr 3e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[EEF1G]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11170.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.14×** | +13.6 | 3e-39 | 49/49 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.87×** | +12.2 | 1e-31 | 44/44 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +8.6 | 2e-15 | 44/45 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.47×** | +6.6 | 6e-09 | 30/48 (C32, COLO 205, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +6.5 | 8e-09 | 43/47 (COLO 205, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.63×** | +5.9 | 3e-07 | 36/48 (C32, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +4.7 | 2e-04 | 42/48 (HT-29, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +4.5 | 5e-04 | 42/48 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.86×** | +3.9 | 0.006 | 43/48 (HT-29, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +3.8 | 0.008 | 37/48 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.37×** | +3.8 | 0.008 | 30/48 (KATO III, NCI-H460, …) | inconsistent across doses | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.012 | 32/48 (AN3 CA, SK-MEL-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~74% of this change | **1.35×** | +3.6 | 0.014 | 35/48 (BT-474, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.33×** | +3.5 | 0.021 | 30/48 (KATO III, NCI-H460, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.031 | 25/49 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.031 | 27/50 (MIA PaCa-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.038 | 34/48 (C32, NCI-H1792, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +3.1 | 0.055 | 29/48 (C32, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.64×** | +3.1 | 0.057 | 37/48 (CFPAC-1, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.20× | +3.1 | 0.057 | 24/49 (NCI-H2030, AN3 CA, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11170.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.480×; ⚠ cell-cycle shift, explains ~89% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.568×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.706×** | -4.2 | 0.016 | 48/49 (HT-29, SW1417, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.819× | -3.3 | 0.22 | 30/48 (C-33 A, AsPC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.761× | -3.2 | 0.22 | 33/48 (RKO, SW1417, …) | inconsistent across doses | position effect removed |
| [[Pentagastrin (drug)]] 5 µM |  | 0.832× | -3.1 | 0.26 | 22/48 (SNU-1, NCI-H460, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11170. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 254 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +12.1) ⚠ cell-cycle shift, explains ~89% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +8.8) | — |
| [[C32 (line)]] | wt | 333 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +18.4) ⚠ cell-cycle shift, explains ~89% of this change | — |
| [[KATO III (line)]] | alt | 305 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.17× (z +17.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 300 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +15.1) ⚠ cell-cycle shift, explains ~89% of this change | — |
| [[A498 (line)]] | wt | 400 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +13.3) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 244 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +17.2) ⚠ cell-cycle shift, explains ~89% of this change | — |
| [[Hs 766T (line)]] | wt | 372 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +12.4) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 424 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +13.1) ⚠ cell-cycle shift, explains ~89% of this change | — |
| [[NCI-H1573 (line)]] | alt | 232 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +15.3) ⚠ cell-cycle shift, explains ~89% of this change | — |
| [[SW 900 (line)]] | alt | 787 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +14.0) ⚠ cell-cycle shift, explains ~89% of this change | — |
| [[A-427 (line)]] | wt | 735 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +12.2) ⚠ toxic; transcription drop | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.568× (z -8.9) |
| [[HT-29 (line)]] | alt | 416 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +14.4) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 407 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +12.1) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 743 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +13.3) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 252 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.4) ⚠ cell-cycle shift, explains ~89% of this change | — |
| [[SW480 (line)]] | alt | 608 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +13.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 568 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +13.3) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 335 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +12.3) ⚠ cell-cycle shift, explains ~89% of this change | — |
| [[C-33 A (line)]] | alt | 490 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -10.8) ⚠ cell-cycle shift, explains ~89% of this change |
| [[H4 (line)]] | wt | 427 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +10.5) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 595 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +12.5) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 404 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +11.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 476 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +11.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 507 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +11.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 761 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +11.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 668 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +10.1) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 454 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +12.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 598 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +14.3) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 448 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +12.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 614 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +12.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 232 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 582 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +11.9) ⚠ cell-cycle shift, explains ~89% of this change | — |
| [[SNU-423 (line)]] | alt | 520 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +11.8) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 281 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.21× (z +8.9) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 465 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +8.5) ⚠ cell-cycle shift, explains ~89% of this change | — |
| [[CHP-212 (line)]] | wt | 511 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +10.3) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 478 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 568 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 810 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +12.2) | — |
| [[RKO (line)]] | wt | 591 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +11.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 510 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 438 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +9.1) ⚠ cell-cycle shift, explains ~89% of this change | — |
| [[SW1417 (line)]] | alt | 472 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +12.0) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 575 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +9.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 806 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 549 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 383 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 503 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 522 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 366 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11170), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPA1]] | +0.74 | +0.62 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 923 |
| [[RPL14]] | +0.73 | +0.67 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 706 |
| [[EEF2]] | +0.72 | +0.69 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 538 |
| [[PCBP2]] | +0.68 | +0.67 / +0.69 | both halves | 7e-06 | pathway: SARS-CoV-1 Infection |
| [[RPL3]] | +0.65 | +0.54 / +0.71 | both halves | 1e-05 | STRING 727 |
| [[NAP1L1]] | +0.65 | +0.57 / +0.72 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 827 |
| [[EEF1B2]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 749 |
| [[EIF4B]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[NACA]] ⚠ | +0.61 | +0.59 / +0.56 | both halves | 1e-05 | STRING 424; ⚠ in the vector space only through flagged drug-doses |
| [[MATR3]] | +0.61 | +0.68 / +0.53 | both halves | 1e-05 | STRING 508 |
| [[RSL1D1]] | +0.61 | +0.69 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 606 |
| [[RPS2]] | +0.61 | +0.52 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 517 |
| [[RPS7]] | +0.59 | +0.47 / +0.65 | both halves | 2e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 670 |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCAF15]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[PCSK7]] | -0.48 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[TMED1]] | -0.47 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[POLR2K]] | -0.47 | -0.28 / -0.42 | both halves | 3e-04 | pathway: Chromosome Maintenance |
| [[ZNF530]] | -0.45 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[RAB5IF]] | -0.45 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[FEN1]] | -0.45 | -0.42 / -0.40 | both halves | 5e-05 | pathway: Chromosome Maintenance |
| [[SLC25A44]] | -0.44 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[COPS9]] | -0.44 | -0.50 / -0.37 | both halves | 7e-05 |  |
| [[VPS45]] | -0.44 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[MYCBP]] | -0.43 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[DYNLT1]] | -0.43 | -0.51 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EEF1G]] | C | EEF1G's natural level weakens NPM1's drug response | EEF1G's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.15; direction not clear | 0.043 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[HNRNPA1]] | C | HNRNPA1's natural level weakens NPM1's drug response | HNRNPA1's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.01; direction not clear | 0.076 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.431). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-30.5, -25.6); signed map (-22.8, -33.4). **Vector** length 97.6, 46.9% of its response variance represented; |z| ≥ 3 in 989 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +1.5 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.2 | -0.1 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +3.0 | +0.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +2.8 | -0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +3.3 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.6 | -1.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -7.6 | -0.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | -6.4 | +3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | +1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | -4.4 | +3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.5 | +0.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -1.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.1 | +1.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | nucleophosmin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.1 — chr5:171,387,116-171,411,810 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B23, NPM |
| Hallmark sets | MYC_TARGETS_V2, UNFOLDED_PROTEIN_RESPONSE, ALLOGRAFT_REJECTION, MYC_TARGETS_V1 |
| Reactome | 29 pathways, smallest: TFAP2A acts as a transcriptional repressor during retinoic acid induced cell differentiation; ALK mutants bind TKIs; TP53 regulates transcription of additional cell cycle genes whose exact role in the p53 pathway remain uncertain |
| Matched by | ensembl_id |

**Function**, from UniProt [P06748](https://www.uniprot.org/uniprotkb/P06748) (Nucleophosmin):

> Involved in diverse cellular processes such as ribosome biogenesis, centrosome duplication, protein chaperoning, histone assembly, cell proliferation, and regulation of tumor suppressors p53/TP53 and ARF. Binds ribosome presumably to drive ribosome nuclear export. Associated with nucleolar ribonucleoprotein structures and bind single-stranded nucleic acids. Acts as a chaperonin for the core histones H3, H2B and H4. Stimulates APEX1 endonuclease activity on apurinic/apyrimidinic (AP) …

**Summary**, from NCBI Gene [4869](https://www.ncbi.nlm.nih.gov/gene/4869):

> The protein encoded by this gene is involved in several cellular processes, including centrosome duplication, protein chaperoning, and cell proliferation. The encoded phosphoprotein shuttles between the nucleolus, nucleus, and cytoplasm, chaperoning ribosomal proteins and core histones from the nucleus to the cytoplasm. This protein is also known to sequester the tumor suppressor ARF in the nucleolus, protecting it from degradation until it is needed. Mutations in this gene are associated with …

**Accessions** — [HGNC:7910](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7910) · Entrez [4869](https://www.ncbi.nlm.nih.gov/gene/4869) · UniProt [P06748](https://www.uniprot.org/uniprotkb/P06748) · Ensembl [ENSG00000181163](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181163)

## Data

Gene col 11170: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11170); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11170, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11170]; `tensor/DDL_lfc|DDL_z.npy` [11170]; `embed/gene_vectors.npy` [11170]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11170 or target_col == 11170). Every well: [[NPM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
