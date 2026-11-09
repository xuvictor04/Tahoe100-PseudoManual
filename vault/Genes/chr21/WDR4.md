---
symbol: "WDR4"
type: "gene"
col: 8313
ensembl_id: "ENSG00000160193"
name: "WDR4 tRNA N7-guanosine methyltransferase non-catalytic subunit"
location: "21q22.3"
module: 5
arm: "+"
pooled_cpm: 16.86
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 15
n_dd_up_clean: 20
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# WDR4

*WDR4 tRNA N7-guanosine methyltransferase non-catalytic subunit* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 2.64× (z +12.5, q 3e-33, up in 47 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 2.47× (z +6.1, q 3e-07, up in 27 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (none with an alert); the strongest is [[Trametinib (drug)]] 0.5 µM: 0.731× (z -4.8, q 7e-04, down in 21 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PUS1]] (+0.93, fdr 7e-06), [[POLR1A]] (+0.86, fdr 7e-06), [[ARMC6]] (+0.86, fdr 7e-06); moves opposite to [[KBTBD3]] (-0.67, fdr 7e-06), [[SECISBP2L]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TERT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8313.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.64×** | +12.5 | 3e-33 | 47/47 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.47×** | +6.1 | 3e-07 | 27/44 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.52×** | +5.4 | 1e-05 | 25/46 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~9% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.18×** | +5.3 | 2e-05 | 25/45 (MIA PaCa-2, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.52×** | +5.2 | 2e-05 | 10/26 (NCI-H1792, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +5.2 | 2e-05 | 22/47 (NCI-H1573, A549, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.45×** | +4.8 | 1e-04 | 17/41 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.98×** | +4.6 | 3e-04 | 20/45 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.44×** | +4.5 | 4e-04 | 24/44 (A-172, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +4.3 | 1e-03 | 22/46 (LOX-IMVI, PANC-1, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.88×** | +4.3 | 1e-03 | 14/42 (PANC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +4.2 | 0.001 | 18/46 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.41×** | +4.1 | 0.002 | 15/33 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **1.78×** | +3.9 | 0.004 | 15/45 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +3.9 | 0.004 | 22/46 (CFPAC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.76×** | +3.8 | 0.005 | 15/47 (CFPAC-1, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.006 | 10/48 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.49×** | +3.7 | 0.007 | 11/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.72×** | +3.6 | 0.008 | 10/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.010 | 21/47 (NCI-H1573, A-172, …) | two highest doses | cell-cycle shift (explains ~10% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, none with an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8313.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.5 µM |  | **0.731×** | -4.8 | 7e-04 | 21/48 (HEC-1-A, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.688×** | -4.7 | 7e-04 | 22/46 (SW480, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.700×** | -4.6 | 7e-04 | 24/46 (A498, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.737×** | -4.5 | 1e-03 | 18/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.715×** | -4.4 | 0.001 | 17/47 (LoVo, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.758×** | -4.0 | 0.006 | 18/48 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.806×** | -4.0 | 0.006 | 19/48 (A498, LS 180, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.565×** | -3.9 | 0.008 | 14/44 (RKO, A-427, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.736×** | -3.8 | 0.008 | 19/46 (MIA PaCa-2, C32, …) | all doses, flat |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.766×** | -3.5 | 0.031 | 18/47 (A-427, RKO, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.778×** | -3.3 | 0.058 | 15/48 (LoVo, J82, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | **0.776×** | -3.2 | 0.071 | 13/46 (C-33 A, RPMI-7951, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.776×** | -3.1 | 0.078 | 14/47 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.773×** | -3.1 | 0.078 | 13/47 (MIA PaCa-2, AsPC-1, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.793×** | -3.0 | 0.094 | 14/47 (RKO, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8313. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 33.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 5.19× (z +10.2) ⚠ unreliable plate only | [[Adagrasib (drug)]] 0.05 µM 0.524× (z -13.9) ⚠ position not correctable |
| [[A-427 (line)]] | wt | 25.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[CFPAC-1 (line)]] | alt | 6.57 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 12.4 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.07× (z +9.3) ⚠ unreliable plate only | — |
| [[A-172 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 27.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8313), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUS1]] | +0.93 | +0.92 / +0.92 | both halves | 7e-06 | pathway: tRNA modification in the nucleus and cytosol; STRING 910 |
| [[POLR1A]] | +0.86 | +0.83 / +0.89 | both halves | 7e-06 | STRING 475 |
| [[ARMC6]] | +0.86 | +0.85 / +0.82 | both halves | 7e-06 |  |
| [[URB2]] | +0.84 | +0.85 / +0.86 | both halves | 7e-06 |  |
| [[LETM1]] | +0.84 | +0.80 / +0.85 | both halves | 7e-06 |  |
| [[GNL3L]] | +0.82 | +0.82 / +0.82 | both halves | 7e-06 | STRING 451 |
| [[MYBBP1A]] | +0.82 | +0.86 / +0.83 | both halves | 7e-06 | STRING 439 |
| [[CTPS1]] | +0.81 | +0.80 / +0.82 | both halves | 7e-06 |  |
| [[NOP2]] | +0.81 | +0.81 / +0.80 | both halves | 7e-06 | STRING 689 |
| [[NOP16]] | +0.81 | +0.87 / +0.76 | both halves | 7e-06 |  |
| [[PUM3]] | +0.81 | +0.83 / +0.78 | both halves | 7e-06 | STRING 427 |
| [[PNO1]] | +0.80 | +0.76 / +0.82 | both halves | 7e-06 | STRING 422 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KBTBD3]] | -0.67 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[SECISBP2L]] | -0.66 | -0.67 / -0.65 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TERT]] | B | TERT activity raises WDR4's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.43× lower at baseline in the lines without TERT | 0.006 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[MAP2K1]] | B | MAP2K1 activity raises WDR4's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[ADD3]] | B | ADD3 activity lowers WDR4's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 1.65× higher at baseline in the lines without ADD3 | 0.081 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.933). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.0, -35.9); signed map (-2.0, -47.6). **Vector** length 118, 31.1% of its response variance represented; |z| ≥ 3 in 1,077 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.75 to 13); *rRNA processing* (reactome, mean cos +0.66 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.66 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.1 | +12.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.9 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | +4.6 | +4.5 |
|  | [[EX229 (drug)]] 5 µM |  | +4.6 | +4.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.6 | +5.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.9 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +3.8 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.8 | -4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.7 | -4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.6 | -4.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.5 | -4.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.2 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | WDR4 tRNA N7-guanosine methyltransferase non-catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:42,843,094-42,879,568 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRM82, TRMT82, Wuho |
| Gene groups (HGNC) | WD repeat domain containing |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [P57081](https://www.uniprot.org/uniprotkb/P57081) (tRNA):

> Non-catalytic component of the METTL1-WDR4 methyltransferase complex required for the formation of N(7)-methylguanine in a subset of RNA species, such as tRNAs, mRNAs and microRNAs (miRNAs). In the METTL1-WDR4 methyltransferase complex, WDR4 acts as a scaffold for tRNA-binding. Required for the formation of N(7)-methylguanine at position 46 (m7G46) in a large subset of tRNAs that contain the 5'-RAGGU-3' motif within the variable loop. M7G46 interacts with C13-G22 in the D-loop to stabilize tRNA …

**Summary**, from NCBI Gene [10785](https://www.ncbi.nlm.nih.gov/gene/10785):

> This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. This gene is excluded as a candidate for a form of nonsyndromic deafness …

**Accessions** — [HGNC:12756](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12756) · Entrez [10785](https://www.ncbi.nlm.nih.gov/gene/10785) · UniProt [P57081](https://www.uniprot.org/uniprotkb/P57081) · Ensembl [ENSG00000160193](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160193)

## Data

Gene col 8313: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8313); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8313, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8313]; `tensor/DDL_lfc|DDL_z.npy` [8313]; `embed/gene_vectors.npy` [8313]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8313 or target_col == 8313). Every well: [[WDR4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
