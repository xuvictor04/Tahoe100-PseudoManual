---
symbol: "NDNF"
type: "gene"
col: 10376
ensembl_id: "ENSG00000173376"
name: "neuron derived neurotrophic factor"
location: "4q27"
module: 13
arm: "+"
pooled_cpm: 3.94
n_lines_expressing: 25
n_dd_up: 15
n_dd_down: 15
n_dd_up_clean: 8
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 24
direction_downstream: 19
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# NDNF

*neuron derived neurotrophic factor* — 4q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.44× (z +17.1, q 0e+00, up in 19 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.438× (z -8.1, q 4e-13, down in 16 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADGRB3]] (+0.63, fdr 8e-06), [[CA12]] (+0.63, fdr 1e-05), [[LINC03047]] (+0.63, fdr 1e-05); moves opposite to [[VSIG10]] (-0.46, fdr 6e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[TNS1]] → it (grade B ⚠); 19 go from it, the strongest it → [[MEIS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10376.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.44×** | +17.1 | 0e+00 | 19/21 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.37×** | +11.9 | 4e-30 | 19/21 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.34×** | +11.3 | 1e-27 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +7.6 | 4e-12 | 3/18 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.00×** | +6.8 | 1e-09 | 11/21 (NCI-H460, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +6.0 | 2e-07 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +4.8 | 1e-04 | 0/13 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.3 | 0.001 | 0/13 | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +3.9 | 0.007 | 0/6 | top dose only | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.70×** | +3.7 | 0.012 | 0/11 | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.46×** | +3.7 | 0.012 | 3/21 (CFPAC-1, C-33 A, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +3.3 | 0.047 | 0/12 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.39×** | +3.1 | 0.090 | 2/19 (NCI-H460, SHP-77) | inconsistent across doses | low cells (technical?) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.39×** | +3.0 | 0.090 | 1/20 (HOP62) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.090 | 6/19 (LOX-IMVI, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, none with an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10376.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.438×** | -8.1 | 4e-13 | 16/21 (LOX-IMVI, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.510×** | -6.6 | 1e-08 | 17/21 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.522×** | -6.4 | 3e-08 | 14/21 (NCI-H2030, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.523×** | -6.3 | 3e-08 | 16/18 (HOP62, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.577×** | -5.4 | 9e-06 | 14/21 (SW 900, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.568×** | -5.3 | 1e-05 | 14/19 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.607×** | -4.6 | 3e-04 | 17/21 (HOP62, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.631×** | -4.5 | 5e-04 | 15/21 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.492×** | -3.6 | 0.018 | 11/20 (LOX-IMVI, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Resveratrol (drug)]] 5 µM |  | **0.772×** | -3.6 | 0.019 | 3/22 (LOX-IMVI, CHP-212, …) | top dose only |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.761×** | -3.6 | 0.019 | 5/21 (CFPAC-1, SHP-77, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.692×** | -3.5 | 0.025 | 13/19 (NCI-H1792, H4, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.704×** | -3.4 | 0.026 | 15/21 (H4, HS-578T, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.05 µM |  | **0.704×** | -3.2 | 0.060 | 1/21 (RPMI-7951) | inconsistent across doses |  |
| [[Cilostazol (drug)]] 5 µM |  | **0.721×** | -3.1 | 0.080 | 2/21 (RPMI-7951, NCI-H2030) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10376. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 26.2 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0612× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -13.5) |
| [[CFPAC-1 (line)]] | alt | 12.3 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0293× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0699× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 20.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -10.7) |
| [[HS-578T (line)]] | alt | 11.7 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0297× (z -13.8) |
| [[hTERT-HPNE (line)]] | wt | 16.1 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0717× (z -10.2) |
| [[H4 (line)]] | wt | 23.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0816× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 4.35 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0423× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 8.32 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0315× (z -17.3) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0374× (z -11.6) |
| [[A-172 (line)]] | wt | 6.75 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0746× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 1.98 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -9.0) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SHP-77 (line)]] | alt | 13.6 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0584× (z -12.7) |
| [[A-427 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.353 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.348 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.688 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.302 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.398 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.844 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.253 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.759 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.272 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.593 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.550 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.566 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.326 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.350 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.413 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10376), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRB3]] | +0.63 | +0.66 / +0.58 | both halves | 8e-06 | **novel candidate** |
| [[CA12]] | +0.63 | +0.63 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[LINC03047]] | +0.63 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[SETBP1]] | +0.61 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[KCTD16]] | +0.61 | +0.59 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[SLFN11]] | +0.61 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[LINC01411]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[NOL4]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[NTF3]] | +0.58 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[NEFL]] | +0.57 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[PTPRD]] | +0.57 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[GLYATL2]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VSIG10]] | -0.46 | -0.46 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 4, C 20. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNS1]] | B | TNS1 activity raises NDNF's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 2.16× lower at baseline in the lines without TNS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |
| [[DIRC3]] | B | DIRC3 activity raises NDNF's level | lines that do not express DIRC3 (19) vs lines expressing it (31) | 1.97× lower at baseline in the lines without DIRC3 | 0.071 | ⚠ within organs, on part of the lines; also absent: CD200, MSC, TNS1; maybe low, not absent |
| [[PLOD2]] | B | PLOD2 activity raises NDNF's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 2.50× lower at baseline in the lines without PLOD2 | 0.072 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[MEIS1]] | B | MEIS1 activity raises NDNF's level | lines that do not express MEIS1 (11) vs lines expressing it (39) | 2.48× lower at baseline in the lines without MEIS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: LINC01798, DYNC1I1, CAMK4 |
| [[ITGA11]] | C | ITGA11 activity raises NDNF's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 4.65× lower at baseline in the lines without ITGA11 | 0.004 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises NDNF's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 3.81× lower at baseline in the lines without APCDD1L | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[TMEM200A]] | C | TMEM200A activity raises NDNF's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 2.87× lower at baseline in the lines without TMEM200A | 0.009 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615; co-absent with the target |
| [[AGTR1]] | C | AGTR1 activity raises NDNF's level | lines that do not express AGTR1 (37) vs lines expressing it (13) | 3.31× lower at baseline in the lines without AGTR1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, APBB1IP, CARMN; co-absent with the target |
| [[CA12]] | C | CA12 activity raises NDNF's level | lines that do not express CA12 (29) vs lines expressing it (21) | 3.07× lower at baseline in the lines without CA12 | 0.013 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1; co-absent with the target |
| [[PTGFR]] | C | PTGFR activity raises NDNF's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 3.52× lower at baseline in the lines without PTGFR | 0.013 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX; co-absent with the target |
| [[ODAD2]] | C | ODAD2 activity raises NDNF's level | lines that do not express ODAD2 (27) vs lines expressing it (23) | 3.03× lower at baseline in the lines without ODAD2 | 0.016 | ⚠ within organs, on part of the lines; also absent: FBN2, NDNF, EPHA5; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises NDNF's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 3.95× lower at baseline in the lines without LINC01411 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 5, C 14. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEIS1]] | B | NDNF activity raises MEIS1's level | lines that do not express NDNF (25) vs lines expressing it (25) | 3.12× lower at baseline in the lines without NDNF | 0.003 | ⚠ within organs, on part of the lines; also absent: ADAM23, GUCY1B1, CNRIP1 |
| [[SLC6A6]] | B | NDNF activity raises SLC6A6's level | lines that do not express NDNF (25) vs lines expressing it (25) | 2.44× lower at baseline in the lines without NDNF | 0.069 | ⚠ within organs, on part of the lines; also absent: ADAM23, GUCY1B1, CNRIP1 |
| [[MLLT3]] | B | NDNF activity raises MLLT3's level | lines that do not express NDNF (25) vs lines expressing it (25) | 1.76× lower at baseline in the lines without NDNF | 0.069 | ⚠ within organs, on part of the lines; also absent: ADAM23, GUCY1B1, CNRIP1 |
| [[ELL2]] | B | NDNF activity raises ELL2's level | lines that do not express NDNF (25) vs lines expressing it (25) | 2.70× lower at baseline in the lines without NDNF | 0.073 | ⚠ within organs, on part of the lines; also absent: ADAM23, GUCY1B1, CNRIP1 |
| [[LRIG1]] | B | NDNF activity raises LRIG1's level | lines that do not express NDNF (25) vs lines expressing it (25) | 1.48× lower at baseline in the lines without NDNF | 0.097 | ⚠ within organs, on part of the lines; also absent: ADAM23, GUCY1B1, CNRIP1 |
| [[TCF4]] | C | NDNF activity raises TCF4's level | lines that do not express NDNF (25) vs lines expressing it (25) | 4.90× lower at baseline in the lines without NDNF | 0.014 | ⚠ within organs, on part of the lines; also absent: ADAM23, GUCY1B1, CNRIP1; co-absent with the target |
| [[TWIST2]] | C | NDNF activity raises TWIST2's level | lines that do not express NDNF (25) vs lines expressing it (25) | 5.49× lower at baseline in the lines without NDNF | 0.018 | ⚠ within organs, on part of the lines; also absent: ADAM23, GUCY1B1, CNRIP1; co-absent with the target |
| [[ADAMTS6]] | C | NDNF activity raises ADAMTS6's level | lines that do not express NDNF (25) vs lines expressing it (25) | 3.76× lower at baseline in the lines without NDNF | 0.025 | ⚠ within organs, on part of the lines; also absent: ADAM23, GUCY1B1, CNRIP1; co-absent with the target |
| [[PTGFR]] | C | NDNF activity raises PTGFR's level | lines that do not express NDNF (25) vs lines expressing it (25) | 3.58× lower at baseline in the lines without NDNF | 0.027 | ⚠ within organs, on part of the lines; also absent: ADAM23, GUCY1B1, CNRIP1; co-absent with the target |
| [[TSHZ3]] | C | NDNF activity raises TSHZ3's level | lines that do not express NDNF (25) vs lines expressing it (25) | 5.31× lower at baseline in the lines without NDNF | 0.028 | ⚠ within organs, on part of the lines; also absent: ADAM23, GUCY1B1, CNRIP1; co-absent with the target |
| [[ITGA11]] | C | NDNF activity raises ITGA11's level | lines that do not express NDNF (25) vs lines expressing it (25) | 4.84× lower at baseline in the lines without NDNF | 0.029 | ⚠ within organs, on part of the lines; also absent: ADAM23, GUCY1B1, CNRIP1; co-absent with the target |
| [[GRAMD1B]] | C | NDNF activity raises GRAMD1B's level | lines that do not express NDNF (25) vs lines expressing it (25) | 3.64× lower at baseline in the lines without NDNF | 0.058 | ⚠ within organs, on part of the lines; also absent: ADAM23, GUCY1B1, CNRIP1; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.591). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.3, 19.3); signed map (29.4, 44.3). **Vector** length 60.3, 15.2% of its response variance represented; |z| ≥ 3 in 685 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +17.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.4 | +11.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | -0.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +3.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +0.6 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -2.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.8 |
|  | [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -2.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.6 | -2.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.5 | +1.0 |
|  | [[Encorafenib (drug)]] 5 µM |  | -1.5 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | neuron derived neurotrophic factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q27 — chr4:121,035,613-121,073,021 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23191; previously C4orf31 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TB73](https://www.uniprot.org/uniprotkb/Q8TB73) (Protein NDNF):

> Secretory protein that plays a role in various cellular processes. Acts as a chemorepellent acting on gonadotropin-releasing hormone (GnRH) expressing neurons regulating their migration to the hypothalamus. Also promotes neuron migration, growth and survival as well as neurite outgrowth and is involved in the development of the olfactory system. May also act through the regulation of growth factors activity and downstream signaling. Also regulates extracellular matrix assembly and cell …

**Summary**, from NCBI Gene [79625](https://www.ncbi.nlm.nih.gov/gene/79625):

> Predicted to enable heparin binding activity. Involved in several processes, including cellular response to hypoxia; negative regulation of apoptotic process; and nitric oxide mediated signal transduction. Located in extracellular region. Is active in obsolete extracellular space. Implicated in hypogonadotropic hypogonadism. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26256](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26256) · Entrez [79625](https://www.ncbi.nlm.nih.gov/gene/79625) · UniProt [Q8TB73](https://www.uniprot.org/uniprotkb/Q8TB73) · Ensembl [ENSG00000173376](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173376)

## Data

Gene col 10376: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10376); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10376, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10376]; `tensor/DDL_lfc|DDL_z.npy` [10376]; `embed/gene_vectors.npy` [10376]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10376 or target_col == 10376). Every well: [[NDNF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDNF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
