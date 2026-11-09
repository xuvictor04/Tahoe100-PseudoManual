---
symbol: "TBC1D4"
type: "gene"
col: 5814
ensembl_id: "ENSG00000136111"
name: "TBC1 domain family member 4"
location: "13q22.2"
module: 18
arm: "+"
pooled_cpm: 78.87
n_lines_expressing: 45
n_dd_up: 12
n_dd_down: 14
n_dd_up_clean: 10
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# TBC1D4

*TBC1 domain family member 4* — 13q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.47× (z +12.0, q 3e-30, up in 29 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.462× (z -23.9, q 0e+00, down in 34 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PALS2]] (+0.68, fdr 7e-06), [[UCK2]] (+0.61, fdr 1e-05), [[GMPS]] (+0.60, fdr 1e-05); moves opposite to [[BBS1]] (-0.61, fdr 1e-05), [[NFKBIL1]] (-0.60, fdr 1e-05), [[ATG4D]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[ANKH]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5814.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +12.0 | 3e-30 | 29/44 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +11.8 | 8e-30 | 32/42 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +8.9 | 7e-17 | 27/43 (HEC-1-A, NCI-H1573, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +7.2 | 8e-11 | 30/45 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.86×** | +7.1 | 2e-10 | 26/44 (LoVo, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +7.1 | 2e-10 | 25/43 (NCI-H1573, J82, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +6.5 | 7e-09 | 26/43 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +6.1 | 9e-08 | 24/44 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +5.0 | 4e-05 | 23/42 (COLO 205, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.24×** | +4.7 | 1e-04 | 18/43 (Panc 03.27, AsPC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.22×** | +4.3 | 0.001 | 20/42 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.018 | 13/43 (C32, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 1.11× | +3.1 | 0.085 | 8/44 (A498, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5814.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.462×** | -23.9 | 0e+00 | 34/43 (HepG2/C3A, SW48, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.437×** | -17.4 | 0e+00 | 36/43 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.390×** | -10.8 | 8e-25 | 34/44 (RKO, Panc 03.27, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.633×** | -10.0 | 2e-21 | 28/43 (A-427, SW48, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.698×** | -7.9 | 3e-13 | 26/43 (RKO, LoVo, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.720×** | -6.8 | 1e-09 | 31/43 (A498, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.737×** | -6.7 | 2e-09 | 23/43 (HT-29, HCT15, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.731×** | -6.6 | 2e-09 | 21/38 (CHP-212, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.740×** | -6.6 | 2e-09 | 22/43 (SW48, A498, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.759×** | -6.0 | 8e-08 | 26/43 (A-172, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~21% of this change | **0.771×** | -5.7 | 6e-07 | 27/41 (SW480, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.776×** | -5.6 | 1e-06 | 22/42 (RKO, SW48, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.783×** | -5.4 | 3e-06 | 23/43 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.826×** | -4.0 | 0.002 | 19/42 (NCI-H2030, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.889× | -3.7 | 0.010 | 14/43 (HCT15, LoVo, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.857× | -3.4 | 0.025 | 13/43 (RKO, PANC-1, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.858× | -3.4 | 0.026 | 13/43 (SW 1088, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5814. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 140 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -22.9) |
| [[HEC-1-A (line)]] | alt | 38.0 | 1 | 6 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.94× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -17.9) |
| [[HepG2_C3A (line)]] | wt | 144 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -24.9) |
| [[LoVo (line)]] | wt | 94.1 | 2 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +16.8) | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 139 | 2 (2 ⚠) | 3 | [[Niclosamide (olamine) (drug)]] 5 µM 2.53× (z +11.1) ⚠ toxic; cell-cycle shift, explains ~4% of this change | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -23.5) |
| [[PANC-1 (line)]] | alt | 56.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -16.6) |
| [[SW48 (line)]] | wt | 199 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -24.6) |
| [[A-172 (line)]] | wt | 42.7 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +12.3) | [[Ixazomib citrate (drug)]] 5 µM 0.273× (z -11.6) |
| [[A549 (line)]] | wt | 59.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -23.4) |
| [[C32 (line)]] | wt | 167 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +16.6) | — |
| [[CHP-212 (line)]] | wt | 126 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -16.8) |
| [[Hs 766T (line)]] | wt | 115 | 2 (2 ⚠) | 2 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.53× (z +9.1) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -18.3) |
| [[HT-29 (line)]] | alt | 92.1 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +16.6) | [[Auranofin (drug)]] 5 µM 0.369× (z -11.3) |
| [[LS 180 (line)]] | wt | 111 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +14.8) | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 54.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -17.8) |
| [[NCI-H2030 (line)]] | alt | 67.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -18.1) |
| [[Panc 03.27 (line)]] | alt | 71.1 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -14.4) |
| [[SW480 (line)]] | alt | 93.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -14.5) |
| [[C-33 A (line)]] | alt | 79.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -12.6) |
| [[NCI-H2347 (line)]] | alt | 53.2 | 1 (1 ⚠) | 2 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.07× (z +8.6) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 66.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -15.9) |
| [[A498 (line)]] | wt | 111 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.464× (z -9.9) |
| [[HCT15 (line)]] | alt | 240 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -13.0) |
| [[HOP62 (line)]] | alt | 48.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +13.0) | — |
| [[hTERT-HPNE (line)]] | wt | 70.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +9.3) | [[Docetaxel (drug)]] 0.05 µM 0.336× (z -8.8) ⚠ transcription drop; cell-cycle shift, explains ~21% of this change |
| [[LOX-IMVI (line)]] | wt | 97.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -18.5) |
| [[NCI-H23 (line)]] | alt | 61.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.242× (z -11.5) |
| [[SW 900 (line)]] | alt | 105 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -10.4) |
| [[A-427 (line)]] | wt | 54.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0955× (z -23.3) |
| [[AsPC-1 (line)]] | alt | 89.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.317× (z -9.6) |
| [[BT-474 (line)]] | alt | 78.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -13.0) |
| [[COLO 205 (line)]] | alt | 41.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.03× (z +14.8) | — |
| [[H4 (line)]] | wt | 28.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -9.0) |
| [[J82 (line)]] | alt | 118 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.06× (z +8.5) ⚠ toxic; cell-cycle shift, explains ~4% of this change | — |
| [[SNU-1 (line)]] | wt | 37.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -12.0) |
| [[SW 1271 (line)]] | alt | 52.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0734× (z -8.5) |
| [[SW1417 (line)]] | alt | 75.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.423× (z -8.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.22 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5814), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PALS2]] | +0.68 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[UCK2]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[GMPS]] | +0.60 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[TMTC4]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ABCC4]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[PKP4]] | +0.57 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[PRPS2]] | +0.56 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[CCDC88C]] | +0.56 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[HACD3]] | +0.56 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[CHD7]] | +0.56 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[POLR3G]] | +0.56 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[DOCK9]] | +0.55 | +0.53 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BBS1]] | -0.61 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[NFKBIL1]] | -0.60 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[ATG4D]] | -0.58 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[NPHP1]] | -0.58 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[KAT5]] | -0.57 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[RBSN]] | -0.57 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[STK16]] | -0.57 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[AZI2]] | -0.57 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[DNAL4]] | -0.57 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[TMEM254]] | -0.57 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[RNF40]] | -0.57 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[CHMP4A]] | -0.56 | -0.51 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TBC1D4's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKH]] | B | TBC1D4 activity raises ANKH's level | lines that do not express TBC1D4 (5) vs lines expressing it (45) | 3.24× lower at baseline in the lines without TBC1D4 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZC3H12C, ZNF827 |
| cells under [[NVP-BHG712 (drug)]] 5 µM | B | TBC1D4 activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express TBC1D4 (5) vs lines expressing it (43) | the lines without TBC1D4: 0.80× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: ZC3H12C, ZNF827 |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.570). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-29.1, 1.4); signed map (-4.8, -54.2). **Vector** length 116, 30.5% of its response variance represented; |z| ≥ 3 in 1,219 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +12.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +7.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +11.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~4% of this change | +6.4 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +8.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +3.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +1.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.5 | +3.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.1 | -23.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.3 | -17.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -2.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.3 | -10.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -6.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.9 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -6.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.6 | -0.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q22.2 — chr13:75,283,503-75,482,169 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0603, AS160, DKFZp779C0666 |
| Gene groups (HGNC) | TBC1 domain family members |
| Reactome | 3 pathways, smallest: Translocation of SLC2A4 (GLUT4) to the plasma membrane; Membrane Trafficking; Vesicle-mediated transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O60343](https://www.uniprot.org/uniprotkb/O60343) (TBC1 domain family member 4):

> May act as a GTPase-activating protein for RAB2A, RAB8A, RAB10 and RAB14. Isoform 2 promotes insulin-induced glucose transporter SLC2A4/GLUT4 translocation at the plasma membrane, thus increasing glucose uptake.

**Summary**, from NCBI Gene [9882](https://www.ncbi.nlm.nih.gov/gene/9882):

> This gene is a member of the Tre-2/BUB2/CDC16 domain family. The protein encoded by this gene is a Rab-GTPase-activating protein, and contains two phopshotyrosine-binding domains (PTB1 and PTB2), a calmodulin-binding domain (CBD), a Rab-GTPase domain, and multiple AKT phosphomotifs. This protein is thought to play an important role in glucose homeostasis by regulating the insulin-dependent trafficking of the glucose transporter 4 (GLUT4), important for removing glucose from the bloodstream into …

**Accessions** — [HGNC:19165](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19165) · Entrez [9882](https://www.ncbi.nlm.nih.gov/gene/9882) · UniProt [O60343](https://www.uniprot.org/uniprotkb/O60343) · Ensembl [ENSG00000136111](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136111)

## Data

Gene col 5814: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5814); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5814, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5814]; `tensor/DDL_lfc|DDL_z.npy` [5814]; `embed/gene_vectors.npy` [5814]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5814 or target_col == 5814). Every well: [[TBC1D4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
