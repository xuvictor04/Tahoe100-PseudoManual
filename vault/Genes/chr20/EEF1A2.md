---
symbol: "EEF1A2"
type: "gene"
col: 2096
ensembl_id: "ENSG00000101210"
name: "eukaryotic translation elongation factor 1 alpha 2"
location: "20q13.33"
module: 2
arm: "+"
pooled_cpm: 19.41
n_lines_expressing: 39
n_dd_up: 6
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# EEF1A2

*eukaryotic translation elongation factor 1 alpha 2* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.00× (z +8.4, q 2e-14, up in 21 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 1.77× (z +7.0, q 9e-10, up in 23 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A498 3.12×, SW1417 2.60×, SW 900 2.32×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 3.80×, MIA PaCa-2 3.67×, A498 3.89×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 3.04×, A498 3.48×; ⚠ toxic; transcription drop); [[Tucidinostat (drug)]] 5 µM in 1 line (Hs 766T 3.99×).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.567× (z -9.6, q 6e-19, down in 29 of 36 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EMD]] (+0.60, fdr 2e-05), [[RMRP]] (+0.59, fdr 2e-05), [[APBB3]] (+0.59, fdr 3e-05); moves opposite to [[AGAP4]] (-0.46, fdr 6e-05), [[ORC2]] (-0.45, fdr 2e-04), [[PIK3R4]] (-0.43, fdr 2e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[KCNC3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2096.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A498 3.12×, SW1417 2.60×, SW 900 2.32×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 3.80×, MIA PaCa-2 3.67×, A498 3.89×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 3.04×, A498 3.48×; ⚠ toxic; transcription drop); [[Tucidinostat (drug)]] 5 µM in 1 line (Hs 766T 3.99×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +8.4 | 2e-14 | 21/31 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.77×** | +7.0 | 9e-10 | 23/36 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.83×** | +6.8 | 2e-09 | 18/27 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +6.7 | 3e-09 | 14/22 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +5.9 | 3e-07 | 17/37 (Hs 766T, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.56×** | +5.4 | 7e-06 | 19/32 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2096.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.567×** | -9.6 | 6e-19 | 29/36 (SK-MEL-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.653×** | -5.0 | 2e-04 | 19/36 (Hs 766T, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.702×** | -4.3 | 0.003 | 18/37 (SK-MEL-2, C-33 A, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.706×** | -4.2 | 0.003 | 17/37 (NCI-H1792, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.715×** | -4.1 | 0.005 | 19/36 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.709×** | -4.0 | 0.007 | 21/36 (LOX-IMVI, BT-474, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.796×** | -3.8 | 0.010 | 18/37 (A549, HOP62, …) | top dose only | position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.746×** | -3.6 | 0.026 | 16/37 (HOP62, SHP-77, …) | inconsistent across doses |  |
| [[Berbamine (dihydrochloride) (drug)]] 0.05 µM |  | 0.763× | -3.0 | 0.15 | 7/36 (A549, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2096. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 18.3 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 34.5 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -11.7) |
| [[HCT15 (line)]] | alt | 22.1 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0676× (z -12.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -8.8) |
| [[C-33 A (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -11.4) ⚠ cell-cycle shift, explains ~55% of this change |
| [[H4 (line)]] | wt | 29.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -9.1) |
| [[Hs 766T (line)]] | wt | 11.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.99× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.67× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 35.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -11.0) ⚠ cell-cycle shift, explains ~55% of this change |
| [[PANC-1 (line)]] | alt | 19.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 8.02 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0712× (z -10.3) |
| [[SW 900 (line)]] | alt | 52.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW1417 (line)]] | alt | 42.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW480 (line)]] | alt | 18.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.80× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.29 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.48 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.44 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.84 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2096), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMD]] | +0.60 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[RMRP]] | +0.59 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[APBB3]] | +0.59 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[LZTS3]] | +0.56 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[CACNB1]] | +0.56 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[TPPP]] | +0.55 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[TNKS1BP1]] | +0.55 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[ATP1A3]] | +0.54 | +0.31 / +0.54 | both halves | 2e-04 |  |
| [[FOXO6]] | +0.54 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[KIF5C]] | +0.53 | +0.25 / +0.63 | both halves | 4e-04 |  |
| [[RAP1GAP]] | +0.52 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[SYT7]] | +0.52 | +0.44 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGAP4]] | -0.46 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[ORC2]] | -0.45 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[PIK3R4]] | -0.43 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[ATR]] | -0.43 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[BMS1P1]] | -0.42 | -0.37 / -0.47 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises EEF1A2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[KCNC3]] | B | KCNC3 activity raises EEF1A2's level | lines that do not express KCNC3 (9) vs lines expressing it (41) | 2.68× lower at baseline in the lines without KCNC3 | 0.064 | ⚠ within organs, on part of the lines |
| [[HDAC6]] | B | HDAC6 activity raises EEF1A2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity raises EEF1A2's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNC3]] | B | EEF1A2 activity raises KCNC3's level | lines that do not express EEF1A2 (11) vs lines expressing it (39) | 2.92× lower at baseline in the lines without EEF1A2 | 0.037 | ⚠ within organs, on part of the lines; also absent: NRG2, RRAGD, RAB39A |
| [[PPFIA4]] | B | EEF1A2 activity raises PPFIA4's level | lines that do not express EEF1A2 (11) vs lines expressing it (39) | 2.18× lower at baseline in the lines without EEF1A2 | 0.058 | ⚠ within organs, on part of the lines; also absent: NRG2, RRAGD, RAB39A |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.393). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-8.2, 32.3); signed map (-3.5, 23.2). **Vector** length 74.2, 16.1% of its response variance represented; |z| ≥ 3 in 665 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +5.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +8.4 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +2.2 | +0.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.8 | +2.0 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.5 | -5.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.4 | -9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -3.8 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.2 | -1.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -2.0 | -3.6 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.9 | -1.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.7 | -1.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.5 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation elongation factor 1 alpha 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:63,488,013-63,499,239 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EEF1AL, HS1; previously STNL, STN |
| Gene groups (HGNC) | Translational GTPases |
| Reactome | 2 pathways, smallest: Eukaryotic Translation Elongation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q05639](https://www.uniprot.org/uniprotkb/Q05639) (Elongation factor 1-alpha 2):

> Translation elongation factor that catalyzes the GTP-dependent binding of aminoacyl-tRNA (aa-tRNA) to the A-site of ribosomes during the elongation phase of protein synthesis. Base pairing between the mRNA codon and the aa-tRNA anticodon promotes GTP hydrolysis, releasing the aa-tRNA from EEF1A1 and allowing its accommodation into the ribosome (By similarity). The growing protein chain is subsequently transferred from the P-site peptidyl tRNA to the A-site aa-tRNA, extending it by one amino …

**Summary**, from NCBI Gene [1917](https://www.ncbi.nlm.nih.gov/gene/1917):

> This gene encodes an isoform of the alpha subunit of the elongation factor-1 complex, which is responsible for the enzymatic delivery of aminoacyl tRNAs to the ribosome. This isoform (alpha 2) is expressed in brain, heart and skeletal muscle, and the other isoform (alpha 1) is expressed in brain, placenta, lung, liver, kidney, and pancreas. This gene may be critical in the development of ovarian cancer. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:3192](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3192) · Entrez [1917](https://www.ncbi.nlm.nih.gov/gene/1917) · UniProt [Q05639](https://www.uniprot.org/uniprotkb/Q05639) · Ensembl [ENSG00000101210](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101210)

## Data

Gene col 2096: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2096); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2096, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2096]; `tensor/DDL_lfc|DDL_z.npy` [2096]; `embed/gene_vectors.npy` [2096]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2096 or target_col == 2096). Every well: [[EEF1A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EEF1A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
