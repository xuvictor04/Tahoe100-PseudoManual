---
symbol: "SCFD1"
type: "gene"
col: 1690
ensembl_id: "ENSG00000092108"
name: "sec1 family domain containing 1"
location: "14q12"
module: 41
arm: "+"
pooled_cpm: 254.7
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# SCFD1

*sec1 family domain containing 1* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.31× (z +9.3, q 7e-18, up in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (NCI-H2030 2.18×, LOX-IMVI 2.10×, NCI-H23 2.05×, NCI-H460 1.87×, …); [[Homoharringtonine (drug)]] 0.5 µM in 6 lines (NCI-H1573 2.45×, LOX-IMVI 2.15×, RKO 2.58×, NCI-H460 2.15×, …); [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 1.86×).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.572× (z -12.8, q 6e-35, down in 37 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.753× (z -9.6, q 2e-19, down in 33 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPE]] (+0.71, fdr 7e-06), [[SPTY2D1]] (+0.68, fdr 7e-06), [[SEC23IP]] (+0.67, fdr 7e-06); moves opposite to [[PPM1A]] (-0.58, fdr 1e-05), [[PPP4R1]] (-0.55, fdr 1e-05), [[THAP12]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1690.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (NCI-H2030 2.18×, LOX-IMVI 2.10×, NCI-H23 2.05×, NCI-H460 1.87×, …); [[Homoharringtonine (drug)]] 0.5 µM in 6 lines (NCI-H1573 2.45×, LOX-IMVI 2.15×, RKO 2.58×, NCI-H460 2.15×, …); [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 1.86×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +9.3 | 7e-18 | 30/48 (NCI-H2030, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +7.7 | 3e-12 | 36/48 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.9 | 0.018 | 21/48 (SHP-77, AsPC-1, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | 1.15× | +3.3 | 0.13 | 16/48 (SHP-77, C32, …) | top dose only |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.16× | +3.1 | 0.17 | 11/48 (C32, LoVo, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.14× | +3.1 | 0.17 | 17/48 (NCI-H2030, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1690.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.572×** | -12.8 | 6e-35 | 37/44 (CHP-212, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.646×** | -10.4 | 5e-23 | 38/49 (RKO, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.753×** | -9.6 | 2e-19 | 33/49 (A549, SNU-1, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.740×** | -6.9 | 7e-10 | 35/47 (NCI-H2030, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.756×** | -6.4 | 2e-08 | 30/47 (CFPAC-1, SNU-423, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.774×** | -6.1 | 9e-08 | 40/48 (J82, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.810×** | -5.0 | 4e-05 | 27/48 (SW 900, HOP62, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.806×** | -4.9 | 6e-05 | 26/48 (A-172, AN3 CA, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.817×** | -4.4 | 6e-04 | 25/45 (SW48, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.845× | -4.0 | 0.003 | 22/48 (CFPAC-1, RPMI-7951, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.847× | -3.8 | 0.007 | 21/48 (LoVo, COLO 205, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.761×** | -3.4 | 0.031 | 25/49 (COLO 205, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.766×** | -3.3 | 0.038 | 20/49 (MIA PaCa-2, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | 0.872× | -3.1 | 0.074 | 14/47 (LOX-IMVI, AsPC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.881× | -3.0 | 0.100 | 8/48 (NCI-H2030, AsPC-1, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.869× | -3.0 | 0.100 | 11/47 (HOP62, NCI-H23, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1690. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 282 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.288× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -13.1) |
| [[NCI-H460 (line)]] | wt | 232 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.583× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 351 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.45× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.460× (z -12.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 262 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.58× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -9.1) |
| [[A-172 (line)]] | wt | 123 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +12.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -11.0) ⚠ cell-cycle shift, explains ~18% of this change |
| [[CFPAC-1 (line)]] | alt | 347 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.442× (z -13.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 385 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -10.1) |
| [[Hs 766T (line)]] | wt | 257 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.506× (z -9.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 302 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -11.3) |
| [[LoVo (line)]] | wt | 283 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 293 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.444× (z -12.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 299 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.456× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.658× (z -8.6) |
| [[SHP-77 (line)]] | alt | 298 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 1.86× (z +10.9) | — |
| [[SW48 (line)]] | wt | 457 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 271 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.443× (z -12.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 365 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -9.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 262 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.647× (z -10.3) |
| [[HOP62 (line)]] | alt | 259 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.554× (z -8.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 230 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +17.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 273 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +9.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.525× (z -9.2) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 306 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.529× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.637× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 251 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +18.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.518× (z -10.3) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 198 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +14.2) | — |
| [[SK-MEL-2 (line)]] | alt | 220 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.475× (z -10.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 246 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -15.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 252 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.83× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.515× (z -10.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 278 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -25.0) |
| [[AN3 CA (line)]] | alt | 194 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -9.2) ⚠ cell-cycle shift, explains ~18% of this change |
| [[BT-474 (line)]] | alt | 338 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.503× (z -9.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 204 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.469× (z -10.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 262 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -17.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 276 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.4) | — |
| [[KATO III (line)]] | alt | 265 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.436× (z -9.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 273 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.494× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 262 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +15.9) | — |
| [[A-427 (line)]] | wt | 204 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 172 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 190 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 189 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 186 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 264 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 316 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 270 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 399 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 361 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 275 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 240 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1690), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPE]] | +0.71 | +0.77 / +0.62 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SPTY2D1]] | +0.68 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[SEC23IP]] | +0.67 | +0.65 / +0.66 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 792 |
| [[LYSMD3]] | +0.67 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[ARF4]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[ARFIP2]] | +0.66 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[USP8]] | +0.65 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[RARS1]] | +0.64 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[GNL2]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[RAB5A]] | +0.63 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[TINCR]] | +0.63 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[GOLGA2]] | +0.63 | +0.69 / +0.50 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation; STRING 771 |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPM1A]] | -0.58 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[PPP4R1]] | -0.55 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[THAP12]] | -0.54 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[H3-3A]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[ELMO2]] | -0.53 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[TEAD2]] | -0.52 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[KPNA1]] | -0.52 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[CIPC]] | -0.51 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[RNF138]] | -0.51 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[SCAF4]] | -0.51 | -0.59 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.650). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (11.3, -37.4); signed map (-52.0, 14.6). **Vector** length 134, 46.4% of its response variance represented; |z| ≥ 3 in 982 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.8 | +7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +9.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +2.5 |
|  | [[EX229 (drug)]] 5 µM |  | +3.5 | +2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.4 | +1.4 |
|  | [[EX229 (drug)]] 0.5 µM |  | +3.1 | +1.6 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.9 | -6.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -5.0 | -5.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | -3.5 | -6.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.3 | -2.9 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | -3.2 | -3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -3.2 | -1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.2 | -3.8 |
|  | [[Erlotinib (drug)]] 5 µM |  | -2.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | sec1 family domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:30,622,291-30,737,694 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RA410, KIAA0917, STXBP1L2, SLY1; previously C14orf163 |
| Gene groups (HGNC) | SM family of SNARE chaperones |
| Reactome | 10 pathways, smallest: COPII-mediated vesicle transport; ER to Golgi Anterograde Transport; RHOA GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVM8](https://www.uniprot.org/uniprotkb/Q8WVM8) (Sec1 family domain-containing protein 1):

> Plays a role in SNARE-pin assembly and Golgi-to-ER retrograde transport via its interaction with COG4. Involved in vesicular transport between the endoplasmic reticulum and the Golgi (By similarity).

**Summary**, from NCBI Gene [23256](https://www.ncbi.nlm.nih.gov/gene/23256):

> Involved in negative regulation of autophagosome assembly; regulation of protein transport; and response to toxic substance. Located in cis-Golgi network. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20726](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20726) · Entrez [23256](https://www.ncbi.nlm.nih.gov/gene/23256) · UniProt [Q8WVM8](https://www.uniprot.org/uniprotkb/Q8WVM8) · Ensembl [ENSG00000092108](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092108)

## Data

Gene col 1690: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1690); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1690, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1690]; `tensor/DDL_lfc|DDL_z.npy` [1690]; `embed/gene_vectors.npy` [1690]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1690 or target_col == 1690). Every well: [[SCFD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCFD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
