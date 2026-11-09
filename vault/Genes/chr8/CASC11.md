---
symbol: "CASC11"
type: "gene"
col: 14607
ensembl_id: "ENSG00000249375"
name: "cancer susceptibility 11"
location: "8q24.21"
module: 35
arm: "+"
pooled_cpm: 6.84
n_lines_expressing: 37
n_dd_up: 21
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# CASC11

*cancer susceptibility 11* — 8q24.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.88× (z +22.7, q 0e+00, up in 27 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.690× (z -4.4, q 0.006, down in 16 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC26]] (+0.71, fdr 1e-05), [[SIAH2-AS1]] (+0.69, fdr 2e-05), [[SAXO1]] (+0.68, fdr 1e-05); moves opposite to [[ALAD]] (-0.64, fdr 6e-05), [[CEP57L1]] (-0.57, fdr 8e-05), [[TTC38]] (-0.57, fdr 1e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[HPF1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14607.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.88×** | +22.7 | 0e+00 | 27/31 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.78×** | +11.2 | 1e-26 | 6/8 (NCI-H460, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.92×** | +10.9 | 2e-25 | 19/34 (NCI-H460, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +9.6 | 1e-19 | 1/3 (A498) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.91×** | +7.7 | 2e-12 | 3/15 (NCI-H460, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.57×** | +7.6 | 3e-12 | 12/33 (SW480, NCI-H1792, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +5.7 | 7e-07 | 11/33 (NCI-H1792, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +5.4 | 5e-06 | 8/28 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +4.8 | 1e-04 | 5/15 (A-427, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.5 | 4e-04 | 8/27 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.99×** | +4.2 | 0.001 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +4.2 | 0.001 | 10/31 (HS-578T, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Rosiglitazone (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.003 | 2/32 (NCI-H1573, SW1417) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +3.9 | 0.004 | 4/33 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +3.9 | 0.004 | 2/26 (SW48, A498) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.007 | 7/34 (NCI-H460, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.031 | 8/34 (SW480, NCI-H1792, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14607.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.690×** | -4.4 | 0.006 | 16/34 (SW48, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.713×** | -4.0 | 0.017 | 9/34 (Panc 03.27, RKO, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Hexylresorcinol (drug)]] 5 µM |  | **0.813×** | -3.5 | 0.096 | 3/34 (NCI-H1792, SW48, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.755× | -3.3 | 0.12 | 10/34 (RKO, SW48, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 0.760× | -3.3 | 0.12 | 2/34 (SW480, NCI-H23) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | 0.761× | -3.1 | 0.17 | 10/32 (NCI-H23, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.767× | -3.0 | 0.20 | 3/32 (A549, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14607. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 4.22 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +15.3) | [[Bosentan (hydrate) (drug)]] 5 µM 0.143× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 193 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -9.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 2.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.82× (z +9.8) | — |
| [[SW48 (line)]] | wt | 10.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0730× (z -8.7) |
| [[SW480 (line)]] | alt | 7.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +11.5) | — |
| [[A-172 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.999 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14607), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC26]] | +0.71 | +0.55 / +0.66 | both halves | 1e-05 | same gene group |
| [[SIAH2-AS1]] | +0.69 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[SAXO1]] | +0.68 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[SYT16]] | +0.67 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[CASC8]] | +0.67 | +0.59 / +0.64 | both halves | 7e-06 | same gene group |
| [[CIBAR1-DT]] | +0.67 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[NINJ2]] | +0.66 | +0.58 / +0.39 | both halves | 5e-05 |  |
| [[HEATR4]] | +0.63 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[CDK6-AS1]] | +0.63 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[PAXBP1-AS1]] | +0.63 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[UBE2R2-AS1]] | +0.63 | +0.35 / +0.60 | both halves | 1e-04 |  |
| [[LINC02268]] | +0.62 | +0.45 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALAD]] | -0.64 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[CEP57L1]] | -0.57 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[TTC38]] | -0.57 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[GPATCH11]] | -0.57 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[PARP2]] | -0.56 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[HPF1]] | -0.56 | -0.31 / -0.32 | both halves | 2e-04 |  |
| [[WRAP73]] | -0.56 | -0.35 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CASC11's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises CASC11's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HPF1]] | B | CASC11 activity lowers HPF1's level | lines that do not express CASC11 (13) vs lines expressing it (37) | 1.36× higher at baseline in the lines without CASC11 | 0.028 | ⚠ within organs, on part of the lines; also absent: ANKRD18A; maybe low, not absent |
| [[EMILIN2]] | B | CASC11 activity lowers EMILIN2's level | lines that do not express CASC11 (13) vs lines expressing it (37) | 1.89× higher at baseline in the lines without CASC11 | 0.089 | ⚠ within organs, on part of the lines; also absent: ANKRD18A; maybe low, not absent |
| [[LINC-PINT]] | B | CASC11 activity raises LINC-PINT's level | lines that do not express CASC11 (13) vs lines expressing it (37) | 1.40× lower at baseline in the lines without CASC11 | 0.093 | ⚠ within organs, on part of the lines; also absent: ANKRD18A; maybe low, not absent |

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.626). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (14.6, 21.3); signed map (28.7, 1.9). **Vector** length 45.1, 6.06% of its response variance represented; |z| ≥ 3 in 749 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +22.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +11.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | -0.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -1.3 | -4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -3.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.1 | -4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.9 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | cancer susceptibility 11 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q24.21 — chr8:127,686,343-127,738,987 (-) |
| Ensembl biotype | lncRNA |
| Also known as | TCONS_00014535, LINC00990, CARLo-7, ENST00000518376, MYMLR |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100270680](https://www.ncbi.nlm.nih.gov/gene/100270680):

> Enables chromatin-protein adaptor activity and promoter-enhancer loop anchoring activity. Involved in chromatin looping and positive regulation of transcription by RNA polymerase II. Is active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:48939](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48939) · Entrez [100270680](https://www.ncbi.nlm.nih.gov/gene/100270680) · Ensembl [ENSG00000249375](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249375)

## Data

Gene col 14607: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14607); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14607, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14607]; `tensor/DDL_lfc|DDL_z.npy` [14607]; `embed/gene_vectors.npy` [14607]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14607 or target_col == 14607). Every well: [[CASC11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASC11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
