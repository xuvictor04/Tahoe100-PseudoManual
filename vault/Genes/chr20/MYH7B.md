---
symbol: "MYH7B"
type: "gene"
col: 1235
ensembl_id: "ENSG00000078814"
name: "myosin heavy chain 7B"
location: "20q11.22"
module: 35
arm: "+"
pooled_cpm: 2.97
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 6
n_dd_up_clean: 25
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# MYH7B

*myosin heavy chain 7B* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.58× (z +23.8, q 0e+00, up in 29 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.527× (z -6.3, q 2e-07, down in 17 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRIG2-DT]] (+0.66, fdr 7e-06), [[PLA2G6]] (+0.62, fdr 1e-05), [[BCAR3-AS1]] (+0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FGF20]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1235.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.58×** | +23.8 | 0e+00 | 29/30 (BT-474, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.89×** | +12.8 | 4e-35 | 1/2 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.39×** | +8.2 | 4e-14 | 13/23 (HEC-1-A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.20×** | +7.7 | 2e-12 | 2/10 (SW480, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.56×** | +6.1 | 7e-08 | 8/43 (BT-474, SW1417, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +6.1 | 7e-08 | 14/31 (HEC-1-A, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.30×** | +5.7 | 8e-07 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +5.7 | 9e-07 | 10/32 (C32, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.70×** | +5.0 | 4e-05 | 8/29 (SW480, A-172, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.61×** | +4.7 | 2e-04 | 11/45 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.58×** | +4.3 | 9e-04 | 9/35 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +4.2 | 0.001 | 9/40 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.002 | 6/40 (BT-474, KATO III, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.002 | 3/43 (C-33 A, NCI-H460, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.49×** | +3.9 | 0.004 | 9/37 (CFPAC-1, HS-578T, …) | two highest doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +3.6 | 0.010 | 3/39 (SW 900, SW1417, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.67×** | +3.6 | 0.010 | 1/17 (PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.44×** | +3.6 | 0.010 | 6/43 (SW480, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1235.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.527×** | -6.3 | 2e-07 | 17/39 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.585×** | -5.3 | 3e-05 | 17/44 (A-427, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.588×** | -5.2 | 3e-05 | 15/34 (BT-474, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.651×** | -4.2 | 0.004 | 7/43 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.670×** | -3.9 | 0.010 | 13/38 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.673×** | -3.9 | 0.010 | 9/44 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.724× | -3.0 | 0.19 | 5/39 (AsPC-1, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1235. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 4.84 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0294× (z -12.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Sunitinib (drug)]] 0.5 µM 0.0627× (z -10.0) |
| [[BT-474 (line)]] | alt | 12.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.1× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 2.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.58× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 1.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.12× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 3.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.12× (z +8.6) | — |
| [[SW480 (line)]] | alt | 18.9 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0832× (z -9.2) |
| [[A-172 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.871 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1235), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRIG2-DT]] | +0.66 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[PLA2G6]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[BCAR3-AS1]] | +0.61 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[LRRC56]] | +0.60 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[ERICH2-DT]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[ACKR2]] | +0.59 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[CNN3-DT]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[PSD]] | +0.58 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[COL11A2]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[LINC03048]] | +0.58 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[AXDND1]] | +0.58 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[CCDC17]] | +0.58 | +0.51 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGF20]] | B | FGF20 activity raises MYH7B's level | lines that do not express FGF20 (41) vs lines expressing it (9) | 1.72× lower at baseline in the lines without FGF20 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, HEPHL1, GCG |
| [[NOTUM]] | B | NOTUM activity raises MYH7B's level | lines that do not express NOTUM (31) vs lines expressing it (19) | 1.42× lower at baseline in the lines without NOTUM | 0.040 | ⚠ within organs, on part of the lines; also absent: FGF20, AXIN2, XKR7 |
| [[TOP2A]] | B | TOP2A activity lowers MYH7B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.608). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (15.8, 22.2); signed map (34.3, -1.3). **Vector** length 51.8, 7.02% of its response variance represented; |z| ≥ 3 in 1,068 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +23.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.7 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +6.1 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.1 | +4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +5.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.6 | +2.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.5 | +3.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.3 | -5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.8 | -3.9 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.7 | -5.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.9 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | myosin heavy chain 7B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:34,955,810-35,002,437 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1512, dJ756N5.1, MYH14, MHC14, lncMYH7b |
| Gene groups (HGNC) | Myosin heavy chains, class II; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [A7E2Y1](https://www.uniprot.org/uniprotkb/A7E2Y1) (Myosin-7B):

> Involved in muscle contraction.

**Summary**, from NCBI Gene [57644](https://www.ncbi.nlm.nih.gov/gene/57644):

> The myosin II molecule is a multi-subunit complex consisting of two heavy chains and four light chains. This gene encodes a heavy chain of myosin II, which is a member of the motor-domain superfamily. The heavy chain includes a globular motor domain, which catalyzes ATP hydrolysis and interacts with actin, and a tail domain in which heptad repeat sequences promote dimerization by interacting to form a rod-like alpha-helical coiled coil. This heavy chain subunit is a slow-twitch myosin. …

**Accessions** — [HGNC:15906](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15906) · Entrez [57644](https://www.ncbi.nlm.nih.gov/gene/57644) · UniProt [A7E2Y1](https://www.uniprot.org/uniprotkb/A7E2Y1) · Ensembl [ENSG00000078814](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078814)

## Data

Gene col 1235: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1235); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1235, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1235]; `tensor/DDL_lfc|DDL_z.npy` [1235]; `embed/gene_vectors.npy` [1235]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1235 or target_col == 1235). Every well: [[MYH7B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYH7B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
