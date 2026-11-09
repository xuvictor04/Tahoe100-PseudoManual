---
symbol: "KANSL1"
type: "gene"
col: 4156
ensembl_id: "ENSG00000120071"
name: "KAT8 regulatory NSL complex subunit 1"
location: "17q21.31"
module: 21
arm: "+"
pooled_cpm: 439.09
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 14
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# KANSL1

*KAT8 regulatory NSL complex subunit 1* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.23× (z +11.8, q 1e-29, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.306× (z -24.3, q 0e+00, down in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.351× (z -21.5, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (64 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 37 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPBP1L1]] (+0.67, fdr 1e-05), [[C2CD5-AS1]] (+0.66, fdr 1e-04), [[ZNF451-AS1]] (+0.65, fdr 2e-04).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ARL17B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4156.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.23×** | +11.8 | 1e-29 | 48/49 (NCI-H460, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.60×** | +9.7 | 1e-19 | 46/48 (C32, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +7.9 | 6e-13 | 38/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.28×** | +5.0 | 6e-05 | 34/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +4.9 | 1e-04 | 29/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.25×** | +4.6 | 4e-04 | 27/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.6 | 0.031 | 17/49 (SW1417, RKO, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.18× | +3.3 | 0.059 | 19/49 (HepG2/C3A, SHP-77, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.11× | +3.1 | 0.10 | 13/48 (SNU-1, A498, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4156.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.306×** | -24.3 | 0e+00 | 49/49 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.328×** | -22.0 | 0e+00 | 44/44 (NCI-H1792, CHP-212, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.351×** | -21.5 | 0e+00 | 48/48 (LOX-IMVI, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.360×** | -20.9 | 0e+00 | 48/48 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.418×** | -17.9 | 0e+00 | 48/48 (SNU-423, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.421×** | -16.4 | 0e+00 | 43/45 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.627×** | -9.6 | 9e-20 | 46/48 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.728×** | -6.5 | 5e-09 | 37/48 (SNU-423, A-172, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **0.734×** | -6.3 | 1e-08 | 41/48 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.830×** | -5.4 | 4e-06 | 24/48 (LOX-IMVI, CHP-212, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.789×** | -4.9 | 6e-05 | 29/48 (C32, NCI-H1573, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.791×** | -4.8 | 8e-05 | 28/48 (HCT15, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.796×** | -4.5 | 3e-04 | 28/47 (CFPAC-1, MIA PaCa-2, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 0.863× | -4.3 | 8e-04 | 10/48 (SNU-423, Panc 03.27, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.693×** | -3.7 | 0.008 | 31/49 (CFPAC-1, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4156. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 1,584 | 0 | 12 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0795× (z -31.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.171× (z -21.8) |
| [[LOX-IMVI (line)]] | wt | 396 | 3 | 8 (4 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.18× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.282× (z -20.7) |
| [[LoVo (line)]] | wt | 383 | 3 (1 ⚠) | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.15× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.234× (z -22.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.461× (z -12.3) |
| [[C32 (line)]] | wt | 260 | 1 | 8 (5 ⚠) | [[PH-797804 (drug)]] 5 µM 8.07× (z +14.6) | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -25.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.431× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 478 | 2 | 7 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 4.33× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.309× (z -18.3) |
| [[HOP62 (line)]] | alt | 641 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -20.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.254× (z -17.4) |
| [[HT-29 (line)]] | alt | 355 | 3 (1 ⚠) | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.93× (z +12.5) | [[Panobinostat (drug)]] 0.5 µM 0.305× (z -16.9) |
| [[J82 (line)]] | alt | 214 | 3 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +13.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.83× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.446× (z -13.2) |
| [[LS 180 (line)]] | wt | 315 | 3 | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.391× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 893 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -30.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.266× (z -18.3) |
| [[SW1417 (line)]] | alt | 308 | 1 (1 ⚠) | 8 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.300× (z -18.7) |
| [[A-172 (line)]] | wt | 284 | 1 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +14.4) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.339× (z -17.9) |
| [[A549 (line)]] | wt | 673 | 1 | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.77× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -24.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.285× (z -20.4) |
| [[HepG2_C3A (line)]] | wt | 401 | 1 | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.99× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.377× (z -13.3) |
| [[KATO III (line)]] | alt | 382 | 2 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.47× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.322× (z -17.2) |
| [[MIA PaCa-2 (line)]] | alt | 353 | 1 | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.15× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.194× (z -24.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.350× (z -16.4) |
| [[NCI-H1573 (line)]] | alt | 802 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.263× (z -13.0) |
| [[NCI-H2030 (line)]] | alt | 255 | 2 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.16× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.474× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 332 | 2 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.95× (z +14.4) | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -18.6) |
| [[Panc 03.27 (line)]] | alt | 505 | 2 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.34× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.318× (z -18.2) |
| [[SK-MEL-2 (line)]] | alt | 494 | 2 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.22× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.194× (z -24.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.355× (z -15.9) |
| [[SW480 (line)]] | alt | 538 | 2 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.71× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.187× (z -25.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.305× (z -18.9) |
| [[NCI-H2347 (line)]] | alt | 473 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.254× (z -16.5) |
| [[PANC-1 (line)]] | alt | 377 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -21.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.346× (z -16.5) |
| [[RPMI-7951 (line)]] | alt | 237 | 1 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.01× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.364× (z -14.0) |
| [[SNU-423 (line)]] | alt | 362 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.270× (z -21.3) |
| [[A-427 (line)]] | wt | 434 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.449× (z -11.2) |
| [[A498 (line)]] | wt | 360 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -21.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.370× (z -15.9) |
| [[AsPC-1 (line)]] | alt | 530 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.255× (z -15.8) |
| [[CHP-212 (line)]] | wt | 602 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0804× (z -28.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.249× (z -16.4) |
| [[COLO 205 (line)]] | alt | 478 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.99× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.319× (z -15.0) |
| [[H4 (line)]] | wt | 491 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.319× (z -12.6) |
| [[HS-578T (line)]] | alt | 214 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.378× (z -14.3) |
| [[hTERT-HPNE (line)]] | wt | 268 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.382× (z -12.9) |
| [[NCI-H23 (line)]] | alt | 391 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -20.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.370× (z -14.8) |
| [[RKO (line)]] | wt | 267 | 4 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +14.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.26× (z +13.1) | [[Panobinostat (drug)]] 0.5 µM 0.445× (z -10.9) |
| [[SHP-77 (line)]] | alt | 479 | 1 | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.430× (z -12.1) |
| [[SW 900 (line)]] | alt | 269 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.298× (z -15.5) |
| [[AN3 CA (line)]] | alt | 486 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0897× (z -23.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.422× (z -8.9) |
| [[C-33 A (line)]] | alt | 326 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.368× (z -13.4) |
| [[Hs 766T (line)]] | wt | 206 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.74× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.350× (z -14.0) |
| [[BT-474 (line)]] | alt | 188 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 3.58× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.413× (z -12.9) |
| [[HCT15 (line)]] | alt | 425 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -24.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.512× (z -8.5) |
| [[NCI-H661 (line)]] | alt | 285 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.154× (z -14.4) |
| [[SNU-1 (line)]] | wt | 299 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.86× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.506× (z -9.0) |
| [[SW48 (line)]] | wt | 435 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.00× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW 1088 (line)]] | alt | 385 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.194× (z -10.8) |
| [[SW 1271 (line)]] | alt | 524 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.300× (z -10.2) |
| [[NCI-H2122 (line)]] | alt | 492 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 458 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4156), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 37 of them with an alert (⚠; 36 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPBP1L1]] | +0.67 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[C2CD5-AS1]] | +0.66 | +0.36 / +0.45 | both halves | 1e-04 |  |
| [[ZNF451-AS1]] | +0.65 | +0.30 / +0.50 | both halves | 2e-04 |  |
| [[UBOX5-AS1]] | +0.65 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[CARNMT1-AS1]] | +0.65 | +0.33 / +0.42 | both halves | 1e-04 |  |
| [[SREK1IP1]] | +0.64 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[GEMIN7-AS1]] | +0.64 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[SPATA1]] | +0.64 | +0.16 / +0.52 | ⚠ one half (not replicated) | 0.001 |  |
| [[TICAM2-AS1]] | +0.63 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[HOXB-AS3]] | +0.62 | +0.30 / +0.51 | both halves | 2e-04 |  |
| [[C2orf76]] | +0.62 | +0.16 / +0.47 | ⚠ not reproduced | 0.001 |  |
| [[PAXBP1-AS1]] | +0.62 | +0.06 / +0.50 | ⚠ not reproduced | 0.004 |  |
| [[WDR20]] | +0.61 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[WDFY3]] | +0.61 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[MYLK3]] | +0.61 | +0.39 / +0.25 | both halves | 4e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARL17B]] | B | ARL17B activity raises KANSL1's level | lines that do not express ARL17B (25) vs lines expressing it (25) | 1.42× lower at baseline in the lines without ARL17B | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000290457, ENSG00000251598, AFAP1-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.1, 27.0); signed map (34.2, 2.0). **Vector** length 99.7, 40.1% of its response variance represented; |z| ≥ 3 in 1,362 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +14.2 | +3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +8.7 | +0.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.1 | -0.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.0 | +3.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.2 | +11.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.1 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +9.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.5 | -0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.9 | +0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.6 | +3.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.9 | -17.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.9 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -3.3 | -4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.2 | -21.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.8 | -20.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -3.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -5.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -0.2 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -1.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | KAT8 regulatory NSL complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:46,029,916-46,225,389 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP727C091, MSL1v1, CENP-36, NSL1; previously KIAA1267 |
| Gene groups (HGNC) | NSL histone acetyltransferase complex |
| Reactome | 6 pathways, smallest: Formation of WDR5-containing histone-modifying complexes; HATs acetylate histones; Epigenetic regulation by WDR5-containing histone modifying complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z3B3](https://www.uniprot.org/uniprotkb/Q7Z3B3) (KAT8 regulatory NSL complex subunit 1):

> Non-catalytic component of the NSL histone acetyltransferase complex, a multiprotein complex that mediates histone H4 acetylation at 'Lys-5'- and 'Lys-8' (H4K5ac and H4K8ac) at transcription start sites and promotes transcription initiation. The NSL complex also acts as a regulator of gene expression in mitochondria. In addition to its role in transcription, KANSL1 also plays an essential role in spindle assembly during mitosis. Associates with microtubule ends and contributes to microtubule …

**Summary**, from NCBI Gene [284058](https://www.ncbi.nlm.nih.gov/gene/284058):

> This gene encodes a nuclear protein that is a subunit of two protein complexes involved with histone acetylation, the MLL1 complex and the NSL1 complex. The encoded protein has been implicated in a variety of cellular processes including enhancer regulation, cell proliferation, and mitosis. Mutations in this gene are associated with Koolen-de Vries Syndrome. [provided by RefSeq, May 2022]

**Accessions** — [HGNC:24565](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24565) · Entrez [284058](https://www.ncbi.nlm.nih.gov/gene/284058) · UniProt [Q7Z3B3](https://www.uniprot.org/uniprotkb/Q7Z3B3) · Ensembl [ENSG00000120071](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120071)

## Data

Gene col 4156: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4156); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4156, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4156]; `tensor/DDL_lfc|DDL_z.npy` [4156]; `embed/gene_vectors.npy` [4156]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4156 or target_col == 4156). Every well: [[KANSL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KANSL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
