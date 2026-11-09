---
symbol: "RCC1"
type: "gene"
col: 11087
ensembl_id: "ENSG00000180198"
name: "regulator of chromosome condensation 1"
location: "1p35.3"
module: 15
arm: "+"
pooled_cpm: 73.41
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# RCC1

*regulator of chromosome condensation 1* — 1p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.04× (z +22.1, q 0e+00, up in 48 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (CHP-212 0.0794×); [[Belinostat (drug)]] 0.5 µM in 1 line (AN3 CA 0.215×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSH4]] (+0.66, fdr 2e-05), [[CCDC62]] (+0.63, fdr 1e-05), [[LINC00880]] (+0.62, fdr 8e-05); moves opposite to [[ISCA2]] (-0.63, fdr 8e-05), [[RFC1]] (-0.58, fdr 6e-05), [[DCTN3]] (-0.58, fdr 6e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11087.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.04×** | +22.1 | 0e+00 | 48/49 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.64×** | +13.9 | 2e-41 | 47/47 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.91×** | +12.0 | 9e-31 | 44/48 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.86×** | +9.8 | 1e-20 | 35/48 (C32, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.34×** | +9.2 | 6e-18 | 37/43 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.29×** | +8.9 | 4e-17 | 46/50 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.67×** | +8.1 | 4e-14 | 43/48 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +7.2 | 6e-11 | 38/44 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +6.6 | 3e-09 | 44/48 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.76×** | +6.4 | 1e-08 | 41/48 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +6.3 | 1e-08 | 32/48 (C32, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +6.3 | 2e-08 | 39/47 (COLO 205, NCI-H460, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.75×** | +6.2 | 2e-08 | 38/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.62×** | +5.4 | 2e-06 | 35/48 (LoVo, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **1.50×** | +4.6 | 2e-04 | 34/47 (SW 900, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **2.14×** | +4.4 | 3e-04 | 38/48 (Panc 03.27, COLO 205, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +4.4 | 4e-04 | 32/48 (NCI-H1792, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +4.2 | 7e-04 | 34/48 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.05×** | +4.2 | 8e-04 | 35/48 (BT-474, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.02×** | +4.1 | 0.001 | 35/48 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.61×** | +3.8 | 0.003 | 28/48 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.92×** | +3.8 | 0.003 | 33/48 (A549, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +3.7 | 0.005 | 30/48 (KATO III, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.42×** | +3.7 | 0.005 | 25/47 (C-33 A, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11087.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (CHP-212 0.0794×); [[Belinostat (drug)]] 0.5 µM in 1 line (AN3 CA 0.215×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.747× | -3.3 | 0.58 | 32/48 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11087. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 38.3 | 9 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +22.6) | — |
| [[LoVo (line)]] | wt | 134 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +19.4) | — |
| [[NCI-H460 (line)]] | wt | 80.5 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +13.1) | — |
| [[SW480 (line)]] | alt | 93.5 | 8 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +14.2) | — |
| [[hTERT-HPNE (line)]] | wt | 48.3 | 7 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.76× (z +16.6) | — |
| [[C32 (line)]] | wt | 42.3 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.5× (z +24.5) | — |
| [[COLO 205 (line)]] | alt | 29.9 | 6 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +11.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 94.6 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.28× (z +16.7) | — |
| [[HEC-1-A (line)]] | alt | 77.8 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +20.4) | — |
| [[HS-578T (line)]] | alt | 68.7 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.46× (z +17.3) | — |
| [[LS 180 (line)]] | wt | 78.0 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 32.0 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +14.1) | — |
| [[PANC-1 (line)]] | alt | 60.6 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +19.0) | — |
| [[HT-29 (line)]] | alt | 76.4 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +12.8) | — |
| [[LOX-IMVI (line)]] | wt | 94.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +12.8) | — |
| [[RKO (line)]] | wt | 118 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +12.9) | — |
| [[RPMI-7951 (line)]] | alt | 56.7 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.61× (z +14.0) | — |
| [[SNU-423 (line)]] | alt | 40.7 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.78× (z +15.8) | — |
| [[A-172 (line)]] | wt | 29.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.90× (z +14.7) | — |
| [[A549 (line)]] | wt | 51.9 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.83× (z +15.8) | — |
| [[CFPAC-1 (line)]] | alt | 34.2 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.38× (z +18.5) | — |
| [[Hs 766T (line)]] | wt | 59.4 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.84× (z +15.5) | — |
| [[J82 (line)]] | alt | 56.1 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +15.2) | — |
| [[KATO III (line)]] | alt | 45.4 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +17.9) | — |
| [[NCI-H1792 (line)]] | alt | 32.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.1× (z +22.4) | — |
| [[Panc 03.27 (line)]] | alt | 44.3 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +16.8) | — |
| [[SW1417 (line)]] | alt | 64.4 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +15.5) | — |
| [[A498 (line)]] | wt | 62.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +15.9) | — |
| [[BT-474 (line)]] | alt | 50.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.90× (z +16.6) | — |
| [[HCT15 (line)]] | alt | 132 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +11.9) | — |
| [[SHP-77 (line)]] | alt | 51.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +12.7) | — |
| [[SK-MEL-2 (line)]] | alt | 71.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +12.7) | — |
| [[AN3 CA (line)]] | alt | 83.0 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.215× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 30.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.84× (z +17.4) | — |
| [[CHP-212 (line)]] | wt | 37.3 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0794× (z -10.0) |
| [[H4 (line)]] | wt | 74.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.96× (z +13.7) | — |
| [[HepG2_C3A (line)]] | wt | 92.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 100 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +10.9) | — |
| [[NCI-H2347 (line)]] | alt | 73.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.57× (z +18.7) | — |
| [[SNU-1 (line)]] | wt | 79.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +11.0) | — |
| [[SW 900 (line)]] | alt | 27.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.20× (z +12.5) | — |
| [[SW48 (line)]] | wt | 136 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +10.6) | — |
| [[A-427 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 272 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11087), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSH4]] | +0.66 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[CCDC62]] | +0.63 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[LINC00880]] | +0.62 | +0.62 / +0.37 | both halves | 8e-05 |  |
| [[GTF3C2-AS2]] | +0.61 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[AGBL3]] | +0.58 | +0.56 / +0.43 | both halves | 4e-05 |  |
| [[SLC13A3]] | +0.57 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[SNHG1]] | +0.57 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[MRPS25]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[GABPB1-AS1]] | +0.57 | +0.53 / +0.35 | both halves | 1e-04 |  |
| [[SNHG10]] | +0.57 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[PCBP1-AS1]] | +0.57 | +0.57 / +0.25 | both halves | 4e-04 |  |
| [[PRC1-AS1]] | +0.56 | +0.55 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISCA2]] | -0.63 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[RFC1]] | -0.58 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[DCTN3]] | -0.58 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[IFT22]] | -0.57 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[SNAP29]] | -0.56 | -0.26 / -0.40 | both halves | 4e-04 |  |
| [[GPATCH11]] | -0.56 | -0.42 / -0.27 | both halves | 3e-04 |  |
| [[MIA3]] | -0.55 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[CYB5R1]] | -0.52 | -0.41 / -0.28 | both halves | 3e-04 |  |
| [[CETN2]] | -0.52 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[ZNF184]] | -0.51 | -0.25 / -0.38 | both halves | 4e-04 |  |
| [[HDGFL2]] | -0.51 | -0.43 / -0.27 | both halves | 3e-04 |  |
| [[INIP]] | -0.50 | -0.30 / -0.35 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RCC1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PLSCR2]] | B | PLSCR2 activity lowers RCC1's level | lines that do not express PLSCR2 (6) vs lines expressing it (44) | 2.00× higher at baseline in the lines without PLSCR2 | 0.063 | ⚠ within organs, on part of the lines; also absent: TRIB1, SLC2A1, CEMIP2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.507). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (26.8, -12.9); signed map (18.2, 2.0). **Vector** length 96.1, 32.2% of its response variance represented; |z| ≥ 3 in 1,119 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.2 | +6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +8.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.6 | +13.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.4 | +3.7 |
|  | [[EX229 (drug)]] 5 µM |  | +4.1 | +4.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.0 | +4.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.6 | +3.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.9 | +0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.3 | +1.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | +1.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.5 | +0.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | +1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -1.9 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | -1.8 | +0.2 |
|  | [[Carbamazepine (drug)]] 5 µM |  | -1.7 | -0.2 |
|  | [[Saquinavir (drug)]] 5 µM |  | -1.7 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | regulator of chromosome condensation 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.3 — chr1:28,505,943-28,539,300 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CHC1 |
| Reactome | 15 pathways, smallest: Postmitotic nuclear pore complex (NPC) reformation; Nuclear import of Rev protein; Rev-mediated nuclear export of HIV RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [P18754](https://www.uniprot.org/uniprotkb/P18754) (Regulator of chromosome condensation):

> Guanine-nucleotide releasing factor that promotes the exchange of Ran-bound GDP by GTP, and thereby plays an important role in RAN-mediated functions in nuclear import and mitosis. Contributes to the generation of high levels of chromosome-associated, GTP-bound RAN, which is important for mitotic spindle assembly and normal progress through mitosis. Via its role in maintaining high levels of GTP-bound RAN in the nucleus, contributes to the release of cargo proteins from importins after nuclear …

**Summary**, from NCBI Gene [1104](https://www.ncbi.nlm.nih.gov/gene/1104):

> Enables several functions, including guanyl-nucleotide exchange factor activity; nucleosomal DNA binding activity; and protein heterodimerization activity. Involved in G1/S transition of mitotic cell cycle; regulation of cell cycle process; and spindle organization. Located in chromatin; cytoplasm; and nuclear lumen. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:1913](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1913) · Entrez [1104](https://www.ncbi.nlm.nih.gov/gene/1104) · UniProt [P18754](https://www.uniprot.org/uniprotkb/P18754) · Ensembl [ENSG00000180198](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180198)

## Data

Gene col 11087: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11087); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11087, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11087]; `tensor/DDL_lfc|DDL_z.npy` [11087]; `embed/gene_vectors.npy` [11087]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11087 or target_col == 11087). Every well: [[RCC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RCC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
