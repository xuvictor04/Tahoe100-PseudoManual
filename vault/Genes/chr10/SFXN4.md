---
symbol: "SFXN4"
type: "gene"
col: 11423
ensembl_id: "ENSG00000183605"
name: "sideroflexin 4"
location: "10q26.11"
module: 18
arm: "+"
pooled_cpm: 13.71
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 16
n_dd_up_clean: 10
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# SFXN4

*sideroflexin 4* — 10q26.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.47× (z +6.4, q 1e-07, up in 20 of 41 measured lines) ⚠ toxic. The strongest without an alert is [[EX229 (drug)]] 5 µM: 1.81× (z +5.4, q 1e-05, up in 19 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.434× (z -20.3, q 0e+00, down in 38 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FXN]] (+0.73, fdr 7e-06), [[TSEN2]] (+0.72, fdr 7e-06), [[DTD2]] (+0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DUXAP8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11423.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +6.4 | 1e-07 | 20/41 (C32, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +6.1 | 4e-07 | 23/47 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.81×** | +5.4 | 1e-05 | 19/45 (SW1417, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.75×** | +5.1 | 5e-05 | 15/45 (LoVo, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.75×** | +5.1 | 5e-05 | 13/45 (Hs 766T, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.64×** | +4.5 | 7e-04 | 10/45 (NCI-H460, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.55×** | +4.0 | 0.006 | 9/45 (LoVo, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.46×** | +3.4 | 0.039 | 6/42 (SW480, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.039 | 7/42 (SK-MEL-2, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.040 | 13/46 (SW48, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.040 | 11/45 (LS 180, LoVo, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.072 | 4/43 (A549, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.1 | 0.072 | 5/36 (J82, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.19× | +3.0 | 0.099 | 4/45 (SW1417, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11423.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.434×** | -20.3 | 0e+00 | 38/46 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.620×** | -11.6 | 8e-29 | 32/46 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.561×** | -9.6 | 2e-19 | 28/47 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.677×** | -6.7 | 3e-09 | 21/47 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.689×** | -6.4 | 2e-08 | 20/47 (SW48, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.504×** | -6.2 | 6e-08 | 21/46 (LoVo, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.709×** | -5.9 | 3e-07 | 21/47 (MIA PaCa-2, SW48, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.728×** | -5.4 | 4e-06 | 21/47 (C-33 A, LS 180, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.737×** | -5.0 | 3e-05 | 19/45 (SK-MEL-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.918× | -4.9 | 5e-05 | 5/48 (A498, NCI-H2030, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.764×** | -4.6 | 2e-04 | 13/47 (LOX-IMVI, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.770×** | -4.5 | 4e-04 | 11/46 (AsPC-1, J82, …) | all doses, flat | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.647×** | -3.9 | 0.004 | 11/44 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.799×** | -3.8 | 0.005 | 15/46 (LoVo, SNU-423, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.818×** | -3.4 | 0.023 | 14/45 (A-427, RKO, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.689×** | -3.3 | 0.029 | 13/45 (SW48, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.873× | -3.3 | 0.038 | 14/48 (SW1417, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11423. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 19.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -17.6) |
| [[NCI-H460 (line)]] | wt | 14.6 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -9.6) |
| [[PANC-1 (line)]] | alt | 30.8 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -18.6) |
| [[SW48 (line)]] | wt | 40.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -14.0) |
| [[A-427 (line)]] | wt | 18.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -10.4) |
| [[C-33 A (line)]] | alt | 30.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -15.7) |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.166× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -9.0) |
| [[RKO (line)]] | wt | 23.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -12.3) |
| [[SNU-1 (line)]] | wt | 30.6 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0820× (z -13.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.253× (z -10.8) |
| [[A-172 (line)]] | wt | 8.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +11.8) | — |
| [[A498 (line)]] | wt | 12.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -8.6) |
| [[A549 (line)]] | wt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -8.9) |
| [[BT-474 (line)]] | alt | 6.70 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -9.3) |
| [[C32 (line)]] | wt | 8.53 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -8.5) ⚠ cell-cycle shift, explains ~8% of this change |
| [[HEC-1-A (line)]] | alt | 12.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -9.1) |
| [[LoVo (line)]] | wt | 15.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -14.1) |
| [[SHP-77 (line)]] | alt | 30.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 11.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -10.0) |
| [[SNU-423 (line)]] | alt | 11.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -9.3) |
| [[SW1417 (line)]] | alt | 15.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -8.5) |
| [[SW480 (line)]] | alt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -13.8) |
| [[AN3 CA (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.02 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11423), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FXN]] | +0.73 | +0.73 / +0.73 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 438 |
| [[TSEN2]] | +0.72 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[DTD2]] | +0.71 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[ADAT2]] | +0.69 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[ZNF485]] | +0.68 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[MDN1]] | +0.68 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[SORD]] | +0.67 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[ASB13]] | +0.67 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[EEF1E1]] | +0.66 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[EBPL]] | +0.66 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[ANGEL1]] | +0.66 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[CENPV]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUXAP8]] | B | DUXAP8 activity raises SFXN4's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 1.91× lower at baseline in the lines without DUXAP8 | 0.009 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2 |
| [[ANK2]] | B | ANK2 activity raises SFXN4's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.32× lower at baseline in the lines without ANK2 | 0.087 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.764). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-9.8, -38.0); signed map (-6.4, -53.7). **Vector** length 88.5, 17.5% of its response variance represented; |z| ≥ 3 in 900 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.50 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.7 | +6.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.8 | +6.4 |
|  | [[EX229 (drug)]] 5 µM |  | +3.8 | +5.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.8 | +5.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.6 | +3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.1 | +5.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.4 | -20.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.4 | -6.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.7 | -2.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.4 | -4.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.4 | -4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -3.3 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | sideroflexin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.11 — chr10:119,140,767-119,165,714 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SLC56A4 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors; Solute carrier family 56, sideroflexins |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P4A7](https://www.uniprot.org/uniprotkb/Q6P4A7) (Sideroflexin-4):

> Mitochondrial amino-acid transporter (By similarity). Does not act as a serine transporter: not able to mediate transport of serine into mitochondria.

**Summary**, from NCBI Gene [119559](https://www.ncbi.nlm.nih.gov/gene/119559):

> This gene encodes a member of the sideroflexin family. The encoded protein is a transmembrane protein of the inner mitochondrial membrane, and is required for mitochondrial respiratory homeostasis and erythropoiesis. Mutations in this gene are associated with mitochondriopathy and macrocytic anemia. Alternatively spliced transcript variants have been found in this gene. [provided by RefSeq, Jan 2014]

**Accessions** — [HGNC:16088](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16088) · Entrez [119559](https://www.ncbi.nlm.nih.gov/gene/119559) · UniProt [Q6P4A7](https://www.uniprot.org/uniprotkb/Q6P4A7) · Ensembl [ENSG00000183605](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183605)

## Data

Gene col 11423: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11423); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11423, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11423]; `tensor/DDL_lfc|DDL_z.npy` [11423]; `embed/gene_vectors.npy` [11423]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11423 or target_col == 11423). Every well: [[SFXN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SFXN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
