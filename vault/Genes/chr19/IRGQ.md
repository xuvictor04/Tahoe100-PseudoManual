---
symbol: "IRGQ"
type: "gene"
col: 9459
ensembl_id: "ENSG00000167378"
name: "immunity related GTPase Q"
location: "19q13.31"
module: 157
arm: "+"
pooled_cpm: 13.8
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 5
n_dd_up_clean: 23
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# IRGQ

*immunity related GTPase Q* — 19q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (15 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.33× (z +15.5, q 0e+00, up in 40 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 0.05 µM: 0.704× (z -4.6, q 0.003, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RHBDF1]] (+0.59, fdr 1e-05), [[BCL2L2]] (+0.56, fdr 2e-05), [[PCBP4]] (+0.56, fdr 1e-05); moves opposite to [[SHPRH]] (-0.54, fdr 3e-05), [[ACBD6]] (-0.53, fdr 2e-05), [[SRRM1]] (-0.50, fdr 3e-05).
> It is in [[Module 157]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9459.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +15.5 | 0e+00 | 40/44 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.56×** | +12.1 | 3e-31 | 41/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.30×** | +10.7 | 1e-24 | 42/48 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +9.6 | 7e-20 | 30/47 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.11×** | +9.6 | 7e-20 | 41/47 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +9.4 | 4e-19 | 37/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.97×** | +8.8 | 2e-16 | 36/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.86×** | +8.0 | 1e-13 | 33/47 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.82×** | +7.7 | 6e-13 | 33/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.81×** | +7.6 | 1e-12 | 36/47 (HS-578T, HCT15, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +7.0 | 1e-10 | 30/48 (A-172, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.65×** | +6.2 | 3e-08 | 27/41 (HT-29, SNU-1, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.63×** | +6.1 | 6e-08 | 26/46 (HS-578T, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.63×** | +5.8 | 2e-07 | 19/31 (LoVo, MIA PaCa-2, …) | all doses, flat | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +5.7 | 4e-07 | 25/42 (NCI-H23, C32, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.36×** | +5.6 | 9e-07 | 27/48 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.1 | 1e-05 | 19/48 (HOP62, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.50×** | +5.0 | 2e-05 | 22/46 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +5.0 | 2e-05 | 22/46 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.44×** | +4.7 | 7e-05 | 19/45 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +3.9 | 0.003 | 16/48 (HEC-1-A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9459.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.704×** | -4.6 | 0.003 | 22/47 (SW 1271, A498, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.731×** | -4.1 | 0.013 | 15/47 (COLO 205, AsPC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **0.754×** | -3.7 | 0.037 | 10/48 (SW 1088, LS 180, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.584×** | -3.6 | 0.037 | 17/43 (NCI-H460, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~23% here); noisy plate (z scaled); position effect removed |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.759×** | -3.6 | 0.037 | 12/47 (SW 900, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9459. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 12.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -10.2) |
| [[HOP62 (line)]] | alt | 14.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +10.5) | — |
| [[A498 (line)]] | wt | 18.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +13.8) | — |
| [[AsPC-1 (line)]] | alt | 15.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +11.7) | — |
| [[CFPAC-1 (line)]] | alt | 9.46 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 15.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +12.0) | — |
| [[J82 (line)]] | alt | 16.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +8.5) | — |
| [[KATO III (line)]] | alt | 10.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 15.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.22× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 18.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +12.0) | — |
| [[NCI-H460 (line)]] | wt | 10.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.47× (z +9.6) | — |
| [[PANC-1 (line)]] | alt | 6.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +10.7) | — |
| [[RPMI-7951 (line)]] | alt | 16.9 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.146× (z -9.0) |
| [[SW480 (line)]] | alt | 17.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +9.0) | — |
| [[A-172 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.01 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9459), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHBDF1]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[BCL2L2]] | +0.56 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[PCBP4]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[LENG8]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[GSK3A]] | +0.55 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[NDST2]] | +0.54 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[STXBP2]] | +0.52 | +0.40 / +0.50 | both halves | 4e-05 |  |
| [[EME2]] | +0.52 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[LYPLA2]] | +0.52 | +0.48 / +0.40 | both halves | 5e-05 |  |
| [[DHRS11]] | +0.51 | +0.42 / +0.34 | both halves | 1e-04 |  |
| [[SLC9A3-AS1]] | +0.51 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[POMGNT1]] | +0.51 | +0.40 / +0.51 | both halves | 5e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHPRH]] | -0.54 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[ACBD6]] | -0.53 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[SRRM1]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[PIK3R1]] | -0.50 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[ZMYND8]] | -0.50 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[CCDC6]] | -0.50 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[RFC1]] | -0.49 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[GPATCH11]] | -0.49 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[NUDT12]] | -0.48 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[AGGF1]] | -0.48 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[KBTBD7]] | -0.48 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[IMMT]] | -0.47 | -0.31 / -0.38 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers IRGQ's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SRC]] | B | SRC activity raises IRGQ's level | compounds that target SRC: 2 of 3 lower it (NG25, Ponatinib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.560). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.2, -21.5); signed map (2.5, 3.0). **Vector** length 74.4, 14.4% of its response variance represented; |z| ≥ 3 in 1,089 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +15.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.9 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +3.8 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | +3.7 | +3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | +3.5 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +7.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.7 | +4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +5.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.1 | +3.9 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -4.4 | -0.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | +1.1 |
|  | [[NG25 (drug)]] 5 µM |  | -2.5 | -3.6 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -2.1 | -3.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.0 | -0.3 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | -2.0 | -3.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.8 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | immunity related GTPase Q |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.31 — chr19:43,584,367-43,596,134 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FKSG27; previously IRGQ1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WZA9](https://www.uniprot.org/uniprotkb/Q8WZA9) (Immunity-related GTPase family Q protein):

> Autophagy receptor that specifically promotes clearance of misfolded MHC class I molecules by targeting them to the lysosome for degradation. Acts as a molecular adapter that specifically recognizes and binds (1) misfolded MHC class I molecules following their ubiquitination, as well as (2) autophagy-related proteins, promoting the recruitment of misfolded MHC class I molecules to autophagy machinery for degradation. Degradation of misfolded MHC class I molecules is essential to prevent …

**Summary**, from NCBI Gene [126298](https://www.ncbi.nlm.nih.gov/gene/126298):

> Enables protein-macromolecule adaptor activity. Involved in positive regulation of autophagy; protein quality control for misfolded or incompletely synthesized proteins; and substrate localization to autophagosome. Is active in autophagosome and lysosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24868](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24868) · Entrez [126298](https://www.ncbi.nlm.nih.gov/gene/126298) · UniProt [Q8WZA9](https://www.uniprot.org/uniprotkb/Q8WZA9) · Ensembl [ENSG00000167378](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167378)

## Data

Gene col 9459: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9459); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9459, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9459]; `tensor/DDL_lfc|DDL_z.npy` [9459]; `embed/gene_vectors.npy` [9459]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9459 or target_col == 9459). Every well: [[IRGQ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IRGQ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
