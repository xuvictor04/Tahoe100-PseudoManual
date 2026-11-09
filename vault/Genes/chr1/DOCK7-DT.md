---
symbol: "DOCK7-DT"
type: "gene"
col: 14026
ensembl_id: "ENSG00000235545"
name: "DOCK7 divergent transcript"
location: "1p31.3"
module: 15
arm: "+"
pooled_cpm: 4.59
n_lines_expressing: 48
n_dd_up: 17
n_dd_down: 12
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# DOCK7-DT

*DOCK7 divergent transcript* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.97× (z +17.7, q 0e+00, up in 32 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.447× (z -13.1, q 2e-36, down in 28 of 39 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.554× (z -6.8, q 2e-09, down in 20 of 44 measured lines).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCL2L2-PABPN1]] (+0.59, fdr 3e-05), [[PPP1R26-AS1]] (+0.57, fdr 5e-05), [[PHC2-AS1]] (+0.57, fdr 5e-05); moves opposite to [[NUP98]] (-0.49, fdr 7e-04), [[WDR70]] (-0.49, fdr 2e-04), [[ECHS1]] (-0.49, fdr 4e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF529-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14026.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.97×** | +17.7 | 0e+00 | 32/37 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.68×** | +11.4 | 2e-27 | 31/40 (RKO, SW480, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.52×** | +6.8 | 2e-09 | 13/43 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.72×** | +6.3 | 6e-08 | 18/44 (A-172, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +4.9 | 1e-04 | 11/41 (HEC-1-A, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.52×** | +4.8 | 1e-04 | 12/41 (NCI-H2030, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.45×** | +4.2 | 0.002 | 8/41 (NCI-H1573, SW1417, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.011 | 3/45 (J82, LoVo, …) | inconsistent across doses | position effect removed |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.40×** | +3.7 | 0.015 | 7/40 (HS-578T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.023 | 5/32 (RKO, A-172, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.35×** | +3.5 | 0.023 | 5/41 (KATO III, CFPAC-1, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.023 | 11/44 (HOP62, H4, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.023 | 8/42 (RPMI-7951, NCI-H1573, …) | all doses, flat |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.32×** | +3.2 | 0.060 | 7/36 (SNU-423, NCI-H2030, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.093 | 4/43 (SW48, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14026.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.447×** | -13.1 | 2e-36 | 28/39 (HEC-1-A, NCI-H460, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.448×** | -8.9 | 2e-16 | 27/42 (C32, NCI-H460, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.554×** | -6.8 | 2e-09 | 20/44 (SK-MEL-2, SW480, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.587×** | -6.1 | 1e-07 | 18/45 (HepG2/C3A, SK-MEL-2, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.628×** | -5.4 | 9e-06 | 17/36 (SK-MEL-2, C32, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.416×** | -5.3 | 1e-05 | 18/40 (MIA PaCa-2, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.640×** | -4.9 | 6e-05 | 15/27 (PANC-1, HS-578T, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.695×** | -4.2 | 0.002 | 14/44 (SK-MEL-2, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.701×** | -4.1 | 0.003 | 13/44 (SW1417, KATO III, …) | inconsistent across doses | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.524×** | -3.9 | 0.006 | 13/34 (SK-MEL-2, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.757×** | -3.2 | 0.066 | 15/42 (C32, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.764×** | -3.1 | 0.088 | 2/45 (NCI-H1792, SW480) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14026. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 15.8 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -12.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SK-MEL-2 (line)]] | alt | 13.0 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -10.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.114× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 8.22 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -12.3) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HEC-1-A (line)]] | alt | 6.69 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -12.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HepG2_C3A (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0976× (z -10.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 5.19 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -9.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[MIA PaCa-2 (line)]] | alt | 6.42 | 0 | 1 | — | [[NG25 (drug)]] 0.05 µM 0.0732× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 4.08 | 0 | 1 | — | [[Sacubitril_Valsartan (drug)]] 0.05 µM 0.0697× (z -9.0) |
| [[PANC-1 (line)]] | alt | 3.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 3.73 | 0 | 1 | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 0.5 µM 0.0592× (z -8.6) |
| [[SW480 (line)]] | alt | 5.20 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.182× (z -9.2) |
| [[A-172 (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.890 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14026), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 18 of them with an alert (⚠; 18 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL2L2-PABPN1]] | +0.59 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[PPP1R26-AS1]] | +0.57 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[PHC2-AS1]] | +0.57 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[PELO-AS1]] | +0.57 | +0.31 / +0.53 | both halves | 2e-04 |  |
| [[ANO7]] | +0.57 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[GLUD1P3]] | +0.56 | +0.37 / +0.54 | both halves | 8e-05 |  |
| [[VPS13B-DT]] | +0.56 | +0.38 / +0.46 | both halves | 6e-05 | same gene group |
| [[ING2-DT]] | +0.55 | +0.48 / +0.40 | both halves | 5e-05 | same gene group |
| [[CTC-338M12.4]] | +0.55 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[DYNLT2]] | +0.55 | +0.28 / +0.52 | both halves | 3e-04 |  |
| [[HPSE2]] | +0.54 | +0.22 / +0.49 | both halves | 6e-04 |  |
| [[GOT1-DT]] | +0.54 | +0.34 / +0.51 | both halves | 1e-04 | same gene group |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP98]] | -0.49 | -0.20 / -0.57 | both halves | 7e-04 |  |
| [[WDR70]] | -0.49 | -0.33 / -0.32 | both halves | 2e-04 |  |
| [[ECHS1]] | -0.49 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[PKN2]] | -0.48 | -0.26 / -0.50 | both halves | 4e-04 |  |
| [[WDR7]] | -0.48 | -0.24 / -0.42 | both halves | 5e-04 |  |
| [[THEM6]] | -0.48 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[MLST8]] | -0.48 | -0.37 / -0.44 | both halves | 7e-05 |  |
| [[THRAP3]] | -0.47 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[ARAF]] | -0.46 | -0.37 / -0.51 | both halves | 9e-05 |  |
| [[SNAPIN]] | -0.45 | -0.43 / -0.25 | both halves | 4e-04 |  |
| [[PABIR1]] | -0.45 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[C2CD5]] | -0.45 | -0.33 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF529-AS1]] | B | ZNF529-AS1 activity raises DOCK7-DT's level | lines that do not express ZNF529-AS1 (8) vs lines expressing it (42) | 1.66× lower at baseline in the lines without ZNF529-AS1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF529, HOMER2 |
| [[ZNF790]] | B | ZNF790 activity raises DOCK7-DT's level | lines that do not express ZNF790 (14) vs lines expressing it (36) | 1.38× lower at baseline in the lines without ZNF790 | 0.069 | ⚠ within organs, on part of the lines; also absent: ZNF345, ZNF606, ZNF569 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.588). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-9.2, 22.2); signed map (17.5, -4.0). **Vector** length 68.7, 11.1% of its response variance represented; |z| ≥ 3 in 1,028 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +17.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.1 | +11.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +3.6 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.4 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +6.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.6 | +3.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.1 | -8.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.7 | -6.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.7 | -6.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -2.2 | -13.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.2 | -0.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -0.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.1 | -0.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.1 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | DOCK7 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p31.3 — chr1:62,688,482-62,710,694 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55670](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55670) · Entrez [121832810](https://www.ncbi.nlm.nih.gov/gene/121832810) · Ensembl [ENSG00000235545](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235545)

## Data

Gene col 14026: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14026); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14026, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14026]; `tensor/DDL_lfc|DDL_z.npy` [14026]; `embed/gene_vectors.npy` [14026]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14026 or target_col == 14026). Every well: [[DOCK7-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DOCK7-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
