---
symbol: "SBF1"
type: "gene"
col: 1901
ensembl_id: "ENSG00000100241"
name: "SET binding factor 1"
location: "22q13.33"
module: 2
arm: "+"
pooled_cpm: 23.76
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# SBF1

*SET binding factor 1* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.64× (z +15.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.756× (z -4.6, q 0.003, down in 22 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.150×, LS 180 0.454×; ⚠ cell-cycle shift, explains ~57% of this change); [[Bendamustine (drug)]] 5 µM in 1 line (SW48 0.0633×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 0.237×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-427 0.247×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (A-427 0.249×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKT1]] (+0.78, fdr 7e-06), [[INTS11]] (+0.74, fdr 7e-06), [[MAN2B2]] (+0.74, fdr 7e-06); moves opposite to [[KIAA1586]] (-0.62, fdr 1e-05), [[GSPT2]] (-0.59, fdr 7e-05), [[PIGBOS1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1901.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.64×** | +15.8 | 0e+00 | 48/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.49×** | +14.8 | 0e+00 | 45/48 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +12.9 | 2e-35 | 41/47 (AsPC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +12.6 | 2e-34 | 32/36 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.00×** | +11.3 | 2e-27 | 41/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.91×** | +10.5 | 7e-24 | 34/40 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +8.8 | 8e-17 | 29/37 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +5.9 | 2e-07 | 26/46 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +5.3 | 9e-06 | 24/45 (SW 900, AsPC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +5.2 | 1e-05 | 23/48 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +4.5 | 4e-04 | 20/47 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.32×** | +4.4 | 6e-04 | 21/48 (NCI-H460, RKO, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.56×** | +3.8 | 0.007 | 13/48 (NCI-H1792, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.3 | 0.042 | 12/48 (SNU-1, NCI-H460, …) | top dose only | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.071 | 7/48 (NCI-H2347, A498, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1901.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.150×, LS 180 0.454×; ⚠ cell-cycle shift, explains ~57% of this change); [[Bendamustine (drug)]] 5 µM in 1 line (SW48 0.0633×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 0.237×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-427 0.247×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (A-427 0.249×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.756×** | -4.6 | 0.003 | 22/47 (C-33 A, C32, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.764×** | -4.4 | 0.003 | 22/48 (A-427, LS 180, …) | all doses, flat | cell-cycle shift (explains ~1% here); position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | 0.812× | -3.4 | 0.12 | 14/47 (SW 900, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.809× | -3.3 | 0.12 | 20/48 (LoVo, LOX-IMVI, …) | all doses, flat | composition shift; position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 0.813× | -3.3 | 0.13 | 17/47 (SW480, HT-29, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.816× | -3.1 | 0.20 | 13/47 (LoVo, BT-474, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | 0.826× | -3.0 | 0.20 | 15/47 (J82, A498, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1901. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 16.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -11.9) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.247× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 20.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.90× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +8.5) | — |
| [[SW480 (line)]] | alt | 29.1 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 3.07× (z +11.3) | — |
| [[HOP62 (line)]] | alt | 22.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.21× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 16.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 16.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +8.6) | — |
| [[A-172 (line)]] | wt | 17.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +8.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 17.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +10.9) | — |
| [[C32 (line)]] | wt | 33.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +9.5) | — |
| [[HEC-1-A (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -11.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 41.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.78× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 36.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -9.2) ⚠ cell-cycle shift, explains ~57% of this change |
| [[NCI-H1573 (line)]] | alt | 31.5 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.11× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 25.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 35.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.54× (z +8.5) | — |
| [[SW48 (line)]] | wt | 30.1 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0633× (z -14.2) |
| [[A498 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1901), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKT1]] | +0.78 | +0.70 / +0.79 | both halves | 7e-06 | same gene group; pathway: RAB GEFs exchange GTP for GDP on RABs; STRING 412 |
| [[INTS11]] | +0.74 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[MAN2B2]] | +0.74 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[INTS1]] | +0.73 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[ABCA2]] | +0.73 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[TESK1]] | +0.72 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[SH3GLB2]] | +0.71 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[FBRSL1]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[LLGL1]] | +0.71 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[TUBGCP6]] | +0.70 | +0.66 / +0.60 | both halves | 7e-06 | STRING 541 |
| [[PLCB3]] | +0.69 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[ZDHHC8]] | +0.69 | +0.63 / +0.62 | both halves | 7e-06 | STRING 498 |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA1586]] | -0.62 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[GSPT2]] | -0.59 | -0.38 / -0.66 | both halves | 7e-05 |  |
| [[PIGBOS1]] | -0.57 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[RPP25L]] | -0.56 | -0.39 / -0.51 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SBF1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.828). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-8.4, -22.8); signed map (-45.9, -10.7). **Vector** length 89.4, 18.7% of its response variance represented; |z| ≥ 3 in 930 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.8 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +8.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.6 | +14.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +12.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.7 | +1.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.6 | +2.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.6 | +2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.4 | +2.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -6.3 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.7 | -4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.3 | -4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -4.6 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.8 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | SET binding factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:50,443,219-50,483,923 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MTMR5, DENND7A |
| Gene groups (HGNC) | DENN domain containing; Pleckstrin homology domain containing; Myotubularins |
| Reactome | 8 pathways, smallest: Synthesis of PIPs at the ER membrane; PI Metabolism; RAB GEFs exchange GTP for GDP on RABs |
| Matched by | ensembl_id |

**Function**, from UniProt [O95248](https://www.uniprot.org/uniprotkb/O95248) (Myotubularin-related protein 5):

> Acts as an adapter for the phosphatase MTMR2 to regulate MTMR2 catalytic activity and subcellular location. Promotes the exchange of GDP to GTP, converting inactive GDP-bound Rab proteins into their active GTP-bound form. May function as a guanine nucleotide exchange factor (GEF) activating RAB28. Acts as a suppressor of autophagy in neurons. Together with its binding partner, the phosphatase MTMR2, plays a role in dephosphorylation of phosphoinositides critical for autophagy initiation and …

**Summary**, from NCBI Gene [6305](https://www.ncbi.nlm.nih.gov/gene/6305):

> This gene encodes a member of the protein-tyrosine phosphatase family. However, the encoded protein does not appear to be a catalytically active phosphatase because it lacks several amino acids in the catalytic pocket. This protein contains a Guanine nucleotide exchange factor (GEF) domain which is necessary for its role in growth and differentiation. Mutations in this gene have been associated with Charcot-Marie-Tooth disease 4B3. Pseudogenes of this gene have been defined on chromosomes 1 and …

**Accessions** — [HGNC:10542](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10542) · Entrez [6305](https://www.ncbi.nlm.nih.gov/gene/6305) · UniProt [O95248](https://www.uniprot.org/uniprotkb/O95248) · Ensembl [ENSG00000100241](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100241)

## Data

Gene col 1901: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1901); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1901, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1901]; `tensor/DDL_lfc|DDL_z.npy` [1901]; `embed/gene_vectors.npy` [1901]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1901 or target_col == 1901). Every well: [[SBF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SBF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
