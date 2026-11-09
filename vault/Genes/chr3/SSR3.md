---
symbol: "SSR3"
type: "gene"
col: 3594
ensembl_id: "ENSG00000114850"
name: "signal sequence receptor subunit 3"
location: "3q25.31"
module: 42
arm: "+"
pooled_cpm: 121.14
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# SSR3

*signal sequence receptor subunit 3* — 3q25.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.34× (z +11.9, q 7e-30, up in 41 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.59× (z +6.7, q 3e-09, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.648× (z -9.0, q 2e-16, down in 36 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 12 lines (RKO 0.221×, J82 0.362×, A498 0.375×, NCI-H2030 0.319×, …); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A498 0.346×, RPMI-7951 0.230×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.356×; ⚠ cell-cycle shift, would explain all of this change); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 1 line (RKO 0.357×); [[Neratinib (drug)]] 5 µM in 1 line (SW 1088 0.0734×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSR1]] (+0.77, fdr 7e-06), [[SEC63]] (+0.71, fdr 7e-06), [[SRPRB]] (+0.71, fdr 7e-06); moves opposite to [[COQ7]] (-0.58, fdr 3e-05), [[SLC9A8]] (-0.54, fdr 1e-04), [[BAZ2B]] (-0.53, fdr 1e-04).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RPS6KA2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 13 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3594.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.34×** | +11.9 | 7e-30 | 41/44 (SNU-423, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.07×** | +10.0 | 6e-21 | 45/49 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +6.7 | 3e-09 | 38/48 (SW480, hTERT-HPNE, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.48×** | +5.7 | 2e-06 | 32/48 (SNU-423, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.62×** | +5.4 | 6e-06 | 34/45 (A-172, SHP-77, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.04×** | +5.4 | 6e-06 | 42/48 (SW480, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +5.2 | 2e-05 | 37/48 (SW480, NCI-H1792, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.40×** | +4.9 | 6e-05 | 33/48 (LS 180, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +4.8 | 9e-05 | 32/48 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +4.8 | 9e-05 | 31/49 (SK-MEL-2, H4, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.39×** | +4.8 | 9e-05 | 30/48 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.35×** | +4.3 | 7e-04 | 23/48 (PANC-1, SHP-77, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.34×** | +4.3 | 8e-04 | 24/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.34×** | +4.3 | 8e-04 | 29/48 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.33×** | +4.2 | 0.001 | 29/48 (H4, NCI-H23, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.65×** | +3.8 | 0.005 | 30/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **1.20×** | +3.7 | 0.006 | 21/49 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.59×** | +3.5 | 0.011 | 26/48 (CFPAC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.011 | 26/49 (NCI-H1792, SW480, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.019 | 27/48 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.55×** | +3.3 | 0.021 | 29/48 (NCI-H1573, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.026 | 23/48 (HS-578T, LOX-IMVI, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.036 | 22/48 (SW480, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[Lipoic acid (drug)]] 5 µM |  | 1.16× | +3.0 | 0.056 | 10/48 (PANC-1, HepG2/C3A, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.16× | +3.0 | 0.067 | 13/48 (SW1417, COLO 205, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3594.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 12 lines (RKO 0.221×, J82 0.362×, A498 0.375×, NCI-H2030 0.319×, …); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A498 0.346×, RPMI-7951 0.230×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.356×; ⚠ cell-cycle shift, would explain all of this change); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 1 line (RKO 0.357×); [[Neratinib (drug)]] 5 µM in 1 line (SW 1088 0.0734×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.648×** | -9.0 | 2e-16 | 36/48 (RKO, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.734×** | -6.4 | 4e-08 | 39/48 (RKO, J82, …) | rises with dose | low cells (technical?) |
| [[Anethole trithione (drug)]] 0.05 µM |  | 0.797× | -3.3 | 0.14 | 23/48 (KATO III, SW1417, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.853× | -3.3 | 0.14 | 21/48 (A498, RKO, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.802× | -3.1 | 0.22 | 20/47 (RKO, LOX-IMVI, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.675× | -3.0 | 0.23 | 22/50 (RKO, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3594. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 442 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -26.0) |
| [[A498 (line)]] | wt | 194 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.45× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -16.7) |
| [[A-172 (line)]] | wt | 132 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[HS-578T (line)]] | alt | 183 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 142 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -9.2) |
| [[J82 (line)]] | alt | 205 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.24× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -16.7) |
| [[LOX-IMVI (line)]] | wt | 216 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.36× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -13.5) |
| [[SW480 (line)]] | alt | 102 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.36× (z +9.8) | — |
| [[A549 (line)]] | wt | 94.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H1792 (line)]] | alt | 75.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.10× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[PANC-1 (line)]] | alt | 76.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.12× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[RPMI-7951 (line)]] | alt | 114 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 104 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.62× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -9.5) |
| [[SNU-423 (line)]] | alt | 69.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.24× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-427 (line)]] | wt | 179 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -10.9) |
| [[C-33 A (line)]] | alt | 65.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.97× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1573 (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.41× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2030 (line)]] | alt | 115 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -14.3) |
| [[NCI-H23 (line)]] | alt | 153 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H2347 (line)]] | alt | 138 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 78.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[Panc 03.27 (line)]] | alt | 130 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -9.2) |
| [[SHP-77 (line)]] | alt | 90.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[SNU-1 (line)]] | wt | 130 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -14.2) |
| [[SW 1088 (line)]] | alt | 88.6 | 0 | 1 | — | [[Neratinib (drug)]] 5 µM 0.0734× (z -9.5) |
| [[AN3 CA (line)]] | alt | 83.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 64.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 93.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 100.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 135 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 68.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 90.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 83.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 140 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 129 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 154 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 247 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 97.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 115 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3594), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSR1]] | +0.77 | +0.76 / +0.74 | both halves | 7e-06 | same gene group; pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 999 |
| [[SEC63]] | +0.71 | +0.66 / +0.65 | both halves | 7e-06 | STRING 533 |
| [[SRPRB]] | +0.71 | +0.71 / +0.68 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 631 |
| [[SEC61A1]] | +0.69 | +0.72 / +0.61 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 989 |
| [[PDIA5]] | +0.69 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[OSTC]] | +0.68 | +0.72 / +0.59 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 927 |
| [[TMED9]] | +0.67 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[SND1]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[HSPA5]] | +0.65 | +0.64 / +0.58 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum |
| [[SEC24D]] | +0.65 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[SLC31A1]] | +0.65 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[NFXL1]] | +0.64 | +0.65 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COQ7]] | -0.58 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[SLC9A8]] | -0.54 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[BAZ2B]] | -0.53 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[YJU2]] | -0.53 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[PNRC2]] | -0.53 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[LYRM2]] | -0.51 | -0.56 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPS6KA2]] | B | RPS6KA2 activity lowers SSR3's level | lines that do not express RPS6KA2 (6) vs lines expressing it (44) | 1.58× higher at baseline in the lines without RPS6KA2 | 0.048 | ⚠ within organs, on part of the lines; also absent: RAB20, FAM102A, LINC02100 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.695). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.6, -33.1); signed map (-53.3, 9.7). **Vector** length 117, 40.7% of its response variance represented; |z| ≥ 3 in 1,141 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.57 to 11); *Maturation of DENV proteins* (reactome, mean cos +0.51 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.50 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.6 | +2.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +5.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +4.2 | +5.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.0 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.8 | +4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +1.2 |
|  | [[Budesonide (drug)]] 5 µM |  | +3.2 | +0.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.5 | -9.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -6.5 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.2 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.5 | +0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | -0.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.4 | -2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.3 | -2.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | signal sequence receptor subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.31 — chr3:156,539,553-156,555,149 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRAPG |
| Gene groups (HGNC) | Translocon associated protein complex subunits |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 2 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNL2](https://www.uniprot.org/uniprotkb/Q9UNL2) (Translocon-associated protein subunit gamma):

> TRAP proteins are part of a complex whose function is to bind calcium to the ER membrane and thereby regulate the retention of ER resident proteins.

**Summary**, from NCBI Gene [6747](https://www.ncbi.nlm.nih.gov/gene/6747):

> The signal sequence receptor (SSR) is a glycosylated endoplasmic reticulum (ER) membrane receptor associated with protein translocation across the ER membrane. The SSR is comprised of four membrane proteins/subunits: alpha, beta, gamma, and delta. The first two are glycosylated subunits and the latter two are non-glycosylated subunits. This gene encodes the gamma subunit, which is predicted to span the membrane four times. [provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:11325](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11325) · Entrez [6747](https://www.ncbi.nlm.nih.gov/gene/6747) · UniProt [Q9UNL2](https://www.uniprot.org/uniprotkb/Q9UNL2) · Ensembl [ENSG00000114850](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114850)

## Data

Gene col 3594: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3594); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3594, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3594]; `tensor/DDL_lfc|DDL_z.npy` [3594]; `embed/gene_vectors.npy` [3594]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3594 or target_col == 3594). Every well: [[SSR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SSR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
