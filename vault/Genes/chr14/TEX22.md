---
symbol: "TEX22"
type: "gene"
col: 13515
ensembl_id: "ENSG00000226174"
name: "testis expressed 22"
location: "14q32.33"
module: 83
arm: "+"
pooled_cpm: 8.03
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# TEX22

*testis expressed 22* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.78× (z +5.8, q 3e-06, up in 21 of 39 measured lines) ⚠ toxic. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.48× (z +5.7, q 3e-06, up in 22 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.614× (z -5.0, q 4e-04, down in 19 of 36 measured lines) ⚠ toxic; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.703× (z -3.7, q 0.051, down in 17 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF26]] (+0.71, fdr 7e-06), [[SMIM15-AS1]] (+0.70, fdr 7e-06), [[MYH3]] (+0.67, fdr 2e-05); moves opposite to [[EFNA4]] (-0.58, fdr 9e-05), [[MPP1]] (-0.58, fdr 1e-04), [[VDAC3]] (-0.57, fdr 6e-05).
> It sits in the **+** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13515.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +5.8 | 3e-06 | 21/39 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.7 | 3e-06 | 22/47 (CFPAC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.56×** | +4.6 | 8e-04 | 18/44 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +4.3 | 0.002 | 20/44 (HCT15, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.1 | 0.004 | 15/43 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.11×** | +4.1 | 0.004 | 11/46 (LoVo, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.024 | 8/47 (HCT15, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +3.6 | 0.024 | 11/21 (SW480, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.42×** | +3.4 | 0.037 | 10/45 (A-427, A549, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.037 | 16/45 (NCI-H23, SHP-77, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.26×** | +3.3 | 0.043 | 17/43 (NCI-H460, LS 180, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.076 | 13/45 (NCI-H2030, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13515.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.614×** | -5.0 | 4e-04 | 19/36 (PANC-1, J82, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.703×** | -3.7 | 0.051 | 17/46 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Ritonavir (drug)]] 0.5 µM |  | **0.712×** | -3.6 | 0.054 | 17/44 (NCI-H1792, HCT15, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.716×** | -3.6 | 0.054 | 15/47 (RPMI-7951, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.736× | -3.3 | 0.12 | 6/47 (NCI-H460, PANC-1, …) | rises with dose | position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | 0.579× | -3.0 | 0.23 | 8/38 (PANC-1, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13515. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 13.1 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -10.7) |
| [[C-33 A (line)]] | alt | 14.1 | 0 | 2 | — | [[5-Fluorouracil (drug)]] 0.5 µM 0.0550× (z -11.6) |
| [[PANC-1 (line)]] | alt | 8.64 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.214× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.239× (z -9.4) |
| [[SNU-423 (line)]] | alt | 4.80 | 0 | 2 | — | [[Cinacalcet (drug)]] 0.05 µM 0.0597× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 5.79 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0843× (z -9.9) |
| [[J82 (line)]] | alt | 6.39 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.127× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[NCI-H23 (line)]] | alt | 9.63 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.103× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 3.54 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0860× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 8.59 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.206× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 24.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.120× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 7.02 | 0 | 1 | — | [[Afatinib (drug)]] 0.05 µM 0.179× (z -8.8) |
| [[A-172 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13515), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF26]] | +0.71 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[SMIM15-AS1]] | +0.70 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[MYH3]] | +0.67 | +0.71 / +0.47 | both halves | 2e-05 |  |
| [[PSMG3-AS1]] | +0.67 | +0.68 / +0.46 | both halves | 2e-05 |  |
| [[C19orf18]] | +0.64 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[PPP1R3F]] | +0.64 | +0.65 / +0.41 | both halves | 4e-05 |  |
| [[PCF11]] | +0.64 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[DPH5-DT]] | +0.64 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[PRC1-AS1]] | +0.64 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[ST20-MTHFS]] | +0.63 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[ANKAR]] | +0.63 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[SSU72]] | +0.62 | +0.47 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFNA4]] | -0.58 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[MPP1]] | -0.58 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[VDAC3]] | -0.57 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[ECI2]] | -0.57 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[ALAD]] | -0.56 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[HPF1]] | -0.56 | -0.18 / -0.41 | ⚠ not reproduced | 1e-03 |  |
| [[PIN1]] | -0.55 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[HACE1]] | -0.55 | -0.53 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TEX22's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HSF2BP]] | C | HSF2BP activity raises TEX22's level | lines that do not express HSF2BP (4) vs lines expressing it (46) | 1.47× lower at baseline in the lines without HSF2BP | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.701). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (28.4, -12.1); signed map (16.6, 2.2). **Vector** length 66.7, 10.2% of its response variance represented; |z| ≥ 3 in 1,014 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +5.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.3 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.9 | +3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +5.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | +1.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +1.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -3.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | testis expressed 22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:105,398,538-105,450,106 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [C9J3V5](https://www.uniprot.org/uniprotkb/C9J3V5) carries no function annotation.

**Summary**, from NCBI Gene [647310](https://www.ncbi.nlm.nih.gov/gene/647310):

> Predicted to be located in acrosomal vesicle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:40026](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40026) · Entrez [647310](https://www.ncbi.nlm.nih.gov/gene/647310) · UniProt [C9J3V5](https://www.uniprot.org/uniprotkb/C9J3V5) · Ensembl [ENSG00000226174](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226174)

## Data

Gene col 13515: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13515); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13515, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13515]; `tensor/DDL_lfc|DDL_z.npy` [13515]; `embed/gene_vectors.npy` [13515]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13515 or target_col == 13515). Every well: [[TEX22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TEX22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
