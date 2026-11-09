---
symbol: "DNTTIP1"
type: "gene"
col: 2142
ensembl_id: "ENSG00000101457"
name: "deoxynucleotidyltransferase terminal interacting protein 1"
location: "20q13.12"
module: 149
arm: "+"
pooled_cpm: 65.21
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 25
n_dd_up_clean: 7
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/149"]
generated_by: "tahoemap"
---

# DNTTIP1

*deoxynucleotidyltransferase terminal interacting protein 1* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.01× (z +11.6, q 2e-28, up in 41 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.577× (z -12.4, q 1e-32, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELOF1]] (+0.65, fdr 1e-04), [[ZNF557]] (+0.64, fdr 1e-05), [[BCL10]] (+0.63, fdr 1e-05); moves opposite to [[STT3B]] (-0.69, fdr 9e-06), [[PON2]] (-0.68, fdr 8e-06), [[NCKAP1]] (-0.60, fdr 1e-05).
> It is in [[Module 149]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[WFDC3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2142.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.01×** | +11.6 | 2e-28 | 41/49 (NCI-H460, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.19×** | +6.6 | 1e-08 | 30/47 (SNU-423, A-172, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.31×** | +4.4 | 0.002 | 27/48 (SW48, A-172, …) | all doses, flat |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.67×** | +4.3 | 0.002 | 25/48 (SW480, RPMI-7951, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.31×** | +4.3 | 0.002 | 25/47 (A-172, KATO III, …) | all doses, flat |  |
| [[4EGI-1 (drug)]] 5 µM |  | **1.58×** | +3.8 | 0.013 | 22/48 (SW480, MIA PaCa-2, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.50×** | +3.5 | 0.032 | 11/48 (RPMI-7951, A-172, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.17× | +3.5 | 0.032 | 20/47 (A-427, KATO III, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.5 | 0.032 | 20/48 (PANC-1, SW48, …) | all doses, flat |  |
| [[Infigratinib (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.037 | 11/48 (NCI-H2347, A-172, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | 1.15× | +3.3 | 0.055 | 13/49 (SW1417, SNU-1, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | 1.41× | +3.0 | 0.12 | 11/48 (LS 180, MIA PaCa-2, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2142.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.577×** | -12.4 | 1e-32 | 37/48 (AsPC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.499×** | -10.7 | 4e-24 | 37/48 (MIA PaCa-2, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.650×** | -9.7 | 4e-20 | 42/48 (SW1417, SNU-423, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.628×** | -7.4 | 1e-11 | 33/48 (COLO 205, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.698×** | -5.7 | 1e-06 | 26/48 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.692×** | -5.7 | 1e-06 | 31/49 (MIA PaCa-2, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.714×** | -5.2 | 2e-05 | 23/39 (RPMI-7951, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.749×** | -4.6 | 3e-04 | 26/48 (SW1417, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.753×** | -4.5 | 4e-04 | 23/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.757×** | -4.3 | 0.001 | 25/47 (NCI-H460, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.754×** | -4.2 | 0.002 | 25/48 (AsPC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.773×** | -4.1 | 0.002 | 23/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.622×** | -4.0 | 0.003 | 23/48 (MIA PaCa-2, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.842× | -3.8 | 0.007 | 17/48 (AsPC-1, NCI-H460, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.795×** | -3.7 | 0.009 | 24/48 (COLO 205, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.801×** | -3.5 | 0.014 | 22/48 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.803×** | -3.5 | 0.016 | 18/48 (AsPC-1, NCI-H460, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.793×** | -3.3 | 0.028 | 20/48 (NCI-H23, AsPC-1, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.682×** | -3.2 | 0.039 | 16/47 (SW 900, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2142. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 176 | 0 | 11 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -19.3) |
| [[NCI-H460 (line)]] | wt | 59.1 | 1 | 9 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 7.64× (z +11.2) | [[Digitoxin (drug)]] 0.5 µM 0.212× (z -16.3) |
| [[AsPC-1 (line)]] | alt | 278 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -19.5) |
| [[SW1417 (line)]] | alt | 142 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -17.2) |
| [[RPMI-7951 (line)]] | alt | 98.3 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.19× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.107× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -13.0) |
| [[A-172 (line)]] | wt | 51.0 | 4 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.84× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -9.8) |
| [[COLO 205 (line)]] | alt | 126 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0911× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 66.5 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.303× (z -10.9) |
| [[SNU-423 (line)]] | alt | 114 | 1 | 3 | [[PH-797804 (drug)]] 5 µM 5.12× (z +8.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -12.9) |
| [[A498 (line)]] | wt | 72.1 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 4.78× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -18.7) |
| [[CFPAC-1 (line)]] | alt | 88.4 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -11.0) |
| [[Hs 766T (line)]] | wt | 116 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.04× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.212× (z -12.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 99.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 76.8 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -9.6) |
| [[A-427 (line)]] | wt | 27.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +12.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[H4 (line)]] | wt | 46.3 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -10.1) |
| [[HS-578T (line)]] | alt | 47.6 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.421× (z -11.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -8.5) |
| [[LoVo (line)]] | wt | 22.3 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 11.9× (z +10.2) | — |
| [[NCI-H1792 (line)]] | alt | 72.3 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.24× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 77.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -15.4) |
| [[NCI-H2347 (line)]] | alt | 57.1 | 0 | 2 | — | [[Tucidinostat (drug)]] 5 µM 0.479× (z -10.9) |
| [[Panc 03.27 (line)]] | alt | 69.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -8.8) |
| [[C32 (line)]] | wt | 42.3 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 33.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -8.7) |
| [[HT-29 (line)]] | alt | 36.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -9.6) |
| [[KATO III (line)]] | alt | 37.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +11.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LOX-IMVI (line)]] | wt | 40.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -10.1) |
| [[RKO (line)]] | wt | 41.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -9.5) |
| [[SW 900 (line)]] | alt | 55.0 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -10.1) |
| [[SW480 (line)]] | alt | 95.0 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -9.2) |
| [[A549 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2142), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELOF1]] | +0.65 | +0.61 / +0.34 | both halves | 1e-04 |  |
| [[ZNF557]] | +0.64 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[BCL10]] | +0.63 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[LENG1]] | +0.63 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[CINP]] | +0.61 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[MRPL10]] | +0.60 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[FAM32A]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[R3HCC1]] | +0.59 | +0.54 / +0.39 | both halves | 5e-05 |  |
| [[ZNF23]] | +0.59 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[ZKSCAN5]] | +0.59 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[ZNF3]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[ADPRS]] | +0.59 | +0.53 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STT3B]] | -0.69 | -0.57 / -0.67 | both halves | 9e-06 |  |
| [[PON2]] | -0.68 | -0.57 / -0.60 | both halves | 8e-06 |  |
| [[NCKAP1]] | -0.60 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[LAPTM4B]] | -0.59 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[CRTAP]] | -0.58 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[GOLM1]] | -0.56 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[NFIA]] | -0.55 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[CMPK1]] | -0.55 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[FUCA2]] | -0.54 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[TMEM123]] | -0.54 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[TMEM64]] | -0.53 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[FAM53B]] ⚠ | -0.52 | -0.53 / -0.42 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[UBQLN4]] | -0.52 | -0.47 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WFDC3]] | B | WFDC3 activity raises DNTTIP1's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 2.09× lower at baseline in the lines without WFDC3 | 0.004 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |
| [[WFDC10B]] | B | WFDC10B activity raises DNTTIP1's level | lines that do not express WFDC10B (20) vs lines expressing it (30) | 1.82× lower at baseline in the lines without WFDC10B | 0.008 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent |
| [[WFDC10B]] | B | WFDC10B activity strengthens DNTTIP1's drug response | lines that do not express WFDC10B (20) vs lines expressing it (29) | the lines without WFDC10B respond 0.51× as strongly (z diff +2.26); strongest at Panobinostat 5 µM: 0.98x vs 0.54x (z diff +4.1) | 0.034 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[HRH1]] | B | HRH1 activity raises DNTTIP1's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 2.06× lower at baseline in the lines without HRH1 | 0.050 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[WFDC3]] | C | WFDC3's natural level strengthens DNTTIP1's drug response | WFDC3's natural level across 34 lines (lineage-adjusted; a glimpse) | r +0.76, reverse +0.60; direction not clear | 0.071 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 149]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.611). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.3, -7.9); signed map (-4.8, -12.8). **Vector** length 125, 37.0% of its response variance represented; |z| ≥ 3 in 1,200 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +10.5 | +11.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +6.8 | +4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.9 | +6.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | +2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +5.5 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.3 | +2.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.4 | -9.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.2 | -7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.1 | -5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -10.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.7 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.5 | -4.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.4 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.2 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | deoxynucleotidyltransferase terminal interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:45,791,954-45,811,427 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ447F3.4, Tdif1; previously C20orf167 |
| Gene groups (HGNC) | MiDAC complex subunits |
| Reactome | 9 pathways, smallest: Negative Regulation of CDH1 Gene Transcription; Regulation of CDH1 Gene Transcription; Regulation of CDH1 Expression and Function |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H147](https://www.uniprot.org/uniprotkb/Q9H147) (Deoxynucleotidyltransferase terminal-interacting protein 1):

> Increases DNTT terminal deoxynucleotidyltransferase activity (in vitro). Also acts as a transcriptional regulator, binding to the consensus sequence 5'-GNTGCATG-3' following an AT-tract. Associates with RAB20 promoter and positively regulates its transcription. Binds DNA and nucleosomes; may recruit HDAC1 complexes to nucleosomes or naked DNA.

**Summary**, from NCBI Gene [116092](https://www.ncbi.nlm.nih.gov/gene/116092):

> DNTTIP1 binds DNA and enhances the activity of terminal deoxynucleotidyltransferase (TDT, or DNTT; MIM 187410), a DNA polymerase that catalyzes the polymerization of DNA in the absence of a DNA template (Yamashita et al., 2001 [PubMed 11473582]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:16160](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16160) · Entrez [116092](https://www.ncbi.nlm.nih.gov/gene/116092) · UniProt [Q9H147](https://www.uniprot.org/uniprotkb/Q9H147) · Ensembl [ENSG00000101457](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101457)

## Data

Gene col 2142: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2142); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2142, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2142]; `tensor/DDL_lfc|DDL_z.npy` [2142]; `embed/gene_vectors.npy` [2142]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2142 or target_col == 2142). Every well: [[DNTTIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNTTIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
