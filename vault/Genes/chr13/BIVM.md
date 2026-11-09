---
symbol: "BIVM"
type: "gene"
col: 5621
ensembl_id: "ENSG00000134897"
name: "basic, immunoglobulin-like variable motif containing"
location: "13q33.1"
module: 175
arm: "+"
pooled_cpm: 29.52
n_lines_expressing: 47
n_dd_up: 8
n_dd_down: 19
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/175"]
generated_by: "tahoemap"
---

# BIVM

*basic, immunoglobulin-like variable motif containing* — 13q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +13.4, q 2e-38, up in 34 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.566× (z -15.5, q 0e+00, down in 36 of 44 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.679× (z -7.4, q 9e-12, down in 30 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCB10]] (+0.70, fdr 7e-06), [[PIGX]] (+0.61, fdr 2e-05), [[TMED8]] (+0.61, fdr 1e-05); moves opposite to [[MKNK1]] (-0.55, fdr 5e-05), [[JUND]] (-0.53, fdr 3e-05), [[LINC02968]] (-0.52, fdr 3e-05).
> It is in [[Module 175]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[CHPT1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5621.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +13.4 | 2e-38 | 34/45 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.9 | 3e-04 | 19/43 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.005 | 17/45 (SW480, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.006 | 15/45 (KATO III, LS 180, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.023 | 10/45 (BT-474, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.023 | 15/44 (PANC-1, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.20×** | +3.6 | 0.023 | 12/45 (COLO 205, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.023 | 8/45 (COLO 205, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.14× | +3.5 | 0.028 | 4/45 (A498, RKO, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.19× | +3.4 | 0.036 | 12/44 (hTERT-HPNE, J82, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.19× | +3.4 | 0.037 | 7/45 (KATO III, BT-474, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.089 | 13/44 (NCI-H1573, PANC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5621.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.566×** | -15.5 | 0e+00 | 36/44 (NCI-H1573, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.484×** | -14.0 | 8e-42 | 36/45 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.561×** | -11.1 | 2e-26 | 35/43 (NCI-H460, SHP-77, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.630×** | -8.9 | 1e-16 | 26/44 (NCI-H460, A-172, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.641×** | -8.5 | 2e-15 | 32/44 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.633×** | -8.4 | 3e-15 | 25/45 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.663×** | -7.9 | 3e-13 | 27/45 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.679×** | -7.4 | 9e-12 | 30/45 (KATO III, SNU-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.692×** | -7.1 | 1e-10 | 32/44 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.713×** | -6.5 | 5e-09 | 28/45 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.534×** | -6.3 | 2e-08 | 25/45 (NCI-H460, A-172, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.554×** | -5.9 | 1e-07 | 21/44 (COLO 205, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.742×** | -5.7 | 5e-07 | 26/45 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.611×** | -4.9 | 3e-05 | 17/44 (MIA PaCa-2, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.788×** | -4.5 | 2e-04 | 21/45 (NCI-H460, SW480, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.859× | -4.1 | 0.002 | 10/45 (SNU-1, MIA PaCa-2, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.869× | -3.8 | 0.005 | 18/45 (A-172, LS 180, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.709×** | -3.4 | 0.015 | 13/43 (HCT15, A498, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.841× | -3.3 | 0.026 | 14/43 (A-172, AN3 CA, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5621. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 33.4 | 1 | 13 (13 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.0668× (z -27.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 58.4 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -27.0) ⚠ cell-cycle shift, explains ~47% of this change |
| [[PANC-1 (line)]] | alt | 18.8 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -15.2) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A-172 (line)]] | wt | 64.7 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -21.1) ⚠ cell-cycle shift, explains ~47% of this change |
| [[HOP62 (line)]] | alt | 20.4 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -11.4) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A498 (line)]] | wt | 36.2 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +9.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.369× (z -10.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 21.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -13.6) ⚠ cell-cycle shift, explains ~47% of this change |
| [[COLO 205 (line)]] | alt | 39.1 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.211× (z -10.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0799× (z -8.9) |
| [[HCT15 (line)]] | alt | 29.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.152× (z -12.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[RKO (line)]] | wt | 42.9 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.135× (z -16.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 44.3 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.165× (z -11.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.345× (z -9.8) |
| [[SW480 (line)]] | alt | 67.9 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +11.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.462× (z -9.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HS-578T (line)]] | alt | 16.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -18.3) ⚠ cell-cycle shift, explains ~47% of this change |
| [[hTERT-HPNE (line)]] | wt | 31.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -15.7) ⚠ cell-cycle shift, explains ~47% of this change |
| [[LOX-IMVI (line)]] | wt | 47.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -16.2) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H23 (line)]] | alt | 23.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -15.0) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A-427 (line)]] | wt | 21.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -9.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[BT-474 (line)]] | alt | 11.2 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.117× (z -9.4) |
| [[C32 (line)]] | wt | 26.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +9.1) | — |
| [[CHP-212 (line)]] | wt | 42.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.1000× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 24.2 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.290× (z -10.7) |
| [[KATO III (line)]] | alt | 26.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +9.0) | — |
| [[LoVo (line)]] | wt | 27.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -13.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H2030 (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -9.8) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SHP-77 (line)]] | alt | 74.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.318× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.243× (z -8.6) ⚠ cell-cycle shift, explains ~49% of this change |
| [[SW 900 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -9.8) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SW48 (line)]] | wt | 31.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -8.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[AN3 CA (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.50 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 58.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.13 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5621), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCB10]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[PIGX]] | +0.61 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[TMED8]] | +0.61 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ANGEL2]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[DTD2]] | +0.58 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[METTL9]] | +0.58 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[TTC13]] | +0.57 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[WHAMMP1]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[STRADB]] | +0.57 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[TDRD3]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[DRAM2]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[FZD3]] | +0.55 | +0.54 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MKNK1]] | -0.55 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[JUND]] | -0.53 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[LINC02968]] | -0.52 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[RHOB]] | -0.52 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[TUFT1]] | -0.52 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[TUBB2A]] | -0.50 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[CTNND1]] | -0.50 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[PILRB]] | -0.49 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[AMDHD2]] | -0.49 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[ARID5A]] | -0.48 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[PSMB1]] | -0.48 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[ADNP2]] | -0.48 | -0.46 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BIVM's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[NT5M]] | B | NT5M activity raises BIVM's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.81× lower at baseline in the lines without NT5M | 0.066 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHPT1]] | C | BIVM activity raises CHPT1's level | lines that do not express BIVM (3) vs lines expressing it (47) | 3.43× lower at baseline in the lines without BIVM | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, RAPGEF4, SYCP2L; maybe low, not absent; co-absent with the target; its own permutation p |
| [[HS6ST1]] | C | BIVM activity raises HS6ST1's level | lines that do not express BIVM (3) vs lines expressing it (47) | 2.46× lower at baseline in the lines without BIVM | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, RAPGEF4, SYCP2L; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 175]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.669). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.2, 16.0); signed map (-30.8, -19.5). **Vector** length 77.6, 15.4% of its response variance represented; |z| ≥ 3 in 1,005 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +13.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +4.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.8 | +3.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +3.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.4 | +1.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.4 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +4.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.2 | +0.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -4.4 | -15.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | +0.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.3 | -5.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -3.2 | -4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -7.4 |
|  | [[Docetaxel (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | +0.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | basic, immunoglobulin-like variable motif containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q33.1 — chr13:102,799,119-102,841,533 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20159 |
| Matched by | ensembl_id |

UniProt [Q86UB2](https://www.uniprot.org/uniprotkb/Q86UB2) carries no function annotation.

**Summary**, from NCBI Gene [54841](https://www.ncbi.nlm.nih.gov/gene/54841):

> Predicted to enable DNA endonuclease activity and single-stranded DNA binding activity. Predicted to be involved in DNA metabolic process. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16034](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16034) · Entrez [54841](https://www.ncbi.nlm.nih.gov/gene/54841) · UniProt [Q86UB2](https://www.uniprot.org/uniprotkb/Q86UB2) · Ensembl [ENSG00000134897](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134897)

## Data

Gene col 5621: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5621); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5621, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5621]; `tensor/DDL_lfc|DDL_z.npy` [5621]; `embed/gene_vectors.npy` [5621]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5621 or target_col == 5621). Every well: [[BIVM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BIVM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
