---
symbol: "TMEM186"
type: "gene"
col: 11582
ensembl_id: "ENSG00000184857"
name: "transmembrane protein 186"
location: "16p13.2"
module: 15
arm: "+"
pooled_cpm: 4.66
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 3
n_dd_up_clean: 17
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# TMEM186

*transmembrane protein 186* — 16p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.97× (z +18.3, q 0e+00, up in 33 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.526× (z -7.7, q 8e-12, down in 19 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BAAT]] (+0.68, fdr 1e-05), [[LINC01618]] (+0.66, fdr 7e-06), [[SMIM12]] (+0.66, fdr 7e-06); moves opposite to [[NDRG3]] (-0.60, fdr 3e-05), [[RTN3]] (-0.56, fdr 5e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PXDC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11582.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.97×** | +18.3 | 0e+00 | 33/38 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +8.4 | 1e-14 | 7/9 (SW480, J82, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +7.9 | 5e-13 | 13/24 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.93×** | +7.8 | 9e-13 | 25/44 (SW480, NCI-H23, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.56×** | +7.4 | 1e-11 | 14/46 (A-172, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +7.4 | 2e-11 | 17/38 (HCT15, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +7.2 | 5e-11 | 0/4 | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +6.9 | 3e-10 | 18/37 (LoVo, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +6.0 | 1e-07 | 10/32 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.2 | 1e-05 | 10/37 (SW480, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +5.2 | 1e-05 | 11/23 (A-427, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +4.9 | 4e-05 | 10/44 (A549, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.52×** | +4.6 | 2e-04 | 10/38 (LoVo, A-172, …) | all doses, flat | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.6 | 2e-04 | 6/48 (BT-474, KATO III, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +4.4 | 5e-04 | 9/44 (HepG2/C3A, J82, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +4.3 | 7e-04 | 8/42 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.005 | 3/45 (SW480, SNU-423, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.032 | 7/40 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.034 | 5/42 (LOX-IMVI, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.034 | 8/38 (BT-474, NCI-H2347, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11582.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.526×** | -7.7 | 8e-12 | 19/46 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.679×** | -4.7 | 9e-04 | 17/45 (AsPC-1, HCT15, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.718×** | -4.0 | 0.013 | 15/44 (RPMI-7951, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.765× | -3.2 | 0.18 | 15/36 (PANC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Allantoin (drug)]] 5 µM |  | 0.838× | -3.0 | 0.28 | 6/44 (hTERT-HPNE, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11582. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.42 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.13× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -9.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 44.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -12.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 4.83 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0836× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 4.46 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0512× (z -11.3) |
| [[SW480 (line)]] | alt | 4.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +9.3) | — |
| [[A-172 (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11582), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAAT]] | +0.68 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[LINC01618]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[SMIM12]] | +0.66 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[KDM4D]] | +0.65 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[CHTF8]] | +0.65 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[SMIM15-AS1]] | +0.65 | +0.70 / +0.40 | both halves | 5e-05 |  |
| [[IL34]] | +0.64 | +0.63 / +0.38 | both halves | 6e-05 |  |
| [[HAVCR2]] | +0.64 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[BCDIN3D]] | +0.63 | +0.71 / +0.38 | both halves | 6e-05 |  |
| [[MZF1-AS1]] | +0.63 | +0.69 / +0.41 | both halves | 4e-05 |  |
| [[MYH3]] | +0.63 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[FAM200A]] | +0.63 | +0.66 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDRG3]] | -0.60 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[RTN3]] | -0.56 | -0.50 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PXDC1]] | B | PXDC1 activity lowers TMEM186's level | lines that do not express PXDC1 (9) vs lines expressing it (41) | 1.57× higher at baseline in the lines without PXDC1 | 0.015 | ⚠ within organs, on part of the lines; also absent: TSPAN4, OSMR, VIM |
| [[TOP2A]] | B | TOP2A activity lowers TMEM186's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.482). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (11.3, 6.2); signed map (19.1, -6.9). **Vector** length 48.1, 5.55% of its response variance represented; |z| ≥ 3 in 898 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +18.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +7.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.5 | +7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +4.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -1.9 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -7.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -4.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -1.4 | +3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | +0.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 186 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.2 — chr16:8,780,384-8,797,642 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564K2062; previously C16orf51 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors; Mitochondrial complex I assembly complex |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96B77](https://www.uniprot.org/uniprotkb/Q96B77) (Transmembrane protein 186):

> As part of the MCIA complex, required for efficient assembly of the mitochondrial complex I.

**Summary**, from NCBI Gene [25880](https://www.ncbi.nlm.nih.gov/gene/25880):

> This gene encodes a potential transmembrane protein. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:24530](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24530) · Entrez [25880](https://www.ncbi.nlm.nih.gov/gene/25880) · UniProt [Q96B77](https://www.uniprot.org/uniprotkb/Q96B77) · Ensembl [ENSG00000184857](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184857)

## Data

Gene col 11582: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11582); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11582, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11582]; `tensor/DDL_lfc|DDL_z.npy` [11582]; `embed/gene_vectors.npy` [11582]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11582 or target_col == 11582). Every well: [[TMEM186 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM186.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
