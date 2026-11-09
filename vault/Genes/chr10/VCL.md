---
symbol: "VCL"
type: "gene"
col: 428
ensembl_id: "ENSG00000035403"
name: "vinculin"
location: "10q22.2"
module: 111
arm: "+"
pooled_cpm: 594.47
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 26
n_dd_up_clean: 6
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# VCL

*vinculin* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.68× (z +5.5, q 2e-05, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.479× (z -7.5, q 4e-11, down in 43 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.503× (z -7.3, q 1e-10, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPM4]] (+0.65, fdr 1e-05), [[PDLIM5]] (+0.63, fdr 1e-05), [[MAP3K14]] (+0.61, fdr 1e-05); moves opposite to [[ASB7]] (-0.59, fdr 1e-05), [[GOT1-DT]] (-0.57, fdr 3e-05), [[ELMOD3]] (-0.55, fdr 2e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MYO1E]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 428.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.68×** | +5.5 | 2e-05 | 34/47 (RKO, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +4.8 | 4e-04 | 39/47 (SK-MEL-2, AN3 CA, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.48×** | +4.1 | 0.007 | 37/47 (NCI-H1792, J82, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.017 | 25/47 (RKO, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +3.8 | 0.017 | 30/47 (RKO, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Busulfan (drug)]] 0.05 µM |  | **1.38×** | +3.4 | 0.067 | 36/48 (SW 900, J82, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.35× | +3.1 | 0.14 | 32/48 (SK-MEL-2, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 428.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.479×** | -7.5 | 4e-11 | 43/46 (SNU-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.503×** | -7.3 | 1e-10 | 42/47 (HT-29, SNU-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.590×** | -5.6 | 4e-06 | 39/47 (HepG2/C3A, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.697×** | -5.4 | 8e-06 | 36/48 (SNU-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.605×** | -5.0 | 5e-05 | 40/47 (HepG2/C3A, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.638×** | -4.8 | 2e-04 | 40/47 (HepG2/C3A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.735×** | -4.6 | 3e-04 | 35/47 (SW480, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.446×** | -4.5 | 5e-04 | 37/48 (NCI-H1792, HepG2/C3A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.659×** | -4.4 | 6e-04 | 39/47 (MIA PaCa-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.654×** | -4.3 | 8e-04 | 32/46 (HepG2/C3A, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **0.768×** | -4.0 | 0.004 | 37/47 (A549, HEC-1-A, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | **0.770×** | -3.9 | 0.004 | 33/47 (RPMI-7951, A-172, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.691×** | -3.9 | 0.004 | 32/47 (HepG2/C3A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.695×** | -3.9 | 0.004 | 28/47 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.690×** | -3.8 | 0.006 | 36/48 (HepG2/C3A, COLO 205, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.701×** | -3.8 | 0.006 | 34/47 (HepG2/C3A, HT-29, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.704×** | -3.7 | 0.006 | 38/47 (HT-29, A-172, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.709×** | -3.7 | 0.008 | 30/47 (NCI-H1573, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 428. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 1,941 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -15.0) |
| [[HepG2_C3A (line)]] | wt | 787 | 0 | 9 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.215× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 218 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.83× (z +12.3) | — |
| [[RKO (line)]] | wt | 320 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +16.5) | — |
| [[KATO III (line)]] | alt | 219 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.90× (z +12.2) | — |
| [[A498 (line)]] | wt | 686 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -9.6) |
| [[CHP-212 (line)]] | wt | 962 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 711 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 501 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.317× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.320× (z -9.0) |
| [[A549 (line)]] | wt | 821 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -11.3) |
| [[AsPC-1 (line)]] | alt | 682 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.389× (z -9.0) |
| [[C-33 A (line)]] | alt | 599 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 473 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.6) | — |
| [[HT-29 (line)]] | alt | 594 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.264× (z -11.2) |
| [[LoVo (line)]] | wt | 639 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.283× (z -10.0) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 539 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.386× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 418 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.289× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 514 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.68× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 543 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.1) | — |
| [[PANC-1 (line)]] | alt | 1,391 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -9.2) |
| [[SW480 (line)]] | alt | 729 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.535× (z -8.5) |
| [[A-172 (line)]] | wt | 462 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 281 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 538 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 388 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 432 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 684 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 492 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 419 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 637 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 566 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 466 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 553 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 404 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 653 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 486 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 369 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 354 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 479 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 413 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 514 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 435 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 141 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 894 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 661 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 398 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 719 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 542 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 619 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 428), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPM4]] | +0.65 | +0.57 / +0.56 | both halves | 1e-05 | pathway: Muscle contraction; STRING 711 |
| [[PDLIM5]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 508 |
| [[MAP3K14]] | +0.61 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[WDR1]] | +0.60 | +0.64 / +0.60 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation; STRING 654 |
| [[COTL1]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[RALY]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[CCN2]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[EGR3]] | +0.58 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[MYH9]] | +0.57 | +0.49 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_APICAL_JUNCTION; STRING 638 |
| [[EGR2]] | +0.57 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[NUP98]] | +0.57 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[LMCD1]] | +0.55 | +0.48 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASB7]] | -0.59 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[GOT1-DT]] | -0.57 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[ELMOD3]] | -0.55 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[VPS13B-DT]] | -0.55 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[TMEM68]] | -0.55 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[MAFIP]] | -0.55 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[FHIP2A]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[MORN4]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[LRRC37B]] | -0.53 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[RWDD3]] | -0.53 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[CAPN10-DT]] | -0.53 | -0.37 / -0.54 | both halves | 9e-05 |  |
| [[ZNF343]] | -0.52 | -0.49 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO1E]] | B | MYO1E activity raises VCL's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 1.88× lower at baseline in the lines without MYO1E | 0.028 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers VCL's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[NCEH1]] | B | NCEH1 activity raises VCL's level | lines that do not express NCEH1 (6) vs lines expressing it (44) | 1.43× lower at baseline in the lines without NCEH1 | 0.086 | ⚠ within organs, on part of the lines; also absent: KCNK6, SMCO2; maybe low, not absent |
| [[EGR3]] | B | EGR3 activity raises VCL's level | lines that do not express EGR3 (9) vs lines expressing it (41) | 1.59× lower at baseline in the lines without EGR3 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000261026 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.1, 26.6); signed map (-8.1, 36.0). **Vector** length 154, 59.0% of its response variance represented; |z| ≥ 3 in 1,272 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Sensory processing of sound by inner hair cells of the cochlea* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.7 | +2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.3 | +3.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.7 | +5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +3.8 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | +4.5 | +2.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +4.5 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +4.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +4.1 | +2.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +4.0 | +2.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.7 | -7.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.6 | -4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -7.4 | -3.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -6.4 | -3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.2 | -7.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -5.4 | -3.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -5.2 | -2.7 |
|  | [[Terfenadine (drug)]] 5 µM |  | -4.9 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | vinculin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.2 — chr10:73,995,193-74,121,363 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VINC |
| Hallmark sets | APICAL_JUNCTION, MITOTIC_SPINDLE |
| Reactome | 37 pathways, smallest: Turbulent (oscillatory, disturbed) flow shear stress activates signaling by PIEZO1 and integrins in endothelial cells; Signaling by high-kinase activity BRAF mutants; Smooth Muscle Contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [P18206](https://www.uniprot.org/uniprotkb/P18206) (Vinculin):

> Actin filament (F-actin)-binding protein involved in cell-matrix adhesion and cell-cell adhesion. Regulates cell-surface E-cadherin expression and potentiates mechanosensing by the E-cadherin complex. May also play important roles in cell morphology and locomotion.

**Summary**, from NCBI Gene [7414](https://www.ncbi.nlm.nih.gov/gene/7414):

> Vinculin is a cytoskeletal protein associated with cell-cell and cell-matrix junctions, where it is thought to function as one of several interacting proteins involved in anchoring F-actin to the membrane. Defects in VCL are the cause of cardiomyopathy dilated type 1W. Dilated cardiomyopathy is a disorder characterized by ventricular dilation and impaired systolic function, resulting in congestive heart failure and arrhythmia. Multiple alternatively spliced transcript variants have been found …

**Accessions** — [HGNC:12665](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12665) · Entrez [7414](https://www.ncbi.nlm.nih.gov/gene/7414) · UniProt [P18206](https://www.uniprot.org/uniprotkb/P18206) · Ensembl [ENSG00000035403](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000035403)

## Data

Gene col 428: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 428); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 428, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 428]; `tensor/DDL_lfc|DDL_z.npy` [428]; `embed/gene_vectors.npy` [428]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 428 or target_col == 428). Every well: [[VCL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VCL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
