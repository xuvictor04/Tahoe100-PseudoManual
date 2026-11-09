---
symbol: "VPS33A"
type: "gene"
col: 6338
ensembl_id: "ENSG00000139719"
name: "VPS33A core subunit of CORVET and HOPS complexes"
location: "12q24.31"
module: 89
arm: "+"
pooled_cpm: 23.31
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# VPS33A

*VPS33A core subunit of CORVET and HOPS complexes* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.30× (z +7.4, q 1e-10, up in 24 of 48 measured lines) ⚠ cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.39× (z +6.5, q 2e-08, up in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LOX-IMVI 4.01×, A-172 2.77×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.625× (z -13.2, q 5e-37, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALKBH3]] (+0.73, fdr 7e-06), [[POLR3F]] (+0.72, fdr 7e-06), [[WASHC2C]] (+0.69, fdr 7e-06); moves opposite to [[ARHGAP26]] (-0.58, fdr 2e-05), [[ZSWIM6]] (-0.57, fdr 4e-05), [[EPB41L2]] (-0.56, fdr 2e-05).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[EMP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6338.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LOX-IMVI 4.01×, A-172 2.77×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.30×** | +7.4 | 1e-10 | 24/48 (RKO, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +6.5 | 2e-08 | 27/48 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.29×** | +5.1 | 6e-05 | 20/48 (SW1417, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.9 | 2e-04 | 13/48 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +4.4 | 0.001 | 18/44 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.27×** | +4.3 | 0.002 | 13/48 (NCI-H1792, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.004 | 10/47 (NCI-H1792, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.16× | +4.0 | 0.005 | 11/48 (SW1417, SHP-77, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.5 | 0.026 | 6/48 (hTERT-HPNE, MIA PaCa-2, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.041 | 11/47 (RPMI-7951, AsPC-1, …) | rises with dose |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.12 | 2/47 (HepG2/C3A, NCI-H2347) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6338.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.625×** | -13.2 | 5e-37 | 42/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.614×** | -9.7 | 1e-19 | 28/47 (LS 180, SW48, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.644×** | -8.8 | 4e-16 | 33/47 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.649×** | -8.6 | 1e-15 | 27/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.673×** | -6.7 | 2e-09 | 30/47 (PANC-1, SW 900, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **0.783×** | -4.5 | 6e-04 | 20/46 (SW 900, HS-578T, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.800×** | -4.4 | 8e-04 | 16/48 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.804×** | -4.0 | 0.004 | 20/48 (PANC-1, COLO 205, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 0.834× | -3.6 | 0.020 | 11/47 (NCI-H23, SW480, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.694×** | -3.5 | 0.030 | 16/46 (SW480, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.703×** | -3.4 | 0.041 | 10/46 (PANC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6338. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 27.0 | 0 | 3 (1 ⚠) | — | [[Tucidinostat (drug)]] 5 µM 0.488× (z -11.3) |
| [[A549 (line)]] | wt | 22.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 19.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C32 (line)]] | wt | 23.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 19.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.246× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[LoVo (line)]] | wt | 26.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 23.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +15.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LS 180 (line)]] | wt | 15.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H460 (line)]] | wt | 29.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.451× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[PANC-1 (line)]] | alt | 30.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.477× (z -8.9) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW 900 (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.211× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~48% of this change |
| [[SW1417 (line)]] | alt | 25.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.320× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SW48 (line)]] | wt | 20.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A-427 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6338), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALKBH3]] | +0.73 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[POLR3F]] | +0.72 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[WASHC2C]] | +0.69 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[PAAF1]] | +0.68 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[BRAP]] | +0.67 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[SLC38A7]] | +0.67 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[WASHC2A]] | +0.64 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[TMEM199]] | +0.63 | +0.60 / +0.60 | both halves | 7e-06 | STRING 497 |
| [[INTS14]] | +0.63 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[MTERF4]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[GATB]] | +0.61 | +0.59 / +0.57 | both halves | 8e-06 |  |
| [[MAPKAPK5]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP26]] | -0.58 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[ZSWIM6]] | -0.57 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[EPB41L2]] | -0.56 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[JPT1]] | -0.55 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[SH3GL3]] | -0.55 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[GLS]] | -0.55 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[DIAPH1]] | -0.54 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[PKM]] | -0.53 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[RCOR1]] | -0.53 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[CALM2]] | -0.53 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[CCNYL1]] | -0.53 | -0.39 / -0.57 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EMP1]] | B | EMP1 activity lowers VPS33A's level | lines that do not express EMP1 (10) vs lines expressing it (40) | 1.38× higher at baseline in the lines without EMP1 | 0.070 | ⚠ within organs, on part of the lines |
| [[SH3GL3]] | B | SH3GL3 activity lowers VPS33A's level | lines that do not express SH3GL3 (21) vs lines expressing it (29) | 1.17× higher at baseline in the lines without SH3GL3 | 0.082 | ⚠ within organs, on part of the lines; also absent: S1PR3, SPANXA2-OT1, SALL1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.758). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-44.2, 7.7); signed map (-9.3, -17.8). **Vector** length 82.3, 16.0% of its response variance represented; |z| ≥ 3 in 767 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +5.0 | +7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.9 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +6.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +0.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +3.3 | +5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +1.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +1.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.9 | +2.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.7 | -13.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.5 | -8.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | -4.8 | -4.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -2.8 | -9.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.4 | -2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -0.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | VPS33A core subunit of CORVET and HOPS complexes |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:122,229,564-122,266,502 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | HOPS complex; CORVET complex; SM family of SNARE chaperones |
| Reactome | 5 pathways, smallest: SARS-CoV-2 modulates autophagy; SARS-CoV-2-host interactions; SARS-CoV-2 Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96AX1](https://www.uniprot.org/uniprotkb/Q96AX1) (Vacuolar protein sorting-associated protein 33A):

> Plays a role in vesicle-mediated protein trafficking to lysosomal compartments including the endocytic membrane transport and autophagic pathways. Believed to act as a core component of the putative HOPS and CORVET endosomal tethering complexes which are proposed to be involved in the Rab5-to-Rab7 endosome conversion probably implicating MON1A/B, and via binding SNAREs and SNARE complexes to mediate tethering and docking events during SNARE-mediated membrane fusion. The HOPS complex is proposed …

**Summary**, from NCBI Gene [65082](https://www.ncbi.nlm.nih.gov/gene/65082):

> This gene encodes a tethering protein and a core subunit of the homotypic fusion and protein sorting (HOPS) complex. The HOPS complex and a second endosomal tethering complex called the class C core vacuole/endosome tethering (CORVET) complex, perform diverse functions in endocytosis including membrane tethering, RabGTPase interaction, activation and proofreading of synaptic-soluble N-ethylmaleimide-sensitive factor attachment receptor (SNARE) assembly to drive membrane fusion, and …

**Accessions** — [HGNC:18179](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18179) · Entrez [65082](https://www.ncbi.nlm.nih.gov/gene/65082) · UniProt [Q96AX1](https://www.uniprot.org/uniprotkb/Q96AX1) · Ensembl [ENSG00000139719](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139719)

## Data

Gene col 6338: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6338); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6338, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6338]; `tensor/DDL_lfc|DDL_z.npy` [6338]; `embed/gene_vectors.npy` [6338]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6338 or target_col == 6338). Every well: [[VPS33A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS33A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
