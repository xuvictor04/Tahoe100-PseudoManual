---
symbol: "COL4A2"
type: "gene"
col: 5616
ensembl_id: "ENSG00000134871"
name: "collagen type IV alpha 2 chain"
location: "13q34"
module: 66
arm: "+"
pooled_cpm: 88.74
n_lines_expressing: 25
n_dd_up: 7
n_dd_down: 19
n_dd_up_clean: 4
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 23
direction_downstream: 25
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# COL4A2

*collagen type IV alpha 2 chain* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.04× (z +21.8, q 0e+00, up in 18 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.19× (z +4.8, q 2e-04, up in 4 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.751× (z -5.6, q 9e-06, down in 17 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL4A1]] (+0.86, fdr 7e-06, ⚠ same locus), [[FN1]] (+0.67, fdr 7e-06), [[ANTXR1]] (+0.67, fdr 7e-06), [[SDC2]] (+0.65, fdr 7e-06); moves opposite to [[ARL8A]] (-0.50, fdr 1e-04), [[RPL36AL]] (-0.46, fdr 3e-04, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[RASSF7]] (-0.46, fdr 1e-04), [[KDF1]] (-0.45, fdr 1e-04).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[ARHGDIB]] → it (grade B ⚠); 25 go from it, the strongest it → [[COL13A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5616.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.04×** | +21.8 | 0e+00 | 18/23 (A549, HOP62, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.84×** | +18.9 | 0e+00 | 16/21 (HOP62, A549, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.46×** | +17.0 | 0e+00 | 14/21 (HOP62, A549, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.8 | 2e-04 | 4/23 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.26×** | +4.1 | 0.004 | 10/23 (HOP62, SNU-423, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.009 | 7/23 (NCI-H1792, RPMI-7951, …) | top dose only |  |
| [[Sacubitril_Valsartan (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.035 | 8/23 (SNU-423, A549, …) | inconsistent across doses | position effect removed |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.044 | 7/23 (A-172, J82, …) | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.044 | 6/23 (A549, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Vitamin K4 (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.084 | 0/24 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5616.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.751×** | -5.6 | 9e-06 | 17/23 (NCI-H1792, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.754×** | -5.5 | 9e-06 | 14/23 (NCI-H1792, RPMI-7951, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.753×** | -5.3 | 1e-05 | 9/22 (A549, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.753×** | -5.3 | 1e-05 | 12/23 (C32, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.764×** | -5.3 | 2e-05 | 17/23 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.774×** | -5.0 | 5e-05 | 13/23 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.791×** | -4.6 | 3e-04 | 5/22 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.793×** | -4.5 | 4e-04 | 9/23 (C32, HOP62, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.807×** | -4.2 | 0.002 | 15/23 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.808×** | -4.2 | 0.002 | 14/23 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.813×** | -4.0 | 0.003 | 10/23 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | 0.868× | -3.9 | 0.005 | 1/23 (NCI-H1792) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.689×** | -3.8 | 0.006 | 12/23 (A498, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.874× | -3.7 | 0.009 | 10/23 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.829×** | -3.7 | 0.009 | 13/24 (CHP-212, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.830×** | -3.7 | 0.009 | 16/23 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.820×** | -3.6 | 0.011 | 2/23 (J82, HEC-1-A) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5616. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 94.2 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -18.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.257× (z -10.7) |
| [[HOP62 (line)]] | alt | 299 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +10.7) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.415× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.448× (z -8.6) |
| [[A549 (line)]] | wt | 92.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +12.2) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 323 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -12.7) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 121 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.130× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 259 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 56.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -14.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 40.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -19.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 386 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +9.2) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 137 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +9.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CHP-212 (line)]] | wt | 303 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 294 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 23.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 29.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.91× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H596 (line)]] | alt | 69.9 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.117× (z -10.1) ⚠ transcription drop |
| [[Panc 03.27 (line)]] | alt | 140 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 900 (line)]] | alt | 29.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 274 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.62 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.65 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 19.7 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.07 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.51 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.46 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.02 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.68 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 488 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.93 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.67 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.15 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.87 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.07 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.26 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 7.68 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.58 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.62 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.23 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.39 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 277 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 312 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.64 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.95 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.68 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5616), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL4A1]] | +0.86 | +0.75 / +0.91 | both halves | 7e-06 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 999; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[FN1]] | +0.67 | +0.62 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT; STRING 750 |
| [[ANTXR1]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 | same gene group; pathway: Bacterial Infection Pathways |
| [[SDC2]] | +0.65 | +0.65 / +0.59 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[PDGFRB]] | +0.64 | +0.67 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 428 |
| [[COL6A3]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 792 |
| [[DKK3]] | +0.60 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[AK5]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ITGA4]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 | pathway: Extracellular matrix organization; STRING 744 |
| [[PXDN]] | +0.58 | +0.44 / +0.67 | both halves | 3e-05 | pathway: Assembly of collagen fibrils and other multimeric structures; STRING 447 |
| [[COL1A2]] | +0.58 | +0.61 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 786 |
| [[EHD3]] | +0.57 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[COL5A1]] | +0.57 | +0.62 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 872 |

## Genes that move opposite

*6 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL8A]] | -0.50 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[RPL36AL]] ⚠ | -0.46 | -0.28 / -0.50 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[RASSF7]] | -0.46 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[KDF1]] | -0.45 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[TMEM53]] | -0.44 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[SMIM26]] ⚠ | -0.44 | -0.31 / -0.44 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 2, C 21. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGDIB]] | B | ARHGDIB activity raises COL4A2's level | lines that do not express ARHGDIB (23) vs lines expressing it (27) | 1.95× lower at baseline in the lines without ARHGDIB | 0.057 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |
| [[COL13A1]] | B | COL13A1 activity raises COL4A2's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 3.72× lower at baseline in the lines without COL13A1 | 0.095 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[COL4A1]] | C | COL4A1 activity raises COL4A2's level | lines that do not express COL4A1 (29) vs lines expressing it (21) | 15.73× lower at baseline in the lines without COL4A1 | 1e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL4A2, NID2, ABI3BP; co-absent with the target |
| [[NID2]] | C | NID2 activity raises COL4A2's level | lines that do not express NID2 (32) vs lines expressing it (18) | 9.41× lower at baseline in the lines without NID2 | 1e-03 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1; co-absent with the target |
| [[BICC1]] | C | BICC1 activity raises COL4A2's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 9.28× lower at baseline in the lines without BICC1 | 0.001 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2; co-absent with the target |
| [[COL7A1]] | C | COL7A1 activity raises COL4A2's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 7.49× lower at baseline in the lines without COL7A1 | 0.007 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent; co-absent with the target |
| [[MYLK]] | C | MYLK activity raises COL4A2's level | lines that do not express MYLK (20) vs lines expressing it (30) | 7.32× lower at baseline in the lines without MYLK | 0.012 | ⚠ within organs, on part of the lines; also absent: ADAMTS2, COL4A1, CPEB1; co-absent with the target |
| [[ADAMTS12]] | C | ADAMTS12 activity raises COL4A2's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 7.78× lower at baseline in the lines without ADAMTS12 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises COL4A2's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 9.80× lower at baseline in the lines without PDGFRB | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[COL15A1]] | C | COL15A1 activity raises COL4A2's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 3.96× lower at baseline in the lines without COL15A1 | 0.017 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises COL4A2's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 7.56× lower at baseline in the lines without ITGA11 | 0.021 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[IGFBP7]] | C | IGFBP7 activity raises COL4A2's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 5.80× lower at baseline in the lines without IGFBP7 | 0.022 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1; co-absent with the target |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 4, C 21. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL13A1]] | B | COL4A2 activity raises COL13A1's level | lines that do not express COL4A2 (25) vs lines expressing it (25) | 2.71× lower at baseline in the lines without COL4A2 | 0.017 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, ROR1-AS1 |
| [[PTPN14]] | B | COL4A2 activity raises PTPN14's level | lines that do not express COL4A2 (25) vs lines expressing it (25) | 1.56× lower at baseline in the lines without COL4A2 | 0.077 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, ROR1-AS1 |
| [[F2R]] | B | COL4A2 activity raises F2R's level | lines that do not express COL4A2 (25) vs lines expressing it (25) | 3.10× lower at baseline in the lines without COL4A2 | 0.079 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, ROR1-AS1 |
| [[DZIP1L]] | B | COL4A2 activity raises DZIP1L's level | lines that do not express COL4A2 (25) vs lines expressing it (25) | 2.20× lower at baseline in the lines without COL4A2 | 0.099 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, ROR1-AS1 |
| [[COL4A1]] | C | COL4A2 activity raises COL4A1's level | lines that do not express COL4A2 (25) vs lines expressing it (25) | 11.77× lower at baseline in the lines without COL4A2 | 3e-04 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, ROR1-AS1; co-absent with the target |
| [[IGFBP7]] | C | COL4A2 activity raises IGFBP7's level | lines that do not express COL4A2 (25) vs lines expressing it (25) | 6.42× lower at baseline in the lines without COL4A2 | 0.016 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, ROR1-AS1; co-absent with the target |
| [[BICC1]] | C | COL4A2 activity raises BICC1's level | lines that do not express COL4A2 (25) vs lines expressing it (25) | 4.70× lower at baseline in the lines without COL4A2 | 0.021 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, ROR1-AS1; co-absent with the target |
| [[FAM20C]] | C | COL4A2 activity raises FAM20C's level | lines that do not express COL4A2 (25) vs lines expressing it (25) | 5.38× lower at baseline in the lines without COL4A2 | 0.024 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, ROR1-AS1; co-absent with the target |
| [[NID2]] | C | COL4A2 activity raises NID2's level | lines that do not express COL4A2 (25) vs lines expressing it (25) | 3.23× lower at baseline in the lines without COL4A2 | 0.034 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, ROR1-AS1; co-absent with the target |
| [[COL15A1]] | C | COL4A2 activity raises COL15A1's level | lines that do not express COL4A2 (25) vs lines expressing it (25) | 2.67× lower at baseline in the lines without COL4A2 | 0.043 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, ROR1-AS1; co-absent with the target |
| [[FN1]] | C | COL4A2 activity raises FN1's level | lines that do not express COL4A2 (25) vs lines expressing it (25) | 6.26× lower at baseline in the lines without COL4A2 | 0.045 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, ROR1-AS1; co-absent with the target |
| [[PCDHGC3]] | C | COL4A2 activity raises PCDHGC3's level | lines that do not express COL4A2 (25) vs lines expressing it (25) | 2.72× lower at baseline in the lines without COL4A2 | 0.054 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, ROR1-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.485). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (54.6, 22.5); signed map (24.7, 41.7). **Vector** length 85.4, 28.3% of its response variance represented; |z| ≥ 3 in 606 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.4 | +21.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.1 | +18.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.0 | +17.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +4.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +3.9 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.7 | +4.1 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.6 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +2.3 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -3.3 | -5.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.8 | -3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.7 | -4.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | collagen type IV alpha 2 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:110,305,812-110,513,209 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22259, DKFZp686I14213 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Network forming collagens |
| Hallmark sets | MYOGENESIS, COMPLEMENT, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 27 pathways, smallest: Anchoring fibril formation; Scavenging by Class A Receptors; Crosslinking of collagen fibrils |
| Matched by | ensembl_id |

**Function**, from UniProt [P08572](https://www.uniprot.org/uniprotkb/P08572) (Collagen alpha-2(IV) chain):

> Type IV collagen is the major structural component of glomerular basement membranes (GBM), forming a 'chicken-wire' meshwork together with laminins, proteoglycans and entactin/nidogen.; Canstatin, a cleavage product corresponding to the collagen alpha 2(IV) NC1 domain, possesses both anti-angiogenic and anti-tumor cell activity. It inhibits proliferation and migration of endothelial cells, reduces mitochondrial membrane potential, and induces apoptosis. Specifically induces Fas-dependent …

**Summary**, from NCBI Gene [1284](https://www.ncbi.nlm.nih.gov/gene/1284):

> This gene encodes one of the six subunits of type IV collagen, the major structural component of basement membranes. The C-terminal portion of the protein, known as canstatin, is an inhibitor of angiogenesis and tumor growth. Like the other members of the type IV collagen gene family, this gene is organized in a head-to-head conformation with another type IV collagen gene so that each gene pair shares a common promoter. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2203](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2203) · Entrez [1284](https://www.ncbi.nlm.nih.gov/gene/1284) · UniProt [P08572](https://www.uniprot.org/uniprotkb/P08572) · Ensembl [ENSG00000134871](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134871)

## Data

Gene col 5616: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5616); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5616, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5616]; `tensor/DDL_lfc|DDL_z.npy` [5616]; `embed/gene_vectors.npy` [5616]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5616 or target_col == 5616). Every well: [[COL4A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL4A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
