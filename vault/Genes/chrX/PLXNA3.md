---
symbol: "PLXNA3"
type: "gene"
col: 5138
ensembl_id: "ENSG00000130827"
name: "plexin A3"
location: "Xq28"
module: 2
arm: "+"
pooled_cpm: 34.55
n_lines_expressing: 48
n_dd_up: 4
n_dd_down: 15
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# PLXNA3

*plexin A3* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.98× (z +7.6, q 1e-11, up in 36 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.539× (z -9.8, q 6e-20, down in 38 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R12C]] (+0.72, fdr 7e-06), [[GDI1]] (+0.69, fdr 7e-06, ⚠ same locus), [[AMDHD2]] (+0.66, fdr 9e-06), [[NAGK]] (+0.65, fdr 1e-05); moves opposite to [[QRSL1]] (-0.59, fdr 2e-05), [[SMAD1]] (-0.58, fdr 3e-05), [[ARID2]] (-0.57, fdr 9e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5138.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.98×** | +7.6 | 1e-11 | 36/46 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.76×** | +6.3 | 9e-08 | 30/46 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +5.0 | 1e-04 | 25/46 (PANC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.41×** | +3.9 | 0.015 | 26/45 (SK-MEL-2, NCI-H460, …) | two highest doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.35× | +3.2 | 0.13 | 17/45 (SK-MEL-2, SNU-423, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | 1.22× | +3.1 | 0.16 | 20/45 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5138.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.539×** | -9.8 | 6e-20 | 38/46 (NCI-H1792, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.506×** | -7.6 | 6e-12 | 35/46 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.542×** | -6.6 | 6e-09 | 28/46 (A-172, RPMI-7951, …) | rises with dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.556×** | -6.6 | 6e-09 | 34/46 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.594×** | -5.6 | 2e-06 | 27/45 (LOX-IMVI, NCI-H1792, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.421×** | -5.1 | 4e-05 | 35/47 (CFPAC-1, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.633×** | -4.9 | 7e-05 | 27/46 (A-172, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~23% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.658×** | -4.7 | 2e-04 | 26/46 (A-172, H4, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.651×** | -4.5 | 3e-04 | 26/46 (HOP62, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.672×** | -4.5 | 5e-04 | 27/46 (NCI-H1792, HOP62, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.665×** | -4.4 | 5e-04 | 27/46 (RPMI-7951, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.510×** | -3.9 | 0.004 | 25/40 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.735×** | -3.5 | 0.023 | 23/46 (NCI-H23, NCI-H1573, …) | all doses, flat |  |
| [[Riluzole hydrochloride (drug)]] 5 µM |  | **0.808×** | -3.4 | 0.028 | 19/46 (CFPAC-1, A-172, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.755×** | -3.2 | 0.060 | 21/46 (A-172, A-427, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5138. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 99.7 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -16.8) |
| [[RPMI-7951 (line)]] | alt | 28.5 | 0 | 4 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.120× (z -10.9) |
| [[HT-29 (line)]] | alt | 60.6 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.08× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.288× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 57.6 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.323× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 27.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -16.4) |
| [[Panc 03.27 (line)]] | alt | 48.6 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 3.08× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -11.0) |
| [[PANC-1 (line)]] | alt | 26.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.87× (z +10.8) | — |
| [[SW480 (line)]] | alt | 35.5 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.81× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -9.0) |
| [[A549 (line)]] | wt | 17.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.206× (z -8.6) ⚠ cell-cycle shift, explains ~79% of this change |
| [[CFPAC-1 (line)]] | alt | 46.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -15.7) |
| [[CHP-212 (line)]] | wt | 34.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -8.8) |
| [[H4 (line)]] | wt | 49.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.191× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 41.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -8.9) |
| [[Hs 766T (line)]] | wt | 53.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 43.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.78× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 22.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.171× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[MIA PaCa-2 (line)]] | alt | 39.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -14.1) |
| [[NCI-H23 (line)]] | alt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 45.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.321× (z -8.6) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H460 (line)]] | wt | 21.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 48.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -10.2) |
| [[SW 1088 (line)]] | alt | 65.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0568× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 1271 (line)]] | alt | 37.6 | 0 | 1 (1 ⚠) | — | [[Ribociclib (drug)]] 5 µM 0.0513× (z -8.5) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 40.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -10.6) |
| [[SW1417 (line)]] | alt | 51.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -10.3) |
| [[A-427 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.32 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 24.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5138), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R12C]] | +0.72 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[GDI1]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 | ⚠ same locus (14.8 kb, same strand: neighbours can correlate without regulation) |
| [[AMDHD2]] | +0.66 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[NAGK]] | +0.65 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[BAIAP3]] | +0.64 | +0.68 / +0.41 | both halves | 4e-05 |  |
| [[APBB3]] | +0.63 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[GNAI2]] | +0.62 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[DLGAP4]] | +0.62 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[PLCB3]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[HEMK1]] | +0.59 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[FGFRL1]] | +0.59 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[GPSM1]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[TPCN2]] | +0.59 | +0.48 / +0.56 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QRSL1]] | -0.59 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[SMAD1]] | -0.58 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[ARID2]] | -0.57 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[PDS5B]] | -0.54 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[DPY19L1P1]] | -0.54 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[KLHL42]] | -0.51 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[TDRD3]] | -0.51 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[RTN4IP1]] | -0.50 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[TTC39C]] | -0.50 | -0.46 / -0.37 | both halves | 7e-05 |  |
| [[NSMAF]] | -0.50 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[TRAPPC13]] | -0.50 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[ECHDC1]] | -0.50 | -0.53 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers PLXNA3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises PLXNA3's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.608). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (12.7, -3.1); signed map (-20.6, 24.7). **Vector** length 116, 32.3% of its response variance represented; |z| ≥ 3 in 980 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +6.1 | +7.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.6 | +6.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.0 | +5.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.7 | -0.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.0 | +2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +3.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.3 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +0.8 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[Posaconazole (drug)]] 5 µM |  | +2.1 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.5 | -9.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -4.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.2 | -4.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -4.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.5 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | +0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.9 | +0.0 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -2.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | plexin A3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:154,458,281-154,477,779 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SEX, XAP-6, 6.3, Plxn3; previously PLXN4 |
| Gene groups (HGNC) | Plexins; IPT domain containing |
| Reactome | 6 pathways, smallest: SEMA3A-Plexin repulsion signaling by inhibiting Integrin adhesion; CRMPs in Sema3A signaling; Sema3A PAK dependent Axon repulsion |
| Matched by | ensembl_id |

**Function**, from UniProt [P51805](https://www.uniprot.org/uniprotkb/P51805) (Plexin-A3):

> Coreceptor for SEMA3A and SEMA3F. Necessary for signaling by class 3 semaphorins and subsequent remodeling of the cytoskeleton. Plays a role in axon guidance in the developing nervous system. Regulates the migration of sympathetic neurons, but not of neural crest precursors. Required for normal dendrite spine morphology in pyramidal neurons. May play a role in regulating semaphorin-mediated programmed cell death in the developing nervous system. Class 3 semaphorins bind to a complex composed of …

**Summary**, from NCBI Gene [55558](https://www.ncbi.nlm.nih.gov/gene/55558):

> This gene encodes a member of the plexin class of proteins. The encoded protein is a class 3 semaphorin receptor, and may be involved in cytoskeletal remodeling and as well as apoptosis. Studies of a similar gene in zebrafish suggest that it is important for axon pathfinding in the developing nervous system. This gene may be associated with tumor progression. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:9101](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9101) · Entrez [55558](https://www.ncbi.nlm.nih.gov/gene/55558) · UniProt [P51805](https://www.uniprot.org/uniprotkb/P51805) · Ensembl [ENSG00000130827](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130827)

## Data

Gene col 5138: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5138); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5138, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5138]; `tensor/DDL_lfc|DDL_z.npy` [5138]; `embed/gene_vectors.npy` [5138]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5138 or target_col == 5138). Every well: [[PLXNA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLXNA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
