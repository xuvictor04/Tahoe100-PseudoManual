---
symbol: "SH3BP1"
type: "gene"
col: 1863
ensembl_id: "ENSG00000100092"
name: "SH3 domain binding protein 1"
location: "22q13.1"
module: 161
arm: "+"
pooled_cpm: 8.51
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# SH3BP1

*SH3 domain binding protein 1* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.54× (z +5.6, q 1e-05, up in 7 of 16 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.48× (z +5.3, q 3e-05, up in 16 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.539× (z -8.0, q 5e-13, down in 24 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SIPA1]] (+0.58, fdr 2e-05), [[PPP4C]] (+0.58, fdr 1e-05), [[SEMA3F]] (+0.57, fdr 1e-05); moves opposite to [[RNF115]] (-0.59, fdr 1e-05), [[WAC-AS1]] (-0.55, fdr 3e-05), [[TCEAL4]] (-0.55, fdr 4e-05).
> It is in [[Module 161]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC00659]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1863.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.54×** | +5.6 | 1e-05 | 7/16 (KATO III, RPMI-7951, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +5.3 | 3e-05 | 16/42 (CFPAC-1, LS 180, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.46×** | +5.1 | 7e-05 | 12/29 (LoVo, LOX-IMVI, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +4.3 | 0.003 | 11/46 (PANC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.029 | 13/44 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.29×** | +3.4 | 0.058 | 8/35 (LoVo, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.29×** | +3.4 | 0.058 | 14/45 (CFPAC-1, NCI-H460, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.25× | +3.0 | 0.19 | 5/43 (RPMI-7951, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1863.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.539×** | -8.0 | 5e-13 | 24/44 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.632×** | -6.2 | 1e-07 | 23/41 (RKO, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.663×** | -5.6 | 5e-06 | 19/43 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.750×** | -5.5 | 5e-06 | 21/41 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.483×** | -5.2 | 3e-05 | 20/45 (Panc 03.27, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.685×** | -5.1 | 3e-05 | 20/45 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.708×** | -4.7 | 2e-04 | 17/44 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.735×** | -4.2 | 0.002 | 18/46 (COLO 205, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.723×** | -4.1 | 0.003 | 9/47 (RPMI-7951, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~13% here); noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.742×** | -4.1 | 0.003 | 16/44 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.827×** | -3.6 | 0.014 | 13/42 (COLO 205, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.608×** | -3.5 | 0.021 | 13/42 (RKO, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.775×** | -3.5 | 0.023 | 13/43 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.769×** | -3.4 | 0.024 | 8/44 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.841× | -3.0 | 0.092 | 8/45 (HEC-1-A, SK-MEL-2, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **0.656×** | -3.0 | 0.097 | 6/44 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1863. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 21.0 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 19.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -10.7) |
| [[KATO III (line)]] | alt | 13.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -14.9) |
| [[LS 180 (line)]] | wt | 19.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -11.0) |
| [[HCT15 (line)]] | alt | 12.9 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.107× (z -8.8) ⚠ toxic · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.123× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 7.81 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0751× (z -11.3) |
| [[RKO (line)]] | wt | 17.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0816× (z -13.6) |
| [[SW480 (line)]] | alt | 14.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.219× (z -10.5) |
| [[HT-29 (line)]] | alt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -12.2) |
| [[NCI-H1573 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.194× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 9.72 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.114× (z -9.1) ⚠ toxic |
| [[SW1417 (line)]] | alt | 11.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -9.5) |
| [[SW48 (line)]] | wt | 13.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0959× (z -9.4) |
| [[A-172 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1863), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIPA1]] | +0.58 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[PPP4C]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[SEMA3F]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[MYRF]] | +0.57 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[MFNG]] | +0.56 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[NXPH4]] | +0.55 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[ARHGEF16]] | +0.55 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[CADM4]] | +0.55 | +0.54 / +0.38 | both halves | 7e-05 |  |
| [[RAPGEF3]] | +0.54 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[MPZL2]] | +0.54 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[GDPGP1]] | +0.54 | +0.51 / +0.39 | both halves | 6e-05 |  |
| [[PLEKHO2]] | +0.54 | +0.45 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF115]] | -0.59 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[WAC-AS1]] | -0.55 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[TCEAL4]] | -0.55 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[POLR3C]] | -0.53 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[C11orf58]] | -0.51 | -0.43 / -0.43 | both halves | 4e-05 |  |
| [[ZFX]] | -0.50 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[PPP2R3C]] | -0.50 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[ERCC6L2-AS1]] | -0.49 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[TLK2]] | -0.49 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[ANKRD49]] | -0.49 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[HEXIM2-AS1]] | -0.49 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[WASHC3]] | -0.49 | -0.39 / -0.51 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00659]] | B | LINC00659 activity raises SH3BP1's level | lines that do not express LINC00659 (26) vs lines expressing it (24) | 1.63× lower at baseline in the lines without LINC00659 | 0.030 | ⚠ within organs, on part of the lines; also absent: KLK6, TRIM15, ENSG00000225680 |
| [[HDAC6]] | B | HDAC6 activity lowers SH3BP1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MCF2L]] | B | MCF2L activity strengthens SH3BP1's drug response | lines that do not express MCF2L (14) vs lines expressing it (32) | the lines without MCF2L respond 0.56× as strongly (z diff +1.30); strongest at Homoharringtonine 5 µM: 0.97x vs 0.58x (z diff +4.0) | 0.099 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.534). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (1.2, 31.8); signed map (-14.9, 35.5). **Vector** length 76.6, 13.7% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +4.3 | +5.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.7 | +5.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.2 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +3.1 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +1.6 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +1.4 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +0.4 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.3 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -6.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.9 | -4.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.8 | -8.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -3.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | SH3 domain binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:37,634,654-37,656,117 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARHGAP43 |
| Gene groups (HGNC) | N-BAR domain containing; AH/BAR family Rho GTPase activating proteins |
| Reactome | 4 pathways, smallest: RAC1 GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3L3](https://www.uniprot.org/uniprotkb/Q9Y3L3) (SH3 domain-binding protein 1):

> GTPase activating protein (GAP) which specifically converts GTP-bound Rho-type GTPases including RAC1 and CDC42 in their inactive GDP-bound form. By specifically inactivating RAC1 at the leading edge of migrating cells, it regulates the spatiotemporal organization of cell protrusions which is important for proper cell migration. Also negatively regulates CDC42 in the process of actin remodeling and the formation of epithelial cell junctions. Through its GAP activity toward RAC1 and/or CDC42 …

**Summary**, from NCBI Gene [23616](https://www.ncbi.nlm.nih.gov/gene/23616):

> This gene encodes a member of the Rho GTPase activating protein (RhoGAP) family. The encoded protein regulates Rac signaling and plays a role in cytoskeletal dynamics, cell motility and epithelial junction formation. This protein's association with the exocyst complex, which tethers secretory vesicles to the plasma membrane, has been demonstrated to be important in cell motility. In a distinct complex, this protein has been shown to regulate epithelial junction formation and morphogenesis. By …

**Accessions** — [HGNC:10824](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10824) · Entrez [23616](https://www.ncbi.nlm.nih.gov/gene/23616) · UniProt [Q9Y3L3](https://www.uniprot.org/uniprotkb/Q9Y3L3) · Ensembl [ENSG00000100092](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100092)

## Data

Gene col 1863: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1863); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1863, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1863]; `tensor/DDL_lfc|DDL_z.npy` [1863]; `embed/gene_vectors.npy` [1863]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1863 or target_col == 1863). Every well: [[SH3BP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH3BP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
