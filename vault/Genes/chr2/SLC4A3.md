---
symbol: "SLC4A3"
type: "gene"
col: 3602
ensembl_id: "ENSG00000114923"
name: "solute carrier family 4 member 3"
location: "2q35"
module: 132
arm: "+"
pooled_cpm: 4.92
n_lines_expressing: 42
n_dd_up: 0
n_dd_down: 25
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 15
direction_downstream: 30
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# SLC4A3

*solute carrier family 4 member 3* — 2q35

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.470× (z -11.6, q 3e-28, down in 24 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF783]] (+0.70, fdr 7e-06, ⚠ ZNF783 in the vector space only through flagged drug-doses), [[SEPTIN5]] (+0.68, fdr 7e-06), [[ARHGEF25]] (+0.65, fdr 7e-06), [[IDUA]] (+0.65, fdr 1e-05); moves opposite to [[COX8A]] (-0.61, fdr 1e-05), [[ATP5PF]] (-0.53, fdr 2e-05), [[NDUFA2]] (-0.52, fdr 8e-05).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[FAXC]] → it (grade B ⚠); 30 go from it, the strongest it → [[FAXC]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3602.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.38× | +3.4 | 0.34 | 8/23 (SW480, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.35× | +3.2 | 0.34 | 4/12 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.32× | +3.0 | 0.34 | 7/32 (A-172, NCI-H2030, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3602.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.470×** | -11.6 | 3e-28 | 24/33 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.405×** | -9.8 | 3e-20 | 27/37 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.449×** | -8.7 | 7e-16 | 26/38 (J82, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.457×** | -8.5 | 3e-15 | 25/37 (NCI-H23, SW48, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.472×** | -8.1 | 4e-14 | 24/37 (C-33 A, SW48, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.520×** | -7.1 | 1e-10 | 24/37 (LoVo, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.651×** | -6.6 | 3e-09 | 20/34 (PANC-1, J82, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.595×** | -5.6 | 1e-06 | 15/37 (A-172, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.596×** | -5.6 | 1e-06 | 16/34 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.608×** | -5.2 | 1e-05 | 15/36 (SNU-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.609×** | -5.2 | 1e-05 | 13/35 (NCI-H23, LOX-IMVI, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.626×** | -5.1 | 2e-05 | 17/38 (A-427, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.646×** | -4.7 | 9e-05 | 14/32 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.653×** | -4.6 | 2e-04 | 16/34 (SNU-423, J82, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.656×** | -4.6 | 2e-04 | 16/37 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.677×** | -4.1 | 0.002 | 10/36 (HCT15, HOP62, …) | top dose only |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **0.699×** | -3.8 | 0.005 | 8/36 (C-33 A, H4, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.714×** | -3.7 | 0.008 | 11/35 (SNU-1, AsPC-1, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.731×** | -3.4 | 0.019 | 6/38 (NCI-H460, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.809×** | -3.3 | 0.030 | 11/38 (CFPAC-1, SW 900, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.571×** | -3.2 | 0.036 | 3/36 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | **0.816×** | -3.1 | 0.044 | 8/38 (Hs 766T, J82, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3602. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 8.88 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0294× (z -15.3) ⚠ cell-cycle shift, explains ~56% of this change |
| [[LOX-IMVI (line)]] | wt | 4.43 | 0 | 3 (1 ⚠) | — | [[Verteporfin (drug)]] 5 µM 0.0626× (z -9.1) |
| [[PANC-1 (line)]] | alt | 4.83 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0605× (z -13.9) |
| [[C-33 A (line)]] | alt | 8.62 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0407× (z -11.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Captopril (drug)]] 0.05 µM 0.0860× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 9.36 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.167× (z -8.8) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 5.41 | 0 | 1 | — | [[Penfluridol (drug)]] 5 µM 0.122× (z -10.5) |
| [[C32 (line)]] | wt | 13.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -10.1) ⚠ cell-cycle shift, explains ~55% of this change |
| [[HOP62 (line)]] | alt | 6.16 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -11.8) |
| [[HS-578T (line)]] | alt | 5.96 | 0 | 1 (1 ⚠) | — | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.0530× (z -10.9) ⚠ toxic |
| [[J82 (line)]] | alt | 2.73 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0385× (z -10.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[MIA PaCa-2 (line)]] | alt | 6.48 | 0 | 1 (1 ⚠) | — | [[OTS514 (drug)]] 0.05 µM 0.0845× (z -9.2) ⚠ transcription drop |
| [[NCI-H2347 (line)]] | alt | 2.90 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0852× (z -8.8) ⚠ transcription drop |
| [[Panc 03.27 (line)]] | alt | 4.56 | 0 | 1 | — | [[Hydroxyurea (drug)]] 5 µM 0.0659× (z -8.7) |
| [[SNU-423 (line)]] | alt | 4.97 | 0 | 1 | — | [[Hesperidin (drug)]] 0.5 µM 0.0785× (z -8.6) |
| [[SW48 (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.101× (z -8.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW480 (line)]] | alt | 7.49 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -10.6) |
| [[A-172 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.576 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.627 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.322 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.349 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3602), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF783]] ⚠ | +0.70 | +0.68 / +0.61 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SEPTIN5]] | +0.68 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[ARHGEF25]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[IDUA]] | +0.65 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[OPLAH]] ⚠ | +0.61 | +0.55 / +0.58 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[BRSK2]] | +0.61 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[SDC3]] | +0.61 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[DBN1]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[LZTR1]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[PRDM11]] | +0.60 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[LAMC3]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[WIZ]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[MTA1]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[MAPK12]] | +0.57 | +0.60 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX8A]] | -0.61 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[ATP5PF]] | -0.53 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[NDUFA2]] | -0.52 | -0.37 / -0.58 | both halves | 8e-05 |  |
| [[ZNHIT1]] | -0.52 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[NDUFA1]] | -0.52 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[DDT]] | -0.50 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[DPM3]] | -0.50 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[COX7B]] | -0.50 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[NDUFA7]] | -0.49 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[PGRMC2]] | -0.49 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[UQCR10]] ⚠ | -0.49 | -0.44 / -0.49 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PTPRR]] | -0.49 | -0.50 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 13, C 2. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAXC]] | B | FAXC activity raises SLC4A3's level | lines that do not express FAXC (11) vs lines expressing it (39) | 2.32× lower at baseline in the lines without FAXC | 0.005 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[TBX1]] | B | TBX1 activity raises SLC4A3's level | lines that do not express TBX1 (23) vs lines expressing it (27) | 1.60× lower at baseline in the lines without TBX1 | 0.014 | ⚠ within organs, on part of the lines; also absent: BEGAIN, PALM, OLFM1 |
| [[PDZD4]] | B | PDZD4 activity raises SLC4A3's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 1.89× lower at baseline in the lines without PDZD4 | 0.017 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[SPEG]] | B | SPEG activity raises SLC4A3's level | lines that do not express SPEG (16) vs lines expressing it (34) | 2.07× lower at baseline in the lines without SPEG | 0.019 | ⚠ within organs, on part of the lines; also absent: APBA2, FBXO17, GJC1 |
| [[GNAZ]] | B | GNAZ activity raises SLC4A3's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.91× lower at baseline in the lines without GNAZ | 0.022 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises SLC4A3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EBF4]] | B | EBF4 activity raises SLC4A3's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 1.99× lower at baseline in the lines without EBF4 | 0.036 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[VASH1]] | B | VASH1 activity strengthens SLC4A3's drug response | lines that do not express VASH1 (11) vs lines expressing it (28) | the lines without VASH1 respond 0.55× as strongly (z diff +1.48); strongest at Idarubicin (hydrochloride) 5 µM: 0.64x vs 0.38x (z diff +2.9) | 0.037 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B; target measured in part of the lines; artifact flags |
| [[ELFN1]] | B | ELFN1 activity raises SLC4A3's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 1.86× lower at baseline in the lines without ELFN1 | 0.047 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[CYS1]] | B | CYS1 activity raises SLC4A3's level | lines that do not express CYS1 (22) vs lines expressing it (28) | 1.56× lower at baseline in the lines without CYS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: MT1A, FMNL1-DT, SEC14L4 |
| [[BRSK2]] | B | BRSK2 activity raises SLC4A3's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 1.89× lower at baseline in the lines without BRSK2 | 0.080 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[LAMC3]] | B | LAMC3 activity raises SLC4A3's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.57× lower at baseline in the lines without LAMC3 | 0.089 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |

### Downstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 29, C 1. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAXC]] | B | SLC4A3 activity raises FAXC's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 2.76× lower at baseline in the lines without SLC4A3 | 0.008 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[CNOT6]] | B | SLC4A3 activity raises CNOT6's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 1.36× lower at baseline in the lines without SLC4A3 | 0.008 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[GNAZ]] | B | SLC4A3 activity raises GNAZ's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 2.00× lower at baseline in the lines without SLC4A3 | 0.012 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[SLC29A3]] | B | SLC4A3 activity raises SLC29A3's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 1.09× lower at baseline in the lines without SLC4A3 | 0.016 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[BRSK2]] | B | SLC4A3 activity raises BRSK2's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 2.29× lower at baseline in the lines without SLC4A3 | 0.016 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[TOP1MT]] | B | SLC4A3 activity raises TOP1MT's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 1.52× lower at baseline in the lines without SLC4A3 | 0.021 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[PRRC2A]] | B | SLC4A3 activity raises PRRC2A's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 1.51× lower at baseline in the lines without SLC4A3 | 0.027 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[ZNF589]] | B | SLC4A3 activity raises ZNF589's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 1.34× lower at baseline in the lines without SLC4A3 | 0.035 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[NDST1]] | B | SLC4A3 activity raises NDST1's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 2.28× lower at baseline in the lines without SLC4A3 | 0.038 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[SDC3]] | B | SLC4A3 activity raises SDC3's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 2.26× lower at baseline in the lines without SLC4A3 | 0.042 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[ZNF783]] | B | SLC4A3 activity raises ZNF783's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 1.28× lower at baseline in the lines without SLC4A3 | 0.045 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[DGCR5]] | B | SLC4A3 activity raises DGCR5's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 2.41× lower at baseline in the lines without SLC4A3 | 0.052 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (7.8, 41.1); signed map (23.4, 26.9). **Vector** length 53.8, 7.90% of its response variance represented; |z| ≥ 3 in 914 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.9 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +3.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.2 | +1.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.2 | +3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.2 | +0.8 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.1 | +2.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.7 | -7.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -2.7 | -8.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | -2.7 | -5.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -2.6 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.5 | -5.1 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.5 | -1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.3 | -4.1 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 4 member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:219,627,394-219,641,980 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AE3, SLC2C |
| Gene groups (HGNC) | Solute carrier family 4 |
| Reactome | 4 pathways, smallest: Bicarbonate transporters; SLC-mediated transport of inorganic anions; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P48751](https://www.uniprot.org/uniprotkb/P48751) (Anion exchange protein 3):

> Sodium-independent anion exchanger which mediates the electroneutral exchange of chloride for bicarbonate ions across the cell membrane. May be involved in the regulation of intracellular pH, and the modulation of cardiac action potential.

**Summary**, from NCBI Gene [6508](https://www.ncbi.nlm.nih.gov/gene/6508):

> The protein encoded by this gene is a plasma membrane anion exchange protein. The encoded protein has been found in brain, heart, kidney, small intestine, and lung. [provided by RefSeq, May 2016]

**Accessions** — [HGNC:11029](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11029) · Entrez [6508](https://www.ncbi.nlm.nih.gov/gene/6508) · UniProt [P48751](https://www.uniprot.org/uniprotkb/P48751) · Ensembl [ENSG00000114923](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114923)

## Data

Gene col 3602: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3602); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3602, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3602]; `tensor/DDL_lfc|DDL_z.npy` [3602]; `embed/gene_vectors.npy` [3602]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3602 or target_col == 3602). Every well: [[SLC4A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC4A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
