---
symbol: "HNRNPDL"
type: "gene"
col: 7660
ensembl_id: "ENSG00000152795"
name: "heterogeneous nuclear ribonucleoprotein D like"
location: "4q21.22"
module: 17
arm: "+"
pooled_cpm: 176.48
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# HNRNPDL

*heterogeneous nuclear ribonucleoprotein D like* — 4q21.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.83× (z +11.1, q 8e-26, up in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~53% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.27× (z +5.8, q 7e-07, up in 41 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.646× (z -7.9, q 1e-12, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRPF39]] (+0.64, fdr 2e-05), [[CCDC180]] (+0.57, fdr 3e-05), [[SKIC3]] (+0.57, fdr 3e-05); moves opposite to [[TLCD3A]] (-0.58, fdr 2e-04), [[DCTN5]] (-0.55, fdr 4e-04), [[PTGR3]] (-0.54, fdr 8e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DYNC2H1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 15 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7660.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.83×** | +11.1 | 8e-26 | 43/48 (COLO 205, NCI-H1792, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.05×** | +9.3 | 3e-18 | 44/47 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.71×** | +7.2 | 1e-10 | 38/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.70×** | +7.2 | 1e-10 | 40/48 (NCI-H460, KATO III, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.68×** | +7.0 | 3e-10 | 40/48 (COLO 205, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.59×** | +6.2 | 5e-08 | 39/49 (A549, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.27×** | +5.8 | 7e-07 | 41/49 (NCI-H23, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +5.6 | 1e-06 | 39/48 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +5.0 | 3e-05 | 37/48 (PANC-1, HCT15, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.47×** | +4.8 | 1e-04 | 37/45 (MIA PaCa-2, NCI-H1792, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.87×** | +4.4 | 5e-04 | 34/48 (NCI-H1573, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.40×** | +4.4 | 6e-04 | 36/48 (COLO 205, AsPC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.36×** | +4.2 | 0.001 | 33/48 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.34×** | +3.8 | 0.007 | 25/44 (NCI-H460, SNU-423, …) | all doses, flat | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.007 | 30/49 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.054 | 26/48 (NCI-H460, H4, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.51×** | +2.9 | 0.091 | 26/48 (CFPAC-1, Hs 766T, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7660.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.646×** | -7.9 | 1e-12 | 42/49 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.732×** | -5.6 | 5e-06 | 35/48 (LoVo, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.787×** | -4.2 | 0.004 | 31/48 (LOX-IMVI, A-427, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.918× | -3.9 | 0.013 | 0/50 | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.765×** | -3.6 | 0.037 | 34/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.775×** | -3.4 | 0.061 | 30/48 (HOP62, J82, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.779×** | -3.4 | 0.065 | 31/48 (A-427, NCI-H2347, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.787×** | -3.2 | 0.096 | 32/49 (A-427, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7660. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 130 | 10 (10 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.01× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[LoVo (line)]] | wt | 195 | 4 (4 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +13.5) ⚠ cell-cycle shift, explains ~53% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -11.8) |
| [[COLO 205 (line)]] | alt | 134 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +19.1) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[LS 180 (line)]] | wt | 141 | 5 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.92× (z +12.6) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[LOX-IMVI (line)]] | wt | 182 | 3 (3 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +9.7) ⚠ cell-cycle shift, explains ~42% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 138 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -9.1) |
| [[PANC-1 (line)]] | alt | 135 | 3 (3 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +11.4) ⚠ cell-cycle shift, explains ~42% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -9.4) |
| [[SW480 (line)]] | alt | 223 | 3 (3 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 1.96× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -16.0) |
| [[AsPC-1 (line)]] | alt | 167 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +12.8) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[KATO III (line)]] | alt | 164 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.44× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H1792 (line)]] | alt | 134 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +15.4) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[NCI-H23 (line)]] | alt | 123 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +13.4) ⚠ cell-cycle shift, explains ~53% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -13.0) |
| [[SHP-77 (line)]] | alt | 197 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -8.9) |
| [[A549 (line)]] | wt | 177 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[NCI-H1573 (line)]] | alt | 196 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +12.6) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[A-427 (line)]] | wt | 129 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[A498 (line)]] | wt | 239 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.1) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[C32 (line)]] | wt | 127 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +12.6) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[HCT15 (line)]] | alt | 231 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 183 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.1) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[Hs 766T (line)]] | wt | 145 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.7) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[HT-29 (line)]] | alt | 194 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.4) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 177 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.1) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[RKO (line)]] | wt | 207 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -13.2) |
| [[RPMI-7951 (line)]] | alt | 195 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.4) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 119 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +15.1) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[SNU-1 (line)]] | wt | 131 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.76× (z +8.6) ⚠ toxic | — |
| [[SW1417 (line)]] | alt | 193 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.4) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[A-172 (line)]] | wt | 176 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 180 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 168 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 212 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 198 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 150 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 166 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 330 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 235 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 182 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7660), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPF39]] | +0.64 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[CCDC180]] | +0.57 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[SKIC3]] | +0.57 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[STRA6LP]] | +0.57 | +0.54 / +0.33 | both halves | 1e-04 |  |
| [[NECAP1]] | +0.57 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[ANKRD24]] | +0.53 | +0.29 / +0.45 | both halves | 2e-04 |  |
| [[ZC3H15]] | +0.53 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[ELP1]] | +0.52 | +0.46 / +0.29 | both halves | 2e-04 |  |
| [[NOP53]] | +0.52 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[IFTAP]] | +0.51 | +0.29 / +0.38 | both halves | 2e-04 |  |
| [[MNS1]] | +0.50 | +0.39 / +0.34 | both halves | 1e-04 |  |
| [[METTL17]] | +0.50 | +0.46 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLCD3A]] | -0.58 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[DCTN5]] | -0.55 | -0.24 / -0.49 | both halves | 4e-04 |  |
| [[PTGR3]] | -0.54 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[TMEM11-DT]] | -0.53 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[ANXA2R-OT1]] | -0.53 | -0.27 / -0.38 | both halves | 3e-04 |  |
| [[TOR1A]] | -0.52 | -0.26 / -0.37 | both halves | 3e-04 |  |
| [[TIGD7]] | -0.52 | -0.23 / -0.39 | both halves | 6e-04 |  |
| [[PRR14L]] | -0.52 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[PIGW]] | -0.51 | -0.10 / -0.49 | ⚠ not reproduced | 0.003 |  |
| [[PRDM15]] | -0.51 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[SOCS4]] | -0.51 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[E2F3]] | -0.51 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[ZNF808]] | -0.51 | -0.28 / -0.38 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DYNC2H1]] | B | DYNC2H1 activity weakens HNRNPDL's drug response | lines that do not express DYNC2H1 (8) vs lines expressing it (41) | the lines without DYNC2H1 respond 1.26× as strongly (z diff -1.01); strongest at Ouabain (Octahydrate) 5 µM: 2.41x vs 1.63x (z diff -3.1) | 0.068 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.521). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-4.6, -4.0); signed map (-26.1, -14.4). **Vector** length 91.1, 32.5% of its response variance represented; |z| ≥ 3 in 980 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +1.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +4.8 | +6.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.6 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | +4.5 | +3.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +4.3 | +3.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +1.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +1.1 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.9 | +1.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.7 | -3.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.2 | -7.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.5 | -2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -5.5 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.3 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | +0.1 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.0 | -3.6 |
|  | [[Infigratinib (drug)]] 5 µM |  | -1.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | heterogeneous nuclear ribonucleoprotein D like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.22 — chr4:82,422,565-82,430,462 (-) |
| Ensembl biotype | protein_coding |
| Also known as | JKTBP, laAUF1; previously HNRPDL, LGMD1G |
| Gene groups (HGNC) | RNA binding motif containing; Heterogeneous nuclear ribonucleoproteins |
| Reactome | 5 pathways, smallest: Gene and protein expression by JAK-STAT signaling after Interleukin-12 stimulation; Interleukin-12 signaling; Interleukin-12 family signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O14979](https://www.uniprot.org/uniprotkb/O14979) (Heterogeneous nuclear ribonucleoprotein D-like):

> Acts as a transcriptional regulator. Promotes transcription repression. Promotes transcription activation in differentiated myotubes (By similarity). Binds to double- and single-stranded DNA sequences. Binds to the transcription suppressor CATR sequence of the COX5B promoter (By similarity). Binds with high affinity to RNA molecules that contain AU-rich elements (AREs) found within the 3'-UTR of many proto-oncogenes and cytokine mRNAs. Binds both to nuclear and cytoplasmic poly(A) mRNAs. Binds …

**Summary**, from NCBI Gene [9987](https://www.ncbi.nlm.nih.gov/gene/9987):

> This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in the nucleus, some seem to shuttle between the nucleus and the cytoplasm. The hnRNP proteins have …

**Accessions** — [HGNC:5037](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5037) · Entrez [9987](https://www.ncbi.nlm.nih.gov/gene/9987) · UniProt [O14979](https://www.uniprot.org/uniprotkb/O14979) · Ensembl [ENSG00000152795](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152795)

## Data

Gene col 7660: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7660); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7660, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7660]; `tensor/DDL_lfc|DDL_z.npy` [7660]; `embed/gene_vectors.npy` [7660]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7660 or target_col == 7660). Every well: [[HNRNPDL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNRNPDL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
