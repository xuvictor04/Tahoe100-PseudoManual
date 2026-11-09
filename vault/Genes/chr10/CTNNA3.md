---
symbol: "CTNNA3"
type: "gene"
col: 11382
ensembl_id: "ENSG00000183230"
name: "catenin alpha 3"
location: "10q21.3"
module: 9
arm: "+"
pooled_cpm: 35.26
n_lines_expressing: 46
n_dd_up: 10
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 7
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# CTNNA3

*catenin alpha 3* — 10q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.51× (z +14.3, q 7e-44, up in 29 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.90× (z +10.3, q 7e-23, up in 28 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.679× (z -4.4, q 0.005, down in 23 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRID2]] (+0.67, fdr 7e-06), [[AGBL4]] (+0.64, fdr 1e-05), [[PCDH11X]] (+0.64, fdr 3e-05); moves opposite to [[LSM11]] (-0.49, fdr 6e-05), [[HSDL1]] (-0.46, fdr 1e-04), [[SMYD4]] (-0.46, fdr 7e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KCNT2]] → it (grade B ⚠); 7 go from it, the strongest it → [[CACNA2D1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11382.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.51×** | +14.3 | 7e-44 | 29/37 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.16×** | +12.7 | 3e-34 | 27/34 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.76×** | +10.7 | 2e-24 | 23/36 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +10.3 | 7e-23 | 28/43 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +6.2 | 6e-08 | 26/44 (NCI-H460, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +5.1 | 4e-05 | 23/43 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +4.8 | 1e-04 | 21/43 (A498, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.011 | 18/43 (SK-MEL-2, MIA PaCa-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.014 | 17/44 (SNU-423, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.5 | 0.023 | 9/44 (NCI-H23, LoVo, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.48×** | +3.2 | 0.076 | 16/39 (J82, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | 1.31× | +3.0 | 0.11 | 5/44 (NCI-H1573, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11382.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.679×** | -4.4 | 0.005 | 23/44 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.771×** | -4.2 | 0.007 | 18/44 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.698×** | -4.1 | 0.007 | 18/43 (NCI-H23, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.726×** | -3.7 | 0.034 | 16/43 (NCI-H2030, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.744×** | -3.4 | 0.077 | 16/43 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.763× | -3.1 | 0.18 | 15/43 (SHP-77, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11382. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 838 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 81.8 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0900× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.137× (z -11.6) |
| [[PANC-1 (line)]] | alt | 19.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.80× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +8.6) | — |
| [[A549 (line)]] | wt | 14.7 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.93× (z +10.3) | — |
| [[HEC-1-A (line)]] | alt | 10.7 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.62× (z +12.5) | — |
| [[A498 (line)]] | wt | 12.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +11.7) | — |
| [[NCI-H460 (line)]] | wt | 9.94 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +13.4) | — |
| [[H4 (line)]] | wt | 26.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 12.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +9.3) | — |
| [[KATO III (line)]] | alt | 41.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.14× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 54.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.07× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 8.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.92× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 11.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.87× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.65× (z +12.4) | — |
| [[NCI-H661 (line)]] | alt | 669 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 32.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 38.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0956× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 37.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.11 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.32 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.51 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.37 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11382), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRID2]] | +0.67 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[AGBL4]] | +0.64 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[PCDH11X]] | +0.64 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[SPAG17]] | +0.60 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[UNC5C]] | +0.60 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[MAPK10]] | +0.59 | +0.53 / +0.59 | both halves | 1e-05 | same gene group |
| [[ATRNL1]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[DMD]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 | same gene group |
| [[CDH18]] | +0.57 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[LINC01122]] | +0.55 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[ADIRF]] | +0.55 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[NREP]] | +0.54 | +0.48 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSM11]] | -0.49 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[HSDL1]] | -0.46 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[SMYD4]] | -0.46 | -0.38 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNT2]] | B | KCNT2 activity lowers CTNNA3's level | lines that do not express KCNT2 (25) vs lines expressing it (25) | 1.82× higher at baseline in the lines without KCNT2 | 0.085 | ⚠ within organs, on part of the lines; also absent: TCF4, FGF14, MSC-AS1 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNA2D1]] | C | CTNNA3 activity lowers CACNA2D1's level | lines that do not express CTNNA3 (4) vs lines expressing it (46) | 2.03× higher at baseline in the lines without CTNNA3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL10, MYO15B; maybe low, not absent; its own permutation p |
| [[UBR5]] | C | CTNNA3 activity lowers UBR5's level | lines that do not express CTNNA3 (4) vs lines expressing it (46) | 1.55× higher at baseline in the lines without CTNNA3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL10, MYO15B; maybe low, not absent; its own permutation p |
| [[LINC02268]] | C | CTNNA3 activity lowers LINC02268's level | lines that do not express CTNNA3 (4) vs lines expressing it (46) | 1.28× higher at baseline in the lines without CTNNA3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL10, MYO15B; maybe low, not absent; its own permutation p |
| [[OR3A2]] | C | CTNNA3 activity raises OR3A2's level | lines that do not express CTNNA3 (4) vs lines expressing it (46) | 1.19× lower at baseline in the lines without CTNNA3 | 0.062 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL10, MYO15B; maybe low, not absent |
| [[KRT8]] | C | CTNNA3 activity raises KRT8's level | lines that do not express CTNNA3 (4) vs lines expressing it (46) | 3.10× lower at baseline in the lines without CTNNA3 | 0.069 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL10, MYO15B; maybe low, not absent |
| [[LINC00882]] | C | CTNNA3 activity lowers LINC00882's level | lines that do not express CTNNA3 (4) vs lines expressing it (46) | 2.88× higher at baseline in the lines without CTNNA3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL10, MYO15B; maybe low, not absent; its own permutation p |
| [[ZFHX4-AS1]] | C | CTNNA3 activity raises ZFHX4-AS1's level | lines that do not express CTNNA3 (4) vs lines expressing it (46) | 1.41× lower at baseline in the lines without CTNNA3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL10, MYO15B; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.494). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (27.4, 28.2); signed map (38.0, 17.0). **Vector** length 90.4, 20.7% of its response variance represented; |z| ≥ 3 in 896 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.6 | +14.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.6 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.8 | +10.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.4 | +10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.2 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +3.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.8 | +1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +1.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.4 | -3.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -4.2 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.4 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.3 | -3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | catenin alpha 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.3 — chr10:65,912,457-67,763,637 (-) |
| Ensembl biotype | protein_coding |
| Also known as | VR22, MGC26194 |
| Gene groups (HGNC) | Alpha catenins; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UI47](https://www.uniprot.org/uniprotkb/Q9UI47) (Catenin alpha-3):

> May be involved in formation of stretch-resistant cell-cell adhesion complexes.

**Summary**, from NCBI Gene [29119](https://www.ncbi.nlm.nih.gov/gene/29119):

> This gene encodes a protein that belongs to the vinculin/alpha-catenin family. The encoded protein plays a role in cell-cell adhesion in muscle cells. Mutations in this gene are associated with arrhythmogenic right ventricular dysplasia, familial 13. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:2511](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2511) · Entrez [29119](https://www.ncbi.nlm.nih.gov/gene/29119) · UniProt [Q9UI47](https://www.uniprot.org/uniprotkb/Q9UI47) · Ensembl [ENSG00000183230](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183230)

## Data

Gene col 11382: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11382); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11382, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11382]; `tensor/DDL_lfc|DDL_z.npy` [11382]; `embed/gene_vectors.npy` [11382]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11382 or target_col == 11382). Every well: [[CTNNA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTNNA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
