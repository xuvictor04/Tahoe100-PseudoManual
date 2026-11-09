---
symbol: "CENATAC"
type: "gene"
col: 11785
ensembl_id: "ENSG00000186166"
name: "centrosomal AT-AC splicing factor"
location: "11q23.3"
module: 64
arm: "+"
pooled_cpm: 35.92
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 1
n_dd_up_clean: 24
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# CENATAC

*centrosomal AT-AC splicing factor* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (9 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.73× (z +19.8, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.669× (z -11.1, q 8e-26, down in 38 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (HS-578T 0.287×, NCI-H1792 0.274×, SW480 0.480×, RPMI-7951 0.280×, …); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RKO 0.230×, A-427 0.281×, SHP-77 0.304×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.213×, SNU-1 0.213×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.349×).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUDT9]] (+0.64, fdr 7e-06), [[BLMH]] (+0.56, fdr 1e-05), [[CAP2]] (+0.55, fdr 1e-05); moves opposite to [[CXCR4]] (-0.51, fdr 5e-05), [[IVNS1ABP]] (-0.51, fdr 2e-05), [[KLHL15]] (-0.50, fdr 7e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11785.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.73×** | +19.8 | 0e+00 | 47/48 (RKO, PANC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.10×** | +14.7 | 0e+00 | 39/47 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.69×** | +14.3 | 4e-44 | 33/47 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.88×** | +12.5 | 2e-33 | 40/48 (A498, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.74×** | +11.0 | 6e-26 | 39/48 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +10.8 | 2e-25 | 30/47 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.72×** | +10.7 | 1e-24 | 38/48 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.72×** | +10.6 | 1e-24 | 39/48 (PANC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.68×** | +10.2 | 1e-22 | 38/48 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +9.9 | 4e-21 | 32/45 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.63×** | +9.2 | 3e-18 | 34/48 (NCI-H2347, A498, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +9.1 | 6e-18 | 25/41 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.55×** | +8.0 | 8e-14 | 28/44 (LS 180, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +6.5 | 2e-09 | 25/48 (Hs 766T, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +6.5 | 3e-09 | 26/48 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.55×** | +6.2 | 2e-08 | 26/48 (A498, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +6.0 | 7e-08 | 27/47 (HT-29, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.77×** | +5.3 | 4e-06 | 26/48 (HT-29, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11785.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (HS-578T 0.287×, NCI-H1792 0.274×, SW480 0.480×, RPMI-7951 0.280×, …); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RKO 0.230×, A-427 0.281×, SHP-77 0.304×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.213×, SNU-1 0.213×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.349×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.669×** | -11.1 | 8e-26 | 38/48 (HS-578T, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Terfenadine (drug)]] 0.5 µM |  | 0.860× | -3.0 | 0.73 | 14/48 (NCI-H460, NCI-H661, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11785. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 54.5 | 7 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +18.6) | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -13.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 53.9 | 7 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -12.2) |
| [[NCI-H2347 (line)]] | alt | 40.5 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.43× (z +12.2) | — |
| [[KATO III (line)]] | alt | 76.1 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -10.4) |
| [[A-172 (line)]] | wt | 24.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +16.8) | — |
| [[PANC-1 (line)]] | alt | 46.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +21.5) | — |
| [[SNU-1 (line)]] | wt | 125 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -11.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 12.1 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.84× (z +12.8) | — |
| [[LOX-IMVI (line)]] | wt | 35.2 | 3 | 1 | [[Auranofin (drug)]] 5 µM 4.12× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -11.6) |
| [[LS 180 (line)]] | wt | 32.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +10.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 22.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.25× (z +18.8) | — |
| [[SW1417 (line)]] | alt | 73.6 | 3 | 1 | [[Ixazomib citrate (drug)]] 5 µM 3.10× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -8.8) |
| [[A-427 (line)]] | wt | 35.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.61× (z +21.5) | [[Dinaciclib (drug)]] 0.05 µM 0.281× (z -9.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 60.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.32× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -10.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 32.9 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.21× (z +11.2) | — |
| [[HOP62 (line)]] | alt | 20.2 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.30× (z +11.3) | — |
| [[LoVo (line)]] | wt | 26.0 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.00× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 24.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.91× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 31.5 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.49× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -14.7) |
| [[HT-29 (line)]] | alt | 28.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +14.2) | — |
| [[NCI-H2030 (line)]] | alt | 58.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +13.7) | — |
| [[NCI-H23 (line)]] | alt | 42.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +19.3) | — |
| [[NCI-H460 (line)]] | wt | 35.5 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.29× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -11.2) |
| [[SHP-77 (line)]] | alt | 38.9 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.29× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.304× (z -9.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 24.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +12.8) | — |
| [[AsPC-1 (line)]] | alt | 20.9 | 1 | 0 | [[Belinostat (drug)]] 5 µM 3.94× (z +8.5) | — |
| [[C32 (line)]] | wt | 19.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -8.8) |
| [[COLO 205 (line)]] | alt | 21.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -8.5) |
| [[Hs 766T (line)]] | wt | 26.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 32.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -14.4) |
| [[RPMI-7951 (line)]] | alt | 29.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -12.2) |
| [[SK-MEL-2 (line)]] | alt | 16.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -10.9) |
| [[SW 900 (line)]] | alt | 38.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.80× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11785), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT9]] | +0.64 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[BLMH]] | +0.56 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[CAP2]] | +0.55 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[ZFP82]] | +0.55 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[NSFL1C]] | +0.53 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[DNAJC7]] | +0.52 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[ZNF567-DT]] | +0.52 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[USP14]] | +0.51 | +0.37 / +0.54 | both halves | 7e-05 |  |
| [[ZNF583]] | +0.51 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[PSMD11]] | +0.51 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[UBE2K]] | +0.50 | +0.31 / +0.56 | both halves | 2e-04 |  |
| [[ZNF527]] | +0.50 | +0.29 / +0.58 | both halves | 3e-04 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CXCR4]] | -0.51 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[IVNS1ABP]] | -0.51 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[KLHL15]] | -0.50 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[INTS6L]] | -0.49 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[POLR2A]] | -0.48 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[GTF2B]] | -0.47 | -0.32 / -0.46 | both halves | 1e-04 |  |
| [[RSPRY1]] | -0.46 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[IKZF4]] | -0.45 | -0.16 / -0.49 | ⚠ not reproduced | 0.001 |  |
| [[HERPUD2]] | -0.45 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[IQCD]] | -0.45 | -0.24 / -0.39 | both halves | 5e-04 |  |
| [[TOB2]] | -0.44 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[PHC2-AS1]] | -0.44 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[TMTC2]] | -0.43 | -0.41 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.514). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-21.1, -7.3); signed map (-24.8, -21.2). **Vector** length 112, 29.5% of its response variance represented; |z| ≥ 3 in 1,213 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.2 | +19.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.0 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +9.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.8 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +8.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.5 | +6.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +3.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -12.3 | -11.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.0 | -2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -1.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -2.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.9 | -1.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | +0.7 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | -1.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | centrosomal AT-AC splicing factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:118,998,138-119,015,793 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DLNB14; previously CCDC84 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UT8](https://www.uniprot.org/uniprotkb/Q86UT8) (Centrosomal AT-AC splicing factor):

> Component of the minor spliceosome that promotes splicing of a specific, rare minor intron subtype. Negative regulator of centrosome duplication. Constrains centriole number by modulating the degradation of the centrosome-duplication-associated protein SASS6 in an acetylation-dependent manner. SIRT1 deacetylates CENATAC in G1 phase, allowing for SASS6 accumulation on the centrosome and subsequent procentriole assembly. The CENATAC acetylation level is restored in mitosis by NAT10, promoting …

**Summary**, from NCBI Gene [338657](https://www.ncbi.nlm.nih.gov/gene/338657):

> This gene encodes a protein thought to contain a coiled coil motif. No function has been determined for the encoded protein. A pseudogene of this gene is located on chromosome 20. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:30460](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30460) · Entrez [338657](https://www.ncbi.nlm.nih.gov/gene/338657) · UniProt [Q86UT8](https://www.uniprot.org/uniprotkb/Q86UT8) · Ensembl [ENSG00000186166](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186166)

## Data

Gene col 11785: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11785); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11785, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11785]; `tensor/DDL_lfc|DDL_z.npy` [11785]; `embed/gene_vectors.npy` [11785]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11785 or target_col == 11785). Every well: [[CENATAC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CENATAC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
