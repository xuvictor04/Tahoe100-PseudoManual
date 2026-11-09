---
symbol: "ARF6"
type: "gene"
col: 9141
ensembl_id: "ENSG00000165527"
name: "ARF GTPase 6"
location: "14q21.3"
module: 78
arm: "+"
pooled_cpm: 79.97
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 18
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# ARF6

*ARF GTPase 6* — 14q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.69× (z +9.1, q 8e-17, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.388× (z -23.0, q 0e+00, down in 43 of 49 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C15orf39]] (+0.61, fdr 2e-05), [[ARHGDIA]] (+0.58, fdr 4e-05), [[MAP1S]] (+0.57, fdr 2e-05); moves opposite to [[CSDE1]] (-0.57, fdr 4e-05), [[REXO2]] (-0.55, fdr 3e-05), [[BORCS7]] (-0.53, fdr 3e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9141.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.69×** | +9.1 | 8e-17 | 40/48 (HOP62, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.60×** | +8.1 | 1e-13 | 44/48 (hTERT-HPNE, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.52×** | +6.7 | 3e-09 | 37/47 (A549, SW480, …) | all doses, flat | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.34×** | +5.1 | 5e-05 | 32/48 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.28×** | +3.7 | 0.022 | 23/48 (SNU-423, NCI-H1792, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.7 | 0.024 | 23/44 (SW480, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.028 | 24/49 (NCI-H1573, A549, …) | top dose only | plate-row cell shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.21× | +3.1 | 0.12 | 19/48 (C32, NCI-H2030, …) | all doses, flat | composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.28× | +3.1 | 0.14 | 11/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9141.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.388×** | -23.0 | 0e+00 | 43/49 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.582×** | -8.9 | 1e-16 | 35/47 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.607×** | -8.3 | 3e-14 | 35/48 (SK-MEL-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.629×** | -7.6 | 3e-12 | 32/42 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.637×** | -7.4 | 1e-11 | 35/50 (SK-MEL-2, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.663×** | -7.1 | 2e-10 | 36/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.672×** | -6.8 | 7e-10 | 32/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.773×** | -6.2 | 3e-08 | 27/48 (MIA PaCa-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.689×** | -6.0 | 1e-07 | 30/48 (HOP62, PANC-1, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.521×** | -5.8 | 3e-07 | 32/45 (HCT15, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.716×** | -5.7 | 5e-07 | 33/48 (hTERT-HPNE, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.733×** | -5.3 | 5e-06 | 28/49 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.754×** | -4.8 | 6e-05 | 28/48 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.831×** | -4.5 | 3e-04 | 23/48 (A-172, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.759×** | -4.1 | 0.001 | 24/48 (A549, SW1417, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.755×** | -3.4 | 0.018 | 17/49 (PANC-1, HCT15, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.837× | -3.0 | 0.071 | 19/48 (LoVo, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.880× | -3.0 | 0.072 | 14/48 (LoVo, MIA PaCa-2, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.836× | -2.9 | 0.087 | 18/47 (A-172, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.842× | -2.9 | 0.087 | 16/48 (SK-MEL-2, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9141. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 121 | 0 | 10 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -18.2) |
| [[HOP62 (line)]] | alt | 120 | 1 | 7 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.58× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -22.9) |
| [[PANC-1 (line)]] | alt | 78.0 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -18.9) |
| [[SK-MEL-2 (line)]] | alt | 114 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -18.9) |
| [[MIA PaCa-2 (line)]] | alt | 192 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -26.6) |
| [[hTERT-HPNE (line)]] | wt | 128 | 1 | 3 | [[Homoharringtonine (drug)]] 0.05 µM 3.07× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -17.1) |
| [[NCI-H1573 (line)]] | alt | 79.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0752× (z -26.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -8.9) |
| [[SW480 (line)]] | alt | 76.5 | 1 | 3 | [[Harringtonine (drug)]] 0.5 µM 1.95× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -19.0) |
| [[A498 (line)]] | wt | 75.2 | 1 | 2 | [[Homoharringtonine (drug)]] 0.05 µM 2.27× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -19.7) |
| [[SNU-423 (line)]] | alt | 46.7 | 1 | 2 | [[Harringtonine (drug)]] 0.5 µM 2.54× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -14.2) |
| [[AsPC-1 (line)]] | alt | 55.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.364× (z -9.7) |
| [[C32 (line)]] | wt | 78.6 | 1 | 1 | [[Harringtonine (drug)]] 0.5 µM 2.65× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -11.8) |
| [[COLO 205 (line)]] | alt | 66.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -13.4) |
| [[HCT15 (line)]] | alt | 98.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -12.5) |
| [[Hs 766T (line)]] | wt | 78.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -13.7) |
| [[LOX-IMVI (line)]] | wt | 49.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 78.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 136 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -13.1) |
| [[NCI-H460 (line)]] | wt | 59.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -10.1) |
| [[NCI-H596 (line)]] | alt | 72.5 | 0 | 2 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.176× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 83.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 81.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -14.2) |
| [[SW1417 (line)]] | alt | 87.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -15.5) |
| [[SW48 (line)]] | wt | 93.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -11.7) |
| [[A549 (line)]] | wt | 88.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -14.4) |
| [[CFPAC-1 (line)]] | alt | 104 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -15.1) |
| [[CHP-212 (line)]] | wt | 66.2 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM 0.194× (z -8.8) |
| [[H4 (line)]] | wt | 68.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 81.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -12.1) |
| [[HS-578T (line)]] | alt | 61.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -13.2) |
| [[HT-29 (line)]] | alt | 43.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -11.6) |
| [[J82 (line)]] | alt | 92.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -15.2) |
| [[KATO III (line)]] | alt | 54.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -10.4) |
| [[LoVo (line)]] | wt | 91.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -18.1) |
| [[LS 180 (line)]] | wt | 79.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 63.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -11.8) |
| [[RKO (line)]] | wt | 44.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +9.3) | — |
| [[SNU-1 (line)]] | wt | 45.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.228× (z -9.1) ⚠ toxic |
| [[SW 900 (line)]] | alt | 71.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -11.3) |
| [[A-427 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9141), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C15orf39]] | +0.61 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[ARHGDIA]] | +0.58 | +0.68 / +0.41 | both halves | 4e-05 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 426 |
| [[MAP1S]] | +0.57 | +0.46 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[GALE]] | +0.56 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[CLIC1]] | +0.55 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[ARL4C]] | +0.55 | +0.49 / +0.50 | both halves | 1e-05 | same gene group |
| [[DCLRE1B]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[KLHL9]] | +0.55 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[UBL4A]] | +0.54 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[ZKSCAN2]] | +0.53 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[ZNF184]] | +0.53 | +0.41 / +0.38 | both halves | 6e-05 |  |
| [[EEFSEC]] | +0.52 | +0.46 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSDE1]] | -0.57 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[REXO2]] | -0.55 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[BORCS7]] | -0.53 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[CYBRD1]] | -0.52 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[C8orf44-SGK3]] | -0.52 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[GPBP1L1]] | -0.51 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[ALDH2]] | -0.51 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[PAXBP1]] | -0.49 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[UFC1]] | -0.48 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[DNASE2]] | -0.48 | -0.44 / -0.40 | both halves | 4e-05 |  |
| [[ZBTB47-AS1]] | -0.48 | -0.37 / -0.56 | both halves | 7e-05 |  |
| [[UBXN8]] | -0.48 | -0.45 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ARF6's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CDC42EP3]] | B | CDC42EP3 activity raises ARF6's level | lines that do not express CDC42EP3 (8) vs lines expressing it (42) | 1.71× lower at baseline in the lines without CDC42EP3 | 0.048 | ⚠ within organs, on part of the lines; also absent: CCDC110, C3orf52, KLF12 |
| [[SLCO4A1]] | B | SLCO4A1 activity raises ARF6's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 1.32× lower at baseline in the lines without SLCO4A1 | 0.089 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |
| [[CTSD]] | C | CTSD activity raises ARF6's level | lines that do not express CTSD (4) vs lines expressing it (46) | 1.60× lower at baseline in the lines without CTSD | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFITM10, SQOR, ST6GALNAC2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.408). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-48.1, 16.2); signed map (-6.6, 30.7). **Vector** length 115, 34.0% of its response variance represented; |z| ≥ 3 in 1,178 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +10.3 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +9.6 | +8.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +6.2 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +5.9 | +3.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.2 | -7.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.6 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +1.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -8.3 | -5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.1 | -7.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.0 | -23.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.6 | -3.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | -6.1 | -6.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.6 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -2.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.5 | -2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -2.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | ARF GTPase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.3 — chr14:49,893,079-49,897,054 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | ARF GTPase family |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 8 pathways, smallest: MET receptor recycling; TBC/RABGAPs; Signaling by MET |
| Matched by | ensembl_id |

**Function**, from UniProt [P62330](https://www.uniprot.org/uniprotkb/P62330) (ADP-ribosylation factor 6):

> GTP-binding protein involved in protein trafficking that regulates endocytic recycling and cytoskeleton remodeling. GTP-bound form plays an important role in the transport of multiple palmitoylated proteins form the Golgi to the plasma membrane. Required for normal completion of mitotic cytokinesis (By similarity). Plays a role in the reorganization of the actin cytoskeleton and the formation of stress fibers (By similarity). Involved in the regulation of dendritic spine development, …

**Summary**, from NCBI Gene [382](https://www.ncbi.nlm.nih.gov/gene/382):

> This gene encodes a member of the human ARF gene family, which is part of the RAS superfamily. The ARF genes encode small guanine nucleotide-binding proteins that stimulate the ADP-ribosyltransferase activity of cholera toxin and play a role in vesicular trafficking and as activators of phospholipase D. The product of this gene is localized to the plasma membrane, and regulates vesicular trafficking, remodelling of membrane lipids, and signaling pathways that lead to actin remodeling. A …

**Accessions** — [HGNC:659](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:659) · Entrez [382](https://www.ncbi.nlm.nih.gov/gene/382) · UniProt [P62330](https://www.uniprot.org/uniprotkb/P62330) · Ensembl [ENSG00000165527](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165527)

## Data

Gene col 9141: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9141); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9141, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9141]; `tensor/DDL_lfc|DDL_z.npy` [9141]; `embed/gene_vectors.npy` [9141]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9141 or target_col == 9141). Every well: [[ARF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
