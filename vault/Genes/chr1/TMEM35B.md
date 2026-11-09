---
symbol: "TMEM35B"
type: "gene"
col: 14377
ensembl_id: "ENSG00000243749"
name: "transmembrane protein 35B"
location: "1p34.3"
module: 68
arm: "+"
pooled_cpm: 9.96
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# TMEM35B

*transmembrane protein 35B* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.93× (z +9.7, q 2e-19, up in 29 of 31 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H2030 5.66×, HOP62 4.81×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.226× (z -13.3, q 8e-38, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RWDD2B]] (+0.73, fdr 7e-06), [[HHLA3]] (+0.71, fdr 2e-05), [[PHYH]] (+0.71, fdr 1e-05); moves opposite to [[LPCAT1]] (-0.67, fdr 1e-05), [[GNB1L]] (-0.62, fdr 3e-05), [[KIF21B]] (-0.61, fdr 8e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14377.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H2030 5.66×, HOP62 4.81×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.93×** | +9.7 | 2e-19 | 29/31 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.02×** | +9.6 | 3e-19 | 18/18 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +5.6 | 4e-06 | 20/28 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14377.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.226×** | -13.3 | 8e-38 | 43/47 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.254×** | -12.3 | 3e-32 | 44/47 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.307×** | -10.6 | 7e-24 | 42/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.487×** | -6.4 | 2e-08 | 38/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.271×** | -6.1 | 1e-07 | 32/41 (SW480, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.678×** | -4.9 | 9e-05 | 21/44 (J82, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.356×** | -4.8 | 1e-04 | 27/45 (NCI-H460, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.587×** | -4.8 | 1e-04 | 23/45 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.383×** | -4.5 | 4e-04 | 19/45 (KATO III, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.606×** | -4.5 | 4e-04 | 24/44 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.727×** | -4.0 | 0.003 | 23/44 (KATO III, A-427, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.647×** | -3.9 | 0.005 | 22/46 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.647×** | -3.7 | 0.008 | 20/44 (A498, LOX-IMVI, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.780×** | -3.1 | 0.071 | 19/46 (HT-29, MIA PaCa-2, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14377. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 7.60 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0926× (z -13.8) |
| [[A-172 (line)]] | wt | 9.41 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.126× (z -10.9) |
| [[J82 (line)]] | alt | 11.8 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0931× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.155× (z -10.0) |
| [[KATO III (line)]] | alt | 8.91 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.100× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 6.49 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.165× (z -9.4) |
| [[PANC-1 (line)]] | alt | 11.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.184× (z -10.6) |
| [[A-427 (line)]] | wt | 13.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.172× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 7.86 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.126× (z -9.0) |
| [[COLO 205 (line)]] | alt | 9.10 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0645× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 15.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.131× (z -10.8) |
| [[HOP62 (line)]] | alt | 12.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.81× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 11.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.153× (z -9.4) |
| [[HT-29 (line)]] | alt | 7.26 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.117× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 14.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.136× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 8.69 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.124× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 6.07 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0655× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 16.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.66× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 8.38 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0391× (z -14.3) |
| [[RKO (line)]] | wt | 11.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -8.9) |
| [[SNU-423 (line)]] | alt | 8.49 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.138× (z -8.5) |
| [[A498 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14377), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RWDD2B]] | +0.73 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[HHLA3]] | +0.71 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[PHYH]] | +0.71 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[SDSL]] | +0.67 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[LACTB2]] | +0.67 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[PIGP]] | +0.66 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[GYG1]] | +0.66 | +0.61 / +0.37 | both halves | 7e-05 |  |
| [[CASD1]] | +0.65 | +0.50 / +0.36 | both halves | 1e-04 |  |
| [[NNT-AS1]] | +0.65 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[FAM200B]] | +0.65 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[BAZ2B]] | +0.65 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[TAPBPL]] | +0.65 | +0.50 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPCAT1]] | -0.67 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[GNB1L]] | -0.62 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[KIF21B]] | -0.61 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[INTS11]] | -0.60 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[EHBP1L1]] | -0.59 | -0.51 / -0.31 | both halves | 2e-04 |  |
| [[ANKRD27]] | -0.59 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[TCF3]] | -0.58 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[TPST2]] | -0.58 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[LRFN3]] | -0.58 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[ST6GALNAC6]] | -0.57 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[ABHD17A]] | -0.57 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[TNK2]] | -0.56 | -0.51 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | TMEM35B's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | TMEM35B's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.62 | 0.451 over the table, 0.068 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.733). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (1.4, 12.2); signed map (20.8, -16.0). **Vector** length 60.6, 11.2% of its response variance represented; |z| ≥ 3 in 800 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +1.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +1.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.0 | +2.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +9.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +1.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.8 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +0.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +0.6 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -6.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.8 | -10.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.7 | -12.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.6 | -13.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.4 | -4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.2 | -2.5 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[EX229 (drug)]] 5 µM |  | -1.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 35B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:34,981,380-34,985,347 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ZMYM6NB |
| Matched by | ensembl_id |

UniProt [Q8NCS4](https://www.uniprot.org/uniprotkb/Q8NCS4) carries no function annotation.

**Summary**, from NCBI Gene [100506144](https://www.ncbi.nlm.nih.gov/gene/100506144):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:40021](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40021) · Entrez [100506144](https://www.ncbi.nlm.nih.gov/gene/100506144) · UniProt [Q8NCS4](https://www.uniprot.org/uniprotkb/Q8NCS4) · Ensembl [ENSG00000243749](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243749)

## Data

Gene col 14377: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14377); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14377, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14377]; `tensor/DDL_lfc|DDL_z.npy` [14377]; `embed/gene_vectors.npy` [14377]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14377 or target_col == 14377). Every well: [[TMEM35B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM35B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
