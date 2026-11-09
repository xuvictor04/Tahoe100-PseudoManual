---
symbol: "PIP4K2A"
type: "gene"
col: 7465
ensembl_id: "ENSG00000150867"
name: "phosphatidylinositol-5-phosphate 4-kinase type 2 alpha"
location: "10p12.2"
module: 95
arm: "-"
pooled_cpm: 121.86
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 16
n_dd_up_clean: 8
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# PIP4K2A

*phosphatidylinositol-5-phosphate 4-kinase type 2 alpha* — 10p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.63× (z +9.8, q 7e-20, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.480× (z -20.9, q 0e+00, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PACC1]] (+0.72, fdr 7e-06), [[TPST2]] (+0.68, fdr 1e-05), [[GNA12]] (+0.66, fdr 2e-05); moves opposite to [[HELQ]] (-0.67, fdr 3e-05), [[LATS1]] (-0.65, fdr 3e-05), [[PIGV]] (-0.65, fdr 4e-05).
> It sits in the **-** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7465.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +9.8 | 7e-20 | 41/48 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.49×** | +8.0 | 3e-13 | 36/48 (LoVo, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +7.5 | 9e-12 | 36/48 (SW1417, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +6.9 | 9e-10 | 29/48 (LoVo, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.76×** | +5.9 | 3e-07 | 39/49 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.37×** | +5.9 | 3e-07 | 30/48 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +5.5 | 3e-06 | 25/47 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +5.5 | 3e-06 | 26/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 4e-04 | 28/48 (SW1417, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.24×** | +4.4 | 6e-04 | 23/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.24×** | +4.4 | 6e-04 | 22/48 (Hs 766T, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.20×** | +3.7 | 0.011 | 21/48 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.031 | 20/48 (SNU-423, Hs 766T, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.37×** | +3.3 | 0.036 | 18/45 (SW480, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.18× | +3.3 | 0.041 | 18/48 (LS 180, BT-474, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.070 | 19/47 (NCI-H2030, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.070 | 18/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.080 | 12/48 (NCI-H2030, SK-MEL-2, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7465.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.480×** | -20.9 | 0e+00 | 40/48 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.578×** | -15.6 | 0e+00 | 41/49 (NCI-H2347, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.494×** | -13.6 | 6e-40 | 40/48 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.595×** | -10.4 | 3e-23 | 38/48 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.573×** | -10.4 | 4e-23 | 35/45 (RKO, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.588×** | -10.3 | 1e-22 | 31/44 (Panc 03.27, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.636×** | -9.1 | 8e-18 | 36/49 (A-427, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.643×** | -8.9 | 5e-17 | 40/48 (RKO, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.703×** | -6.8 | 6e-10 | 35/50 (SW48, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.609×** | -5.2 | 1e-05 | 28/49 (A549, A-172, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **0.773×** | -5.2 | 1e-05 | 31/48 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.772×** | -5.0 | 3e-05 | 27/48 (NCI-H23, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.820×** | -4.0 | 0.003 | 23/48 (A549, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.755×** | -3.7 | 0.008 | 21/48 (CFPAC-1, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.827×** | -3.5 | 0.016 | 22/47 (A549, CHP-212, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.853× | -3.1 | 0.071 | 17/49 (RKO, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7465. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 130 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -32.8) |
| [[SW48 (line)]] | wt | 107 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -26.9) |
| [[HOP62 (line)]] | alt | 75.1 | 2 (1 ⚠) | 6 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.51× (z +10.3) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 2.21× (z +9.2) | [[Harringtonine (drug)]] 5 µM 0.352× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 61.8 | 2 (1 ⚠) | 5 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.11× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -20.6) |
| [[PANC-1 (line)]] | alt | 123 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -27.4) |
| [[RKO (line)]] | wt | 166 | 0 | 7 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0777× (z -28.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.247× (z -17.1) |
| [[A498 (line)]] | wt | 144 | 1 (1 ⚠) | 5 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.18× (z +10.0) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -15.4) |
| [[NCI-H1792 (line)]] | alt | 241 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -22.9) |
| [[NCI-H2030 (line)]] | alt | 103 | 3 | 3 | [[Belinostat (drug)]] 5 µM 2.71× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -15.5) |
| [[NCI-H23 (line)]] | alt | 74.4 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -27.0) |
| [[CFPAC-1 (line)]] | alt | 341 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -18.2) |
| [[HEC-1-A (line)]] | alt | 120 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -16.0) |
| [[HS-578T (line)]] | alt | 101 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -20.3) |
| [[LoVo (line)]] | wt | 90.9 | 3 | 2 | [[Belinostat (drug)]] 5 µM 2.41× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -20.5) |
| [[LOX-IMVI (line)]] | wt | 108 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -24.3) |
| [[NCI-H1573 (line)]] | alt | 61.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -17.9) |
| [[A-172 (line)]] | wt | 148 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -15.0) |
| [[A-427 (line)]] | wt | 101 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -22.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.415× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 81.3 | 2 | 2 | [[Panobinostat (drug)]] 5 µM 2.89× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -11.5) |
| [[J82 (line)]] | alt | 159 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -13.6) |
| [[KATO III (line)]] | alt | 115 | 1 | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.19× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.287× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.562× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 43.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0689× (z -23.6) |
| [[SNU-423 (line)]] | alt | 112 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -17.5) |
| [[AsPC-1 (line)]] | alt | 425 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -16.9) |
| [[HepG2_C3A (line)]] | wt | 150 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -16.6) |
| [[NCI-H2347 (line)]] | alt | 94.1 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -19.0) |
| [[RPMI-7951 (line)]] | alt | 144 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.326× (z -10.9) |
| [[SW 900 (line)]] | alt | 200 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -17.8) |
| [[SW480 (line)]] | alt | 120 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.474× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.626× (z -9.0) |
| [[HCT15 (line)]] | alt | 71.6 | 1 | 1 | [[Belinostat (drug)]] 5 µM 2.65× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -15.5) |
| [[LS 180 (line)]] | wt | 99.7 | 2 (1 ⚠) | 0 | [[Peretinoin (drug)]] 5 µM 2.44× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 166 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -16.2) |
| [[BT-474 (line)]] | alt | 95.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -13.0) |
| [[C-33 A (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.100× (z -21.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 140 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 78.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0691× (z -26.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 179 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -17.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 95.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -11.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 84.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -15.1) |
| [[AN3 CA (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 86.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7465), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*33 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PACC1]] | +0.72 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[TPST2]] | +0.68 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[GNA12]] | +0.66 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[DNMT3B]] | +0.65 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[SH3PXD2B]] | +0.65 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[ST6GALNAC4]] | +0.65 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[SERAC1]] | +0.63 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[GPRIN1]] | +0.62 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[INPP4A]] | +0.62 | +0.59 / +0.45 | both halves | 3e-05 | pathway: PI Metabolism |
| [[PEDS1]] | +0.61 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[MBOAT2]] | +0.61 | +0.65 / +0.42 | both halves | 4e-05 | pathway: Phospholipid metabolism |
| [[AP3M2]] | +0.61 | +0.63 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*67 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HELQ]] | -0.67 | -0.73 / -0.45 | both halves | 3e-05 |  |
| [[LATS1]] | -0.65 | -0.66 / -0.45 | both halves | 3e-05 |  |
| [[PIGV]] | -0.65 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[METTL6]] | -0.65 | -0.71 / -0.32 | both halves | 2e-04 |  |
| [[INO80D]] | -0.64 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[LINC00869-1]] | -0.64 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[COQ5]] | -0.64 | -0.67 / -0.49 | both halves | 1e-05 |  |
| [[TP53]] | -0.64 | -0.64 / -0.43 | both halves | 3e-05 | pathway: Intracellular signaling by second messengers |
| [[NEK8]] | -0.63 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[SMIM19]] | -0.63 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[ZNF585A]] | -0.63 | -0.71 / -0.37 | both halves | 8e-05 |  |
| [[PAN2]] | -0.63 | -0.67 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PIP4K2A's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **-** arm (projection on the module's main direction -0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (2.1, 5.6); signed map (-42.2, -6.4). **Vector** length 127, 40.0% of its response variance represented; |z| ≥ 3 in 1,508 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.1 | +3.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +8.1 | +9.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.5 | +7.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.9 | +6.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.7 | +8.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.6 | +5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.5 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +5.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.9 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.7 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -14.0 | -20.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.0 | -15.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.9 | -10.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.5 | -13.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.4 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -4.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.8 | -2.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.0 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol-5-phosphate 4-kinase type 2 alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.2 — chr10:22,534,854-22,714,578 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PIP5KIIA, PIP5KIIalpha; previously PIP5K2A |
| Gene groups (HGNC) | Phosphatidylinositol-5-phosphate 4-kinase type 2 family |
| Reactome | 13 pathways, smallest: Synthesis of PIPs in the nucleus; PI5P Regulates TP53 Acetylation; Regulation of TP53 Activity through Acetylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P48426](https://www.uniprot.org/uniprotkb/P48426) (Phosphatidylinositol 5-phosphate 4-kinase type-2 alpha):

> Catalyzes the phosphorylation of phosphatidylinositol 5-phosphate (PtdIns5P) on the fourth hydroxyl of the myo-inositol ring, to form phosphatidylinositol 4,5-bisphosphate (PtdIns(4,5)P2). Has both ATP- and GTP-dependent kinase activities. May exert its function by regulating the levels of PtdIns5P, which functions in the cytosol by increasing AKT activity and in the nucleus signals through ING2. May regulate the pool of cytosolic PtdIns5P in response to the activation of tyrosine …

**Summary**, from NCBI Gene [5305](https://www.ncbi.nlm.nih.gov/gene/5305):

> Phosphatidylinositol-5,4-bisphosphate, the precursor to second messengers of the phosphoinositide signal transduction pathways, is thought to be involved in the regulation of secretion, cell proliferation, differentiation, and motility. The protein encoded by this gene is one of a family of enzymes capable of catalyzing the phosphorylation of phosphatidylinositol-5-phosphate on the fourth hydroxyl of the myo-inositol ring to form phosphatidylinositol-5,4-bisphosphate. The amino acid sequence of …

**Accessions** — [HGNC:8997](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8997) · Entrez [5305](https://www.ncbi.nlm.nih.gov/gene/5305) · UniProt [P48426](https://www.uniprot.org/uniprotkb/P48426) · Ensembl [ENSG00000150867](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150867)

## Data

Gene col 7465: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7465); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7465, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7465]; `tensor/DDL_lfc|DDL_z.npy` [7465]; `embed/gene_vectors.npy` [7465]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7465 or target_col == 7465). Every well: [[PIP4K2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIP4K2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
