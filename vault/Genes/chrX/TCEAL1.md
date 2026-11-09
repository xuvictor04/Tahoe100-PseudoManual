---
symbol: "TCEAL1"
type: "gene"
col: 10259
ensembl_id: "ENSG00000172465"
name: "transcription elongation factor A like 1"
location: "Xq22.2"
module: 35
arm: "+"
pooled_cpm: 10.09
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# TCEAL1

*transcription elongation factor A like 1* — Xq22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.15× (z +7.3, q 1e-10, up in 21 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +7.2, q 1e-10, up in 27 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.541× (z -5.9, q 1e-06, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHYH]] (+0.72, fdr 3e-05), [[PIGP]] (+0.71, fdr 1e-05), [[TCEAL4]] (+0.70, fdr 1e-05, ⚠ same locus), [[CREB3L4]] (+0.70, fdr 1e-05); moves opposite to [[FBXW2]] (-0.66, fdr 3e-05), [[TREX2]] (-0.65, fdr 1e-05), [[PPM1F]] (-0.63, fdr 6e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10259.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.15×** | +7.3 | 1e-10 | 21/30 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +7.2 | 1e-10 | 27/42 (HOP62, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +6.7 | 5e-09 | 12/15 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +6.3 | 6e-08 | 26/38 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.71×** | +5.2 | 3e-05 | 17/37 (HEC-1-A, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +5.1 | 4e-05 | 17/46 (RKO, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.37×** | +4.3 | 0.002 | 21/42 (A498, J82, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.55×** | +4.1 | 0.003 | 20/44 (NCI-H2030, A498, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +3.7 | 0.013 | 11/20 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.6 | 0.017 | 15/38 (SK-MEL-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.87×** | +3.1 | 0.082 | 9/39 (NCI-H460, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.082 | 10/45 (SNU-423, SK-MEL-2, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10259.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.541×** | -5.9 | 1e-06 | 27/46 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.544×** | -5.8 | 1e-06 | 24/46 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.569×** | -5.4 | 1e-05 | 27/46 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.591×** | -5.0 | 6e-05 | 24/45 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.615×** | -4.7 | 4e-04 | 18/45 (SW480, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.641×** | -4.3 | 0.002 | 21/45 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.669×** | -3.9 | 0.009 | 16/46 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.686×** | -3.6 | 0.021 | 16/43 (NCI-H23, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 0.721× | -3.1 | 0.11 | 6/46 (HOP62, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10259. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 8.09 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +9.4) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[AsPC-1 (line)]] | alt | 6.74 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0844× (z -9.4) |
| [[C32 (line)]] | wt | 7.93 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0748× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 12.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.87× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 10.2 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0715× (z -11.2) |
| [[A-172 (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.873 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.96 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10259), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHYH]] | +0.72 | +0.74 / +0.43 | both halves | 3e-05 |  |
| [[PIGP]] | +0.71 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[TCEAL4]] | +0.70 | +0.71 / +0.56 | both halves | 1e-05 | same gene group; STRING 963; ⚠ same locus (41.0 kb, same strand: neighbours can correlate without regulation) |
| [[CREB3L4]] | +0.70 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[ZC2HC1C]] | +0.70 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[ZNF428]] | +0.69 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[CA11]] | +0.69 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[PPCS]] | +0.67 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[RWDD2B]] | +0.66 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[LACTB2]] | +0.66 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[PAXIP1-AS2]] | +0.66 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[TCEAL3]] | +0.66 | +0.68 / +0.62 | both halves | 7e-06 | same gene group; STRING 731; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[PLS3-AS1]] | +0.65 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[ATF5]] | +0.65 | +0.57 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW2]] | -0.66 | -0.69 / -0.44 | both halves | 3e-05 |  |
| [[TREX2]] | -0.65 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[PPM1F]] | -0.63 | -0.67 / -0.38 | both halves | 6e-05 |  |
| [[GNB1L]] | -0.62 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[GRK6]] | -0.61 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[TBCD]] | -0.60 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[NUP93]] | -0.59 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[CORO7]] | -0.59 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[WDR5]] | -0.58 | -0.63 / -0.39 | both halves | 6e-05 |  |
| [[TCF3]] | -0.58 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[ATAD3B]] | -0.58 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[ERI1]] | -0.58 | -0.53 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises TCEAL1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TMEM17]] | C | TMEM17 activity raises TCEAL1's level | lines that do not express TMEM17 (3) vs lines expressing it (47) | 2.38× lower at baseline in the lines without TMEM17 | 0.031 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: MNS1, ENSG00000283491, AGK |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.620). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-2.3, 15.4); signed map (19.4, -14.0). **Vector** length 70.0, 13.6% of its response variance represented; |z| ≥ 3 in 724 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.8 | +4.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.6 | +5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +5.2 | +4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +7.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +1.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +2.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.5 | -5.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.3 | -5.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.3 | -5.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -5.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.1 | +0.4 |
|  | [[Pemetrexed (drug)]] 0.5 µM |  | -1.0 | -1.9 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | transcription elongation factor A like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.2 — chrX:103,628,704-103,630,953 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p21, pp21, SIIR, P21, WEX9 |
| Gene groups (HGNC) | Transcription elongation factor A like family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15170](https://www.uniprot.org/uniprotkb/Q15170) (Transcription elongation factor A protein-like 1):

> May be involved in transcriptional regulation. Modulates various viral and cellular promoters in a promoter context-dependent manner. For example, transcription from the FOS promoter is increased, while Rous sarcoma virus (RSV) long terminal repeat (LTR) promoter activity is repressed. Does not bind DNA directly.

**Summary**, from NCBI Gene [9338](https://www.ncbi.nlm.nih.gov/gene/9338):

> This gene encodes a member of the transcription elongation factor A (SII)-like (TCEAL) gene family. Members of this family may function as nuclear phosphoproteins that modulate transcription in a promoter context-dependent manner. The encoded protein is similar to transcription elongation factor A/transcription factor SII and contains a zinc finger-like motif as well as a sequence related to the transcription factor SII Pol II-binding region. It may exert its effects via protein-protein …

**Accessions** — [HGNC:11616](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11616) · Entrez [9338](https://www.ncbi.nlm.nih.gov/gene/9338) · UniProt [Q15170](https://www.uniprot.org/uniprotkb/Q15170) · Ensembl [ENSG00000172465](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172465)

## Data

Gene col 10259: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10259); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10259, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10259]; `tensor/DDL_lfc|DDL_z.npy` [10259]; `embed/gene_vectors.npy` [10259]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10259 or target_col == 10259). Every well: [[TCEAL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCEAL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
