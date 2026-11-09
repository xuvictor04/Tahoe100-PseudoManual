---
symbol: "DUSP2"
type: "gene"
col: 8126
ensembl_id: "ENSG00000158050"
name: "dual specificity phosphatase 2"
location: "2q11.2"
module: 162
arm: "+"
pooled_cpm: 2.26
n_lines_expressing: 27
n_dd_up: 20
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/162"]
generated_by: "tahoemap"
---

# DUSP2

*dual specificity phosphatase 2* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 10.1× (z +19.9, q 0e+00, up in 13 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.341× (z -6.1, q 7e-07, down in 16 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASTL]] (+0.76, fdr 7e-06, ⚠ same locus), [[NRARP]] (+0.72, fdr 7e-06), [[EGR3]] (+0.69, fdr 7e-06), [[EGR2]] (+0.66, fdr 7e-06); moves opposite to [[MFSD8]] (-0.59, fdr 1e-05), [[GPALPP1]] (-0.56, fdr 3e-05), [[PDHX]] (-0.53, fdr 4e-05).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NKD2]] → it (grade B ⚠); 2 go from it, the strongest it → [[JUNB]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8126.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **10.1×** | +19.9 | 0e+00 | 13/17 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **12.3×** | +15.2 | 0e+00 | 21/22 (MIA PaCa-2, SW48, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **9.30×** | +13.0 | 1e-36 | 14/20 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **7.29×** | +11.6 | 5e-29 | 1/3 (HOP62) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.47×** | +11.4 | 8e-28 | 11/15 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **5.91×** | +10.8 | 5e-25 | 20/23 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **5.64×** | +10.5 | 5e-24 | 6/10 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **4.70×** | +8.7 | 2e-16 | 3/4 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.97×** | +8.4 | 3e-15 | 19/23 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **3.50×** | +7.3 | 1e-11 | 8/15 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.70×** | +6.0 | 9e-08 | 11/23 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **2.39×** | +5.3 | 6e-06 | 3/10 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.23×** | +4.9 | 5e-05 | 4/14 (NCI-H460, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +4.3 | 7e-04 | 2/9 (NCI-H460, NCI-H23) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.63×** | +4.2 | 1e-03 | 10/23 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.80×** | +3.5 | 0.013 | 12/24 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Carbamazepine (drug)]] 5 µM |  | **1.73×** | +3.3 | 0.029 | 5/23 (SW480, RKO, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.70×** | +3.2 | 0.037 | 2/17 (RKO, PANC-1) | rises with dose | cell-cycle shift (explains ~23% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8126.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.341×** | -6.1 | 7e-07 | 16/23 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.374×** | -5.8 | 2e-06 | 19/23 (SW48, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.474×** | -4.6 | 9e-04 | 16/23 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 0.578× | -3.1 | 0.27 | 4/23 (HCT15, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.55 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8126. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.15 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 43.5× (z +13.6) | — |
| [[PANC-1 (line)]] | alt | 4.25 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 61.1× (z +18.6) | [[Verteporfin (drug)]] 5 µM 0.0376× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 16.2 | 0 | 3 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.406× (z -12.0) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 0.0654× (z -10.2) |
| [[HOP62 (line)]] | alt | 4.79 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 51.8× (z +13.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.52 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 35.6× (z +10.1) | [[Adagrasib (drug)]] 0.05 µM 0.379× (z -9.4) ⚠ position not correctable |
| [[CFPAC-1 (line)]] | alt | 0.746 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 301× (z +12.1) | — |
| [[NCI-H1792 (line)]] | alt | 1.70 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 126× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 1.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.8× (z +10.8) | — |
| [[SW48 (line)]] | wt | 13.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.105× (z -10.0) ⚠ cell-cycle shift, explains ~84% of this change |
| [[A-172 (line)]] | wt | 0.190 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.830 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.223 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.725 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.426 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.598 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.214 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.255 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.273 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.903 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.204 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.308 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.189 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.433 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.198 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.255 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.69 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8126), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASTL]] | +0.76 | +0.74 / +0.78 | both halves | 7e-06 | ⚠ same locus (4.7 kb, same strand: neighbours can correlate without regulation) |
| [[NRARP]] | +0.72 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[EGR3]] | +0.69 | +0.66 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE; STRING 532 |
| [[EGR2]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 540 |
| [[NTMT1]] | +0.66 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[IER2]] | +0.64 | +0.63 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 440 |
| [[ARC]] | +0.62 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[MAP3K14]] | +0.62 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[NR4A1]] | +0.62 | +0.54 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 596 |
| [[EGR1]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 573 |
| [[SPATA2L]] | +0.61 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[SHH]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[PLEKHO2]] | +0.59 | +0.54 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD8]] | -0.59 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[GPALPP1]] | -0.56 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[PDHX]] | -0.53 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[CLCC1]] | -0.53 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[GPBP1L1]] | -0.51 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[TMEM94]] | -0.51 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[SAP30L-AS1]] | -0.51 | -0.38 / -0.38 | both halves | 6e-05 |  |
| [[NADSYN1]] | -0.50 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[RAB11FIP2]] | -0.50 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[ADD1]] | -0.50 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[SELENOF]] | -0.50 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[GLUD1P3]] | -0.49 | -0.51 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NKD2]] | B | NKD2 activity raises DUSP2's level | lines that do not express NKD2 (16) vs lines expressing it (34) | 1.98× lower at baseline in the lines without NKD2 | 0.049 | ⚠ within organs, on part of the lines; also absent: CHRNA7, ASTL, PALD1 |
| [[ASTL]] | C | ASTL activity raises DUSP2's level | lines that do not express ASTL (26) vs lines expressing it (24) | 2.94× lower at baseline in the lines without ASTL | 3e-04 | ⚠ within organs, on part of the lines; also absent: DUSP2, HOXA11, FGF20; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JUNB]] | B | DUSP2 activity lowers JUNB's level | lines that do not express DUSP2 (23) vs lines expressing it (27) | 1.28× higher at baseline in the lines without DUSP2 | 0.092 | ⚠ within organs, on part of the lines; also absent: ASTL, HOXA11, KCNE3; maybe low, not absent |
| [[ASTL]] | C | DUSP2 activity raises ASTL's level | lines that do not express DUSP2 (23) vs lines expressing it (27) | 2.60× lower at baseline in the lines without DUSP2 | 0.017 | ⚠ within organs, on part of the lines; also absent: ASTL, HOXA11, KCNE3; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction 0.819). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.4, -1.1); signed map (6.5, 29.5). **Vector** length 54.8, 13.3% of its response variance represented; |z| ≥ 3 in 563 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.2 | +15.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +19.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +4.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.8 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +2.5 | +8.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +1.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.0 | +1.3 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -6.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.1 | -5.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -4.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.5 | -2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -2.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | dual specificity phosphatase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:96,143,169-96,145,440 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PAC-1 |
| Gene groups (HGNC) | MAP kinase phosphatases |
| Hallmark sets | MYC_TARGETS_V2, ESTROGEN_RESPONSE_LATE, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 5 pathways, smallest: RAF-independent MAPK1/3 activation; Negative regulation of MAPK pathway; RAF/MAP kinase cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [Q05923](https://www.uniprot.org/uniprotkb/Q05923) (Dual specificity protein phosphatase 2):

> Dephosphorylates both phosphorylated Thr and Tyr residues in MAPK1, and dephosphorylation of phosphotyrosine is slightly faster than that of phosphothreonine. Can dephosphorylate MAPK1 (By similarity).

**Summary**, from NCBI Gene [1844](https://www.ncbi.nlm.nih.gov/gene/1844):

> The protein encoded by this gene is a member of the dual specificity protein phosphatase subfamily. These phosphatases inactivate their target kinases by dephosphorylating both the phosphoserine/threonine and phosphotyrosine residues. They negatively regulate members of the mitogen-activated protein (MAP) kinase superfamily (MAPK/ERK, SAPK/JNK, p38), which are associated with cellular proliferation and differentiation. Different members of the family of dual specificity phosphatases show …

**Accessions** — [HGNC:3068](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3068) · Entrez [1844](https://www.ncbi.nlm.nih.gov/gene/1844) · UniProt [Q05923](https://www.uniprot.org/uniprotkb/Q05923) · Ensembl [ENSG00000158050](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158050)

## Data

Gene col 8126: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8126); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8126, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8126]; `tensor/DDL_lfc|DDL_z.npy` [8126]; `embed/gene_vectors.npy` [8126]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8126 or target_col == 8126). Every well: [[DUSP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUSP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
