---
symbol: "VPS18"
type: "gene"
col: 2420
ensembl_id: "ENSG00000104142"
name: "VPS18 core subunit of CORVET and HOPS complexes"
location: "15q15.1"
module: 59
arm: "+"
pooled_cpm: 8.59
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 5
n_dd_up_clean: 28
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# VPS18

*VPS18 core subunit of CORVET and HOPS complexes* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (7 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.38× (z +14.1, q 4e-42, up in 42 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.640× (z -6.5, q 5e-08, down in 20 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 0.05 µM: 0.752× (z -4.1, q 0.010, down in 6 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP6V0D1]] (+0.60, fdr 1e-05), [[C6orf47]] (+0.58, fdr 1e-05), [[SERTAD3]] (+0.56, fdr 3e-05); moves opposite to [[HPRT1]] (-0.51, fdr 2e-05), [[CLNS1A]] (-0.50, fdr 7e-05), [[NBEAP2]] (-0.49, fdr 2e-04).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ELF3-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2420.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.38×** | +14.1 | 4e-42 | 42/44 (SW480, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +13.8 | 1e-40 | 29/41 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.53×** | +13.5 | 4e-39 | 43/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.47×** | +13.1 | 3e-37 | 42/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.47×** | +12.6 | 2e-34 | 31/44 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.16×** | +11.2 | 6e-27 | 39/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +7.9 | 2e-13 | 19/44 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.72×** | +7.8 | 3e-13 | 30/47 (Hs 766T, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.60×** | +7.3 | 2e-11 | 23/40 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.62×** | +7.0 | 2e-10 | 21/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +6.2 | 3e-08 | 16/42 (HEC-1-A, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +6.1 | 5e-08 | 18/36 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +6.0 | 1e-07 | 15/41 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.50×** | +5.9 | 2e-07 | 17/43 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +5.8 | 3e-07 | 17/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +5.7 | 3e-07 | 16/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +4.8 | 5e-05 | 14/46 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +4.6 | 1e-04 | 12/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2420.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.640×** | -6.5 | 5e-08 | 20/33 (MIA PaCa-2, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.752×** | -4.1 | 0.010 | 6/46 (LOX-IMVI, SHP-77, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.754×** | -3.8 | 0.021 | 11/23 (SNU-423, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.771×** | -3.8 | 0.021 | 14/45 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.785×** | -3.4 | 0.078 | 9/48 (AN3 CA, NCI-H1573, …) | top dose only |  |
| [[Procainamide (hydrochloride) (drug)]] 5 µM |  | 0.799× | -3.2 | 0.15 | 7/45 (AsPC-1, A-172, …) | top dose only |  |
| [[Radotinib (drug)]] 0.5 µM |  | 0.808× | -3.1 | 0.15 | 9/43 (CFPAC-1, KATO III, …) | inconsistent across doses |  |
| [[Ixazomib (drug)]] 0.05 µM |  | 0.802× | -3.0 | 0.17 | 5/44 (H4, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2420. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 6.03 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.14× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -10.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 8.51 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +12.7) | — |
| [[HT-29 (line)]] | alt | 23.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0797× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 15.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.219× (z -8.8) |
| [[SHP-77 (line)]] | alt | 6.97 | 0 | 2 | — | [[Brivudine (drug)]] 0.05 µM 0.0793× (z -10.1) |
| [[SNU-1 (line)]] | wt | 7.70 | 0 | 2 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0743× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 5.52 | 0 | 1 | — | [[Auranofin (drug)]] 0.5 µM 0.0459× (z -11.9) |
| [[HCT15 (line)]] | alt | 14.6 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.106× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 6.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 5.24 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0787× (z -9.5) |
| [[J82 (line)]] | alt | 8.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +8.9) | — |
| [[KATO III (line)]] | alt | 8.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.87 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0803× (z -11.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 7.15 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 6.69 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.73× (z +8.5) | — |
| [[A-427 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.56 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2420), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V0D1]] | +0.60 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[C6orf47]] | +0.58 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[SERTAD3]] | +0.56 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[ZNF669]] | +0.55 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[BLOC1S3]] | +0.55 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[NEU1]] | +0.53 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[PHF23]] | +0.53 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[TOLLIP]] | +0.51 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[SCO2]] | +0.51 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[TRAF4]] | +0.49 | +0.47 / +0.53 | both halves | 2e-05 | same gene group |
| [[UAP1L1]] | +0.49 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[MVP-DT]] | +0.49 | +0.57 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HPRT1]] | -0.51 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[CLNS1A]] | -0.50 | -0.38 / -0.57 | both halves | 7e-05 |  |
| [[NBEAP2]] | -0.49 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[PSMD14]] | -0.48 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[NAE1]] | -0.47 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[NIT2]] | -0.45 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[SEPTIN7]] | -0.43 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[PTDSS1]] | -0.42 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[CLCC1]] | -0.42 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[VBP1]] | -0.42 | -0.37 / -0.31 | both halves | 2e-04 |  |
| [[TBC1D31]] | -0.41 | -0.39 / -0.30 | both halves | 2e-04 |  |
| [[C2orf27A]] | -0.41 | -0.36 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises VPS18's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 1.42× lower at baseline in the lines without ELF3-AS1 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.380). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-45.9, -0.7); signed map (-5.2, -25.2). **Vector** length 75.7, 13.2% of its response variance represented; |z| ≥ 3 in 1,015 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +14.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.1 | +4.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.0 | +12.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.8 | +7.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.7 | +3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +7.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.3 | +1.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.2 | +2.9 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +0.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -1.9 | -3.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.8 | -3.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | VPS18 core subunit of CORVET and HOPS complexes |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:40,894,450-40,903,975 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1475, PEP3 |
| Gene groups (HGNC) | HOPS complex; CORVET complex; RING finger E3 ubiquitin protein ligases |
| Reactome | 5 pathways, smallest: SARS-CoV-2 modulates autophagy; SARS-CoV-2-host interactions; SARS-CoV-2 Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P253](https://www.uniprot.org/uniprotkb/Q9P253) (Vacuolar protein sorting-associated protein 18 homolog):

> Plays a role in vesicle-mediated protein trafficking to lysosomal compartments including the endocytic membrane transport and autophagic pathways. Believed to act as a core component of the putative HOPS and CORVET endosomal tethering complexes which are proposed to be involved in the Rab5-to-Rab7 endosome conversion probably implicating MON1A/B, and via binding SNAREs and SNARE complexes to mediate tethering and docking events during SNARE-mediated membrane fusion. The HOPS complex is proposed …

**Summary**, from NCBI Gene [57617](https://www.ncbi.nlm.nih.gov/gene/57617):

> Vesicle mediated protein sorting plays an important role in segregation of intracellular molecules into distinct organelles. Genetic studies in yeast have identified more than 40 vacuolar protein sorting (VPS) genes involved in vesicle transport to vacuoles. This gene encodes the human homolog of yeast class C Vps18 protein. The mammalian class C Vps proteins are predominantly associated with late endosomes/lysosomes, and like their yeast counterparts, may mediate vesicle trafficking steps in …

**Accessions** — [HGNC:15972](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15972) · Entrez [57617](https://www.ncbi.nlm.nih.gov/gene/57617) · UniProt [Q9P253](https://www.uniprot.org/uniprotkb/Q9P253) · Ensembl [ENSG00000104142](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104142)

## Data

Gene col 2420: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2420); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2420, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2420]; `tensor/DDL_lfc|DDL_z.npy` [2420]; `embed/gene_vectors.npy` [2420]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2420 or target_col == 2420). Every well: [[VPS18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
