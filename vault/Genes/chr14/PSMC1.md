---
symbol: "PSMC1"
type: "gene"
col: 2019
ensembl_id: "ENSG00000100764"
name: "proteasome 26S subunit, ATPase 1"
location: "14q32.11"
module: 64
arm: "+"
pooled_cpm: 55.07
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 8
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# PSMC1

*proteasome 26S subunit, ATPase 1* — 14q32.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.82× (z +14.4, q 3e-44, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.734× (z -5.7, q 6e-06, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJC7]] (+0.71, fdr 7e-06), [[BRF2]] (+0.70, fdr 7e-06), [[PSMC4]] (+0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2019.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.82×** | +14.4 | 3e-44 | 47/48 (LoVo, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.76×** | +14.1 | 1e-42 | 48/48 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.46×** | +11.8 | 8e-30 | 47/48 (NCI-H1573, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.86×** | +8.6 | 1e-15 | 40/49 (NCI-H23, SW480, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.14×** | +8.3 | 1e-14 | 45/49 (LoVo, HOP62, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +6.9 | 6e-10 | 45/48 (BT-474, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.62×** | +6.4 | 1e-08 | 27/41 (PANC-1, SW480, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.41×** | +6.4 | 1e-08 | 40/44 (LOX-IMVI, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.25×** | +5.9 | 2e-07 | 34/48 (LS 180, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +5.8 | 3e-07 | 33/45 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.00×** | +5.0 | 3e-05 | 41/49 (LOX-IMVI, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.40×** | +4.6 | 2e-04 | 29/48 (NCI-H1573, PANC-1, …) | two highest doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +4.3 | 8e-04 | 22/37 (Panc 03.27, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.0 | 0.003 | 31/47 (NCI-H2030, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.30×** | +3.7 | 0.009 | 22/47 (SW480, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2019.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.734×** | -5.7 | 6e-06 | 38/48 (CFPAC-1, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.681×** | -5.3 | 2e-05 | 35/48 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.681×** | -5.3 | 2e-05 | 34/48 (H4, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.778×** | -4.7 | 3e-04 | 28/48 (CHP-212, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.715×** | -4.7 | 4e-04 | 38/48 (SW480, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.724×** | -4.5 | 7e-04 | 30/48 (NCI-H460, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.741×** | -4.2 | 0.002 | 31/48 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.930× | -3.3 | 0.066 | 1/49 (SW 1271) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.645×** | -3.2 | 0.092 | 21/48 (A-427, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2019. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 45.9 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.77× (z +13.4) | — |
| [[SW480 (line)]] | alt | 54.2 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.47× (z +12.8) | — |
| [[PANC-1 (line)]] | alt | 41.2 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.89× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 67.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.76× (z +13.1) | — |
| [[HEC-1-A (line)]] | alt | 44.6 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.47× (z +10.7) | — |
| [[KATO III (line)]] | alt | 47.4 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.64× (z +11.4) | — |
| [[LOX-IMVI (line)]] | wt | 43.3 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.42× (z +12.1) | — |
| [[NCI-H1573 (line)]] | alt | 52.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.40× (z +13.6) | — |
| [[NCI-H1792 (line)]] | alt | 54.0 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.56× (z +10.4) | — |
| [[NCI-H2347 (line)]] | alt | 81.2 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.54× (z +10.1) | — |
| [[NCI-H460 (line)]] | wt | 51.6 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.96× (z +12.0) | — |
| [[Panc 03.27 (line)]] | alt | 63.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.52× (z +11.6) | — |
| [[SW48 (line)]] | wt | 75.2 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.73× (z +9.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 53.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.71× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 118 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.43× (z +9.3) | — |
| [[C32 (line)]] | wt | 52.9 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.99× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 32.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.05× (z +9.7) | — |
| [[HCT15 (line)]] | alt | 52.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.08× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 65.8 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.62× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 27.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.93× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 61.1 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.64× (z +11.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 61.6 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.45× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 104 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.47× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 51.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.75× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 53.8 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.67× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 62.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.71× (z +9.0) | — |
| [[A-427 (line)]] | wt | 72.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A498 (line)]] | wt | 40.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[AN3 CA (line)]] | alt | 86.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 60.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -8.5) |
| [[H4 (line)]] | wt | 64.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.50× (z +9.1) | — |
| [[RKO (line)]] | wt | 63.5 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.50× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 61.1 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.85× (z +11.1) | — |
| [[SNU-423 (line)]] | alt | 47.9 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.33× (z +9.3) | — |
| [[SW1417 (line)]] | alt | 48.0 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.68× (z +8.6) | — |
| [[A-172 (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 64.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2019), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC7]] | +0.71 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[BRF2]] | +0.70 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[PSMC4]] | +0.68 | +0.71 / +0.63 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[ANKRD23]] | +0.68 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[PSMA1]] | +0.67 | +0.67 / +0.63 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[EFCAB7]] | +0.67 | +0.63 / +0.58 | both halves | 7e-06 | pathway: Hedgehog 'on' state |
| [[PSMC2]] | +0.67 | +0.72 / +0.64 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMC5]] | +0.66 | +0.65 / +0.55 | both halves | 1e-05 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[NRDE2]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 | STRING 588; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[GTF3C3]] | +0.65 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[DCTN4]] | +0.65 | +0.63 / +0.68 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[PSMD3]] | +0.64 | +0.68 / +0.60 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[CWC27]] | +0.64 | +0.59 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises PSMC1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises PSMC1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.833). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-23.1, -8.0); signed map (-23.8, -23.4). **Vector** length 90.9, 26.6% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Antigen processing: Ub, ATP-independent proteasomal degradation* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +11.3 | +14.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.9 | +11.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.0 | +14.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.9 | +6.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.3 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +6.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +5.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +1.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | +0.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.5 | +2.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | -3.7 | +3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | +1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -5.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | +1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.2 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 26S subunit, ATPase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.11 — chr14:90,256,527-90,275,429 (+) |
| Ensembl biotype | protein_coding |
| Also known as | S4, p56, RPT2 |
| Gene groups (HGNC) | AAA ATPases; Proteasome |
| Reactome | 171 pathways, smallest: N-glycan trimming in the ER and Calnexin/Calreticulin cycle; Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC) |
| Matched by | ensembl_id |

**Function**, from UniProt [P62191](https://www.uniprot.org/uniprotkb/P62191) (26S proteasome regulatory subunit 4):

> Component of the 26S proteasome, a multiprotein complex involved in the ATP-dependent degradation of ubiquitinated proteins. This complex plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged proteins, which could impair cellular functions, and by removing proteins whose functions are no longer required. Therefore, the proteasome participates in numerous cellular processes, including cell cycle progression, apoptosis, or DNA damage repair. PSMC1 belongs to …

**Summary**, from NCBI Gene [5700](https://www.ncbi.nlm.nih.gov/gene/5700):

> The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, and a lid, which contains up to 10 non-ATPase subunits. Proteasomes are distributed throughout …

**Accessions** — [HGNC:9547](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9547) · Entrez [5700](https://www.ncbi.nlm.nih.gov/gene/5700) · UniProt [P62191](https://www.uniprot.org/uniprotkb/P62191) · Ensembl [ENSG00000100764](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100764)

## Data

Gene col 2019: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2019); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2019, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2019]; `tensor/DDL_lfc|DDL_z.npy` [2019]; `embed/gene_vectors.npy` [2019]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2019 or target_col == 2019). Every well: [[PSMC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
