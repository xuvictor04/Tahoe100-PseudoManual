---
symbol: "STARD4-AS1"
type: "gene"
col: 14472
ensembl_id: "ENSG00000246859"
name: "STARD4 antisense RNA 1"
location: "5q22.1"
module: 26
arm: "+"
pooled_cpm: 7.05
n_lines_expressing: 48
n_dd_up: 16
n_dd_down: 12
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# STARD4-AS1

*STARD4 antisense RNA 1* — 5q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.44× (z +30.2, q 0e+00, up in 39 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.562× (z -7.2, q 3e-10, down in 25 of 44 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PBLD]] (+0.72, fdr 2e-04), [[TMLHE-AS1]] (+0.69, fdr 2e-05), [[CCDC90B-AS1]] (+0.68, fdr 1e-04); moves opposite to [[COMMD2]] (-0.71, fdr 2e-05), [[GPATCH11]] (-0.68, fdr 1e-04), [[WRAP73]] (-0.61, fdr 2e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14472.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.44×** | +30.2 | 0e+00 | 39/40 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.75×** | +12.3 | 4e-32 | 24/38 (NCI-H460, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.50×** | +11.6 | 1e-28 | 12/23 (NCI-H460, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.59×** | +11.5 | 1e-28 | 27/39 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +9.0 | 3e-17 | 7/13 (NCI-H2347, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +8.3 | 6e-15 | 4/10 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +7.9 | 3e-13 | 24/45 (A-172, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +4.6 | 3e-04 | 15/39 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +4.3 | 9e-04 | 12/42 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.39×** | +4.1 | 0.002 | 5/32 (NCI-H2030, HS-578T, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.005 | 12/44 (NCI-H23, NCI-H2030, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.040 | 6/44 (A549, NCI-H1573, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.044 | 10/43 (SW480, HOP62, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.20×** | +3.2 | 0.061 | 2/44 (NCI-H1792, Panc 03.27) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.068 | 9/43 (RPMI-7951, A549, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.082 | 5/44 (HS-578T, PANC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14472.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.562×** | -7.2 | 3e-10 | 25/44 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.570×** | -7.1 | 5e-10 | 19/37 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.471×** | -4.9 | 1e-04 | 12/37 (NCI-H460, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.707×** | -4.4 | 0.002 | 13/42 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.712×** | -4.3 | 0.002 | 13/44 (A-427, H4, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.721×** | -4.1 | 0.004 | 10/43 (NCI-H2030, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.728×** | -3.8 | 0.010 | 9/44 (LOX-IMVI, LS 180, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.739×** | -3.8 | 0.010 | 12/43 (RPMI-7951, HepG2/C3A, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.740×** | -3.8 | 0.010 | 12/44 (A-427, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.771×** | -3.3 | 0.061 | 16/44 (LOX-IMVI, A-427, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.772×** | -3.2 | 0.061 | 14/44 (A-427, C32, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.924× | -3.2 | 0.064 | 6/45 (A549, NCI-H1573, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.768×** | -3.2 | 0.064 | 14/42 (SW480, NCI-H1573, …) | two highest doses | composition shift |
| [[Mifepristone (drug)]] 5 µM |  | 0.779× | -3.0 | 0.11 | 6/43 (COLO 205, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14472. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.59 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 24.8× (z +18.0) | — |
| [[A-427 (line)]] | wt | 110 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0742× (z -12.8) |
| [[NCI-H460 (line)]] | wt | 5.57 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.9× (z +20.0) | — |
| [[LOX-IMVI (line)]] | wt | 5.07 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.58× (z +9.4) | [[Docetaxel (drug)]] 0.05 µM 0.101× (z -8.9) ⚠ transcription drop |
| [[RPMI-7951 (line)]] | alt | 9.54 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.50× (z +9.0) | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0832× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 6.29 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +9.0) | — |
| [[A498 (line)]] | wt | 3.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 2.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 3.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.66× (z +8.7) | — |
| [[HCT15 (line)]] | alt | 5.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 2.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.8× (z +14.8) | — |
| [[HOP62 (line)]] | alt | 4.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.84× (z +10.7) | — |
| [[hTERT-HPNE (line)]] | wt | 6.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.74× (z +8.6) | — |
| [[KATO III (line)]] | alt | 2.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.6× (z +11.6) | — |
| [[LoVo (line)]] | wt | 4.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.8× (z +15.6) | — |
| [[LS 180 (line)]] | wt | 2.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.0× (z +12.7) | — |
| [[SHP-77 (line)]] | alt | 2.94 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 5 µM 0.109× (z -8.9) |
| [[SNU-423 (line)]] | alt | 9.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.79× (z +9.8) | — |
| [[SW480 (line)]] | alt | 6.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +12.4) | — |
| [[A549 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14472), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBLD]] | +0.72 | +0.63 / +0.30 | both halves | 2e-04 |  |
| [[TMLHE-AS1]] | +0.69 | +0.57 / +0.47 | both halves | 2e-05 | same gene group |
| [[CCDC90B-AS1]] | +0.68 | +0.61 / +0.33 | both halves | 1e-04 | same gene group |
| [[FAM174B]] | +0.68 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[BHLHE40-AS1]] | +0.68 | +0.58 / +0.43 | both halves | 4e-05 | same gene group |
| [[HDAC2-AS2]] | +0.67 | +0.51 / +0.52 | both halves | 1e-05 | same gene group |
| [[CIBAR1-DT]] | +0.67 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[RNPC3-DT]] | +0.67 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[CPEB2-DT]] | +0.66 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[SNHG31]] | +0.66 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[EFCAB5]] | +0.66 | +0.63 / +0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[PIPOX]] | +0.66 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[CFAP418-AS1]] | +0.66 | +0.67 / +0.25 | both halves | 4e-04 | same gene group |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD2]] | -0.71 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[GPATCH11]] | -0.68 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[WRAP73]] | -0.61 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[PIGH]] | -0.61 | -0.44 / -0.27 | both halves | 3e-04 |  |
| [[TAMM41]] | -0.60 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[DPY30]] | -0.60 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[MRPS31P4]] | -0.60 | -0.28 / -0.54 | both halves | 3e-04 |  |
| [[NDUFA12]] | -0.60 | -0.33 / -0.32 | both halves | 1e-04 |  |
| [[RSAD1]] | -0.60 | -0.36 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers STARD4-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CNN3-DT]] | B | CNN3-DT activity raises STARD4-AS1's level | lines that do not express CNN3-DT (8) vs lines expressing it (42) | 1.94× lower at baseline in the lines without CNN3-DT | 0.032 | ⚠ within organs, on part of the lines; also absent: MPP2, CNN3, SLC35F1; maybe low, not absent |
| [[CACNA2D1]] | B | CACNA2D1 activity raises STARD4-AS1's level | lines that do not express CACNA2D1 (20) vs lines expressing it (30) | 1.55× lower at baseline in the lines without CACNA2D1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ZNF229, BVES-AS1, CCDC169 |
| [[IGF2BP1]] | B | IGF2BP1 activity raises STARD4-AS1's level | lines that do not express IGF2BP1 (23) vs lines expressing it (27) | 1.71× lower at baseline in the lines without IGF2BP1 | 0.069 | ⚠ within organs, on part of the lines; also absent: SLFN11, RUNX3, DPY19L2 |
| [[MAP2K1]] | B | MAP2K1 activity lowers STARD4-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[LHFPL6]] | B | LHFPL6 activity raises STARD4-AS1's level | lines that do not express LHFPL6 (11) vs lines expressing it (39) | 1.79× lower at baseline in the lines without LHFPL6 | 0.092 | ⚠ within organs, on part of the lines; also absent: KATNAL2, AFAP1L1, TTC7B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.683). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (14.9, 19.9); signed map (26.8, -3.8). **Vector** length 71.1, 11.1% of its response variance represented; |z| ≥ 3 in 1,030 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +13.0 | +30.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +11.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +8.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.5 | +3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.4 | +2.9 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.3 | -7.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.8 | -7.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | -2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.1 | -3.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -2.6 | -3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -2.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -3.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.4 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.3 | -2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | STARD4 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q22.1 — chr5:111,510,396-111,739,726 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44117](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44117) · Entrez [100505678](https://www.ncbi.nlm.nih.gov/gene/100505678) · Ensembl [ENSG00000246859](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000246859)

## Data

Gene col 14472: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14472); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14472, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14472]; `tensor/DDL_lfc|DDL_z.npy` [14472]; `embed/gene_vectors.npy` [14472]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14472 or target_col == 14472). Every well: [[STARD4-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STARD4-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
