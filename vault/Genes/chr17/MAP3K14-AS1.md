---
symbol: "MAP3K14-AS1"
type: "gene"
col: 15539
ensembl_id: "ENSG00000267278"
name: "MAP3K14 antisense RNA 1"
location: "17q21.31"
module: 15
arm: "+"
pooled_cpm: 5.49
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 17
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# MAP3K14-AS1

*MAP3K14 antisense RNA 1* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.74× (z +9.1, q 4e-17, up in 20 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.435× (z -9.6, q 3e-19, down in 31 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA2-AS1]] (+0.55, fdr 7e-05), [[SCAMP5]] (+0.55, fdr 3e-05), [[METTL21A]] (+0.53, fdr 2e-05); moves opposite to [[DYNC2H1]] (-0.53, fdr 3e-05), [[CEP290]] (-0.48, fdr 1e-04), [[SPIDR]] (-0.48, fdr 2e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15539.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +9.1 | 4e-17 | 20/36 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +7.0 | 6e-10 | 5/8 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.6 | 7e-04 | 11/34 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +4.4 | 0.001 | 13/43 (NCI-H460, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.003 | 12/44 (A-427, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.41×** | +4.0 | 0.006 | 4/21 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.34× | +3.2 | 0.12 | 4/34 (CFPAC-1, A549, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | 1.31× | +3.1 | 0.12 | 4/40 (CFPAC-1, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15539.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.435×** | -9.6 | 3e-19 | 31/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.630×** | -7.6 | 1e-11 | 23/36 (NCI-H1573, NCI-H2347, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.529×** | -7.4 | 3e-11 | 23/42 (HT-29, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.581×** | -6.3 | 5e-08 | 19/34 (NCI-H23, SW48, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.379×** | -5.9 | 5e-07 | 18/34 (A-427, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.604×** | -5.8 | 5e-07 | 21/35 (LS 180, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.611×** | -5.7 | 1e-06 | 19/42 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.615×** | -5.6 | 1e-06 | 17/42 (H4, A-427, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.656×** | -4.6 | 2e-04 | 17/39 (KATO III, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.661×** | -4.6 | 2e-04 | 19/42 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.683×** | -4.4 | 6e-04 | 14/44 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.704×** | -4.1 | 0.002 | 14/43 (PANC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.541×** | -3.7 | 0.009 | 16/40 (SW48, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.737×** | -3.4 | 0.029 | 14/29 (LS 180, PANC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.761×** | -3.2 | 0.060 | 7/45 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Rucaparib (phosphate) (drug)]] 5 µM |  | **0.760×** | -3.0 | 0.082 | 5/45 (SK-MEL-2, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15539. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 13.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -9.4) ⚠ cell-cycle shift, explains ~58% of this change |
| [[HT-29 (line)]] | alt | 5.61 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0747× (z -9.8) |
| [[LS 180 (line)]] | wt | 5.92 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1573 (line)]] | alt | 8.84 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -16.1) ⚠ cell-cycle shift, explains ~58% of this change |
| [[NCI-H2030 (line)]] | alt | 9.64 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -8.6) ⚠ cell-cycle shift, explains ~58% of this change |
| [[NCI-H23 (line)]] | alt | 9.89 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 6.14 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -10.0) ⚠ cell-cycle shift, explains ~58% of this change |
| [[NCI-H460 (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0953× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 6.34 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.209× (z -9.2) |
| [[A-172 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.80 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.727 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15539), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA2-AS1]] | +0.55 | +0.37 / +0.53 | both halves | 7e-05 | same gene group |
| [[SCAMP5]] | +0.55 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[METTL21A]] | +0.53 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[DENND5B-AS1]] | +0.52 | +0.36 / +0.53 | both halves | 1e-04 | same gene group |
| [[DLGAP1-AS2]] | +0.51 | +0.44 / +0.44 | both halves | 3e-05 | same gene group |
| [[SPESP1]] | +0.51 | +0.35 / +0.52 | both halves | 1e-04 |  |
| [[CDC20-DT]] | +0.51 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[DPY19L3-DT]] | +0.50 | +0.39 / +0.41 | both halves | 5e-05 |  |
| [[TP53TG5]] | +0.50 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[ZNF774]] | +0.50 | +0.39 / +0.45 | both halves | 6e-05 |  |
| [[IRGQ]] | +0.48 | +0.34 / +0.45 | both halves | 1e-04 |  |
| [[SMUG1]] | +0.48 | +0.31 / +0.40 | both halves | 2e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYNC2H1]] | -0.53 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[CEP290]] | -0.48 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[SPIDR]] | -0.48 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[NEK1]] | -0.48 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[NUDT12]] | -0.47 | -0.37 / -0.33 | both halves | 1e-04 |  |
| [[SCAPER]] | -0.47 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[FHIT]] | -0.46 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[TNS3]] | -0.45 | -0.32 / -0.56 | both halves | 2e-04 |  |
| [[BABAM2]] | -0.44 | -0.29 / -0.46 | both halves | 2e-04 |  |
| [[SHPRH]] | -0.44 | -0.26 / -0.46 | both halves | 3e-04 |  |
| [[AGTPBP1]] | -0.44 | -0.47 / -0.29 | both halves | 2e-04 |  |
| [[CCDC144BP]] | -0.43 | -0.38 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MAP3K14-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SSPOP]] | B | SSPOP activity raises MAP3K14-AS1's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 1.48× lower at baseline in the lines without SSPOP | 0.027 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2 |
| [[TOP2B]] | B | TOP2B activity lowers MAP3K14-AS1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[TNS3]] | C | TNS3's natural level strengthens MAP3K14-AS1's drug response | TNS3's natural level across 37 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.05; direction not clear | 0.077 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.467). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (9.7, 25.7); signed map (34.3, -0.2). **Vector** length 52.2, 6.90% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.3 | +1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.0 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +0.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.3 | +0.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.3 | -7.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -5.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -1.6 | -4.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.5 | -2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.2 | -0.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.2 | -0.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | MAP3K14 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q21.31 — chr17:45,247,916-45,269,824 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44359](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44359) · Entrez [100133991](https://www.ncbi.nlm.nih.gov/gene/100133991) · Ensembl [ENSG00000267278](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267278)

## Data

Gene col 15539: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15539); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15539, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15539]; `tensor/DDL_lfc|DDL_z.npy` [15539]; `embed/gene_vectors.npy` [15539]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15539 or target_col == 15539). Every well: [[MAP3K14-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP3K14-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
