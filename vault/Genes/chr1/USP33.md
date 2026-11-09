---
symbol: "USP33"
type: "gene"
col: 1181
ensembl_id: "ENSG00000077254"
name: "ubiquitin specific peptidase 33"
location: "1p31.1"
module: 45
arm: "+"
pooled_cpm: 121.97
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# USP33

*ubiquitin specific peptidase 33* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.68× (z +12.5, q 4e-33, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.633× (z -10.7, q 6e-24, down in 41 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.642× (z -5.5, q 6e-06, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RCOR3]] (+0.73, fdr 7e-06), [[TMEM59]] (+0.73, fdr 7e-06), [[MBIP]] (+0.66, fdr 7e-06); moves opposite to [[PUS1]] (-0.65, fdr 7e-06), [[METTL1]] (-0.61, fdr 7e-06), [[PNO1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NABP1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1181.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.68×** | +12.5 | 4e-33 | 39/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.55×** | +10.4 | 4e-23 | 39/48 (SK-MEL-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +10.2 | 6e-22 | 36/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +9.1 | 1e-17 | 33/48 (BT-474, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.43×** | +8.6 | 1e-15 | 39/48 (J82, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.88×** | +7.9 | 2e-13 | 37/49 (Panc 03.27, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +7.1 | 8e-11 | 32/47 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.30×** | +6.4 | 1e-08 | 30/48 (J82, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +6.2 | 4e-08 | 29/48 (A-427, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +6.1 | 6e-08 | 28/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +5.5 | 2e-06 | 27/50 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.51×** | +5.1 | 1e-05 | 30/48 (PANC-1, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.16× | +5.1 | 2e-05 | 17/49 (MIA PaCa-2, SW48, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +4.9 | 3e-05 | 24/48 (C32, NCI-H2030, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.23×** | +4.9 | 4e-05 | 24/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +4.7 | 8e-05 | 13/48 (AsPC-1, J82, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +4.7 | 1e-04 | 24/48 (HEC-1-A, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.44×** | +4.6 | 1e-04 | 30/49 (NCI-H460, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +4.0 | 0.002 | 12/48 (J82, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1181.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.633×** | -10.7 | 6e-24 | 41/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -6.2 | 2e-07 | 2/50 (SW 1088, SW 1271) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.642×** | -5.5 | 6e-06 | 33/48 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.648×** | -5.4 | 8e-06 | 32/48 (MIA PaCa-2, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.671×** | -5.0 | 6e-05 | 29/48 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.719×** | -4.1 | 0.004 | 23/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.848× | -4.0 | 0.006 | 18/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.852× | -3.6 | 0.027 | 18/45 (SNU-423, A549, …) | inconsistent across doses | composition shift |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.759×** | -3.5 | 0.034 | 17/45 (RPMI-7951, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.867× | -3.3 | 0.054 | 14/47 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.872× | -3.3 | 0.054 | 14/48 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.875× | -3.2 | 0.063 | 6/48 (J82, SNU-423, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.875× | -3.2 | 0.063 | 18/48 (KATO III, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.882× | -3.0 | 0.10 | 12/48 (HT-29, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1181. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 107 | 10 (5 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.72× (z +16.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +16.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.516× (z -11.0) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 119 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +22.0) | — |
| [[BT-474 (line)]] | alt | 86.4 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +16.9) | — |
| [[J82 (line)]] | alt | 106 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.34× (z +10.9) | — |
| [[LoVo (line)]] | wt | 124 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +14.2) | — |
| [[SW48 (line)]] | wt | 112 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 123 | 1 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +8.8) ⚠ cell-cycle shift, explains ~10% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.335× (z -13.2) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.265× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 109 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 116 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.83× (z +13.1) | — |
| [[HEC-1-A (line)]] | alt | 162 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +13.3) | — |
| [[KATO III (line)]] | alt | 122 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +13.3) | — |
| [[LOX-IMVI (line)]] | wt | 118 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.06× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 149 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +14.9) | — |
| [[NCI-H2030 (line)]] | alt | 93.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.26× (z +10.1) | — |
| [[SW480 (line)]] | alt | 153 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +10.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.554× (z -9.2) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 108 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +10.0) | — |
| [[AN3 CA (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.298× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.444× (z -8.9) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 158 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 77.4 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0831× (z -12.1) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 88.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 110 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.04× (z +9.3) | — |
| [[NCI-H2347 (line)]] | alt | 125 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.83× (z +9.2) | — |
| [[RKO (line)]] | wt | 112 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 138 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0579× (z -16.7) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 131 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 86.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 146 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 121 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 96.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 83.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 87.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 182 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 168 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 128 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 57.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1181), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCOR3]] | +0.73 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[TMEM59]] | +0.73 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[MBIP]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[FBXO3]] | +0.66 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[CAT]] | +0.64 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[ARL6IP5]] | +0.64 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[AUH]] | +0.64 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[ELF2]] | +0.64 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[MED30]] | +0.61 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[TXNDC16]] | +0.61 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[COPS4]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[PPP2R5A]] | +0.61 | +0.61 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUS1]] | -0.65 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[METTL1]] | -0.61 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[PNO1]] | -0.61 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[GTPBP4]] | -0.60 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[PPRC1]] | -0.60 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[ZNF562]] | -0.59 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[ZNF121]] | -0.57 | -0.64 / -0.44 | both halves | 3e-05 |  |
| [[CHRNA10]] | -0.57 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[REXO1]] | -0.57 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[NOP2]] | -0.57 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[EIF3J]] | -0.57 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[GEMIN4]] | -0.57 | -0.56 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NABP1]] | C | NABP1 activity lowers USP33's level | lines that do not express NABP1 (4) vs lines expressing it (46) | 1.32× higher at baseline in the lines without NABP1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, LACC1, NMI; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.704). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-1.2, -42.5); signed map (-24.2, -5.6). **Vector** length 111, 33.7% of its response variance represented; |z| ≥ 3 in 1,138 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +6.0 | +4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.8 | +4.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +4.6 | +3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +6.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.8 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +2.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.7 | -10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.3 | -4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.0 | -5.5 |
|  | [[EX229 (drug)]] 5 µM |  | -5.9 | -5.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.6 | -5.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.4 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 33 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:77,695,987-77,759,852 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1097, VDU1 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Reactome | 6 pathways, smallest: Regulation of expression of SLITs and ROBOs; Ub-specific processing proteases; Signaling by ROBO receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TEY7](https://www.uniprot.org/uniprotkb/Q8TEY7) (Ubiquitin carboxyl-terminal hydrolase 33):

> Deubiquitinating enzyme involved in various processes such as centrosome duplication, cellular migration and beta-2 adrenergic receptor/ADRB2 recycling. Involved in regulation of centrosome duplication by mediating deubiquitination of CCP110 in S and G2/M phase, leading to stabilize CCP110 during the period which centrioles duplicate and elongate. Involved in cell migration via its interaction with intracellular domain of ROBO1, leading to regulate the Slit signaling. Plays a role in …

**Summary**, from NCBI Gene [23032](https://www.ncbi.nlm.nih.gov/gene/23032):

> This gene encodes a deubiquinating enzyme important in a variety of processes, including Slit-dependent cell migration and beta-2 adrenergic receptor signaling. The protein is negatively regulated through ubiquitination by von Hippel-Lindau tumor protein (VHL). Alternative splicing results in multiple transcript variants and protein isoforms. [provided by RefSeq, Jun 2012]

**Accessions** — [HGNC:20059](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20059) · Entrez [23032](https://www.ncbi.nlm.nih.gov/gene/23032) · UniProt [Q8TEY7](https://www.uniprot.org/uniprotkb/Q8TEY7) · Ensembl [ENSG00000077254](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077254)

## Data

Gene col 1181: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1181); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1181, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1181]; `tensor/DDL_lfc|DDL_z.npy` [1181]; `embed/gene_vectors.npy` [1181]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1181 or target_col == 1181). Every well: [[USP33 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP33.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
