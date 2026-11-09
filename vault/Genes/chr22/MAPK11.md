---
symbol: "MAPK11"
type: "gene"
col: 11671
ensembl_id: "ENSG00000185386"
name: "mitogen-activated protein kinase 11"
location: "22q13.33"
module: 2
arm: "+"
pooled_cpm: 2.52
n_lines_expressing: 47
n_dd_up: 7
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 7
direction_downstream: 3
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# MAPK11

*mitogen-activated protein kinase 11* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.08× (z +10.1, q 3e-21, up in 2 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.39× (z +4.3, q 0.002, up in 10 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.590× (z -7.0, q 1e-09, down in 17 of 30 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PITPNM1]] (+0.68, fdr 1e-05), [[BCAM]] (+0.64, fdr 1e-05), [[MAPK12]] (+0.64, fdr 1e-05, ⚠ same locus), [[RHPN1]] (+0.64, fdr 1e-05); moves opposite to [[GTF2IRD2B]] (-0.51, fdr 6e-05), [[YARS2]] (-0.49, fdr 7e-05), [[PDSS2]] (-0.48, fdr 4e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[VSIR]] → it (grade B ⚠); 3 go from it, the strongest it → cells under [[Radotinib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11671.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.08×** | +10.1 | 3e-21 | 2/3 (A498, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.33×** | +7.3 | 8e-11 | 1/2 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.37×** | +7.2 | 8e-11 | 5/11 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +4.3 | 0.002 | 10/40 (LS 180, SW480, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.14×** | +3.7 | 0.023 | 1/4 (PANC-1) | top dose only | noisy plate (z scaled) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.094 | 4/28 (hTERT-HPNE, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +3.2 | 0.094 | 8/41 (LS 180, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Saquinavir (drug)]] 0.5 µM |  | 1.41× | +3.1 | 0.13 | 7/28 (SHP-77, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11671.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.590×** | -7.0 | 1e-09 | 17/30 (LOX-IMVI, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.544×** | -5.7 | 3e-06 | 17/37 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.552×** | -5.5 | 6e-06 | 14/28 (LoVo, RKO, …) | two highest doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.605×** | -4.7 | 3e-04 | 12/42 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.720×** | -4.4 | 0.001 | 12/29 (A549, Hs 766T, …) | two highest doses | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.661×** | -3.7 | 0.017 | 12/31 (KATO III, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.698×** | -3.4 | 0.057 | 8/41 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.533× | -3.1 | 0.13 | 6/32 (Hs 766T, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 0.715× | -3.1 | 0.13 | 9/36 (LOX-IMVI, RKO, …) | rises with dose | composition shift; position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.538× | -3.0 | 0.13 | 8/24 (LoVo, KATO III, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11671. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 4.37 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0823× (z -9.5) |
| [[KATO III (line)]] | alt | 2.38 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -8.9) |
| [[LoVo (line)]] | wt | 2.94 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0617× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 3.95 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -9.8) |
| [[SW1417 (line)]] | alt | 3.07 | 0 | 1 | — | [[AZD-7648 (drug)]] 0.05 µM 0.0382× (z -10.1) |
| [[A-172 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.636 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.751 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.822 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.687 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.994 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.745 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.442 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11671), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PITPNM1]] | +0.68 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[BCAM]] | +0.64 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[MAPK12]] | +0.64 | +0.72 / +0.57 | both halves | 1e-05 | same gene group; pathway: Activation of PPARGC1A (PGC-1alpha) by phosphorylation; STRING 856; ⚠ same locus (2.0 kb, same strand: neighbours can correlate without regulation) |
| [[RHPN1]] | +0.64 | +0.62 / +0.50 | both halves | 1e-05 | pathway: RHO GTPase Effectors |
| [[TCIRG1]] | +0.63 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[SEMA3F]] | +0.60 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[SH3GLB2]] | +0.60 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[ADAMTSL5]] | +0.59 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[PLCB3]] | +0.58 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[PGGHG]] | +0.58 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[KLHL17]] | +0.58 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[GDPD5]] | +0.58 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[LLGL1]] | +0.58 | +0.59 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2IRD2B]] | -0.51 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[YARS2]] | -0.49 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[PDSS2]] | -0.48 | -0.25 / -0.48 | both halves | 4e-04 |  |
| [[CNPY2]] | -0.48 | -0.44 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VSIR]] | B | VSIR activity lowers MAPK11's level | lines that do not express VSIR (14) vs lines expressing it (36) | 1.53× higher at baseline in the lines without VSIR | 0.006 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |
| [[IGSF9]] | B | IGSF9 activity lowers MAPK11's level | lines that do not express IGSF9 (16) vs lines expressing it (34) | 1.25× higher at baseline in the lines without IGSF9 | 0.048 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| [[GNAZ]] | B | GNAZ activity raises MAPK11's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.27× lower at baseline in the lines without GNAZ | 0.054 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers MAPK11's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[ADGRB2]] | B | ADGRB2 activity raises MAPK11's level | lines that do not express ADGRB2 (7) vs lines expressing it (43) | 1.55× lower at baseline in the lines without ADGRB2 | 0.074 | ⚠ within organs, on part of the lines; also absent: IRX5, CAMKK1, CNTNAP1 |
| [[SH3BP2]] | B | SH3BP2 activity lowers MAPK11's level | lines that do not express SH3BP2 (8) vs lines expressing it (42) | 1.40× higher at baseline in the lines without SH3BP2 | 0.090 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SDC3]] | C | SDC3 activity raises MAPK11's level | lines that do not express SDC3 (4) vs lines expressing it (46) | 1.87× lower at baseline in the lines without SDC3 | 0.089 | ⚠ few lines (4 vs 46); across organs |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Radotinib (drug)]] 5 µM | C | MAPK11 activity raises the cells' numbers under Radotinib 5 µM (protects the cells) | lines that do not express MAPK11 (3) vs lines expressing it (45) | the lines without MAPK11: 0.82× the cells of the other lines | 0.046 | ⚠ few lines (3 vs 47); across organs; also absent: ADCY7, DBN1, LAMC1; maybe low, not absent |
| [[LAMA5]] | C | MAPK11 activity raises LAMA5's level | lines that do not express MAPK11 (3) vs lines expressing it (47) | 5.80× lower at baseline in the lines without MAPK11 | 0.047 | ⚠ few lines (3 vs 47); across organs; also absent: ADCY7, DBN1, LAMC1; maybe low, not absent |
| [[PLEC]] | C | MAPK11 activity raises PLEC's level | lines that do not express MAPK11 (3) vs lines expressing it (47) | 2.82× lower at baseline in the lines without MAPK11 | 0.0995 | ⚠ few lines (3 vs 47); across organs; also absent: ADCY7, DBN1, LAMC1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.637). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (11.5, -5.1); signed map (-10.3, 29.2). **Vector** length 43.4, 5.09% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.3 | +1.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.2 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.3 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -5.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -1.4 | -3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.4 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.5 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.2 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:50,263,713-50,270,767 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p38-2, p38Beta, SAPK2; previously PRKM11 |
| Gene groups (HGNC) | Mitogen-activated protein kinase 11-14 (p38) family |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 59 pathways, smallest: Activation of PPARGC1A (PGC-1alpha) by phosphorylation; Activation of the AP-1 family of transcription factors; p38MAPK events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15759](https://www.uniprot.org/uniprotkb/Q15759) (Mitogen-activated protein kinase 11):

> Serine/threonine kinase which acts as an essential component of the MAP kinase signal transduction pathway. MAPK11 is one of the four p38 MAPKs which play an important role in the cascades of cellular responses evoked by extracellular stimuli such as pro-inflammatory cytokines or physical stress leading to direct activation of transcription factors. Accordingly, p38 MAPKs phosphorylate a broad range of proteins and it has been estimated that they may have approximately 200 to 300 substrates …

**Summary**, from NCBI Gene [5600](https://www.ncbi.nlm.nih.gov/gene/5600):

> This gene encodes a member of a family of protein kinases that are involved in the integration of biochemical signals for a wide variety of cellular processes, including cell proliferation, differentiation, transcriptional regulation, and development. The encoded protein can be activated by proinflammatory cytokines and environmental stresses through phosphorylation by mitogen activated protein kinase kinases (MKKs). Alternative splicing results in multiple transcript variants. [provided by …

**Accessions** — [HGNC:6873](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6873) · Entrez [5600](https://www.ncbi.nlm.nih.gov/gene/5600) · UniProt [Q15759](https://www.uniprot.org/uniprotkb/Q15759) · Ensembl [ENSG00000185386](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185386)

## Data

Gene col 11671: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11671); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11671, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11671]; `tensor/DDL_lfc|DDL_z.npy` [11671]; `embed/gene_vectors.npy` [11671]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11671 or target_col == 11671). Every well: [[MAPK11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPK11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
