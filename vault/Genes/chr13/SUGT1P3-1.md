---
symbol: "SUGT1P3-1"
type: "gene"
col: 16478
ensembl_id: "ENSG00000290464"
name: ""
location: ""
module: 12
arm: "+"
pooled_cpm: 21.06
n_lines_expressing: 48
n_dd_up: 20
n_dd_down: 23
n_dd_up_clean: 17
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# SUGT1P3-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.95× (z +15.4, q 0e+00, up in 39 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.410× (z -14.5, q 1e-44, down in 33 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.548× (z -9.8, q 5e-20, down in 33 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUGT1P3]] (+0.71, fdr 7e-06, ⚠ same locus), [[TPTE2P5]] (+0.70, fdr 7e-06, ⚠ same locus), [[KBTBD7]] (+0.63, fdr 7e-06), [[ZNF385C]] (+0.61, fdr 1e-05), [[MMADHC]] (+0.60, fdr 3e-05); moves opposite to [[UBE2G2]] (-0.59, fdr 4e-05), [[NIPA2]] (-0.58, fdr 2e-05), [[NDOR1]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF385C]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16478.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +15.4 | 0e+00 | 39/45 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.06×** | +11.7 | 3e-29 | 37/45 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +10.2 | 5e-22 | 37/46 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.61×** | +7.8 | 1e-12 | 28/45 (HT-29, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +7.7 | 1e-12 | 29/45 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +6.6 | 4e-09 | 26/45 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.29×** | +5.9 | 3e-07 | 23/46 (HOP62, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +5.7 | 6e-07 | 23/40 (Panc 03.27, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +5.1 | 2e-05 | 24/45 (HT-29, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +4.8 | 1e-04 | 20/45 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +4.7 | 1e-04 | 18/44 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.31×** | +4.4 | 5e-04 | 14/45 (SW480, KATO III, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.002 | 17/45 (LS 180, SW480, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.005 | 17/45 (HOP62, LS 180, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.8 | 0.005 | 13/45 (AsPC-1, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +3.6 | 0.011 | 13/46 (HEC-1-A, Hs 766T, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.018 | 11/46 (HEC-1-A, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.50×** | +3.4 | 0.018 | 11/46 (HT-29, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16478.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.410×** | -14.5 | 1e-44 | 33/45 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.548×** | -9.8 | 5e-20 | 33/45 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.552×** | -9.7 | 9e-20 | 32/45 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.569×** | -9.1 | 9e-18 | 32/45 (PANC-1, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.582×** | -8.1 | 5e-14 | 18/32 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.631×** | -7.2 | 6e-11 | 24/43 (SW 900, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **0.646×** | -7.1 | 1e-10 | 25/42 (PANC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.685×** | -6.1 | 6e-08 | 24/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.685×** | -5.9 | 2e-07 | 18/29 (KATO III, Panc 03.27, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.721×** | -5.3 | 6e-06 | 20/45 (Panc 03.27, KATO III, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.712×** | -5.3 | 6e-06 | 24/45 (NCI-H23, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.738×** | -4.9 | 4e-05 | 23/39 (CFPAC-1, KATO III, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.573×** | -4.7 | 1e-04 | 15/45 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.757×** | -4.5 | 3e-04 | 19/45 (CFPAC-1, SW 900, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.779×** | -4.1 | 0.002 | 16/45 (RKO, HOP62, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.623×** | -4.0 | 0.002 | 14/45 (SW 900, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.636×** | -3.8 | 0.004 | 12/45 (Hs 766T, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.857× | -3.5 | 0.012 | 16/46 (HCT15, HT-29, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.676×** | -3.3 | 0.023 | 10/44 (Hs 766T, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.825×** | -3.1 | 0.044 | 16/45 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.833×** | -3.0 | 0.070 | 14/45 (LS 180, SW480, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16478. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 40.5 | 4 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.83× (z +11.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.269× (z -11.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.277× (z -10.8) |
| [[PANC-1 (line)]] | alt | 28.4 | 1 | 7 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.66× (z +9.6) | [[Digitoxin (drug)]] 5 µM 0.243× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.258× (z -13.5) |
| [[SW480 (line)]] | alt | 29.7 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +15.8) | [[Digitoxin (drug)]] 5 µM 0.293× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.328× (z -10.9) |
| [[COLO 205 (line)]] | alt | 68.3 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +11.1) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.251× (z -11.1) |
| [[KATO III (line)]] | alt | 34.4 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.91× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.128× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[LoVo (line)]] | wt | 17.1 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.65× (z +18.1) | [[Digitoxin (drug)]] 5 µM 0.179× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 18.3 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.9) | [[Digitoxin (drug)]] 5 µM 0.271× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.05 µM 0.272× (z -10.9) |
| [[HOP62 (line)]] | alt | 16.5 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.226× (z -10.9) |
| [[Panc 03.27 (line)]] | alt | 41.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.143× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[CFPAC-1 (line)]] | alt | 32.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[HEC-1-A (line)]] | alt | 44.5 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.53× (z +8.5) | [[Lonafarnib (drug)]] 5 µM 0.0837× (z -11.7) ⚠ toxic |
| [[J82 (line)]] | alt | 16.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[LOX-IMVI (line)]] | wt | 14.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +10.7) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.208× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 32.4 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0851× (z -18.5) ⚠ cell-cycle shift, explains ~14% of this change |
| [[SK-MEL-2 (line)]] | alt | 9.98 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +8.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.127× (z -8.6) ⚠ toxic |
| [[SW 900 (line)]] | alt | 23.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +10.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.251× (z -8.9) ⚠ toxic |
| [[A-172 (line)]] | wt | 6.51 | 0 | 1 | — | [[Irinotecan (hydrochloride) (drug)]] 0.05 µM 0.0816× (z -9.6) |
| [[A-427 (line)]] | wt | 20.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.252× (z -9.6) ⚠ transcription drop; cell-cycle shift, explains ~28% of this change |
| [[C32 (line)]] | wt | 6.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.62× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 45.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[Hs 766T (line)]] | wt | 15.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[hTERT-HPNE (line)]] | wt | 17.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.150× (z -9.5) |
| [[LS 180 (line)]] | wt | 24.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[MIA PaCa-2 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.130× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.128× (z -11.1) ⚠ toxic |
| [[RKO (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0878× (z -12.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 4.42 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.66 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16478), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUGT1P3]] | +0.71 | +0.81 / +0.68 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[TPTE2P5]] | +0.70 | +0.79 / +0.62 | both halves | 7e-06 | ⚠ same locus (18.2 kb, same strand: neighbours can correlate without regulation) |
| [[KBTBD7]] | +0.63 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[ZNF385C]] | +0.61 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[MMADHC]] | +0.60 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[EPC1]] | +0.59 | +0.62 / +0.37 | both halves | 8e-05 |  |
| [[SAP18]] | +0.58 | +0.72 / +0.45 | both halves | 3e-05 |  |
| [[MRPL54]] | +0.58 | +0.32 / +0.40 | both halves | 1e-04 |  |
| [[TRA2A]] | +0.58 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[DCTN6]] | +0.58 | +0.62 / +0.38 | both halves | 7e-05 |  |
| [[NFKBIL1]] | +0.56 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[LNX1]] | +0.56 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[YJU2]] | +0.56 | +0.72 / +0.27 | both halves | 3e-04 |  |
| [[ING3]] | +0.56 | +0.56 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2G2]] | -0.59 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[NIPA2]] | -0.58 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[NDOR1]] | -0.57 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[BCAP31]] | -0.57 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[DPAGT1]] | -0.55 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[CTDP1]] | -0.54 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[CHID1]] | -0.54 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[KIF1C]] | -0.54 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[XPO5]] | -0.54 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[AKT1]] | -0.53 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[ADAM15]] | -0.53 | -0.58 / -0.39 | both halves | 6e-05 |  |
| [[ZNF731P]] | -0.53 | -0.54 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF385C]] | C | ZNF385C activity raises SUGT1P3-1's level | lines that do not express ZNF385C (4) vs lines expressing it (46) | 2.17× lower at baseline in the lines without ZNF385C | 0.065 | ⚠ few lines (4 vs 46); across organs; also absent: SMC1B, ARG2, SPRY1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.576). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-26.3, 14.6); signed map (8.8, -18.2). **Vector** length 71.8, 13.4% of its response variance represented; |z| ≥ 3 in 1,122 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +15.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.1 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +10.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +6.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +3.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.0 | +2.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.0 | +2.5 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -5.2 | -2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.5 | +3.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.1 | -14.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -1.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -3.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -4.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.8 | -2.4 |

## What is on record

> [!warning] No registry record
> SUGT1P3-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16478: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16478); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16478, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16478]; `tensor/DDL_lfc|DDL_z.npy` [16478]; `embed/gene_vectors.npy` [16478]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16478 or target_col == 16478). Every well: [[SUGT1P3-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUGT1P3-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
