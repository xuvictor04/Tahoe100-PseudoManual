---
symbol: "P4HB"
type: "gene"
col: 11704
ensembl_id: "ENSG00000185624"
name: "prolyl 4-hydroxylase subunit beta"
location: "17q25.3"
module: 42
arm: "+"
pooled_cpm: 469.48
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 18
n_dd_up_clean: 12
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# P4HB

*prolyl 4-hydroxylase subunit beta* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.75× (z +7.8, q 4e-12, up in 38 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.56× (z +6.1, q 2e-07, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.437× (z -15.0, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDIA4]] (+0.87, fdr 7e-06), [[HSP90B1]] (+0.85, fdr 7e-06), [[TMED9]] (+0.85, fdr 7e-06); moves opposite to [[RNF115]] (-0.64, fdr 2e-05), [[GTF3C6]] (-0.64, fdr 3e-05), [[THOC7]] (-0.61, fdr 3e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11704.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.75×** | +7.8 | 4e-12 | 38/49 (A-427, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +6.1 | 2e-07 | 40/48 (J82, SW480, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.50×** | +5.4 | 1e-05 | 32/44 (SNU-423, A498, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.44×** | +5.0 | 7e-05 | 36/48 (SW480, J82, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.98×** | +4.9 | 9e-05 | 43/48 (Hs 766T, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +4.8 | 1e-04 | 38/48 (Panc 03.27, SW480, …) | top dose only |  |
| [[Larotrectinib (drug)]] 0.5 µM |  | **1.38×** | +4.4 | 9e-04 | 42/49 (NCI-H2347, A498, …) | inconsistent across doses | position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.53×** | +4.2 | 0.002 | 38/48 (C-33 A, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +4.1 | 0.003 | 34/48 (SW480, SHP-77, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.32×** | +3.9 | 0.007 | 26/48 (SW480, SHP-77, …) | top dose only | position effect removed |
| [[EX229 (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.010 | 38/49 (NCI-H1792, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 0.05 µM |  | **1.30×** | +3.4 | 0.035 | 34/48 (A498, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[EX229 (drug)]] 0.05 µM |  | **1.29×** | +3.3 | 0.039 | 27/48 (LoVo, NCI-H1792, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.039 | 35/48 (C-33 A, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.29×** | +3.2 | 0.049 | 28/45 (A-427, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **1.54×** | +3.1 | 0.063 | 28/48 (RPMI-7951, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.067 | 33/48 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11704.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.437×** | -15.0 | 0e+00 | 46/48 (NCI-H2347, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.430×** | -11.7 | 5e-29 | 46/48 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.494×** | -9.4 | 1e-18 | 47/48 (A-172, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.623×** | -8.4 | 4e-15 | 45/48 (A-427, AsPC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.687×** | -5.0 | 7e-05 | 40/49 (A498, SW 900, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.698×** | -4.8 | 2e-04 | 28/47 (C-33 A, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.712×** | -4.4 | 7e-04 | 38/47 (HOP62, SW 900, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.788×** | -4.4 | 7e-04 | 31/48 (SW 900, A498, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.736×** | -4.2 | 0.001 | 41/48 (hTERT-HPNE, SW 900, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.750×** | -4.0 | 0.004 | 35/48 (A-427, C-33 A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.751×** | -4.0 | 0.004 | 37/48 (SW 900, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.774×** | -3.5 | 0.018 | 25/48 (A-172, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.725×** | -3.5 | 0.018 | 33/48 (A-427, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.786×** | -3.2 | 0.055 | 27/47 (SW 900, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | **0.831×** | -3.2 | 0.058 | 23/48 (C32, Panc 03.27, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.792×** | -3.1 | 0.067 | 25/48 (SW 900, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.762×** | -3.0 | 0.090 | 25/49 (LS 180, HT-29, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.806×** | -3.0 | 0.090 | 28/48 (SW 900, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11704. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 283 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -22.6) |
| [[A498 (line)]] | wt | 698 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.360× (z -14.9) |
| [[AsPC-1 (line)]] | alt | 304 | 2 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +12.7) ⚠ cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 5 µM 0.557× (z -9.1) |
| [[SW480 (line)]] | alt | 307 | 4 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.81× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -9.2) |
| [[A-172 (line)]] | wt | 586 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -19.3) |
| [[J82 (line)]] | alt | 514 | 2 | 2 | [[Panobinostat (drug)]] 5 µM 2.40× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -16.1) |
| [[LOX-IMVI (line)]] | wt | 326 | 1 | 3 | [[Panobinostat (drug)]] 0.5 µM 2.36× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -13.7) |
| [[RPMI-7951 (line)]] | alt | 384 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -14.4) |
| [[SNU-423 (line)]] | alt | 424 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.415× (z -9.5) |
| [[BT-474 (line)]] | alt | 412 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -16.7) |
| [[C-33 A (line)]] | alt | 266 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -12.7) |
| [[C32 (line)]] | wt | 455 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -12.9) |
| [[H4 (line)]] | wt | 801 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -19.8) |
| [[HS-578T (line)]] | alt | 727 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -18.2) |
| [[NCI-H2347 (line)]] | alt | 482 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -20.9) |
| [[Panc 03.27 (line)]] | alt | 354 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.56× (z +12.2) | — |
| [[PANC-1 (line)]] | alt | 332 | 2 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +9.6) ⚠ cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 292 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -13.7) |
| [[SW 900 (line)]] | alt | 861 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.424× (z -10.0) |
| [[A549 (line)]] | wt | 375 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -12.8) |
| [[HCT15 (line)]] | alt | 1,173 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 372 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -10.2) |
| [[HOP62 (line)]] | alt | 678 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -19.7) |
| [[hTERT-HPNE (line)]] | wt | 887 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -13.0) |
| [[NCI-H1573 (line)]] | alt | 434 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.315× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 659 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -13.1) |
| [[NCI-H661 (line)]] | alt | 274 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -11.1) |
| [[RKO (line)]] | wt | 392 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -20.3) |
| [[AN3 CA (line)]] | alt | 220 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[CFPAC-1 (line)]] | alt | 582 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -10.8) |
| [[CHP-212 (line)]] | wt | 510 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -11.2) |
| [[HT-29 (line)]] | alt | 453 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -12.2) |
| [[KATO III (line)]] | alt | 716 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.383× (z -10.4) |
| [[LoVo (line)]] | wt | 353 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.336× (z -10.3) |
| [[LS 180 (line)]] | wt | 443 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 539 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.218× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 808 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.335× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 250 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -12.7) |
| [[SHP-77 (line)]] | alt | 357 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.22× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 308 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -15.7) |
| [[SW 1088 (line)]] | alt | 610 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -11.8) |
| [[SW48 (line)]] | wt | 346 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -11.2) |
| [[COLO 205 (line)]] | alt | 554 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 358 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 304 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 439 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 407 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 468 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 249 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 289 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11704), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDIA4]] | +0.87 | +0.87 / +0.81 | both halves | 7e-06 | same gene group; STRING 799 |
| [[HSP90B1]] | +0.85 | +0.87 / +0.79 | both halves | 7e-06 | pathway: Post-translational protein phosphorylation; STRING 983 |
| [[TMED9]] | +0.85 | +0.84 / +0.78 | both halves | 7e-06 | STRING 499 |
| [[CALU]] | +0.82 | +0.81 / +0.79 | both halves | 7e-06 | pathway: Post-translational protein phosphorylation; STRING 872 |
| [[LMAN1]] | +0.79 | +0.82 / +0.74 | both halves | 7e-06 | STRING 520 |
| [[CALR]] | +0.79 | +0.77 / +0.71 | both halves | 7e-06 | pathway: Dengue Virus Genome Translation and Replication; STRING 994 |
| [[SLC31A1]] | +0.79 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[HSPA5]] | +0.78 | +0.79 / +0.70 | both halves | 7e-06 | pathway: Dengue Virus Genome Translation and Replication; STRING 996 |
| [[SEC61A1]] | +0.77 | +0.78 / +0.80 | both halves | 7e-06 | STRING 855 |
| [[SLC35E1]] | +0.76 | +0.83 / +0.66 | both halves | 7e-06 |  |
| [[MANF]] | +0.76 | +0.70 / +0.72 | both halves | 7e-06 | STRING 406 |
| [[KDELR2]] | +0.74 | +0.73 / +0.78 | both halves | 7e-06 | STRING 420 |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF115]] | -0.64 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[GTF3C6]] | -0.64 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[THOC7]] | -0.61 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[MIER3]] | -0.61 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[WAC-AS1]] | -0.61 | -0.60 / -0.35 | both halves | 1e-04 |  |
| [[FAIM]] | -0.61 | -0.61 / -0.37 | both halves | 8e-05 |  |
| [[DCUN1D1]] | -0.61 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[ITPA]] | -0.61 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[ZFY]] | -0.61 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[AASDHPPT]] | -0.60 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[USP24]] | -0.60 | -0.32 / -0.52 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.852). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.2, -31.1); signed map (-53.7, 7.9). **Vector** length 168, 65.8% of its response variance represented; |z| ≥ 3 in 1,234 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.73 to 11); *Asparagine N-linked glycosylation* (reactome, mean cos +0.52 to 23); *Cargo concentration in the ER* (reactome, mean cos +0.56 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +10.8 | +6.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +10.5 | +5.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +8.9 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +4.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.8 | +4.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.4 | +4.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +4.1 | +4.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.0 | +3.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +3.5 | +2.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -11.0 | -9.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -10.9 | -8.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.2 | -11.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.9 | -15.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.8 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.8 | -3.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.7 | -4.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.6 | -2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -4.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | prolyl 4-hydroxylase subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:81,843,159-81,860,856 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PDIA1, PROHB, DSI, GIT, PDI, PO4HB, P4Hbeta; previously PO4DB, ERBA2L |
| Gene groups (HGNC) | Protein disulfide isomerases; Prolyl 4-hydroxylase subunits |
| Reactome | 28 pathways, smallest: VLDL assembly; Chylomicron assembly; Interleukin-23 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P07237](https://www.uniprot.org/uniprotkb/P07237) (Protein disulfide-isomerase):

> This multifunctional protein catalyzes the formation, breakage and rearrangement of disulfide bonds. At the cell surface, seems to act as a reductase that cleaves disulfide bonds of proteins attached to the cell. May therefore cause structural modifications of exofacial proteins. Inside the cell, seems to form/rearrange disulfide bonds of nascent proteins. At high concentrations and following phosphorylation by FAM20C, functions as a chaperone that inhibits aggregation of misfolded proteins. At …

**Summary**, from NCBI Gene [5034](https://www.ncbi.nlm.nih.gov/gene/5034):

> This gene encodes the beta subunit of prolyl 4-hydroxylase, a highly abundant multifunctional enzyme that belongs to the protein disulfide isomerase family. When present as a tetramer consisting of two alpha and two beta subunits, this enzyme is involved in hydroxylation of prolyl residues in preprocollagen. This enzyme is also a disulfide isomerase containing two thioredoxin domains that catalyze the formation, breakage and rearrangement of disulfide bonds. Other known functions include its …

**Accessions** — [HGNC:8548](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8548) · Entrez [5034](https://www.ncbi.nlm.nih.gov/gene/5034) · UniProt [P07237](https://www.uniprot.org/uniprotkb/P07237) · Ensembl [ENSG00000185624](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185624)

## Data

Gene col 11704: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11704); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11704, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11704]; `tensor/DDL_lfc|DDL_z.npy` [11704]; `embed/gene_vectors.npy` [11704]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11704 or target_col == 11704). Every well: [[P4HB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/P4HB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
