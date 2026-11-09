---
symbol: "LEMD2"
type: "gene"
col: 8458
ensembl_id: "ENSG00000161904"
name: "LEM domain nuclear envelope protein 2"
location: "6p21.31"
module: 7
arm: "+"
pooled_cpm: 25.79
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# LEMD2

*LEM domain nuclear envelope protein 2* — 6p21.31

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.471× (z -17.0, q 0e+00, down in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.682× (z -12.2, q 4e-32, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAPPC12]] (+0.59, fdr 3e-05), [[AP4E1]] (+0.58, fdr 2e-05), [[TRAPPC3]] (+0.58, fdr 2e-05); moves opposite to [[BZW2]] (-0.57, fdr 1e-05), [[TRA2A]] (-0.53, fdr 1e-05), [[NPTN]] (-0.48, fdr 2e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8458.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ferulic acid (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.41 | 9/47 (NCI-H2030, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.15× | +3.2 | 0.41 | 8/47 (SW480, KATO III, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.47 | 8/47 (NCI-H2030, J82, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8458.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.471×** | -17.0 | 0e+00 | 44/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.550×** | -13.5 | 5e-39 | 42/48 (KATO III, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.579×** | -12.3 | 1e-32 | 37/48 (SW480, J82, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.682×** | -12.2 | 4e-32 | 38/47 (A-172, H4, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.737×** | -9.7 | 2e-20 | 28/47 (SK-MEL-2, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.693×** | -7.7 | 2e-12 | 20/40 (LoVo, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.703×** | -7.6 | 2e-12 | 28/45 (RKO, HT-29, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.794×** | -7.4 | 1e-11 | 31/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.765×** | -5.8 | 4e-07 | 24/47 (RKO, H4, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.933× | -5.5 | 3e-06 | 2/48 (NCI-H2030, CHP-212) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.783×** | -5.3 | 6e-06 | 23/48 (J82, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.791×** | -5.3 | 6e-06 | 15/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.797×** | -5.1 | 1e-05 | 19/48 (SW 1088, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.814×** | -4.5 | 3e-04 | 18/48 (A-427, NCI-H23, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.686×** | -4.5 | 3e-04 | 14/48 (PANC-1, SNU-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 0.860× | -3.3 | 0.039 | 13/47 (AsPC-1, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8458. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 25.9 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.351× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[J82 (line)]] | alt | 29.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -11.5) |
| [[KATO III (line)]] | alt | 35.1 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.313× (z -10.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[LoVo (line)]] | wt | 21.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0921× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[AsPC-1 (line)]] | alt | 19.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 19.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SK-MEL-2 (line)]] | alt | 26.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -11.5) |
| [[SNU-1 (line)]] | wt | 19.0 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.156× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 34.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -10.0) |
| [[A498 (line)]] | wt | 24.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -9.1) |
| [[COLO 205 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change |
| [[H4 (line)]] | wt | 33.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -9.9) |
| [[HOP62 (line)]] | alt | 36.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 30.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -10.6) |
| [[LS 180 (line)]] | wt | 18.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0956× (z -18.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 19.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 32.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 37.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 27.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.213× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[RPMI-7951 (line)]] | alt | 28.8 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.151× (z -8.9) |
| [[SHP-77 (line)]] | alt | 23.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -9.6) |
| [[A-427 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8458), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC12]] | +0.59 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[AP4E1]] | +0.58 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[TRAPPC3]] | +0.58 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[ASXL2]] | +0.55 | +0.37 / +0.62 | both halves | 8e-05 |  |
| [[VPS4A]] | +0.54 | +0.48 / +0.50 | both halves | 2e-05 | pathway: Mitotic Anaphase; STRING 640 |
| [[NBPF20]] | +0.54 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[ZNF8]] | +0.53 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[ATMIN]] | +0.52 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[PRKAB1]] | +0.52 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[TTC4]] | +0.51 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[ZNF623]] | +0.51 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[SLC66A1]] | +0.51 | +0.31 / +0.51 | both halves | 2e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BZW2]] | -0.57 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[TRA2A]] | -0.53 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[NPTN]] | -0.48 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[KLHL15]] | -0.48 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[PTMA]] | -0.48 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[NUP62CL]] | -0.47 | -0.28 / -0.57 | both halves | 3e-04 |  |
| [[CDKL2]] | -0.47 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[FHIP1A]] | -0.47 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[TFG]] | -0.46 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[TEC]] | -0.45 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[EED]] | -0.44 | -0.29 / -0.57 | both halves | 2e-04 |  |
| [[H3-3A]] | -0.44 | -0.41 / -0.45 | both halves | 4e-05 | pathway: Mitotic Prophase |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises LEMD2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.477). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-14.5, 5.6); signed map (-4.8, -21.4). **Vector** length 62.5, 9.39% of its response variance represented; |z| ≥ 3 in 917 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.0 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +2.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | +1.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.8 | +1.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.0 | -5.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -2.5 |
|  | [[Allantoin (drug)]] 0.5 µM |  | -1.2 | -1.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | LEM domain nuclear envelope protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:33,771,202-33,789,130 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ482C21.1, NET25, LEM2 |
| Gene groups (HGNC) | LEM domain containing |
| Reactome | 11 pathways, smallest: Depolymerization of the Nuclear Lamina; Initiation of Nuclear Envelope (NE) Reformation; Sealing of the nuclear envelope (NE) by ESCRT-III |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NC56](https://www.uniprot.org/uniprotkb/Q8NC56) (LEM domain-containing protein 2):

> Nuclear lamina-associated inner nuclear membrane protein that is involved in nuclear structure organization, maintenance of nuclear envelope (NE) integrity and NE reformation after mitosis. Plays a role as transmembrane adapter for the endosomal sorting complexes required for transport (ESCRT), and is thereby involved in ESCRT-mediated NE reformation. Promotes ESCRT-mediated NE closure by recruiting CHMP7 and downstream ESCRT-III proteins IST1/CHMP8 and CHMP2A to the reforming NE during …

**Summary**, from NCBI Gene [221496](https://www.ncbi.nlm.nih.gov/gene/221496):

> This gene encodes a LEM domain-containing transmembrane protein of the inner nuclear membrane. The protein is involved in nuclear structure organization and plays a role in cell signaling and differentiation. Mutations in this gene result in Cataract 46, juvenile-onset. Multiple transcript variants have been found for this gene. [provided by RefSeq, Feb 2017]

**Accessions** — [HGNC:21244](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21244) · Entrez [221496](https://www.ncbi.nlm.nih.gov/gene/221496) · UniProt [Q8NC56](https://www.uniprot.org/uniprotkb/Q8NC56) · Ensembl [ENSG00000161904](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161904)

## Data

Gene col 8458: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8458); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8458, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8458]; `tensor/DDL_lfc|DDL_z.npy` [8458]; `embed/gene_vectors.npy` [8458]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8458 or target_col == 8458). Every well: [[LEMD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LEMD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
