---
symbol: "UBQLN2"
type: "gene"
col: 11969
ensembl_id: "ENSG00000188021"
name: "ubiquilin 2"
location: "Xp11.21"
module: 16
arm: "+"
pooled_cpm: 28.73
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# UBQLN2

*ubiquilin 2* — Xp11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.85× (z +9.9, q 2e-20, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.443× (z -13.6, q 4e-39, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB33]] (+0.81, fdr 7e-06), [[ZNF24]] (+0.79, fdr 7e-06), [[ZXDB]] (+0.77, fdr 7e-06); moves opposite to [[CORO7]] (-0.69, fdr 7e-06), [[UQCRH]] (-0.65, fdr 1e-05), [[HDAC3]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11969.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.85×** | +9.9 | 2e-20 | 43/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +9.4 | 1e-18 | 41/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.74×** | +9.3 | 3e-18 | 41/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.41×** | +8.2 | 3e-14 | 30/47 (NCI-H460, A549, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +6.5 | 7e-09 | 28/48 (A-427, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +5.4 | 6e-06 | 24/46 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.28×** | +4.1 | 0.003 | 21/48 (BT-474, J82, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.24×** | +3.6 | 0.021 | 16/45 (NCI-H460, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.47×** | +3.4 | 0.047 | 13/46 (PANC-1, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.21×** | +3.2 | 0.068 | 13/48 (HT-29, A549, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.21×** | +3.1 | 0.086 | 17/48 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11969.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.443×** | -13.6 | 4e-39 | 47/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.484×** | -12.1 | 4e-31 | 44/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.494×** | -11.7 | 1e-29 | 40/48 (LoVo, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.725×** | -7.6 | 6e-12 | 30/48 (RKO, HEC-1-A, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.732×** | -5.0 | 7e-05 | 26/47 (SNU-423, hTERT-HPNE, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.751×** | -4.8 | 2e-04 | 22/48 (LoVo, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.768×** | -4.4 | 9e-04 | 23/47 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.925× | -4.2 | 0.002 | 2/48 (NCI-H661, C-33 A) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.645×** | -3.8 | 0.009 | 12/48 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11969. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 26.0 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.2) ⚠ cell-cycle shift, explains ~42% of this change | [[Panobinostat (drug)]] 0.5 µM 0.364× (z -8.7) |
| [[KATO III (line)]] | alt | 52.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.319× (z -12.1) |
| [[LoVo (line)]] | wt | 25.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.268× (z -12.7) |
| [[NCI-H460 (line)]] | wt | 32.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.29× (z +8.6) | — |
| [[A549 (line)]] | wt | 23.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +10.6) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.55× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 29.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.262× (z -8.6) |
| [[SNU-423 (line)]] | alt | 54.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.334× (z -9.7) |
| [[SW480 (line)]] | alt | 39.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.374× (z -11.8) |
| [[A-427 (line)]] | wt | 36.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -11.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HOP62 (line)]] | alt | 28.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.326× (z -9.3) |
| [[LS 180 (line)]] | wt | 29.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.337× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 36.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 28.0 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.39× (z +8.5) | — |
| [[RKO (line)]] | wt | 33.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -9.9) ⚠ cell-cycle shift, explains ~22% of this change |
| [[A-172 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11969), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB33]] | +0.81 | +0.70 / +0.81 | both halves | 7e-06 |  |
| [[ZNF24]] | +0.79 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[ZXDB]] | +0.77 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[ZNF260]] | +0.76 | +0.72 / +0.78 | both halves | 7e-06 |  |
| [[HNRNPH2]] | +0.74 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[LIG4]] | +0.74 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[ZNF776]] | +0.74 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[LYRM2]] | +0.73 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[METTL18]] | +0.71 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[ASF1A]] | +0.71 | +0.79 / +0.63 | both halves | 7e-06 |  |
| [[RTL6]] | +0.70 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.70 | +0.68 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CORO7]] | -0.69 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[UQCRH]] | -0.65 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[HDAC3]] | -0.65 | -0.65 / -0.53 | both halves | 1e-05 | STRING 412 |
| [[BUD23]] | -0.63 | -0.43 / -0.63 | both halves | 3e-05 |  |
| [[SSBP4]] | -0.63 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[SEC11A]] | -0.62 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[COG5]] | -0.62 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[SFI1]] | -0.62 | -0.60 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises UBQLN2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.743). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-31.1, 12.0); signed map (3.7, -28.9). **Vector** length 107, 25.3% of its response variance represented; |z| ≥ 3 in 925 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.0 | +9.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.1 | +9.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.9 | +9.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +7.1 | +8.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.8 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.0 | +2.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.0 | +2.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.8 | +2.1 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -5.4 | -13.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.2 | -12.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.3 | -11.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -3.9 | -7.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.7 | -1.6 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.6 | -2.2 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -2.1 | -1.9 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -2.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ubiquilin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.21 — chrX:56,563,627-56,567,868 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Chap1, Dsk2, RIHFB2157, LIC-2, CHAP1/DSK2, PLIC-2, N4BP4, PLIC2 |
| Gene groups (HGNC) | Ubiquilin family |
| Reactome | 4 pathways, smallest: Cargo recognition for clathrin-mediated endocytosis; Clathrin-mediated endocytosis; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHD9](https://www.uniprot.org/uniprotkb/Q9UHD9) (Ubiquilin-2):

> Plays an important role in the regulation of different protein degradation mechanisms and pathways including ubiquitin-proteasome system (UPS), autophagy and the endoplasmic reticulum-associated protein degradation (ERAD) pathway. Mediates the proteasomal targeting of misfolded or accumulated proteins for degradation by binding (via UBA domain) to their polyubiquitin chains and by interacting (via ubiquitin-like domain) with the subunits of the proteasome. Plays a role in the ERAD pathway via …

**Summary**, from NCBI Gene [29978](https://www.ncbi.nlm.nih.gov/gene/29978):

> This gene encodes an ubiquitin-like protein (ubiquilin) that shares high degree of similarity with related products in yeast, rat and frog. Ubiquilins contain a N-terminal ubiquitin-like domain and a C-terminal ubiquitin-associated domain. They physically associate with both proteasomes and ubiquitin ligases; and thus, are thought to functionally link the ubiquitination machinery to the proteasome to affect in vivo protein degradation. This ubiquilin has also been shown to bind the ATPase …

**Accessions** — [HGNC:12509](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12509) · Entrez [29978](https://www.ncbi.nlm.nih.gov/gene/29978) · UniProt [Q9UHD9](https://www.uniprot.org/uniprotkb/Q9UHD9) · Ensembl [ENSG00000188021](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188021)

## Data

Gene col 11969: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11969); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11969, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11969]; `tensor/DDL_lfc|DDL_z.npy` [11969]; `embed/gene_vectors.npy` [11969]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11969 or target_col == 11969). Every well: [[UBQLN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBQLN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
