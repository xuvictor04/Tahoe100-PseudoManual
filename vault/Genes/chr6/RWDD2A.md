---
symbol: "RWDD2A"
type: "gene"
col: 272
ensembl_id: "ENSG00000013392"
name: "RWD domain containing 2A"
location: "6q14.1"
module: 49
arm: "+"
pooled_cpm: 3.97
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# RWDD2A

*RWD domain containing 2A* — 6q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.79× (z +9.8, q 9e-20, up in 28 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.464× (z -8.7, q 1e-15, down in 27 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FICD]] (+0.66, fdr 1e-05), [[ALG2]] (+0.62, fdr 7e-06), [[SLC33A1]] (+0.60, fdr 1e-05); moves opposite to [[CHRNA5]] (-0.47, fdr 1e-04), [[BRI3BP]] (-0.46, fdr 8e-05), [[FARP1]] (-0.46, fdr 9e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 272.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +9.8 | 9e-20 | 28/38 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.31×** | +4.5 | 0.002 | 5/45 (PANC-1, C-33 A, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +4.0 | 0.012 | 2/8 (HOP62, HT-29) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.018 | 9/46 (J82, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +3.6 | 0.031 | 5/25 (PANC-1, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.097 | 8/46 (hTERT-HPNE, A498, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.35× | +3.1 | 0.15 | 3/43 (A498, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.30× | +3.0 | 0.19 | 5/46 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 272.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.464×** | -8.7 | 1e-15 | 27/45 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.512×** | -7.9 | 8e-13 | 25/47 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.520×** | -7.7 | 2e-12 | 24/37 (J82, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.557×** | -6.7 | 4e-09 | 21/44 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.422×** | -5.3 | 1e-05 | 15/39 (HEC-1-A, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.637×** | -5.3 | 1e-05 | 18/46 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.697×** | -3.7 | 0.018 | 16/30 (KATO III, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.808×** | -3.6 | 0.024 | 15/38 (NCI-H460, SW 900, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.731×** | -3.6 | 0.024 | 15/43 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.732×** | -3.5 | 0.028 | 8/43 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.717×** | -3.4 | 0.034 | 6/46 (Panc 03.27, SW480, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.583×** | -3.3 | 0.041 | 10/37 (SW480, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.825×** | -3.2 | 0.060 | 9/47 (KATO III, NCI-H1573, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.610×** | -3.0 | 0.094 | 5/26 (SNU-423, LS 180, …) | top dose only | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 272. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 4.72 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -9.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 6.17 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.172× (z -8.5) |
| [[LS 180 (line)]] | wt | 4.21 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0800× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 3.27 | 0 | 1 | — | [[Ligustrazine (drug)]] 0.05 µM 0.0795× (z -8.5) |
| [[A-172 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 272), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FICD]] | +0.66 | +0.79 / +0.56 | both halves | 1e-05 |  |
| [[ALG2]] | +0.62 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[SLC33A1]] | +0.60 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[RUSF1]] | +0.60 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[DNAJB9]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[LYSMD3]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[TBL2]] | +0.56 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[LCA5L]] | +0.56 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[BET1]] | +0.55 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[XBP1]] | +0.54 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[HID1]] | +0.54 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[NRBF2]] | +0.53 | +0.46 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHRNA5]] | -0.47 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[BRI3BP]] | -0.46 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[FARP1]] | -0.46 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[DROSHA]] | -0.45 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[CERS6]] | -0.44 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[MMS22L]] | -0.44 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[SPIDR]] | -0.44 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[TBCD]] | -0.43 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[PRIM2]] | -0.43 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[SHMT1]] | -0.43 | -0.36 / -0.37 | both halves | 9e-05 |  |
| [[ACOT7]] | -0.42 | -0.43 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers RWDD2A's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CATSPER2P1]] | C | CATSPER2P1 activity raises RWDD2A's level | lines that do not express CATSPER2P1 (3) vs lines expressing it (47) | 1.73× lower at baseline in the lines without CATSPER2P1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FAM182B, SLFNL1-AS1, ENSG00000287400; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.496). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.2, -37.8); signed map (-55.1, 13.3). **Vector** length 44.8, 4.99% of its response variance represented; |z| ≥ 3 in 915 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +0.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +2.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.1 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.3 | +0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.2 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +0.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +1.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.0 | -0.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -1.6 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -3.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -8.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.2 | -7.9 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | -1.2 | -0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.0 | -1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | RWD domain containing 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.1 — chr6:83,193,357-83,198,935 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC13523, dJ747H23.2; previously RWDD2 |
| Gene groups (HGNC) | RWD domain containing |
| Matched by | ensembl_id |

UniProt [Q9UIY3](https://www.uniprot.org/uniprotkb/Q9UIY3) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:21385](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21385) · Entrez [112611](https://www.ncbi.nlm.nih.gov/gene/112611) · UniProt [Q9UIY3](https://www.uniprot.org/uniprotkb/Q9UIY3) · Ensembl [ENSG00000013392](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000013392)

## Data

Gene col 272: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 272); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 272, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 272]; `tensor/DDL_lfc|DDL_z.npy` [272]; `embed/gene_vectors.npy` [272]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 272 or target_col == 272). Every well: [[RWDD2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RWDD2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
