---
symbol: "ANKUB1"
type: "gene"
col: 13039
ensembl_id: "ENSG00000206199"
name: "ankyrin repeat and ubiquitin domain containing 1"
location: "3q25.1"
module: 15
arm: "+"
pooled_cpm: 49.91
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 17
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ANKUB1

*ankyrin repeat and ubiquitin domain containing 1* — 3q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.10× (z +16.3, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.567× (z -8.8, q 8e-16, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C9orf24]] (+0.66, fdr 7e-06), [[PHTF1]] (+0.63, fdr 8e-06), [[CTC-338M12.4]] (+0.59, fdr 2e-05); moves opposite to [[PKN2]] (-0.54, fdr 5e-05), [[TMEM14C]] (-0.54, fdr 2e-05), [[IFTAP]] (-0.50, fdr 3e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13039.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +16.3 | 0e+00 | 43/48 (Panc 03.27, HT-29, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.86×** | +9.6 | 1e-19 | 38/48 (LoVo, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.70×** | +8.3 | 2e-14 | 38/48 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.74×** | +8.1 | 5e-14 | 34/48 (LoVo, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.69×** | +8.1 | 6e-14 | 37/48 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.6 | 5e-04 | 22/48 (SHP-77, BT-474, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.50×** | +4.5 | 6e-04 | 24/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.33×** | +4.4 | 6e-04 | 23/47 (LoVo, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.004 | 21/48 (HS-578T, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | 1.22× | +3.1 | 0.12 | 12/48 (A498, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13039.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.567×** | -8.8 | 8e-16 | 35/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.703×** | -7.7 | 3e-12 | 29/48 (A-172, HOP62, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.654×** | -6.6 | 8e-09 | 32/48 (HOP62, AN3 CA, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.662×** | -6.4 | 2e-08 | 29/48 (NCI-H1573, HOP62, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.658×** | -6.2 | 5e-08 | 32/48 (AN3 CA, A-172, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.702×** | -5.5 | 4e-06 | 28/48 (HOP62, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.742×** | -4.6 | 3e-04 | 23/48 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.746×** | -4.5 | 4e-04 | 23/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.746×** | -4.5 | 4e-04 | 25/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.748×** | -4.5 | 4e-04 | 22/48 (SW 900, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.744×** | -4.4 | 5e-04 | 24/47 (BT-474, SNU-1, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -4.3 | 8e-04 | 3/49 (KATO III, SW1417, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.772×** | -3.8 | 0.005 | 22/48 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.785×** | -3.7 | 0.007 | 20/48 (NCI-H460, NCI-H1573, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.810×** | -3.3 | 0.042 | 16/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.817×** | -3.1 | 0.064 | 8/48 (J82, SW 900, …) | inconsistent across doses |  |
| [[Methylthiouracil (drug)]] 5 µM |  | **0.819×** | -3.1 | 0.067 | 7/48 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Uridine (drug)]] 5 µM |  | **0.824×** | -3.0 | 0.087 | 7/48 (A-427, C-33 A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13039. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 43.5 | 7 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +12.1) | — |
| [[NCI-H1573 (line)]] | alt | 74.1 | 1 | 6 (5 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.78× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -13.7) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.270× (z -11.8) |
| [[HOP62 (line)]] | alt | 110 | 1 | 5 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.17× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -19.4) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.327× (z -9.3) |
| [[A-172 (line)]] | wt | 89.2 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -19.6) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.289× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 69.3 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.361× (z -11.0) |
| [[HS-578T (line)]] | alt | 76.0 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -12.1) ⚠ cell-cycle shift, explains ~54% of this change |
| [[NCI-H2347 (line)]] | alt | 25.4 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.42× (z +10.6) | — |
| [[J82 (line)]] | alt | 74.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -10.6) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -9.3) |
| [[PANC-1 (line)]] | alt | 47.6 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +13.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.380× (z -8.9) |
| [[SW 900 (line)]] | alt | 75.3 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.22× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -11.7) ⚠ cell-cycle shift, explains ~54% of this change |
| [[AN3 CA (line)]] | alt | 103 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -16.8) ⚠ cell-cycle shift, explains ~54% of this change |
| [[BT-474 (line)]] | alt | 34.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +13.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0685× (z -16.4) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[C32 (line)]] | wt | 41.0 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.59× (z +11.7) | — |
| [[HEC-1-A (line)]] | alt | 91.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +10.4) | — |
| [[SHP-77 (line)]] | alt | 74.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.17× (z +11.6) | — |
| [[A498 (line)]] | wt | 35.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +11.0) | — |
| [[A549 (line)]] | wt | 35.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +12.4) | — |
| [[C-33 A (line)]] | alt | 74.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.298× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[CFPAC-1 (line)]] | alt | 23.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +11.4) | — |
| [[H4 (line)]] | wt | 105 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -11.3) ⚠ cell-cycle shift, explains ~54% of this change |
| [[HepG2_C3A (line)]] | wt | 45.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.211× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[HT-29 (line)]] | alt | 34.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +14.2) | — |
| [[KATO III (line)]] | alt | 13.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.94× (z +8.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 43.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +13.2) | — |
| [[LS 180 (line)]] | wt | 15.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +9.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 33.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 44.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +10.7) | — |
| [[NCI-H596 (line)]] | alt | 56.0 | 1 | 0 | [[Elimusertib hydrochloride (drug)]] 0.5 µM 2.80× (z +17.5) | — |
| [[Panc 03.27 (line)]] | alt | 29.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.69× (z +16.8) | — |
| [[RKO (line)]] | wt | 26.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.156× (z -10.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[RPMI-7951 (line)]] | alt | 49.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -8.8) ⚠ cell-cycle shift, explains ~54% of this change |
| [[SK-MEL-2 (line)]] | alt | 62.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +8.6) | — |
| [[SNU-1 (line)]] | wt | 49.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0743× (z -13.7) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[SNU-423 (line)]] | alt | 29.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 18.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +13.2) | — |
| [[SW48 (line)]] | wt | 61.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +8.5) | — |
| [[SW480 (line)]] | alt | 26.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +12.2) | — |
| [[A-427 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 81.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 66.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 75.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13039), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C9orf24]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[PHTF1]] | +0.63 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[CTC-338M12.4]] | +0.59 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[NPHP3-ACAD11]] | +0.58 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[SYCE1L]] | +0.57 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[PSMB5]] | +0.57 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[GSK3B-DT]] | +0.57 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[EXOSC3]] | +0.57 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[PEX6]] | +0.56 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[CCDC32]] | +0.55 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[PPP1R26-AS1]] | +0.55 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[PLD5P1]] | +0.55 | +0.36 / +0.47 | both halves | 1e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKN2]] | -0.54 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[TMEM14C]] | -0.54 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[IFTAP]] | -0.50 | -0.27 / -0.47 | both halves | 3e-04 |  |
| [[VPS8]] | -0.50 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[ATG3]] | -0.48 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[C4orf33]] | -0.47 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[CYP2S1]] | -0.47 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[THEM6]] | -0.46 | -0.44 / -0.29 | both halves | 2e-04 |  |
| [[TJP2]] | -0.46 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[BTBD8]] | -0.46 | -0.32 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers ANKUB1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.429). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.4, 19.8); signed map (4.0, -0.4). **Vector** length 125, 34.9% of its response variance represented; |z| ≥ 3 in 967 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +10.5 | +8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.5 | +16.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +10.2 | +9.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.9 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.0 | +8.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.1 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +4.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.9 | +1.6 |
| fall | [[Belumosudil (drug)]] 5 µM |  | -4.3 | -3.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.9 | -6.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.8 | -5.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.5 | -6.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.3 | -4.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.3 | -2.9 |
|  | [[AZD-8055 (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | -2.2 | -2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and ubiquitin domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.1 — chr3:149,761,100-149,968,385 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C3orf16 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

UniProt [A6NFN9](https://www.uniprot.org/uniprotkb/A6NFN9) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:29642](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29642) · Entrez [389161](https://www.ncbi.nlm.nih.gov/gene/389161) · UniProt [A6NFN9](https://www.uniprot.org/uniprotkb/A6NFN9) · Ensembl [ENSG00000206199](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206199)

## Data

Gene col 13039: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13039); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13039, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13039]; `tensor/DDL_lfc|DDL_z.npy` [13039]; `embed/gene_vectors.npy` [13039]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13039 or target_col == 13039). Every well: [[ANKUB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKUB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
