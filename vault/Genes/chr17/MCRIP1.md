---
symbol: "MCRIP1"
type: "gene"
col: 13474
ensembl_id: "ENSG00000225663"
name: "MAPK regulated corepressor interacting protein 1"
location: "17q25.3"
module: 3
arm: "+"
pooled_cpm: 19.48
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# MCRIP1

*MAPK regulated corepressor interacting protein 1* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.91× (z +8.2, q 7e-14, up in 29 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.90× (z +8.2, q 7e-14, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.640× (z -5.7, q 5e-06, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF333]] (+0.67, fdr 7e-06), [[WIPF2]] (+0.66, fdr 7e-06), [[B3GAT3]] (+0.64, fdr 7e-06); moves opposite to [[BAG2]] (-0.64, fdr 1e-05), [[ME1]] (-0.56, fdr 1e-05), [[CAPS2]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13474.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.91×** | +8.2 | 7e-14 | 29/39 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.90×** | +8.2 | 7e-14 | 37/47 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.82×** | +7.7 | 3e-12 | 35/47 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +6.7 | 2e-09 | 32/45 (A549, LoVo, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +5.5 | 5e-06 | 24/44 (HEC-1-A, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +5.2 | 2e-05 | 25/47 (SW480, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.41×** | +4.4 | 9e-04 | 18/47 (SW480, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.43×** | +4.4 | 9e-04 | 17/26 (SNU-423, A-172, …) | all doses, flat | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.58×** | +4.2 | 0.002 | 21/46 (RPMI-7951, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.41×** | +4.0 | 0.004 | 17/35 (A498, HS-578T, …) | all doses, flat | composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.54×** | +3.9 | 0.005 | 14/46 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.010 | 19/48 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.74×** | +3.7 | 0.010 | 18/46 (Hs 766T, KATO III, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.50×** | +3.7 | 0.011 | 13/46 (COLO 205, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.22×** | +3.6 | 0.011 | 23/47 (NCI-H2347, KATO III, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.046 | 15/47 (NCI-H1573, SW 900, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.064 | 9/47 (HS-578T, NCI-H2030, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.39×** | +3.0 | 0.076 | 14/45 (AsPC-1, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13474.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.640×** | -5.7 | 5e-06 | 26/47 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.749×** | -5.3 | 4e-05 | 25/47 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.652×** | -5.2 | 4e-05 | 27/47 (J82, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.714×** | -4.3 | 0.002 | 22/47 (C-33 A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 0.775× | -3.3 | 0.11 | 15/47 (SW480, BT-474, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.780× | -3.2 | 0.13 | 16/47 (SK-MEL-2, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13474. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 13.4 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.57× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.194× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[A549 (line)]] | wt | 29.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 24.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -10.0) |
| [[HOP62 (line)]] | alt | 28.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 11.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +8.8) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[NCI-H460 (line)]] | wt | 6.96 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 14.8 | 0 | 1 | — | [[Pemigatinib (drug)]] 0.05 µM 0.0691× (z -12.3) |
| [[A-172 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13474), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF333]] | +0.67 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[WIPF2]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[B3GAT3]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[GALNT11]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[PPP1R14B]] | +0.61 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[VPS37C]] | +0.59 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[FAAP20]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[KXD1]] | +0.58 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[TOLLIP]] | +0.57 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[SLC39A13]] | +0.55 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[COMMD6]] | +0.55 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[SH3GL1]] | +0.55 | +0.51 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAG2]] | -0.64 | -0.67 / -0.53 | both halves | 1e-05 |  |
| [[ME1]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[CAPS2]] | -0.55 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[TYW3]] | -0.54 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[HSPB8]] | -0.53 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[PSMD12]] | -0.53 | -0.47 / -0.57 | both halves | 2e-05 | pathway: Adherens junctions interactions |
| [[DLG2]] | -0.52 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[PSMD11]] | -0.52 | -0.47 / -0.51 | both halves | 2e-05 | pathway: Adherens junctions interactions |
| [[PSMC3]] | -0.52 | -0.47 / -0.50 | both halves | 2e-05 | pathway: Adherens junctions interactions |
| [[USP7]] | -0.51 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[HNRNPA2B1]] | -0.51 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[DNAJB4]] | -0.50 | -0.47 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises MCRIP1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.498). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-16.7, -4.3); signed map (-31.0, 12.7). **Vector** length 75.6, 14.7% of its response variance represented; |z| ≥ 3 in 757 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.4 | +7.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.3 | +8.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.5 | +6.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +8.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.3 | +2.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.0 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +3.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.4 | -5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -3.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.0 | -5.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.8 | -2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -2.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | MAPK regulated corepressor interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:81,822,361-81,833,302 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GRAN2, MCRIP; previously FAM195B |
| Reactome | 9 pathways, smallest: Negative Regulation of CDH1 Gene Transcription; Regulation of CDH1 Gene Transcription; Regulation of CDH1 Expression and Function |
| Matched by | ensembl_id |

**Function**, from UniProt [C9JLW8](https://www.uniprot.org/uniprotkb/C9JLW8) (Mapk-regulated corepressor-interacting protein 1):

> The phosphorylation status of MCRIP1 functions as a molecular switch to regulate epithelial-mesenchymal transition. Unphosphorylated MCRIP1 binds to and inhibits the transcriptional corepressor CTBP(s). When phosphorylated by MAPK/ERK, MCRIP1 releases CTBP(s) resulting in transcriptional silencing of the E-cadherin gene and induction of epithelial-mesenchymal transition.

**Summary**, from NCBI Gene [348262](https://www.ncbi.nlm.nih.gov/gene/348262):

> Involved in regulation of epithelial to mesenchymal transition. Located in cytoplasmic stress granule and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28007](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28007) · Entrez [348262](https://www.ncbi.nlm.nih.gov/gene/348262) · UniProt [C9JLW8](https://www.uniprot.org/uniprotkb/C9JLW8) · Ensembl [ENSG00000225663](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225663)

## Data

Gene col 13474: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13474); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13474, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13474]; `tensor/DDL_lfc|DDL_z.npy` [13474]; `embed/gene_vectors.npy` [13474]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13474 or target_col == 13474). Every well: [[MCRIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCRIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
