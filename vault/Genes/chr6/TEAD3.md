---
symbol: "TEAD3"
type: "gene"
col: 152
ensembl_id: "ENSG00000007866"
name: "TEA domain transcription factor 3"
location: "6p21.31"
module: 100
arm: "+"
pooled_cpm: 14.07
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 14
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# TEAD3

*TEA domain transcription factor 3* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.73× (z +11.0, q 2e-25, up in 39 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.503× (z -9.8, q 5e-20, down in 37 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOL4L]] (+0.68, fdr 7e-06), [[HIP1R]] (+0.61, fdr 1e-05), [[DUSP22]] (+0.60, fdr 1e-05); moves opposite to [[SLX4IP]] (-0.55, fdr 1e-05), [[DDX1]] (-0.54, fdr 1e-05), [[CRADD]] (-0.53, fdr 1e-05).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 152.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +11.0 | 2e-25 | 39/45 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.65×** | +6.7 | 6e-09 | 27/45 (MIA PaCa-2, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +6.0 | 4e-07 | 22/46 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.41×** | +4.9 | 2e-04 | 18/46 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +4.3 | 0.002 | 18/46 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +4.3 | 0.002 | 21/45 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +4.1 | 0.003 | 20/45 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.011 | 12/45 (SNU-423, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.60×** | +3.5 | 0.028 | 12/36 (NCI-H2030, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.055 | 15/46 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.085 | 4/47 (PANC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 152.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.503×** | -9.8 | 5e-20 | 37/44 (RKO, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.607×** | -6.6 | 1e-08 | 18/32 (Panc 03.27, SW480, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.730×** | -6.4 | 4e-08 | 22/46 (COLO 205, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.749×** | -5.9 | 7e-07 | 25/47 (Panc 03.27, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.505×** | -5.1 | 4e-05 | 22/47 (Panc 03.27, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.728×** | -4.4 | 0.001 | 14/46 (SK-MEL-2, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.753×** | -3.9 | 0.008 | 15/29 (HT-29, Panc 03.27, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.772×** | -3.7 | 0.015 | 14/46 (HT-29, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[EX229 (drug)]] 5 µM |  | **0.611×** | -3.7 | 0.015 | 10/43 (COLO 205, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.774×** | -3.5 | 0.023 | 17/46 (RKO, COLO 205, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.784×** | -3.5 | 0.026 | 15/46 (HT-29, SNU-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.632×** | -3.4 | 0.028 | 16/43 (Hs 766T, A-427, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.651×** | -3.2 | 0.059 | 10/43 (HOP62, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Hesperidin (drug)]] 0.05 µM |  | **0.792×** | -3.1 | 0.083 | 9/45 (A549, RKO, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 152. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 34.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.398× (z -9.9) |
| [[SW480 (line)]] | alt | 10.3 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.90× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -12.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 13.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -10.4) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -9.3) |
| [[LoVo (line)]] | wt | 17.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[AN3 CA (line)]] | alt | 35.4 | 0 | 1 | — | [[Berbamine (dihydrochloride) (drug)]] 0.05 µM 0.0620× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 15.6 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.299× (z -9.8) |
| [[HOP62 (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -9.6) ⚠ cell-cycle shift, explains ~71% of this change |
| [[HS-578T (line)]] | alt | 16.6 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.338× (z -9.0) |
| [[HT-29 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[KATO III (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -8.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 12.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[MIA PaCa-2 (line)]] | alt | 9.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 7.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +11.6) | — |
| [[RKO (line)]] | wt | 30.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -15.8) |
| [[RPMI-7951 (line)]] | alt | 9.27 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0988× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0745× (z -13.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 21.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0543× (z -13.8) |
| [[A-172 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 152), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOL4L]] | +0.68 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[HIP1R]] | +0.61 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[DUSP22]] | +0.60 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[UBTD1]] | +0.58 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[MBOAT7]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[RBPMS2]] | +0.58 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[PITPNA]] | +0.57 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[TSPAN17]] | +0.57 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[ZFYVE27]] | +0.56 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[RXRA]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[KLHL25]] | +0.55 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[TFEB]] | +0.54 | +0.66 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLX4IP]] | -0.55 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[DDX1]] | -0.54 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[CRADD]] | -0.53 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[RAD50]] | -0.52 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[ING3]] | -0.52 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[EPC1]] | -0.51 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[LDAH]] | -0.51 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[DARS1]] | -0.51 | -0.60 / -0.35 | both halves | 1e-04 |  |
| [[AGGF1]] | -0.50 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[ZNF480]] | -0.50 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ZNF182]] | -0.49 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[IFTAP]] | -0.49 | -0.47 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers TEAD3's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.367). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-8.8, -2.1); signed map (-17.9, 21.0). **Vector** length 92.5, 19.3% of its response variance represented; |z| ≥ 3 in 888 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +11.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.4 | +3.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +4.2 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +1.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.1 | +6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +3.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +1.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.7 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.0 | -9.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.1 | -5.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.0 | -5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -4.0 | -6.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -2.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -4.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.4 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | TEA domain transcription factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:35,473,597-35,497,079 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TEF-5, ETFR-1; previously TEAD5 |
| Gene groups (HGNC) | TEA domain transcription factors |
| Reactome | 8 pathways, smallest: RUNX3 regulates YAP1-mediated transcription; YAP1- and WWTR1 (TAZ)-stimulated gene expression; Regulation of PD-L1(CD274) transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99594](https://www.uniprot.org/uniprotkb/Q99594) (Transcriptional enhancer factor TEF-5):

> Transcription factor which plays a key role in the Hippo signaling pathway, a pathway involved in organ size control and tumor suppression by restricting proliferation and promoting apoptosis. The core of this pathway is composed of a kinase cascade wherein MST1/MST2, in complex with its regulatory protein SAV1, phosphorylates and activates LATS1/2 in complex with its regulatory protein MOB1, which in turn phosphorylates and inactivates YAP1 oncoprotein and WWTR1/TAZ. Acts by mediating gene …

**Summary**, from NCBI Gene [7005](https://www.ncbi.nlm.nih.gov/gene/7005):

> This gene product is a member of the transcriptional enhancer factor (TEF) family of transcription factors, which contain the TEA/ATTS DNA-binding domain. It is predominantly expressed in the placenta and is involved in the transactivation of the chorionic somatomammotropin-B gene enhancer. Translation of this protein is initiated at a non-AUG (AUA) start codon. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11716](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11716) · Entrez [7005](https://www.ncbi.nlm.nih.gov/gene/7005) · UniProt [Q99594](https://www.uniprot.org/uniprotkb/Q99594) · Ensembl [ENSG00000007866](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000007866)

## Data

Gene col 152: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 152); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 152, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 152]; `tensor/DDL_lfc|DDL_z.npy` [152]; `embed/gene_vectors.npy` [152]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 152 or target_col == 152). Every well: [[TEAD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TEAD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
