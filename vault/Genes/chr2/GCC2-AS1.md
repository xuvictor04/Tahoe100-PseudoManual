---
symbol: "GCC2-AS1"
type: "gene"
col: 13182
ensembl_id: "ENSG00000214184"
name: "GCC2 antisense RNA 1"
location: "2q12.3"
module: 21
arm: "+"
pooled_cpm: 7.25
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 9
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# GCC2-AS1

*GCC2 antisense RNA 1* — 2q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.32× (z +20.4, q 0e+00, up in 13 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.46× (z +14.6, q 0e+00, up in 36 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.586× (z -6.2, q 4e-07, down in 23 of 47 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.609× (z -5.7, q 3e-06, down in 26 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C2CD5-AS1]] (+0.70, fdr 7e-06), [[CNGB3]] (+0.68, fdr 7e-06), [[MROH8]] (+0.67, fdr 1e-05); moves opposite to [[SLC39A3]] (-0.56, fdr 1e-04).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ANKRD20A21P]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13182.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.32×** | +20.4 | 0e+00 | 13/14 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.71×** | +17.8 | 0e+00 | 27/29 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.46×** | +14.6 | 0e+00 | 36/40 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.87×** | +11.2 | 5e-27 | 16/19 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +7.6 | 4e-12 | 28/39 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.58×** | +7.5 | 7e-12 | 24/48 (A498, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +6.0 | 2e-07 | 13/35 (A-427, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +4.7 | 2e-04 | 15/40 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.27×** | +3.7 | 0.013 | 5/48 (SW480, NCI-H1792, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.36×** | +3.6 | 0.020 | 7/43 (A-427, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.021 | 10/45 (HOP62, SW1417, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.031 | 15/48 (A-172, SHP-77, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.040 | 9/47 (A-172, SW480, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.049 | 6/48 (SW480, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.32×** | +3.1 | 0.062 | 4/48 (HOP62, Hs 766T, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13182.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.586×** | -6.2 | 4e-07 | 23/47 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.609×** | -5.7 | 3e-06 | 26/45 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.483×** | -4.4 | 0.002 | 16/43 (PANC-1, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.694×** | -4.2 | 0.003 | 19/39 (PANC-1, NCI-H1573, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.516×** | -4.0 | 0.008 | 19/41 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.718×** | -3.8 | 0.013 | 12/45 (PANC-1, A-172, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.721×** | -3.8 | 0.013 | 16/46 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.729×** | -3.6 | 0.019 | 15/46 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.746×** | -3.4 | 0.045 | 8/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13182. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 16.6 | 0 | 10 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0926× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.166× (z -15.2) |
| [[HEC-1-A (line)]] | alt | 9.58 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.06× (z +12.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 7.23 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.22× (z +11.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 11.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.90× (z +12.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 5.83 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.7× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +11.0) | — |
| [[LOX-IMVI (line)]] | wt | 8.06 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 10.2× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 9.74 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.128× (z -9.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.139× (z -9.5) |
| [[SW 900 (line)]] | alt | 5.05 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 33.1× (z +11.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 7.69 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0720× (z -11.5) |
| [[A549 (line)]] | wt | 9.38 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.02× (z +9.1) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 4.37 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.6× (z +8.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 4.69 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.9× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 7.71 | 0 | 1 | — | [[Penfluridol (drug)]] 5 µM 0.0537× (z -8.7) |
| [[Hs 766T (line)]] | wt | 5.60 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.9× (z +8.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 5.00 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.76× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 4.47 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0833× (z -9.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H2030 (line)]] | alt | 5.79 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.7× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 5.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +10.1) | — |
| [[A-427 (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13182), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2CD5-AS1]] | +0.70 | +0.60 / +0.64 | both halves | 7e-06 | same gene group |
| [[CNGB3]] | +0.68 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[MROH8]] | +0.67 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[LRIG2-DT]] | +0.66 | +0.71 / +0.45 | both halves | 3e-05 |  |
| [[ZNF451-AS1]] | +0.66 | +0.54 / +0.60 | both halves | 1e-05 | same gene group |
| [[HSPA2-AS1]] | +0.66 | +0.52 / +0.65 | both halves | 1e-05 | same gene group |
| [[CARNMT1-AS1]] | +0.65 | +0.62 / +0.56 | both halves | 1e-05 | same gene group |
| [[TICAM2-AS1]] | +0.65 | +0.49 / +0.67 | both halves | 1e-05 | same gene group |
| [[GEMIN7-AS1]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 | same gene group |
| [[UGDH-AS1]] | +0.63 | +0.65 / +0.55 | both halves | 1e-05 | same gene group |
| [[OOEP]] | +0.63 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[CYB5D2]] | +0.63 | +0.61 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC39A3]] | -0.56 | -0.44 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD20A21P]] | B | ANKRD20A21P activity raises GCC2-AS1's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 1.33× lower at baseline in the lines without ANKRD20A21P | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |
| [[TOP2A]] | B | TOP2A activity lowers GCC2-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ATF7IP2]] | B | ATF7IP2 activity raises GCC2-AS1's level | lines that do not express ATF7IP2 (12) vs lines expressing it (38) | 1.15× lower at baseline in the lines without ATF7IP2 | 0.076 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.658). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.2, 26.0); signed map (33.3, 2.3). **Vector** length 70.8, 11.8% of its response variance represented; |z| ≥ 3 in 889 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +20.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +17.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +14.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +11.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +7.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.0 | +2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +2.9 |
|  | [[Infigratinib (drug)]] 5 µM |  | +1.4 | +1.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.5 | -0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -0.1 |
|  | [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.6 | -0.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -1.0 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | -1.3 | -0.5 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -1.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | GCC2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q12.3 — chr2:108,507,515-108,534,196 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28126](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28126) · Entrez [644903](https://www.ncbi.nlm.nih.gov/gene/644903) · Ensembl [ENSG00000214184](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214184)

## Data

Gene col 13182: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13182); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13182, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13182]; `tensor/DDL_lfc|DDL_z.npy` [13182]; `embed/gene_vectors.npy` [13182]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13182 or target_col == 13182). Every well: [[GCC2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GCC2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
