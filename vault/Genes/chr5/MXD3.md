---
symbol: "MXD3"
type: "gene"
col: 13098
ensembl_id: "ENSG00000213347"
name: "MAX dimerization protein 3"
location: "5q35.3"
module: 22
arm: "+"
pooled_cpm: 6.61
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 19
n_dd_up_clean: 9
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# MXD3

*MAX dimerization protein 3* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.09× (z +12.8, q 2e-34, up in 38 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.537× (z -7.6, q 1e-11, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC25C]] (+0.72, fdr 7e-06), [[CDCA3]] (+0.70, fdr 7e-06), [[PIMREG]] (+0.70, fdr 7e-06); moves opposite to [[GPATCH4]] (-0.61, fdr 2e-05), [[GCFC2]] (-0.58, fdr 3e-04), [[COA7]] (-0.55, fdr 1e-04).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13098.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.09×** | +12.8 | 2e-34 | 38/44 (A549, A498, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.98×** | +8.4 | 2e-14 | 31/47 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.96×** | +8.2 | 4e-14 | 32/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.90×** | +7.9 | 5e-13 | 28/47 (A498, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +7.3 | 4e-11 | 23/40 (A-172, C32, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.63×** | +5.9 | 3e-07 | 13/31 (A-172, SW480, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +5.2 | 1e-05 | 19/42 (Panc 03.27, A-172, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.45×** | +4.5 | 5e-04 | 12/38 (HEC-1-A, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +4.1 | 0.003 | 14/42 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +3.7 | 0.011 | 10/47 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.098 | 3/46 (A549, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13098.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.537×** | -7.6 | 1e-11 | 27/46 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.536×** | -7.4 | 6e-11 | 25/46 (HS-578T, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.602×** | -6.2 | 1e-07 | 22/47 (A-172, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.623×** | -5.8 | 9e-07 | 20/40 (HT-29, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.607×** | -5.8 | 1e-06 | 22/47 (SNU-423, A-172, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.629×** | -5.7 | 1e-06 | 21/47 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.644×** | -5.4 | 5e-06 | 19/46 (H4, SNU-1, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.655×** | -5.2 | 1e-05 | 17/47 (BT-474, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.742×** | -5.2 | 1e-05 | 20/43 (A-172, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.662×** | -5.1 | 2e-05 | 22/46 (BT-474, SW480, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.664×** | -4.8 | 7e-05 | 18/43 (BT-474, SW1417, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.497×** | -4.5 | 4e-04 | 11/44 (HT-29, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.686×** | -4.4 | 5e-04 | 14/44 (SK-MEL-2, C32, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.537×** | -4.0 | 0.003 | 12/41 (SW480, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.812×** | -3.6 | 0.011 | 11/48 (CHP-212, MIA PaCa-2, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM |  | **0.755×** | -3.5 | 0.018 | 8/47 (NCI-H2347, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | **0.770×** | -3.0 | 0.087 | 6/47 (C-33 A, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13098. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 9.36 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -9.7) |
| [[A498 (line)]] | wt | 5.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +9.7) | — |
| [[A549 (line)]] | wt | 4.28 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.69× (z +9.9) | — |
| [[BT-474 (line)]] | alt | 6.77 | 0 | 1 | — | [[Cyclosporin A (drug)]] 0.5 µM 0.0578× (z -10.7) |
| [[HCT15 (line)]] | alt | 7.93 | 0 | 1 | — | [[Raltitrexed (drug)]] 0.5 µM 0.0698× (z -8.6) |
| [[Hs 766T (line)]] | wt | 6.55 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.111× (z -8.5) |
| [[HS-578T (line)]] | alt | 7.27 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0923× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 4.90 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0823× (z -9.0) |
| [[A-427 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13098), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC25C]] | +0.72 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[CDCA3]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[PIMREG]] | +0.70 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[PRR11]] | +0.66 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[POC1A]] | +0.66 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[TROAP]] | +0.65 | +0.68 / +0.58 | both halves | 8e-06 |  |
| [[PIF1]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[GTSE1]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[TACC3]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[CDCA2]] | +0.64 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[CDCA8]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[KIF22]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH4]] | -0.61 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[GCFC2]] | -0.58 | -0.28 / -0.60 | both halves | 3e-04 |  |
| [[COA7]] | -0.55 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[SMIM15]] | -0.55 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[SSB]] | -0.54 | -0.31 / -0.58 | both halves | 2e-04 |  |
| [[RRP15]] | -0.54 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[RPL7L1]] | -0.54 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[KICS2]] | -0.53 | -0.30 / -0.55 | both halves | 2e-04 |  |
| [[FAM169A]] | -0.53 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[C12orf29]] | -0.52 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[FAM83H]] | -0.51 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[LACC1]] | -0.51 | -0.28 / -0.51 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MXD3's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[C21orf58]] | C | C21orf58 activity raises MXD3's level | lines that do not express C21orf58 (3) vs lines expressing it (47) | 1.64× lower at baseline in the lines without C21orf58 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.538). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-34.9, -56.9); signed map (-51.7, -40.2). **Vector** length 65.5, 10.2% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cyclin A/B1/B2 associated events during G2/M transition* (reactome, mean cos +0.51 to 12); *G2/M DNA replication checkpoint* (reactome, mean cos +0.50 to 5); *Chk1/Chk2(Cds1) mediated inactivation of Cyclin B:Cdk1 complex* (reactome, mean cos +0.54 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +12.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +7.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +5.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.0 | +7.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.8 | +8.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.4 | +0.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.3 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +0.8 |
|  | [[HI-TOPK-032 (drug)]] 0.5 µM |  | +1.0 | +1.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -5.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.6 | -7.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -2.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -1.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | MAX dimerization protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:177,301,461-177,312,757 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MAD3, bHLHc13 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; MAX dimerization proteins |
| Hallmark sets | E2F_TARGETS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BW11](https://www.uniprot.org/uniprotkb/Q9BW11) (Max dimerization protein 3):

> Transcriptional repressor. Binds with MAX to form a sequence-specific DNA-binding protein complex which recognizes the core sequence 5'-CAC[GA]TG-3'. Antagonizes MYC transcriptional activity by competing for MAX and suppresses MYC dependent cell transformation (By similarity).

**Summary**, from NCBI Gene [83463](https://www.ncbi.nlm.nih.gov/gene/83463):

> This gene encodes a member of the Myc superfamily of basic helix-loop-helix leucine zipper transcriptional regulators. The encoded protein forms a heterodimer with the cofactor MAX which binds specific E-box DNA motifs in the promoters of target genes and regulates their transcription. Disruption of the MAX-MXD3 complex is associated with uncontrolled cell proliferation and tumorigenesis. Transcript variants of this gene encoding different isoforms have been described.[provided by RefSeq, Dec …

**Accessions** — [HGNC:14008](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14008) · Entrez [83463](https://www.ncbi.nlm.nih.gov/gene/83463) · UniProt [Q9BW11](https://www.uniprot.org/uniprotkb/Q9BW11) · Ensembl [ENSG00000213347](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213347)

## Data

Gene col 13098: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13098); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13098, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13098]; `tensor/DDL_lfc|DDL_z.npy` [13098]; `embed/gene_vectors.npy` [13098]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13098 or target_col == 13098). Every well: [[MXD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MXD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
