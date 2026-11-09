---
symbol: "ITCH"
type: "gene"
col: 1231
ensembl_id: "ENSG00000078747"
name: "itchy E3 ubiquitin protein ligase"
location: "20q11.22"
module: 170
arm: "+"
pooled_cpm: 359.76
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 13
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/170"]
generated_by: "tahoemap"
---

# ITCH

*itchy E3 ubiquitin protein ligase* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.51× (z +9.1, q 7e-17, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.495× (z -15.3, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL22]] (+0.61, fdr 2e-05), [[STX12]] (+0.59, fdr 3e-05), [[LRCH3]] (+0.59, fdr 3e-05); moves opposite to [[HPSE]] (-0.56, fdr 3e-05), [[VASH2]] (-0.51, fdr 1e-04), [[CCDC88C]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 170]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1231.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.51×** | +9.1 | 7e-17 | 42/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +7.3 | 1e-10 | 29/48 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +6.6 | 6e-09 | 32/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +5.8 | 1e-06 | 38/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.27×** | +5.3 | 2e-05 | 29/48 (NCI-H23, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.7 | 0.018 | 22/47 (HepG2/C3A, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.16× | +3.3 | 0.084 | 18/48 (A-427, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1231.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.495×** | -15.3 | 0e+00 | 48/48 (AsPC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.521×** | -14.2 | 4e-43 | 48/48 (AsPC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.565×** | -12.4 | 4e-33 | 39/49 (A-172, J82, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.583×** | -11.7 | 1e-29 | 48/48 (NCI-H2347, AsPC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.581×** | -11.3 | 9e-28 | 37/44 (A-172, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.683×** | -8.3 | 1e-14 | 42/48 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.653×** | -7.9 | 3e-13 | 37/45 (J82, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.796×** | -7.0 | 2e-10 | 29/49 (A549, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.741×** | -6.5 | 5e-09 | 34/48 (CHP-212, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.755×** | -5.8 | 3e-07 | 35/47 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~19% of this change | **0.766×** | -5.8 | 4e-07 | 33/48 (SW1417, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.838× | -5.4 | 3e-06 | 23/48 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.826×** | -4.1 | 0.002 | 24/48 (A-172, NCI-H460, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.881× | -3.9 | 0.004 | 16/48 (NCI-H2347, HS-578T, …) | top dose only | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.891× | -3.5 | 0.018 | 3/48 (SNU-1, RPMI-7951, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.717×** | -3.3 | 0.032 | 28/49 (AsPC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.862× | -3.2 | 0.047 | 18/48 (KATO III, LoVo, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1231. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 528 | 0 | 10 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.312× (z -15.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.347× (z -13.9) |
| [[NCI-H1792 (line)]] | alt | 562 | 1 | 8 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.363× (z -13.5) |
| [[A-172 (line)]] | wt | 309 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.398× (z -15.6) |
| [[CFPAC-1 (line)]] | alt | 416 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.369× (z -12.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.391× (z -11.9) |
| [[HS-578T (line)]] | alt | 350 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.391× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.438× (z -12.1) |
| [[J82 (line)]] | alt | 548 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.396× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.531× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 295 | 3 (2 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.463× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.530× (z -9.6) |
| [[SW1417 (line)]] | alt | 543 | 1 | 6 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.79× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.467× (z -13.1) |
| [[SW480 (line)]] | alt | 321 | 3 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +12.7) | [[Panobinostat (drug)]] 0.5 µM 0.471× (z -14.1) |
| [[A549 (line)]] | wt | 292 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -20.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.448× (z -13.2) |
| [[HEC-1-A (line)]] | alt | 301 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -14.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.486× (z -12.3) |
| [[HOP62 (line)]] | alt | 376 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.369× (z -15.7) |
| [[Panc 03.27 (line)]] | alt | 519 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.391× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.430× (z -13.8) |
| [[A498 (line)]] | wt | 315 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.452× (z -14.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.480× (z -13.0) |
| [[AsPC-1 (line)]] | alt | 638 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.343× (z -16.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.346× (z -16.1) |
| [[BT-474 (line)]] | alt | 1,399 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.487× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.544× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 456 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.432× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.446× (z -11.3) |
| [[LoVo (line)]] | wt | 236 | 2 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +10.7) | [[Panobinostat (drug)]] 0.5 µM 0.520× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 295 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.443× (z -12.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.468× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 248 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +12.8) | — |
| [[PANC-1 (line)]] | alt | 196 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +17.1) | — |
| [[RKO (line)]] | wt | 326 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.546× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[RPMI-7951 (line)]] | alt | 465 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.502× (z -9.7) |
| [[COLO 205 (line)]] | alt | 275 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[KATO III (line)]] | alt | 359 | 2 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.544× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 275 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.457× (z -11.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.470× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 413 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.459× (z -10.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.526× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 252 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +12.7) | [[Panobinostat (drug)]] 0.5 µM 0.426× (z -15.4) |
| [[SNU-423 (line)]] | alt | 362 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.488× (z -11.5) |
| [[Hs 766T (line)]] | wt | 810 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HT-29 (line)]] | alt | 281 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.482× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 229 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.519× (z -9.4) |
| [[SW 900 (line)]] | alt | 306 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.450× (z -11.9) |
| [[A-427 (line)]] | wt | 226 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +12.4) | — |
| [[C-33 A (line)]] | alt | 206 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.484× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 283 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.463× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.529× (z -9.1) |
| [[SNU-1 (line)]] | wt | 320 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +9.5) | — |
| [[C32 (line)]] | wt | 213 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.479× (z -8.9) |
| [[H4 (line)]] | wt | 201 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.9) | — |
| [[SW 1271 (line)]] | alt | 750 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[AN3 CA (line)]] | alt | 250 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 240 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 288 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 206 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 346 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 339 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 285 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 396 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 240 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1231), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL22]] | +0.61 | +0.52 / +0.46 | both halves | 2e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[STX12]] | +0.59 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[LRCH3]] | +0.59 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[CYP20A1]] | +0.58 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[HGSNAT]] | +0.56 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[NDUFV3]] | +0.56 | +0.52 / +0.36 | both halves | 1e-04 |  |
| [[RC3H2]] | +0.56 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[DCAF10]] | +0.55 | +0.57 / +0.38 | both halves | 6e-05 |  |
| [[TMEM260]] | +0.55 | +0.36 / +0.44 | both halves | 9e-05 |  |
| [[TAF12]] | +0.55 | +0.49 / +0.32 | both halves | 2e-04 |  |
| [[LARP1B]] | +0.54 | +0.34 / +0.47 | both halves | 1e-04 |  |
| [[TRNAU1AP]] | +0.53 | +0.55 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HPSE]] | -0.56 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[VASH2]] | -0.51 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[CCDC88C]] | -0.50 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[UGT8]] | -0.49 | -0.34 / -0.51 | both halves | 1e-04 | same gene group |
| [[LHX6]] | -0.49 | -0.27 / -0.53 | both halves | 3e-04 |  |
| [[LDHB]] | -0.48 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[ASIC1]] | -0.48 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[TRAK1]] | -0.48 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[GLB1L2]] | -0.48 | -0.37 / -0.36 | both halves | 9e-05 |  |
| [[PFKM]] | -0.48 | -0.53 / -0.37 | both halves | 7e-05 | same gene group |
| [[KCNK5]] | -0.48 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[FAM234B]] | -0.47 | -0.22 / -0.47 | both halves | 6e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 170]]; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.541). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-21.8, 17.1); signed map (-1.5, -7.6). **Vector** length 89.4, 33.0% of its response variance represented; |z| ≥ 3 in 1,242 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +7.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.8 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | +5.4 | +3.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | -0.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | -0.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.9 | -0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.0 | +1.3 |
|  | [[Resveratrol (drug)]] 5 µM |  | +1.8 | +0.8 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | +2.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.2 | -6.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.9 | -8.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -1.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.8 | -1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | itchy E3 ubiquitin protein ligase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:34,363,235-34,511,773 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AIP4 |
| Gene groups (HGNC) | C2 domain containing; MicroRNA protein coding host genes; Nedd4 family E3 ubiquitin protein ligases |
| Reactome | 29 pathways, smallest: Downregulation of ERBB4 signaling; Activated NOTCH1 Transmits Signal to the Nucleus; RIPK1-mediated regulated necrosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96J02](https://www.uniprot.org/uniprotkb/Q96J02) (E3 ubiquitin-protein ligase Itchy homolog):

> Acts as an Acts as an E3 ubiquitin-protein ligase which accepts ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then directly transfers the ubiquitin to targeted substrates. Catalyzes 'Lys-29'-, 'Lys-48'- and 'Lys-63'-linked ubiquitin conjugation. Involved in the control of inflammatory signaling pathways. Essential component of a ubiquitin-editing protein complex, comprising also TNFAIP3, TAX1BP1 and RNF11, that ensures the transient nature of inflammatory …

**Summary**, from NCBI Gene [83737](https://www.ncbi.nlm.nih.gov/gene/83737):

> This gene encodes a member of the Nedd4 family of HECT domain E3 ubiquitin ligases. HECT domain E3 ubiquitin ligases transfer ubiquitin from E2 ubiquitin-conjugating enzymes to protein substrates, thus targeting specific proteins for lysosomal degradation. The encoded protein plays a role in multiple cellular processes including erythroid and lymphoid cell differentiation and the regulation of immune responses. Mutations in this gene are a cause of syndromic multisystem autoimmune disease. …

**Accessions** — [HGNC:13890](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13890) · Entrez [83737](https://www.ncbi.nlm.nih.gov/gene/83737) · UniProt [Q96J02](https://www.uniprot.org/uniprotkb/Q96J02) · Ensembl [ENSG00000078747](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078747)

## Data

Gene col 1231: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1231); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1231, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1231]; `tensor/DDL_lfc|DDL_z.npy` [1231]; `embed/gene_vectors.npy` [1231]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1231 or target_col == 1231). Every well: [[ITCH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITCH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
