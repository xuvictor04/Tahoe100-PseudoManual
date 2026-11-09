---
symbol: "UACA"
type: "gene"
col: 6081
ensembl_id: "ENSG00000137831"
name: "uveal autoantigen with coiled-coil domains and ankyrin repeats"
location: "15q23"
module: 161
arm: "+"
pooled_cpm: 373.58
n_lines_expressing: 45
n_dd_up: 1
n_dd_down: 25
n_dd_up_clean: 1
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# UACA

*uveal autoantigen with coiled-coil domains and ankyrin repeats* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.26× (z +4.8, q 1e-03, up in 25 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (COLO 205 2.60×, LoVo 1.90×, C32 1.95×, A-172 2.60×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1573 2.45×, CFPAC-1 1.76×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (HT-29 2.27×, C32 2.28×; ⚠ cell-cycle shift, would explain all of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 2.26×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (HT-29 1.52×).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.539× (z -13.0, q 6e-36, down in 42 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VIM]] (+0.57, fdr 3e-05), [[ACTR1B]] (+0.55, fdr 2e-05), [[DRAP1]] (+0.55, fdr 2e-05); moves opposite to [[HEXA]] (-0.53, fdr 3e-05), [[TRMT11]] (-0.53, fdr 3e-05), [[UBXN8]] (-0.52, fdr 4e-05).
> It is in [[Module 161]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LRRC61]] → it (grade B ⚠); 3 go from it, the strongest it → [[RNF19A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6081.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (COLO 205 2.60×, LoVo 1.90×, C32 1.95×, A-172 2.60×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1573 2.45×, CFPAC-1 1.76×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (HT-29 2.27×, C32 2.28×; ⚠ cell-cycle shift, would explain all of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 2.26×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (HT-29 1.52×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.8 | 1e-03 | 25/43 (C32, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.7 | 0.064 | 21/45 (C32, C-33 A, …) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 1.11× | +3.3 | 0.17 | 2/43 (CFPAC-1, AN3 CA) | top dose only | position effect removed |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.20 | 13/43 (AsPC-1, HEC-1-A, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6081.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.539×** | -13.0 | 6e-36 | 42/43 (HOP62, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.566×** | -12.0 | 1e-30 | 42/43 (HOP62, HepG2/C3A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.346×** | -11.7 | 2e-29 | 42/44 (PANC-1, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.575×** | -11.2 | 5e-27 | 37/42 (HOP62, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.591×** | -10.4 | 2e-23 | 39/43 (HOP62, J82, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.619×** | -10.1 | 5e-22 | 41/43 (HOP62, J82, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.413×** | -9.8 | 1e-20 | 38/43 (SK-MEL-2, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.776×** | -7.5 | 4e-12 | 31/43 (J82, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.717×** | -7.0 | 2e-10 | 34/43 (HepG2/C3A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.719×** | -6.9 | 2e-10 | 36/43 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.731×** | -6.6 | 3e-09 | 35/43 (Hs 766T, H4, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.744×** | -6.2 | 3e-08 | 29/43 (HepG2/C3A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.757×** | -5.8 | 2e-07 | 26/43 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.605×** | -5.5 | 1e-06 | 29/40 (HOP62, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.845× | -5.0 | 3e-05 | 21/43 (HOP62, A549, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.796×** | -4.8 | 7e-05 | 26/43 (Hs 766T, A498, …) | inconsistent across doses | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.681×** | -4.2 | 8e-04 | 30/43 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.821×** | -4.1 | 0.001 | 21/43 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.707×** | -3.8 | 0.004 | 25/43 (MIA PaCa-2, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.779×** | -3.7 | 0.005 | 22/44 (HOP62, PANC-1, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6081. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 1,483 | 0 | 42 (17 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.140× (z -19.8) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.168× (z -18.7) |
| [[A549 (line)]] | wt | 963 | 0 | 17 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -22.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.281× (z -13.4) |
| [[PANC-1 (line)]] | alt | 1,330 | 0 | 17 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -23.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.353× (z -15.3) |
| [[HepG2_C3A (line)]] | wt | 463 | 0 | 16 (9 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.188× (z -19.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.226× (z -18.0) |
| [[J82 (line)]] | alt | 471 | 0 | 13 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.234× (z -13.9) |
| [[C32 (line)]] | wt | 304 | 4 (3 ⚠) | 8 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +11.4) | [[Ixazomib citrate (drug)]] 5 µM 0.443× (z -11.7) |
| [[HT-29 (line)]] | alt | 402 | 5 (4 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.52× (z +9.5) | [[Auranofin (drug)]] 5 µM 0.484× (z -11.6) |
| [[H4 (line)]] | wt | 346 | 0 | 6 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.264× (z -13.4) |
| [[HEC-1-A (line)]] | alt | 474 | 0 | 6 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.442× (z -10.6) |
| [[LoVo (line)]] | wt | 299 | 3 (3 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +13.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.519× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.335× (z -8.7) |
| [[HCT15 (line)]] | alt | 437 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.388× (z -9.8) |
| [[Hs 766T (line)]] | wt | 298 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.348× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 175 | 0 | 4 | — | [[Ixazomib citrate (drug)]] 5 µM 0.350× (z -14.9) |
| [[SK-MEL-2 (line)]] | alt | 307 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.422× (z -12.5) |
| [[A498 (line)]] | wt | 377 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.422× (z -9.5) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.452× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 413 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.355× (z -12.2) |
| [[COLO 205 (line)]] | alt | 249 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +15.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.453× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 489 | 0 | 3 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.339× (z -14.7) |
| [[NCI-H23 (line)]] | alt | 175 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.54× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.394× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 212 | 0 | 3 | — | [[TAK-901 (drug)]] 5 µM 0.333× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 172 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.481× (z -9.0) |
| [[LS 180 (line)]] | wt | 260 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[PH-797804 (drug)]] 5 µM 0.247× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 121 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +17.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1792 (line)]] | alt | 296 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.473× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.306× (z -9.5) |
| [[SNU-423 (line)]] | alt | 252 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.491× (z -9.2) |
| [[SW 900 (line)]] | alt | 212 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.446× (z -10.6) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.460× (z -10.6) |
| [[A-172 (line)]] | wt | 154 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +13.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 97.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.398× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 170 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 774 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.270× (z -8.9) |
| [[KATO III (line)]] | alt | 232 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.335× (z -8.8) |
| [[NCI-H661 (line)]] | alt | 1,151 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 252 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.274× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 280 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.433× (z -10.5) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 948 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.294× (z -8.8) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 247 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 93.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 184 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 276 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 257 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 282 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 82.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 27.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 83.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 312 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 167 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6081), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VIM]] | +0.57 | +0.52 / +0.45 | both halves | 3e-05 | pathway: Apoptosis |
| [[ACTR1B]] | +0.55 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[DRAP1]] | +0.55 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[SMC4]] | +0.54 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[CSMD2]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[HJURP]] | +0.53 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[NBPF10]] | +0.52 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[TEAD1]] | +0.52 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[PPFIBP1]] | +0.52 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[NBPF14]] | +0.51 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[DPF3]] | +0.50 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[IQCJ-SCHIP1]] | +0.50 | +0.46 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEXA]] | -0.53 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[TRMT11]] | -0.53 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[UBXN8]] | -0.52 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[KEAP1]] | -0.48 | -0.53 / -0.36 | both halves | 9e-05 |  |
| [[JRK]] | -0.48 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[MGST1]] | -0.48 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[UBE2L3]] | -0.48 | -0.45 / -0.41 | both halves | 4e-05 | pathway: Programmed Cell Death |
| [[NAGPA]] | -0.48 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[SMG5]] | -0.48 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[LRRC61]] | -0.47 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[MED28]] | -0.47 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[MRPS15]] | -0.47 | -0.43 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC61]] | B | LRRC61 activity lowers UACA's level | lines that do not express LRRC61 (16) vs lines expressing it (34) | 1.91× higher at baseline in the lines without LRRC61 | 0.034 | ⚠ within organs, on part of the lines; also absent: ACTR3C, ARHGEF5, ENPP4 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF19A]] | B | UACA activity lowers RNF19A's level | lines that do not express UACA (5) vs lines expressing it (45) | 1.74× higher at baseline in the lines without UACA | 0.060 | ⚠ within organs, on part of the lines; also absent: IGF2BP2, PNCK, SPTBN5; maybe low, not absent |
| [[SYNJ2]] | B | UACA activity raises SYNJ2's level | lines that do not express UACA (5) vs lines expressing it (45) | 3.09× lower at baseline in the lines without UACA | 0.080 | ⚠ within organs, on part of the lines; also absent: IGF2BP2, PNCK, SPTBN5; maybe low, not absent |
| [[LRRC61]] | B | UACA activity lowers LRRC61's level | lines that do not express UACA (5) vs lines expressing it (45) | 2.59× higher at baseline in the lines without UACA | 0.087 | ⚠ within organs, on part of the lines; also absent: IGF2BP2, PNCK, SPTBN5; maybe low, not absent |

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.243). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.8, -5.4); signed map (-7.1, 41.3). **Vector** length 132, 42.6% of its response variance represented; |z| ≥ 3 in 1,613 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +2.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.7 | +0.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.5 | +3.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +4.2 | +1.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.5 | +2.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +3.0 | +3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +1.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.7 | +1.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.7 | +2.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -11.1 | -11.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -10.3 | -7.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -8.3 | -13.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -7.7 | -10.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.6 | -12.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.9 | -10.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.5 | -9.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.8 | -4.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | uveal autoantigen with coiled-coil domains and ankyrin repeats |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:70,654,554-70,763,558 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10128, KIAA1561 |
| Gene groups (HGNC) | N-Ank proteins |
| Reactome | 11 pathways, smallest: Formation of apoptosome; Regulation of the apoptosome activity; Cytochrome c-mediated apoptotic response |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZF9](https://www.uniprot.org/uniprotkb/Q9BZF9) (Uveal autoantigen with coiled-coil domains and ankyrin repeats):

> Regulates APAF1 expression and plays an important role in the regulation of stress-induced apoptosis. Promotes apoptosis by regulating three pathways, apoptosome up-regulation, LGALS3/galectin-3 down-regulation and NF-kappa-B inactivation. Regulates the redistribution of APAF1 into the nucleus after pro-apoptotic stress. Down-regulates the expression of LGALS3 by inhibiting NFKB1 (By similarity).; Modulates isoactin dynamics to regulate the morphological alterations required for cell growth and …

**Summary**, from NCBI Gene [55075](https://www.ncbi.nlm.nih.gov/gene/55075):

> This gene encodes a protein that contains ankyrin repeats and coiled coil domains and likely plays a role in apoptosis. Studies in rodents have implicated the encoded protein in the stimulation of apoptosis and the regulation of mammary gland involution, in which the mammary gland returns to its pre-pregnant state. This protein has also been proposed to negatively regulate apoptosis based on experiments in human cell lines in which the protein was shown to interact with PRKC apoptosis WT1 …

**Accessions** — [HGNC:15947](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15947) · Entrez [55075](https://www.ncbi.nlm.nih.gov/gene/55075) · UniProt [Q9BZF9](https://www.uniprot.org/uniprotkb/Q9BZF9) · Ensembl [ENSG00000137831](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137831)

## Data

Gene col 6081: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6081); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6081, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6081]; `tensor/DDL_lfc|DDL_z.npy` [6081]; `embed/gene_vectors.npy` [6081]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6081 or target_col == 6081). Every well: [[UACA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UACA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
