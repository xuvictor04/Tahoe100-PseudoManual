---
symbol: "POMGNT1"
type: "gene"
col: 1448
ensembl_id: "ENSG00000085998"
name: "protein O-linked mannose N-acetylglucosaminyltransferase 1 (beta 1,2-)"
location: "1p34.1"
module: 50
arm: "+"
pooled_cpm: 17.63
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 11
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# POMGNT1

*protein O-linked mannose N-acetylglucosaminyltransferase 1 (beta 1,2-)* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.07× (z +12.7, q 4e-34, up in 22 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.26× (z +5.8, q 8e-07, up in 24 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 3.79×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 3.61×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.515× (z -17.1, q 0e+00, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SELENON]] (+0.73, fdr 7e-06), [[MAN2C1]] (+0.67, fdr 7e-06), [[CTSZ]] (+0.66, fdr 7e-06); moves opposite to [[PIGBOS1]] (-0.63, fdr 1e-05), [[CEP350]] (-0.62, fdr 8e-06), [[PPIG]] (-0.61, fdr 1e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1448.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 3.79×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 3.61×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +12.7 | 4e-34 | 22/29 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.96×** | +12.2 | 8e-32 | 35/41 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +7.0 | 5e-10 | 21/35 (SK-MEL-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +5.8 | 8e-07 | 24/47 (NCI-H1792, A498, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.8 | 0.020 | 1/48 (HCT15) | inconsistent across doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.19 | 8/47 (J82, NCI-H23, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1448.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.515×** | -17.1 | 0e+00 | 36/47 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.563×** | -10.5 | 3e-23 | 33/47 (MIA PaCa-2, H4, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.632×** | -8.1 | 1e-13 | 31/47 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.700×** | -6.5 | 9e-09 | 25/48 (RKO, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.708×** | -6.3 | 3e-08 | 26/48 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.742×** | -5.5 | 4e-06 | 20/48 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.752×** | -5.2 | 1e-05 | 23/48 (RKO, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.761×** | -5.0 | 4e-05 | 20/47 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Adagrasib (drug)]] 5 µM |  | **0.802×** | -3.9 | 0.006 | 9/48 (AN3 CA, NCI-H23, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.803×** | -3.9 | 0.006 | 15/47 (AsPC-1, SW 900, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.863× | -3.8 | 0.006 | 18/48 (HOP62, KATO III, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.865× | -3.5 | 0.024 | 12/47 (MIA PaCa-2, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.879× | -3.3 | 0.040 | 8/48 (MIA PaCa-2, SW1417, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.828×** | -3.3 | 0.040 | 12/47 (AN3 CA, SW 1271, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 0.842× | -3.2 | 0.059 | 12/48 (NCI-H2030, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1448. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 17.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -12.6) |
| [[PANC-1 (line)]] | alt | 27.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -17.6) |
| [[A-427 (line)]] | wt | 21.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.194× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 17.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 23.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.187× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 13.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -9.6) |
| [[A549 (line)]] | wt | 14.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -12.3) |
| [[BT-474 (line)]] | alt | 9.85 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.175× (z -8.6) |
| [[C32 (line)]] | wt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -9.2) |
| [[H4 (line)]] | wt | 19.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0846× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.112× (z -8.9) ⚠ cell-cycle shift, explains ~2% of this change |
| [[HOP62 (line)]] | alt | 23.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -12.1) |
| [[Hs 766T (line)]] | wt | 29.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -9.9) |
| [[J82 (line)]] | alt | 13.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -11.7) |
| [[LoVo (line)]] | wt | 13.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.61× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 14.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.155× (z -11.4) |
| [[LS 180 (line)]] | wt | 18.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 17.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 34.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -9.8) |
| [[SNU-1 (line)]] | wt | 23.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -9.7) |
| [[A-172 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1448), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENON]] | +0.73 | +0.69 / +0.72 | both halves | 7e-06 | STRING 432 |
| [[MAN2C1]] | +0.67 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[CTSZ]] | +0.66 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[AKT1]] | +0.66 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[CHID1]] | +0.66 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[CERS2]] | +0.64 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[MAN2B2]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[CNPY3]] | +0.62 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[PLBD2]] | +0.62 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[BCAP31]] | +0.62 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[SLC41A3]] | +0.61 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[EMC1]] | +0.61 | +0.57 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGBOS1]] | -0.63 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[CEP350]] | -0.62 | -0.59 / -0.58 | both halves | 8e-06 |  |
| [[PPIG]] | -0.61 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[ATF4]] | -0.60 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[MTRFR]] | -0.59 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[PNRC1]] | -0.58 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[ZMYM5]] | -0.58 | -0.70 / -0.45 | both halves | 3e-05 |  |
| [[CCDC174]] | -0.58 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[MED19]] | -0.58 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[ANKHD1]] | -0.57 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[SUMO4]] | -0.57 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[GGNBP2]] | -0.57 | -0.56 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises POMGNT1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.653). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.6, -26.3); signed map (-24.8, -43.3). **Vector** length 73.1, 12.3% of its response variance represented; |z| ≥ 3 in 841 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +12.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.8 | +5.8 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.6 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +0.4 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +1.5 | +1.4 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | -2.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.7 | -10.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.1 | -17.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.9 | -8.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.6 | -5.0 |
|  | [[Adagrasib (drug)]] 5 µM |  | -2.0 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | protein O-linked mannose N-acetylglucosaminyltransferase 1 (beta 1,2-) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:46,188,683-46,220,305 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20277, MGAT1.2, LGMD2O; previously MEB |
| Gene groups (HGNC) | O-linked N-acetylglucosaminyltransferases |
| Reactome | 8 pathways, smallest: DAG1 core M1 glycosylations; DAG1 core M2 glycosylations; Matriglycan biosynthesis on DAG1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WZA1](https://www.uniprot.org/uniprotkb/Q8WZA1) (Protein O-linked-mannose beta-1,2-N-acetylglucosaminyltransferase 1):

> Participates in O-mannosyl glycosylation by catalyzing the addition of N-acetylglucosamine to O-linked mannose on glycoproteins. Catalyzes the synthesis of the GlcNAc(beta1-2)Man(alpha1-)O-Ser/Thr moiety on alpha-dystroglycan and other O-mannosylated proteins, providing the necessary basis for the addition of further carbohydrate moieties. Is specific for alpha linked terminal mannose and does not have MGAT3, MGAT4, MGAT5, MGAT7 or MGAT8 activity.

**Summary**, from NCBI Gene [55624](https://www.ncbi.nlm.nih.gov/gene/55624):

> This gene encodes a type II transmembrane protein that resides in the Golgi apparatus. It participates in O-mannosyl glycosylation and is specific for alpha linked terminal mannose. Mutations in this gene may be associated with muscle-eye-brain disease and several congenital muscular dystrophies. Alternatively spliced transcript variants that encode different protein isoforms have been described. [provided by RefSeq, Feb 2014]

**Accessions** — [HGNC:19139](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19139) · Entrez [55624](https://www.ncbi.nlm.nih.gov/gene/55624) · UniProt [Q8WZA1](https://www.uniprot.org/uniprotkb/Q8WZA1) · Ensembl [ENSG00000085998](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085998)

## Data

Gene col 1448: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1448); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1448, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1448]; `tensor/DDL_lfc|DDL_z.npy` [1448]; `embed/gene_vectors.npy` [1448]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1448 or target_col == 1448). Every well: [[POMGNT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POMGNT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
