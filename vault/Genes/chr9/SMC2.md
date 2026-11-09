---
symbol: "SMC2"
type: "gene"
col: 5910
ensembl_id: "ENSG00000136824"
name: "structural maintenance of chromosomes 2"
location: "9q31.1"
module: 22
arm: "+"
pooled_cpm: 110.0
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 13
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# SMC2

*structural maintenance of chromosomes 2* — 9q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.99× (z +13.9, q 5e-41, up in 46 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.05 µM: 1.40× (z +4.0, q 0.007, up in 35 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (A549 4.98×, PANC-1 3.67×, A498 3.87×, NCI-H1792 3.73×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (A549 4.15×, PANC-1 3.54×, SW480 3.29×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A549 2.17×).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.586× (z -6.4, q 1e-07, down in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.750× (z -5.1, q 9e-05, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZGRF1]] (+0.78, fdr 7e-06), [[KIF15]] (+0.76, fdr 7e-06), [[NCAPG]] (+0.76, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MYBL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5910.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (A549 4.98×, PANC-1 3.67×, A498 3.87×, NCI-H1792 3.73×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (A549 4.15×, PANC-1 3.54×, SW480 3.29×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A549 2.17×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.99×** | +13.9 | 5e-41 | 46/49 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.96×** | +13.2 | 2e-37 | 43/44 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.87×** | +7.3 | 4e-11 | 39/45 (NCI-H2347, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.45×** | +4.8 | 3e-04 | 32/48 (NCI-H1792, A549, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.30×** | +4.7 | 3e-04 | 36/48 (HT-29, HS-578T, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.40×** | +4.0 | 0.007 | 35/47 (A549, NCI-H1792, …) | all doses, flat | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.29×** | +3.3 | 0.076 | 26/48 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.3 | 0.076 | 27/48 (A549, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.30×** | +3.2 | 0.076 | 26/48 (A549, NCI-H1792, …) | all doses, flat | composition shift |
| [[Thymol (drug)]] 5 µM |  | 1.19× | +3.1 | 0.11 | 16/48 (NCI-H23, A-427, …) | top dose only |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 1.18× | +3.1 | 0.11 | 16/49 (SW 900, HT-29, …) | rises with dose | position effect removed |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.18× | +3.0 | 0.11 | 13/49 (NCI-H1573, H4, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5910.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.586×** | -6.4 | 1e-07 | 43/48 (A-172, H4, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.750×** | -5.1 | 9e-05 | 29/48 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.499×** | -4.6 | 8e-04 | 33/45 (H4, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.777×** | -4.5 | 0.001 | 28/48 (A498, A-427, …) | rises with dose | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.779×** | -4.4 | 0.001 | 35/48 (HCT15, H4, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.741×** | -3.8 | 0.016 | 29/48 (A-172, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.746×** | -3.7 | 0.017 | 26/48 (SHP-77, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.813×** | -3.7 | 0.017 | 28/48 (COLO 205, RPMI-7951, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.758×** | -3.5 | 0.029 | 26/48 (SHP-77, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.759×** | -3.5 | 0.029 | 27/48 (A-172, A498, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.750×** | -3.4 | 0.032 | 30/48 (Hs 766T, LoVo, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.654×** | -3.4 | 0.037 | 29/48 (KATO III, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.620×** | -3.1 | 0.072 | 27/49 (Hs 766T, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5910. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 177 | 2 (2 ⚠) | 4 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Selinexor (drug)]] 5 µM 0.418× (z -12.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 128 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Selinexor (drug)]] 5 µM 0.344× (z -13.4) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 91.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -18.0) |
| [[NCI-H1573 (line)]] | alt | 64.2 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -12.9) |
| [[A549 (line)]] | wt | 85.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.98× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.3) | — |
| [[HCT15 (line)]] | alt | 161 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -9.8) |
| [[HT-29 (line)]] | alt | 70.7 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +10.8) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H2347 (line)]] | alt | 78.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H460 (line)]] | wt | 102 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Selinexor (drug)]] 5 µM 0.529× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 172 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.22× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -10.9) |
| [[SW1417 (line)]] | alt | 87.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[SW480 (line)]] | alt | 135 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[H4 (line)]] | wt | 129 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -12.1) |
| [[HOP62 (line)]] | alt | 96.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[Hs 766T (line)]] | wt | 162 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[HS-578T (line)]] | alt | 80.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 65.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[KATO III (line)]] | alt | 120 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[LoVo (line)]] | wt | 62.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H1792 (line)]] | alt | 80.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H2030 (line)]] | alt | 74.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[Panc 03.27 (line)]] | alt | 85.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[PANC-1 (line)]] | alt | 86.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[SNU-423 (line)]] | alt | 137 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[SW 900 (line)]] | alt | 84.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[A-427 (line)]] | wt | 127 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.354× (z -13.0) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 178 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 56.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.02× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[COLO 205 (line)]] | alt | 77.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.296× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 186 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[LOX-IMVI (line)]] | wt | 144 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.529× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 89.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H23 (line)]] | alt | 138 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[SHP-77 (line)]] | alt | 158 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[SNU-1 (line)]] | wt | 98.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 169 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 76.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 164 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5910), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZGRF1]] | +0.78 | +0.75 / +0.80 | both halves | 7e-06 |  |
| [[KIF15]] | +0.76 | +0.76 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 840 |
| [[NCAPG]] | +0.76 | +0.74 / +0.74 | both halves | 7e-06 | same gene group; pathway: Condensation of Prometaphase Chromosomes; STRING 999 |
| [[SMC4]] | +0.75 | +0.73 / +0.76 | both halves | 7e-06 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 999 |
| [[CIP2A]] | +0.75 | +0.72 / +0.75 | both halves | 7e-06 | STRING 633 |
| [[SGO1]] | +0.74 | +0.70 / +0.77 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 445 |
| [[ATAD5]] | +0.73 | +0.72 / +0.71 | both halves | 7e-06 | STRING 874 |
| [[KIF11]] | +0.73 | +0.71 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 967 |
| [[CENPU]] | +0.72 | +0.69 / +0.71 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 420 |
| [[ESCO2]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 | STRING 759 |
| [[RAD51AP1]] | +0.72 | +0.69 / +0.72 | both halves | 7e-06 | STRING 779 |
| [[PLK4]] | +0.72 | +0.71 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 691 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYBL1]] | B | MYBL1 activity raises SMC2's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.83× lower at baseline in the lines without MYBL1 | 0.036 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[ZNF724]] | B | ZNF724 activity raises SMC2's level | lines that do not express ZNF724 (8) vs lines expressing it (42) | 1.31× lower at baseline in the lines without ZNF724 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000283201, ENSG00000269237, ZNF577 |
| [[E2F8]] | B | E2F8 activity raises SMC2's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 1.83× lower at baseline in the lines without E2F8 | 0.089 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises SMC2's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.28× lower at baseline in the lines without NDC80 | 0.020 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises SMC2's level | lines that do not express AURKB (4) vs lines expressing it (46) | 1.94× lower at baseline in the lines without AURKB | 0.096 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.648). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-39.5, -50.7); signed map (-45.8, -46.7). **Vector** length 119, 44.8% of its response variance represented; |z| ≥ 3 in 1,015 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.53 to 28); *E2F targets* (hallmark, mean cos +0.51 to 46); *Resolution of Sister Chromatid Cohesion* (reactome, mean cos +0.51 to 33).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.5 | +3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +5.1 | +4.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.9 | +4.0 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +2.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +3.3 |
|  | [[Methotrexate (drug)]] 0.5 µM |  | +2.4 | +1.8 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | +2.4 | +0.5 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.3 | +1.2 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | -7.0 | -6.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.7 | -4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.0 | -0.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | -4.5 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.7 | -3.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.6 | -4.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.6 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.4 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | structural maintenance of chromosomes 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.1 — chr9:104,094,260-104,141,419 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hCAP-E, CAP-E; previously SMC2L1 |
| Gene groups (HGNC) | Structural maintenance of chromosomes proteins; Condensin I subunits; Condensin II subunits |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 7 pathways, smallest: Condensation of Prometaphase Chromosomes; Condensation of Prophase Chromosomes; Mitotic Prophase |
| Matched by | ensembl_id |

**Function**, from UniProt [O95347](https://www.uniprot.org/uniprotkb/O95347) (Structural maintenance of chromosomes protein 2):

> Central component of the condensin complex, a complex required for conversion of interphase chromatin into mitotic-like condense chromosomes. The condensin complex probably introduces positive supercoils into relaxed DNA in the presence of type I topoisomerases and converts nicked DNA into positive knotted forms in the presence of type II topoisomerases.

**Summary**, from NCBI Gene [10592](https://www.ncbi.nlm.nih.gov/gene/10592):

> Predicted to enable chromatin binding activity. Involved in mitotic chromosome condensation and positive regulation of chromosome condensation. Located in condensed chromosome; cytoplasm; and nuclear lumen. Part of condensin complex. Implicated in colon adenocarcinoma. Biomarker of colorectal cancer. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14011](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14011) · Entrez [10592](https://www.ncbi.nlm.nih.gov/gene/10592) · UniProt [O95347](https://www.uniprot.org/uniprotkb/O95347) · Ensembl [ENSG00000136824](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136824)

## Data

Gene col 5910: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5910); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5910, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5910]; `tensor/DDL_lfc|DDL_z.npy` [5910]; `embed/gene_vectors.npy` [5910]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5910 or target_col == 5910). Every well: [[SMC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
