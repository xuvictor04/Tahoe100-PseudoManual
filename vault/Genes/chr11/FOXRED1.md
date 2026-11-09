---
symbol: "FOXRED1"
type: "gene"
col: 3111
ensembl_id: "ENSG00000110074"
name: "FAD dependent oxidoreductase domain containing 1"
location: "11q24.2"
module: 52
arm: "+"
pooled_cpm: 19.96
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 9
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# FOXRED1

*FAD dependent oxidoreductase domain containing 1* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.89× (z +11.3, q 7e-27, up in 36 of 47 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.37× (z +7.9, q 5e-13, up in 26 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.583× (z -9.6, q 5e-19, down in 30 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.723× (z -5.8, q 2e-06, down in 21 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EDC3]] (+0.69, fdr 7e-06), [[CCDC9]] (+0.68, fdr 7e-06), [[STK19]] (+0.64, fdr 1e-05); moves opposite to [[ARL15]] (-0.49, fdr 1e-04), [[KRAS]] (-0.48, fdr 2e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3111.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.89×** | +11.3 | 7e-27 | 36/47 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.68×** | +9.2 | 9e-18 | 32/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +8.6 | 1e-15 | 7/47 (Hs 766T, LoVo, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +7.9 | 5e-13 | 26/46 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.35×** | +7.5 | 1e-11 | 27/46 (PANC-1, HEC-1-A, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.50×** | +7.3 | 4e-11 | 27/46 (MIA PaCa-2, SW480, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +4.7 | 2e-04 | 18/46 (HCT15, HS-578T, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +4.0 | 0.005 | 10/47 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.013 | 12/44 (LS 180, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.23×** | +3.6 | 0.020 | 12/46 (SW480, SNU-423, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3111.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.583×** | -9.6 | 5e-19 | 30/46 (SHP-77, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.723×** | -5.8 | 2e-06 | 21/46 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.737×** | -5.4 | 1e-05 | 22/47 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.740×** | -5.4 | 1e-05 | 18/46 (LS 180, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.750×** | -5.1 | 3e-05 | 22/46 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.747×** | -5.1 | 3e-05 | 22/47 (HOP62, AN3 CA, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.827×** | -4.8 | 1e-04 | 18/47 (HOP62, HepG2/C3A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.765×** | -4.6 | 3e-04 | 16/31 (NCI-H1573, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.784×** | -4.3 | 1e-03 | 20/47 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.841× | -3.1 | 0.12 | 5/46 (AN3 CA, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3111. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 33.2 | 0 | 2 (1 ⚠) | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0993× (z -12.4) |
| [[HT-29 (line)]] | alt | 20.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[A-172 (line)]] | wt | 9.93 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.218× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0934× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[LoVo (line)]] | wt | 24.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 29.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -9.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -8.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.194× (z -11.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 9.93 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.108× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 11.7 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0854× (z -9.1) |
| [[SW480 (line)]] | alt | 24.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.385× (z -9.6) |
| [[A-427 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.29 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3111), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EDC3]] | +0.69 | +0.68 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[CCDC9]] | +0.68 | +0.61 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[STK19]] | +0.64 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[SRA1]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[SEC16A]] | +0.63 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[RECQL5]] | +0.62 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[UTP6]] | +0.62 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[POLE3]] | +0.61 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[SEC23IP]] | +0.60 | +0.71 / +0.46 | both halves | 2e-05 |  |
| [[ARF4]] | +0.60 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[TMEM104]] | +0.59 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[GOLGA3]] | +0.59 | +0.61 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL15]] | -0.49 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[KRAS]] | -0.48 | -0.51 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers FOXRED1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ARHGEF19]] | C | ARHGEF19 activity raises FOXRED1's level | lines that do not express ARHGEF19 (3) vs lines expressing it (47) | 1.94× lower at baseline in the lines without ARHGEF19 | 0.089 | ⚠ few lines (3 vs 47); across organs; also absent: SLC35F2, ENSG00000274213; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.721). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (9.2, -37.1); signed map (-50.7, 16.7). **Vector** length 80.7, 15.3% of its response variance represented; |z| ≥ 3 in 826 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.2 | +8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +4.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | -0.3 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.7 | +2.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.6 | +2.4 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +1.3 | +1.6 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | +1.3 | +1.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.6 | -4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -5.8 | -5.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.2 | -9.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.3 | -5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.9 | -5.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.1 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | FAD dependent oxidoreductase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:126,269,024-126,278,131 (+) |
| Ensembl biotype | protein_coding |
| Also known as | H17 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors; Flavoproteins; Oxidoreductases |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CU9](https://www.uniprot.org/uniprotkb/Q96CU9) (FAD-dependent oxidoreductase domain-containing protein 1):

> Required for the assembly of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I). Involved in mid-late stages of complex I assembly.

**Summary**, from NCBI Gene [55572](https://www.ncbi.nlm.nih.gov/gene/55572):

> This gene encodes a protein that contains a FAD-dependent oxidoreductase domain. The encoded protein is localized to the mitochondria and may function as a chaperone protein required for the function of mitochondrial complex I. Mutations in this gene are associated with mitochondrial complex I deficiency. Alternatively spliced transcript variants have been observed for this gene. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:26927](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26927) · Entrez [55572](https://www.ncbi.nlm.nih.gov/gene/55572) · UniProt [Q96CU9](https://www.uniprot.org/uniprotkb/Q96CU9) · Ensembl [ENSG00000110074](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110074)

## Data

Gene col 3111: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3111); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3111, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3111]; `tensor/DDL_lfc|DDL_z.npy` [3111]; `embed/gene_vectors.npy` [3111]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3111 or target_col == 3111). Every well: [[FOXRED1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXRED1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
