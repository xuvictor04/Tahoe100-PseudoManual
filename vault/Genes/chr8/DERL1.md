---
symbol: "DERL1"
type: "gene"
col: 5953
ensembl_id: "ENSG00000136986"
name: "derlin 1"
location: "8q24.13"
module: 56
arm: "+"
pooled_cpm: 65.02
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 18
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# DERL1

*derlin 1* — 8q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.35× (z +8.6, q 3e-15, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.614× (z -13.3, q 2e-37, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAR1A]] (+0.71, fdr 7e-06), [[GOLT1B]] (+0.70, fdr 7e-06), [[SEC61A1]] (+0.69, fdr 7e-06); moves opposite to [[TNFRSF12A]] (-0.59, fdr 1e-05), [[IGF2BP2]] (-0.55, fdr 5e-05), [[ZC3H7B]] (-0.55, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5953.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.35×** | +8.6 | 3e-15 | 43/49 (C32, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.99×** | +7.0 | 9e-10 | 35/48 (C32, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +4.5 | 0.001 | 22/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.7 | 0.025 | 19/45 (NCI-H1573, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.20×** | +3.4 | 0.075 | 18/48 (HT-29, COLO 205, …) | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.20× | +3.3 | 0.082 | 10/48 (SW1417, A498, …) | rises with dose | plate-row cell shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.3 | 0.082 | 17/48 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.25× | +3.1 | 0.12 | 9/48 (LoVo, NCI-H2030, …) | two highest doses | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.12× | +3.1 | 0.12 | 1/48 (MIA PaCa-2) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5953.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.614×** | -13.3 | 2e-37 | 41/48 (AsPC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.509×** | -13.0 | 4e-36 | 43/48 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.545×** | -11.7 | 3e-29 | 41/48 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.539×** | -11.5 | 3e-28 | 44/48 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.569×** | -10.9 | 2e-25 | 39/48 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.647×** | -8.4 | 5e-15 | 36/48 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.686×** | -7.3 | 3e-11 | 35/48 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.698×** | -6.6 | 2e-09 | 24/40 (SK-MEL-2, HT-29, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.717×** | -6.4 | 1e-08 | 32/48 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.718×** | -6.4 | 1e-08 | 34/48 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.726×** | -6.2 | 4e-08 | 32/48 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.775×** | -4.7 | 1e-04 | 27/48 (A498, H4, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.637×** | -4.5 | 3e-04 | 28/48 (A498, SNU-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.863× | -4.0 | 0.003 | 15/48 (A498, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **0.814×** | -3.8 | 0.006 | 21/46 (SW 900, H4, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.823×** | -3.7 | 0.007 | 15/48 (CFPAC-1, COLO 205, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.824×** | -3.6 | 0.011 | 17/48 (NCI-H2347, J82, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.825×** | -3.4 | 0.020 | 16/47 (A-172, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5953. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 158 | 0 | 12 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -19.5) |
| [[AsPC-1 (line)]] | alt | 102 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -18.5) |
| [[A-172 (line)]] | wt | 41.0 | 0 | 6 | — | [[Belinostat (drug)]] 5 µM 0.289× (z -12.4) |
| [[KATO III (line)]] | alt | 74.6 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.304× (z -12.1) |
| [[HT-29 (line)]] | alt | 138 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.415× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 113 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -13.1) |
| [[H4 (line)]] | wt | 77.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -10.0) |
| [[HS-578T (line)]] | alt | 160 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -14.0) |
| [[RKO (line)]] | wt | 75.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.433× (z -9.2) |
| [[HOP62 (line)]] | alt | 64.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.436× (z -9.6) |
| [[Hs 766T (line)]] | wt | 78.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 48.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.398× (z -8.5) |
| [[BT-474 (line)]] | alt | 50.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.337× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 37.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.46× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[C32 (line)]] | wt | 57.4 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 12.1× (z +10.5) | — |
| [[CHP-212 (line)]] | wt | 43.7 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 5 µM 0.269× (z -9.0) |
| [[COLO 205 (line)]] | alt | 76.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 65.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 55.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 78.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -9.4) |
| [[SHP-77 (line)]] | alt | 59.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[SNU-423 (line)]] | alt | 48.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.334× (z -9.2) |
| [[SW 900 (line)]] | alt | 75.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -11.2) |
| [[A-427 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 56.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 98.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 38.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5953), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAR1A]] | +0.71 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[GOLT1B]] | +0.70 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[SEC61A1]] | +0.69 | +0.77 / +0.69 | both halves | 7e-06 | STRING 909 |
| [[ALKBH5]] | +0.69 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[TMEM39A]] | +0.69 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[NUS1]] | +0.68 | +0.80 / +0.63 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[CDC26]] | +0.67 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[COPA]] | +0.67 | +0.77 / +0.63 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[IER3IP1]] | +0.66 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.66 | +0.76 / +0.61 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[TM9SF2]] | +0.66 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.65 | +0.80 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFRSF12A]] | -0.59 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[IGF2BP2]] | -0.55 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[ZC3H7B]] | -0.55 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[CMTR2]] | -0.54 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[EXOC6]] | -0.54 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[SLK]] | -0.53 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[TGIF2]] | -0.53 | -0.59 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers DERL1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.618). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.3, -31.6); signed map (-50.0, 9.0). **Vector** length 101, 26.7% of its response variance represented; |z| ≥ 3 in 1,003 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ER to Golgi Anterograde Transport* (reactome, mean cos +0.51 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.51 to 16); *COPII-mediated vesicle transport* (reactome, mean cos +0.55 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.2 | -0.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.9 | +8.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +7.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | -1.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | +3.0 | +3.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.7 | +2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.2 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | -0.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.4 | -11.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.9 | -8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | -13.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.5 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -6.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -3.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.9 | -3.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.6 | -3.7 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -2.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | derlin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.13 — chr8:123,013,170-123,042,302 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3067, PRO2577, FLJ13784, DER1, DER-1, derlin-1 |
| Gene groups (HGNC) | Rhomboid family |
| Reactome | 15 pathways, smallest: N-glycan trimming in the ER and Calnexin/Calreticulin cycle; Defective CFTR causes cystic fibrosis; E3 ubiquitin ligases ubiquitinate target proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUN8](https://www.uniprot.org/uniprotkb/Q9BUN8) (Derlin-1):

> Functional component of endoplasmic reticulum-associated degradation (ERAD) for misfolded lumenal proteins. Forms homotetramers which encircle a large channel traversing the endoplasmic reticulum (ER) membrane. This allows the retrotranslocation of misfolded proteins from the ER into the cytosol where they are ubiquitinated and degraded by the proteasome. The channel has a lateral gate within the membrane which provides direct access to membrane proteins with no need to reenter the ER lumen …

**Summary**, from NCBI Gene [79139](https://www.ncbi.nlm.nih.gov/gene/79139):

> The protein encoded by this gene is a member of the derlin family. Members of this family participate in the ER-associated degradation response and retrotranslocate misfolded or unfolded proteins from the ER lumen to the cytosol for proteasomal degradation. This protein recognizes substrate in the ER and works in a complex to retrotranslocate it across the ER membrane into the cytosol. This protein may select cystic fibrosis transmembrane conductance regulator protein (CFTR) for degradation as …

**Accessions** — [HGNC:28454](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28454) · Entrez [79139](https://www.ncbi.nlm.nih.gov/gene/79139) · UniProt [Q9BUN8](https://www.uniprot.org/uniprotkb/Q9BUN8) · Ensembl [ENSG00000136986](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136986)

## Data

Gene col 5953: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5953); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5953, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5953]; `tensor/DDL_lfc|DDL_z.npy` [5953]; `embed/gene_vectors.npy` [5953]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5953 or target_col == 5953). Every well: [[DERL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DERL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
