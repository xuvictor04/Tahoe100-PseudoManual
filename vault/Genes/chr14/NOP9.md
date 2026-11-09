---
symbol: "NOP9"
type: "gene"
col: 12308
ensembl_id: "ENSG00000196943"
name: "NOP9 nucleolar protein"
location: "14q12"
module: 127
arm: "+"
pooled_cpm: 11.38
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# NOP9

*NOP9 nucleolar protein* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.31× (z +14.6, q 1e-45, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.721× (z -4.0, q 0.037, down in 17 of 47 measured lines) ⚠ unreliable plate only; position not correctable. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (CFPAC-1 0.0897×; ⚠ toxic; cell-cycle shift, explains ~70% of this change); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (HS-578T 0.0805×); [[Orlistat (drug)]] 0.05 µM in 1 line (NCI-H23 0.127×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (RKO 0.133×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANAPC2]] (+0.74, fdr 7e-06), [[PCNX3]] (+0.74, fdr 7e-06), [[NOC2L]] (+0.72, fdr 7e-06); moves opposite to [[TIPRL]] (-0.60, fdr 1e-05), [[SNHG32]] (-0.59, fdr 1e-05), [[TRIM52-AS1]] (-0.58, fdr 1e-05).
> It is in [[Module 127]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12308.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.31×** | +14.6 | 1e-45 | 45/47 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.78×** | +12.5 | 2e-33 | 46/47 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.42×** | +10.8 | 6e-25 | 44/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.44×** | +6.3 | 5e-08 | 23/46 (SW480, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.69×** | +6.2 | 8e-08 | 11/20 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.59×** | +6.1 | 1e-07 | 30/47 (LS 180, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.4 | 5e-06 | 25/48 (A-427, Panc 03.27, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +5.4 | 6e-06 | 2/48 (HS-578T, SW 900) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.21×** | +5.1 | 3e-05 | 22/43 (LS 180, KATO III, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.45×** | +4.4 | 7e-04 | 16/46 (SW480, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.005 | 14/47 (NCI-H460, SW480, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.35×** | +3.7 | 0.011 | 12/36 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.37×** | +3.7 | 0.011 | 13/47 (HEC-1-A, SW1417, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.022 | 12/47 (NCI-H1573, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.028 | 7/47 (NCI-H1573, A498, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12308.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (CFPAC-1 0.0897×; ⚠ toxic; cell-cycle shift, explains ~70% of this change); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (HS-578T 0.0805×); [[Orlistat (drug)]] 0.05 µM in 1 line (NCI-H23 0.127×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (RKO 0.133×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.721×** | -4.0 | 0.037 | 17/47 (HT-29, NCI-H2347, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.736×** | -3.7 | 0.052 | 12/47 (HEC-1-A, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12308. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 14.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.90× (z +8.8) | — |
| [[SW480 (line)]] | alt | 13.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.81× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0897× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~70% of this change |
| [[Hs 766T (line)]] | wt | 7.47 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.05 µM 0.103× (z -9.0) |
| [[HS-578T (line)]] | alt | 7.34 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0805× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 8.94 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0895× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 16.2 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.127× (z -10.6) |
| [[RKO (line)]] | wt | 15.8 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.133× (z -9.9) |
| [[A-172 (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12308), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC2]] | +0.74 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[PCNX3]] | +0.74 | +0.62 / +0.76 | both halves | 7e-06 |  |
| [[NOC2L]] | +0.72 | +0.72 / +0.67 | both halves | 7e-06 | same gene group; STRING 916 |
| [[TBL3]] | +0.72 | +0.69 / +0.71 | both halves | 7e-06 | STRING 861 |
| [[BAP1]] | +0.72 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[CHID1]] | +0.71 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[TUBGCP6]] | +0.71 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[CDK9]] | +0.69 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[EMC1]] | +0.68 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[CCDC61]] | +0.68 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[MYBBP1A]] | +0.66 | +0.67 / +0.65 | both halves | 7e-06 | same gene group |
| [[GRWD1]] | +0.66 | +0.70 / +0.68 | both halves | 7e-06 | STRING 853 |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIPRL]] | -0.60 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[SNHG32]] | -0.59 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[TRIM52-AS1]] | -0.58 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[SNHG8]] | -0.58 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[ZMYM5]] | -0.55 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[NACA4P]] ⚠ | -0.55 | -0.41 / -0.61 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NKAP]] | -0.54 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[GATAD1]] | -0.54 | -0.47 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NOP9's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.755). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.1, -26.9); signed map (-13.5, -31.3). **Vector** length 70.7, 11.6% of its response variance represented; |z| ≥ 3 in 983 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.3 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +5.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.2 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +3.1 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | +2.9 | +3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +5.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.0 | +3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | -1.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -2.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | +2.5 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.0 | -2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | NOP9 nucleolar protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:24,299,850-24,309,124 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C14orf21 |
| Gene groups (HGNC) | SSU processome; Armadillo like helical domain containing |
| Matched by | ensembl_id |

UniProt [Q86U38](https://www.uniprot.org/uniprotkb/Q86U38) carries no function annotation.

**Summary**, from NCBI Gene [161424](https://www.ncbi.nlm.nih.gov/gene/161424):

> Enables RNA binding activity. Predicted to be involved in ribosome biogenesis. Predicted to be part of 90S preribosome and preribosome, small subunit precursor. Predicted to be active in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19826](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19826) · Entrez [161424](https://www.ncbi.nlm.nih.gov/gene/161424) · UniProt [Q86U38](https://www.uniprot.org/uniprotkb/Q86U38) · Ensembl [ENSG00000196943](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196943)

## Data

Gene col 12308: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12308); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12308, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12308]; `tensor/DDL_lfc|DDL_z.npy` [12308]; `embed/gene_vectors.npy` [12308]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12308 or target_col == 12308). Every well: [[NOP9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOP9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
