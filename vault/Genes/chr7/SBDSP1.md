---
symbol: "SBDSP1"
type: "gene"
col: 13472
ensembl_id: "ENSG00000225648"
name: "SBDS pseudogene 1"
location: "7q11.23"
module: 25
arm: "+"
pooled_cpm: 11.31
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 3
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# SBDSP1

*SBDS pseudogene 1* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.70× (z +23.5, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.829× (z -6.7, q 1e-08, down in 26 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 0.561× (z -4.4, q 0.003, down in 19 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (NCI-H23 0.0603×); [[Bergenin (drug)]] 0.5 µM in 1 line (NCI-H23 0.0741×); [[XRK3F2 (drug)]] 0.5 µM in 1 line (J82 0.0877×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SBDSP1-1]] (+0.76, fdr 7e-06, ⚠ same locus), [[SBDS]] (+0.71, fdr 7e-06), [[GMFB]] (+0.65, fdr 7e-06), [[TAF9]] (+0.64, fdr 2e-05); moves opposite to [[RNF122]] (-0.61, fdr 1e-05), [[UBL5]] (-0.60, fdr 1e-05), [[COX6A1]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13472.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.70×** | +23.5 | 0e+00 | 45/46 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.99×** | +14.9 | 0e+00 | 32/33 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.96×** | +14.8 | 0e+00 | 45/46 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.35×** | +12.0 | 5e-31 | 25/27 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.95×** | +11.1 | 9e-27 | 18/21 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.75×** | +10.4 | 2e-23 | 41/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.29×** | +8.6 | 9e-16 | 34/40 (NCI-H1792, LoVo, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.13×** | +8.1 | 4e-14 | 36/47 (SW480, KATO III, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.11×** | +8.0 | 8e-14 | 37/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +6.8 | 8e-10 | 23/46 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.79×** | +6.2 | 2e-08 | 25/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.79×** | +6.2 | 2e-08 | 25/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.78×** | +5.8 | 3e-07 | 28/46 (SNU-423, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.72×** | +5.8 | 3e-07 | 27/47 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +5.7 | 3e-07 | 28/44 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.58×** | +4.9 | 4e-05 | 22/47 (SW480, PANC-1, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.34×** | +4.8 | 6e-05 | 26/46 (A498, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.55×** | +4.7 | 8e-05 | 24/44 (SW480, A498, …) | two highest doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +4.5 | 2e-04 | 15/48 (SNU-423, LOX-IMVI, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +4.5 | 2e-04 | 17/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13472.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (NCI-H23 0.0603×); [[Bergenin (drug)]] 0.5 µM in 1 line (NCI-H23 0.0741×); [[XRK3F2 (drug)]] 0.5 µM in 1 line (J82 0.0877×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.829×** | -6.7 | 1e-08 | 26/48 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.561×** | -4.4 | 0.003 | 19/40 (SW480, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.713×** | -3.6 | 0.054 | 18/46 (RKO, SW 900, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Thymol (drug)]] 0.5 µM |  | 0.735× | -3.3 | 0.13 | 21/43 (HS-578T, KATO III, …) | inconsistent across doses | position effect removed |
| [[Cepharanthine (drug)]] 0.5 µM |  | 0.745× | -3.2 | 0.16 | 16/45 (NCI-H1792, H4, …) | inconsistent across doses | position effect removed |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | 0.751× | -3.1 | 0.16 | 10/44 (SW48, HCT15, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.754× | -3.0 | 0.16 | 14/47 (J82, NCI-H460, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.674× | -3.0 | 0.16 | 13/40 (J82, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.820× | -3.0 | 0.16 | 16/48 (SK-MEL-2, SW480, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13472. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 18.3 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +14.2) | — |
| [[LoVo (line)]] | wt | 11.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +14.3) | — |
| [[NCI-H23 (line)]] | alt | 5.28 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +8.5) | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0603× (z -9.7) |
| [[PANC-1 (line)]] | alt | 10.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +14.2) | — |
| [[A498 (line)]] | wt | 21.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +16.4) | — |
| [[A549 (line)]] | wt | 8.37 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.16× (z +12.6) | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.150× (z -8.5) |
| [[J82 (line)]] | alt | 10.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +12.1) | [[XRK3F2 (drug)]] 0.5 µM 0.0877× (z -8.8) |
| [[LS 180 (line)]] | wt | 6.47 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.23× (z +11.5) | — |
| [[NCI-H1573 (line)]] | alt | 7.58 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.68× (z +12.7) | — |
| [[NCI-H460 (line)]] | wt | 7.79 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +11.8) | — |
| [[A-172 (line)]] | wt | 11.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +12.9) | — |
| [[AsPC-1 (line)]] | alt | 17.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.40× (z +14.7) | — |
| [[C32 (line)]] | wt | 7.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.71× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 7.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.01× (z +10.6) | — |
| [[HEC-1-A (line)]] | alt | 17.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +10.3) | — |
| [[HOP62 (line)]] | alt | 7.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +10.5) | — |
| [[Hs 766T (line)]] | wt | 9.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.46× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 10.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 11.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +11.8) | — |
| [[KATO III (line)]] | alt | 13.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.92× (z +14.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.06× (z +12.2) | — |
| [[NCI-H1792 (line)]] | alt | 8.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +10.0) | — |
| [[RKO (line)]] | wt | 12.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +10.8) | — |
| [[SW 900 (line)]] | alt | 10.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 17.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +9.8) | — |
| [[A-427 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13472), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SBDSP1-1]] | +0.76 | +0.76 / +0.74 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[SBDS]] | +0.71 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[GMFB]] | +0.65 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[TAF9]] | +0.64 | +0.72 / +0.47 | both halves | 2e-05 |  |
| [[FLII]] | +0.64 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[IMPACT]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[HDHD2]] | +0.63 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[CCT6P3]] | +0.61 | +0.71 / +0.46 | both halves | 2e-05 |  |
| [[EIF3C]] | +0.61 | +0.45 / +0.72 | both halves | 3e-05 |  |
| [[ZNF326]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[GUF1]] | +0.60 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[ZMPSTE24]] | +0.60 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[MRPL9]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF122]] | -0.61 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[UBL5]] | -0.60 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[COX6A1]] | -0.59 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[SDHAF1]] | -0.58 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[IGFBP2]] | -0.58 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[DTX2P1-UPK3BP1-PMS2P11]] | -0.58 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[RABGEF1P1]] | -0.56 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[SEC61G]] | -0.56 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[NUDT22]] | -0.56 | -0.33 / -0.61 | both halves | 1e-04 |  |
| [[COX6C]] | -0.56 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[C4orf3]] | -0.55 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[COX6B1]] | -0.55 | -0.39 / -0.54 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.556). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-32.9, -18.5); signed map (5.9, -33.9). **Vector** length 66.0, 11.8% of its response variance represented; |z| ≥ 3 in 1,161 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +11.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +23.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.0 | +14.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +8.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.7 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +0.1 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -2.5 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.2 | +3.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.1 | +4.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.1 | +5.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -4.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.5 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | SBDS pseudogene 1 |
| Locus type | pseudogene |
| Location | 7q11.23 — chr7:72,829,656-72,836,701 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously SBDSP |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:21646](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21646) · Entrez [155370](https://www.ncbi.nlm.nih.gov/gene/155370) · Ensembl [ENSG00000225648](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225648)

## Data

Gene col 13472: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13472); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13472, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13472]; `tensor/DDL_lfc|DDL_z.npy` [13472]; `embed/gene_vectors.npy` [13472]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13472 or target_col == 13472). Every well: [[SBDSP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SBDSP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
