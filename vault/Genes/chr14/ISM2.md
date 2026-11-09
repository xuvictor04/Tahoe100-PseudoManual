---
symbol: "ISM2"
type: "gene"
col: 1994
ensembl_id: "ENSG00000100593"
name: "isthmin 2"
location: "14q24.3"
module: 103
arm: "+"
pooled_cpm: 2.35
n_lines_expressing: 41
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 7
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# ISM2

*isthmin 2* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.67× (z +8.6, q 4e-15, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.59× (z +6.0, q 7e-07, up in 12 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.357× (z -9.5, q 1e-18, down in 22 of 29 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM74B]] (+0.63, fdr 7e-06), [[DPYSL4]] (+0.61, fdr 1e-05), [[NIM1K]] (+0.60, fdr 2e-05); moves opposite to [[PCED1B]] (-0.41, fdr 1e-04), [[RUFY3]] (-0.41, fdr 1e-04), [[PKP4]] (-0.40, fdr 2e-04).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP3K15]] → it (grade B ⚠); 7 go from it, the strongest it → [[GDF1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1994.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.67×** | +8.6 | 4e-15 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +6.0 | 7e-07 | 12/32 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +5.8 | 1e-06 | 7/22 (HEC-1-A, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.84×** | +5.5 | 4e-06 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.27×** | +5.3 | 1e-05 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +4.8 | 2e-04 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +4.2 | 0.003 | 5/28 (HOP62, SW480, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.008 | 2/33 (HEC-1-A, SW1417) | top dose only | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +3.7 | 0.013 | 8/26 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.53×** | +3.7 | 0.013 | 2/17 (C-33 A, A-172) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +3.6 | 0.018 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.2 | 0.059 | 2/9 (SW480, LoVo) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +3.1 | 0.078 | 0/2 | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.61×** | +3.1 | 0.080 | 1/11 (HOP62) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1994.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.357×** | -9.5 | 1e-18 | 22/29 (HepG2/C3A, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.448×** | -7.4 | 4e-11 | 21/36 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.566×** | -5.1 | 8e-05 | 17/31 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.599×** | -4.7 | 3e-04 | 16/26 (HepG2/C3A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.634×** | -4.2 | 0.003 | 12/34 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.638×** | -4.2 | 0.003 | 11/25 (NCI-H1792, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.657×** | -3.9 | 0.008 | 10/30 (HepG2/C3A, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1994. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 9.03 | 0 | 7 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0201× (z -16.1) |
| [[NCI-H460 (line)]] | wt | 4.90 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0259× (z -15.0) |
| [[HepG2_C3A (line)]] | wt | 33.4 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0231× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.112× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 7.43 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0248× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0717× (z -10.1) |
| [[A-172 (line)]] | wt | 2.97 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0615× (z -8.6) ⚠ cell-cycle shift, explains ~16% of this change |
| [[A-427 (line)]] | wt | 3.21 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0558× (z -9.1) |
| [[HOP62 (line)]] | alt | 2.89 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0692× (z -8.9) |
| [[SW480 (line)]] | alt | 2.33 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0654× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 0.442 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.698 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.861 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.774 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.471 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.911 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.406 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.439 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.749 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.707 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.470 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.551 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.813 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.000 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1994), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM74B]] | +0.63 | +0.58 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[DPYSL4]] | +0.61 | +0.49 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[NIM1K]] | +0.60 | +0.46 / +0.67 | both halves | 2e-05 |  |
| [[C2orf72]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[MAP3K15]] | +0.57 | +0.51 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[CPNE5]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[B3GNT4]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[KCNG2]] | +0.55 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[CASKIN1]] | +0.54 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[RGS2]] | +0.54 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[NRN1]] | +0.53 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[NRG4]] | +0.52 | +0.45 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCED1B]] | -0.41 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[RUFY3]] | -0.41 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[PKP4]] | -0.40 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[MIR31HG]] | -0.39 | -0.35 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP3K15]] | B | MAP3K15 activity raises ISM2's level | lines that do not express MAP3K15 (19) vs lines expressing it (31) | 1.75× lower at baseline in the lines without MAP3K15 | 0.0996 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, NEXMIF, BARX1 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GDF1]] | B | ISM2 activity raises GDF1's level | lines that do not express ISM2 (9) vs lines expressing it (41) | 2.07× lower at baseline in the lines without ISM2 | 0.055 | ⚠ within organs, on part of the lines; also absent: DYSF, CSRP2, LINC02609; maybe low, not absent |
| [[GPR155]] | B | ISM2 activity raises GPR155's level | lines that do not express ISM2 (9) vs lines expressing it (41) | 2.76× lower at baseline in the lines without ISM2 | 0.063 | ⚠ within organs, on part of the lines; also absent: DYSF, CSRP2, LINC02609; maybe low, not absent |
| [[ITGA2B]] | B | ISM2 activity raises ITGA2B's level | lines that do not express ISM2 (9) vs lines expressing it (41) | 1.83× lower at baseline in the lines without ISM2 | 0.065 | ⚠ within organs, on part of the lines; also absent: DYSF, CSRP2, LINC02609; maybe low, not absent |
| [[FAM234B]] | B | ISM2 activity raises FAM234B's level | lines that do not express ISM2 (9) vs lines expressing it (41) | 1.82× lower at baseline in the lines without ISM2 | 0.070 | ⚠ within organs, on part of the lines; also absent: DYSF, CSRP2, LINC02609; maybe low, not absent |
| [[SCUBE1]] | B | ISM2 activity raises SCUBE1's level | lines that do not express ISM2 (9) vs lines expressing it (41) | 1.07× lower at baseline in the lines without ISM2 | 0.085 | ⚠ within organs, on part of the lines; also absent: DYSF, CSRP2, LINC02609; maybe low, not absent |
| [[WDR54]] | B | ISM2 activity raises WDR54's level | lines that do not express ISM2 (9) vs lines expressing it (41) | 2.18× lower at baseline in the lines without ISM2 | 0.085 | ⚠ within organs, on part of the lines; also absent: DYSF, CSRP2, LINC02609; maybe low, not absent |
| [[BOC]] | B | ISM2 activity raises BOC's level | lines that do not express ISM2 (9) vs lines expressing it (41) | 2.31× lower at baseline in the lines without ISM2 | 0.095 | ⚠ within organs, on part of the lines; also absent: DYSF, CSRP2, LINC02609; maybe low, not absent |

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.675). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (5.8, 44.9); signed map (-29.8, 34.8). **Vector** length 53.4, 9.44% of its response variance represented; |z| ≥ 3 in 792 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +2.9 | +4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.7 | +3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.7 | +8.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.9 | -1.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +0.8 | +0.8 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -2.3 | -4.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -9.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.0 | -4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.9 | -7.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.7 | -4.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -3.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[Benztropine (mesylate) (drug)]] 0.5 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | isthmin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:77,474,394-77,498,816 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32147, TAIL1; previously THSD3 |
| Gene groups (HGNC) | Isthmin family |
| Matched by | ensembl_id |

UniProt [Q6H9L7](https://www.uniprot.org/uniprotkb/Q6H9L7) carries no function annotation.

**Summary**, from NCBI Gene [145501](https://www.ncbi.nlm.nih.gov/gene/145501):

> The protein encoded by this gene contains a type 1 thrombospondin domain, which is present in thrombospondin, a number of proteins involved in the complement pathway, as well as in extracellular matrix proteins. Two alternatively spliced transcript variants encoding distinct isoforms have been observed. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:23176](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23176) · Entrez [145501](https://www.ncbi.nlm.nih.gov/gene/145501) · UniProt [Q6H9L7](https://www.uniprot.org/uniprotkb/Q6H9L7) · Ensembl [ENSG00000100593](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100593)

## Data

Gene col 1994: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1994); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1994, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1994]; `tensor/DDL_lfc|DDL_z.npy` [1994]; `embed/gene_vectors.npy` [1994]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1994 or target_col == 1994). Every well: [[ISM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ISM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
