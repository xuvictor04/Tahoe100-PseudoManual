---
symbol: "NUP42"
type: "gene"
col: 5841
ensembl_id: "ENSG00000136243"
name: "nucleoporin 42"
location: "7p15.3"
module: 4
arm: "+"
pooled_cpm: 31.16
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# NUP42

*nucleoporin 42* — 7p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 2.64× (z +17.0, q 0e+00, up in 34 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.34× (z +5.5, q 2e-06, up in 21 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SK-MEL-2 0.259×, C32 0.270×, SNU-1 0.223×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.464×, AN3 CA 0.280×; ⚠ cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SHP-77 0.270×; ⚠ toxic; cell-cycle shift, explains ~21% of this change); [[Pemetrexed (drug)]] 5 µM in 1 line (SNU-423 0.205×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEX26]] (+0.73, fdr 7e-06), [[TMEM138]] (+0.73, fdr 7e-06), [[GFM1]] (+0.65, fdr 7e-06); moves opposite to [[KDM5B]] (-0.58, fdr 2e-05), [[FAM53C]] (-0.58, fdr 1e-05), [[ING1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 16 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5841.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.64×** | +17.0 | 0e+00 | 34/42 (NCI-H2030, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +15.5 | 0e+00 | 30/38 (HOP62, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.06×** | +13.7 | 2e-40 | 38/46 (HOP62, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +12.8 | 4e-35 | 44/47 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.46×** | +7.1 | 1e-10 | 31/48 (NCI-H460, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.43×** | +6.8 | 1e-09 | 25/48 (HT-29, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.42×** | +6.6 | 3e-09 | 28/48 (SNU-423, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +5.9 | 3e-07 | 27/47 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +5.5 | 2e-06 | 21/48 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +5.5 | 2e-06 | 23/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.72×** | +5.4 | 4e-06 | 15/34 (HOP62, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +5.1 | 1e-05 | 23/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +5.0 | 2e-05 | 21/48 (LS 180, LoVo, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.29×** | +4.9 | 5e-05 | 21/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +4.8 | 5e-05 | 20/48 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.001 | 17/48 (LS 180, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +4.1 | 0.001 | 17/48 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.51×** | +4.0 | 0.002 | 15/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.22×** | +3.7 | 0.005 | 19/48 (LS 180, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.45×** | +3.7 | 0.006 | 13/48 (NCI-H460, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.014 | 8/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.020 | 9/48 (NCI-H460, SW480, …) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.39×** | +3.3 | 0.022 | 9/48 (SW 900, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.035 | 4/48 (PANC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.037 | 7/48 (SW 900, NCI-H23, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.35×** | +3.0 | 0.054 | 12/48 (KATO III, SW1417, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5841.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SK-MEL-2 0.259×, C32 0.270×, SNU-1 0.223×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.464×, AN3 CA 0.280×; ⚠ cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SHP-77 0.270×; ⚠ toxic; cell-cycle shift, explains ~21% of this change); [[Pemetrexed (drug)]] 5 µM in 1 line (SNU-423 0.205×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.832× | -3.3 | 0.33 | 21/48 (SK-MEL-2, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Malotilate (drug)]] 0.05 µM |  | 0.843× | -3.2 | 0.33 | 15/48 (SW480, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5841. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 26.8 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.28× (z +14.4) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 18.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.4× (z +17.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 46.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.63× (z +12.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 34.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +12.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 35.5 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.77× (z +10.6) ⚠ toxic; transcription drop | [[AZD2858 (drug)]] 0.5 µM 0.126× (z -9.0) ⚠ toxic · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -8.6) |
| [[SW 900 (line)]] | alt | 27.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +10.3) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 44.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 20.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.9× (z +11.8) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 36.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.88× (z +9.0) ⚠ toxic; transcription drop | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 12.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.62× (z +10.7) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 40.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.75× (z +12.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 22.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.87× (z +12.2) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 34.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.97× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 39.8 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -10.3) |
| [[SW1417 (line)]] | alt | 38.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +11.0) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 53.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.39× (z +11.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 63.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 29.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.30× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 36.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.63× (z +13.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 18.6 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.25× (z +8.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[Panc 03.27 (line)]] | alt | 23.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.68× (z +11.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 33.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +10.7) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 53.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.270× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~21% of this change |
| [[SNU-423 (line)]] | alt | 16.9 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.205× (z -9.7) |
| [[A-172 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 54.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5841), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX26]] | +0.73 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[TMEM138]] | +0.73 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[GFM1]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[TMEM33]] | +0.63 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[COMT]] | +0.63 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[TIMM23B]] | +0.62 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[NADK]] | +0.61 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[ERCC8]] | +0.60 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[SENP3]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[TANGO6]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[MED9]] | +0.58 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[EFTUD2]] | +0.58 | +0.43 / +0.61 | both halves | 3e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM5B]] | -0.58 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[FAM53C]] | -0.58 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ING1]] | -0.57 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[GTF2B]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 | pathway: HIV Infection |
| [[DDIT3]] | -0.54 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[MORF4L2]] | -0.54 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[SHOC2]] | -0.52 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[YIPF3]] | -0.51 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[MYLIP]] | -0.51 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[CDKL5]] | -0.51 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[FSCN1]] | -0.50 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[GALE]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.526). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-17.3, -30.7); signed map (-8.6, -42.5). **Vector** length 93.9, 20.4% of its response variance represented; |z| ≥ 3 in 872 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.9 | +17.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.1 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +13.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +15.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.5 | +5.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.3 | +3.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +4.1 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.9 | -0.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -0.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.8 | -0.9 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -2.4 | -2.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.1 | -0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | nucleoporin 42 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.3 — chr7:23,181,841-23,201,011 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NLP_1, CG1, hCG1, H_RG271G13.9; previously NUPL2 |
| Gene groups (HGNC) | Zinc fingers CCCH-type |
| Reactome | 69 pathways, smallest: IP3 and IP4 transport between cytosol and nucleus; IP6 and IP7 transport between cytosol and nucleus; IPs transport between nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [O15504](https://www.uniprot.org/uniprotkb/O15504) (Nucleoporin NUP42):

> Required for the export of mRNAs containing poly(A) tails from the nucleus into the cytoplasm.; (Microbial infection) In case of infection by HIV-1, it may participate in the docking of viral Vpr at the nuclear envelope.

**Summary**, from NCBI Gene [11097](https://www.ncbi.nlm.nih.gov/gene/11097):

> Enables nuclear export signal receptor activity. Involved in protein export from nucleus. Located in nuclear membrane and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17010](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17010) · Entrez [11097](https://www.ncbi.nlm.nih.gov/gene/11097) · UniProt [O15504](https://www.uniprot.org/uniprotkb/O15504) · Ensembl [ENSG00000136243](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136243)

## Data

Gene col 5841: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5841); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5841, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5841]; `tensor/DDL_lfc|DDL_z.npy` [5841]; `embed/gene_vectors.npy` [5841]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5841 or target_col == 5841). Every well: [[NUP42 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUP42.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
