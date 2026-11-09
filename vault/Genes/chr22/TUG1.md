---
symbol: "TUG1"
type: "gene"
col: 14798
ensembl_id: "ENSG00000253352"
name: "taurine up-regulated 1"
location: "22q12.2"
module: 3
arm: "-"
pooled_cpm: 68.38
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# TUG1

*taurine up-regulated 1* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +9.1, q 4e-17, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.727× (z -4.6, q 0.002, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF4G2]] (+0.82, fdr 7e-06), [[C6orf120]] (+0.78, fdr 7e-06), [[PURB]] (+0.76, fdr 7e-06); moves opposite to [[ATP5MJ]] (-0.75, fdr 1e-05), [[RPP21]] (-0.73, fdr 7e-06), [[CAMLG]] (-0.72, fdr 7e-06).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14798.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +9.1 | 4e-17 | 39/49 (AsPC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +8.5 | 7e-15 | 41/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +7.4 | 3e-11 | 39/48 (NCI-H2347, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +7.0 | 3e-10 | 32/43 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +6.0 | 3e-07 | 35/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.15×** | +5.7 | 1e-06 | 35/49 (LoVo, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.6 | 2e-06 | 29/48 (HS-578T, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.5 | 2e-06 | 35/48 (SW1417, Hs 766T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +4.7 | 2e-04 | 26/49 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +4.2 | 0.001 | 27/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.36×** | +4.1 | 0.002 | 26/45 (C32, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +4.0 | 0.003 | 31/48 (AsPC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +3.8 | 0.008 | 26/48 (KATO III, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.038 | 24/48 (NCI-H2347, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.054 | 21/50 (AsPC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14798.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.727×** | -4.6 | 0.002 | 31/48 (A-427, J82, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.654×** | -4.4 | 0.003 | 32/48 (SW480, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.781×** | -3.6 | 0.066 | 25/48 (BT-474, J82, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.775×** | -3.5 | 0.069 | 23/48 (A549, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 0.5 µM |  | 0.726× | -3.3 | 0.11 | 21/48 (HS-578T, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.801× | -3.2 | 0.12 | 24/48 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.857× | -3.2 | 0.12 | 17/48 (HCT15, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14798. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 53.4 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +12.5) | — |
| [[Hs 766T (line)]] | wt | 48.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +10.3) | — |
| [[NCI-H23 (line)]] | alt | 82.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 63.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +15.3) | — |
| [[A-172 (line)]] | wt | 62.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 75.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 51.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 59.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +11.4) | — |
| [[KATO III (line)]] | alt | 106 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +10.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 82.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 49.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 66.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +15.0) | — |
| [[NCI-H2347 (line)]] | alt | 47.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.74× (z +10.0) | — |
| [[NCI-H661 (line)]] | alt | 71.9 | 0 | 1 | — | [[PH-797804 (drug)]] 0.5 µM 0.0605× (z -8.6) |
| [[RKO (line)]] | wt | 49.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +9.3) | — |
| [[SW 1271 (line)]] | alt | 78.2 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.124× (z -8.5) |
| [[SW1417 (line)]] | alt | 104 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.7) | — |
| [[A-427 (line)]] | wt | 46.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 73.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 67.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 65.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 93.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 68.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 71.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 57.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 78.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14798), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | +0.82 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[C6orf120]] | +0.78 | +0.81 / +0.64 | both halves | 7e-06 |  |
| [[PURB]] | +0.76 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[ZNF655]] | +0.74 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[TASOR]] | +0.71 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[LINC00667]] | +0.71 | +0.72 / +0.47 | both halves | 2e-05 |  |
| [[HNRNPK]] | +0.71 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[TRIP12]] | +0.70 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[SSU72]] | +0.70 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[DDX6]] | +0.70 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[MAPRE1]] | +0.69 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[NXT2]] | +0.69 | +0.62 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5MJ]] | -0.75 | -0.54 / -0.72 | both halves | 1e-05 |  |
| [[RPP21]] | -0.73 | -0.60 / -0.68 | both halves | 7e-06 |  |
| [[CAMLG]] | -0.72 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[DPY30]] | -0.72 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[LCMT1]] | -0.70 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[NBPF3]] | -0.69 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[LAMTOR5]] | -0.69 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[SCAI]] | -0.69 | -0.70 / -0.54 | both halves | 1e-05 |  |
| [[AFMID]] | -0.68 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[POLR2I]] | -0.68 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[RAC3]] | -0.68 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[HEATR5B]] | -0.67 | -0.55 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TUG1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises TUG1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LNC-LBCS]] | B | LNC-LBCS activity weakens TUG1's drug response | lines that do not express LNC-LBCS (13) vs lines expressing it (36) | the lines without LNC-LBCS respond 1.39× as strongly (z diff -0.91); strongest at Idarubicin (hydrochloride) 5 µM: 1.83x vs 1.42x (z diff -2.4) | 0.097 | ⚠ within organs, on part of the lines; also absent: ANKS1B, TERT, SAMD11; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.737). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (0.9, -12.3); signed map (17.6, -32.3). **Vector** length 125, 34.5% of its response variance represented; |z| ≥ 3 in 845 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mRNA 3'-end processing* (reactome, mean cos +0.50 to 12); *mRNA Polyadenylation* (reactome, mean cos +0.51 to 11); *Dengue Virus-Host Interactions* (reactome, mean cos +0.54 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.8 | +7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.4 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.1 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.7 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.5 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +3.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.0 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +2.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -6.4 | -4.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.2 | -3.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.7 | -3.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -1.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.1 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.8 | -2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.1 | -4.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | taurine up-regulated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:30,969,245-30,979,395 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20618, NCRNA00080, LINC00080 |
| Matched by | ensembl_id |

UniProt [A0A6I8PU40](https://www.uniprot.org/uniprotkb/A0A6I8PU40) carries no function annotation.

**Summary**, from NCBI Gene [55000](https://www.ncbi.nlm.nih.gov/gene/55000):

> Predicted to enable cis-regulatory region sequence-specific DNA binding activity. Predicted to act upstream of or within several processes, including mitochondrion organization; photoreceptor cell development; and spermatogenesis. Predicted to be located in nucleus. Biomarker of Huntington's disease. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26066](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26066) · Entrez [55000](https://www.ncbi.nlm.nih.gov/gene/55000) · UniProt [A0A6I8PU40](https://www.uniprot.org/uniprotkb/A0A6I8PU40) · Ensembl [ENSG00000253352](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253352)

## Data

Gene col 14798: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14798); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14798, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14798]; `tensor/DDL_lfc|DDL_z.npy` [14798]; `embed/gene_vectors.npy` [14798]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14798 or target_col == 14798). Every well: [[TUG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
