---
symbol: "SLC39A9"
type: "gene"
col: 390
ensembl_id: "ENSG00000029364"
name: "solute carrier family 39 member 9"
location: "14q24.1"
module: 56
arm: "+"
pooled_cpm: 98.12
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 5
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# SLC39A9

*solute carrier family 39 member 9* — 14q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.83× (z +12.5, q 6e-33, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.678× (z -8.6, q 4e-15, down in 31 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.786× (z -5.4, q 1e-05, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (KATO III 0.159×, RPMI-7951 0.244×, SNU-1 0.149×, SW1417 0.257×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SHP-77 0.144×, RKO 0.121×, KATO III 0.263×, NCI-H23 0.295×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.117×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPA]] (+0.68, fdr 7e-06), [[MON2]] (+0.66, fdr 7e-06), [[AP1G1]] (+0.66, fdr 7e-06); moves opposite to [[ZNF354B]] (-0.59, fdr 1e-05), [[ZNF354A]] (-0.58, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 390.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.83×** | +12.5 | 6e-33 | 45/49 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.63×** | +11.2 | 2e-26 | 42/48 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.16×** | +9.2 | 4e-18 | 37/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.42×** | +8.1 | 1e-13 | 35/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.40×** | +7.6 | 3e-12 | 36/48 (LOX-IMVI, C-33 A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **1.31×** | +6.2 | 6e-08 | 33/48 (BT-474, SHP-77, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.29×** | +5.7 | 8e-07 | 26/48 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.19× | +5.6 | 1e-06 | 22/49 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.23×** | +4.7 | 2e-04 | 26/48 (BT-474, SNU-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.24×** | +4.4 | 7e-04 | 25/48 (NCI-H23, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.20× | +4.1 | 0.002 | 19/48 (NCI-H2030, NCI-H2347, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.7 | 0.010 | 19/48 (NCI-H460, NCI-H1573, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.18× | +3.7 | 0.011 | 18/48 (BT-474, SHP-77, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.6 | 0.012 | 12/48 (HT-29, SW1417, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +3.5 | 0.019 | 17/48 (BT-474, SW1417, …) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.10× | +3.1 | 0.070 | 1/49 (H4) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 390.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (KATO III 0.159×, RPMI-7951 0.244×, SNU-1 0.149×, SW1417 0.257×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SHP-77 0.144×, RKO 0.121×, KATO III 0.263×, NCI-H23 0.295×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.117×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.678×** | -8.6 | 4e-15 | 31/44 (KATO III, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.677×** | -8.3 | 3e-14 | 34/45 (A-427, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.713×** | -7.8 | 1e-12 | 35/49 (SHP-77, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.786×** | -5.4 | 1e-05 | 31/48 (PANC-1, SK-MEL-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.798×** | -5.2 | 2e-05 | 30/48 (A498, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.838× | -4.1 | 0.004 | 23/48 (A549, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.834× | -3.9 | 0.008 | 19/47 (NCI-H2347, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.847× | -3.9 | 0.008 | 19/48 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.849× | -3.6 | 0.017 | 21/47 (RKO, RPMI-7951, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.906× | -3.3 | 0.062 | 6/48 (COLO 205, C32, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.962× | -3.2 | 0.084 | 1/50 (NCI-H661) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.876× | -3.1 | 0.10 | 13/48 (SW 1088, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 390. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 111 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.50× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.536× (z -9.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 92.4 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +13.2) | — |
| [[LOX-IMVI (line)]] | wt | 74.3 | 4 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.68× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 157 | 2 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.35× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -15.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 98.7 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -22.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 136 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -18.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 72.0 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.50× (z +9.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 121 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.20× (z +11.0) | — |
| [[SNU-1 (line)]] | wt | 108 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.149× (z -17.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 87.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -24.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 70.5 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 3.52× (z +9.1) | — |
| [[KATO III (line)]] | alt | 116 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -20.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 117 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +10.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 83.0 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.24× (z +9.8) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2030 (line)]] | alt | 147 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 91.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +14.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 110 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -25.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 125 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.18× (z +9.7) | — |
| [[SW48 (line)]] | wt | 138 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -11.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 115 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.263× (z -9.0) ⚠ cell-cycle shift, explains ~52% of this change |
| [[HepG2_C3A (line)]] | wt | 91.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.395× (z -8.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 91.8 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 3.19× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 67.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.388× (z -11.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -9.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.446× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.479× (z -10.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -14.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 87.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -16.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 79.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 96.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 107 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 90.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 143 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 69.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 99.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 129 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 390), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPA]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[MON2]] | +0.66 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[AP1G1]] | +0.66 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[SEC31A]] | +0.65 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[SAR1A]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[SEC13]] | +0.63 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[COPB1]] | +0.63 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[SRP54]] | +0.62 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[MYDGF]] | +0.62 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[DHDDS]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[PMM2]] | +0.61 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[COPB2]] | +0.61 | +0.64 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF354B]] | -0.59 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[ZNF354A]] | -0.58 | -0.56 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers SLC39A9's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.647). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.1, -34.2); signed map (-51.9, 11.8). **Vector** length 107, 29.7% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.53 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.56 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.56 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.8 | +12.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.8 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +3.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.6 | +5.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +9.2 |
|  | [[EX229 (drug)]] 0.05 µM |  | +2.1 | +2.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.1 | +2.5 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | +1.9 | +1.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.1 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.9 | -4.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.4 | -0.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.7 | +0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -5.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 39 member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.1 — chr14:69,398,015-69,462,390 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11274, ZIP9 |
| Gene groups (HGNC) | Solute carrier family 39 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUM3](https://www.uniprot.org/uniprotkb/Q9NUM3) (Zinc transporter ZIP9):

> Transports zinc ions across cell and organelle membranes into the cytoplasm and regulates intracellular zinc homeostasis. Participates in the zinc ions efflux out of the secretory compartments. Regulates intracellular zinc level, resulting in the enhancement of AKT1 and MAPK3/MAPK1 (Erk1/2) phosphorylation in response to the BCR activation. Also functions as a membrane androgen receptor that mediates, through a G protein, the non-classical androgen signaling pathway, characterized by the …

**Summary**, from NCBI Gene [55334](https://www.ncbi.nlm.nih.gov/gene/55334):

> Enables G protein-coupled receptor activity; androgen binding activity; and zinc efflux transmembrane transporter activity. Involved in intracellular zinc ion homeostasis; regulation of vascular endothelial cell proliferation; and zinc ion transmembrane transport. Located in several cellular components, including mitochondrial membrane; perinuclear region of cytoplasm; and trans-Golgi network. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20182](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20182) · Entrez [55334](https://www.ncbi.nlm.nih.gov/gene/55334) · UniProt [Q9NUM3](https://www.uniprot.org/uniprotkb/Q9NUM3) · Ensembl [ENSG00000029364](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000029364)

## Data

Gene col 390: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 390); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 390, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 390]; `tensor/DDL_lfc|DDL_z.npy` [390]; `embed/gene_vectors.npy` [390]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 390 or target_col == 390). Every well: [[SLC39A9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC39A9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
