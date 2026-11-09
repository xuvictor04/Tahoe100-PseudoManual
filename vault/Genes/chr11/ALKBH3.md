---
symbol: "ALKBH3"
type: "gene"
col: 9260
ensembl_id: "ENSG00000166199"
name: "alkB homolog 3, alpha-ketoglutarate dependent dioxygenase"
location: "11p11.2"
module: 89
arm: "+"
pooled_cpm: 19.74
n_lines_expressing: 46
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# ALKBH3

*alkB homolog 3, alpha-ketoglutarate dependent dioxygenase* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.28× (z +8.4, q 2e-14, up in 28 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.532× (z -12.4, q 2e-32, down in 32 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.770× (z -7.2, q 5e-11, down in 29 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS33A]] (+0.73, fdr 7e-06), [[TACO1]] (+0.71, fdr 7e-06), [[POLL]] (+0.71, fdr 7e-06); moves opposite to [[RCOR1]] (-0.57, fdr 1e-05).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF675]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9260.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.28×** | +8.4 | 2e-14 | 28/44 (LoVo, SW480, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.28×** | +6.8 | 3e-09 | 24/44 (RKO, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +6.4 | 3e-08 | 25/44 (LoVo, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.39×** | +6.1 | 2e-07 | 16/42 (LoVo, A-172, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.75×** | +5.7 | 1e-06 | 17/42 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.29×** | +4.7 | 3e-04 | 15/43 (HEC-1-A, A-172, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.7 | 3e-04 | 2/44 (MIA PaCa-2, SW 1271) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.26×** | +4.6 | 3e-04 | 10/44 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.26×** | +4.6 | 3e-04 | 14/42 (Hs 766T, AsPC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +4.4 | 7e-04 | 13/44 (A-172, PANC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.003 | 13/43 (J82, SW1417, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.20×** | +3.6 | 0.016 | 11/43 (J82, HOP62, …) | two highest doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.19× | +3.5 | 0.018 | 3/44 (C32, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.5 | 0.022 | 5/44 (J82, LOX-IMVI, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.20× | +3.4 | 0.028 | 13/42 (NCI-H460, J82, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.12× | +3.2 | 0.050 | 6/44 (SW480, NCI-H1792, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.14× | +2.9 | 0.099 | 8/44 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +2.9 | 0.099 | 4/42 (SNU-423, A549, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 12 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9260.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.532×** | -12.4 | 2e-32 | 32/42 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.611×** | -8.9 | 1e-16 | 20/33 (LoVo, NCI-H460, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.642×** | -8.7 | 7e-16 | 28/44 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.651×** | -7.9 | 4e-13 | 22/41 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.770×** | -7.2 | 5e-11 | 29/44 (SW480, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.699×** | -6.7 | 2e-09 | 22/44 (PANC-1, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.748×** | -5.7 | 1e-06 | 17/44 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.751×** | -5.6 | 1e-06 | 20/44 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.766×** | -5.0 | 4e-05 | 16/42 (PANC-1, SW 900, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.856× | -4.3 | 9e-04 | 18/44 (PANC-1, NCI-H1792, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.803×** | -4.3 | 9e-04 | 20/44 (SW480, NCI-H661, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.822×** | -3.8 | 0.006 | 18/44 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | 0.836× | -3.5 | 0.020 | 16/39 (SHP-77, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.844× | -3.3 | 0.036 | 8/44 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 0.841× | -3.2 | 0.045 | 5/44 (HEC-1-A, SW480, …) | all doses, flat |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | 0.858× | -3.0 | 0.096 | 8/44 (A549, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9260. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 24.1 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.268× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 17.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 35.2 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.243× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.597× (z -8.6) |
| [[LoVo (line)]] | wt | 19.1 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.68× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 25.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 30.3 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -9.7) ⚠ cell-cycle shift, explains ~92% of this change |
| [[H4 (line)]] | wt | 29.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HepG2_C3A (line)]] | wt | 11.9 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.115× (z -8.6) ⚠ toxic; unreliable plate only |
| [[LS 180 (line)]] | wt | 22.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.178× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 6.35 | 0 | 1 | — | [[Macitentan (drug)]] 5 µM 0.0787× (z -8.9) |
| [[A-172 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9260), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS33A]] | +0.73 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[TACO1]] | +0.71 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[POLL]] | +0.71 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[PAAF1]] | +0.69 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[METTL22]] | +0.69 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[POLR3F]] | +0.69 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[ZSCAN25]] | +0.68 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[TMLHE]] | +0.68 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[MRPL1]] | +0.67 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[ALKBH1]] | +0.67 | +0.64 / +0.61 | both halves | 7e-06 | same gene group; STRING 990 |
| [[SART3]] | +0.66 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ZNF777]] | +0.66 | +0.72 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCOR1]] | -0.57 | -0.55 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF675]] | B | ZNF675 activity raises ALKBH3's level | lines that do not express ZNF675 (5) vs lines expressing it (45) | 1.08× lower at baseline in the lines without ZNF675 | 0.034 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF573, ZNF420 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ALKBH3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises ALKBH3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.790). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-44.5, 7.2); signed map (-9.9, -17.0). **Vector** length 80.0, 15.9% of its response variance represented; |z| ≥ 3 in 802 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +7.1 | +6.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.6 | +8.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.5 | +5.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +6.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | +1.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.6 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +1.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -7.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.6 | -6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.5 | -3.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.3 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.1 | -8.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -2.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | alkB homolog 3, alpha-ketoglutarate dependent dioxygenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:43,880,811-43,920,274 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DEPC-1 |
| Gene groups (HGNC) | Alkylation repair homologs |
| Reactome | 4 pathways, smallest: ALKBH3 mediated reversal of alkylation damage; Reversal of alkylation damage by DNA dioxygenases; DNA Damage Reversal |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96Q83](https://www.uniprot.org/uniprotkb/Q96Q83) (Alpha-ketoglutarate-dependent dioxygenase alkB homolog 3):

> Dioxygenase that mediates demethylation of DNA and RNA containing 1-methyladenosine (m1A). Repairs alkylated DNA containing 1-methyladenosine (m1A) and 3-methylcytosine (m3C) by oxidative demethylation. Has a strong preference for single-stranded DNA. Able to process alkylated m3C within double-stranded regions via its interaction with ASCC3, which promotes DNA unwinding to generate single-stranded substrate needed for ALKBH3. Can repair exocyclic 3,N4-ethenocytosine adducs in single-stranded …

**Summary**, from NCBI Gene [221120](https://www.ncbi.nlm.nih.gov/gene/221120):

> The Escherichia coli AlkB protein protects against the cytotoxicity of methylating agents by repair of the specific DNA lesions generated in single-stranded DNA. ALKBH2 (MIM 610602) and ALKBH3 are E. coli AlkB homologs that catalyze the removal of 1-methyladenine and 3-methylcytosine (Duncan et al., 2002 [PubMed 12486230]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:30141](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30141) · Entrez [221120](https://www.ncbi.nlm.nih.gov/gene/221120) · UniProt [Q96Q83](https://www.uniprot.org/uniprotkb/Q96Q83) · Ensembl [ENSG00000166199](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166199)

## Data

Gene col 9260: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9260); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9260, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9260]; `tensor/DDL_lfc|DDL_z.npy` [9260]; `embed/gene_vectors.npy` [9260]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9260 or target_col == 9260). Every well: [[ALKBH3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALKBH3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
