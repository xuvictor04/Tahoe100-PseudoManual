---
symbol: "PAXIP1"
type: "gene"
col: 8051
ensembl_id: "ENSG00000157212"
name: "PAX interacting protein 1"
location: "7q36.2"
module: 1
arm: "+"
pooled_cpm: 40.82
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PAXIP1

*PAX interacting protein 1* — 7q36.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +12.1, q 5e-31, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.725× (z -6.3, q 2e-07, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[QSER1]] (+0.67, fdr 1e-05), [[SLC5A6]] (+0.65, fdr 1e-05), [[IGF2BP1]] (+0.63, fdr 3e-05); moves opposite to [[HERPUD1]] (-0.58, fdr 3e-05), [[RIOK3]] (-0.57, fdr 2e-05), [[PNPLA8]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8051.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +12.1 | 5e-31 | 34/48 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +6.7 | 8e-09 | 26/48 (A498, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +6.2 | 9e-08 | 32/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +5.2 | 4e-05 | 24/48 (CFPAC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.24×** | +4.2 | 0.003 | 16/48 (SW480, C32, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.22×** | +3.9 | 0.011 | 16/47 (SW 900, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.21×** | +3.5 | 0.030 | 14/48 (A498, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.20×** | +3.5 | 0.030 | 18/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.14× | +3.4 | 0.036 | 13/48 (NCI-H1573, CFPAC-1, …) | top dose only | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | 1.20× | +3.3 | 0.061 | 17/47 (HCT15, A-172, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8051.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.725×** | -6.3 | 2e-07 | 29/48 (HEC-1-A, SW48, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.748×** | -5.3 | 3e-05 | 25/48 (SK-MEL-2, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.766×** | -5.2 | 4e-05 | 27/48 (HEC-1-A, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.832×** | -3.3 | 0.098 | 18/44 (A-427, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.787×** | -3.3 | 0.098 | 17/48 (KATO III, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8051. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 47.9 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +15.2) | — |
| [[A549 (line)]] | wt | 33.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +17.3) | — |
| [[CFPAC-1 (line)]] | alt | 27.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +19.3) | [[AZD2858 (drug)]] 0.5 µM 0.249× (z -8.6) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 54.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +15.2) | — |
| [[SNU-1 (line)]] | wt | 52.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.339× (z -10.4) |
| [[A-172 (line)]] | wt | 30.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 19.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 20.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +16.2) | — |
| [[Panc 03.27 (line)]] | alt | 31.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +16.4) | — |
| [[RKO (line)]] | wt | 55.3 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.102× (z -19.2) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[SW 900 (line)]] | alt | 34.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +9.8) | — |
| [[A-427 (line)]] | wt | 46.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -13.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 73.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -9.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 17.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 45.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.334× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 32.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +10.6) | — |
| [[J82 (line)]] | alt | 40.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +13.6) | — |
| [[KATO III (line)]] | alt | 51.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.316× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 41.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +12.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 66.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.250× (z -15.0) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1792 (line)]] | alt | 33.8 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.92× (z +10.5) | — |
| [[NCI-H23 (line)]] | alt | 60.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 38.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 39.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.311× (z -9.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 35.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.9) | — |
| [[SW48 (line)]] | wt | 58.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[C-33 A (line)]] | alt | 98.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 52.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8051), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QSER1]] | +0.67 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[SLC5A6]] | +0.65 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[IGF2BP1]] | +0.63 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[ZDHHC23]] | +0.62 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[OXCT1]] | +0.59 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[UBQLN4]] | +0.58 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[MCCC2]] | +0.58 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[UMPS]] | +0.58 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[RNASEH2B]] | +0.57 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[SEPTIN8]] | +0.57 | +0.39 / +0.45 | both halves | 5e-05 |  |
| [[POGLUT1]] | +0.57 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[USP13]] | +0.57 | +0.44 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERPUD1]] | -0.58 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[RIOK3]] | -0.57 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[PNPLA8]] | -0.57 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[PSMB1]] | -0.56 | -0.45 / -0.39 | both halves | 5e-05 | pathway: DNA Double-Strand Break Repair |
| [[WASF2]] | -0.54 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[RAB2A]] | -0.54 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[TMEM92]] | -0.53 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[PIGH]] | -0.53 | -0.40 / -0.27 | both halves | 3e-04 |  |
| [[MACO1]] | -0.53 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[CAST]] | -0.53 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[SARAF]] | -0.52 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[GP6-AS1]] | -0.52 | -0.49 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises PAXIP1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.417). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-4.2, 6.1); signed map (22.6, -33.8). **Vector** length 94.2, 20.0% of its response variance represented; |z| ≥ 3 in 838 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.2 | +6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +12.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.6 | +6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.7 | +4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +2.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.3 | +1.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +2.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.2 | +1.9 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -4.4 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -6.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.7 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.2 | -5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -1.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.4 | -2.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -1.6 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | PAX interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.2 — chr7:154,943,687-155,003,124 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CAGF29, CAGF28, TNRC2, PTIP; previously PAXIP1L |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 15 pathways, smallest: Formation of WDR5-containing histone-modifying complexes; Nonhomologous End-Joining (NHEJ); Activation of HOX genes during differentiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZW49](https://www.uniprot.org/uniprotkb/Q6ZW49) (PAX-interacting protein 1):

> Involved in DNA damage response and in transcriptional regulation through histone methyltransferase (HMT) complexes. Plays a role in early development. In DNA damage response is required for cell survival after ionizing radiation. In vitro shown to be involved in the homologous recombination mechanism for the repair of double-strand breaks (DSBs). Its localization to DNA damage foci requires RNF8 and UBE2N. Recruits TP53BP1 to DNA damage foci and, at least in particular repair processes, …

**Summary**, from NCBI Gene [22976](https://www.ncbi.nlm.nih.gov/gene/22976):

> This gene is a member of the paired box (PAX) gene family and encodes a nuclear protein with six BRCT (breast cancer carboxy-terminal) domains. This protein plays a critical role in maintaining genome stability, condensation of chromatin and progression through mitosis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8624](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8624) · Entrez [22976](https://www.ncbi.nlm.nih.gov/gene/22976) · UniProt [Q6ZW49](https://www.uniprot.org/uniprotkb/Q6ZW49) · Ensembl [ENSG00000157212](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157212)

## Data

Gene col 8051: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8051); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8051, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8051]; `tensor/DDL_lfc|DDL_z.npy` [8051]; `embed/gene_vectors.npy` [8051]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8051 or target_col == 8051). Every well: [[PAXIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAXIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
