---
symbol: "CYB5R1"
type: "gene"
col: 8247
ensembl_id: "ENSG00000159348"
name: "cytochrome b5 reductase 1"
location: "1q32.1"
module: 64
arm: "+"
pooled_cpm: 7.94
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# CYB5R1

*cytochrome b5 reductase 1* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 4.33× (z +20.6, q 0e+00, up in 46 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.718× (z -6.6, q 2e-08, down in 22 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW 900 0.291×, MIA PaCa-2 0.203×); [[Imiquimod (hydrochloride) (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0485×); [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0959×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NSFL1C]] (+0.75, fdr 7e-06), [[FAM241B]] (+0.71, fdr 7e-06), [[ETNK2]] (+0.68, fdr 1e-05); moves opposite to [[UBTF]] (-0.64, fdr 3e-05), [[MSANTD2]] (-0.62, fdr 3e-05), [[LEMD3]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[OSBPL7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8247.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **4.33×** | +20.6 | 0e+00 | 46/46 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **3.88×** | +19.1 | 0e+00 | 46/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.44×** | +17.4 | 0e+00 | 45/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.43×** | +17.3 | 0e+00 | 42/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.24×** | +16.5 | 0e+00 | 44/46 (HOP62, C32, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.78×** | +13.6 | 4e-40 | 39/44 (PANC-1, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.06×** | +10.2 | 2e-22 | 33/47 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.04×** | +10.0 | 1e-21 | 31/45 (PANC-1, SW 900, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +9.3 | 1e-18 | 8/14 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.76×** | +8.0 | 1e-13 | 28/40 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +6.2 | 3e-08 | 17/30 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +6.2 | 3e-08 | 15/39 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +6.1 | 6e-08 | 7/23 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.15×** | +5.3 | 4e-06 | 11/46 (A498, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +5.2 | 8e-06 | 13/34 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +4.9 | 4e-05 | 17/45 (A-427, NCI-H460, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +4.7 | 1e-04 | 16/47 (J82, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.64×** | +4.6 | 1e-04 | 13/45 (HOP62, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.023 | 5/44 (C32, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8247.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW 900 0.291×, MIA PaCa-2 0.203×); [[Imiquimod (hydrochloride) (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0485×); [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0959×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.718×** | -6.6 | 2e-08 | 22/42 (SW 900, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.737×** | -4.3 | 0.005 | 14/46 (C32, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.793× | -3.2 | 0.30 | 11/42 (COLO 205, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8247. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.12 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.34× (z +9.7) | — |
| [[NCI-H460 (line)]] | wt | 6.51 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.37× (z +9.6) | — |
| [[SW480 (line)]] | alt | 6.23 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.15× (z +11.2) | — |
| [[C32 (line)]] | wt | 12.5 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 7.26× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 9.63 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.63× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.81 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0735× (z -10.2) |
| [[A498 (line)]] | wt | 10.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.12× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 4.41 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0849× (z -8.7) ⚠ cell-cycle shift, explains ~50% of this change |
| [[HEC-1-A (line)]] | alt | 10.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.18× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 7.32 | 0 | 1 | — | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM 0.0485× (z -10.9) |
| [[LoVo (line)]] | wt | 3.56 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 9.46× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 5.26 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0883× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 5.37 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0959× (z -10.3) |
| [[SW 900 (line)]] | alt | 30.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -11.7) |
| [[A-172 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.26 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8247), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSFL1C]] | +0.75 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[FAM241B]] | +0.71 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[ETNK2]] | +0.68 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[MAPRE3]] | +0.66 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[DNAJB1]] | +0.66 | +0.54 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_UP |
| [[SAMD4B]] | +0.65 | +0.65 / +0.39 | both halves | 5e-05 |  |
| [[MYG1]] | +0.65 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[PSMD3]] | +0.65 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[MRGBP]] | +0.64 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[CALCOCO2]] | +0.63 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[PSMB1]] | +0.63 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[CAMK2G]] | +0.63 | +0.55 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBTF]] | -0.64 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[MSANTD2]] | -0.62 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[LEMD3]] | -0.61 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[ZNF337-AS1]] | -0.59 | -0.36 / -0.27 | both halves | 3e-04 |  |
| [[PHC2-AS1]] | -0.58 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[PCBP1-AS1]] | -0.57 | -0.27 / -0.40 | both halves | 3e-04 |  |
| [[PSPC1]] | -0.57 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[GNG12-AS1]] | -0.56 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[SLC12A2-DT]] | -0.56 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[RXYLT1]] | -0.56 | -0.36 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[HIVEP1]] | -0.55 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[PSMD6-AS1]] | -0.55 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[C10orf88B]] | -0.55 | -0.35 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OSBPL7]] | B | OSBPL7 activity raises CYB5R1's level | lines that do not express OSBPL7 (7) vs lines expressing it (43) | 1.43× lower at baseline in the lines without OSBPL7 | 0.091 | ⚠ within organs, on part of the lines; also absent: TBXAS1, PYROXD2, ETS2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.471). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-3.3, 11.6); signed map (-19.6, -6.4). **Vector** length 83.9, 16.4% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +8.2 | +17.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.1 | +16.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.8 | +13.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +20.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.1 | +17.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +10.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.4 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +3.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.7 | -6.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | +0.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -1.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.3 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome b5 reductase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:202,961,873-202,967,275 (-) |
| Ensembl biotype | protein_coding |
| Also known as | humb5R2; previously NQO3A2 |
| Gene groups (HGNC) | Cytochrome b5 reductases; Flavoproteins |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 7 pathways, smallest: Erythrocytes take up carbon dioxide and release oxygen; O2/CO2 exchange in erythrocytes; Platelet degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHQ9](https://www.uniprot.org/uniprotkb/Q9UHQ9) (NADH-cytochrome b5 reductase 1):

> Catalyzes the reduction of two molecules of cytochrome b5 using NADH as the electron donor.

**Summary**, from NCBI Gene [51706](https://www.ncbi.nlm.nih.gov/gene/51706):

> Predicted to enable FAD binding activity and cytochrome-b5 reductase activity, acting on NAD(P)H. Predicted to be involved in bicarbonate transport. Located in extracellular exosome; membrane; and mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13397](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13397) · Entrez [51706](https://www.ncbi.nlm.nih.gov/gene/51706) · UniProt [Q9UHQ9](https://www.uniprot.org/uniprotkb/Q9UHQ9) · Ensembl [ENSG00000159348](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159348)

## Data

Gene col 8247: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8247); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8247, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8247]; `tensor/DDL_lfc|DDL_z.npy` [8247]; `embed/gene_vectors.npy` [8247]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8247 or target_col == 8247). Every well: [[CYB5R1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYB5R1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
