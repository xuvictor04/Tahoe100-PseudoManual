---
symbol: "MTMR9LP"
type: "gene"
col: 13301
ensembl_id: "ENSG00000220785"
name: "myotubularin related protein 9 like, pseudogene"
location: "1p35.2"
module: 35
arm: "+"
pooled_cpm: 2.1
n_lines_expressing: 41
n_dd_up: 3
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# MTMR9LP

*myotubularin related protein 9 like, pseudogene* — 1p35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.34× (z +3.7, q 0.054, up in 0 of 35 measured lines) ⚠ cell-cycle shift, explains ~98% of this change. The strongest without an alert is [[Ponatinib (drug)]] 0.5 µM: 1.50× (z +3.7, q 0.054, up in 7 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.448× (z -7.2, q 3e-10, down in 20 of 38 measured lines) ⚠ cell-cycle shift, explains ~57% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.568× (z -5.1, q 3e-05, down in 14 of 35 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IGDCC4]] (+0.57, fdr 4e-05), [[TEKTIP1]] (+0.54, fdr 3e-05), [[RABGEF1P3]] (+0.48, fdr 6e-05); moves opposite to [[SPIDR]] (-0.46, fdr 1e-04), [[MT1A]] (-0.44, fdr 2e-04), [[LDLRAD3]] (-0.44, fdr 1e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[IGDCC4]] → it (grade B ⚠); 2 go from it, the strongest it → [[PTOV1-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13301.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.34×** | +3.7 | 0.054 | 0/35 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.50×** | +3.7 | 0.054 | 7/32 (AsPC-1, CFPAC-1, …) | two highest doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +3.6 | 0.054 | 0/2 | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 1.50× | +3.4 | 0.11 | 2/37 (HEC-1-A, NCI-H23) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.43× | +3.3 | 0.12 | 3/18 (HEC-1-A, PANC-1, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | 1.44× | +3.0 | 0.20 | 0/18 | inconsistent across doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.41× | +3.0 | 0.20 | 6/23 (RPMI-7951, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13301.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.448×** | -7.2 | 3e-10 | 20/38 (SNU-423, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.457×** | -7.0 | 5e-10 | 19/33 (SK-MEL-2, SNU-423, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.469×** | -6.8 | 2e-09 | 21/37 (HT-29, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.478×** | -6.6 | 4e-09 | 20/34 (HT-29, J82, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.480×** | -6.6 | 5e-09 | 17/33 (RKO, SW480, …) | two highest doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.482×** | -6.3 | 3e-08 | 17/32 (KATO III, SK-MEL-2, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.568×** | -5.1 | 3e-05 | 14/35 (LS 180, J82, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.595×** | -4.7 | 2e-04 | 8/36 (AN3 CA, COLO 205, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **0.597×** | -4.6 | 2e-04 | 13/20 (SW480, CFPAC-1, …) | two highest doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.612×** | -4.4 | 6e-04 | 11/30 (HOP62, BT-474, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.623×** | -4.2 | 0.001 | 11/37 (SNU-423, SW480, …) | all doses, stronger at high dose |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.754×** | -3.6 | 0.017 | 9/34 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Terfenadine (drug)]] 0.5 µM |  | **0.687×** | -3.4 | 0.034 | 9/32 (RKO, Hs 766T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.774×** | -3.2 | 0.050 | 12/29 (SK-MEL-2, SNU-423, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.523×** | -3.0 | 0.089 | 8/23 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.65 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13301. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 6.93 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0278× (z -13.3) ⚠ cell-cycle shift, explains ~57% of this change |
| [[HEC-1-A (line)]] | alt | 6.33 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0726× (z -10.7) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 6.10 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0575× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 6.33 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0492× (z -10.2) ⚠ cell-cycle shift, explains ~51% of this change |
| [[SW480 (line)]] | alt | 2.85 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0691× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change |
| [[A-172 (line)]] | wt | 0.473 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.445 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.246 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.931 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.513 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.711 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.850 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.971 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.373 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.681 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.358 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.877 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13301), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGDCC4]] | +0.57 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[TEKTIP1]] | +0.54 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[RABGEF1P3]] | +0.48 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[CCDC73]] | +0.48 | +0.36 / +0.41 | both halves | 9e-05 |  |
| [[FAM13C]] | +0.47 | +0.48 / +0.36 | both halves | 1e-04 |  |
| [[KCP]] | +0.47 | +0.31 / +0.46 | both halves | 2e-04 |  |
| [[ATP6V0D2]] | +0.47 | +0.27 / +0.51 | both halves | 3e-04 |  |
| [[TMEM30A-DT]] | +0.46 | +0.44 / +0.36 | both halves | 1e-04 |  |
| [[MIAT]] | +0.46 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[ARMCX4]] | +0.46 | +0.47 / +0.26 | both halves | 4e-04 |  |
| [[SPATA24]] | +0.46 | +0.31 / +0.45 | both halves | 2e-04 |  |
| [[EIF3J-DT]] | +0.46 | +0.37 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPIDR]] | -0.46 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[MT1A]] | -0.44 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[LDLRAD3]] | -0.44 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[PKP2]] | -0.44 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[MT1E]] | -0.43 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[EFNA5]] | -0.43 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[CCND3]] | -0.43 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[SAA1]] | -0.42 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[ERRFI1]] | -0.42 | -0.32 / -0.35 | both halves | 2e-04 |  |
| [[MT1X]] | -0.42 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[TBC1D8]] | -0.42 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[HS2ST1]] | -0.42 | -0.34 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IGDCC4]] | B | IGDCC4 activity raises MTMR9LP's level | lines that do not express IGDCC4 (18) vs lines expressing it (32) | 1.36× lower at baseline in the lines without IGDCC4 | 0.099 | ⚠ within organs, on part of the lines; also absent: C19orf18, ENSG00000176593, LINC02813; maybe low, not absent |
| [[ARMCX4]] | C | ARMCX4 activity raises MTMR9LP's level | lines that do not express ARMCX4 (18) vs lines expressing it (32) | 1.68× lower at baseline in the lines without ARMCX4 | 0.001 | ⚠ within organs, on part of the lines; also absent: TLR2, LYPD5, GALC; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTOV1-AS1]] | B | MTMR9LP activity lowers PTOV1-AS1's level | lines that do not express MTMR9LP (9) vs lines expressing it (41) | 1.20× higher at baseline in the lines without MTMR9LP | 0.070 | ⚠ within organs, on part of the lines; also absent: SMAD7, TNFRSF21, TNFRSF14; maybe low, not absent |
| [[ARMCX4]] | C | MTMR9LP activity raises ARMCX4's level | lines that do not express MTMR9LP (9) vs lines expressing it (41) | 4.84× lower at baseline in the lines without MTMR9LP | 0.005 | ⚠ within organs, on part of the lines; also absent: SMAD7, TNFRSF21, TNFRSF14; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.445). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (17.2, 22.3); signed map (29.9, 4.0). **Vector** length 39.8, 4.98% of its response variance represented; |z| ≥ 3 in 876 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.2 | +2.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.9 | +1.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | +1.9 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.0 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | +0.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -1.4 | -6.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -1.3 | -6.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -1.2 | -6.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | -1.2 | -4.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -1.8 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.0 | -1.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.0 | -2.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | myotubularin related protein 9 like, pseudogene |
| Locus type | pseudogene |
| Location | 1p35.2 — chr1:32,231,847-32,241,592 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously MTMR9L |
| Gene groups (HGNC) | Unitary pseudogenes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27920](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27920) · Entrez [339483](https://www.ncbi.nlm.nih.gov/gene/339483) · Ensembl [ENSG00000220785](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000220785)

## Data

Gene col 13301: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13301); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13301, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13301]; `tensor/DDL_lfc|DDL_z.npy` [13301]; `embed/gene_vectors.npy` [13301]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13301 or target_col == 13301). Every well: [[MTMR9LP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTMR9LP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
