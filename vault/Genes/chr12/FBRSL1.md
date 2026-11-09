---
symbol: "FBRSL1"
type: "gene"
col: 3407
ensembl_id: "ENSG00000112787"
name: "fibrosin like 1"
location: "12q24.33"
module: 2
arm: "+"
pooled_cpm: 38.21
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# FBRSL1

*fibrosin like 1* — 12q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.33× (z +14.3, q 2e-43, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.725× (z -5.5, q 2e-05, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SK-MEL-2 0.138×, RKO 0.299×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (A-427 0.247×, SW480 0.440×; ⚠ cell-cycle shift, explains ~28% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.418×; ⚠ cell-cycle shift, explains ~0% of this change); [[Monocrotaline (drug)]] 0.05 µM in 1 line (AN3 CA 0.112×); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-427 0.364×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R12C]] (+0.74, fdr 7e-06), [[TCF3]] (+0.73, fdr 7e-06), [[SBF1]] (+0.71, fdr 7e-06); moves opposite to [[ZNF711]] (-0.61, fdr 2e-05), [[PLEKHF2]] (-0.61, fdr 1e-05), [[TRMT1L]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[COL18A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3407.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.33×** | +14.3 | 2e-43 | 46/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.01×** | +11.8 | 7e-30 | 44/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.71×** | +9.0 | 3e-17 | 44/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.30×** | +4.5 | 0.001 | 24/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.27×** | +4.1 | 0.006 | 24/47 (SW48, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +4.0 | 0.006 | 25/47 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.25×** | +3.8 | 0.013 | 19/47 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.21×** | +3.2 | 0.098 | 15/47 (J82, MIA PaCa-2, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.29× | +3.1 | 0.11 | 14/46 (SHP-77, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.21× | +3.1 | 0.11 | 10/48 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.20× | +3.1 | 0.11 | 13/47 (LOX-IMVI, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3407.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SK-MEL-2 0.138×, RKO 0.299×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (A-427 0.247×, SW480 0.440×; ⚠ cell-cycle shift, explains ~28% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.418×; ⚠ cell-cycle shift, explains ~0% of this change); [[Monocrotaline (drug)]] 0.05 µM in 1 line (AN3 CA 0.112×); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-427 0.364×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.725×** | -5.5 | 2e-05 | 26/48 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.729×** | -5.2 | 6e-05 | 24/48 (A-427, SW480, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.785×** | -4.1 | 0.006 | 24/47 (PANC-1, RKO, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 5 µM |  | 0.862× | -3.6 | 0.042 | 10/48 (LOX-IMVI, NCI-H1573, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.820× | -3.3 | 0.12 | 14/48 (NCI-H23, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Hexylresorcinol (drug)]] 0.5 µM |  | 0.832× | -3.1 | 0.16 | 11/48 (SHP-77, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Afatinib (drug)]] 0.05 µM |  | 0.874× | -3.1 | 0.17 | 13/48 (A498, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3407. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 42.7 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.42× (z +13.9) | [[Harringtonine (drug)]] 5 µM 0.440× (z -9.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 39.9 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.247× (z -11.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.364× (z -8.6) |
| [[KATO III (line)]] | alt | 33.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.87× (z +11.9) | — |
| [[NCI-H460 (line)]] | wt | 44.8 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 32.9 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.45× (z +9.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.456× (z -8.7) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A549 (line)]] | wt | 40.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.92× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 41.7 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.112× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 47.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 34.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.79× (z +10.8) | — |
| [[LoVo (line)]] | wt | 61.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.33× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 47.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +8.5) ⚠ cell-cycle shift, explains ~13% of this change | — |
| [[LS 180 (line)]] | wt | 46.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.65× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 35.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.06× (z +9.0) | — |
| [[RKO (line)]] | wt | 50.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.299× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 38.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 72.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3407), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R12C]] | +0.74 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[TCF3]] | +0.73 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[SBF1]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[PACS2]] | +0.68 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[SKI]] | +0.67 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[GALNS]] | +0.66 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[NSMF]] | +0.66 | +0.67 / +0.56 | both halves | 1e-05 | same gene group |
| [[EPN1]] | +0.65 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[GPSM1]] | +0.64 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[CORO7]] | +0.64 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[AKT1]] | +0.63 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[MAPKAPK2]] | +0.63 | +0.64 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF711]] | -0.61 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[PLEKHF2]] | -0.61 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[TRMT1L]] | -0.61 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[RBM43]] | -0.56 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[CASC9]] | -0.56 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[KIAA1586]] | -0.56 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[C1orf131]] | -0.56 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[RWDD2B]] | -0.55 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[PPCS]] | -0.55 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[FUNDC1]] | -0.55 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[TCEAL1]] | -0.55 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[GIN1]] | -0.55 | -0.49 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL18A1]] | B | COL18A1 activity lowers FBRSL1's level | lines that do not express COL18A1 (18) vs lines expressing it (32) | 1.32× higher at baseline in the lines without COL18A1 | 0.046 | ⚠ within organs, on part of the lines; also absent: NGFR, CX3CL1, PPP2R2B |
| [[ITPR3]] | B | ITPR3 activity lowers FBRSL1's level | lines that do not express ITPR3 (6) vs lines expressing it (44) | 1.23× higher at baseline in the lines without ITPR3 | 0.060 | ⚠ within organs, on part of the lines; also absent: SAT1, LRRC8E, HTATIP2; its own permutation p |
| [[HDAC6]] | B | HDAC6 activity lowers FBRSL1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.777). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-6.6, -23.6); signed map (-45.2, -8.8). **Vector** length 107, 26.1% of its response variance represented; |z| ≥ 3 in 871 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +8.5 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +8.0 | +2.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.8 | +14.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.0 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.8 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.7 | +3.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +3.4 | +2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.0 | +3.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +4.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.7 | +0.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -6.8 | -5.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.9 | -5.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -5.2 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.3 | -1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.8 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | fibrosin like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.33 — chr12:132,489,551-132,585,188 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1545 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q9HCM7](https://www.uniprot.org/uniprotkb/Q9HCM7) carries no function annotation.

**Summary**, from NCBI Gene [57666](https://www.ncbi.nlm.nih.gov/gene/57666):

> Enables RNA binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29308](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29308) · Entrez [57666](https://www.ncbi.nlm.nih.gov/gene/57666) · UniProt [Q9HCM7](https://www.uniprot.org/uniprotkb/Q9HCM7) · Ensembl [ENSG00000112787](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112787)

## Data

Gene col 3407: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3407); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3407, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3407]; `tensor/DDL_lfc|DDL_z.npy` [3407]; `embed/gene_vectors.npy` [3407]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3407 or target_col == 3407). Every well: [[FBRSL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBRSL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
