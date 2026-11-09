---
symbol: "MYORG"
type: "gene"
col: 9048
ensembl_id: "ENSG00000164976"
name: "myogenesis regulating glycosidase"
location: "9p13.3"
module: 31
arm: "+"
pooled_cpm: 4.21
n_lines_expressing: 48
n_dd_up: 18
n_dd_down: 11
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# MYORG

*myogenesis regulating glycosidase* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.90× (z +10.2, q 7e-22, up in 25 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.422× (z -9.8, q 9e-20, down in 30 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[P2RY2]] (+0.59, fdr 2e-05), [[PCDH1]] (+0.56, fdr 3e-05), [[TPPP]] (+0.55, fdr 1e-05); moves opposite to [[PKD2]] (-0.48, fdr 5e-05), [[MEF2C-AS1]] (-0.45, fdr 6e-05), [[GIGYF2]] (-0.44, fdr 4e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PCDH1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9048.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.90×** | +10.2 | 7e-22 | 25/43 (SW480, J82, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.31×** | +9.5 | 6e-19 | 30/44 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.92×** | +7.4 | 2e-11 | 20/42 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +5.9 | 4e-07 | 19/44 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +5.3 | 1e-05 | 11/42 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +5.2 | 2e-05 | 14/44 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.55×** | +5.0 | 6e-05 | 12/42 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +4.9 | 9e-05 | 1/8 (PANC-1) | inconsistent across doses | cell-cycle shift (explains ~6% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.50×** | +4.6 | 3e-04 | 11/43 (SW480, RKO, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.49×** | +4.4 | 7e-04 | 9/25 (HCT15, A549, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +3.8 | 0.007 | 2/12 (HT-29, HS-578T) | inconsistent across doses | cell-cycle shift (explains ~9% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.39×** | +3.8 | 0.008 | 7/39 (A-172, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.39×** | +3.7 | 0.008 | 5/44 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.011 | 9/38 (H4, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.027 | 7/35 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.038 | 3/44 (HepG2/C3A, A-427, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9048.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.422×** | -9.8 | 9e-20 | 30/44 (HCT15, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.454×** | -8.6 | 2e-15 | 23/39 (Hs 766T, A-427, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.476×** | -8.4 | 9e-15 | 21/29 (BT-474, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.536×** | -7.1 | 2e-10 | 23/41 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.537×** | -7.0 | 2e-10 | 22/42 (BT-474, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.409×** | -5.3 | 1e-05 | 15/37 (SW480, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.485×** | -4.3 | 0.001 | 12/31 (BT-474, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.711×** | -3.9 | 0.007 | 13/44 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **0.713×** | -3.8 | 0.007 | 10/25 (LoVo, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.713×** | -3.8 | 0.007 | 13/43 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.713×** | -3.8 | 0.007 | 13/32 (AsPC-1, KATO III, …) | inconsistent across doses |  |
| [[Resveratrol (drug)]] 5 µM |  | 0.827× | -3.0 | 0.11 | 8/43 (SHP-77, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9048. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 6.74 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0320× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 4.56 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0520× (z -10.1) ⚠ cell-cycle shift, explains ~45% of this change |
| [[BT-474 (line)]] | alt | 13.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0781× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 4.01 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0671× (z -9.9) |
| [[Hs 766T (line)]] | wt | 7.11 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0990× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change |
| [[J82 (line)]] | alt | 4.08 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.109× (z -8.6) ⚠ toxic; unreliable plate only |
| [[LoVo (line)]] | wt | 6.28 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.168× (z -8.9) |
| [[A-172 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.887 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.602 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9048), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[P2RY2]] | +0.59 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[PCDH1]] | +0.56 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[TPPP]] | +0.55 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[B3GNT2]] | +0.54 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[MMP15]] | +0.53 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[BCKDK]] | +0.53 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[SEMA4G]] | +0.53 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[ACTB]] | +0.53 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[CACNB1]] | +0.52 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[EPHA1]] | +0.52 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[EPPK1]] | +0.52 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[CAPG]] | +0.51 | +0.32 / +0.49 | both halves | 2e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKD2]] | -0.48 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[MEF2C-AS1]] | -0.45 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[GIGYF2]] | -0.44 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[BMS1P4-1]] | -0.44 | -0.29 / -0.42 | both halves | 2e-04 |  |
| [[YBEY]] | -0.44 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[UBN2]] | -0.44 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[CEP57]] | -0.43 | -0.24 / -0.49 | both halves | 4e-04 |  |
| [[ASH1L]] | -0.43 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[HSCB]] | -0.42 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[ZNF785]] | -0.42 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[ZNF862]] | -0.42 | -0.28 / -0.39 | both halves | 3e-04 |  |
| [[C2orf42]] | -0.42 | -0.42 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDH1]] | B | PCDH1 activity raises MYORG's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 1.64× lower at baseline in the lines without PCDH1 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[EPPK1]] | B | EPPK1 activity raises MYORG's level | lines that do not express EPPK1 (25) vs lines expressing it (25) | 1.49× lower at baseline in the lines without EPPK1 | 0.037 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3 |
| [[CRYBG2]] | B | CRYBG2 activity raises MYORG's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 1.54× lower at baseline in the lines without CRYBG2 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[P2RY2]] | B | P2RY2 activity raises MYORG's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 1.51× lower at baseline in the lines without P2RY2 | 0.043 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[FGFR4]] | B | FGFR4 activity raises MYORG's level | lines that do not express FGFR4 (11) vs lines expressing it (39) | 1.50× lower at baseline in the lines without FGFR4 | 0.075 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, PATJ, LLGL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.488). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.9, 30.7); signed map (-15.9, 39.2). **Vector** length 60.9, 8.44% of its response variance represented; |z| ≥ 3 in 1,253 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.9 | +10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +4.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.0 | +3.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +2.7 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +3.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +5.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.2 | +1.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.1 | -7.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -7.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.7 | -9.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.5 | -8.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -0.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.5 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.1 | -0.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.1 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | myogenesis regulating glycosidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:34,366,666-34,376,898 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NET37; previously KIAA1161 |
| Gene groups (HGNC) | Glycoside hydrolase family 31 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NSJ0](https://www.uniprot.org/uniprotkb/Q6NSJ0) (Alpha-galactosidase MYORG):

> Alpha-galactosidase with unusual specificity for the Gal-alpha1,4-Glc structure, whose in vivo substrate is still unknown. Promotes myogenesis by activating AKT signaling through the maturation and secretion of IGF2 (By similarity).

**Summary**, from NCBI Gene [57462](https://www.ncbi.nlm.nih.gov/gene/57462):

> Enables alpha-galactosidase activity. Involved in skeletal muscle fiber development. Located in endoplasmic reticulum membrane. Implicated in basal ganglia calcification. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19918](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19918) · Entrez [57462](https://www.ncbi.nlm.nih.gov/gene/57462) · UniProt [Q6NSJ0](https://www.uniprot.org/uniprotkb/Q6NSJ0) · Ensembl [ENSG00000164976](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164976)

## Data

Gene col 9048: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9048); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9048, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9048]; `tensor/DDL_lfc|DDL_z.npy` [9048]; `embed/gene_vectors.npy` [9048]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9048 or target_col == 9048). Every well: [[MYORG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYORG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
