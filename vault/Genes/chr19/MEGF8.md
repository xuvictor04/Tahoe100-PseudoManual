---
symbol: "MEGF8"
type: "gene"
col: 2603
ensembl_id: "ENSG00000105429"
name: "multiple EGF like domains 8"
location: "19q13.2"
module: 173
arm: "+"
pooled_cpm: 17.97
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/173"]
generated_by: "tahoemap"
---

# MEGF8

*multiple EGF like domains 8* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.94× (z +8.3, q 4e-14, up in 25 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 0.5 µM: 1.36× (z +4.1, q 0.005, up in 21 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.500× (z -9.2, q 3e-17, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PBX2]] (+0.65, fdr 5e-05), [[MED12]] (+0.58, fdr 8e-05), [[ZC3H4]] (+0.57, fdr 1e-04); moves opposite to [[EEF1AKMT4]] (-0.53, fdr 1e-04), [[HEBP1]] (-0.52, fdr 7e-04), [[NME2]] (-0.50, fdr 4e-04).
> It is in [[Module 173]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PLEKHG4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2603.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +8.3 | 4e-14 | 25/41 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +7.8 | 2e-12 | 21/30 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.53×** | +5.6 | 4e-06 | 32/46 (PANC-1, SHP-77, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +4.8 | 2e-04 | 18/35 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.36×** | +4.1 | 0.005 | 21/47 (A-172, SK-MEL-2, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.016 | 18/45 (A-427, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.016 | 12/47 (SW480, KATO III, …) | rises with dose |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 1.27× | +3.2 | 0.11 | 8/45 (RPMI-7951, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.27× | +3.1 | 0.11 | 8/47 (KATO III, RKO, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.25× | +3.0 | 0.15 | 10/46 (HOP62, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2603.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.500×** | -9.2 | 3e-17 | 39/47 (SNU-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.571×** | -7.4 | 4e-11 | 33/47 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.600×** | -6.7 | 3e-09 | 27/46 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.614×** | -6.4 | 2e-08 | 28/46 (SW480, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.618×** | -6.1 | 1e-07 | 28/43 (HT-29, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.632×** | -6.1 | 1e-07 | 29/45 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.628×** | -5.9 | 3e-07 | 29/46 (HS-578T, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.658×** | -5.5 | 2e-06 | 27/47 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.683×** | -5.0 | 3e-05 | 25/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.754×** | -3.7 | 0.011 | 17/46 (MIA PaCa-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.586×** | -3.7 | 0.012 | 15/43 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.778×** | -3.3 | 0.046 | 16/47 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.646× | -3.0 | 0.11 | 16/47 (SW480, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2603. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 18.0 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.291× (z -10.6) |
| [[HT-29 (line)]] | alt | 17.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.195× (z -9.6) |
| [[A-172 (line)]] | wt | 18.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.48× (z +9.4) ⚠ toxic; transcription drop | [[Canagliflozin (drug)]] 0.05 µM 0.218× (z -9.2) |
| [[A-427 (line)]] | wt | 23.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 28.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -11.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 23.5 | 0 | 1 | — | [[Idoxuridine (drug)]] 0.05 µM 0.0864× (z -8.6) |
| [[KATO III (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0880× (z -14.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 17.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.252× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 19.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-1 (line)]] | wt | 13.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0521× (z -11.1) |
| [[A498 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2603), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBX2]] | +0.65 | +0.70 / +0.39 | both halves | 5e-05 |  |
| [[MED12]] | +0.58 | +0.62 / +0.37 | both halves | 8e-05 |  |
| [[ZC3H4]] | +0.57 | +0.69 / +0.33 | both halves | 1e-04 |  |
| [[ZBTB4]] | +0.57 | +0.65 / +0.40 | both halves | 5e-05 |  |
| [[DEDD]] | +0.56 | +0.60 / +0.37 | both halves | 7e-05 |  |
| [[GIGYF1]] | +0.56 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[SLC24A1]] | +0.56 | +0.54 / +0.40 | both halves | 4e-05 |  |
| [[FIZ1]] | +0.56 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[SCAF1]] | +0.55 | +0.67 / +0.32 | both halves | 2e-04 |  |
| [[BRD4]] | +0.55 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[RGL2]] | +0.55 | +0.60 / +0.29 | both halves | 2e-04 |  |
| [[ZNF764]] | +0.54 | +0.67 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEF1AKMT4]] | -0.53 | -0.58 / -0.35 | both halves | 1e-04 |  |
| [[HEBP1]] | -0.52 | -0.64 / -0.20 | both halves | 7e-04 |  |
| [[NME2]] | -0.50 | -0.64 / -0.24 | both halves | 4e-04 |  |
| [[GPR180]] | -0.49 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[PIP4K2A]] | -0.47 | -0.59 / -0.26 | both halves | 3e-04 |  |
| [[GMCL1]] | -0.47 | -0.56 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHG4]] | B | PLEKHG4 activity raises MEGF8's level | lines that do not express PLEKHG4 (11) vs lines expressing it (39) | 1.52× lower at baseline in the lines without PLEKHG4 | 0.051 | ⚠ within organs, on part of the lines; also absent: SLC2A12, PPP1R1C, TMEM51-AS1 |
| [[ZNF594]] | B | ZNF594 activity raises MEGF8's level | lines that do not express ZNF594 (6) vs lines expressing it (44) | 1.40× lower at baseline in the lines without ZNF594 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with NF1; also absent: ZNF594-DT, MIR3659HG, SYNGR1 |
| [[TEX9]] | C | TEX9 activity raises MEGF8's level | lines that do not express TEX9 (3) vs lines expressing it (47) | 2.10× lower at baseline in the lines without TEX9 | 0.031 | ⚠ few lines (3 vs 47); across organs; also absent: ZMAT3, PDE4C, LCA5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 173]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.618). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-9.7, 4.2); signed map (13.9, -22.7). **Vector** length 65.1, 10.8% of its response variance represented; |z| ≥ 3 in 846 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.6 | +2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +4.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.7 | -3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +2.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +4.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +3.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.5 | +1.6 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.4 | +2.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.3 | -6.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.0 | -6.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.8 | -5.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +0.3 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.4 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -0.3 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | multiple EGF like domains 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:42,325,609-42,378,769 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SBP1, FLJ22365; previously EGFL4, C19orf49 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z7M0](https://www.uniprot.org/uniprotkb/Q7Z7M0) (Multiple epidermal growth factor-like domains protein 8):

> Substrate-recognition component of the MMM ubiquitin ligase complex, a multiprotein complex that acts as a negative regulator of smoothened signaling pathway by mediating the ubiquitination and degradation of smoothened (SMO) in primary cilia. Within the MMM complex, MEGF8 both recognizes SMO and recruits the cytoplasmic E3 ubiquitin ligase MGRN1.

**Summary**, from NCBI Gene [1954](https://www.ncbi.nlm.nih.gov/gene/1954):

> The protein encoded by this gene is a single-pass type I membrane protein of unknown function that contains several EGF-like domains, Kelch repeats, and PSI domains. Defects in this gene are a cause of Carpenter syndrome 2. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:3233](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3233) · Entrez [1954](https://www.ncbi.nlm.nih.gov/gene/1954) · UniProt [Q7Z7M0](https://www.uniprot.org/uniprotkb/Q7Z7M0) · Ensembl [ENSG00000105429](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105429)

## Data

Gene col 2603: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2603); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2603, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2603]; `tensor/DDL_lfc|DDL_z.npy` [2603]; `embed/gene_vectors.npy` [2603]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2603 or target_col == 2603). Every well: [[MEGF8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MEGF8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
