---
symbol: "NDOR1"
type: "gene"
col: 12025
ensembl_id: "ENSG00000188566"
name: "NADPH dependent diflavin oxidoreductase 1"
location: "9q34.3"
module: 71
arm: "+"
pooled_cpm: 13.24
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 5
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# NDOR1

*NADPH dependent diflavin oxidoreductase 1* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (16 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.57× (z +18.6, q 0e+00, up in 42 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.687× (z -7.4, q 6e-11, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPLOC4]] (+0.68, fdr 7e-06), [[DGCR8]] (+0.68, fdr 7e-06), [[TRAPPC10]] (+0.66, fdr 7e-06); moves opposite to [[RYBP]] (-0.58, fdr 1e-05), [[SMIM30]] (-0.58, fdr 4e-05), [[ARL4A]] (-0.58, fdr 2e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12025.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.57×** | +18.6 | 0e+00 | 42/44 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **2.12×** | +10.5 | 4e-23 | 40/47 (SW480, LoVo, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.99×** | +9.6 | 2e-19 | 37/47 (SW480, RKO, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.03×** | +9.5 | 4e-19 | 37/47 (SW480, SNU-423, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.75×** | +7.8 | 7e-13 | 35/47 (SW480, LoVo, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.71×** | +7.1 | 9e-11 | 31/47 (LS 180, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **1.69×** | +7.0 | 2e-10 | 24/39 (SW480, COLO 205, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +6.7 | 2e-09 | 26/48 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +6.4 | 9e-09 | 23/47 (SW480, LoVo, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.53×** | +5.9 | 2e-07 | 23/47 (SW480, LoVo, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +4.7 | 1e-04 | 15/47 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.39×** | +4.5 | 3e-04 | 14/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.41×** | +4.5 | 3e-04 | 13/47 (SW480, AN3 CA, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.37×** | +4.4 | 5e-04 | 15/47 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.33×** | +4.0 | 0.003 | 15/45 (LOX-IMVI, A549, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.69×** | +3.8 | 0.004 | 9/47 (SW480, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +3.6 | 0.010 | 10/44 (LOX-IMVI, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.010 | 16/47 (SW480, SNU-423, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.039 | 7/47 (BT-474, SW480, …) | rises with dose |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.26×** | +3.0 | 0.072 | 5/47 (SNU-1, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12025.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.687×** | -7.4 | 6e-11 | 30/48 (SW1417, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.592×** | -7.3 | 6e-11 | 28/46 (A549, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.718×** | -4.6 | 7e-04 | 19/47 (AsPC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.679×** | -3.9 | 0.015 | 12/45 (HEC-1-A, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.768×** | -3.7 | 0.025 | 6/47 (LoVo, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.62 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12025. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 15.7 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.49× (z +9.4) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.38× (z +9.1) | — |
| [[AsPC-1 (line)]] | alt | 8.38 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.42× (z +10.8) | [[Flutamide (drug)]] 0.5 µM 0.0539× (z -13.2) |
| [[A-172 (line)]] | wt | 31.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 10.4 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0603× (z -10.6) |
| [[Hs 766T (line)]] | wt | 11.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 8.62 | 0 | 1 | — | [[Nevirapine (drug)]] 0.05 µM 0.0573× (z -9.9) |
| [[LoVo (line)]] | wt | 12.7 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.10× (z +8.7) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[NCI-H2347 (line)]] | alt | 8.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +8.9) | — |
| [[PANC-1 (line)]] | alt | 8.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +9.6) | — |
| [[RKO (line)]] | wt | 26.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 29.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 8.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.46× (z +8.8) | — |
| [[A-427 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.08 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12025), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPLOC4]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[DGCR8]] | +0.68 | +0.61 / +0.77 | both halves | 7e-06 |  |
| [[TRAPPC10]] | +0.66 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[TONSL]] | +0.66 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[DHRS11]] | +0.65 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[MCM5]] | +0.65 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[HCFC1]] | +0.65 | +0.58 / +0.63 | both halves | 8e-06 |  |
| [[XRCC3]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[NUP50]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[PASK]] | +0.64 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[SMPD4]] | +0.64 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[ZNF142]] | +0.64 | +0.59 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RYBP]] | -0.58 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[SMIM30]] | -0.58 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[ARL4A]] | -0.58 | -0.49 / -0.49 | both halves | 2e-05 |  |
| [[CTR9]] | -0.57 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[SUGT1P3-1]] | -0.57 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[BTG1]] | -0.56 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[SNX2]] | -0.56 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[TTC3P1]] | -0.54 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[ZC3H15]] | -0.54 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[CHMP2B]] | -0.54 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[KPNA5]] | -0.54 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[PITPNA-AS1]] | -0.53 | -0.51 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NDOR1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.605). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.5, -28.0); signed map (-45.5, -22.2). **Vector** length 80.9, 15.3% of its response variance represented; |z| ≥ 3 in 1,012 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +18.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.5 | +9.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +6.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.7 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +6.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | +3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.7 | +3.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.8 | -7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.0 | -7.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -1.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.8 | +1.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +0.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.3 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | +0.8 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | NADPH dependent diflavin oxidoreductase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:137,205,685-137,219,361 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NR1, bA350O14.9, CIAE1 |
| Gene groups (HGNC) | Cytosolic iron-sulfur assembly components; Flavoproteins; Oxidoreductases |
| Reactome | 1 pathways, smallest: Cytosolic iron-sulfur cluster assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHB4](https://www.uniprot.org/uniprotkb/Q9UHB4) (NADPH-dependent diflavin oxidoreductase 1):

> NADPH-dependent reductase which is a central component of the cytosolic iron-sulfur (Fe-S) protein assembly (CIA) machinery. Transfers electrons from NADPH via its FAD and FMN prosthetic groups to the [2Fe-2S] cluster of CIAPIN1, another key component of the CIA machinery. In turn, this reduced cluster provides electrons for assembly of cytosolic iron-sulfur cluster proteins. It can also reduce the [2Fe-2S] cluster of CISD1 and activate this protein implicated in Fe/S cluster repair. In vitro …

**Summary**, from NCBI Gene [27158](https://www.ncbi.nlm.nih.gov/gene/27158):

> This gene encodes an NADPH-dependent diflavin reductase that contains both flavin mononucleotide (FMN) and flavin adenine dinucleotide (FAD) binding domains. The encoded protein catalyzes the transfer of electrons from NADPH through FAD and FMN cofactors to potential redox partners. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2012]

**Accessions** — [HGNC:29838](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29838) · Entrez [27158](https://www.ncbi.nlm.nih.gov/gene/27158) · UniProt [Q9UHB4](https://www.uniprot.org/uniprotkb/Q9UHB4) · Ensembl [ENSG00000188566](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188566)

## Data

Gene col 12025: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12025); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12025, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12025]; `tensor/DDL_lfc|DDL_z.npy` [12025]; `embed/gene_vectors.npy` [12025]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12025 or target_col == 12025). Every well: [[NDOR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDOR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
