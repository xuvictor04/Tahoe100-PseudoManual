---
symbol: "CDK16"
type: "gene"
col: 2228
ensembl_id: "ENSG00000102225"
name: "cyclin dependent kinase 16"
location: "Xp11.3"
module: 50
arm: "+"
pooled_cpm: 38.82
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 2
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# CDK16

*cyclin dependent kinase 16* — Xp11.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.33× (z +13.9, q 7e-41, up in 38 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.30× (z +4.3, q 0.003, up in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (HEC-1-A 4.33×, PANC-1 3.31×, NCI-H1573 3.70×, A498 2.54×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (HEC-1-A 3.87×, NCI-H1573 3.72×, PANC-1 2.54×, MIA PaCa-2 2.79×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 3.10×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.680× (z -6.3, q 2e-07, down in 33 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (MIA PaCa-2 0.219×, A-427 0.237×, C32 0.422×, SNU-1 0.282×, …); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.267×, C32 0.269×); [[Panobinostat (drug)]] 0.5 µM in 1 line (C32 0.235×; ⚠ cell-cycle shift, explains ~0% of this change); [[LJI308 (drug)]] 5 µM in 1 line (HCT15 0.0746×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FKBP9]] (+0.73, fdr 7e-06), [[PCNX3]] (+0.69, fdr 7e-06), [[SELENON]] (+0.69, fdr 7e-06); moves opposite to [[CROCCP2-1]] (-0.65, fdr 1e-05), [[SMIM26]] (-0.64, fdr 1e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[PIGBOS1]] (-0.61, fdr 1e-05), [[MRPS18C]] (-0.59, fdr 1e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CELSR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2228.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (HEC-1-A 4.33×, PANC-1 3.31×, NCI-H1573 3.70×, A498 2.54×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (HEC-1-A 3.87×, NCI-H1573 3.72×, PANC-1 2.54×, MIA PaCa-2 2.79×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 3.10×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.33×** | +13.9 | 7e-41 | 38/43 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +11.7 | 5e-29 | 35/39 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +7.9 | 4e-13 | 30/42 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.30×** | +4.3 | 0.003 | 23/48 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.30×** | +4.2 | 0.003 | 22/46 (HS-578T, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.44× | +3.1 | 0.17 | 13/41 (A498, SW 900, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2228.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (MIA PaCa-2 0.219×, A-427 0.237×, C32 0.422×, SNU-1 0.282×, …); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.267×, C32 0.269×); [[Panobinostat (drug)]] 0.5 µM in 1 line (C32 0.235×; ⚠ cell-cycle shift, explains ~0% of this change); [[LJI308 (drug)]] 5 µM in 1 line (HCT15 0.0746×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.680×** | -6.3 | 2e-07 | 33/48 (A-427, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.803×** | -5.1 | 1e-04 | 27/48 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ciclopirox (drug)]] 5 µM |  | 0.866× | -3.3 | 0.17 | 11/48 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | 0.871× | -3.2 | 0.17 | 12/48 (PANC-1, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.818× | -3.2 | 0.17 | 21/48 (C32, A-427, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.875× | -3.1 | 0.19 | 16/48 (AsPC-1, SW1417, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2228. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 92.2 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.235× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 61.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +15.7) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 77.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -20.8) |
| [[A-427 (line)]] | wt | 49.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -19.2) |
| [[A498 (line)]] | wt | 35.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 42.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +12.0) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 38.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.55× (z +9.4) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 42.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +13.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 35.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 37.7 | 0 | 1 | — | [[LJI308 (drug)]] 5 µM 0.0746× (z -8.6) |
| [[J82 (line)]] | alt | 46.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +9.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 51.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -8.7) |
| [[LoVo (line)]] | wt | 26.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +9.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 43.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +8.5) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 50.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 23.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -8.8) |
| [[SNU-423 (line)]] | alt | 48.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.77× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 52.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 41.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2228), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKBP9]] | +0.73 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[PCNX3]] | +0.69 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[SELENON]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[PRPF8]] | +0.69 | +0.56 / +0.75 | both halves | 1e-05 |  |
| [[NCSTN]] | +0.69 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[BAP1]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[BAG6]] | +0.68 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[AKT1]] | +0.68 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[ATP13A1]] | +0.68 | +0.47 / +0.76 | both halves | 2e-05 |  |
| [[SF3B4]] | +0.67 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[ADAM15]] | +0.67 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[ACADVL]] | +0.67 | +0.54 / +0.71 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP2-1]] | -0.65 | -0.56 / -0.67 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | -0.64 | -0.49 / -0.69 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PIGBOS1]] | -0.61 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[NSUN5P2-1]] ⚠ | -0.61 | -0.47 / -0.66 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPS18C]] | -0.59 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[PPIG]] | -0.59 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[NKAP]] | -0.58 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | -0.57 | -0.35 / -0.65 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[NACA4P]] ⚠ | -0.56 | -0.37 / -0.63 | both halves | 8e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SELENOH]] | -0.56 | -0.32 / -0.63 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CELSR2]] | B | CELSR2 activity raises CDK16's level | lines that do not express CELSR2 (9) vs lines expressing it (41) | 1.32× lower at baseline in the lines without CELSR2 | 0.062 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, CMTM8; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.723). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.4, -23.8); signed map (-16.0, -34.0). **Vector** length 104, 24.6% of its response variance represented; |z| ≥ 3 in 724 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.5 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.9 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.2 | +7.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +5.3 | +4.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.8 | +2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.5 | +1.2 |
|  | [[Folic acid (drug)]] 5 µM |  | +2.3 | +1.3 |
|  | [[Pentoxifylline (drug)]] 0.5 µM |  | +2.3 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.3 | -1.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.7 | -3.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | -2.2 | -2.7 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | -2.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.3 — chrX:47,217,860-47,229,997 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PCTAIRE, PCTAIRE1, PCTGAIRE, FLJ16665; previously PCTK1 |
| Gene groups (HGNC) | Cyclin dependent kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00536](https://www.uniprot.org/uniprotkb/Q00536) (Cyclin-dependent kinase 16):

> Protein kinase that plays a role in vesicle-mediated transport processes and exocytosis. Regulates GH1 release by brain neurons. Phosphorylates NSF, and thereby regulates NSF oligomerization. Required for normal spermatogenesis. Regulates neuron differentiation and dendrite development (By similarity). Plays a role in the regulation of insulin secretion in response to changes in blood glucose levels. Can phosphorylate CCNY at 'Ser-336' (in vitro).

**Summary**, from NCBI Gene [5127](https://www.ncbi.nlm.nih.gov/gene/5127):

> The protein encoded by this gene belongs to the cdc2/cdkx subfamily of the ser/thr family of protein kinases. It may play a role in signal transduction cascades in terminally differentiated cells; in exocytosis; and in transport of secretory cargo from the endoplasmic reticulum. This gene is thought to escape X inactivation. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Dec 2009]

**Accessions** — [HGNC:8749](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8749) · Entrez [5127](https://www.ncbi.nlm.nih.gov/gene/5127) · UniProt [Q00536](https://www.uniprot.org/uniprotkb/Q00536) · Ensembl [ENSG00000102225](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102225)

## Data

Gene col 2228: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2228); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2228, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2228]; `tensor/DDL_lfc|DDL_z.npy` [2228]; `embed/gene_vectors.npy` [2228]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2228 or target_col == 2228). Every well: [[CDK16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
