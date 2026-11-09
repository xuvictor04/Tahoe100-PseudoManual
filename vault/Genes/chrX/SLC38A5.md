---
symbol: "SLC38A5"
type: "gene"
col: 302
ensembl_id: "ENSG00000017483"
name: "solute carrier family 38 member 5"
location: "Xp11.23"
module: 4
arm: "+"
pooled_cpm: 6.77
n_lines_expressing: 15
n_dd_up: 8
n_dd_down: 5
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# SLC38A5

*solute carrier family 38 member 5* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.75× (z +11.9, q 8e-30, up in 8 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.53× (z +3.2, q 0.094, up in 3 of 12 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 3.91×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.429× (z -6.5, q 3e-08, down in 10 of 12 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGMAT]] (+0.56, fdr 3e-05), [[FAM222A-AS1]] (+0.52, fdr 2e-05), [[LINC01357]] (+0.52, fdr 1e-04); moves opposite to [[SRGAP2B]] (-0.37, fdr 2e-04), [[TNRC6B]] (-0.36, fdr 2e-04).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 4 go from it, the strongest it → [[SLC12A8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 302.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 3.91×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.75×** | +11.9 | 8e-30 | 8/10 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.98×** | +11.8 | 1e-29 | 5/7 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.98×** | +7.7 | 2e-12 | 3/7 (KATO III, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.6 | 0.038 | 3/10 (HT-29, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +3.5 | 0.061 | 3/11 (LoVo, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.4 | 0.061 | 3/11 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.56×** | +3.4 | 0.061 | 2/7 (SW480, NCI-H1792) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +3.2 | 0.094 | 3/12 (SW480, NCI-H460, …) | top dose only |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.52× | +3.1 | 0.10 | 0/11 | top dose only | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | 2.10× | +3.1 | 0.11 | 1/11 (NCI-H460) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.5 µM |  | 1.50× | +3.1 | 0.11 | 3/11 (NCI-H460, SW48, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 302.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.429×** | -6.5 | 3e-08 | 10/12 (SW480, RKO, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.431×** | -6.4 | 3e-08 | 10/12 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.512×** | -5.1 | 5e-05 | 11/12 (NCI-H1792, SW480, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.604×** | -3.9 | 0.015 | 7/11 (SW48, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.649×** | -3.3 | 0.098 | 12/12 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~15% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 302. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 38.6 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.139× (z -11.5) |
| [[KATO III (line)]] | alt | 30.8 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +8.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.162× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 26.7 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.125× (z -15.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.146× (z -10.3) |
| [[SW480 (line)]] | alt | 40.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.116× (z -14.9) |
| [[NCI-H460 (line)]] | wt | 12.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.157× (z -10.5) |
| [[LoVo (line)]] | wt | 10.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -8.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.202× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 17.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.158× (z -9.5) |
| [[SW48 (line)]] | wt | 11.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0474× (z -10.5) |
| [[A-172 (line)]] | wt | 0.737 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.642 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.499 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.445 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.557 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.571 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.644 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.778 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.623 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.971 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.935 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.967 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.593 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.559 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.538 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.597 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.948 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.815 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.614 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.565 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.641 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.905 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.755 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 302), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGMAT]] | +0.56 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[FAM222A-AS1]] | +0.52 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[LINC01357]] | +0.52 | +0.55 / +0.33 | both halves | 1e-04 |  |
| [[ADAT2]] | +0.50 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[LARGE2]] | +0.50 | +0.46 / +0.35 | both halves | 1e-04 |  |
| [[KAT2A]] | +0.50 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[LAD1]] | +0.49 | +0.36 / +0.54 | both halves | 1e-04 |  |
| [[SLC17A9]] | +0.49 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[SPTBN2]] | +0.48 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[CGREF1]] | +0.48 | +0.39 / +0.40 | both halves | 5e-05 |  |
| [[TSPOAP1]] | +0.47 | +0.43 / +0.35 | both halves | 1e-04 |  |
| [[CENPV]] | +0.47 | +0.46 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGAP2B]] | -0.37 | -0.32 / -0.35 | both halves | 2e-04 |  |
| [[TNRC6B]] | -0.36 | -0.31 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SLC38A5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SLC17A9]] | C | SLC17A9 activity raises SLC38A5's level | lines that do not express SLC17A9 (27) vs lines expressing it (23) | 2.82× lower at baseline in the lines without SLC17A9 | 0.012 | ⚠ within organs, on part of the lines; also absent: UGT1A9, MT1G, TTC22; co-absent with the target |
| [[ACSL5]] | C | ACSL5 activity raises SLC38A5's level | lines that do not express ACSL5 (24) vs lines expressing it (26) | 2.83× lower at baseline in the lines without ACSL5 | 0.020 | ⚠ within organs, on part of the lines; also absent: TNFRSF14-AS1, IL20RA, TINAGL1; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC12A8]] | B | SLC38A5 activity raises SLC12A8's level | lines that do not express SLC38A5 (35) vs lines expressing it (15) | 1.90× lower at baseline in the lines without SLC38A5 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: XIST, HEPH, KRT5 |
| [[SLC12A8]] | B | SLC38A5 activity strengthens SLC12A8's drug response | lines that do not express SLC38A5 (20) vs lines expressing it (11) | the lines without SLC38A5 respond 0.56× as strongly (z diff +2.56); strongest at Panobinostat 5 µM: 0.74x vs 0.31x (z diff +4.3) | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: XIST, HEPH, KRT5; target measured in part of the lines; artifact flags |
| [[SLC17A9]] | C | SLC38A5 activity raises SLC17A9's level | lines that do not express SLC38A5 (35) vs lines expressing it (15) | 3.30× lower at baseline in the lines without SLC38A5 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: XIST, HEPH, KRT5; co-absent with the target |
| [[PKP1]] | C | SLC38A5 activity raises PKP1's level | lines that do not express SLC38A5 (35) vs lines expressing it (15) | 2.20× lower at baseline in the lines without SLC38A5 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: XIST, HEPH, KRT5; co-absent with the target |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.273). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (0.2, 44.6); signed map (-1.4, 27.5). **Vector** length 31.0, 8.20% of its response variance represented; |z| ≥ 3 in 228 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +7.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.1 | +2.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +11.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +3.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.2 | +1.4 |
|  | [[EX229 (drug)]] 5 µM |  | +1.1 | +1.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.0 | +1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +0.9 | +1.2 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -1.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.7 | -2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.7 | -1.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.6 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.6 | -2.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.5 | -2.4 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -0.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 38 member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:48,458,537-48,470,260 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SN2, JM24, SNAT5 |
| Gene groups (HGNC) | Solute carrier family 38 |
| Reactome | 4 pathways, smallest: Amino acid transport across the plasma membrane; SLC-mediated transport of amino acids; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUX1](https://www.uniprot.org/uniprotkb/Q8WUX1) (Sodium-coupled neutral amino acid transporter 5):

> Symporter that cotransports neutral amino acids and sodium ions, coupled to an H(+) antiporter activity. Releases L-glutamine and glycine from astroglial cells and may participate in the glutamate/GABA-L-glutamine cycle and the NMDA receptors activation (By similarity). In addition, contributes significantly to L-glutamine uptake in retina, namely in ganglion and Mueller cells therefore, participates in the retinal glutamate-glutamine cycle (By similarity). The transport activity is pH …

**Summary**, from NCBI Gene [92745](https://www.ncbi.nlm.nih.gov/gene/92745):

> The protein encoded by this gene is a system N sodium-coupled amino acid transporter. The encoded protein transports glutamine, asparagine, histidine, serine, alanine, and glycine across the cell membrane, but does not transport charged amino acids, imino acids, or N-alkylated amino acids. Alternative splicing results in multiple transcript variants, but the full-length nature of some of these variants has not been determined. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:18070](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18070) · Entrez [92745](https://www.ncbi.nlm.nih.gov/gene/92745) · UniProt [Q8WUX1](https://www.uniprot.org/uniprotkb/Q8WUX1) · Ensembl [ENSG00000017483](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000017483)

## Data

Gene col 302: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 302); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 302, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 302]; `tensor/DDL_lfc|DDL_z.npy` [302]; `embed/gene_vectors.npy` [302]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 302 or target_col == 302). Every well: [[SLC38A5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC38A5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
