---
symbol: "CTSB"
type: "gene"
col: 8996
ensembl_id: "ENSG00000164733"
name: "cathepsin B"
location: "8p23.1"
module: 50
arm: "+"
pooled_cpm: 159.84
n_lines_expressing: 47
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# CTSB

*cathepsin B* — 8p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.57× (z +18.0, q 0e+00, up in 41 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.37× (z +8.6, q 1e-15, up in 38 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.549× (z -16.2, q 0e+00, down in 37 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IDS]] (+0.66, fdr 1e-05), [[APLP2]] (+0.65, fdr 7e-06), [[GRN]] (+0.63, fdr 7e-06); moves opposite to [[IWS1]] (-0.63, fdr 2e-05), [[PPIG]] (-0.54, fdr 1e-05), [[SREK1]] (-0.52, fdr 3e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[COL6A1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ZC3HC1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8996.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.57×** | +18.0 | 0e+00 | 41/46 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +13.7 | 5e-40 | 37/41 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.84×** | +10.8 | 7e-25 | 38/43 (RPMI-7951, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +8.6 | 1e-15 | 38/45 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +5.5 | 4e-06 | 32/46 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~15% of this change | **1.26×** | +4.4 | 0.001 | 26/45 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.3 | 0.001 | 19/46 (LoVo, SNU-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.005 | 24/45 (SW480, RPMI-7951, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.060 | 18/44 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.2 | 0.065 | 20/45 (HCT15, HS-578T, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.2 | 0.065 | 15/34 (HS-578T, NCI-H2347, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.2 | 0.074 | 19/45 (HepG2/C3A, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8996.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.549×** | -16.2 | 0e+00 | 37/45 (RPMI-7951, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.474×** | -14.3 | 1e-43 | 43/45 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.547×** | -11.5 | 3e-28 | 35/45 (HOP62, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.592×** | -10.0 | 3e-21 | 32/45 (HS-578T, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.632×** | -8.4 | 5e-15 | 37/46 (A-172, HOP62, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.671×** | -7.6 | 3e-12 | 35/45 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.670×** | -7.3 | 2e-11 | 32/45 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.720×** | -6.3 | 3e-08 | 30/45 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.760×** | -5.2 | 1e-05 | 24/45 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.763×** | -4.9 | 6e-05 | 23/45 (SW480, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.775×** | -4.9 | 6e-05 | 29/45 (A-172, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.794×** | -4.4 | 5e-04 | 26/45 (SW480, J82, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.679×** | -3.9 | 0.005 | 22/45 (Panc 03.27, LoVo, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 0.867× | -3.8 | 0.005 | 16/45 (LS 180, HT-29, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.831×** | -3.5 | 0.016 | 22/45 (SW480, COLO 205, …) | top dose only | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 5 µM |  | 0.840× | -3.2 | 0.049 | 15/45 (HOP62, H4, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.847× | -3.0 | 0.090 | 18/44 (SW48, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8996. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 163 | 6 (3 ⚠) | 7 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.78× (z +18.0) | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -23.3) |
| [[A-172 (line)]] | wt | 397 | 3 (2 ⚠) | 9 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.74× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -19.8) |
| [[HS-578T (line)]] | alt | 399 | 4 (4 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -13.3) |
| [[HOP62 (line)]] | alt | 244 | 3 (3 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +13.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -16.2) |
| [[LOX-IMVI (line)]] | wt | 386 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -19.2) |
| [[hTERT-HPNE (line)]] | wt | 309 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.321× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.349× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 394 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +13.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -23.6) |
| [[SW 900 (line)]] | alt | 192 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -13.1) |
| [[CHP-212 (line)]] | wt | 210 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -21.0) |
| [[COLO 205 (line)]] | alt | 269 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -16.6) |
| [[A549 (line)]] | wt | 103 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.549× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 88.8 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.51× (z +14.8) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 122 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -15.9) |
| [[LS 180 (line)]] | wt | 147 | 3 (2 ⚠) | 1 | [[Tucidinostat (drug)]] 5 µM 1.78× (z +10.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.444× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 82.5 | 4 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.38× (z +12.4) | — |
| [[PANC-1 (line)]] | alt | 71.3 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +14.1) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.408× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.456× (z -8.8) |
| [[A498 (line)]] | wt | 138 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +15.1) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 108 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 375 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -17.0) |
| [[KATO III (line)]] | alt | 135 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -10.7) |
| [[LoVo (line)]] | wt | 48.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +12.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 68.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.20× (z +12.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 95.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 390 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -15.1) |
| [[AsPC-1 (line)]] | alt | 230 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +12.4) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 138 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +11.9) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 187 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -20.6) |
| [[NCI-H1792 (line)]] | alt | 71.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.355× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 435 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -17.0) |
| [[NCI-H460 (line)]] | wt | 65.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +11.0) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 62.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +9.9) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.348× (z -8.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 276 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -23.5) |
| [[SNU-1 (line)]] | wt | 52.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.82× (z +13.0) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 79.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +10.6) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.466× (z -8.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 412 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 52.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +12.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 63.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 109 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.257× (z -14.5) |
| [[Hs 766T (line)]] | wt | 121 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 130 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 97.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.30× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 58.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +8.9) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.1 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 300 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8996), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDS]] | +0.66 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[APLP2]] | +0.65 | +0.58 / +0.65 | both halves | 7e-06 | STRING 642 |
| [[GRN]] | +0.63 | +0.62 / +0.61 | both halves | 7e-06 | STRING 619 |
| [[BSG]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_HEME_METABOLISM; STRING 484 |
| [[PSAP]] | +0.63 | +0.55 / +0.67 | both halves | 1e-05 | STRING 678 |
| [[MXRA7]] | +0.61 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[NUCB1]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[TIMP2]] | +0.58 | +0.50 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_COMPLEMENT; STRING 477 |
| [[ITM2C]] | +0.57 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[ITGB1]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 | pathway: Affinity selection of immunoglobulins |
| [[TGM2]] | +0.55 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[PTTG1IP]] | +0.55 | +0.50 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IWS1]] | -0.63 | -0.49 / -0.65 | both halves | 2e-05 | pathway: Affinity selection of immunoglobulins |
| [[PPIG]] | -0.54 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[SREK1]] | -0.52 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[BRIX1]] | -0.52 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[CCDC66]] | -0.51 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[ERCC4]] | -0.51 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[ATP6V0D1-DT]] | -0.51 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[ZC3HC1]] | -0.50 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[THUMPD2]] | -0.50 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[OBI1]] | -0.50 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[NSUN4]] | -0.49 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[RNF135]] | -0.49 | -0.38 / -0.46 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL6A1]] | B | COL6A1 activity raises CTSB's level | lines that do not express COL6A1 (24) vs lines expressing it (26) | 2.37× lower at baseline in the lines without COL6A1 | 0.005 | ⚠ within organs, on part of the lines; also absent: COL6A2, PLAT, PTN |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZC3HC1]] | C | CTSB activity lowers ZC3HC1's level | lines that do not express CTSB (3) vs lines expressing it (47) | 1.85× higher at baseline in the lines without CTSB | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FUCA2, AIFM2, TRAF3IP2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.620). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.7, -20.5); signed map (-10.0, 39.0). **Vector** length 121, 36.6% of its response variance represented; |z| ≥ 3 in 1,240 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.2 | +8.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.3 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +18.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.6 | +3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +13.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +0.6 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | +2.5 | +2.3 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | +2.5 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.1 | -14.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.8 | -5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.5 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.4 | -4.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.1 | -7.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.8 | -1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.2 | -8.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | cathepsin B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.1 — chr8:11,842,524-11,869,533 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cathepsins; Elastases; Cysteine endopeptidases |
| Hallmark sets | COAGULATION, COMPLEMENT, HEME_METABOLISM |
| Reactome | 25 pathways, smallest: Trafficking and processing of endosomal TLR; SRC activates STAT3 in a quantitative manner, through Cadherin-11 (CDH11), RAC1 and gp130 (IL6ST); Collagen degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P07858](https://www.uniprot.org/uniprotkb/P07858) (Cathepsin B):

> Thiol protease which is believed to participate in intracellular degradation and turnover of proteins. Cleaves matrix extracellular phosphoglycoprotein MEPE. Involved in the solubilization of cross-linked TG/thyroglobulin in the thyroid follicle lumen (By similarity). Has also been implicated in tumor invasion and metastasis.

**Summary**, from NCBI Gene [1508](https://www.ncbi.nlm.nih.gov/gene/1508):

> This gene encodes a member of the C1 family of peptidases. Alternative splicing of this gene results in multiple transcript variants. At least one of these variants encodes a preproprotein that is proteolytically processed to generate multiple protein products. These products include the cathepsin B light and heavy chains, which can dimerize to form the double chain form of the enzyme. This enzyme is a lysosomal cysteine protease with both endopeptidase and exopeptidase activity that may play a …

**Accessions** — [HGNC:2527](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2527) · Entrez [1508](https://www.ncbi.nlm.nih.gov/gene/1508) · UniProt [P07858](https://www.uniprot.org/uniprotkb/P07858) · Ensembl [ENSG00000164733](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164733)

## Data

Gene col 8996: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8996); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8996, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8996]; `tensor/DDL_lfc|DDL_z.npy` [8996]; `embed/gene_vectors.npy` [8996]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8996 or target_col == 8996). Every well: [[CTSB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTSB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
