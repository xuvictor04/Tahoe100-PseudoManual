---
symbol: "FURIN"
type: "gene"
col: 6433
ensembl_id: "ENSG00000140564"
name: "furin, paired basic amino acid cleaving enzyme"
location: "15q26.1"
module: 92
arm: "+"
pooled_cpm: 16.31
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# FURIN

*furin, paired basic amino acid cleaving enzyme* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.66× (z +8.4, q 3e-14, up in 32 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.618× (z -5.7, q 9e-06, down in 23 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Verteporfin (drug)]] 5 µM: 0.669× (z -4.5, q 0.002, down in 24 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC42EP2]] (+0.59, fdr 1e-05), [[SPRY4]] (+0.57, fdr 1e-05), [[PNP]] (+0.57, fdr 1e-05); moves opposite to [[ATP5MC2]] (-0.50, fdr 4e-05), [[EMC2]] (-0.47, fdr 3e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FES]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6433.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +8.4 | 3e-14 | 32/43 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +6.8 | 3e-09 | 21/36 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +4.9 | 2e-04 | 21/47 (SW480, KATO III, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +4.8 | 2e-04 | 18/34 (CFPAC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.4 | 0.001 | 20/43 (LS 180, A498, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +4.3 | 0.001 | 19/42 (A498, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.012 | 17/43 (LS 180, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +3.4 | 0.048 | 8/31 (HepG2/C3A, A549, …) | top dose only | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.45× | +3.1 | 0.14 | 7/45 (Panc 03.27, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6433.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.618×** | -5.7 | 9e-06 | 23/46 (SHP-77, NCI-H460, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.669×** | -4.5 | 0.002 | 24/46 (RKO, HepG2/C3A, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.688×** | -4.4 | 0.002 | 21/46 (SHP-77, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.511×** | -4.1 | 0.005 | 17/44 (NCI-H1792, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.731×** | -3.7 | 0.022 | 16/47 (HEC-1-A, SW 1271, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.722×** | -3.7 | 0.022 | 21/46 (NCI-H23, NCI-H1573, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.739×** | -3.6 | 0.028 | 13/46 (A-172, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.562×** | -3.5 | 0.028 | 15/39 (SW 900, PANC-1, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.767×** | -3.4 | 0.044 | 16/47 (NCI-H1573, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.752×** | -3.4 | 0.044 | 17/47 (NCI-H1573, C32, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | **0.827×** | -3.2 | 0.077 | 15/47 (C32, NCI-H460, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.819× | -3.0 | 0.10 | 13/46 (SK-MEL-2, NCI-H1573, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.761× | -3.0 | 0.10 | 18/45 (NCI-H1573, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6433. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 72.7 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.183× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 55.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -14.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.241× (z -10.1) |
| [[SHP-77 (line)]] | alt | 48.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.152× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 29.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.206× (z -9.7) |
| [[H4 (line)]] | wt | 14.4 | 0 | 1 | — | [[Docetaxel (Trihydrate) (drug)]] 5 µM 0.0325× (z -11.8) |
| [[HT-29 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -9.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 14.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +11.3) | — |
| [[LS 180 (line)]] | wt | 14.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 15.1 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.87× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 19.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.57 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6433), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC42EP2]] | +0.59 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[SPRY4]] | +0.57 | +0.58 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[PNP]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[NT5E]] | +0.56 | +0.54 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[HCG20]] | +0.56 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[FOXP4]] | +0.55 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[TRIM8]] | +0.55 | +0.53 / +0.53 | both halves | 1e-05 | pathway: Interferon Signaling |
| [[RHBDF1]] | +0.54 | +0.52 / +0.52 | both halves | 1e-05 | STRING 416 |
| [[PICART1]] | +0.54 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[SPRED2]] | +0.54 | +0.50 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[ETV4]] | +0.54 | +0.54 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[ANGPTL2]] | +0.53 | +0.55 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5MC2]] | -0.50 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[EMC2]] | -0.47 | -0.43 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FES]] | B | FES activity raises FURIN's level | lines that do not express FES (11) vs lines expressing it (39) | 2.24× lower at baseline in the lines without FES | 0.014 | ⚠ within organs, on part of the lines; also absent: RBPMS, GLRX, SEMA4A; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers FURIN's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FLT1]] | B | FLT1 activity raises FURIN's level | lines that do not express FLT1 (28) vs lines expressing it (22) | 1.48× lower at baseline in the lines without FLT1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ZNF365, COL19A1, PDGFRB |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.7, 7.1); signed map (7.8, 46.4). **Vector** length 93.4, 19.4% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +8.1 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.9 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.0 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +4.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.9 | +2.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.9 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +2.0 |
| fall | [[Trametinib (drug)]] 5 µM |  | -4.3 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.9 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.2 | -3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.2 | -2.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.0 | -2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | furin, paired basic amino acid cleaving enzyme |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:90,868,588-90,883,564 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPC1; previously PCSK3, FUR, PACE |
| Gene groups (HGNC) | Proprotein convertase subtilisin/kexin family |
| Hallmark sets | TGF_BETA_SIGNALING, COAGULATION, UV_RESPONSE_UP, IL2_STAT5_SIGNALING |
| Reactome | 68 pathways, smallest: Expression and Processing of Neurotrophins; NGF processing; Removal of aminoterminal propeptides from gamma-carboxylated proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P09958](https://www.uniprot.org/uniprotkb/P09958) (Furin):

> Ubiquitous endoprotease within constitutive secretory pathways capable of cleavage at the RX(K/R)R consensus motif. Mediates processing of TGFB1, an essential step in TGF-beta-1 activation. Converts through proteolytic cleavage the non-functional Brain natriuretic factor prohormone into its active hormone BNP(1-32). By mediating processing of accessory subunit ATP6AP1/Ac45 of the V-ATPase, regulates the acidification of dense-core secretory granules in islets of Langerhans cells (By …

**Summary**, from NCBI Gene [5045](https://www.ncbi.nlm.nih.gov/gene/5045):

> This gene encodes a member of the subtilisin-like proprotein convertase family, which includes proteases that process protein and peptide precursors trafficking through regulated or constitutive branches of the secretory pathway. It encodes a type 1 membrane bound protease that is expressed in many tissues, including neuroendocrine, liver, gut, and brain. The encoded protein undergoes an initial autocatalytic processing event in the ER and then sorts to the trans-Golgi network through endosomes …

**Accessions** — [HGNC:8568](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8568) · Entrez [5045](https://www.ncbi.nlm.nih.gov/gene/5045) · UniProt [P09958](https://www.uniprot.org/uniprotkb/P09958) · Ensembl [ENSG00000140564](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140564)

## Data

Gene col 6433: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6433); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6433, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6433]; `tensor/DDL_lfc|DDL_z.npy` [6433]; `embed/gene_vectors.npy` [6433]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6433 or target_col == 6433). Every well: [[FURIN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FURIN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
