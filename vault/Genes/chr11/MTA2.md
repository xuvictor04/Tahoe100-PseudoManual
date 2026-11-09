---
symbol: "MTA2"
type: "gene"
col: 7376
ensembl_id: "ENSG00000149480"
name: "metastasis associated 1 family member 2"
location: "11q12.3"
module: 126
arm: "+"
pooled_cpm: 23.43
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# MTA2

*metastasis associated 1 family member 2* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.14× (z +9.7, q 1e-19, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.726× (z -4.2, q 0.012, down in 25 of 47 measured lines) ⚠ unreliable plate only; position not correctable. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.826× (z -3.6, q 0.069, down in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H1573 0.167×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[U2AF2]] (+0.80, fdr 7e-06), [[SF3B4]] (+0.73, fdr 7e-06), [[PPP1R9B]] (+0.69, fdr 7e-06); moves opposite to [[RPL18]] (-0.66, fdr 1e-05, ⚠ RPL18 in the vector space only through flagged drug-doses), [[CAMLG]] (-0.66, fdr 1e-05), [[NACA4P]] (-0.62, fdr 2e-05, ⚠ NACA4P in the vector space only through flagged drug-doses), [[SNHG6]] (-0.62, fdr 1e-05), [[UBE2B]] (-0.61, fdr 1e-05).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7376.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.14×** | +9.7 | 1e-19 | 42/47 (HOP62, SW480, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.25×** | +9.6 | 2e-19 | 32/40 (A-427, SW480, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.06×** | +9.4 | 1e-18 | 44/48 (LS 180, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +9.2 | 3e-18 | 38/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.64×** | +8.9 | 5e-17 | 33/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +8.7 | 4e-16 | 41/47 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.86×** | +7.9 | 2e-13 | 30/42 (PANC-1, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.90×** | +7.9 | 2e-13 | 29/36 (KATO III, PANC-1, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.85×** | +7.8 | 3e-13 | 40/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.78×** | +7.4 | 9e-12 | 39/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +7.2 | 2e-11 | 36/48 (A549, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +7.2 | 4e-11 | 33/47 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.49×** | +6.1 | 4e-08 | 30/46 (LS 180, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +5.7 | 5e-07 | 31/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +5.6 | 9e-07 | 32/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +5.5 | 1e-06 | 30/47 (Panc 03.27, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +4.3 | 5e-04 | 26/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.019 | 19/47 (SW48, C32, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.022 | 17/48 (PANC-1, A549, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7376.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H1573 0.167×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.726×** | -4.2 | 0.012 | 25/47 (NCI-H2347, HepG2/C3A, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.732×** | -4.1 | 0.012 | 22/48 (HT-29, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.826×** | -3.6 | 0.069 | 18/48 (NCI-H2347, SW480, …) | rises with dose | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | 0.791× | -3.1 | 0.29 | 8/48 (Panc 03.27, SW 1088, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7376. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 21.8 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.6) | — |
| [[SW480 (line)]] | alt | 35.8 | 5 (3 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.03× (z +10.8) | — |
| [[NCI-H460 (line)]] | wt | 15.6 | 4 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.33× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.66× (z +9.5) | — |
| [[KATO III (line)]] | alt | 29.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.63× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LS 180 (line)]] | wt | 32.5 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.81× (z +9.9) | — |
| [[A-427 (line)]] | wt | 32.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.79× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 23.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +8.6) | — |
| [[A549 (line)]] | wt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 22.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.15× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LoVo (line)]] | wt | 18.0 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.69× (z +9.3) ⚠ toxic | — |
| [[NCI-H1573 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -9.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 34.2 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 6.83× (z +9.7) | — |
| [[A-172 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7376), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[U2AF2]] | +0.80 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[SF3B4]] | +0.73 | +0.62 / +0.71 | both halves | 7e-06 | pathway: ATP-dependent chromatin remodelers |
| [[PPP1R9B]] | +0.69 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[CCAR2]] | +0.69 | +0.54 / +0.76 | both halves | 1e-05 |  |
| [[ATP13A1]] | +0.68 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[INPPL1]] | +0.67 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[EME2]] | +0.67 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[STRN4]] | +0.66 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[CERS2]] | +0.66 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[SSU72]] | +0.66 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[ATN1]] | +0.65 | +0.48 / +0.58 | both halves | 2e-05 | pathway: Intracellular signaling by second messengers; STRING 592 |
| [[SRSF1]] | +0.65 | +0.58 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 8 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL18]] ⚠ | -0.66 | -0.49 / -0.65 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CAMLG]] | -0.66 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[NACA4P]] ⚠ | -0.62 | -0.48 / -0.64 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG6]] | -0.62 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[UBE2B]] | -0.61 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[RPL31]] | -0.60 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[RPL36]] | -0.60 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[RPL35A]] | -0.60 | -0.44 / -0.63 | both halves | 3e-05 |  |
| [[LAMTOR5]] | -0.59 | -0.47 / -0.53 | both halves | 2e-05 | pathway: Intracellular signaling by second messengers |
| [[ADGRL3-AS1]] | -0.59 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[TMEM256]] | -0.59 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[ATP5MJ]] | -0.58 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[IFI27L2]] | -0.58 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[ATP5MC2]] | -0.58 | -0.40 / -0.62 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MTA2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.811). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.1, -24.6); signed map (-12.4, -34.8). **Vector** length 89.5, 21.2% of its response variance represented; |z| ≥ 3 in 1,041 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +6.6 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +5.9 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.7 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +9.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +6.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +3.4 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | +2.3 | +2.2 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | -0.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | +0.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +1.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.0 | -0.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -3.1 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | metastasis associated 1 family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,593,214-62,601,865 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MTA1-L1; previously MTA1L1 |
| Gene groups (HGNC) | GATA zinc finger domain containing; Myb/SANT domain containing; NuRD complex subunits |
| Reactome | 31 pathways, smallest: Transcriptional regulation of brown and beige adipocyte differentiation; Transcriptional regulation of brown and beige adipocyte differentiation by EBF2; ERCC6 (CSB) and EHMT2 (G9a) positively regulate rRNA expression |
| Matched by | ensembl_id |

**Function**, from UniProt [O94776](https://www.uniprot.org/uniprotkb/O94776) (Metastasis-associated protein MTA2):

> May function as a transcriptional coregulator. Acts as a component of the histone deacetylase NuRD complex which participates in the remodeling of chromatin.

**Summary**, from NCBI Gene [9219](https://www.ncbi.nlm.nih.gov/gene/9219):

> This gene encodes a protein that has been identified as a component of NuRD, a nucleosome remodeling deacetylase complex identified in the nucleus of human cells. It shows a very broad expression pattern and is strongly expressed in many tissues. It may represent one member of a small gene family that encode different but related proteins involved either directly or indirectly in transcriptional regulation. Their indirect effects on transcriptional regulation may include chromatin remodeling. …

**Accessions** — [HGNC:7411](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7411) · Entrez [9219](https://www.ncbi.nlm.nih.gov/gene/9219) · UniProt [O94776](https://www.uniprot.org/uniprotkb/O94776) · Ensembl [ENSG00000149480](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149480)

## Data

Gene col 7376: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7376); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7376, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7376]; `tensor/DDL_lfc|DDL_z.npy` [7376]; `embed/gene_vectors.npy` [7376]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7376 or target_col == 7376). Every well: [[MTA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
