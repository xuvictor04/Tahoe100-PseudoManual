---
symbol: "IGSF9B"
type: "gene"
col: 1297
ensembl_id: "ENSG00000080854"
name: "immunoglobulin superfamily member 9B"
location: "11q25"
module: 195
arm: "+"
pooled_cpm: 19.48
n_lines_expressing: 33
n_dd_up: 18
n_dd_down: 11
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/195"]
generated_by: "tahoemap"
---

# IGSF9B

*immunoglobulin superfamily member 9B* — 11q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.92× (z +8.4, q 2e-14, up in 17 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.669× (z -5.2, q 6e-05, down in 15 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRR5]] (+0.62, fdr 1e-05), [[CACNA1H]] (+0.62, fdr 1e-05), [[GLI2]] (+0.62, fdr 1e-05); moves opposite to [[ASH1L]] (-0.50, fdr 6e-05), [[C21orf62-AS1]] (-0.50, fdr 2e-04), [[GTF2IRD2B]] (-0.49, fdr 5e-05).
> It is in [[Module 195]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BEGAIN]] → it (grade B ⚠); 2 go from it, the strongest it → [[SLC19A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1297.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.92×** | +8.4 | 2e-14 | 17/31 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +7.9 | 7e-13 | 15/31 (HT-29, LOX-IMVI, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +7.4 | 3e-11 | 17/31 (A549, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.75×** | +7.2 | 9e-11 | 16/31 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +6.8 | 9e-10 | 16/31 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +5.4 | 8e-06 | 15/31 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +5.1 | 2e-05 | 13/31 (MIA PaCa-2, BT-474, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.48×** | +5.0 | 4e-05 | 16/30 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.94×** | +4.5 | 5e-04 | 12/29 (SW480, CHP-212, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +4.4 | 8e-04 | 11/31 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.90×** | +4.3 | 8e-04 | 8/31 (PANC-1, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +4.0 | 0.003 | 16/31 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.35×** | +3.9 | 0.005 | 12/31 (PANC-1, C-33 A, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.36×** | +3.8 | 0.007 | 10/30 (HT-29, NCI-H1573, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.008 | 11/29 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.053 | 13/30 (SW48, H4, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1297.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.669×** | -5.2 | 6e-05 | 15/30 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.672×** | -5.1 | 6e-05 | 15/31 (HS-578T, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.672×** | -5.1 | 6e-05 | 14/30 (HS-578T, RKO, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.798×** | -4.1 | 0.005 | 7/31 (H4, RKO, …) | top dose only | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.740×** | -3.9 | 0.012 | 11/31 (SW1417, SW 900, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.587×** | -3.6 | 0.030 | 8/29 (KATO III, AsPC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.747×** | -3.6 | 0.030 | 9/30 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.761×** | -3.5 | 0.030 | 13/30 (HS-578T, RKO, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **0.764×** | -3.5 | 0.033 | 9/30 (A-172, SW48, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.772×** | -3.3 | 0.048 | 9/31 (NCI-H1573, SW480, …) | inconsistent across doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.771×** | -3.2 | 0.067 | 10/30 (KATO III, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1297. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 69.2 | 0 | 10 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.196× (z -12.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -11.6) |
| [[PANC-1 (line)]] | alt | 14.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.94× (z +10.5) | — |
| [[A549 (line)]] | wt | 5.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.27× (z +10.4) | — |
| [[BT-474 (line)]] | alt | 22.2 | 0 | 1 | — | [[Tadalafil (drug)]] 0.05 µM 0.173× (z -8.8) |
| [[CHP-212 (line)]] | wt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0852× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change |
| [[H4 (line)]] | wt | 18.6 | 1 (1 ⚠) | 0 | [[Pitavastatin (Calcium) (drug)]] 5 µM 8.95× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 12.2 | 0 | 1 | — | [[Elimusertib hydrochloride (drug)]] 0.05 µM 0.0405× (z -14.1) |
| [[NCI-H2030 (line)]] | alt | 9.08 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0959× (z -11.4) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 22.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.178× (z -10.6) ⚠ cell-cycle shift, explains ~56% of this change |
| [[SW 900 (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change |
| [[SW1417 (line)]] | alt | 15.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +12.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.69 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.81 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 137 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.77 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 189 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 51.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1297), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR5]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[CACNA1H]] | +0.62 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[GLI2]] | +0.62 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[PPP2R2C]] | +0.61 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[IQSEC1]] | +0.61 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ACOT7]] | +0.61 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[FLNB]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[VAV2]] | +0.60 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[PAQR5]] | +0.58 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[LINC00659]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[SYT7]] | +0.56 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[ANO1]] | +0.56 | +0.45 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASH1L]] | -0.50 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[C21orf62-AS1]] | -0.50 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[GTF2IRD2B]] | -0.49 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[XRN1]] | -0.48 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[PAXIP1-AS2]] | -0.48 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[PPP4R3B]] | -0.47 | -0.43 / -0.37 | both halves | 9e-05 |  |
| [[MTUS1-DT]] | -0.47 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[RBM5]] | -0.47 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[ING3]] | -0.47 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[ANKHD1]] | -0.47 | -0.58 / -0.32 | both halves | 1e-04 |  |
| [[NIPBL]] | -0.46 | -0.48 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BEGAIN]] | B | BEGAIN activity raises IGSF9B's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 2.45× lower at baseline in the lines without BEGAIN | 0.042 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC19A1]] | B | IGSF9B activity raises SLC19A1's level | lines that do not express IGSF9B (17) vs lines expressing it (33) | 1.31× lower at baseline in the lines without IGSF9B | 0.019 | ⚠ within organs, on part of the lines; also absent: ADRA2C, PTPRN2, CBFA2T3 |
| [[PKP1]] | B | IGSF9B activity lowers PKP1's level | lines that do not express IGSF9B (17) vs lines expressing it (33) | 1.74× higher at baseline in the lines without IGSF9B | 0.072 | ⚠ within organs, on part of the lines; also absent: ADRA2C, PTPRN2, CBFA2T3 |

## Where it sits

- **Module**: [[Module 195]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.779). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.0, 3.2); signed map (-13.8, 42.7). **Vector** length 74.0, 15.9% of its response variance represented; |z| ≥ 3 in 859 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +5.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | +3.1 | +3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | +2.8 | -0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +4.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.8 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +4.0 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.6 | -5.1 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.3 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -3.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.0 | -2.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | immunoglobulin superfamily member 9B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q25 — chr11:133,896,438-133,956,968 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1030, LINC00947, LOC283174; previously MIR4697HG |
| Gene groups (HGNC) | Fibronectin type III domain containing; V-set domain containing; I-set domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPX0](https://www.uniprot.org/uniprotkb/Q9UPX0) (Protein turtle homolog B):

> Transmembrane protein which is abundantly expressed in interneurons, where it may regulate inhibitory synapse development (By similarity). May mediate homophilic cell adhesion (By similarity). Is involved in the organization and maintenance of axon initial segment (AIS) architecture, likely cooperating with PRICKLE2 to regulate ANK3/ANKG localization to AIS (By similarity).

**Summary**, from NCBI Gene [22997](https://www.ncbi.nlm.nih.gov/gene/22997):

> Predicted to enable kinase binding activity. Predicted to be involved in synaptic membrane adhesion. Predicted to act upstream of or within homophilic cell-cell adhesion and positive regulation of inhibitory postsynaptic potential. Predicted to be located in dendrite; inhibitory synapse; and neuronal cell body. Predicted to be active in GABA-ergic synapse; neuron projection; and postsynaptic specialization of symmetric synapse. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:32326](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32326) · Entrez [22997](https://www.ncbi.nlm.nih.gov/gene/22997) · UniProt [Q9UPX0](https://www.uniprot.org/uniprotkb/Q9UPX0) · Ensembl [ENSG00000080854](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080854)

## Data

Gene col 1297: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1297); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1297, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1297]; `tensor/DDL_lfc|DDL_z.npy` [1297]; `embed/gene_vectors.npy` [1297]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1297 or target_col == 1297). Every well: [[IGSF9B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGSF9B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
