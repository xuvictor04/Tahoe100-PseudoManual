---
symbol: "PALS1"
type: "gene"
col: 1018
ensembl_id: "ENSG00000072415"
name: "protein associated with LIN7 1, MAGUK p55 family member"
location: "14q23.3"
module: 17
arm: "+"
pooled_cpm: 134.64
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 12
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# PALS1

*protein associated with LIN7 1, MAGUK p55 family member* — 14q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.85× (z +22.1, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.725× (z -11.6, q 3e-28, down in 33 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAB2]] (+0.55, fdr 1e-05), [[QPRT]] (+0.54, fdr 1e-05), [[RAB30]] (+0.53, fdr 4e-05); moves opposite to [[LINC01128]] (-0.52, fdr 4e-05), [[NPAS2]] (-0.50, fdr 1e-05), [[WDR27]] (-0.49, fdr 6e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1018.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.85×** | +22.1 | 0e+00 | 44/48 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +10.8 | 8e-25 | 38/48 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.78×** | +7.7 | 3e-12 | 38/49 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +7.4 | 1e-11 | 28/48 (C32, A-172, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +7.3 | 2e-11 | 34/48 (HOP62, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +6.4 | 2e-08 | 29/48 (LS 180, HOP62, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +5.1 | 3e-05 | 12/48 (PANC-1, NCI-H2030, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +5.0 | 5e-05 | 25/48 (HT-29, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.21×** | +4.9 | 5e-05 | 21/49 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +4.6 | 2e-04 | 21/47 (PANC-1, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.18× | +4.4 | 6e-04 | 20/50 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.17× | +3.8 | 0.007 | 16/48 (PANC-1, NCI-H1573, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.7 | 0.011 | 20/48 (LS 180, SW48, …) | top dose only | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +3.5 | 0.017 | 12/49 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.16× | +3.5 | 0.020 | 13/48 (HEC-1-A, AsPC-1, …) | all doses, flat |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.15× | +3.4 | 0.027 | 11/48 (SK-MEL-2, SNU-423, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.14× | +3.2 | 0.038 | 13/49 (AsPC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.13× | +3.2 | 0.041 | 11/48 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1018.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.725×** | -11.6 | 3e-28 | 33/49 (RKO, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.766×** | -9.6 | 3e-19 | 34/48 (SW480, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.679×** | -9.5 | 5e-19 | 31/44 (SHP-77, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.738×** | -7.7 | 1e-12 | 36/48 (SW480, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.745×** | -6.8 | 1e-09 | 29/45 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.768×** | -6.7 | 2e-09 | 31/49 (SNU-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.793×** | -5.7 | 1e-06 | 26/50 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~16% of this change | **0.820×** | -4.9 | 8e-05 | 25/47 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.830×** | -4.6 | 3e-04 | 25/48 (RKO, SW480, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.848× | -4.0 | 0.003 | 19/48 (LoVo, RKO, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.854× | -4.0 | 0.003 | 19/48 (SW1417, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[4EGI-1 (drug)]] 5 µM |  | **0.748×** | -3.9 | 0.005 | 23/48 (SW 1271, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.766×** | -3.6 | 0.016 | 17/47 (SW 900, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.779×** | -3.3 | 0.035 | 17/45 (RKO, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.917× | -3.1 | 0.067 | 2/48 (SHP-77, NCI-H661) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1018. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 261 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -21.2) |
| [[SW 900 (line)]] | alt | 174 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.338× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -9.9) |
| [[SW480 (line)]] | alt | 141 | 0 | 6 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.334× (z -20.3) |
| [[LS 180 (line)]] | wt | 101 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.446× (z -10.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 143 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +18.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.496× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~16% of this change |
| [[A-427 (line)]] | wt | 193 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.406× (z -12.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 194 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -12.2) |
| [[HOP62 (line)]] | alt | 86.4 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 219 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +9.1) | [[Auranofin (drug)]] 5 µM 0.516× (z -9.6) |
| [[PANC-1 (line)]] | alt | 121 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +30.9) | — |
| [[A-172 (line)]] | wt | 94.0 | 2 | 1 | [[Harringtonine (drug)]] 5 µM 1.93× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -10.6) |
| [[A549 (line)]] | wt | 103 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +22.3) | — |
| [[AsPC-1 (line)]] | alt | 123 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.354× (z -12.8) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -11.6) |
| [[H4 (line)]] | wt | 119 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +13.4) | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -9.7) |
| [[HS-578T (line)]] | alt | 67.1 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +15.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 197 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -15.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 77.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +19.0) | — |
| [[SNU-1 (line)]] | wt | 180 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -14.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 169 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -10.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 148 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.343× (z -8.6) |
| [[C32 (line)]] | wt | 39.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.92× (z +16.5) | — |
| [[CFPAC-1 (line)]] | alt | 162 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +23.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -15.7) |
| [[HepG2_C3A (line)]] | wt | 108 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.370× (z -9.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 108 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +14.2) | [[Auranofin (drug)]] 5 µM 0.459× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 113 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.385× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 140 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +22.2) | — |
| [[NCI-H2030 (line)]] | alt | 264 | 1 | 1 | [[Harringtonine (drug)]] 5 µM 1.85× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.659× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 280 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -19.6) |
| [[SNU-423 (line)]] | alt | 91.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.4) | [[Auranofin (drug)]] 5 µM 0.499× (z -8.7) |
| [[A498 (line)]] | wt | 109 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +11.3) | — |
| [[BT-474 (line)]] | alt | 92.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +16.1) | — |
| [[C-33 A (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.375× (z -11.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 147 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.421× (z -8.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 103 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 106 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +16.7) | — |
| [[J82 (line)]] | alt | 107 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 90.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +12.5) | — |
| [[SHP-77 (line)]] | alt | 62.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -20.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 74.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +16.1) | — |
| [[SW 1088 (line)]] | alt | 86.9 | 0 | 1 | — | [[5-Azacytidine (drug)]] 5 µM 0.0757× (z -9.9) |
| [[SW 1271 (line)]] | alt | 189 | 0 | 1 | — | [[4EGI-1 (drug)]] 5 µM 0.0692× (z -8.5) |
| [[SW1417 (line)]] | alt | 182 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.649× (z -8.9) |
| [[CHP-212 (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 102 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 117 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 148 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 192 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1018), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAB2]] | +0.55 | +0.59 / +0.52 | both halves | 1e-05 | pathway: SARS-CoV-2 Infection |
| [[QPRT]] | +0.54 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[RAB30]] | +0.53 | +0.40 / +0.55 | both halves | 4e-05 |  |
| [[COMMD7]] | +0.52 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[TTBK2]] | +0.52 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[CD2AP]] | +0.52 | +0.44 / +0.50 | both halves | 3e-05 | same gene group; pathway: Cell-Cell communication |
| [[SSH2]] | +0.51 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[EPB41]] | +0.51 | +0.54 / +0.44 | both halves | 3e-05 | STRING 805 |
| [[CCNC]] | +0.50 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[RPAP3]] | +0.50 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[PTPN13]] | +0.50 | +0.44 / +0.54 | both halves | 3e-05 | same gene group |
| [[CDC5L]] | +0.50 | +0.45 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01128]] | -0.52 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[NPAS2]] | -0.50 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[WDR27]] | -0.49 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[ANKMY1]] | -0.48 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[EXOSC3]] | -0.47 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[SPRY4-AS1]] | -0.47 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[LENG8-AS1]] | -0.47 | -0.28 / -0.54 | both halves | 3e-04 |  |
| [[CAPN15]] | -0.47 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[MAD1L1]] | -0.47 | -0.45 / -0.40 | both halves | 4e-05 |  |
| [[ZNF778]] | -0.47 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[ATG7]] | -0.47 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[VAC14]] | -0.47 | -0.42 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PALS1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.452). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (11.3, -7.7); signed map (-7.0, 14.5). **Vector** length 122, 36.6% of its response variance represented; |z| ≥ 3 in 1,269 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +22.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | +6.6 | +4.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +10.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.6 | +4.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.0 | +3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.6 | +5.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.5 | +2.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.4 | -7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -11.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.3 | -9.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | +0.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | -0.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.2 | -4.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -0.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.5 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | protein associated with LIN7 1, MAGUK p55 family member |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.3 — chr14:67,240,713-67,336,061 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12615; previously MPP5 |
| Gene groups (HGNC) | Membrane associated guanylate kinases; PDZ domain containing; Crumbs complex components; SH3 domain containing |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 11 pathways, smallest: SARS-CoV-2 targets PDZ proteins in cell-cell junction; Tight junction interactions; SARS-CoV-1-host interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N3R9](https://www.uniprot.org/uniprotkb/Q8N3R9) (Protein PALS1):

> Plays a role in tight junction biogenesis and in the establishment of cell polarity in epithelial cells. Also involved in adherens junction biogenesis by ensuring correct localization of the exocyst complex protein EXOC4/SEC8 which allows trafficking of adherens junction structural component CDH1 to the cell surface (By similarity). Plays a role through its interaction with CDH5 in vascular lumen formation and endothelial membrane polarity. Required during embryonic and postnatal retinal …

**Summary**, from NCBI Gene [64398](https://www.ncbi.nlm.nih.gov/gene/64398):

> This gene encodes a member of the p55-like subfamily of the membrane-associated guanylate kinase (MAGUK) gene superfamily. The encoded protein participates in the polarization of differentiating cells, has been shown to regulate myelinating Schwann cells (PMID: 20237282), and is one of the components of the Crumbs complex in the retina. Mice which express lower levels of the orthologous protein have retinal degeneration and impaired vision (PMID: 22114289). Multiple transcript variants encoding …

**Accessions** — [HGNC:18669](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18669) · Entrez [64398](https://www.ncbi.nlm.nih.gov/gene/64398) · UniProt [Q8N3R9](https://www.uniprot.org/uniprotkb/Q8N3R9) · Ensembl [ENSG00000072415](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072415)

## Data

Gene col 1018: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1018); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1018, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1018]; `tensor/DDL_lfc|DDL_z.npy` [1018]; `embed/gene_vectors.npy` [1018]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1018 or target_col == 1018). Every well: [[PALS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PALS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
