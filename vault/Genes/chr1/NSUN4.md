---
symbol: "NSUN4"
type: "gene"
col: 3916
ensembl_id: "ENSG00000117481"
name: "NOP2/Sun RNA methyltransferase 4"
location: "1p33"
module: 156
arm: "+"
pooled_cpm: 28.93
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 14
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/156"]
generated_by: "tahoemap"
---

# NSUN4

*NOP2/Sun RNA methyltransferase 4* — 1p33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.14× (z +10.0, q 9e-21, up in 6 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 1.37× (z +3.6, q 0.061, up in 7 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.611× (z -15.3, q 0e+00, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPP14]] (+0.67, fdr 1e-05), [[METTL2A]] (+0.64, fdr 7e-06), [[PSMD5]] (+0.63, fdr 1e-05); moves opposite to [[YWHAZ]] (-0.60, fdr 1e-05), [[EPB41L2]] (-0.57, fdr 1e-05), [[NPTN]] (-0.57, fdr 1e-05).
> It is in [[Module 156]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3916.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +10.0 | 9e-21 | 6/48 (PANC-1, J82, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +5.9 | 8e-07 | 20/48 (NCI-H2347, SW480, …) | inconsistent across doses | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.061 | 7/48 (NCI-H460, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.16× | +3.2 | 0.22 | 11/48 (COLO 205, SK-MEL-2, …) | inconsistent across doses |  |
| [[Oxaprozin (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.27 | 6/47 (SNU-1, HepG2/C3A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3916.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.611×** | -15.3 | 0e+00 | 38/47 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.526×** | -14.1 | 8e-43 | 35/44 (NCI-H23, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.552×** | -13.0 | 1e-36 | 42/47 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.557×** | -12.8 | 2e-35 | 38/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.564×** | -12.1 | 2e-31 | 26/34 (A-172, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.590×** | -11.1 | 9e-27 | 36/47 (SK-MEL-2, H4, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.598×** | -10.4 | 1e-23 | 28/40 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.633×** | -10.0 | 7e-22 | 37/48 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.641×** | -9.8 | 1e-20 | 37/48 (A498, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.640×** | -9.4 | 3e-19 | 33/48 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.710×** | -7.5 | 3e-12 | 30/47 (CHP-212, A549, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.806×** | -6.7 | 1e-09 | 23/48 (A498, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.839× | -5.4 | 2e-06 | 21/48 (HOP62, A-427, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.700×** | -4.1 | 0.002 | 11/48 (MIA PaCa-2, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | 0.857× | -3.4 | 0.025 | 11/48 (SHP-77, SW480, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.849× | -3.4 | 0.025 | 12/47 (RKO, A498, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.874× | -2.9 | 0.096 | 0/48 | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3916. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 47.4 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -14.4) |
| [[NCI-H460 (line)]] | wt | 27.4 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.352× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -9.4) |
| [[PANC-1 (line)]] | alt | 39.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.362× (z -12.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 40.9 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 39.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.368× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 29.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -13.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 42.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.191× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -9.3) |
| [[SW48 (line)]] | wt | 37.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0765× (z -14.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 36.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.445× (z -10.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 21.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -17.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 28.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -9.1) |
| [[A549 (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -11.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 31.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -8.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -8.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 44.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -13.9) |
| [[HepG2_C3A (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -11.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 31.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -8.5) |
| [[HT-29 (line)]] | alt | 26.6 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -9.5) |
| [[LoVo (line)]] | wt | 25.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 36.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0913× (z -10.7) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.302× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 36.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 27.0 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -12.1) |
| [[AN3 CA (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3916), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP14]] | +0.67 | +0.53 / +0.71 | both halves | 1e-05 | pathway: rRNA processing |
| [[METTL2A]] | +0.64 | +0.60 / +0.66 | both halves | 7e-06 | same gene group |
| [[PSMD5]] | +0.63 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[SETDB1]] | +0.62 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[TTC4]] | +0.62 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[ZC3HC1]] | +0.61 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[LSM7]] | +0.61 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[SDHAF2]] | +0.61 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[THUMPD2]] | +0.61 | +0.47 / +0.60 | both halves | 2e-05 | same gene group |
| [[BMS1P4]] | +0.61 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[ECSIT]] | +0.60 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[ESF1]] | +0.59 | +0.39 / +0.63 | both halves | 6e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YWHAZ]] | -0.60 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[EPB41L2]] | -0.57 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[NPTN]] | -0.57 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[PKM]] | -0.56 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[TWSG1]] | -0.56 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[ITM2C]] | -0.54 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[IDS]] | -0.54 | -0.36 / -0.56 | both halves | 9e-05 |  |
| [[TMEM30A]] | -0.54 | -0.38 / -0.57 | both halves | 7e-05 |  |
| [[APLP2]] | -0.54 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[BSG]] | -0.54 | -0.36 / -0.56 | both halves | 9e-05 |  |
| [[SPTBN1]] | -0.53 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[CFL1]] | -0.52 | -0.46 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NSUN4's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TMSB4X]] | B | TMSB4X activity lowers NSUN4's level | lines that do not express TMSB4X (9) vs lines expressing it (41) | 1.25× higher at baseline in the lines without TMSB4X | 0.083 | ⚠ within organs, on part of the lines; also absent: PRSS23, TCN2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 156]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.686). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.7, -1.9); signed map (-6.2, -15.0). **Vector** length 84.7, 16.8% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.7 | +2.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +5.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | +3.1 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +1.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +2.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.9 | +2.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.6 | +2.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.2 | +2.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.2 | +1.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.2 | +3.6 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.5 | -14.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -2.5 | -10.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.5 | -9.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.4 | -11.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -5.4 |
|  | [[crizotinib (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -2.0 | -2.5 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -2.0 | -1.9 |
|  | [[Artemether (drug)]] 0.05 µM |  | -1.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | NOP2/Sun RNA methyltransferase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p33 — chr1:46,340,789-46,365,152 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC22960, SHTAP |
| Gene groups (HGNC) | NOP2/Sun RNA methyltransferase family; DNA/RNA methyltransferases |
| Reactome | 4 pathways, smallest: rRNA modification in the mitochondrion; rRNA processing in the mitochondrion; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CB9](https://www.uniprot.org/uniprotkb/Q96CB9) (5-cytosine rRNA methyltransferase NSUN4):

> Mitochondrial RNA cytosine C(5)-methyltransferase that methylates cytosine to 5-methylcytosine (m5C) in various RNAs, such as rRNAs, mRNAs and some long non-coding RNAs (lncRNAs). Involved in mitochondrial ribosome small subunit (mt-SSU) maturation by catalyzing methylation of mitochondrial 12S rRNA; the function is independent of MTERF4 and assembled mitochondrial ribosome large subunit (mt-LSU). Targeted to mt-LSU by MTERF4 and probably is involved in a final step in ribosome biogenesis to …

**Summary**, from NCBI Gene [387338](https://www.ncbi.nlm.nih.gov/gene/387338):

> Enables mRNA (cytidine-5-)-methyltransferase activity; mitochondrial ribosomal large subunit rRNA binding activity; and rRNA (cytosine-C5-)-methyltransferase activity. Involved in RNA metabolic process and mitochondrial large ribosomal subunit assembly. Located in mitochondrial matrix. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:31802](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31802) · Entrez [387338](https://www.ncbi.nlm.nih.gov/gene/387338) · UniProt [Q96CB9](https://www.uniprot.org/uniprotkb/Q96CB9) · Ensembl [ENSG00000117481](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117481)

## Data

Gene col 3916: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3916); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3916, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3916]; `tensor/DDL_lfc|DDL_z.npy` [3916]; `embed/gene_vectors.npy` [3916]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3916 or target_col == 3916). Every well: [[NSUN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSUN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
