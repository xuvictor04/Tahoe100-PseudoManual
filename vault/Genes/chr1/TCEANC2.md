---
symbol: "TCEANC2"
type: "gene"
col: 3775
ensembl_id: "ENSG00000116205"
name: "transcription elongation factor A N-terminal and central domain containing 2"
location: "1p32.3"
module: 61
arm: "+"
pooled_cpm: 12.32
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# TCEANC2

*transcription elongation factor A N-terminal and central domain containing 2* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +11.2, q 2e-26, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.657× (z -9.6, q 6e-19, down in 29 of 46 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.565× (z -9.2, q 8e-18, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METTL4]] (+0.67, fdr 1e-05), [[POLR1HASP]] (+0.64, fdr 1e-05), [[PAAF1]] (+0.63, fdr 1e-05); moves opposite to [[ZMIZ2]] (-0.58, fdr 4e-05), [[PADI2]] (-0.57, fdr 3e-05), [[SYN1]] (-0.57, fdr 4e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FLNB]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3775.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +11.2 | 2e-26 | 34/46 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.3 | 4e-05 | 18/45 (MIA PaCa-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +5.2 | 4e-05 | 13/44 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.24×** | +4.9 | 1e-04 | 16/48 (AN3 CA, J82, …) | top dose only | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +4.8 | 2e-04 | 18/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.003 | 15/47 (NCI-H23, HOP62, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.020 | 7/47 (A-172, NCI-H1573, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.020 | 10/46 (SW480, KATO III, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.5 | 0.027 | 6/48 (PANC-1, KATO III, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.21× | +3.1 | 0.10 | 9/38 (SHP-77, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3775.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.657×** | -9.6 | 6e-19 | 29/46 (COLO 205, H4, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.558×** | -9.4 | 2e-18 | 27/45 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.565×** | -9.2 | 8e-18 | 28/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.616×** | -7.7 | 2e-12 | 29/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.627×** | -7.2 | 6e-11 | 23/39 (MIA PaCa-2, COLO 205, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.446×** | -6.8 | 1e-09 | 28/48 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.655×** | -6.7 | 1e-09 | 26/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.453×** | -6.7 | 2e-09 | 20/43 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.680×** | -6.2 | 4e-08 | 21/47 (Hs 766T, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.697×** | -5.8 | 4e-07 | 20/46 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.693×** | -5.7 | 7e-07 | 22/46 (COLO 205, RKO, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.833× | -4.1 | 0.002 | 19/48 (hTERT-HPNE, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.790×** | -3.8 | 0.007 | 12/47 (RPMI-7951, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.803×** | -3.5 | 0.018 | 6/48 (NCI-H2030, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.828×** | -3.0 | 0.093 | 11/46 (Hs 766T, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3775. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 17.8 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +9.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.304× (z -12.1) |
| [[COLO 205 (line)]] | alt | 19.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -11.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SW480 (line)]] | alt | 14.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.322× (z -9.9) |
| [[A498 (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -8.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[H4 (line)]] | wt | 15.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -8.9) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HOP62 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.239× (z -9.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.190× (z -11.2) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 23.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -8.7) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H460 (line)]] | wt | 7.73 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.09× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[RKO (line)]] | wt | 9.18 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0859× (z -9.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SHP-77 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3775), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL4]] | +0.67 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[POLR1HASP]] | +0.64 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[PAAF1]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[C5orf34]] | +0.61 | +0.58 / +0.39 | both halves | 5e-05 |  |
| [[DNAAF10]] | +0.59 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[PRIMPOL]] | +0.59 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[HSPA14]] | +0.58 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[SAP30L-AS1]] | +0.57 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[NSD3]] | +0.57 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[NIFK-AS1]] | +0.56 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[PHC2-AS1]] | +0.54 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[TIRAP]] | +0.54 | +0.36 / +0.61 | both halves | 1e-04 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMIZ2]] | -0.58 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[PADI2]] | -0.57 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[SYN1]] | -0.57 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[MFSD12]] | -0.56 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[EPHB1]] | -0.55 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[CADM4]] | -0.54 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[GDPD5]] | -0.53 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[EPPK1]] | -0.53 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[IER3]] | -0.52 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[RHOB]] | -0.51 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[CSRP1]] | -0.51 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[RAP1B]] | -0.51 | -0.49 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FLNB]] | C | FLNB activity lowers TCEANC2's level | lines that do not express FLNB (3) vs lines expressing it (47) | 1.77× higher at baseline in the lines without FLNB | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYO1E, B4GALT1, SMOX; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction -0.424). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.0, 21.2); signed map (5.7, -0.9). **Vector** length 56.8, 7.94% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +11.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +4.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +5.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +4.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +1.8 | +4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.3 | +1.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.2 | +1.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.2 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | -4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.8 | -3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -2.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -1.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.0 | -9.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -0.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | transcription elongation factor A N-terminal and central domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:54,053,584-54,112,519 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32112; previously C1orf83 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q96MN5](https://www.uniprot.org/uniprotkb/Q96MN5) carries no function annotation.

**Summary**, from NCBI Gene [127428](https://www.ncbi.nlm.nih.gov/gene/127428):

> Predicted to enable transcription elongation factor activity. Predicted to be involved in transcription elongation by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26494](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26494) · Entrez [127428](https://www.ncbi.nlm.nih.gov/gene/127428) · UniProt [Q96MN5](https://www.uniprot.org/uniprotkb/Q96MN5) · Ensembl [ENSG00000116205](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116205)

## Data

Gene col 3775: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3775); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3775, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3775]; `tensor/DDL_lfc|DDL_z.npy` [3775]; `embed/gene_vectors.npy` [3775]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3775 or target_col == 3775). Every well: [[TCEANC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCEANC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
