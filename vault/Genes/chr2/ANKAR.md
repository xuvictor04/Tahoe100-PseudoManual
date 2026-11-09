---
symbol: "ANKAR"
type: "gene"
col: 7549
ensembl_id: "ENSG00000151687"
name: "ankyrin and armadillo repeat containing"
location: "2q32.2"
module: 39
arm: "+"
pooled_cpm: 25.15
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 16
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# ANKAR

*ankyrin and armadillo repeat containing* — 2q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.53× (z +7.1, q 1e-09, up in 40 of 48 measured lines) ⚠ cell-cycle shift, explains ~75% of this change. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.56× (z +4.8, q 4e-04, up in 31 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 4.29×, A498 4.91×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (AsPC-1 3.62×; ⚠ cell-cycle shift, explains ~75% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 2.18×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (14 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.379× (z -11.3, q 1e-26, down in 42 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.628× (z -5.4, q 4e-06, down in 28 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (PANC-1 0.162×, LOX-IMVI 0.135×, SW480 0.237×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 3 lines (J82 0.0824×, AN3 CA 0.0292×, NCI-H460 0.201×; ⚠ cell-cycle shift, explains ~37% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (SNU-423 0.0994×, SW480 0.217×, PANC-1 0.207×; ⚠ cell-cycle shift, explains ~44% of this change); [[Belinostat (drug)]] 0.5 µM in 2 lines (RKO 0.207×, SNU-423 0.207×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (Panc 03.27 0.180×); [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM in 1 line (COLO 205 0.156×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKDD1B]] (+0.73, fdr 1e-05), [[MSH4]] (+0.72, fdr 1e-05), [[PLAC8L1]] (+0.69, fdr 1e-05); moves opposite to [[DNAAF3]] (-0.63, fdr 1e-04), [[LIFR]] (-0.61, fdr 5e-05), [[FOXO6]] (-0.58, fdr 1e-04).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SCUBE2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7549.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 4.29×, A498 4.91×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (AsPC-1 3.62×; ⚠ cell-cycle shift, explains ~75% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 2.18×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.53×** | +7.1 | 1e-09 | 40/48 (AsPC-1, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +4.8 | 4e-04 | 31/47 (RKO, HT-29, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.3 | 0.003 | 25/45 (A-172, RKO, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Ponatinib (drug)]] 5 µM |  | 1.30× | +3.1 | 0.26 | 21/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.30× | +3.0 | 0.26 | 13/48 (KATO III, C-33 A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 14 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7549.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (PANC-1 0.162×, LOX-IMVI 0.135×, SW480 0.237×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 3 lines (J82 0.0824×, AN3 CA 0.0292×, NCI-H460 0.201×; ⚠ cell-cycle shift, explains ~37% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (SNU-423 0.0994×, SW480 0.217×, PANC-1 0.207×; ⚠ cell-cycle shift, explains ~44% of this change); [[Belinostat (drug)]] 0.5 µM in 2 lines (RKO 0.207×, SNU-423 0.207×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (Panc 03.27 0.180×); [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM in 1 line (COLO 205 0.156×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.379×** | -11.3 | 1e-26 | 42/47 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.423×** | -10.0 | 5e-21 | 39/48 (SNU-423, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.480×** | -8.5 | 3e-15 | 40/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.472×** | -8.4 | 7e-15 | 35/47 (LOX-IMVI, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.506×** | -7.9 | 3e-13 | 40/48 (J82, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.562×** | -6.7 | 2e-09 | 37/48 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.582×** | -6.0 | 1e-07 | 29/48 (HOP62, PANC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.611×** | -5.7 | 7e-07 | 31/48 (RKO, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.717×** | -5.4 | 3e-06 | 25/47 (A-427, SNU-423, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.628×** | -5.4 | 4e-06 | 28/47 (RKO, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.643×** | -5.1 | 2e-05 | 26/48 (LoVo, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.687×** | -4.4 | 6e-04 | 24/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.685×** | -4.1 | 0.002 | 23/43 (NCI-H1573, A-427, …) | inconsistent across doses | composition shift |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.703×** | -3.9 | 0.003 | 24/47 (Panc 03.27, NCI-H2030, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **0.735×** | -3.6 | 0.014 | 18/46 (A-172, PANC-1, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7549. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 38.0 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0467× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 29.3 | 2 (2 ⚠) | 6 (6 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.201× (z -12.9) ⚠ cell-cycle shift, explains ~37% of this change |
| [[PANC-1 (line)]] | alt | 29.8 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.162× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[H4 (line)]] | wt | 32.3 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H1573 (line)]] | alt | 28.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 27.3 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.217× (z -13.4) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A-427 (line)]] | wt | 36.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -13.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 30.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.91× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 36.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 31.9 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.192× (z -11.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.207× (z -10.6) |
| [[SNU-423 (line)]] | alt | 18.5 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0994× (z -13.7) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.207× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 38.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[J82 (line)]] | alt | 19.8 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0824× (z -14.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[LoVo (line)]] | wt | 30.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.327× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[LS 180 (line)]] | wt | 24.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.04× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 32.6 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.218× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[A-172 (line)]] | wt | 27.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 30.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 33.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0292× (z -13.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[AsPC-1 (line)]] | alt | 13.5 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.62× (z +9.1) ⚠ cell-cycle shift, explains ~75% of this change | — |
| [[C-33 A (line)]] | alt | 35.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.168× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[COLO 205 (line)]] | alt | 24.3 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.156× (z -9.0) |
| [[HOP62 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.215× (z -8.9) ⚠ cell-cycle shift, explains ~74% of this change |
| [[hTERT-HPNE (line)]] | wt | 29.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.125× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H2030 (line)]] | alt | 33.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.234× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[Panc 03.27 (line)]] | alt | 17.3 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.180× (z -9.5) |
| [[SHP-77 (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[BT-474 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7549), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKDD1B]] | +0.73 | +0.75 / +0.53 | both halves | 1e-05 | same gene group |
| [[MSH4]] | +0.72 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[PLAC8L1]] | +0.69 | +0.70 / +0.49 | both halves | 1e-05 |  |
| [[KANSL1L-AS1]] | +0.69 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[BAAT]] | +0.69 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[LINC01355]] | +0.67 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[EEF1AKMT1]] | +0.67 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[SMIM15-AS1]] | +0.67 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[SHLD1]] | +0.66 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[RAPSN]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[PCBD2]] | +0.66 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ZNF37A]] | +0.65 | +0.61 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF3]] | -0.63 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[LIFR]] | -0.61 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[FOXO6]] | -0.58 | -0.45 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCUBE2]] | B | SCUBE2 activity raises ANKAR's level | lines that do not express SCUBE2 (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without SCUBE2 | 0.048 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent |
| [[HMSD]] | B | HMSD activity raises ANKAR's level | lines that do not express HMSD (26) vs lines expressing it (24) | 1.23× lower at baseline in the lines without HMSD | 0.055 | ⚠ within organs, on part of the lines; also absent: LGSN, LRRN2, HEYL |
| [[SPOCK2]] | B | SPOCK2 activity raises ANKAR's level | lines that do not express SPOCK2 (6) vs lines expressing it (44) | 1.48× lower at baseline in the lines without SPOCK2 | 0.059 | ⚠ within organs, on part of the lines; also absent: UACA, MPP4, GLIPR2; maybe low, not absent |
| [[NR3C2]] | B | NR3C2 activity lowers ANKAR's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.31× higher at baseline in the lines without NR3C2 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.632). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.3, -11.9); signed map (16.8, 3.6). **Vector** length 95.5, 23.7% of its response variance represented; |z| ≥ 3 in 1,091 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +8.2 | +7.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.7 | +4.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.3 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.0 | +4.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.9 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | +0.5 |
|  | [[EX229 (drug)]] 5 µM |  | +3.7 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.4 | +2.4 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -5.1 | -6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -4.9 | -5.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | -4.6 | -3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -4.1 | -5.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.0 | -5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.8 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -2.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.6 | -2.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.5 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin and armadillo repeat containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.2 — chr2:189,674,290-189,761,193 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25415 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Armadillo repeat containing |
| Matched by | ensembl_id |

UniProt [Q7Z5J8](https://www.uniprot.org/uniprotkb/Q7Z5J8) carries no function annotation.

**Summary**, from NCBI Gene [150709](https://www.ncbi.nlm.nih.gov/gene/150709):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26350](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26350) · Entrez [150709](https://www.ncbi.nlm.nih.gov/gene/150709) · UniProt [Q7Z5J8](https://www.uniprot.org/uniprotkb/Q7Z5J8) · Ensembl [ENSG00000151687](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151687)

## Data

Gene col 7549: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7549); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7549, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7549]; `tensor/DDL_lfc|DDL_z.npy` [7549]; `embed/gene_vectors.npy` [7549]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7549 or target_col == 7549). Every well: [[ANKAR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKAR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
