---
symbol: "DLGAP1"
type: "gene"
col: 9977
ensembl_id: "ENSG00000170579"
name: "DLG associated protein 1"
location: "18p11.31"
module: 75
arm: "+"
pooled_cpm: 50.09
n_lines_expressing: 44
n_dd_up: 27
n_dd_down: 6
n_dd_up_clean: 21
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# DLGAP1

*DLG associated protein 1* — 18p11.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.24× (z +29.1, q 0e+00, up in 35 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.905× (z -6.2, q 4e-07, down in 5 of 43 measured lines) ⚠ position not correctable. The strongest without an alert is [[Digitoxin (drug)]] 0.05 µM: 0.768× (z -4.6, q 0.001, down in 16 of 41 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLCO5A1]] (+0.65, fdr 2e-05), [[LINC00513]] (+0.63, fdr 1e-05), [[MYO16]] (+0.63, fdr 4e-05); moves opposite to [[PXMP4]] (-0.57, fdr 1e-04), [[WRAP73]] (-0.56, fdr 5e-05), [[HAUS3]] (-0.54, fdr 2e-04).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PEBP4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9977.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.24×** | +29.1 | 0e+00 | 35/41 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.03×** | +27.4 | 0e+00 | 37/42 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.38×** | +21.3 | 0e+00 | 30/38 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.09×** | +18.2 | 0e+00 | 26/34 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.80×** | +17.3 | 0e+00 | 24/33 (A549, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.20×** | +13.8 | 2e-41 | 32/41 (HS-578T, SW48, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.69×** | +9.2 | 3e-18 | 29/42 (HOP62, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +8.8 | 1e-16 | 22/42 (NCI-H23, NCI-H2030, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +8.0 | 6e-14 | 27/41 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.56×** | +7.5 | 4e-12 | 20/41 (HOP62, LoVo, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +6.5 | 5e-09 | 18/42 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +6.0 | 1e-07 | 21/41 (NCI-H23, C32, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +5.4 | 3e-06 | 14/41 (SW1417, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.6 | 2e-04 | 12/43 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.007 | 13/41 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Pralsetinib (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.017 | 4/42 (PANC-1, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.018 | 9/42 (HEC-1-A, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.018 | 8/42 (LoVo, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9977.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -6.2 | 4e-07 | 5/43 (NCI-H23, SW 1088, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.768×** | -4.6 | 0.001 | 16/41 (RPMI-7951, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.774×** | -4.5 | 0.001 | 17/42 (NCI-H460, C-33 A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.775×** | -4.4 | 0.001 | 20/42 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.779×** | -4.3 | 0.002 | 15/41 (NCI-H460, C-33 A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.780×** | -4.1 | 0.004 | 10/42 (SW 1271, HS-578T, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.828×** | -3.3 | 0.087 | 8/42 (SW 1088, NCI-H2030, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.839× | -3.0 | 0.16 | 8/41 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9977. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 23.2 | 10 (4 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 6.69× (z +20.1) | — |
| [[HOP62 (line)]] | alt | 23.6 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.59× (z +22.9) | — |
| [[NCI-H1573 (line)]] | alt | 88.2 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +19.4) | [[Dinaciclib (drug)]] 5 µM 0.0965× (z -19.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 111 | 6 (1 ⚠) | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 5.30× (z +21.4) | [[Dinaciclib (drug)]] 5 µM 0.124× (z -18.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 16.2 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +14.4) | — |
| [[LS 180 (line)]] | wt | 418 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.174× (z -9.9) |
| [[A-172 (line)]] | wt | 12.8 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.60× (z +16.9) | — |
| [[LoVo (line)]] | wt | 18.4 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +14.7) | — |
| [[PANC-1 (line)]] | alt | 17.9 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +22.0) | — |
| [[C32 (line)]] | wt | 14.8 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.39× (z +12.6) | — |
| [[J82 (line)]] | alt | 18.8 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +12.9) | — |
| [[SW480 (line)]] | alt | 26.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +14.6) | — |
| [[A-427 (line)]] | wt | 310 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0329× (z -32.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -13.4) |
| [[A549 (line)]] | wt | 15.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.3× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +11.4) | — |
| [[C-33 A (line)]] | alt | 112 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -11.6) |
| [[HS-578T (line)]] | alt | 17.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +23.1) | — |
| [[LOX-IMVI (line)]] | wt | 17.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +11.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 28.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +13.8) | — |
| [[NCI-H460 (line)]] | wt | 134 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.121× (z -16.7) |
| [[SK-MEL-2 (line)]] | alt | 384 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -9.7) |
| [[SW 900 (line)]] | alt | 14.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.1× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +9.0) | — |
| [[H4 (line)]] | wt | 15.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.32× (z +9.2) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 20.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.89× (z +12.6) | [[Cobimetinib (drug)]] 0.05 µM 0.142× (z -9.1) |
| [[KATO III (line)]] | alt | 19.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 16.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +10.6) | — |
| [[RPMI-7951 (line)]] | alt | 17.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 16.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +14.6) | — |
| [[SW48 (line)]] | wt | 33.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +17.5) | — |
| [[AsPC-1 (line)]] | alt | 16.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +9.9) | — |
| [[HCT15 (line)]] | alt | 16.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +10.9) | — |
| [[HT-29 (line)]] | alt | 24.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +9.5) | — |
| [[RKO (line)]] | wt | 23.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 14.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.13× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 31.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +8.9) | — |
| [[A498 (line)]] | wt | 11.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9977), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLCO5A1]] | +0.65 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[LINC00513]] | +0.63 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[MYO16]] | +0.63 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[GALNT17]] | +0.63 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[RYR2]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[PCDH15]] | +0.62 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[LINC02755]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[CFAP54]] | +0.60 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[LINC00534]] | +0.60 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[CSMD1]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 | STRING 435 |
| [[PDE8B]] | +0.59 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[EYS]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PXMP4]] | -0.57 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[WRAP73]] | -0.56 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[HAUS3]] | -0.54 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[WDR5]] | -0.53 | -0.59 / -0.32 | both halves | 2e-04 |  |
| [[SDHA]] | -0.51 | -0.62 / -0.26 | both halves | 3e-04 |  |
| [[GIT2]] | -0.50 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[SNRNP25]] | -0.50 | -0.46 / -0.25 | both halves | 4e-04 |  |
| [[STUB1]] | -0.50 | -0.43 / -0.20 | both halves | 7e-04 |  |
| [[NUBP2]] | -0.49 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[AP2S1]] | -0.49 | -0.59 / -0.13 | ⚠ one half (not replicated) | 0.002 | pathway: Neuronal System |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises DLGAP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAPK14]] | B | MAPK14 activity raises DLGAP1's level | compounds that target MAPK14: 2 of 2 lower it (PH-797804, Ralimetinib dimesylate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PEBP4]] | B | DLGAP1 activity lowers PEBP4's level | lines that do not express DLGAP1 (6) vs lines expressing it (44) | 1.29× higher at baseline in the lines without DLGAP1 | 0.053 | ⚠ within organs, on part of the lines; also absent: ZSWIM5, LINC00922; maybe low, not absent |

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.636). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.2, 25.1); signed map (35.2, 11.1). **Vector** length 93.0, 19.4% of its response variance represented; |z| ≥ 3 in 933 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.8 | +27.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.6 | +21.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.3 | +29.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.3 | +18.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.3 | +17.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +8.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +6.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.3 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.9 | +1.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.5 | -4.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.3 | -4.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.0 | -4.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.7 | -4.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -1.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | DLG associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.31 — chr18:3,496,032-4,455,307 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GKAP, SAPAP1, DAP-1 |
| Reactome | 3 pathways, smallest: Neurexins and neuroligins; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [O14490](https://www.uniprot.org/uniprotkb/O14490) (DLG-associated protein 1):

> Part of the postsynaptic scaffold in neuronal cells.

**Summary**, from NCBI Gene [9229](https://www.ncbi.nlm.nih.gov/gene/9229):

> Predicted to enable molecular adaptor activity. Predicted to be a structural constituent of postsynaptic density. Predicted to be involved in several processes, including aggresome assembly; protein localization to synapse; and regulation of proteasomal protein catabolic process. Predicted to be located in plasma membrane. Predicted to be active in glutamatergic synapse and postsynaptic density, intracellular component. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:2905](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2905) · Entrez [9229](https://www.ncbi.nlm.nih.gov/gene/9229) · UniProt [O14490](https://www.uniprot.org/uniprotkb/O14490) · Ensembl [ENSG00000170579](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170579)

## Data

Gene col 9977: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9977); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9977, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9977]; `tensor/DDL_lfc|DDL_z.npy` [9977]; `embed/gene_vectors.npy` [9977]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9977 or target_col == 9977). Every well: [[DLGAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DLGAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
