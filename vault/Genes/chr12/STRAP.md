---
symbol: "STRAP"
type: "gene"
col: 350
ensembl_id: "ENSG00000023734"
name: "serine/threonine kinase receptor associated protein"
location: "12p12.3"
module: 42
arm: "+"
pooled_cpm: 127.94
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 4
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# STRAP

*serine/threonine kinase receptor associated protein* — 12p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (19 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.25× (z +12.0, q 4e-30, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Bimiralisib (drug)]] 5 µM: 0.627× (z -3.9, q 0.037, down in 32 of 50 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TM9SF2]] (+0.73, fdr 7e-06), [[EIF3H]] (+0.71, fdr 7e-06), [[DCAF13]] (+0.70, fdr 7e-06); moves opposite to [[TRIM47]] (-0.70, fdr 7e-06), [[UNK]] (-0.69, fdr 7e-06), [[DLX2]] (-0.68, fdr 7e-06).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[STAT5A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 19 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 350.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.25×** | +12.0 | 4e-30 | 47/49 (NCI-H1573, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.11×** | +11.8 | 1e-29 | 45/48 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.02×** | +11.1 | 2e-26 | 46/48 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.97×** | +10.7 | 1e-24 | 45/48 (COLO 205, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.96×** | +10.6 | 3e-24 | 47/48 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.90×** | +10.2 | 2e-22 | 40/49 (NCI-H1792, SW480, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.88×** | +9.6 | 9e-20 | 44/47 (LoVo, COLO 205, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.82×** | +9.5 | 2e-19 | 45/48 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.11×** | +9.4 | 4e-19 | 42/48 (LS 180, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.79×** | +9.2 | 2e-18 | 46/48 (SW480, COLO 205, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +9.2 | 3e-18 | 43/48 (RKO, SNU-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.85×** | +9.0 | 1e-17 | 41/45 (SNU-423, NCI-H1792, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.76×** | +8.9 | 2e-17 | 45/48 (A-427, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.77×** | +8.7 | 2e-16 | 35/44 (LoVo, NCI-H1573, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.69×** | +7.8 | 2e-13 | 44/48 (A-427, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.52×** | +4.7 | 7e-05 | 37/49 (MIA PaCa-2, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.007 | 24/48 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.1 | 0.035 | 11/49 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.043 | 20/49 (J82, A498, …) | inconsistent across doses | position effect removed |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.14× | +2.8 | 0.088 | 5/49 (SHP-77, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 350.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bimiralisib (drug)]] 5 µM |  | **0.627×** | -3.9 | 0.037 | 32/50 (NCI-H596, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.778×** | -3.8 | 0.037 | 31/47 (NCI-H1573, H4, …) | rises with dose |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.795×** | -3.6 | 0.051 | 32/49 (NCI-H1573, HT-29, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.803×** | -3.5 | 0.068 | 24/48 (RKO, KATO III, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.747× | -3.3 | 0.11 | 23/47 (SW 1088, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.793× | -3.2 | 0.11 | 23/50 (LoVo, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 0.868× | -3.2 | 0.11 | 14/48 (NCI-H1573, SW 900, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.819× | -3.2 | 0.11 | 21/49 (RPMI-7951, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[AZD-8055 (drug)]] 5 µM |  | 0.687× | -3.1 | 0.11 | 23/49 (RPMI-7951, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.823× | -3.1 | 0.11 | 22/48 (AsPC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~75% of this change | 0.824× | -3.1 | 0.11 | 22/49 (H4, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 350. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 140 | 13 (11 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.08× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.19× (z +9.1) | — |
| [[LoVo (line)]] | wt | 230 | 9 (7 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.49× (z +16.5) ⚠ toxic; cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.67× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.626× (z -9.2) ⚠ cell-cycle shift, explains ~84% of this change |
| [[MIA PaCa-2 (line)]] | alt | 154 | 10 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.59× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 125 | 10 (9 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.47× (z +15.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.40× (z +12.9) | — |
| [[NCI-H1792 (line)]] | alt | 130 | 10 (10 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | — |
| [[KATO III (line)]] | alt | 99.2 | 7 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.98× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.89× (z +10.5) | — |
| [[NCI-H460 (line)]] | wt | 93.4 | 7 (7 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.67× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HOP62 (line)]] | alt | 114 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.57× (z +10.1) | — |
| [[SNU-423 (line)]] | alt | 59.2 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | — |
| [[A-427 (line)]] | wt | 204 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.55× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -15.4) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 136 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.91× (z +16.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.22× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 91.3 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +11.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.34× (z +10.6) | — |
| [[A-172 (line)]] | wt | 51.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.56× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | — |
| [[COLO 205 (line)]] | alt | 43.6 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.04× (z +11.7) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[HT-29 (line)]] | alt | 121 | 4 | 0 | [[Auranofin (drug)]] 5 µM 2.27× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 251 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.22× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.09× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 159 | 4 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.30× (z +10.6) | — |
| [[RKO (line)]] | wt | 180 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 5.32× (z +10.3) | — |
| [[SW48 (line)]] | wt | 175 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.67× (z +12.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 3.29× (z +10.4) | — |
| [[AsPC-1 (line)]] | alt | 113 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +9.2) ⚠ cell-cycle shift, explains ~84% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.34× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 129 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.22× (z +9.6) | — |
| [[A498 (line)]] | wt | 173 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.90× (z +9.0) | — |
| [[A549 (line)]] | wt | 127 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | — |
| [[BT-474 (line)]] | alt | 99.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.62× (z +9.7) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[H4 (line)]] | wt | 149 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0986× (z -10.8) ⚠ toxic |
| [[HCT15 (line)]] | alt | 113 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | — |
| [[LOX-IMVI (line)]] | wt | 153 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +9.2) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H2030 (line)]] | alt | 179 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +9.4) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 118 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.46× (z +8.8) ⚠ toxic; cell-cycle shift, explains ~31% of this change | — |
| [[SW 1088 (line)]] | alt | 102 | 0 | 1 | — | [[Fumaric acid (drug)]] 0.05 µM 0.0932× (z -8.5) |
| [[SW 900 (line)]] | alt | 207 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +8.9) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[AN3 CA (line)]] | alt | 122 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 107 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 89.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 142 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 104 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 90.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 91.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 115 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 111 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 79.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 143 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 350), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TM9SF2]] | +0.73 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[EIF3H]] | +0.71 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[DCAF13]] | +0.70 | +0.64 / +0.67 | both halves | 7e-06 | same gene group |
| [[BTAF1]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[NAPG]] | +0.66 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[GDAP2]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[OPA1]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[MSTO2P]] | +0.65 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[EFCAB14]] | +0.65 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[GRB2]] | +0.64 | +0.71 / +0.46 | both halves | 2e-05 | pathway: Cell-Cell communication |
| [[SAR1A]] | +0.64 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[TIMM10B]] | +0.64 | +0.63 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM47]] | -0.70 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[UNK]] | -0.69 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[DLX2]] | -0.68 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[MAPK1IP1L]] | -0.67 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[MAD2L1BP]] | -0.66 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[ZNF764]] | -0.65 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[PNRC2]] | -0.65 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[PATL2]] | -0.65 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[PLD6]] | -0.64 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[ZCCHC3]] | -0.64 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[SPHK1]] | -0.64 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[EIF4EBP3]] | -0.64 | -0.58 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STAT5A]] | B | STAT5A activity lowers STRAP's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 1.35× higher at baseline in the lines without STAT5A | 0.038 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[SPHK1]] | B | SPHK1 activity raises STRAP's level | lines that do not express SPHK1 (12) vs lines expressing it (38) | 1.20× lower at baseline in the lines without SPHK1 | 0.057 | ⚠ within organs, on part of the lines; also absent: TMEM158, CAV1, NR3C1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.686). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.4, -28.3); signed map (-50.0, -4.1). **Vector** length 90.3, 34.4% of its response variance represented; |z| ≥ 3 in 1,349 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.51 to 11); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.53 to 9); *IRE1alpha activates chaperones* (reactome, mean cos +0.53 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +4.3 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | +4.2 | +10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | +4.1 | +8.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +3.7 | +10.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.5 | +10.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +9.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +4.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +2.4 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | +1.7 | +2.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -12.8 | -1.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -10.4 | +0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -9.0 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -8.0 | +4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.9 | +11.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -0.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | +0.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.6 | -0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | +0.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.5 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | serine/threonine kinase receptor associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.3 — chr12:15,882,387-15,903,478 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UNRIP, pt-wd, MAWD |
| Gene groups (HGNC) | WD repeat domain containing; SMN complex |
| Reactome | 13 pathways, smallest: Positive Regulation of CDH1 Gene Transcription; Downregulation of TGF-beta receptor signaling; TGF-beta receptor signaling activates SMADs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3F4](https://www.uniprot.org/uniprotkb/Q9Y3F4) (Serine-threonine kinase receptor-associated protein):

> The SMN complex catalyzes the assembly of small nuclear ribonucleoproteins (snRNPs), the building blocks of the spliceosome, and thereby plays an important role in the splicing of cellular pre-mRNAs. Most spliceosomal snRNPs contain a common set of Sm proteins SNRPB, SNRPD1, SNRPD2, SNRPD3, SNRPE, SNRPF and SNRPG that assemble in a heptameric protein ring on the Sm site of the small nuclear RNA to form the core snRNP (Sm core). In the cytosol, the Sm proteins SNRPD1, SNRPD2, SNRPE, SNRPF and …

**Summary**, from NCBI Gene [11171](https://www.ncbi.nlm.nih.gov/gene/11171):

> Enables RNA binding activity. Involved in maintenance of gastrointestinal epithelium and spliceosomal snRNP assembly. Acts upstream of with a positive effect on negative regulation of transforming growth factor beta receptor signaling pathway. Located in cytosol. Part of SMN complex. Implicated in adenocarcinoma; colorectal carcinoma; large cell carcinoma; lung carcinoma; and squamous cell neoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30796](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30796) · Entrez [11171](https://www.ncbi.nlm.nih.gov/gene/11171) · UniProt [Q9Y3F4](https://www.uniprot.org/uniprotkb/Q9Y3F4) · Ensembl [ENSG00000023734](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000023734)

## Data

Gene col 350: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 350); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 350, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 350]; `tensor/DDL_lfc|DDL_z.npy` [350]; `embed/gene_vectors.npy` [350]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 350 or target_col == 350). Every well: [[STRAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STRAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
