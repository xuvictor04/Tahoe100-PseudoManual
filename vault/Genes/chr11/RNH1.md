---
symbol: "RNH1"
type: "gene"
col: 340
ensembl_id: "ENSG00000023191"
name: "ribonuclease/angiogenin inhibitor 1"
location: "11p15.5"
module: 148
arm: "+"
pooled_cpm: 30.38
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 9
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# RNH1

*ribonuclease/angiogenin inhibitor 1* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.12× (z +9.5, q 9e-19, up in 39 of 41 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A498 2.65×, A549 3.73×, SNU-423 3.63×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 4.15×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 2.01×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.507× (z -8.6, q 3e-15, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C19orf54]] (+0.59, fdr 3e-05), [[PEF1]] (+0.58, fdr 1e-05), [[TMEM43]] (+0.58, fdr 1e-05); moves opposite to [[HDAC1]] (-0.61, fdr 1e-05), [[FAM102B]] (-0.52, fdr 3e-05), [[HMGN3]] (-0.50, fdr 4e-05).
> It sits in the **+** arm of [[Module 148]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 340.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A498 2.65×, A549 3.73×, SNU-423 3.63×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 4.15×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 2.01×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.12×** | +9.5 | 9e-19 | 39/41 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +8.2 | 6e-14 | 26/33 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +5.2 | 4e-05 | 26/38 (A-427, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.41×** | +4.3 | 0.002 | 25/44 (H4, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.20× | +3.3 | 0.13 | 20/47 (NCI-H2347, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.57× | +3.1 | 0.15 | 15/44 (HOP62, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | 1.60× | +3.1 | 0.15 | 12/46 (HS-578T, SNU-423, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 340.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.507×** | -8.6 | 3e-15 | 40/48 (AsPC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.515×** | -8.4 | 9e-15 | 44/48 (LOX-IMVI, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.548×** | -7.7 | 3e-12 | 43/48 (AsPC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.612×** | -6.3 | 5e-08 | 36/48 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.617×** | -6.2 | 8e-08 | 36/48 (CFPAC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.719×** | -6.0 | 2e-07 | 37/48 (A498, SNU-423, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.679×** | -4.9 | 7e-05 | 30/47 (AN3 CA, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.504×** | -4.6 | 4e-04 | 27/48 (SK-MEL-2, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.831×** | -3.4 | 0.049 | 21/48 (AsPC-1, A498, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 340. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 48.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 56.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +9.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 28.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +9.7) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 35.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -9.9) |
| [[HepG2_C3A (line)]] | wt | 16.3 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.109× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 26.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.288× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 17.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.15× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 28.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 57.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 340), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C19orf54]] | +0.59 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[PEF1]] | +0.58 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[TMEM43]] | +0.58 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[POLDIP2]] | +0.55 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[C8orf33]] | +0.54 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[CYB5D1]] | +0.53 | +0.38 / +0.51 | both halves | 6e-05 |  |
| [[ZPR1]] | +0.53 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[ZNF34]] | +0.53 | +0.48 / +0.34 | both halves | 1e-04 |  |
| [[KPTN]] | +0.53 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[TRIM39]] | +0.53 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[AOC2]] | +0.53 | +0.36 / +0.43 | both halves | 9e-05 |  |
| [[UBE3B]] | +0.52 | +0.39 / +0.52 | both halves | 5e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC1]] | -0.61 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[FAM102B]] | -0.52 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[HMGN3]] | -0.50 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[DPY30]] | -0.50 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[MED30]] | -0.48 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[CKLF]] | -0.48 | -0.46 / -0.25 | both halves | 4e-04 |  |
| [[TMEM185A]] | -0.48 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[EXO5-DT]] | -0.48 | -0.29 / -0.46 | both halves | 3e-04 |  |
| [[ACSF2]] | -0.48 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[MNAT1]] | -0.47 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[NAA40]] | -0.47 | -0.37 / -0.40 | both halves | 7e-05 |  |
| [[SUSD4]] | -0.47 | -0.27 / -0.48 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises RNH1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises RNH1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **+** arm (projection on the module's main direction 0.583). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-11.3, 6.9); signed map (12.9, -8.9). **Vector** length 62.0, 11.8% of its response variance represented; |z| ≥ 3 in 744 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.5 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | -0.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.2 | +0.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | -1.0 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.7 | -0.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +0.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +1.5 | -1.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +1.5 | +0.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.5 | -6.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.5 | -6.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.1 | -2.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.0 | -8.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -4.6 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -1.2 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | ribonuclease/angiogenin inhibitor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:494,512-507,300 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RAI; previously RNH |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [P13489](https://www.uniprot.org/uniprotkb/P13489) (Ribonuclease inhibitor):

> Ribonuclease inhibitor which inhibits RNASE1, RNASE2 and angiogenin (ANG). May play a role in redox homeostasis. Required to inhibit the cytotoxic tRNA ribonuclease activity of ANG in the cytoplasm in absence of stress. Relocates to the nucleus in response to stress, relieving inhibition of ANG in the cytoplasm, and inhibiting the angiogenic activity of ANG in the nucleus.

**Summary**, from NCBI Gene [6050](https://www.ncbi.nlm.nih.gov/gene/6050):

> Placental ribonuclease inhibitor (PRI) is a member of a family of proteinaceous cytoplasmic RNase inhibitors that occur in many tissues and bind to both intracellular and extracellular RNases (summarized by Lee et al., 1988 [PubMed 3219362]). In addition to control of intracellular RNases, the inhibitor may have a role in the regulation of angiogenin (MIM 105850). Ribonuclease inhibitor, of 50,000 Da, binds to ribonucleases and holds them in a latent form. Since neutral and alkaline …

**Accessions** — [HGNC:10074](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10074) · Entrez [6050](https://www.ncbi.nlm.nih.gov/gene/6050) · UniProt [P13489](https://www.uniprot.org/uniprotkb/P13489) · Ensembl [ENSG00000023191](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000023191)

## Data

Gene col 340: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 340); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 340, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 340]; `tensor/DDL_lfc|DDL_z.npy` [340]; `embed/gene_vectors.npy` [340]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 340 or target_col == 340). Every well: [[RNH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
