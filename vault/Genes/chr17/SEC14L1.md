---
symbol: "SEC14L1"
type: "gene"
col: 4994
ensembl_id: "ENSG00000129657"
name: "SEC14 like lipid binding 1"
location: "17q25.2-q25.3"
module: 59
arm: "-"
pooled_cpm: 105.79
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 6
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# SEC14L1

*SEC14 like lipid binding 1* — 17q25.2-q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.71× (z +14.5, q 1e-44, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.757× (z -7.3, q 2e-10, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CUL4A]] (+0.60, fdr 3e-05), [[RBM19]] (+0.58, fdr 1e-05), [[DPP9]] (+0.58, fdr 1e-05); moves opposite to [[MYLIP]] (-0.64, fdr 7e-06), [[EFNA1]] (-0.58, fdr 1e-05), [[KMT2E]] (-0.58, fdr 5e-05).
> It sits in the **-** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RHOV]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4994.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +14.5 | 1e-44 | 41/48 (LoVo, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +10.7 | 2e-24 | 35/45 (A549, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +7.1 | 2e-10 | 30/48 (SW480, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.29×** | +7.0 | 4e-10 | 29/49 (LoVo, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +6.9 | 7e-10 | 27/48 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +6.5 | 6e-09 | 27/48 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.25×** | +6.0 | 2e-07 | 26/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.23×** | +5.7 | 9e-07 | 27/48 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +5.6 | 1e-06 | 24/48 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +5.2 | 1e-05 | 22/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +5.2 | 1e-05 | 15/48 (NCI-H2347, A-427, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +5.0 | 2e-05 | 20/44 (LoVo, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +4.6 | 2e-04 | 18/49 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.19× | +4.5 | 3e-04 | 18/47 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.17× | +4.3 | 7e-04 | 19/48 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.35×** | +4.2 | 9e-04 | 20/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.14× | +3.6 | 0.010 | 11/47 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.021 | 13/48 (NCI-H2347, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.033 | 11/48 (AsPC-1, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4994.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.757×** | -7.3 | 2e-10 | 33/48 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.847× | -6.4 | 5e-08 | 22/49 (CHP-212, LOX-IMVI, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.802×** | -5.8 | 2e-06 | 26/50 (SK-MEL-2, SNU-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.866× | -5.5 | 5e-06 | 20/48 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.820×** | -5.4 | 7e-06 | 25/48 (MIA PaCa-2, SW48, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **0.818×** | -5.3 | 1e-05 | 25/48 (LOX-IMVI, H4, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.836× | -4.9 | 9e-05 | 21/48 (PANC-1, J82, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -4.8 | 1e-04 | 21/48 (HEC-1-A, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.845× | -4.6 | 3e-04 | 22/48 (PANC-1, J82, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.844× | -4.4 | 5e-04 | 18/47 (SW48, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.848× | -4.3 | 8e-04 | 15/48 (MIA PaCa-2, HS-578T, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.858× | -4.2 | 0.001 | 15/47 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.859× | -4.1 | 0.001 | 14/48 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.900× | -4.1 | 0.002 | 14/48 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.878× | -4.1 | 0.002 | 16/48 (MIA PaCa-2, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.753×** | -4.0 | 0.002 | 21/47 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.866× | -3.9 | 0.003 | 14/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.895× | -3.7 | 0.006 | 10/48 (MIA PaCa-2, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.910× | -3.5 | 0.011 | 9/49 (MIA PaCa-2, HEC-1-A, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | 0.873× | -3.4 | 0.015 | 11/47 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.876× | -3.4 | 0.015 | 12/48 (NCI-H2030, SK-MEL-2, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.882× | -3.4 | 0.015 | 7/49 (PANC-1, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4994. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 149 | 1 | 4 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.34× (z +9.3) | [[Adagrasib (drug)]] 0.05 µM 0.595× (z -19.8) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 0.5 µM 0.433× (z -9.2) |
| [[PANC-1 (line)]] | alt | 274 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.57× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.365× (z -15.2) ⚠ cell-cycle shift, explains ~14% of this change |
| [[LoVo (line)]] | wt | 44.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.30× (z +10.9) | — |
| [[NCI-H2347 (line)]] | alt | 62.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.06× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.93× (z +9.0) | — |
| [[RKO (line)]] | wt | 66.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.75× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.551× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 94.2 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.12× (z +8.5) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -12.8) |
| [[SW480 (line)]] | alt | 114 | 3 | 0 | [[Auranofin (drug)]] 5 µM 1.78× (z +9.6) | — |
| [[A-172 (line)]] | wt | 130 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.22× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.621× (z -8.9) ⚠ cell-cycle shift, explains ~4% of this change |
| [[AsPC-1 (line)]] | alt | 107 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.32× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 178 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.491× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 88.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.17× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.07× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 89.1 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -10.3) ⚠ cell-cycle shift, explains ~6% of this change |
| [[NCI-H1573 (line)]] | alt | 55.9 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.26× (z +9.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 112 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.08× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.408× (z -10.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 108 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -12.1) |
| [[A-427 (line)]] | wt | 115 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -9.7) ⚠ cell-cycle shift, explains ~4% of this change |
| [[A549 (line)]] | wt | 86.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.34× (z +10.1) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.585× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 189 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -10.3) ⚠ cell-cycle shift, explains ~4% of this change |
| [[H4 (line)]] | wt | 127 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.143× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~53% of this change |
| [[HCT15 (line)]] | alt | 90.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +11.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HS-578T (line)]] | alt | 110 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 1.98× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 52.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.40× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H596 (line)]] | alt | 91.1 | 0 | 1 | — | [[Bimiralisib (drug)]] 5 µM 0.204× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 163 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 130 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.94× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0941× (z -11.6) ⚠ transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 147 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 106 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 139 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 99.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 55.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 99.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 97.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 69.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 94.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4994), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CUL4A]] | +0.60 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[RBM19]] | +0.58 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[DPP9]] | +0.58 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[ERVK13-1]] | +0.57 | +0.25 / +0.68 | both halves | 4e-04 |  |
| [[ARHGEF1]] | +0.56 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[GCN1]] | +0.55 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[TTL]] | +0.55 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[NBPF20]] | +0.54 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[ZNF731P]] | +0.54 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[MAPKAPK3]] | +0.54 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[THOC5]] | +0.54 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[HSF1]] | +0.54 | +0.54 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYLIP]] | -0.64 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[EFNA1]] | -0.58 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[KMT2E]] | -0.58 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[PSMB9]] | -0.57 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[RAB30]] | -0.55 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[DBP]] | -0.54 | -0.40 / -0.63 | both halves | 5e-05 |  |
| [[PSME2]] | -0.54 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[ATP5IF1]] | -0.54 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[SLC11A2]] | -0.54 | -0.43 / -0.56 | both halves | 3e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[LCA5]] | -0.53 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[NEURL3]] | -0.53 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[CXXC5]] | -0.53 | -0.38 / -0.54 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHOV]] | B | RHOV activity lowers SEC14L1's level | lines that do not express RHOV (23) vs lines expressing it (27) | 1.26× higher at baseline in the lines without RHOV | 0.078 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **-** arm (projection on the module's main direction -0.598). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (7.9, -25.4); signed map (-24.7, -48.6). **Vector** length 113, 29.3% of its response variance represented; |z| ≥ 3 in 1,267 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.2 | +14.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +10.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.5 | +5.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.9 | +4.6 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +3.9 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.7 | +4.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.4 | +4.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.7 | -7.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -5.7 | -5.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.1 | -5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -4.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -5.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.2 | -4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.8 | -3.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.8 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | SEC14 like lipid binding 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.2-q25.3 — chr17:77,088,749-77,217,101 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRELID4A; previously SEC14L |
| Gene groups (HGNC) | SEC14 family; PRELI domain containing |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92503](https://www.uniprot.org/uniprotkb/Q92503) (SEC14-like protein 1):

> May play a role in innate immunity by inhibiting the antiviral RIG-I signaling pathway. In this pathway, functions as a negative regulator of RIGI, the cytoplasmic sensor of viral nucleic acids. Prevents the interaction of RIGI with MAVS/IPS1, an important step in signal propagation. May also regulate the SLC18A3 and SLC5A7 cholinergic transporters.

**Summary**, from NCBI Gene [6397](https://www.ncbi.nlm.nih.gov/gene/6397):

> The protein encoded by this gene belongs to the SEC14 cytosolic factor family. It has similarity to yeast SEC14 and to Japanese flying squid RALBP which suggests a possible role of the gene product in an intracellular transport system. Multiple alternatively spliced transcript variants have been found for this gene; some variants represent read-through transcripts that include exons from the upstream gene C17orf86. [provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:10698](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10698) · Entrez [6397](https://www.ncbi.nlm.nih.gov/gene/6397) · UniProt [Q92503](https://www.uniprot.org/uniprotkb/Q92503) · Ensembl [ENSG00000129657](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129657)

## Data

Gene col 4994: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4994); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4994, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4994]; `tensor/DDL_lfc|DDL_z.npy` [4994]; `embed/gene_vectors.npy` [4994]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4994 or target_col == 4994). Every well: [[SEC14L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC14L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
