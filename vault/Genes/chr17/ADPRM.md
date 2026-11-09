---
symbol: "ADPRM"
type: "gene"
col: 9916
ensembl_id: "ENSG00000170222"
name: "ADP-ribose/CDP-alcohol diphosphatase, manganese dependent"
location: "17p13.1"
module: 20
arm: "-"
pooled_cpm: 9.92
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 6
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# ADPRM

*ADP-ribose/CDP-alcohol diphosphatase, manganese dependent* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.82× (z +6.5, q 3e-08, up in 27 of 40 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.48× (z +6.3, q 8e-08, up in 26 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.534× (z -7.2, q 5e-10, down in 26 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pyridoxine (hydrochloride) (drug)]] 5 µM: 0.807× (z -3.5, q 0.091, down in 15 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPB41L4A-AS1]] (+0.76, fdr 7e-06), [[NKAP]] (+0.75, fdr 7e-06), [[SNHG8]] (+0.75, fdr 7e-06); moves opposite to [[RBBP7]] (-0.72, fdr 7e-06), [[TFDP1]] (-0.68, fdr 7e-06), [[YWHAQ]] (-0.67, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9916.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +6.5 | 3e-08 | 27/40 (NCI-H1573, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +6.3 | 8e-08 | 26/46 (MIA PaCa-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +5.3 | 3e-05 | 25/43 (RKO, KATO III, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +4.7 | 3e-04 | 22/47 (KATO III, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.3 | 0.002 | 20/43 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +3.9 | 0.010 | 19/47 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.022 | 19/46 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.026 | 15/47 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.49×** | +3.2 | 0.079 | 10/44 (AN3 CA, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9916.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.534×** | -7.2 | 5e-10 | 26/34 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.662×** | -4.5 | 0.002 | 14/21 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.807×** | -3.5 | 0.091 | 15/48 (Hs 766T, KATO III, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.813×** | -3.4 | 0.091 | 14/48 (SW1417, LS 180, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.747×** | -3.3 | 0.091 | 16/48 (NCI-H661, A549, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.741×** | -3.3 | 0.091 | 12/40 (SHP-77, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fusidic acid (drug)]] 5 µM |  | 0.823× | -3.2 | 0.13 | 10/48 (SHP-77, SW 1088, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9916. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 9.81 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.138× (z -9.5) ⚠ toxic |
| [[A549 (line)]] | wt | 16.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -9.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 9.33 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0486× (z -11.5) |
| [[Hs 766T (line)]] | wt | 6.59 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.05 µM 0.0906× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 8.98 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0633× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 21.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +11.7) | — |
| [[NCI-H1792 (line)]] | alt | 5.53 | 0 | 1 | — | [[Pimitespib (drug)]] 0.05 µM 0.0641× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -10.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 9.35 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -10.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.117× (z -10.3) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 11.7 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0877× (z -8.5) |
| [[SW480 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9916), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L4A-AS1]] | +0.76 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[NKAP]] | +0.75 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[SNHG8]] | +0.75 | +0.64 / +0.80 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | +0.74 | +0.60 / +0.82 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[MED10]] | +0.73 | +0.53 / +0.74 | both halves | 1e-05 |  |
| [[SNHG7]] | +0.72 | +0.63 / +0.79 | both halves | 7e-06 |  |
| [[CDC37L1]] | +0.72 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[SNHG32]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[ZNF766]] | +0.71 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[NRBF2]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[ZNF593]] | +0.69 | +0.55 / +0.74 | both halves | 1e-05 |  |
| [[CCDC174]] | +0.68 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[MRPL32]] | +0.68 | +0.53 / +0.77 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBBP7]] | -0.72 | -0.66 / -0.69 | both halves | 7e-06 |  |
| [[TFDP1]] | -0.68 | -0.69 / -0.63 | both halves | 7e-06 |  |
| [[YWHAQ]] | -0.67 | -0.57 / -0.73 | both halves | 1e-05 |  |
| [[MTHFD1]] | -0.67 | -0.60 / -0.68 | both halves | 7e-06 |  |
| [[HNRNPA3]] | -0.65 | -0.58 / -0.67 | both halves | 7e-06 |  |
| [[TGOLN2]] | -0.65 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[GNG12]] | -0.64 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[VMA21]] | -0.64 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[MOB1A]] | -0.64 | -0.52 / -0.75 | both halves | 1e-05 |  |
| [[ICMT]] | -0.63 | -0.59 / -0.57 | both halves | 9e-06 |  |
| [[TMX1]] | -0.63 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[PRKDC]] | -0.63 | -0.55 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers ADPRM's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.657). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-39.4, -11.8); signed map (-14.9, -3.4). **Vector** length 77.0, 14.8% of its response variance represented; |z| ≥ 3 in 678 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.3 | +6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.4 | +5.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.9 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +1.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.8 | -7.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.7 | -3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.5 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -3.4 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ADP-ribose/CDP-alcohol diphosphatase, manganese dependent |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:10,697,594-10,711,558 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MDS006; previously C17orf48 |
| Gene groups (HGNC) | Sugar phosphatases |
| Reactome | 4 pathways, smallest: Phosphate bond hydrolysis by NUDT proteins; Purine catabolism; Nucleotide catabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3LIE5](https://www.uniprot.org/uniprotkb/Q3LIE5) (Manganese-dependent ADP-ribose/CDP-alcohol diphosphatase):

> Hydrolyzes ADP-ribose, ADP, CDP-glycerol, CDP-choline, CDP-ethanolamine and cyclic ADP-ribose (cADPR), but not other non-reducing ADP-sugars or CDP-glucose. May be involved in immune cell signaling as suggested by the second-messenger role of ADP-ribose, which activates TRPM2 as a mediator of oxidative/nitrosative stress (By similarity).

**Summary**, from NCBI Gene [56985](https://www.ncbi.nlm.nih.gov/gene/56985):

> Predicted to enable 2',3'-cyclic-nucleotide 2'-phosphodiesterase activity; manganese ion binding activity; and pyrophosphatase activity. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30925](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30925) · Entrez [56985](https://www.ncbi.nlm.nih.gov/gene/56985) · UniProt [Q3LIE5](https://www.uniprot.org/uniprotkb/Q3LIE5) · Ensembl [ENSG00000170222](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170222)

## Data

Gene col 9916: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9916); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9916, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9916]; `tensor/DDL_lfc|DDL_z.npy` [9916]; `embed/gene_vectors.npy` [9916]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9916 or target_col == 9916). Every well: [[ADPRM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADPRM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
