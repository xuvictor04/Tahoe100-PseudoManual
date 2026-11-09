---
symbol: "PLXNA1"
type: "gene"
col: 3565
ensembl_id: "ENSG00000114554"
name: "plexin A1"
location: "3q21.3"
module: 78
arm: "+"
pooled_cpm: 34.44
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# PLXNA1

*plexin A1* — 3q21.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 3.51×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change); [[Budesonide (drug)]] 0.5 µM in 1 line (AsPC-1 4.28×).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.591× (z -9.4, q 2e-18, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACOT7]] (+0.69, fdr 7e-06), [[MICAL2]] (+0.66, fdr 7e-06), [[ACTN1]] (+0.65, fdr 7e-06); moves opposite to [[NAA38]] (-0.59, fdr 1e-05), [[PIGP]] (-0.58, fdr 2e-05), [[MITD1]] (-0.58, fdr 2e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[WT1-AS]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 3.51×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change); [[Budesonide (drug)]] 0.5 µM in 1 line (AsPC-1 4.28×).

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3565.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.591×** | -9.4 | 2e-18 | 35/47 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.563×** | -7.0 | 7e-10 | 34/48 (Panc 03.27, A-427, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.859× | -6.6 | 7e-09 | 14/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.600×** | -6.5 | 1e-08 | 26/47 (PANC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.429×** | -5.6 | 2e-06 | 33/48 (NCI-H23, MIA PaCa-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.680×** | -4.7 | 2e-04 | 24/48 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.540×** | -4.1 | 0.004 | 23/47 (A-427, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.722×** | -3.8 | 0.011 | 19/48 (SW 900, MIA PaCa-2, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.766×** | -3.4 | 0.048 | 18/48 (HOP62, SNU-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.800×** | -3.3 | 0.063 | 20/48 (MIA PaCa-2, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.794×** | -3.2 | 0.077 | 19/48 (MIA PaCa-2, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.781×** | -3.1 | 0.077 | 13/48 (SW1417, NCI-H2030, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.814×** | -3.1 | 0.077 | 19/48 (MIA PaCa-2, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.786×** | -3.0 | 0.095 | 18/48 (HS-578T, HOP62, …) | rises with dose |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.788×** | -3.0 | 0.096 | 11/48 (NCI-H460, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3565. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 184 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0828× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 69.7 | 0 | 6 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.367× (z -24.5) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.130× (z -20.0) |
| [[A-427 (line)]] | wt | 32.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.05 µM 3.51× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 43.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -13.5) |
| [[PANC-1 (line)]] | alt | 53.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -15.5) |
| [[HOP62 (line)]] | alt | 46.8 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.539× (z -14.2) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.245× (z -12.8) |
| [[HS-578T (line)]] | alt | 84.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.244× (z -9.5) |
| [[SW48 (line)]] | wt | 41.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 17.7 | 1 | 0 | [[Budesonide (drug)]] 0.5 µM 4.28× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 38.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.356× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 43.7 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.473× (z -14.0) ⚠ position not correctable |
| [[NCI-H2030 (line)]] | alt | 20.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -9.9) |
| [[SW1417 (line)]] | alt | 29.7 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.233× (z -10.3) |
| [[A-172 (line)]] | wt | 58.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 29.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3565), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACOT7]] | +0.69 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[MICAL2]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[ACTN1]] | +0.65 | +0.66 / +0.58 | both halves | 7e-06 | pathway: RHOD GTPase cycle; STRING 419 |
| [[PODXL]] | +0.64 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[VAV2]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[SPRY4]] | +0.63 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[HPCAL1]] | +0.63 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[PXN]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[ITPR3]] | +0.62 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[KCNC4]] | +0.61 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[APEH]] | +0.61 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[GATAD2A]] | +0.61 | +0.65 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA38]] | -0.59 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[PIGP]] | -0.58 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[MITD1]] | -0.58 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[RAB9A]] | -0.56 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[CIR1]] | -0.56 | -0.64 / -0.46 | both halves | 3e-05 |  |
| [[ATP5MC2]] | -0.56 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[NSA2]] | -0.55 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[ZNF226]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[ANAPC16]] | -0.55 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[GPBP1]] | -0.55 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[MPHOSPH8]] | -0.54 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[FMC1]] | -0.54 | -0.44 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WT1-AS]] | B | WT1-AS activity raises PLXNA1's level | lines that do not express WT1-AS (36) vs lines expressing it (14) | 1.37× lower at baseline in the lines without WT1-AS | 0.017 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG |
| [[SACS]] | B | SACS activity raises PLXNA1's level | lines that do not express SACS (5) vs lines expressing it (45) | 1.82× lower at baseline in the lines without SACS | 0.089 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |
| [[TSPAN4]] | B | TSPAN4 activity raises PLXNA1's level | lines that do not express TSPAN4 (7) vs lines expressing it (43) | 1.66× lower at baseline in the lines without TSPAN4 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: TRPC1, EMP3, PXDC1; maybe low, not absent |
| [[UBASH3B]] | B | UBASH3B activity raises PLXNA1's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 1.45× lower at baseline in the lines without UBASH3B | 0.0998 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.726). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.5, 5.7); signed map (6.6, 46.0). **Vector** length 118, 30.8% of its response variance represented; |z| ≥ 3 in 1,050 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *apical junction* (hallmark, mean cos +0.52 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +2.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.3 | +1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.5 | +2.8 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +2.2 | +2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +1.4 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | +2.0 | +3.0 |
| fall | [[Cobimetinib (drug)]] 5 µM |  | -5.7 | -2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.3 | -3.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -5.1 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.8 | -3.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.8 | -5.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.7 | -3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.5 | -7.0 |

## What is on record

|  |  |
|---|---|
| Name | plexin A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.3 — chr3:126,982,693-127,037,389 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NOV; previously PLXN1 |
| Gene groups (HGNC) | Plexins; IPT domain containing |
| Reactome | 12 pathways, smallest: SEMA3A-Plexin repulsion signaling by inhibiting Integrin adhesion; CRMPs in Sema3A signaling; Other semaphorin interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UIW2](https://www.uniprot.org/uniprotkb/Q9UIW2) (Plexin-A1):

> Coreceptor for SEMA3A, SEMA3C, SEMA3F and SEMA6D. Necessary for signaling by class 3 semaphorins and subsequent remodeling of the cytoskeleton. Plays a role in axon guidance, invasive growth and cell migration. Class 3 semaphorins bind to a complex composed of a neuropilin and a plexin. The plexin modulates the affinity of the complex for specific semaphorins, and its cytoplasmic domain is required for the activation of down-stream signaling events in the cytoplasm. Acts as coreceptor of TREM2 …

**Summary**, from NCBI Gene [5361](https://www.ncbi.nlm.nih.gov/gene/5361):

> Contributes to semaphorin receptor activity. Involved in T cell activation via T cell receptor contact with antigen bound to MHC molecule on antigen presenting cell and semaphorin-plexin signaling pathway. Located in extracellular exosome. Is active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9099](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9099) · Entrez [5361](https://www.ncbi.nlm.nih.gov/gene/5361) · UniProt [Q9UIW2](https://www.uniprot.org/uniprotkb/Q9UIW2) · Ensembl [ENSG00000114554](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114554)

## Data

Gene col 3565: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3565); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3565, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3565]; `tensor/DDL_lfc|DDL_z.npy` [3565]; `embed/gene_vectors.npy` [3565]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3565 or target_col == 3565). Every well: [[PLXNA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLXNA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
