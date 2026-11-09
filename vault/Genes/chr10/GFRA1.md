---
symbol: "GFRA1"
type: "gene"
col: 7577
ensembl_id: "ENSG00000151892"
name: "GDNF family receptor alpha 1"
location: "10q25.3"
module: 66
arm: "+"
pooled_cpm: 4.28
n_lines_expressing: 17
n_dd_up: 35
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# GFRA1

*GDNF family receptor alpha 1* — 10q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.30× (z +22.2, q 0e+00, up in 13 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1QTNF1-AS1]] (+0.67, fdr 1e-05), [[COL12A1]] (+0.66, fdr 7e-06), [[LINC02605]] (+0.61, fdr 1e-05); moves opposite to [[SDHAF1]] (-0.57, fdr 1e-05), [[ZNF549]] (-0.56, fdr 5e-05), [[SMYD4]] (-0.51, fdr 4e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CACNA1E]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7577.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.30×** | +22.2 | 0e+00 | 13/13 (A498, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **5.79×** | +21.2 | 0e+00 | 11/12 (SNU-423, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.29×** | +14.2 | 1e-43 | 4/7 (A498, J82, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.78×** | +12.9 | 1e-35 | 4/4 (J82, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.62×** | +12.1 | 1e-31 | 6/6 (J82, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.01×** | +9.1 | 1e-17 | 12/13 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.56×** | +7.7 | 1e-12 | 8/11 (SNU-423, A-172, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +6.9 | 3e-10 | 8/13 (NCI-H1573, C32, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.71×** | +6.5 | 7e-09 | 6/13 (A-172, A549, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.09×** | +6.3 | 2e-08 | 7/12 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +6.3 | 2e-08 | 2/9 (A-172, BT-474) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +5.7 | 5e-07 | 2/9 (SNU-423, A-172) | top dose only | cell-cycle shift (explains ~10% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.53×** | +5.7 | 7e-07 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +5.5 | 1e-06 | 6/9 (SNU-423, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +5.2 | 8e-06 | 2/8 (Panc 03.27, A498) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.82×** | +5.1 | 1e-05 | 6/13 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.79×** | +4.9 | 3e-05 | 8/14 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +4.8 | 5e-05 | 7/13 (NCI-H2030, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.82×** | +3.6 | 0.007 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.80×** | +3.6 | 0.008 | 0/13 | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +3.5 | 0.013 | 4/13 (BT-474, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.54×** | +3.4 | 0.015 | 0/10 | inconsistent across doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7577. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 39.6 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +9.5) | — |
| [[A-172 (line)]] | wt | 3.44 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.9× (z +12.3) | — |
| [[A498 (line)]] | wt | 19.7 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.18× (z +16.3) | — |
| [[A549 (line)]] | wt | 7.26 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.33× (z +11.9) | — |
| [[BT-474 (line)]] | alt | 6.13 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 46.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.71× (z +15.9) | — |
| [[C32 (line)]] | wt | 1.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 34.6× (z +10.0) | — |
| [[hTERT-HPNE (line)]] | wt | 2.10 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.6× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 3.79 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +9.6) | — |
| [[A-427 (line)]] | wt | 0.532 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.403 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.984 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.386 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.402 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.387 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.425 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.456 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.366 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.340 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.339 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.860 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.338 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.821 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.380 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.783 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.707 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.434 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.397 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.549 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.381 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7577), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1QTNF1-AS1]] | +0.67 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[COL12A1]] | +0.66 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[LINC02605]] | +0.61 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[PSG4]] | +0.60 | +0.70 / +0.44 | both halves | 3e-05 |  |
| [[LINC01933]] | +0.59 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[THSD7B]] | +0.59 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[RBFOX3]] | +0.59 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[OGFRL1]] | +0.58 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[ANK1]] | +0.58 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[LYPD1]] | +0.58 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[RBM24]] | +0.58 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[SSPN]] | +0.57 | +0.45 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAF1]] | -0.57 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[ZNF549]] | -0.56 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[SMYD4]] | -0.51 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[GTF2E2]] | -0.51 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[HERC2P2]] | -0.50 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[CDK5RAP1]] | -0.50 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[HERC2P3]] | -0.49 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[SELENOO]] | -0.49 | -0.28 / -0.44 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GFRA1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNA1E]] | B | GFRA1 activity raises CACNA1E's level | lines that do not express GFRA1 (33) vs lines expressing it (17) | 1.05× lower at baseline in the lines without GFRA1 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NLGN4Y, MAPK4, GREM2 |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.561). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.2, 21.2); signed map (43.7, 19.5). **Vector** length 39.9, 11.1% of its response variance represented; |z| ≥ 3 in 372 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +12.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +22.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +21.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +2.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +0.9 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.9 | +0.8 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +1.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -2.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | +0.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | -1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | -0.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | -2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.8 | +0.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | GDNF family receptor alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.3 — chr10:116,056,925-116,276,803 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RETL1, GDNFR, GFR-ALPHA-1, RET1L, TRNR1; previously GDNFRA |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 10 pathways, smallest: Formation of the ureteric bud; NCAM1 interactions; RET signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P56159](https://www.uniprot.org/uniprotkb/P56159) (GDNF family receptor alpha-1):

> Coreceptor for GDNF, a neurotrophic factor that enhances survival and morphological differentiation of dopaminergic neurons and increases their high-affinity dopamine uptake. GDNF-binding leads to autophosphorylation and activation of the RET receptor.

**Summary**, from NCBI Gene [2674](https://www.ncbi.nlm.nih.gov/gene/2674):

> This gene encodes a member of the glial cell line-derived neurotrophic factor receptor (GDNFR) family of proteins. The encoded preproprotein is proteolytically processed to generate the mature receptor. Glial cell line-derived neurotrophic factor (GDNF) and neurturin (NTN) are two structurally related, potent neurotrophic factors that play key roles in the control of neuron survival and differentiation. This receptor is a glycosylphosphatidylinositol (GPI)-linked cell surface receptor for both …

**Accessions** — [HGNC:4243](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4243) · Entrez [2674](https://www.ncbi.nlm.nih.gov/gene/2674) · UniProt [P56159](https://www.uniprot.org/uniprotkb/P56159) · Ensembl [ENSG00000151892](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151892)

## Data

Gene col 7577: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7577); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7577, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7577]; `tensor/DDL_lfc|DDL_z.npy` [7577]; `embed/gene_vectors.npy` [7577]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7577 or target_col == 7577). Every well: [[GFRA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GFRA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
