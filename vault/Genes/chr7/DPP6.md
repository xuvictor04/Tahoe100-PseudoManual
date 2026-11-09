---
symbol: "DPP6"
type: "gene"
col: 5037
ensembl_id: "ENSG00000130226"
name: "dipeptidyl peptidase like 6"
location: "7q36.2"
module: 75
arm: "+"
pooled_cpm: 6.34
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# DPP6

*dipeptidyl peptidase like 6* — 7q36.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.19× (z +30.2, q 0e+00, up in 35 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Radotinib (drug)]] 0.5 µM in 1 line (LoVo 0.0676×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLVS1]] (+0.86, fdr 7e-06), [[LRRC4C]] (+0.85, fdr 7e-06), [[GRM8]] (+0.85, fdr 7e-06).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5037.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.19×** | +30.2 | 0e+00 | 35/37 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **6.09×** | +23.4 | 0e+00 | 37/42 (SW480, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.79×** | +21.1 | 0e+00 | 10/12 (SW480, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.77×** | +20.3 | 0e+00 | 18/20 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.90×** | +19.5 | 0e+00 | 28/37 (C32, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.25×** | +18.0 | 0e+00 | 6/7 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.47×** | +11.7 | 7e-30 | 23/36 (RPMI-7951, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.21×** | +10.3 | 6e-23 | 25/42 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +9.4 | 3e-19 | 19/44 (SW480, A-427, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.61×** | +8.8 | 8e-17 | 16/46 (A-172, RPMI-7951, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +8.4 | 3e-15 | 15/33 (H4, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.80×** | +7.3 | 1e-11 | 19/43 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +6.2 | 2e-08 | 5/30 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +5.6 | 1e-06 | 11/42 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.11×** | +5.1 | 2e-05 | 0/9 | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.0 | 2e-05 | 14/36 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.009 | 5/46 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.011 | 2/41 (NCI-H460, SHP-77) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.023 | 4/43 (SW1417, HEC-1-A, …) | two highest doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.19× | +3.2 | 0.036 | 4/44 (HOP62, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5037.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Radotinib (drug)]] 0.5 µM in 1 line (LoVo 0.0676×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Entecavir (monohydrate) (drug)]] 0.05 µM |  | 0.755× | -3.4 | 0.45 | 5/41 (J82, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5037. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 3.21 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +12.8) | [[Radotinib (drug)]] 0.5 µM 0.0676× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 2.50 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 36.4× (z +13.7) | — |
| [[C32 (line)]] | wt | 3.12 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.9× (z +12.0) | — |
| [[PANC-1 (line)]] | alt | 2.05 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.14× (z +10.7) | — |
| [[SW480 (line)]] | alt | 6.14 | 3 | 0 | [[Auranofin (drug)]] 5 µM 23.6× (z +17.5) | — |
| [[HEC-1-A (line)]] | alt | 3.87 | 2 | 0 | [[Auranofin (drug)]] 5 µM 20.3× (z +11.6) | — |
| [[A498 (line)]] | wt | 2.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.10× (z +10.6) | — |
| [[A549 (line)]] | wt | 3.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +11.7) | — |
| [[BT-474 (line)]] | alt | 3.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 4.09 | 1 | 0 | [[Auranofin (drug)]] 5 µM 12.6× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 2.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.77× (z +9.7) | — |
| [[Hs 766T (line)]] | wt | 2.67 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 4.87 | 1 | 0 | [[Auranofin (drug)]] 5 µM 29.0× (z +13.1) | — |
| [[KATO III (line)]] | alt | 2.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.2× (z +10.3) | — |
| [[LS 180 (line)]] | wt | 3.72 | 1 | 0 | [[Auranofin (drug)]] 5 µM 19.0× (z +10.2) | — |
| [[SW48 (line)]] | wt | 3.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 51.4× (z +11.4) | — |
| [[A-172 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5037), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLVS1]] | +0.86 | +0.68 / +0.83 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.85 | +0.77 / +0.82 | both halves | 7e-06 |  |
| [[GRM8]] | +0.85 | +0.78 / +0.79 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.83 | +0.79 / +0.76 | both halves | 7e-06 |  |
| [[KCNAB1]] | +0.82 | +0.77 / +0.82 | both halves | 7e-06 | same gene group; STRING 429 |
| [[PPP1R9A-AS1]] | +0.81 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[HPSE2]] | +0.80 | +0.61 / +0.78 | both halves | 7e-06 |  |
| [[CCDC26]] | +0.79 | +0.61 / +0.78 | both halves | 7e-06 |  |
| [[LINC01090]] | +0.79 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[LINC01033]] | +0.78 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[GRM7]] | +0.78 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[OPCML]] | +0.78 | +0.72 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DPP6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.897). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.4, 27.7); signed map (31.9, 13.7). **Vector** length 65.8, 10.2% of its response variance represented; |z| ≥ 3 in 1,007 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.6 | +30.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.2 | +23.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.9 | +20.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.7 | +18.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.0 | +21.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +9.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +8.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +1.3 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.5 | -2.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +0.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -1.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | dipeptidyl peptidase like 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.2 — chr7:153,748,133-154,894,285 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DPPX, DPL1 |
| Gene groups (HGNC) | Potassium voltage-gated channel regulatory subunits; DASH family |
| Matched by | ensembl_id |

**Function**, from UniProt [P42658](https://www.uniprot.org/uniprotkb/P42658) (A-type potassium channel modulatory protein DPP6):

> Promotes cell surface expression of the potassium channel KCND2. Modulates the activity and gating characteristics of the potassium channel KCND2. Has no dipeptidyl aminopeptidase activity.

**Summary**, from NCBI Gene [1804](https://www.ncbi.nlm.nih.gov/gene/1804):

> This gene encodes a single-pass type II membrane protein that is a member of the peptidase S9B family of serine proteases. This protein has no detectable protease activity, most likely due to the absence of the conserved serine residue normally present in the catalytic domain of serine proteases. However, it does bind specific voltage-gated potassium channels and alters their expression and biophysical properties. Variations in this gene may be associated with susceptibility to amyotrophic …

**Accessions** — [HGNC:3010](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3010) · Entrez [1804](https://www.ncbi.nlm.nih.gov/gene/1804) · UniProt [P42658](https://www.uniprot.org/uniprotkb/P42658) · Ensembl [ENSG00000130226](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130226)

## Data

Gene col 5037: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5037); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5037, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5037]; `tensor/DDL_lfc|DDL_z.npy` [5037]; `embed/gene_vectors.npy` [5037]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5037 or target_col == 5037). Every well: [[DPP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
