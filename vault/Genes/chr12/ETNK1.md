---
symbol: "ETNK1"
type: "gene"
col: 6268
ensembl_id: "ENSG00000139163"
name: "ethanolamine kinase 1"
location: "12p12.1"
module: 33
arm: "-"
pooled_cpm: 247.07
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# ETNK1

*ethanolamine kinase 1* — 12p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.98× (z +12.6, q 2e-33, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.663× (z -7.3, q 2e-10, down in 36 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.740× (z -5.4, q 2e-05, down in 37 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (C-33 A 0.318×, CHP-212 0.190×, SW480 0.413×, Hs 766T 0.350×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SW480 0.387×, SW 1271 0.144×, A-427 0.412×, NCI-H2347 0.420×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 0.417×; ⚠ cell-cycle shift, explains ~0% of this change); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SW 1088 0.101×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (CFPAC-1 0.396×); [[Auranofin (drug)]] 5 µM in 1 line (LoVo 0.481×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERINC5]] (+0.52, fdr 4e-05), [[CTSS]] (+0.50, fdr 1e-04), [[ANXA4]] (+0.50, fdr 1e-04); moves opposite to [[EP400]] (-0.53, fdr 4e-05), [[TAMM41]] (-0.52, fdr 2e-04), [[UBL4A]] (-0.52, fdr 3e-05).
> It sits in the **-** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ITIH2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6268.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.98×** | +12.6 | 2e-33 | 45/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +10.7 | 4e-24 | 37/48 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.65×** | +9.2 | 5e-18 | 42/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +7.3 | 5e-11 | 38/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +7.2 | 1e-10 | 39/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +6.2 | 4e-08 | 32/48 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.20×** | +4.7 | 2e-04 | 27/48 (NCI-H2347, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **1.29×** | +4.5 | 4e-04 | 24/48 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cepharanthine (drug)]] 5 µM |  | 1.17× | +4.1 | 0.002 | 19/48 (LS 180, AsPC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.23×** | +3.9 | 0.006 | 25/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.23×** | +3.8 | 0.008 | 24/48 (MIA PaCa-2, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.008 | 22/50 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.026 | 22/48 (A-427, LS 180, …) | all doses, flat |  |
| [[Berbamine (drug)]] 5 µM |  | 1.14× | +3.3 | 0.039 | 11/49 (LS 180, CFPAC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.2 | 0.057 | 21/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.069 | 15/48 (hTERT-HPNE, LS 180, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6268.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (C-33 A 0.318×, CHP-212 0.190×, SW480 0.413×, Hs 766T 0.350×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SW480 0.387×, SW 1271 0.144×, A-427 0.412×, NCI-H2347 0.420×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 0.417×; ⚠ cell-cycle shift, explains ~0% of this change); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SW 1088 0.101×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (CFPAC-1 0.396×); [[Auranofin (drug)]] 5 µM in 1 line (LoVo 0.481×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.663×** | -7.3 | 2e-10 | 36/44 (C-33 A, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.680×** | -7.1 | 3e-10 | 37/49 (SW480, SW 1271, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.740×** | -5.4 | 2e-05 | 37/48 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **0.767×** | -4.9 | 1e-04 | 35/48 (Panc 03.27, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.774×** | -4.7 | 2e-04 | 27/48 (LoVo, LS 180, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **0.771×** | -4.4 | 8e-04 | 25/45 (NCI-H2347, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.831×** | -3.4 | 0.050 | 24/48 (SW480, A549, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.881× | -3.3 | 0.063 | 16/48 (NCI-H1792, MIA PaCa-2, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.887× | -3.2 | 0.092 | 6/48 (KATO III, A498, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.844× | -3.2 | 0.092 | 20/48 (SK-MEL-2, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6268. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 157 | 11 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.60× (z +17.6) | — |
| [[SNU-1 (line)]] | wt | 213 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.90× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.356× (z -10.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 391 | 2 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.481× (z -8.6) |
| [[BT-474 (line)]] | alt | 203 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.42× (z +13.1) | — |
| [[NCI-H1573 (line)]] | alt | 189 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +13.2) | — |
| [[A-427 (line)]] | wt | 289 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.412× (z -12.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 140 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.350× (z -10.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 315 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +20.6) | — |
| [[NCI-H23 (line)]] | alt | 324 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +16.8) | [[Dinaciclib (drug)]] 0.5 µM 0.446× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 191 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.420× (z -11.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 509 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.503× (z -8.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 222 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +10.6) | — |
| [[A549 (line)]] | wt | 411 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 214 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +12.8) | — |
| [[C-33 A (line)]] | alt | 206 | 1 | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.02× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -14.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 243 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +13.4) | — |
| [[CHP-212 (line)]] | wt | 257 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -12.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 105 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.8) | — |
| [[HT-29 (line)]] | alt | 289 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +12.5) | — |
| [[hTERT-HPNE (line)]] | wt | 150 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +14.1) | — |
| [[J82 (line)]] | alt | 131 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +14.5) | — |
| [[LOX-IMVI (line)]] | wt | 255 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +11.1) | — |
| [[LS 180 (line)]] | wt | 246 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 280 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.450× (z -9.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 138 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +15.3) | — |
| [[RKO (line)]] | wt | 265 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +10.7) | — |
| [[SK-MEL-2 (line)]] | alt | 193 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.483× (z -8.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 813 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -12.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 125 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +10.3) | — |
| [[A498 (line)]] | wt | 172 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CFPAC-1 (line)]] | alt | 209 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.396× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 186 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.532× (z -8.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 198 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +15.7) | — |
| [[KATO III (line)]] | alt | 301 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.445× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 232 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 132 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +10.3) | — |
| [[SW 1088 (line)]] | alt | 132 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.101× (z -9.9) |
| [[SW 1271 (line)]] | alt | 269 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -12.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 238 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 162 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 162 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 282 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 217 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6268), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERINC5]] | +0.52 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[CTSS]] | +0.50 | +0.39 / +0.33 | both halves | 1e-04 |  |
| [[ANXA4]] | +0.50 | +0.36 / +0.41 | both halves | 1e-04 |  |
| [[MR1]] | +0.49 | +0.40 / +0.33 | both halves | 1e-04 |  |
| [[BAZ2B]] | +0.49 | +0.41 / +0.28 | both halves | 3e-04 |  |
| [[CASP10]] | +0.49 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[BTG2]] | +0.49 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[DNAJC22]] | +0.48 | +0.44 / +0.37 | both halves | 8e-05 |  |
| [[MVP-DT]] | +0.48 | +0.43 / +0.38 | both halves | 7e-05 |  |
| [[CDKN2A]] | +0.48 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[TMPRSS3]] | +0.47 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[KMT2E-AS1]] | +0.47 | +0.35 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EP400]] | -0.53 | -0.45 / -0.40 | both halves | 4e-05 |  |
| [[TAMM41]] | -0.52 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[UBL4A]] | -0.52 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[RBAK-RBAKDN]] | -0.52 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[NUDCD3]] | -0.51 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[POLRMT]] | -0.51 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[RNF216]] | -0.50 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[TRIM35]] | -0.50 | -0.49 / -0.27 | both halves | 3e-04 |  |
| [[POLR3A]] | -0.50 | -0.47 / -0.37 | both halves | 7e-05 |  |
| [[CAMKK1]] | -0.50 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[DNAJA3]] | -0.49 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[PRR12]] | -0.49 | -0.51 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITIH2]] | B | ITIH2 activity weakens ETNK1's drug response | lines that do not express ITIH2 (42) vs lines expressing it (7) | the lines without ITIH2 respond 3.34× as strongly (z diff -2.39); strongest at Homoharringtonine 5 µM: 1.66x vs 1.04x (z diff -6.9) | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **-** arm (projection on the module's main direction -0.410). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-52.5, 7.4); signed map (37.3, -22.5). **Vector** length 115, 40.5% of its response variance represented; |z| ≥ 3 in 1,134 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +6.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +3.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +6.7 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | +5.7 | -4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.4 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +0.0 |
|  | [[Berbamine (drug)]] 5 µM |  | +3.1 | +3.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.7 | +4.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.7 | -0.2 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -8.0 | +0.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -7.4 | -0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -4.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -5.1 | -3.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.6 | -0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.5 | -3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | ethanolamine kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.1 — chr12:22,625,075-22,690,665 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EKI1, EKI |
| Gene groups (HGNC) | Ethanolamine kinase family |
| Reactome | 4 pathways, smallest: Synthesis of PE; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBU6](https://www.uniprot.org/uniprotkb/Q9HBU6) (Ethanolamine kinase 1):

> Highly specific for ethanolamine phosphorylation. May be a rate-controlling step in phosphatidylethanolamine biosynthesis.

**Summary**, from NCBI Gene [55500](https://www.ncbi.nlm.nih.gov/gene/55500):

> This gene encodes an ethanolamine kinase, which functions in the first committed step of the phosphatidylethanolamine synthesis pathway. This cytosolic enzyme is specific for ethanolamine and exhibits negligible kinase activity on choline. Alternative splicing results in multiple transcript variants encoding distinct isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:24649](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24649) · Entrez [55500](https://www.ncbi.nlm.nih.gov/gene/55500) · UniProt [Q9HBU6](https://www.uniprot.org/uniprotkb/Q9HBU6) · Ensembl [ENSG00000139163](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139163)

## Data

Gene col 6268: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6268); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6268, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6268]; `tensor/DDL_lfc|DDL_z.npy` [6268]; `embed/gene_vectors.npy` [6268]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6268 or target_col == 6268). Every well: [[ETNK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ETNK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
