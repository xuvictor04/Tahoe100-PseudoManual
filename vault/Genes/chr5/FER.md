---
symbol: "FER"
type: "gene"
col: 7518
ensembl_id: "ENSG00000151422"
name: "FER tyrosine kinase"
location: "5q21.3"
module: 65
arm: "-"
pooled_cpm: 275.77
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 16
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# FER

*FER tyrosine kinase* — 5q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.31× (z +4.4, q 0.006, up in 33 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (MIA PaCa-2 2.34×, SK-MEL-2 2.02×, HOP62 2.21×, RPMI-7951 2.10×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (MIA PaCa-2 3.09×, SK-MEL-2 2.20×, RPMI-7951 2.55×, HS-578T 2.61×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (BT-474 3.20×, SNU-1 2.36×; ⚠ cell-cycle shift, explains ~65% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (HOP62 1.84×).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (12 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.423× (z -14.0, q 5e-42, down in 45 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.600× (z -8.7, q 7e-16, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYO9A]] (+0.62, fdr 1e-05), [[CEP112]] (+0.60, fdr 1e-05), [[SCAPER]] (+0.60, fdr 1e-05); moves opposite to [[PRMT9]] (-0.55, fdr 1e-05), [[PRUNE1]] (-0.54, fdr 2e-05), [[SEPTIN7P14]] (-0.53, fdr 2e-05).
> It sits in the **-** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ACOT13]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7518.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (MIA PaCa-2 2.34×, SK-MEL-2 2.02×, HOP62 2.21×, RPMI-7951 2.10×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (MIA PaCa-2 3.09×, SK-MEL-2 2.20×, RPMI-7951 2.55×, HS-578T 2.61×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (BT-474 3.20×, SNU-1 2.36×; ⚠ cell-cycle shift, explains ~65% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (HOP62 1.84×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +4.4 | 0.006 | 33/47 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.28×** | +4.0 | 0.016 | 29/47 (NCI-H460, H4, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.068 | 31/47 (A-172, NCI-H460, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.25× | +3.4 | 0.11 | 24/50 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | 1.45× | +3.3 | 0.11 | 32/48 (MIA PaCa-2, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 1.43× | +3.2 | 0.15 | 25/50 (SNU-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | 1.42× | +3.1 | 0.15 | 27/48 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 15 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7518.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.423×** | -14.0 | 5e-42 | 45/47 (RKO, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.580×** | -9.2 | 7e-18 | 37/48 (LS 180, J82, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.600×** | -8.7 | 7e-16 | 42/48 (C-33 A, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.604×** | -8.2 | 3e-14 | 34/44 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.575×** | -7.8 | 9e-13 | 38/49 (NCI-H1573, A-427, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **0.643×** | -7.5 | 7e-12 | 44/48 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.638×** | -7.0 | 1e-10 | 38/45 (NCI-H23, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.679×** | -6.3 | 2e-08 | 37/47 (J82, LoVo, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.510×** | -6.0 | 1e-07 | 36/49 (A-172, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.734×** | -5.2 | 9e-06 | 29/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.691×** | -5.2 | 1e-05 | 37/48 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.766×** | -4.5 | 3e-04 | 28/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.838× | -4.2 | 0.001 | 25/49 (A549, NCI-H1792, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.787×** | -3.9 | 0.004 | 27/48 (PANC-1, A-427, …) | rises with dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.649×** | -3.8 | 0.005 | 23/38 (Panc 03.27, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.711×** | -3.0 | 0.082 | 24/48 (A-172, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.882× | -3.0 | 0.082 | 1/49 (HS-578T) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7518. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 279 | 0 | 14 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -17.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 365 | 4 (3 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +13.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.84× (z +10.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.410× (z -10.8) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 347 | 0 | 7 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.294× (z -14.5) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.458× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 391 | 0 | 7 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.255× (z -19.1) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 364 | 0 | 7 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -14.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[AN3 CA (line)]] | alt | 623 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.267× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H23 (line)]] | alt | 329 | 1 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -23.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.510× (z -10.5) |
| [[C-33 A (line)]] | alt | 292 | 0 | 5 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.350× (z -13.3) |
| [[HT-29 (line)]] | alt | 225 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.217× (z -19.4) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.391× (z -12.4) |
| [[J82 (line)]] | alt | 323 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.372× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[LS 180 (line)]] | wt | 238 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.297× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[MIA PaCa-2 (line)]] | alt | 294 | 2 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.315× (z -13.8) ⚠ toxic |
| [[A-427 (line)]] | wt | 350 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[RPMI-7951 (line)]] | alt | 271 | 2 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Auranofin (drug)]] 5 µM 0.394× (z -11.0) |
| [[SK-MEL-2 (line)]] | alt | 409 | 2 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +14.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.471× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.511× (z -9.6) |
| [[SW480 (line)]] | alt | 164 | 1 (1 ⚠) | 3 (3 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.397× (z -12.6) ⚠ toxic |
| [[A-172 (line)]] | wt | 342 | 0 | 3 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.285× (z -8.9) |
| [[A549 (line)]] | wt | 244 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -14.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[COLO 205 (line)]] | alt | 118 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.346× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[H4 (line)]] | wt | 362 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.426× (z -9.7) |
| [[HCT15 (line)]] | alt | 312 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.322× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[LoVo (line)]] | wt | 432 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.458× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[NCI-H460 (line)]] | wt | 308 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.420× (z -11.5) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.521× (z -9.0) |
| [[RKO (line)]] | wt | 332 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.172× (z -21.7) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.457× (z -10.0) |
| [[SHP-77 (line)]] | alt | 149 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.366× (z -11.4) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 374 | 1 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +10.4) ⚠ cell-cycle shift, explains ~65% of this change | [[Dinaciclib (drug)]] 5 µM 0.298× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[SNU-423 (line)]] | alt | 286 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.377× (z -11.7) |
| [[BT-474 (line)]] | alt | 97.2 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.20× (z +11.3) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[CHP-212 (line)]] | wt | 242 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.187× (z -13.4) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 434 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.423× (z -12.6) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 239 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.298× (z -12.2) ⚠ toxic |
| [[HS-578T (line)]] | alt | 375 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.61× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.416× (z -8.5) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 309 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.426× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H2347 (line)]] | alt | 257 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 1271 (line)]] | alt | 402 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.255× (z -9.9) |
| [[SW 900 (line)]] | alt | 197 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.356× (z -12.4) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.458× (z -9.7) |
| [[A498 (line)]] | wt | 134 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AsPC-1 (line)]] | alt | 288 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C32 (line)]] | wt | 299 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.381× (z -11.5) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 233 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.268× (z -15.3) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 175 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.175× (z -18.2) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 180 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.219× (z -14.5) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 244 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0595× (z -16.8) ⚠ toxic |
| [[SW48 (line)]] | wt | 304 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -8.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[KATO III (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 270 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 272 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 284 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 366 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 84.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7518), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO9A]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[CEP112]] | +0.60 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[SCAPER]] | +0.60 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[KTN1]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[CCSER2]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[EEA1]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[NPIPB4]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[ERC1]] | +0.55 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[TRIO]] | +0.55 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[NEK1]] | +0.54 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[ATXN1]] | +0.53 | +0.36 / +0.52 | both halves | 1e-04 |  |
| [[MIB1]] | +0.53 | +0.48 / +0.56 | both halves | 2e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRMT9]] | -0.55 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[PRUNE1]] | -0.54 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[SEPTIN7P14]] | -0.53 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[USPL1]] | -0.53 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[SDHAP1]] | -0.53 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[SDHAP4]] | -0.52 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[ACVR1B]] | -0.52 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[PMS2P3-1]] | -0.51 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[TIGD1]] | -0.51 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[MFSD14CP]] | -0.50 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[SLC18B1]] | -0.50 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[NISCH]] | -0.50 | -0.47 / -0.55 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACOT13]] | C | ACOT13's natural level strengthens FER's drug response | ACOT13's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.07; direction not clear | 0.071 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **-** arm (projection on the module's main direction -0.483). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-6.0, -2.0); signed map (10.6, -10.6). **Vector** length 106, 37.2% of its response variance represented; |z| ≥ 3 in 1,323 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.7 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.1 | +2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +4.5 | -3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.4 | +0.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | -0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +2.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.5 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +4.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.8 | -14.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.8 | -5.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.8 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -8.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -2.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.3 | -1.1 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -2.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | FER tyrosine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q21.3 — chr5:108,747,841-109,196,841 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TYK3, PPP1R74 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; SH2 domain containing; F-BAR domain containing; Fes family tyrosine kinases |
| Reactome | 2 pathways, smallest: Signaling by SCF-KIT; Signaling by Receptor Tyrosine Kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [P16591](https://www.uniprot.org/uniprotkb/P16591) (Tyrosine-protein kinase Fer):

> Tyrosine-protein kinase that acts downstream of cell surface receptors for growth factors and plays a role in the regulation of the actin cytoskeleton, microtubule assembly, lamellipodia formation, cell adhesion, cell migration and chemotaxis. Acts downstream of EGFR, KIT, PDGFRA and PDGFRB. Acts downstream of EGFR to promote activation of NF-kappa-B and cell proliferation. May play a role in the regulation of the mitotic cell cycle. Plays a role in the insulin receptor signaling pathway and in …

**Summary**, from NCBI Gene [2241](https://www.ncbi.nlm.nih.gov/gene/2241):

> The protein encoded by this gene is a member of the FPS/FES family of non-transmembrane receptor tyrosine kinases. It regulates cell-cell adhesion and mediates signaling from the cell surface to the cytoskeleton via growth factor receptors. Alternative splicing results in multiple transcript variants. A related pseudogene has been identified on chromosome X. [provided by RefSeq, Apr 2015]

**Accessions** — [HGNC:3655](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3655) · Entrez [2241](https://www.ncbi.nlm.nih.gov/gene/2241) · UniProt [P16591](https://www.uniprot.org/uniprotkb/P16591) · Ensembl [ENSG00000151422](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151422)

## Data

Gene col 7518: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7518); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7518, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7518]; `tensor/DDL_lfc|DDL_z.npy` [7518]; `embed/gene_vectors.npy` [7518]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7518 or target_col == 7518). Every well: [[FER — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FER.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
