---
symbol: "UGT2B7"
type: "gene"
col: 10078
ensembl_id: "ENSG00000171234"
name: "UDP glucuronosyltransferase family 2 member B7"
location: "4q13.2"
module: 62
arm: "+"
pooled_cpm: 6.3
n_lines_expressing: 13
n_dd_up: 14
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# UGT2B7

*UDP glucuronosyltransferase family 2 member B7* — 4q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.91× (z +11.7, q 9e-29, up in 2 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.49× (z +4.2, q 0.004, up in 0 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.504× (z -5.0, q 3e-04, down in 9 of 10 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNMB2-AS1]] (+0.59, fdr 6e-05), [[FGL1]] (+0.53, fdr 1e-04), [[LINC02008]] (+0.53, fdr 3e-04); moves opposite to [[EHBP1L1]] (-0.55, fdr 7e-05), [[ETV5]] (-0.55, fdr 2e-04), [[ODF2]] (-0.51, fdr 1e-04).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 3 go from it, the strongest it → [[RHEX]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10078.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.91×** | +11.7 | 9e-29 | 2/5 (A498, HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.37×** | +10.4 | 6e-23 | 1/4 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.60×** | +8.7 | 6e-16 | 2/4 (LoVo, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.2 | 0.004 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +4.1 | 0.005 | 1/8 (A498) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.7 | 0.022 | 2/10 (A498, HepG2/C3A) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.23×** | +3.6 | 0.030 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Salicylic acid (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.030 | 0/10 | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +3.4 | 0.034 | 3/7 (SK-MEL-2, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.60×** | +3.4 | 0.034 | 0/10 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.64×** | +3.3 | 0.040 | 2/8 (SNU-1, A498) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.54×** | +3.3 | 0.040 | 6/10 (HEC-1-A, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.53×** | +3.1 | 0.082 | 0/8 | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.1 | 0.091 | 0/6 | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10078.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.504×** | -5.0 | 3e-04 | 9/10 (HepG2/C3A, LoVo, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.548×** | -4.4 | 0.003 | 9/10 (HEC-1-A, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.536×** | -4.2 | 0.004 | 1/10 (C-33 A) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.615×** | -3.6 | 0.049 | 8/10 (HEC-1-A, HepG2/C3A, …) | all doses, stronger at high dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.402×** | -3.5 | 0.053 | 4/8 (HEC-1-A, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clofarabine (drug)]] 5 µM |  | 0.637× | -3.2 | 0.14 | 2/9 (LoVo, SNU-423) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10078. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 83.1 | 0 | 6 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0916× (z -13.1) |
| [[A498 (line)]] | wt | 46.2 | 2 (1 ⚠) | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 4.88× (z +9.3) ⚠ cell-cycle shift, explains ~7% of this change · without an alert: [[Selinexor (drug)]] 5 µM 2.69× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.164× (z -11.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.245× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 68.0 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0685× (z -13.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -9.9) |
| [[LoVo (line)]] | wt | 8.91 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0891× (z -11.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.133× (z -9.1) |
| [[SNU-1 (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0514× (z -10.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 0.624 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.517 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.710 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.751 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.742 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.648 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.754 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.750 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.533 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.988 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.905 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.959 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.754 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.669 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.969 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.563 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.597 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.821 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.630 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.838 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.684 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.661 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.750 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.564 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10078), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNMB2-AS1]] | +0.59 | +0.39 / +0.47 | both halves | 6e-05 |  |
| [[FGL1]] | +0.53 | +0.46 / +0.34 | both halves | 1e-04 |  |
| [[LINC02008]] | +0.53 | +0.50 / +0.28 | both halves | 3e-04 |  |
| [[PTCHD4]] | +0.52 | +0.38 / +0.42 | both halves | 6e-05 |  |
| [[AEBP2]] | +0.51 | +0.36 / +0.40 | both halves | 1e-04 |  |
| [[BAX]] | +0.51 | +0.29 / +0.40 | both halves | 2e-04 |  |
| [[DUSP3]] | +0.50 | +0.33 / +0.48 | both halves | 1e-04 |  |
| [[PURPL]] | +0.50 | +0.34 / +0.40 | both halves | 1e-04 |  |
| [[DUSP16]] | +0.50 | +0.35 / +0.38 | both halves | 1e-04 |  |
| [[PLXDC2]] | +0.48 | +0.44 / +0.12 | ⚠ not reproduced | 0.002 |  |
| [[MDM2]] | +0.48 | +0.32 / +0.35 | both halves | 2e-04 |  |
| [[TP53I3]] | +0.48 | +0.23 / +0.46 | both halves | 5e-04 |  |
| [[ABCA12]] | +0.48 | +0.23 / +0.42 | both halves | 5e-04 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHBP1L1]] | -0.55 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[ETV5]] | -0.55 | -0.31 / -0.54 | both halves | 2e-04 |  |
| [[ODF2]] | -0.51 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[KMT5A]] | -0.50 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[RECQL]] | -0.50 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[SLC9A7]] | -0.49 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[DNAAF3]] | -0.49 | -0.31 / -0.35 | both halves | 2e-04 |  |
| [[CENPJ]] | -0.49 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[RNF168]] | -0.49 | -0.20 / -0.48 | both halves | 7e-04 |  |
| [[GNAI2]] | -0.49 | -0.32 / -0.29 | both halves | 3e-04 |  |
| [[SRGAP2C]] | -0.48 | -0.14 / -0.55 | ⚠ one half (not replicated) | 0.002 |  |
| [[MCUB]] | -0.48 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[MTMR14]] | -0.47 | -0.35 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises UGT2B7's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[RHEX]] | C | RHEX activity raises UGT2B7's level | lines that do not express RHEX (43) vs lines expressing it (7) | 6.66× lower at baseline in the lines without RHEX | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, TIMD4, APOB; co-absent with the target |
| [[DPP7]] | C | DPP7 activity lowers UGT2B7's level | lines that do not express DPP7 (3) vs lines expressing it (47) | 9.24× higher at baseline in the lines without DPP7 | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: FAM89A, GALNT7, KLF2; maybe low, not absent |
| [[LINC00958]] | C | LINC00958 activity raises UGT2B7's level | lines that do not express LINC00958 (39) vs lines expressing it (11) | 2.04× lower at baseline in the lines without LINC00958 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SSX1, LINC01320, LINC00879; co-absent with the target |
| [[ZFY]] | C | ZFY activity raises UGT2B7's level | lines that do not express ZFY (29) vs lines expressing it (21) | 1.33× lower at baseline in the lines without ZFY | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PRKY, RPS4Y1, LINC00278; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHEX]] | C | UGT2B7 activity raises RHEX's level | lines that do not express UGT2B7 (37) vs lines expressing it (13) | 3.12× lower at baseline in the lines without UGT2B7 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A1, AFP, RHEX; co-absent with the target |
| [[APOB]] | C | UGT2B7 activity raises APOB's level | lines that do not express UGT2B7 (37) vs lines expressing it (13) | 2.51× lower at baseline in the lines without UGT2B7 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A1, AFP, RHEX; co-absent with the target |
| [[PRLR]] | C | UGT2B7 activity raises PRLR's level | lines that do not express UGT2B7 (37) vs lines expressing it (13) | 1.49× lower at baseline in the lines without UGT2B7 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A1, AFP, RHEX; co-absent with the target |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.433). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.2, -3.0); signed map (42.9, -20.1). **Vector** length 26.9, 6.49% of its response variance represented; |z| ≥ 3 in 283 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.4 | +8.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.2 | +3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.1 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.1 | +0.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.0 | +1.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.9 | +3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.9 | +1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.9 | +2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +0.8 | +1.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -0.9 | -3.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -0.9 | -5.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -0.8 | -4.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.6 | -0.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -0.6 | -2.5 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -0.5 | -1.5 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.4 | -1.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -0.4 | -0.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.4 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.4 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | UDP glucuronosyltransferase family 2 member B7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.2 — chr4:69,051,363-69,112,987 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UGT2B9 |
| Gene groups (HGNC) | UDP glucuronosyltransferases |
| Reactome | 6 pathways, smallest: Prednisone ADME; Glucuronidation; Aspirin ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [P16662](https://www.uniprot.org/uniprotkb/P16662) (UDP-glucuronosyltransferase 2B7):

> UDP-glucuronosyltransferase (UGT) that catalyzes phase II biotransformation reactions in which lipophilic substrates are conjugated with glucuronic acid to increase the metabolite's water solubility, thereby facilitating excretion into either the urine or bile. Essential for the elimination and detoxification of drugs, xenobiotics and endogenous compounds. Catalyzes the glucuronidation of endogenous steroid hormones such as androgens (epitestosterone, androsterone) and estrogens (estradiol, …

**Summary**, from NCBI Gene [7364](https://www.ncbi.nlm.nih.gov/gene/7364):

> The protein encoded by this gene belongs to the UDP-glycosyltransferase (UGT) family. UGTs serve a major role in the conjugation and subsequent elimination of potentially toxic xenobiotics and endogenous compounds. This protein is localized in the microsome membrane, and has unique specificity for 3,4-catechol estrogens and estriol, suggesting that it may play an important role in regulating the level and activity of these potent estrogen metabolites. Alternative splicing results in multiple …

**Accessions** — [HGNC:12554](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12554) · Entrez [7364](https://www.ncbi.nlm.nih.gov/gene/7364) · UniProt [P16662](https://www.uniprot.org/uniprotkb/P16662) · Ensembl [ENSG00000171234](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171234)

## Data

Gene col 10078: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10078); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10078, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10078]; `tensor/DDL_lfc|DDL_z.npy` [10078]; `embed/gene_vectors.npy` [10078]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10078 or target_col == 10078). Every well: [[UGT2B7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UGT2B7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
