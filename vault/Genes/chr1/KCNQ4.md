---
symbol: "KCNQ4"
type: "gene"
col: 3867
ensembl_id: "ENSG00000117013"
name: "potassium voltage-gated channel subfamily Q member 4"
location: "1p34.2"
module: 181
arm: "+"
pooled_cpm: 4.3
n_lines_expressing: 43
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 8
direction_downstream: 3
tags: ["gene", "module/181"]
generated_by: "tahoemap"
---

# KCNQ4

*potassium voltage-gated channel subfamily Q member 4* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.14× (z +12.7, q 5e-34, up in 17 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.552× (z -7.1, q 1e-09, down in 21 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NKAIN1]] (+0.68, fdr 1e-05), [[IL34]] (+0.63, fdr 9e-06), [[MTNR1A]] (+0.63, fdr 1e-05); moves opposite to [[PDZD11]] (-0.56, fdr 9e-05), [[ATP6AP2]] (-0.50, fdr 6e-05), [[C6orf89]] (-0.49, fdr 6e-05).
> It is in [[Module 181]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[IKZF3]] → it (grade B ⚠); 3 go from it, the strongest it → [[SIM2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3867.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.14×** | +12.7 | 5e-34 | 17/30 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +8.0 | 4e-13 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.71×** | +6.3 | 7e-08 | 11/31 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +6.2 | 7e-08 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.007 | 7/30 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.91×** | +4.0 | 0.007 | 1/6 (MIA PaCa-2) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.37×** | +3.7 | 0.020 | 1/17 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.6 | 0.023 | 4/20 (NCI-H460, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.027 | 12/36 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +3.5 | 0.027 | 2/10 (PANC-1, MIA PaCa-2) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.23×** | +3.4 | 0.030 | 4/38 (Panc 03.27, J82, …) | rises with dose | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **1.74×** | +3.4 | 0.030 | 2/24 (Panc 03.27, NCI-H460) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3867.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.552×** | -7.1 | 1e-09 | 21/38 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.586×** | -6.4 | 6e-08 | 22/36 (MIA PaCa-2, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.612×** | -5.8 | 1e-06 | 20/39 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.679×** | -4.6 | 6e-04 | 10/39 (Panc 03.27, RKO, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.694×** | -4.4 | 0.002 | 6/38 (RKO, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | **0.779×** | -4.2 | 0.002 | 9/36 (SK-MEL-2, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.736×** | -3.6 | 0.021 | 15/39 (NCI-H23, NCI-H1573, …) | top dose only | composition shift |
| [[Berbamine (drug)]] 5 µM |  | **0.826×** | -3.2 | 0.083 | 3/39 (J82, RKO, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.597×** | -3.2 | 0.084 | 6/28 (BT-474, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.832× | -3.1 | 0.10 | 4/39 (SW1417, Panc 03.27, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.759× | -3.0 | 0.12 | 5/38 (C32, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3867. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 24.3 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0777× (z -16.3) |
| [[RKO (line)]] | wt | 23.9 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -13.0) |
| [[Panc 03.27 (line)]] | alt | 18.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0996× (z -12.9) |
| [[HEC-1-A (line)]] | alt | 5.56 | 0 | 1 | — | [[Finasteride (drug)]] 0.05 µM 0.0861× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 4.95 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.103× (z -8.6) ⚠ cell-cycle shift, explains ~69% of this change |
| [[PANC-1 (line)]] | alt | 5.23 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 7.24× (z +9.7) | — |
| [[SW48 (line)]] | wt | 14.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0219× (z -13.6) |
| [[A-172 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.787 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.965 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.864 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.960 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.877 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.796 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3867), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NKAIN1]] | +0.68 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[IL34]] | +0.63 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[MTNR1A]] | +0.63 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[TGIF2-RAB5IF]] | +0.62 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[NANOS3]] | +0.61 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[SCARF1]] | +0.60 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[PCSK6]] | +0.59 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[KIF17]] | +0.59 | +0.62 / +0.51 | both halves | 1e-05 | pathway: Neuronal System |
| [[PALD1]] | +0.59 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[ARHGAP40]] | +0.58 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[ADAP1]] | +0.57 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[EFNA2]] | +0.57 | +0.58 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDZD11]] | -0.56 | -0.59 / -0.37 | both halves | 9e-05 |  |
| [[ATP6AP2]] | -0.50 | -0.59 / -0.38 | both halves | 6e-05 |  |
| [[C6orf89]] | -0.49 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[GMPR2]] | -0.48 | -0.54 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IKZF3]] | B | IKZF3 activity raises KCNQ4's level | lines that do not express IKZF3 (31) vs lines expressing it (19) | 1.82× lower at baseline in the lines without IKZF3 | 0.010 | ⚠ within organs, on part of the lines; also absent: SLC34A2, ENSG00000244468, ENSG00000255026; maybe low, not absent |
| [[MTNR1A]] | B | MTNR1A activity strengthens KCNQ4's drug response | lines that do not express MTNR1A (5) vs lines expressing it (34) | the lines without MTNR1A respond 0.57× as strongly (z diff +0.60); strongest at Homoharringtonine 5 µM: 0.31x vs 1.94x (z diff +11.5) | 0.010 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[MSI1]] | B | MSI1 activity raises KCNQ4's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 1.69× lower at baseline in the lines without MSI1 | 0.030 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[EFNA2]] | B | EFNA2 activity raises KCNQ4's level | lines that do not express EFNA2 (8) vs lines expressing it (42) | 1.94× lower at baseline in the lines without EFNA2 | 0.059 | ⚠ within organs, on part of the lines; also absent: TFR2, USP43, BTG3-AS1; maybe low, not absent |
| [[ADRA2C]] | B | ADRA2C activity raises KCNQ4's level | lines that do not express ADRA2C (19) vs lines expressing it (31) | 1.53× lower at baseline in the lines without ADRA2C | 0.075 | ⚠ within organs, on part of the lines; also absent: LRRC4B, CHD5, IGSF9B |
| [[BTBD16]] | B | BTBD16 activity lowers KCNQ4's level | lines that do not express BTBD16 (11) vs lines expressing it (39) | 1.11× higher at baseline in the lines without BTBD16 | 0.092 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[KCNK5]] | B | KCNK5 activity raises KCNQ4's level | lines that do not express KCNK5 (22) vs lines expressing it (28) | 1.92× lower at baseline in the lines without KCNK5 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, SPINT2 |
| [[HDAC6]] | B | HDAC6 activity raises KCNQ4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIM2]] | B | KCNQ4 activity raises SIM2's level | lines that do not express KCNQ4 (7) vs lines expressing it (43) | 2.16× lower at baseline in the lines without KCNQ4 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000248993; maybe low, not absent; its own permutation p |
| [[PPIEL-1]] | B | KCNQ4 activity raises PPIEL-1's level | lines that do not express KCNQ4 (7) vs lines expressing it (43) | 1.65× lower at baseline in the lines without KCNQ4 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000248993; maybe low, not absent; its own permutation p |
| [[PPIEL]] | B | KCNQ4 activity raises PPIEL's level | lines that do not express KCNQ4 (7) vs lines expressing it (43) | 1.62× lower at baseline in the lines without KCNQ4 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000248993; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 181]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.628). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.6, -7.1); signed map (23.4, 6.7). **Vector** length 60.3, 9.76% of its response variance represented; |z| ≥ 3 in 848 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.9 | +12.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.7 | +6.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.7 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -4.6 |
|  | [[NG25 (drug)]] 5 µM |  | -1.8 | -3.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -3.0 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel subfamily Q member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:40,783,787-40,840,452 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Kv7.4; previously DFNA2 |
| Gene groups (HGNC) | Potassium voltage-gated channels |
| Reactome | 7 pathways, smallest: Voltage gated Potassium channels; Sensory processing of sound by outer hair cells of the cochlea; Potassium Channels |
| Matched by | ensembl_id |

**Function**, from UniProt [P56696](https://www.uniprot.org/uniprotkb/P56696) (Potassium voltage-gated channel subfamily KQT member 4):

> Pore-forming subunit of the voltage-gated potassium (Kv) channel involved in the regulation of sensory cells excitability in the cochlea. KCNQ4/Kv7.4 channel is composed of 4 pore-forming subunits assembled as tetramers. Promotes the outflow of potassium ions in the repolarization phase of action potential which plays a role in regulating membrane potential of excitable cells. The channel conducts a slowly activating and deactivating current. Current often shows some inward rectification at …

**Summary**, from NCBI Gene [9132](https://www.ncbi.nlm.nih.gov/gene/9132):

> The protein encoded by this gene forms a potassium channel that is thought to play a critical role in the regulation of neuronal excitability, particularly in sensory cells of the cochlea. The current generated by this channel is inhibited by M1 muscarinic acetylcholine receptors and activated by retigabine, a novel anti-convulsant drug. The encoded protein can form a homomultimeric potassium channel or possibly a heteromultimeric channel in association with the protein encoded by the KCNQ3 …

**Accessions** — [HGNC:6298](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6298) · Entrez [9132](https://www.ncbi.nlm.nih.gov/gene/9132) · UniProt [P56696](https://www.uniprot.org/uniprotkb/P56696) · Ensembl [ENSG00000117013](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117013)

## Data

Gene col 3867: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3867); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3867, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3867]; `tensor/DDL_lfc|DDL_z.npy` [3867]; `embed/gene_vectors.npy` [3867]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3867 or target_col == 3867). Every well: [[KCNQ4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNQ4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
