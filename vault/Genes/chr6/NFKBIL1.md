---
symbol: "NFKBIL1"
type: "gene"
col: 12878
ensembl_id: "ENSG00000204498"
name: "NFKB inhibitor like 1"
location: "6p21.33"
module: 12
arm: "+"
pooled_cpm: 10.53
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# NFKBIL1

*NFKB inhibitor like 1* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.46× (z +6.0, q 1e-06, up in 21 of 47 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.72× (z +3.9, q 0.015, up in 12 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.524× (z -7.2, q 4e-10, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC174]] (+0.81, fdr 7e-06), [[ZNF579]] (+0.76, fdr 7e-06), [[SNHG11]] (+0.74, fdr 7e-06); moves opposite to [[MACROH2A1]] (-0.70, fdr 7e-06), [[PRPS2]] (-0.69, fdr 7e-06), [[EIF5A]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12878.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.46×** | +6.0 | 1e-06 | 21/47 (NCI-H2030, PANC-1, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +5.3 | 3e-05 | 19/40 (Panc 03.27, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.72×** | +3.9 | 0.015 | 12/44 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.028 | 17/46 (NCI-H2030, PANC-1, …) | top dose only | cell-cycle shift (explains ~21% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | 1.76× | +3.2 | 0.18 | 14/47 (KATO III, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.51× | +3.0 | 0.23 | 11/44 (NCI-H460, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12878.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.524×** | -7.2 | 4e-10 | 33/47 (MIA PaCa-2, HOP62, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.613×** | -5.4 | 1e-05 | 25/47 (LOX-IMVI, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.639×** | -4.8 | 3e-04 | 25/44 (SNU-1, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.655×** | -4.7 | 4e-04 | 24/46 (NCI-H2347, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.751×** | -4.5 | 8e-04 | 23/47 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.668×** | -4.3 | 0.002 | 22/45 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.684×** | -4.2 | 0.002 | 20/47 (SK-MEL-2, NCI-H2347, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.703×** | -3.9 | 0.006 | 23/46 (C-33 A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.705×** | -3.9 | 0.006 | 17/44 (RKO, HOP62, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.746×** | -3.3 | 0.064 | 11/47 (CFPAC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.753×** | -3.1 | 0.084 | 11/48 (A-427, KATO III, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | 0.761× | -3.0 | 0.12 | 10/47 (AsPC-1, HEC-1-A, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12878. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 7.24 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0956× (z -8.9) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 7.44 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.140× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -8.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[PANC-1 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.279× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.106× (z -10.1) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.14 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.86 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12878), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC174]] | +0.81 | +0.79 / +0.83 | both halves | 7e-06 |  |
| [[ZNF579]] | +0.76 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[SNHG11]] | +0.74 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[STK16]] | +0.72 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[AMZ2P1-1]] | +0.72 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[HEIH]] | +0.72 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[TJAP1]] | +0.72 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[ATF4]] | +0.72 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[DNAL4]] | +0.72 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[RP9]] | +0.71 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[C18orf21]] | +0.70 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[NRBF2]] | +0.70 | +0.68 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MACROH2A1]] | -0.70 | -0.62 / -0.72 | both halves | 7e-06 |  |
| [[PRPS2]] | -0.69 | -0.61 / -0.68 | both halves | 7e-06 |  |
| [[EIF5A]] | -0.69 | -0.65 / -0.58 | both halves | 7e-06 |  |
| [[RBBP7]] | -0.67 | -0.58 / -0.70 | both halves | 7e-06 |  |
| [[TMX1]] | -0.66 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[GMPS]] | -0.64 | -0.66 / -0.65 | both halves | 7e-06 |  |
| [[MOB1A]] | -0.64 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[LAPTM4B]] | -0.63 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[FUCA2]] | -0.63 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.63 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[SPCS3]] | -0.63 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[PGRMC1]] | -0.62 | -0.54 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NFKBIL1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.819). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-34.6, 1.0); signed map (-7.4, -8.5). **Vector** length 79.3, 16.0% of its response variance represented; |z| ≥ 3 in 713 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mRNA Splicing - Major Pathway* (reactome, mean cos +0.51 to 17); *mRNA Splicing* (reactome, mean cos +0.51 to 17).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +6.1 | +6.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.0 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +2.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.5 | +3.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +0.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.7 | +3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | -0.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.6 | -0.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.5 | -7.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.9 | -4.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.8 | -4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.6 | +0.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.4 | +0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -4.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -3.1 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -1.3 | -1.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | NFKB inhibitor like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,546,870-31,558,829 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IKBL; previously NFKBIL |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBC1](https://www.uniprot.org/uniprotkb/Q9UBC1) (NF-kappa-B inhibitor-like protein 1):

> Involved in the regulation of innate immune response. Acts as negative regulator of Toll-like receptor and interferon-regulatory factor (IRF) signaling pathways. Contributes to the negative regulation of transcriptional activation of NF-kappa-B target genes in response to endogenous pro-inflammatory stimuli.

**Summary**, from NCBI Gene [4795](https://www.ncbi.nlm.nih.gov/gene/4795):

> This gene encodes a divergent member of the I-kappa-B family of proteins. Its function has not been determined. The gene lies within the major histocompatibility complex (MHC) class I region on chromosome 6. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:7800](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7800) · Entrez [4795](https://www.ncbi.nlm.nih.gov/gene/4795) · UniProt [Q9UBC1](https://www.uniprot.org/uniprotkb/Q9UBC1) · Ensembl [ENSG00000204498](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204498)

## Data

Gene col 12878: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12878); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12878, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12878]; `tensor/DDL_lfc|DDL_z.npy` [12878]; `embed/gene_vectors.npy` [12878]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12878 or target_col == 12878). Every well: [[NFKBIL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFKBIL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
