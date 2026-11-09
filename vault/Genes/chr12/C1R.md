---
symbol: "C1R"
type: "gene"
col: 8253
ensembl_id: "ENSG00000159403"
name: "complement C1r"
location: "12p13.31"
module: 167
arm: "+"
pooled_cpm: 19.9
n_lines_expressing: 30
n_dd_up: 15
n_dd_down: 19
n_dd_up_clean: 11
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 25
direction_downstream: 10
tags: ["gene", "module/167"]
generated_by: "tahoemap"
---

# C1R

*complement C1r* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.28× (z +6.6, q 2e-08, up in 5 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM: 1.96× (z +5.4, q 1e-05, up in 21 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.378× (z -11.4, q 2e-27, down in 23 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IDO1]] (+0.68, fdr 7e-06), [[CP]] (+0.67, fdr 7e-06), [[CFB]] (+0.65, fdr 1e-05); moves opposite to [[B4GALT6]] (-0.58, fdr 1e-05), [[CCND1]] (-0.53, fdr 1e-05), [[RASSF3]] (-0.53, fdr 2e-05).
> It is in [[Module 167]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[IFI16]] → it (grade B ⚠); 10 go from it, the strongest it → [[HLA-B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8253.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +6.6 | 2e-08 | 5/16 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.13×** | +6.3 | 9e-08 | 5/22 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.96×** | +5.4 | 1e-05 | 21/28 (MIA PaCa-2, SW 900, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.80×** | +5.0 | 1e-04 | 21/28 (MIA PaCa-2, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.77×** | +4.9 | 1e-04 | 21/28 (MIA PaCa-2, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.73×** | +4.4 | 0.001 | 21/26 (MIA PaCa-2, SW 900, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.52×** | +4.1 | 0.003 | 21/28 (MIA PaCa-2, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.59×** | +3.9 | 0.007 | 19/28 (MIA PaCa-2, HOP62, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.63×** | +3.7 | 0.010 | 4/17 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.39×** | +3.7 | 0.010 | 18/28 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.44×** | +3.4 | 0.030 | 17/28 (MIA PaCa-2, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.53×** | +3.4 | 0.038 | 19/27 (MIA PaCa-2, SW 900, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.49×** | +3.3 | 0.039 | 7/27 (Hs 766T, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Alpelisib (drug)]] 5 µM |  | **2.09×** | +3.2 | 0.051 | 13/25 (NCI-H1792, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.93×** | +3.2 | 0.051 | 18/27 (SW 900, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8253.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.378×** | -11.4 | 2e-27 | 23/27 (RPMI-7951, SW 900, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.437×** | -6.9 | 2e-09 | 23/26 (NCI-H1792, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.499×** | -5.8 | 1e-06 | 23/28 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.493×** | -5.7 | 2e-06 | 19/27 (NCI-H1792, SW 900, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.544×** | -5.1 | 5e-05 | 22/28 (A549, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.568×** | -4.7 | 2e-04 | 21/28 (AN3 CA, NCI-H1792, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.568×** | -4.7 | 2e-04 | 17/28 (HS-578T, NCI-H1792, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.591×** | -4.4 | 9e-04 | 18/28 (SW 900, NCI-H1792, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.601×** | -4.2 | 0.001 | 17/28 (NCI-H23, A549, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.602×** | -4.2 | 0.001 | 19/28 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.719×** | -3.9 | 0.005 | 16/28 (A549, NCI-H2347, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.631×** | -3.8 | 0.006 | 16/28 (A549, NCI-H1792, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.657×** | -3.5 | 0.021 | 19/28 (SW 900, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.662×** | -3.4 | 0.024 | 13/27 (H4, NCI-H1573, …) | two highest doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.652×** | -3.4 | 0.024 | 17/28 (SW 1088, H4, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.749×** | -3.4 | 0.024 | 20/28 (A549, NCI-H2347, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.675×** | -3.3 | 0.036 | 13/27 (A549, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.700×** | -3.0 | 0.093 | 12/28 (MIA PaCa-2, NCI-H1792, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.05 µM |  | **0.701×** | -3.0 | 0.093 | 13/28 (CHP-212, NCI-H2347, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8253. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 37.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -13.8) |
| [[NCI-H1792 (line)]] | alt | 116 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0258× (z -22.5) |
| [[RPMI-7951 (line)]] | alt | 130 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0908× (z -24.9) |
| [[SNU-423 (line)]] | alt | 38.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -17.3) |
| [[H4 (line)]] | wt | 90.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -19.7) |
| [[HS-578T (line)]] | alt | 109 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -14.2) |
| [[NCI-H2347 (line)]] | alt | 20.7 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.147× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.205× (z -10.4) |
| [[SW 1088 (line)]] | alt | 161 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -11.5) |
| [[A498 (line)]] | wt | 51.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -17.3) |
| [[hTERT-HPNE (line)]] | wt | 65.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -10.8) |
| [[J82 (line)]] | alt | 72.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -13.6) |
| [[SK-MEL-2 (line)]] | alt | 10.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -10.5) |
| [[SW 900 (line)]] | alt | 36.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0454× (z -22.1) |
| [[A-172 (line)]] | wt | 33.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -12.4) |
| [[AN3 CA (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0443× (z -9.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[C32 (line)]] | wt | 7.75 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -10.3) |
| [[HOP62 (line)]] | alt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -12.5) |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 6.90 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.84× (z +12.6) ⚠ position not correctable | — |
| [[A-427 (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.81 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.63 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.79 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.26 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8253), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDO1]] | +0.68 | +0.63 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[CP]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT; STRING 401 |
| [[CFB]] | +0.65 | +0.53 / +0.71 | both halves | 1e-05 | same gene group; pathway: HALLMARK_COAGULATION; STRING 524 |
| [[UBE2L6]] | +0.63 | +0.55 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[APOL1]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[IFI44L]] | +0.63 | +0.54 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[TMEM140]] | +0.62 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[TRIM22]] | +0.60 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[IFI16]] | +0.59 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[BST2]] | +0.59 | +0.52 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[TYMP]] | +0.59 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[ODF3B]] | +0.59 | +0.44 / +0.69 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B4GALT6]] | -0.58 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[CCND1]] | -0.53 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[RASSF3]] | -0.53 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[ASAP2]] | -0.50 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ETV4]] | -0.48 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[STK39]] | -0.47 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[AGO2]] | -0.47 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[MYEOV]] | -0.47 | -0.44 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 13, C 12. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFI16]] | B | IFI16 activity raises C1R's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 3.43× lower at baseline in the lines without IFI16 | 0.022 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[SAMD9L]] | B | SAMD9L activity raises C1R's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 3.75× lower at baseline in the lines without SAMD9L | 0.023 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[SLC15A3]] | B | SLC15A3 activity raises C1R's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 3.67× lower at baseline in the lines without SLC15A3 | 0.031 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |
| [[CA12]] | B | CA12 activity raises C1R's level | lines that do not express CA12 (29) vs lines expressing it (21) | 3.98× lower at baseline in the lines without CA12 | 0.036 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers C1R's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[TRIM22]] | B | TRIM22 activity raises C1R's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 2.96× lower at baseline in the lines without TRIM22 | 0.041 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[GBP4]] | B | GBP4 activity raises C1R's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 3.67× lower at baseline in the lines without GBP4 | 0.047 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[XAF1]] | B | XAF1 activity raises C1R's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 3.48× lower at baseline in the lines without XAF1 | 0.052 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |
| [[RHCG]] | B | RHCG activity raises C1R's level | lines that do not express RHCG (33) vs lines expressing it (17) | 2.32× lower at baseline in the lines without RHCG | 0.060 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[CD38]] | B | CD38 activity raises C1R's level | lines that do not express CD38 (35) vs lines expressing it (15) | 2.49× lower at baseline in the lines without CD38 | 0.062 | ⚠ within organs, on part of the lines; also absent: MAGEA10, RNF17, GRIA2; maybe low, not absent |
| [[PTGFR]] | B | PTGFR activity strengthens C1R's drug response | lines that do not express PTGFR (11) vs lines expressing it (17) | the lines without PTGFR respond 0.49× as strongly (z diff +2.40); rises at some drug-doses, falls at others (32% from rises): Harringtonine 5 µM: 0.81x vs 0.25x (z diff +5.1); Homoharringtonine 5 µM: 0.43x vs 0.17x (z diff +5.0); Dinaciclib 0.5 µM: 0.69x vs 1.25x (z diff +2.6) | 0.063 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[ZNF883]] | B | ZNF883 activity raises C1R's level | lines that do not express ZNF883 (22) vs lines expressing it (28) | 2.69× lower at baseline in the lines without ZNF883 | 0.067 | ⚠ within organs, on part of the lines; also absent: AK5, SOX5, GAP43 |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 6, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-B]] | B | C1R activity raises HLA-B's level | lines that do not express C1R (20) vs lines expressing it (30) | 3.22× lower at baseline in the lines without C1R | 0.007 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, LOX, RRAD |
| [[GOLGA8N]] | B | C1R activity raises GOLGA8N's level | lines that do not express C1R (20) vs lines expressing it (30) | 1.63× lower at baseline in the lines without C1R | 0.034 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, LOX, RRAD |
| [[UBE2L6]] | B | C1R activity raises UBE2L6's level | lines that do not express C1R (20) vs lines expressing it (30) | 2.52× lower at baseline in the lines without C1R | 0.037 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, LOX, RRAD |
| [[GBP4]] | B | C1R activity raises GBP4's level | lines that do not express C1R (20) vs lines expressing it (30) | 3.24× lower at baseline in the lines without C1R | 0.065 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, LOX, RRAD |
| [[VAMP5]] | B | C1R activity raises VAMP5's level | lines that do not express C1R (20) vs lines expressing it (30) | 1.91× lower at baseline in the lines without C1R | 0.087 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, LOX, RRAD |
| [[TYMP]] | B | C1R activity strengthens TYMP's drug response | lines that do not express C1R (12) vs lines expressing it (17) | the lines without C1R respond 0.63× as strongly (z diff +1.97); strongest at Homoharringtonine 5 µM: 0.73x vs 0.37x (z diff +3.6) | 0.093 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, LOX, RRAD; target measured in part of the lines; artifact flags |
| [[CFH]] | C | C1R activity raises CFH's level | lines that do not express C1R (20) vs lines expressing it (30) | 3.18× lower at baseline in the lines without C1R | 0.029 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, LOX, RRAD; co-absent with the target |
| [[LOX]] | C | C1R activity raises LOX's level | lines that do not express C1R (20) vs lines expressing it (30) | 7.43× lower at baseline in the lines without C1R | 0.030 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, LOX, RRAD; co-absent with the target |
| [[IFI44L]] | C | C1R activity raises IFI44L's level | lines that do not express C1R (20) vs lines expressing it (30) | 4.46× lower at baseline in the lines without C1R | 0.032 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, LOX, RRAD; co-absent with the target |
| [[OR9Q1]] | C | C1R activity raises OR9Q1's level | lines that do not express C1R (20) vs lines expressing it (30) | 3.05× lower at baseline in the lines without C1R | 0.079 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, LOX, RRAD; co-absent with the target |

## Where it sits

- **Module**: [[Module 167]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.667). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.9, 49.7); signed map (59.9, 28.7). **Vector** length 96.2, 30.7% of its response variance represented; |z| ≥ 3 in 791 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trametinib (drug)]] 0.5 µM |  | +4.4 | +4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.2 | +4.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.1 | +5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.8 | +5.4 |
|  | [[Trametinib (drug)]] 5 µM |  | +3.8 | +4.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.3 | +3.4 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -4.6 | -3.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.4 | -2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.2 | -3.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.1 | -2.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.1 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | complement C1r |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:7,080,214-7,092,540 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Serine proteases; Sushi domain containing; Complement system activation components |
| Hallmark sets | COAGULATION, COMPLEMENT, INTERFERON_GAMMA_RESPONSE |
| Reactome | 5 pathways, smallest: Creation of C4 and C2 activators; Initial triggering of complement; Regulation of Complement cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [P00736](https://www.uniprot.org/uniprotkb/P00736) (Complement C1r subcomponent):

> Serine protease component of the complement C1 complex, a multiprotein complex that initiates the classical pathway of the complement system, a cascade of proteins that leads to phagocytosis and breakdown of pathogens and signaling that strengthens the adaptive immune system. C1R catalyzes the first enzymatic step in the classical complement pathway: it is activated by the C1Q subcomplex of the C1 complex, which associates with IgG or IgM immunoglobulins complexed with antigens to form …

**Summary**, from NCBI Gene [715](https://www.ncbi.nlm.nih.gov/gene/715):

> This gene encodes a member of the peptidase S1 protein family. The encoded protein is a proteolytic subunit in the complement system C1 complex. The complement system acts as a mediator in the innate immune response by ultimately triggering phagocytosis, inflammation, and rupturing the bacterial cell wall. Mutations in this gene are associated with Ehlers-Danlos Syndrome. [provided by RefSeq, Dec 2018]

**Accessions** — [HGNC:1246](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1246) · Entrez [715](https://www.ncbi.nlm.nih.gov/gene/715) · UniProt [P00736](https://www.uniprot.org/uniprotkb/P00736) · Ensembl [ENSG00000159403](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159403)

## Data

Gene col 8253: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8253); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8253, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8253]; `tensor/DDL_lfc|DDL_z.npy` [8253]; `embed/gene_vectors.npy` [8253]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8253 or target_col == 8253). Every well: [[C1R — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C1R.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
