---
symbol: "MORF4L2"
type: "gene"
col: 4443
ensembl_id: "ENSG00000123562"
name: "mortality factor 4 like 2"
location: "Xq22.2"
module: 56
arm: "+"
pooled_cpm: 395.25
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# MORF4L2

*mortality factor 4 like 2* — Xq22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.33× (z +5.0, q 4e-04, up in 34 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.29× (z +4.7, q 6e-04, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.742× (z -5.4, q 3e-05, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM263]] (+0.70, fdr 7e-06), [[PGM3]] (+0.70, fdr 7e-06), [[COPB1]] (+0.68, fdr 7e-06); moves opposite to [[EMC8]] (-0.59, fdr 1e-05), [[URB2]] (-0.58, fdr 1e-05), [[ZNF746]] (-0.55, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Bendamustine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4443.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +5.0 | 4e-04 | 34/47 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.29×** | +4.7 | 6e-04 | 33/48 (NCI-H460, PANC-1, …) | inconsistent across doses | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +4.7 | 6e-04 | 32/48 (SNU-423, SK-MEL-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +4.6 | 6e-04 | 33/48 (HEC-1-A, SK-MEL-2, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.25×** | +4.0 | 0.006 | 28/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.033 | 22/48 (HEC-1-A, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.033 | 24/48 (HEC-1-A, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.45×** | +3.5 | 0.033 | 32/48 (SW1417, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.049 | 23/50 (SK-MEL-2, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.14× | +3.3 | 0.049 | 22/48 (AsPC-1, A498, …) | top dose only | composition shift |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.049 | 25/48 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.10 | 20/48 (A-172, PANC-1, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4443.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.742×** | -5.4 | 3e-05 | 35/48 (CFPAC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.762×** | -4.9 | 2e-04 | 35/48 (hTERT-HPNE, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.784×** | -4.4 | 0.002 | 35/48 (CFPAC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.813×** | -3.8 | 0.024 | 26/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.818×** | -3.6 | 0.026 | 26/48 (NCI-H2030, AsPC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.813×** | -3.6 | 0.026 | 27/48 (LoVo, SW480, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.820×** | -3.6 | 0.026 | 26/48 (HepG2/C3A, NCI-H460, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.822×** | -3.5 | 0.028 | 26/48 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.828×** | -3.3 | 0.062 | 24/48 (AsPC-1, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4443. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 487 | 9 (8 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.21× (z +16.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Gefitinib (drug)]] 5 µM 1.86× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 621 | 3 (3 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +11.2) ⚠ cell-cycle shift, explains ~39% of this change | [[Belinostat (drug)]] 5 µM 0.621× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 457 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +10.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 1.84× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.456× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 482 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +19.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AsPC-1 (line)]] | alt | 523 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +20.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CFPAC-1 (line)]] | alt | 393 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.489× (z -10.4) |
| [[COLO 205 (line)]] | alt | 406 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.84× (z +10.0) ⚠ toxic | — |
| [[hTERT-HPNE (line)]] | wt | 366 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.451× (z -9.7) |
| [[RKO (line)]] | wt | 251 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.11× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.391× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 636 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +12.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.08× (z +10.4) | — |
| [[A549 (line)]] | wt | 432 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HCT15 (line)]] | alt | 480 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.476× (z -8.6) |
| [[Hs 766T (line)]] | wt | 482 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 329 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 460 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.553× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 620 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.504× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 312 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.54× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 342 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.529× (z -8.6) |
| [[A-172 (line)]] | wt | 190 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 286 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 193 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 207 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 223 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 313 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 560 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 239 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 206 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 472 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 292 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 401 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 439 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 480 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 344 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 285 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 329 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 456 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 321 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 330 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 382 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 306 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 281 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 532 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 272 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 324 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 349 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 223 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 452 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4443), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM263]] | +0.70 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[PGM3]] | +0.70 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[COPB1]] | +0.68 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[SEC31A]] | +0.68 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[COPB2]] | +0.68 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[SRP54]] | +0.67 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[EAF2]] | +0.67 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[SUCO]] | +0.67 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[ARF4]] | +0.67 | +0.70 / +0.66 | both halves | 7e-06 | STRING 485 |
| [[TBC1D8B]] | +0.66 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[SPTY2D1]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[GTF2B]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMC8]] | -0.59 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[URB2]] | -0.58 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[ZNF746]] | -0.55 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[GFM1]] | -0.55 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[SCO1]] | -0.55 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[MCAT]] | -0.55 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[TGFBRAP1]] | -0.55 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[NADK]] | -0.54 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[NUP42]] | -0.54 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[ZNF239]] | -0.53 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[UTP4]] | -0.53 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[UBE2F]] | -0.53 | -0.45 / -0.60 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises MORF4L2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Bendamustine (drug)]] 0.5 µM | C | MORF4L2's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | MORF4L2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.63 | 0.417 over the table, 0.085 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.657). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.0, -35.9); signed map (-51.2, 13.1). **Vector** length 128, 47.3% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.53 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.56 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.56 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.7 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.1 | +4.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.3 | +2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.7 | +0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +3.5 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -4.9 | +1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -4.8 | +1.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | -4.5 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.5 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | +2.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.2 | -2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | mortality factor 4 like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.2 — chrX:103,675,496-103,688,158 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0026, MRGX |
| Gene groups (HGNC) | EMSY complex |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15014](https://www.uniprot.org/uniprotkb/Q15014) (Mortality factor 4-like protein 2):

> Component of the NuA4 histone acetyltransferase complex which is involved in transcriptional activation of select genes principally by acetylation of nucleosomal histone H4 and H2A. This modification may both alter nucleosome - DNA interactions and promote interaction of the modified histones with other proteins which positively regulate transcription. This complex may be required for the activation of transcriptional programs associated with oncogene and proto-oncogene mediated growth …

**Summary**, from NCBI Gene [9643](https://www.ncbi.nlm.nih.gov/gene/9643):

> Involved in positive regulation of double-strand break repair via homologous recombination and regulation of cell cycle. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16849](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16849) · Entrez [9643](https://www.ncbi.nlm.nih.gov/gene/9643) · UniProt [Q15014](https://www.uniprot.org/uniprotkb/Q15014) · Ensembl [ENSG00000123562](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123562)

## Data

Gene col 4443: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4443); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4443, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4443]; `tensor/DDL_lfc|DDL_z.npy` [4443]; `embed/gene_vectors.npy` [4443]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4443 or target_col == 4443). Every well: [[MORF4L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MORF4L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
