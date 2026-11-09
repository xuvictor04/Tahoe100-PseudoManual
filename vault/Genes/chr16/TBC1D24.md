---
symbol: "TBC1D24"
type: "gene"
col: 8474
ensembl_id: "ENSG00000162065"
name: "TBC1 domain family member 24"
location: "16p13.3"
module: 2
arm: "+"
pooled_cpm: 9.66
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# TBC1D24

*TBC1 domain family member 24* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.70× (z +20.3, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.440× (z -18.1, q 0e+00, down in 39 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STIMATE]] (+0.76, fdr 7e-06), [[LRRC20]] (+0.72, fdr 7e-06), [[TRABD]] (+0.69, fdr 2e-05); moves opposite to [[ANGPT2]] (-0.71, fdr 3e-05), [[FAM200A]] (-0.69, fdr 1e-05), [[HELQ]] (-0.69, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[KMO]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8474.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.70×** | +20.3 | 0e+00 | 47/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.90×** | +16.5 | 0e+00 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.52×** | +14.4 | 2e-44 | 45/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +7.6 | 3e-12 | 33/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.39×** | +7.1 | 1e-10 | 22/44 (A549, SW480, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.16×** | +6.2 | 4e-08 | 21/48 (PANC-1, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +4.9 | 6e-05 | 15/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +4.9 | 8e-05 | 18/45 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **1.39×** | +4.8 | 1e-04 | 8/25 (SNU-423, PANC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.27×** | +3.7 | 0.012 | 11/37 (SNU-423, CFPAC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.29×** | +3.5 | 0.022 | 6/21 (SNU-423, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~70% of this change | **1.25×** | +3.1 | 0.083 | 4/39 (NCI-H1792, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8474.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.440×** | -18.1 | 0e+00 | 39/45 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.454×** | -11.0 | 9e-26 | 31/47 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.533×** | -9.8 | 3e-20 | 27/45 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.586×** | -8.3 | 1e-14 | 24/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.422×** | -7.0 | 3e-10 | 21/47 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.680×** | -6.0 | 2e-07 | 22/46 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.693×** | -5.7 | 9e-07 | 21/45 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.502×** | -5.6 | 2e-06 | 20/43 (LoVo, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.702×** | -5.5 | 2e-06 | 18/46 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.784×** | -3.8 | 0.009 | 14/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.798×** | -3.5 | 0.022 | 4/47 (HepG2/C3A, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8474. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 9.46 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -10.6) |
| [[SW480 (line)]] | alt | 11.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.25× (z +10.9) | — |
| [[A-172 (line)]] | wt | 14.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 7.66 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -13.7) |
| [[PANC-1 (line)]] | alt | 12.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -15.1) |
| [[SNU-423 (line)]] | alt | 7.29 | 0 | 2 (1 ⚠) | — | [[Verteporfin (drug)]] 5 µM 0.0934× (z -9.4) |
| [[A498 (line)]] | wt | 11.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.67× (z +8.9) | — |
| [[A549 (line)]] | wt | 5.45 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.36× (z +10.0) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[C32 (line)]] | wt | 10.4 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0797× (z -12.3) |
| [[HOP62 (line)]] | alt | 6.18 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.92× (z +8.9) | — |
| [[J82 (line)]] | alt | 15.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -12.7) |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -9.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 9.21 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 5.36 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 6.99 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.124× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.147× (z -9.8) ⚠ toxic |
| [[RKO (line)]] | wt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -10.3) |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0650× (z -9.9) |
| [[SW1417 (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -11.2) |
| [[SW48 (line)]] | wt | 16.0 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.112× (z -8.5) |
| [[A-427 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8474), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STIMATE]] | +0.76 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[LRRC20]] | +0.72 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[TRABD]] | +0.69 | +0.72 / +0.46 | both halves | 2e-05 |  |
| [[PPM1F]] | +0.69 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[PACC1]] | +0.68 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[ZDHHC8]] | +0.68 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[BLTP2]] | +0.68 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[WRNIP1]] | +0.68 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[KATNB1]] | +0.67 | +0.66 / +0.46 | both halves | 3e-05 |  |
| [[GPD1L]] | +0.67 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[GTPBP3]] | +0.67 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[METAP1]] | +0.66 | +0.70 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANGPT2]] | -0.71 | -0.69 / -0.43 | both halves | 3e-05 |  |
| [[FAM200A]] | -0.69 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[HELQ]] | -0.69 | -0.68 / -0.41 | both halves | 4e-05 |  |
| [[ZNF585A]] | -0.68 | -0.69 / -0.45 | both halves | 3e-05 |  |
| [[N4BP2L1]] | -0.68 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[ZNF226]] | -0.68 | -0.63 / -0.46 | both halves | 3e-05 |  |
| [[OFD1]] | -0.67 | -0.70 / -0.54 | both halves | 1e-05 |  |
| [[ZNF764]] | -0.67 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[ANKRD26]] | -0.65 | -0.66 / -0.36 | both halves | 9e-05 |  |
| [[OCIAD1]] | -0.65 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[TCEAL4]] | -0.64 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[CHURC1]] | -0.64 | -0.61 / -0.62 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KMO]] | B | KMO activity lowers TBC1D24's level | lines that do not express KMO (18) vs lines expressing it (32) | 1.46× higher at baseline in the lines without KMO | 0.007 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity lowers TBC1D24's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.35× higher at baseline in the lines without ZNF341-AS1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[GNAZ]] | B | GNAZ activity raises TBC1D24's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.49× lower at baseline in the lines without GNAZ | 0.033 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[CBX2]] | B | CBX2 activity raises TBC1D24's level | lines that do not express CBX2 (6) vs lines expressing it (44) | 1.73× lower at baseline in the lines without CBX2 | 0.034 | ⚠ within organs, on part of the lines; also absent: CCNP, CTXN1, ADGRL1; maybe low, not absent |
| [[LGALS3]] | B | LGALS3 activity lowers TBC1D24's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 1.25× higher at baseline in the lines without LGALS3 | 0.039 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[HDAC6]] | B | HDAC6 activity lowers TBC1D24's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.678). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-6.3, -19.1); signed map (-42.4, -10.6). **Vector** length 66.8, 10.7% of its response variance represented; |z| ≥ 3 in 1,042 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +4.5 | +20.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +16.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.9 | +14.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.1 | +2.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +2.9 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +0.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.5 | +0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +6.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.4 | +0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.4 | -18.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.1 | -11.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.9 | -9.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.1 | -7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | +0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.3 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | +1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.3 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,475,051-2,509,560 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1171, TLDC6, DFNA65; previously DFNB86 |
| Gene groups (HGNC) | TLDc domain containing; TBC1 domain family members |
| Reactome | 4 pathways, smallest: TBC/RABGAPs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULP9](https://www.uniprot.org/uniprotkb/Q9ULP9) (TBC1 domain family member 24):

> May act as a GTPase-activating protein for Rab family protein(s). Involved in neuronal projection development, probably through negative modulation of ARF6 function. Required for the maintenance of postsynaptic neuron dendritic spines in the adult by suppressing ARF6 activity. Involved in the regulation of synaptic vesicle trafficking. Promotes axonal outgrowth and membrane trafficking at the growth cone (By similarity). Positively regulates radial migration and morphological maturation of …

**Summary**, from NCBI Gene [57465](https://www.ncbi.nlm.nih.gov/gene/57465):

> This gene encodes a protein with a conserved domain, referred to as the TBC domain, characteristic of proteins which interact with GTPases. TBC domain proteins may serve as GTPase-activating proteins for a particular group of GTPases, the Rab (Ras-related proteins in brain) small GTPases which are involved in the regulation of membrane trafficking. Mutations in this gene are associated with familial infantile myoclonic epilepsy. Alternative splicing results in multiple transcript variants. …

**Accessions** — [HGNC:29203](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29203) · Entrez [57465](https://www.ncbi.nlm.nih.gov/gene/57465) · UniProt [Q9ULP9](https://www.uniprot.org/uniprotkb/Q9ULP9) · Ensembl [ENSG00000162065](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162065)

## Data

Gene col 8474: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8474); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8474, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8474]; `tensor/DDL_lfc|DDL_z.npy` [8474]; `embed/gene_vectors.npy` [8474]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8474 or target_col == 8474). Every well: [[TBC1D24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
