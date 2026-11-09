---
symbol: "ABRACL"
type: "gene"
col: 7088
ensembl_id: "ENSG00000146386"
name: "ABRA C-terminal like"
location: "6q24.1"
module: 46
arm: "+"
pooled_cpm: 17.4
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# ABRACL

*ABRA C-terminal like* — 6q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.23× (z +11.9, q 8e-30, up in 36 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.45× (z +5.5, q 4e-06, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.449× (z -8.3, q 7e-14, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (80 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LACTB2]] (+0.61, fdr 2e-05), [[MCOLN3]] (+0.61, fdr 4e-04), [[VSIG10]] (+0.57, fdr 4e-05); moves opposite to [[MATCAP1]] (-0.57, fdr 1e-04), [[SLX4]] (-0.56, fdr 9e-05), [[TPCN2]] (-0.51, fdr 1e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7088.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.23×** | +11.9 | 8e-30 | 36/39 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.80×** | +10.3 | 2e-22 | 26/29 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.12×** | +7.2 | 1e-10 | 27/36 (J82, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.77×** | +5.9 | 4e-07 | 29/46 (NCI-H460, SW 900, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.70×** | +5.6 | 3e-06 | 33/44 (HT-29, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.5 | 4e-06 | 31/48 (HOP62, HEC-1-A, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +5.3 | 1e-05 | 26/41 (HOP62, LS 180, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.9 | 6e-05 | 29/41 (CFPAC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.4 | 7e-04 | 21/46 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.006 | 20/48 (SNU-423, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.045 | 19/47 (HOP62, LS 180, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.071 | 15/48 (AsPC-1, NCI-H661, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | 1.35× | +3.0 | 0.11 | 10/46 (J82, CHP-212, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.22× | +3.0 | 0.11 | 14/48 (NCI-H460, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7088.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.449×** | -8.3 | 7e-14 | 36/47 (KATO III, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.455×** | -8.2 | 9e-14 | 36/47 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.526×** | -6.6 | 6e-09 | 32/47 (KATO III, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7088. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 26.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.157× (z -11.5) |
| [[A-172 (line)]] | wt | 25.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.194× (z -10.8) |
| [[J82 (line)]] | alt | 28.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.228× (z -9.5) |
| [[SW480 (line)]] | alt | 11.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.05× (z +9.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.242× (z -8.6) |
| [[A498 (line)]] | wt | 15.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +9.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 38.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.122× (z -8.5) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HOP62 (line)]] | alt | 9.89 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.47× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 27.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -8.8) |
| [[LoVo (line)]] | wt | 25.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 40.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.260× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 13.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.23× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 33.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.317× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 10.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.77× (z +11.0) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 26.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.235× (z -9.5) |
| [[RKO (line)]] | wt | 34.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 13.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -9.0) |
| [[SW48 (line)]] | wt | 30.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -9.6) |
| [[A-427 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.71 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7088), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 17 of them with an alert (⚠; 17 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LACTB2]] | +0.61 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[MCOLN3]] | +0.61 | +0.62 / +0.25 | both halves | 4e-04 |  |
| [[VSIG10]] | +0.57 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[ST7]] | +0.56 | +0.46 / +0.27 | both halves | 3e-04 |  |
| [[GRIP1]] | +0.56 | +0.44 / +0.37 | both halves | 9e-05 |  |
| [[PHACTR2]] | +0.56 | +0.50 / +0.28 | both halves | 3e-04 |  |
| [[BTC]] | +0.55 | +0.42 / +0.36 | both halves | 9e-05 |  |
| [[NINJ2]] | +0.55 | +0.36 / +0.18 | ⚠ not reproduced | 1e-03 |  |
| [[HOXB7]] | +0.55 | +0.37 / +0.39 | both halves | 8e-05 |  |
| [[C10orf95-AS1]] | +0.55 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[ANXA2R-AS1]] | +0.54 | +0.49 / +0.22 | both halves | 6e-04 |  |
| [[TBC1D9]] | +0.54 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[TMEM35B]] | +0.54 | +0.41 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MATCAP1]] | -0.57 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[SLX4]] | -0.56 | -0.37 / -0.40 | both halves | 9e-05 |  |
| [[TPCN2]] | -0.51 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[SCART1]] | -0.51 | -0.27 / -0.42 | both halves | 3e-04 |  |
| [[SPPL2B]] | -0.50 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[INTS11]] | -0.50 | -0.49 / -0.27 | both halves | 3e-04 |  |
| [[GNAI2]] | -0.49 | -0.39 / -0.06 | ⚠ not reproduced | 0.004 |  |
| [[IFT122]] | -0.48 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[STUB1]] | -0.48 | -0.34 / +0.07 | ⚠ not reproduced | 1.00 |  |
| [[NPHP4]] | -0.48 | -0.32 / -0.23 | both halves | 5e-04 |  |
| [[ASCC2]] | -0.47 | -0.37 / -0.26 | both halves | 4e-04 |  |
| [[PORCN]] | -0.47 | -0.38 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[DGKD]] | -0.47 | -0.39 / -0.21 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ABRACL's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.535). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (18.4, 13.8); signed map (40.1, -17.3). **Vector** length 70.4, 15.3% of its response variance represented; |z| ≥ 3 in 680 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +4.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.4 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +1.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +3.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.1 | +2.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.2 | -8.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.0 | -8.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.2 | -6.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | -1.2 | -2.1 |
|  | [[Quinestrol (drug)]] 5 µM |  | -1.1 | -1.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -0.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ABRA C-terminal like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.1 — chr6:139,028,745-139,043,302 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRO2013, HSPC280, Costars; previously C6orf115 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P1F3](https://www.uniprot.org/uniprotkb/Q9P1F3) (Costars family protein ABRACL):

> Associates with the actin cytoskeleton and may modulate actin dynamics, in favor of increasing the relative content of F-actin, therefore may play a role in cell migration. May be acting by inhibiting CFL1-mediated actin depolymerization.

**Summary**, from NCBI Gene [58527](https://www.ncbi.nlm.nih.gov/gene/58527):

> Predicted to be involved in regulation of actin filament-based process. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21230](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21230) · Entrez [58527](https://www.ncbi.nlm.nih.gov/gene/58527) · UniProt [Q9P1F3](https://www.uniprot.org/uniprotkb/Q9P1F3) · Ensembl [ENSG00000146386](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146386)

## Data

Gene col 7088: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7088); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7088, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7088]; `tensor/DDL_lfc|DDL_z.npy` [7088]; `embed/gene_vectors.npy` [7088]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7088 or target_col == 7088). Every well: [[ABRACL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABRACL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
