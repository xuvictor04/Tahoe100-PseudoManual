---
symbol: "SEC24B-AS1"
type: "gene"
col: 14512
ensembl_id: "ENSG00000247950"
name: "SEC24B antisense RNA 1"
location: "4q25"
module: 15
arm: "+"
pooled_cpm: 3.7
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 27
n_dd_up_clean: 19
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# SEC24B-AS1

*SEC24B antisense RNA 1* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.74× (z +22.4, q 0e+00, up in 35 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (15 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.456× (z -7.7, q 1e-11, down in 25 of 43 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.542× (z -6.2, q 6e-08, down in 21 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF213-AS1]] (+0.79, fdr 7e-06), [[SPESP1]] (+0.78, fdr 7e-06), [[ZNF460-AS1]] (+0.77, fdr 7e-06); moves opposite to [[SMYD3]] (-0.63, fdr 5e-04), [[STUB1]] (-0.62, fdr 2e-04), [[EDA]] (-0.61, fdr 3e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14512.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.74×** | +22.4 | 0e+00 | 35/37 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.37×** | +8.5 | 6e-15 | 21/33 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.98×** | +6.7 | 4e-09 | 12/19 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +6.1 | 1e-07 | 19/36 (HEC-1-A, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.62×** | +4.9 | 1e-04 | 15/46 (C-33 A, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +4.6 | 4e-04 | 2/5 (HOP62, CFPAC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.6 | 4e-04 | 6/46 (HEC-1-A, BT-474, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.49×** | +3.7 | 0.013 | 9/46 (C32, NCI-H2030, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.44×** | +3.7 | 0.013 | 9/43 (HT-29, NCI-H2030, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.30×** | +3.7 | 0.013 | 6/45 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.014 | 5/44 (C32, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.021 | 5/42 (KATO III, SW 900, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.44×** | +3.4 | 0.025 | 6/48 (HEC-1-A, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.026 | 8/45 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.89×** | +3.4 | 0.026 | 6/43 (HOP62, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.041 | 3/45 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.82×** | +3.2 | 0.046 | 1/44 (NCI-H2030) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.05 µM |  | **1.39×** | +3.2 | 0.047 | 0/44 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 15 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14512.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.456×** | -7.7 | 1e-11 | 25/43 (PANC-1, KATO III, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.519×** | -6.7 | 6e-09 | 20/45 (H4, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.520×** | -6.6 | 6e-09 | 20/46 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.522×** | -6.6 | 6e-09 | 26/43 (H4, HT-29, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.542×** | -6.2 | 6e-08 | 21/44 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.560×** | -5.9 | 4e-07 | 18/44 (NCI-H460, A549, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.572×** | -5.7 | 1e-06 | 17/46 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.599×** | -5.2 | 2e-05 | 12/35 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.700×** | -5.1 | 2e-05 | 18/37 (A498, PANC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.614×** | -4.9 | 5e-05 | 14/46 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.635×** | -4.6 | 2e-04 | 14/44 (LOX-IMVI, COLO 205, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.438×** | -4.4 | 6e-04 | 11/40 (C-33 A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.653×** | -4.3 | 7e-04 | 13/45 (SW 900, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.673×** | -4.0 | 0.003 | 17/44 (BT-474, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~63% of this change | **0.665×** | -4.0 | 0.003 | 13/26 (NCI-H2030, C32, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.774×** | -3.7 | 0.008 | 9/46 (MIA PaCa-2, LOX-IMVI, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.703×** | -3.6 | 0.012 | 12/45 (NCI-H23, hTERT-HPNE, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.708×** | -3.5 | 0.014 | 12/44 (J82, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.542×** | -3.2 | 0.032 | 12/33 (NCI-H1792, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fluvoxamine (drug)]] 0.05 µM |  | **0.711×** | -3.2 | 0.037 | 4/43 (HepG2/C3A, A-172, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.720×** | -3.1 | 0.042 | 9/41 (H4, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.743×** | -3.0 | 0.061 | 7/46 (AN3 CA, NCI-H661, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **0.735×** | -3.0 | 0.062 | 10/44 (C32, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[EX229 (drug)]] 0.05 µM |  | **0.738×** | -2.9 | 0.080 | 9/43 (A498, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14512. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 6.85 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0632× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 4.72 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 2.82 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +8.6) | — |
| [[C32 (line)]] | wt | 6.07 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0734× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 2.86 | 0 | 1 | — | [[Sunitinib (drug)]] 0.5 µM 0.0620× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 4.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.69× (z +10.8) | — |
| [[LoVo (line)]] | wt | 3.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.73× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 3.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.42× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.194× (z -8.9) ⚠ cell-cycle shift, explains ~53% of this change |
| [[NCI-H460 (line)]] | wt | 2.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.68× (z +8.7) | — |
| [[A-427 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.98 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14512), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF213-AS1]] | +0.79 | +0.61 / +0.69 | both halves | 7e-06 | same gene group |
| [[SPESP1]] | +0.78 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[ZNF460-AS1]] | +0.77 | +0.60 / +0.62 | both halves | 7e-06 | same gene group |
| [[FKBP14-AS1]] | +0.75 | +0.59 / +0.62 | both halves | 7e-06 | same gene group |
| [[TSTD3]] | +0.75 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[MFF-DT]] | +0.74 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[SPATA1]] | +0.74 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[CDNF]] | +0.73 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[KLF3-AS1]] | +0.72 | +0.53 / +0.57 | both halves | 1e-05 | same gene group |
| [[DICER1-AS1]] | +0.72 | +0.59 / +0.53 | both halves | 1e-05 | same gene group |
| [[MYLK4]] | +0.71 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[SAP30L-AS1]] | +0.71 | +0.64 / +0.49 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMYD3]] | -0.63 | -0.49 / -0.23 | both halves | 5e-04 |  |
| [[STUB1]] | -0.62 | -0.35 / -0.30 | both halves | 2e-04 |  |
| [[EDA]] | -0.61 | -0.48 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SEC24B-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02987]] | B | LINC02987 activity lowers SEC24B-AS1's level | lines that do not express LINC02987 (5) vs lines expressing it (45) | 1.25× higher at baseline in the lines without LINC02987 | 0.059 | ⚠ within organs, on part of the lines; also absent: NME4, ZNF566, SPIRE1 |
| [[LMCD1]] | B | LMCD1 activity lowers SEC24B-AS1's level | lines that do not express LMCD1 (11) vs lines expressing it (39) | 1.40× higher at baseline in the lines without LMCD1 | 0.075 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.855). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (2.2, 21.4); signed map (27.6, -6.4). **Vector** length 65.5, 9.97% of its response variance represented; |z| ≥ 3 in 1,099 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.9 | +22.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +8.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.6 | +6.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.0 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +0.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.8 | +3.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.5 | +2.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -3.5 | -6.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.5 | -4.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.2 | -4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -2.8 | -4.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -2.7 | -6.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -1.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.1 | -2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | SEC24B antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q25 — chr4:109,347,475-109,433,817 (-) |
| Ensembl biotype | lncRNA |
| Also known as | 1/2-SBSRNA4 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100533182](https://www.ncbi.nlm.nih.gov/gene/100533182):

> This lncRNA contains a single Alu element which, along with 1/2-sbsRNA3, appears to target the 3' UTR Alu element in MTAP. Downregulation of the RNA appears to up-regulate the target. [provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:44003](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44003) · Entrez [100533182](https://www.ncbi.nlm.nih.gov/gene/100533182) · Ensembl [ENSG00000247950](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247950)

## Data

Gene col 14512: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14512); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14512, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14512]; `tensor/DDL_lfc|DDL_z.npy` [14512]; `embed/gene_vectors.npy` [14512]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14512 or target_col == 14512). Every well: [[SEC24B-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC24B-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
