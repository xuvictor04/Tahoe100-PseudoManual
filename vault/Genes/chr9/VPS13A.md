---
symbol: "VPS13A"
type: "gene"
col: 12501
ensembl_id: "ENSG00000197969"
name: "vacuolar protein sorting 13 homolog A"
location: "9q21.2"
module: 118
arm: "-"
pooled_cpm: 191.25
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# VPS13A

*vacuolar protein sorting 13 homolog A* — 9q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.33× (z +9.7, q 2e-19, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.568× (z -13.1, q 1e-36, down in 45 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.831× (z -6.3, q 5e-08, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DENND1A]] (+0.66, fdr 7e-06), [[CDCA7L]] (+0.62, fdr 1e-05), [[NIN]] (+0.61, fdr 1e-05); moves opposite to [[FBXL12]] (-0.58, fdr 3e-05), [[APPBP2]] (-0.55, fdr 3e-05), [[KBTBD4]] (-0.55, fdr 3e-05).
> It sits in the **-** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TMEM170B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12501.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +9.7 | 2e-19 | 30/48 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.50×** | +9.5 | 6e-19 | 31/48 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +8.3 | 2e-14 | 33/48 (Hs 766T, SW 900, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.38×** | +7.8 | 7e-13 | 34/48 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.03×** | +7.5 | 6e-12 | 27/49 (NCI-H460, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +6.5 | 8e-09 | 22/48 (NCI-H2347, H4, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +5.8 | 5e-07 | 27/48 (Hs 766T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.26×** | +5.7 | 1e-06 | 27/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.26×** | +5.5 | 2e-06 | 28/48 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.67×** | +5.5 | 2e-06 | 35/49 (AsPC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +4.8 | 7e-05 | 24/47 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.21×** | +4.7 | 1e-04 | 23/48 (LOX-IMVI, Hs 766T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.21×** | +4.6 | 2e-04 | 25/48 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.2 | 0.001 | 21/49 (C32, NCI-H2347, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.20× | +4.1 | 0.002 | 24/48 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.9 | 0.004 | 12/49 (MIA PaCa-2, H4, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.7 | 0.006 | 13/47 (LoVo, H4, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.16× | +3.7 | 0.006 | 13/48 (SK-MEL-2, NCI-H2030, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.13× | +2.9 | 0.095 | 12/48 (H4, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12501.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.568×** | -13.1 | 1e-36 | 45/47 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.770×** | -6.3 | 5e-08 | 33/48 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.831×** | -6.3 | 5e-08 | 23/48 (HEC-1-A, BT-474, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.809×** | -5.1 | 4e-05 | 24/48 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.948× | -4.5 | 8e-04 | 1/50 (SW 1088) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.883× | -4.2 | 0.002 | 22/49 (A549, SW48, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.831×** | -4.1 | 0.003 | 22/45 (SW48, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.896× | -3.8 | 0.011 | 5/48 (AsPC-1, H4, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.727×** | -3.4 | 0.041 | 22/47 (RPMI-7951, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.871× | -3.3 | 0.046 | 19/48 (RKO, NCI-H1573, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.815×** | -3.3 | 0.051 | 19/47 (HOP62, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.879× | -3.1 | 0.086 | 22/49 (RKO, MIA PaCa-2, …) | inconsistent across doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12501. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 229 | 11 (5 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.87× (z +16.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.466× (z -11.8) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 192 | 6 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +19.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.409× (z -10.9) ⚠ toxic |
| [[HOP62 (line)]] | alt | 111 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +13.8) | — |
| [[A498 (line)]] | wt | 235 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +26.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.533× (z -9.1) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 305 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +23.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.542× (z -10.3) ⚠ toxic |
| [[HS-578T (line)]] | alt | 128 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +18.0) | — |
| [[J82 (line)]] | alt | 373 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.496× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 222 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +14.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.462× (z -12.9) ⚠ toxic |
| [[A-172 (line)]] | wt | 230 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +28.3) | [[Dinaciclib (drug)]] 0.5 µM 0.461× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 94.1 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +15.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.458× (z -8.9) ⚠ toxic |
| [[A549 (line)]] | wt | 239 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +17.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 155 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +13.8) | — |
| [[LOX-IMVI (line)]] | wt | 260 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.589× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 249 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 79.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +22.7) | — |
| [[PANC-1 (line)]] | alt | 157 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +12.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.588× (z -8.7) ⚠ toxic |
| [[RKO (line)]] | wt | 327 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.568× (z -8.5) |
| [[SW 900 (line)]] | alt | 128 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.8) | — |
| [[SW48 (line)]] | wt | 337 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 370 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 130 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +22.1) | — |
| [[Hs 766T (line)]] | wt | 133 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.18× (z +9.9) | — |
| [[KATO III (line)]] | alt | 157 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.401× (z -12.5) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 129 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.368× (z -14.4) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 160 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.475× (z -9.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 236 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +8.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.454× (z -10.2) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 377 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.360× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 216 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.508× (z -12.9) ⚠ toxic |
| [[A-427 (line)]] | wt | 177 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.537× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 72.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +13.5) | — |
| [[HT-29 (line)]] | alt | 212 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.397× (z -12.8) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 207 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.28× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 225 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.561× (z -13.1) |
| [[RPMI-7951 (line)]] | alt | 101 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.29× (z +12.1) | — |
| [[SNU-423 (line)]] | alt | 198 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +15.3) | — |
| [[AN3 CA (line)]] | alt | 180 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 98.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 151 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 208 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 330 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 159 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12501), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*36 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND1A]] | +0.66 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[CDCA7L]] | +0.62 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[NIN]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[RAB3IP]] | +0.57 | +0.35 / +0.63 | both halves | 1e-04 |  |
| [[NR6A1]] | +0.55 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[NCAM1]] | +0.55 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[G3BP1]] | +0.53 | +0.39 / +0.59 | both halves | 6e-05 |  |
| [[DDHD1]] | +0.53 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[WWC2]] | +0.52 | +0.38 / +0.57 | both halves | 7e-05 |  |
| [[DTNB]] | +0.51 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[TPD52]] | +0.51 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[CPT1A]] | +0.51 | +0.31 / +0.58 | both halves | 2e-04 |  |

## Genes that move opposite

*64 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXL12]] | -0.58 | -0.44 / -0.64 | both halves | 3e-05 |  |
| [[APPBP2]] | -0.55 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[KBTBD4]] | -0.55 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[ZNF586]] | -0.55 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[LINS1]] | -0.54 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[BMS1P4-1]] | -0.54 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[ALKBH1]] | -0.54 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[ZNF547]] | -0.54 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[ZNF561]] | -0.53 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[KANSL2]] | -0.52 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[ZNF490]] | -0.52 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[TMEM92-AS1]] | -0.51 | -0.51 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM170B]] | B | TMEM170B activity raises VPS13A's level | lines that do not express TMEM170B (8) vs lines expressing it (42) | 1.36× lower at baseline in the lines without TMEM170B | 0.095 | ⚠ within organs, on part of the lines; also absent: KCNK13, KDM2B-DT, LINC02609 |
| [[TBL1X]] | C | TBL1X activity raises VPS13A's level | lines that do not express TBL1X (4) vs lines expressing it (46) | 1.43× lower at baseline in the lines without TBL1X | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF160, ZNF845, CRPPA; its own permutation p |
| [[AGTPBP1]] | C | AGTPBP1 activity raises VPS13A's level | lines that do not express AGTPBP1 (3) vs lines expressing it (47) | 1.70× lower at baseline in the lines without AGTPBP1 | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: USP31, ENSG00000232732; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **-** arm (projection on the module's main direction -0.577). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-19.1, 29.1); signed map (-16.3, 32.0). **Vector** length 112, 35.0% of its response variance represented; |z| ≥ 3 in 1,116 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +6.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.8 | +5.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.5 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.8 | +4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.7 | +5.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.8 | +1.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +3.9 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.1 | -13.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.1 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.9 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.8 | -5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | +0.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.6 | -3.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.4 | +1.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | vacuolar protein sorting 13 homolog A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.2 — chr9:77,177,445-77,421,537 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0986, BLTP5A; previously CHAC |
| Gene groups (HGNC) | Bridge-like lipid transfer protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RL7](https://www.uniprot.org/uniprotkb/Q96RL7) (Intermembrane lipid transfer protein VPS13A):

> Mediates the transfer of lipids between membranes at organelle contact sites (By similarity). Binds phospholipids. Required for the formation or stabilization of ER-mitochondria contact sites which enable transfer of lipids between the ER and mitochondria. Negatively regulates lipid droplet size and motility. Required for efficient lysosomal protein degradation.

**Summary**, from NCBI Gene [23230](https://www.ncbi.nlm.nih.gov/gene/23230):

> The protein encoded by this gene may control steps in the cycling of proteins through the trans-Golgi network to endosomes, lysosomes and the plasma membrane. Mutations in this gene cause the autosomal recessive disorder, chorea-acanthocytosis. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1908](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1908) · Entrez [23230](https://www.ncbi.nlm.nih.gov/gene/23230) · UniProt [Q96RL7](https://www.uniprot.org/uniprotkb/Q96RL7) · Ensembl [ENSG00000197969](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197969)

## Data

Gene col 12501: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12501); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12501, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12501]; `tensor/DDL_lfc|DDL_z.npy` [12501]; `embed/gene_vectors.npy` [12501]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12501 or target_col == 12501). Every well: [[VPS13A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS13A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
