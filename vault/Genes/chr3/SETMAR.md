---
symbol: "SETMAR"
type: "gene"
col: 9940
ensembl_id: "ENSG00000170364"
name: "SET and mariner transposase domain methyltransferase"
location: "3p26.1"
module: 1
arm: "+"
pooled_cpm: 2.69
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# SETMAR

*SET and mariner transposase domain methyltransferase* — 3p26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.67× (z +5.1, q 1e-04, up in 5 of 15 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.41× (z +5.0, q 1e-04, up in 8 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.437× (z -8.5, q 1e-14, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPRYD4]] (+0.65, fdr 1e-05), [[PIGW]] (+0.63, fdr 3e-05), [[ZNF239]] (+0.62, fdr 1e-05); moves opposite to [[NBEAL1]] (-0.61, fdr 1e-05), [[SRSF9]] (-0.58, fdr 5e-05, ⚠ SRSF9 in the vector space only through flagged drug-doses), [[PHF1]] (-0.57, fdr 4e-05), [[PPARA]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PGAP4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9940.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +5.1 | 1e-04 | 5/15 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +5.1 | 1e-04 | 0/3 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.0 | 1e-04 | 8/34 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.35×** | +4.4 | 0.002 | 4/44 (SW1417, C-33 A, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +3.7 | 0.025 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.063 | 1/45 (LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.078 | 3/39 (HepG2/C3A, C32, …) | all doses, flat |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.37×** | +3.2 | 0.094 | 4/32 (H4, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | 1.36× | +3.0 | 0.15 | 0/37 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9940.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.437×** | -8.5 | 1e-14 | 26/46 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.597×** | -5.3 | 4e-05 | 17/43 (RKO, LS 180, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.659×** | -4.2 | 0.004 | 10/45 (SW480, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.690×** | -3.8 | 0.021 | 16/42 (SW480, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.695×** | -3.7 | 0.024 | 15/29 (MIA PaCa-2, SW480, …) | two highest doses |  |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | **0.720×** | -3.3 | 0.071 | 7/35 (A498, RPMI-7951, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.722×** | -3.3 | 0.071 | 13/43 (A-172, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | **0.727×** | -3.3 | 0.080 | 12/38 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.729×** | -3.2 | 0.080 | 12/45 (COLO 205, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.731×** | -3.2 | 0.080 | 8/45 (CHP-212, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9940. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 2.21 | 0 | 1 | — | [[Mozavaptan (drug)]] 5 µM 0.0678× (z -8.6) |
| [[A-172 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.681 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9940), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPRYD4]] | +0.65 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[PIGW]] | +0.63 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[ZNF239]] | +0.62 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[EXO5]] | +0.61 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[SCO1]] | +0.61 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[FZD6]] | +0.61 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[MAPKAPK5]] | +0.60 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[MTMR2]] | +0.60 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[FAIM]] | +0.60 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[SLC9B2]] | +0.59 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[ZNF195]] | +0.59 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[PACRGL]] | +0.58 | +0.46 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBEAL1]] | -0.61 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[SRSF9]] ⚠ | -0.58 | -0.40 / -0.46 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PHF1]] | -0.57 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[PPARA]] | -0.55 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[DNAAF3]] | -0.55 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[PGPEP1]] | -0.55 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[VEGFB]] | -0.55 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[MINDY2]] | -0.54 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[CDKN2D]] | -0.54 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[MAPK8IP3]] | -0.54 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[ARID4A]] | -0.54 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[RASA4B]] | -0.54 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[GABARAPL2]] | -0.53 | -0.45 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PGAP4]] | B | PGAP4 activity raises SETMAR's level | lines that do not express PGAP4 (17) vs lines expressing it (33) | 1.10× lower at baseline in the lines without PGAP4 | 0.061 | ⚠ within organs, on part of the lines; also absent: CRACR2A, TMEM98, ARMCX4 |
| [[ZNF239]] | B | ZNF239 activity lowers SETMAR's level | lines that do not express ZNF239 (8) vs lines expressing it (42) | 1.30× higher at baseline in the lines without ZNF239 | 0.080 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.523). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-6.2, 9.1); signed map (12.2, -42.5). **Vector** length 40.1, 3.91% of its response variance represented; |z| ≥ 3 in 1,063 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +2.2 | +3.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +2.1 | +4.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.8 | +2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.0 | +1.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +0.9 | +0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.9 | +3.0 |
|  | [[EX229 (drug)]] 5 µM |  | +0.9 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.8 | +2.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.1 | -8.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | -2.0 | -3.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.9 | -3.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.3 | -3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.8 | -0.2 |
|  | [[Adagrasib (drug)]] 5 µM |  | -0.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | SET and mariner transposase domain methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p26.1 — chr3:4,303,332-4,317,265 (+) |
| Ensembl biotype | protein_coding |
| Also known as | metnase |
| Gene groups (HGNC) | SET domain containing; Mariner transposase derived genes; Putative lysine methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53H47](https://www.uniprot.org/uniprotkb/Q53H47) (Histone-lysine N-methyltransferase SETMAR):

> Protein derived from the fusion of a methylase with the transposase of an Hsmar1 transposon that plays a role in DNA double-strand break repair, stalled replication fork restart and DNA integration. DNA-binding protein, it is indirectly recruited to sites of DNA damage through protein-protein interactions. Also has kept a sequence-specific DNA-binding activity recognizing the 19-mer core of the 5'-terminal inverted repeats (TIRs) of the Hsmar1 element and displays a DNA nicking and end joining …

**Summary**, from NCBI Gene [6419](https://www.ncbi.nlm.nih.gov/gene/6419):

> This gene encodes a fusion protein that contains an N-terminal histone-lysine N-methyltransferase domain and a C-terminal mariner transposase domain. The encoded protein binds DNA and functions in DNA repair activities including non-homologous end joining and double strand break repair. The SET domain portion of this protein specifically methylates histone H3 lysines 4 and 36. This gene exists as a fusion gene only in anthropoid primates, other organisms lack mariner transposase domain. …

**Accessions** — [HGNC:10762](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10762) · Entrez [6419](https://www.ncbi.nlm.nih.gov/gene/6419) · UniProt [Q53H47](https://www.uniprot.org/uniprotkb/Q53H47) · Ensembl [ENSG00000170364](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170364)

## Data

Gene col 9940: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9940); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9940, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9940]; `tensor/DDL_lfc|DDL_z.npy` [9940]; `embed/gene_vectors.npy` [9940]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9940 or target_col == 9940). Every well: [[SETMAR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SETMAR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
