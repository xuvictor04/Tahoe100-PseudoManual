---
symbol: "LEKR1"
type: "gene"
col: 12506
ensembl_id: "ENSG00000197980"
name: "leucine, glutamate and lysine rich 1"
location: "3q25.31"
module: 10
arm: "+"
pooled_cpm: 15.48
n_lines_expressing: 46
n_dd_up: 18
n_dd_down: 15
n_dd_up_clean: 17
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# LEKR1

*leucine, glutamate and lysine rich 1* — 3q25.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.87× (z +21.1, q 0e+00, up in 39 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.376× (z -8.3, q 6e-14, down in 31 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDCL3P4]] (+0.85, fdr 7e-06), [[LINC02340]] (+0.80, fdr 9e-06), [[WARS2-AS1]] (+0.79, fdr 1e-05); moves opposite to [[LCMT1]] (-0.72, fdr 7e-06), [[ECI2]] (-0.71, fdr 1e-05), [[MYPOP]] (-0.71, fdr 1e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Digitoxin (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12506.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.87×** | +21.1 | 0e+00 | 39/43 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.60×** | +11.3 | 3e-27 | 40/42 (AsPC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.80×** | +8.6 | 1e-15 | 36/40 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.19×** | +6.1 | 2e-07 | 19/30 (C32, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.05×** | +5.8 | 8e-07 | 26/42 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +5.2 | 2e-05 | 25/40 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +5.2 | 2e-05 | 24/43 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.9 | 7e-05 | 28/44 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.71×** | +4.5 | 5e-04 | 23/43 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.64×** | +4.1 | 0.003 | 22/42 (KATO III, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.72×** | +4.0 | 0.004 | 18/43 (HS-578T, A549, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.54×** | +3.6 | 0.016 | 17/42 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +3.4 | 0.025 | 20/43 (A498, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +3.2 | 0.061 | 18/40 (LOX-IMVI, AsPC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +3.2 | 0.061 | 10/43 (CFPAC-1, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.44×** | +3.1 | 0.081 | 12/41 (KATO III, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12506.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.376×** | -8.3 | 6e-14 | 31/43 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.399×** | -7.8 | 2e-12 | 34/43 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.404×** | -7.7 | 3e-12 | 27/41 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.493×** | -6.0 | 3e-07 | 33/42 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.498×** | -5.9 | 4e-07 | 27/43 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.499×** | -5.6 | 2e-06 | 26/40 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.541×** | -5.2 | 1e-05 | 28/42 (A-427, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.604×** | -4.2 | 0.002 | 20/43 (SK-MEL-2, NCI-H1573, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.600×** | -4.2 | 0.002 | 19/37 (NCI-H23, C32, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.715×** | -4.1 | 0.003 | 25/44 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.667×** | -3.5 | 0.028 | 21/43 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.632×** | -3.4 | 0.029 | 17/44 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.683×** | -3.3 | 0.050 | 21/43 (AN3 CA, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.487×** | -3.2 | 0.056 | 16/31 (NCI-H1573, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.489×** | -3.2 | 0.057 | 20/39 (NCI-H1573, COLO 205, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12506. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 71.5 | 2 | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +15.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0331× (z -24.0) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.198× (z -11.9) |
| [[SW480 (line)]] | alt | 24.0 | 1 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +10.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.111× (z -13.4) |
| [[A-427 (line)]] | wt | 72.0 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +12.7) | [[Digitoxin (drug)]] 5 µM 0.236× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.237× (z -10.4) |
| [[LoVo (line)]] | wt | 26.9 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.50× (z +18.3) | [[Digitoxin (drug)]] 5 µM 0.207× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.250× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 40.3 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -11.7) |
| [[A-172 (line)]] | wt | 13.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +15.6) | — |
| [[C32 (line)]] | wt | 12.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 17.0× (z +15.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0578× (z -10.9) ⚠ toxic |
| [[HS-578T (line)]] | alt | 7.77 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 32.7× (z +16.7) | [[Temsirolimus (drug)]] 0.5 µM 0.0689× (z -9.1) |
| [[HT-29 (line)]] | alt | 22.8 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.174× (z -9.6) |
| [[KATO III (line)]] | alt | 30.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.2× (z +24.1) | — |
| [[NCI-H460 (line)]] | wt | 12.0 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 16.7× (z +19.9) | [[Ixazomib citrate (drug)]] 5 µM 0.168× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 14.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +15.4) | — |
| [[AsPC-1 (line)]] | alt | 6.55 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.32× (z +10.9) | — |
| [[hTERT-HPNE (line)]] | wt | 6.15 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +11.7) | [[Ixazomib citrate (drug)]] 0.5 µM 0.0477× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 3.93 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +11.5) | — |
| [[NCI-H2030 (line)]] | alt | 12.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.84× (z +12.6) | — |
| [[SK-MEL-2 (line)]] | alt | 25.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.82× (z +12.5) | [[Digitoxin (drug)]] 5 µM 0.173× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 15.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +14.0) | — |
| [[CFPAC-1 (line)]] | alt | 11.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +10.3) | — |
| [[H4 (line)]] | wt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +10.8) | — |
| [[HCT15 (line)]] | alt | 8.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +10.2) | — |
| [[HOP62 (line)]] | alt | 12.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.96× (z +12.8) | — |
| [[J82 (line)]] | alt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +10.2) | — |
| [[LS 180 (line)]] | wt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.09× (z +11.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 19.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 13.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +14.9) | — |
| [[NCI-H2347 (line)]] | alt | 4.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 8.23 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0570× (z -10.5) ⚠ toxic |
| [[A498 (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.65 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12506), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCL3P4]] | +0.85 | +0.90 / +0.62 | both halves | 7e-06 |  |
| [[LINC02340]] | +0.80 | +0.88 / +0.57 | both halves | 9e-06 |  |
| [[WARS2-AS1]] | +0.79 | +0.78 / +0.56 | both halves | 1e-05 |  |
| [[PCNX4-DT]] | +0.78 | +0.85 / +0.48 | both halves | 2e-05 |  |
| [[RFX3-DT]] | +0.77 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[UFL1-AS1]] | +0.77 | +0.79 / +0.54 | both halves | 1e-05 |  |
| [[IQCH-AS1]] | +0.77 | +0.83 / +0.50 | both halves | 1e-05 |  |
| [[KRCC1]] | +0.76 | +0.84 / +0.45 | both halves | 3e-05 |  |
| [[ZC3H4]] | +0.76 | +0.78 / +0.47 | both halves | 2e-05 |  |
| [[ST7L]] | +0.76 | +0.80 / +0.46 | both halves | 3e-05 |  |
| [[LINC00886]] | +0.75 | +0.72 / +0.63 | both halves | 7e-06 | ⚠ same locus (8.4 kb: neighbours can correlate without regulation) |
| [[TMEM202-AS1]] | +0.75 | +0.83 / +0.41 | both halves | 4e-05 |  |
| [[CLHC1]] | +0.75 | +0.80 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LCMT1]] | -0.72 | -0.66 / -0.59 | both halves | 7e-06 |  |
| [[ECI2]] | -0.71 | -0.69 / -0.51 | both halves | 1e-05 |  |
| [[MYPOP]] | -0.71 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[SDHAP1]] | -0.70 | -0.75 / -0.49 | both halves | 1e-05 |  |
| [[SNTA1]] | -0.70 | -0.69 / -0.47 | both halves | 2e-05 |  |
| [[ANKRD27]] | -0.70 | -0.74 / -0.36 | both halves | 9e-05 |  |
| [[SDHAP2]] | -0.69 | -0.72 / -0.50 | both halves | 1e-05 |  |
| [[TSPAN33]] | -0.69 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[KLHL7]] | -0.68 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[HEBP1]] | -0.68 | -0.67 / -0.37 | both halves | 7e-05 |  |
| [[NBPF3]] | -0.67 | -0.69 / -0.35 | both halves | 1e-04 |  |
| [[TMEM120B]] | -0.67 | -0.63 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LEKR1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KLRC3]] | B | KLRC3 activity raises LEKR1's level | lines that do not express KLRC3 (27) vs lines expressing it (23) | 1.84× lower at baseline in the lines without KLRC3 | 0.085 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Digitoxin (drug)]] 0.5 µM | C | LEKR1 activity lowers the cells' numbers under Digitoxin 0.5 µM (makes them more sensitive) | lines that do not express LEKR1 (4) vs lines expressing it (44) | the lines without LEKR1: 1.55× the cells of the other lines | 0.066 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: KLF2, PDP1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.836). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.7, 14.5); signed map (27.8, -11.5). **Vector** length 99.0, 25.4% of its response variance represented; |z| ≥ 3 in 1,023 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.6 | +21.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.3 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +6.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.8 | +5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +11.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +4.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +3.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.9 | +1.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | +1.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.2 | -7.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.4 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -4.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.2 | -4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | +2.6 |

## What is on record

|  |  |
|---|---|
| Name | leucine, glutamate and lysine rich 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.31 — chr3:156,825,481-157,046,129 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ16641 |
| Matched by | ensembl_id |

UniProt [Q6ZMV7](https://www.uniprot.org/uniprotkb/Q6ZMV7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:33765](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33765) · Entrez [389170](https://www.ncbi.nlm.nih.gov/gene/389170) · UniProt [Q6ZMV7](https://www.uniprot.org/uniprotkb/Q6ZMV7) · Ensembl [ENSG00000197980](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197980)

## Data

Gene col 12506: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12506); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12506, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12506]; `tensor/DDL_lfc|DDL_z.npy` [12506]; `embed/gene_vectors.npy` [12506]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12506 or target_col == 12506). Every well: [[LEKR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LEKR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
