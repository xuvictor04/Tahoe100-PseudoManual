---
symbol: "GOLGA8B"
type: "gene"
col: 13256
ensembl_id: "ENSG00000215252"
name: "golgin A8 family member B"
location: "15q14"
module: 21
arm: "+"
pooled_cpm: 30.38
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# GOLGA8B

*golgin A8 family member B* — 15q14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.30× (z +16.3, q 0e+00, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.917× (z -4.3, q 0.009, down in 2 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[Fenofibrate (drug)]] 0.05 µM: 0.761× (z -3.7, q 0.053, down in 13 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1792 0.199×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.05 µM in 1 line (AN3 CA 0.126×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLGA8A]] (+0.83, fdr 7e-06), [[CCNL2]] (+0.60, fdr 1e-05), [[PLCG1-AS1]] (+0.57, fdr 2e-05); moves opposite to [[H2AX]] (-0.60, fdr 2e-05), [[SLC39A3]] (-0.57, fdr 6e-05), [[CBR1]] (-0.57, fdr 4e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13256.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.30×** | +16.3 | 0e+00 | 43/46 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.37×** | +12.8 | 2e-35 | 38/43 (HEC-1-A, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +9.2 | 5e-18 | 30/36 (AsPC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +9.1 | 1e-17 | 32/40 (HEC-1-A, SW480, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +8.8 | 1e-16 | 40/46 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +8.7 | 2e-16 | 38/47 (LS 180, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.76×** | +4.8 | 1e-04 | 24/45 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.009 | 20/47 (LOX-IMVI, J82, …) | rises with dose | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.55×** | +3.7 | 0.012 | 15/47 (SK-MEL-2, NCI-H1573, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.50×** | +3.5 | 0.031 | 15/47 (PANC-1, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.077 | 11/47 (HT-29, hTERT-HPNE, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.077 | 10/47 (AsPC-1, SW 1088, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.44×** | +3.1 | 0.081 | 7/47 (A498, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.17× | +3.0 | 0.10 | 20/46 (hTERT-HPNE, C32, …) | top dose only | composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13256.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1792 0.199×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.05 µM in 1 line (AN3 CA 0.126×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.917× | -4.3 | 0.009 | 2/47 (COLO 205, CHP-212) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.761×** | -3.7 | 0.053 | 13/46 (SW 900, HEC-1-A, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.769× | -3.4 | 0.12 | 16/47 (NCI-H460, MIA PaCa-2, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.672× | -3.1 | 0.29 | 7/46 (MIA PaCa-2, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13256. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 33.1 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 28.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +10.8) | — |
| [[HOP62 (line)]] | alt | 29.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +11.7) | — |
| [[LS 180 (line)]] | wt | 21.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +10.2) | — |
| [[A-172 (line)]] | wt | 20.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +11.0) | — |
| [[A498 (line)]] | wt | 18.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +13.3) | — |
| [[A549 (line)]] | wt | 23.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 40.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.126× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 26.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 26.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +9.3) | — |
| [[J82 (line)]] | alt | 39.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +8.6) | — |
| [[KATO III (line)]] | alt | 21.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 25.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 36.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 47.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +10.1) | — |
| [[NCI-H2347 (line)]] | alt | 12.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +10.5) | — |
| [[NCI-H460 (line)]] | wt | 27.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +10.4) | — |
| [[RPMI-7951 (line)]] | alt | 28.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +10.8) | — |
| [[SW480 (line)]] | alt | 29.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.67 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13256), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGA8A]] | +0.83 | +0.73 / +0.84 | both halves | 7e-06 | same gene group; STRING 543 |
| [[CCNL2]] | +0.60 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[PLCG1-AS1]] | +0.57 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[AP4S1]] | +0.57 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[HOXB-AS3]] | +0.56 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[CCNO-DT]] | +0.56 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[GCC2-AS1]] | +0.55 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[HOXB-AS1]] | +0.55 | +0.36 / +0.52 | both halves | 1e-04 |  |
| [[C2CD5-AS1]] | +0.55 | +0.49 / +0.40 | both halves | 4e-05 |  |
| [[TICAM2-AS1]] | +0.54 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[INSYN2A]] | +0.54 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[KPNB1-DT]] | +0.54 | +0.47 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[H2AX]] | -0.60 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[SLC39A3]] | -0.57 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[CBR1]] | -0.57 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[ECHS1]] | -0.55 | -0.47 / -0.44 | both halves | 3e-05 | same gene group |
| [[DPM2]] | -0.52 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[ATP5MC3]] ⚠ | -0.52 | -0.42 / -0.44 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZFP1]] | -0.50 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[CLTC]] | -0.50 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[ZNF445]] | -0.49 | -0.24 / -0.36 | both halves | 4e-04 |  |
| [[TUBB]] | -0.49 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[ALDOA]] | -0.48 | -0.47 / -0.32 | both halves | 1e-04 |  |
| [[KAT7]] | -0.48 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[DNAJB1]] | -0.48 | -0.36 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GOLGA8B's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HOXB-AS1]] | B | HOXB-AS1 activity raises GOLGA8B's level | lines that do not express HOXB-AS1 (14) vs lines expressing it (36) | 1.30× lower at baseline in the lines without HOXB-AS1 | 0.096 | ⚠ within organs, on part of the lines; also absent: MAP1A, HOXB2, ADAMTS18 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.512). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.0, 26.6); signed map (32.9, 1.6). **Vector** length 80.0, 17.3% of its response variance represented; |z| ≥ 3 in 632 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +16.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +8.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +12.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.2 | +1.5 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.2 | +3.5 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.9 | +3.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -1.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.2 | -4.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.9 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | +1.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.5 | -3.4 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.4 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | golgin A8 family member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q14 — chr15:34,525,095-34,588,503 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Golgin A6 and A8 families |
| Matched by | ensembl_id |

**Function**, from UniProt [A8MQT2](https://www.uniprot.org/uniprotkb/A8MQT2) (Golgin subfamily A member 8B):

> May be involved in maintaining Golgi structure.

**Summary**, from NCBI Gene [440270](https://www.ncbi.nlm.nih.gov/gene/440270):

> Predicted to be involved in Golgi organization. Predicted to be located in Golgi apparatus. Predicted to be active in Golgi cis cisterna; Golgi cisterna membrane; and cis-Golgi network. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:31973](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31973) · Entrez [440270](https://www.ncbi.nlm.nih.gov/gene/440270) · UniProt [A8MQT2](https://www.uniprot.org/uniprotkb/A8MQT2) · Ensembl [ENSG00000215252](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215252)

## Data

Gene col 13256: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13256); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13256, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13256]; `tensor/DDL_lfc|DDL_z.npy` [13256]; `embed/gene_vectors.npy` [13256]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13256 or target_col == 13256). Every well: [[GOLGA8B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOLGA8B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
