---
symbol: "GIT1"
type: "gene"
col: 2929
ensembl_id: "ENSG00000108262"
name: "GIT ArfGAP 1"
location: "17q11.2"
module: 2
arm: "+"
pooled_cpm: 26.92
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 5
n_dd_up_clean: 14
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# GIT1

*GIT ArfGAP 1* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.79× (z +14.5, q 4e-45, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.347× (z -7.8, q 3e-12, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF38]] (+0.75, fdr 7e-06), [[ZFYVE21]] (+0.70, fdr 1e-05), [[CBFA2T2]] (+0.69, fdr 1e-05); moves opposite to [[MIS12]] (-0.65, fdr 1e-05), [[ZNF620]] (-0.63, fdr 1e-05), [[SENP1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ANKRD13B]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2929.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.79×** | +14.5 | 4e-45 | 46/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +14.0 | 3e-42 | 44/48 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.44×** | +12.6 | 2e-34 | 46/48 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.36×** | +12.2 | 7e-32 | 45/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +6.9 | 6e-10 | 36/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.60×** | +6.7 | 2e-09 | 27/43 (NCI-H1573, A-427, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.8 | 5e-07 | 30/47 (NCI-H1792, CHP-212, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.7 | 7e-07 | 30/47 (LOX-IMVI, NCI-H23, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +5.3 | 8e-06 | 27/45 (SW48, PANC-1, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.45×** | +5.1 | 2e-05 | 18/36 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +4.9 | 6e-05 | 32/48 (LOX-IMVI, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.42×** | +4.7 | 1e-04 | 25/48 (LS 180, A549, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.001 | 21/48 (LOX-IMVI, KATO III, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.33×** | +4.0 | 0.002 | 22/46 (Hs 766T, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.66×** | +3.8 | 0.007 | 13/48 (LOX-IMVI, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.42×** | +3.5 | 0.015 | 12/48 (LoVo, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.016 | 16/48 (LS 180, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.30×** | +3.0 | 0.074 | 11/47 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.082 | 15/44 (HEC-1-A, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +2.9 | 0.095 | 12/48 (A-172, HS-578T, …) | rises with dose | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.33×** | +2.9 | 0.098 | 12/47 (HCT15, A498, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2929.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.347×** | -7.8 | 3e-12 | 39/48 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.725×** | -6.4 | 3e-08 | 29/48 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.646×** | -6.0 | 5e-07 | 33/48 (A-427, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.727×** | -4.5 | 9e-04 | 27/47 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.563×** | -4.2 | 0.002 | 23/47 (A-427, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pimozide (drug)]] 5 µM |  | 0.801× | -3.2 | 0.15 | 12/48 (NCI-H2030, HOP62, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2929. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 39.8 | 5 | 1 | [[Panobinostat (drug)]] 0.5 µM 4.45× (z +13.3) | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -11.0) |
| [[A-172 (line)]] | wt | 48.2 | 2 | 3 | [[Panobinostat (drug)]] 0.5 µM 2.63× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -12.9) |
| [[SW480 (line)]] | alt | 29.2 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.58× (z +11.9) | — |
| [[A-427 (line)]] | wt | 40.0 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.199× (z -13.1) |
| [[HEC-1-A (line)]] | alt | 42.3 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.53× (z +11.8) | — |
| [[KATO III (line)]] | alt | 40.8 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.47× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 27.9 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +14.6) | — |
| [[NCI-H460 (line)]] | wt | 24.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +15.0) | — |
| [[A498 (line)]] | wt | 26.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +14.2) | — |
| [[A549 (line)]] | wt | 30.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.34× (z +19.5) | — |
| [[C32 (line)]] | wt | 21.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[HOP62 (line)]] | alt | 22.6 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.62× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 19.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.350× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 18.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +10.8) | — |
| [[J82 (line)]] | alt | 28.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -12.7) |
| [[LoVo (line)]] | wt | 20.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 14.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H2030 (line)]] | alt | 12.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 36.7 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 36.4 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.35× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 23.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -11.7) |
| [[RKO (line)]] | wt | 28.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +11.3) | — |
| [[SW1417 (line)]] | alt | 39.9 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.78× (z +8.5) | — |
| [[SW48 (line)]] | wt | 44.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +10.8) | — |
| [[AN3 CA (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2929), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF38]] | +0.75 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[ZFYVE21]] | +0.70 | +0.57 / +0.72 | both halves | 1e-05 |  |
| [[CBFA2T2]] | +0.69 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[HEBP1]] | +0.68 | +0.46 / +0.67 | both halves | 3e-05 |  |
| [[TSPAN17]] | +0.68 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[STRN]] | +0.68 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[IGSF8]] | +0.66 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[GNB2]] | +0.66 | +0.48 / +0.62 | both halves | 2e-05 | pathway: Neuronal System |
| [[PKD1]] | +0.66 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[MIIP]] | +0.66 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[ZDHHC8]] | +0.65 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[PKD1P6]] | +0.65 | +0.62 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIS12]] | -0.65 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[ZNF620]] | -0.63 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[SENP1]] | -0.62 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[USP40]] | -0.62 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[RBM23]] | -0.62 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[OCIAD1]] | -0.61 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[MCTS1]] | -0.61 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[LEKR1]] | -0.60 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[RIPK2-DT]] | -0.60 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[ZNF655]] | -0.60 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[ST7L]] | -0.60 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[ZNF268]] | -0.59 | -0.53 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD13B]] | C | ANKRD13B activity raises GIT1's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 2.00× lower at baseline in the lines without ANKRD13B | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.635). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-5.7, -20.2); signed map (-41.4, -1.8). **Vector** length 88.1, 20.3% of its response variance represented; |z| ≥ 3 in 884 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.7 | +12.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.5 | +12.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.1 | +14.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.0 | +5.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.2 | +6.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.3 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +2.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.0 | +1.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +3.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.7 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.9 | -4.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.2 | -6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.7 | -6.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.3 | -7.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -4.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | GIT ArfGAP 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:29,573,475-29,594,054 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | ArfGAPs; Ankyrin repeat domain containing |
| Reactome | 21 pathways, smallest: Activation of RAC1 downstream of NMDARs; Ephrin signaling; RHOV GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2X7](https://www.uniprot.org/uniprotkb/Q9Y2X7) (ARF GTPase-activating protein GIT1):

> GTPase-activating protein for ADP ribosylation factor family members, including ARF1. Multidomain scaffold protein that interacts with numerous proteins and therefore participates in many cellular functions, including receptor internalization, focal adhesion remodeling, and signaling by both G protein-coupled receptors and tyrosine kinase receptors (By similarity). Through PAK1 activation, positively regulates microtubule nucleation during interphase. Plays a role in the regulation of …

**Summary**, from NCBI Gene [28964](https://www.ncbi.nlm.nih.gov/gene/28964):

> Enables gamma-tubulin binding activity. Involved in positive regulation of microtubule nucleation and regulation of cytokinesis. Located in cytosol; focal adhesion; and microtubule cytoskeleton. Implicated in attention deficit hyperactivity disorder. Biomarker of Huntington's disease. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:4272](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4272) · Entrez [28964](https://www.ncbi.nlm.nih.gov/gene/28964) · UniProt [Q9Y2X7](https://www.uniprot.org/uniprotkb/Q9Y2X7) · Ensembl [ENSG00000108262](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108262)

## Data

Gene col 2929: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2929); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2929, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2929]; `tensor/DDL_lfc|DDL_z.npy` [2929]; `embed/gene_vectors.npy` [2929]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2929 or target_col == 2929). Every well: [[GIT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GIT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
