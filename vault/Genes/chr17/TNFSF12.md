---
symbol: "TNFSF12"
type: "gene"
col: 14206
ensembl_id: "ENSG00000239697"
name: "TNF superfamily member 12"
location: "17p13.1"
module: 21
arm: "+"
pooled_cpm: 2.06
n_lines_expressing: 38
n_dd_up: 9
n_dd_down: 18
n_dd_up_clean: 5
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# TNFSF12

*TNF superfamily member 12* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.98× (z +13.0, q 4e-36, up in 13 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.384× (z -8.1, q 4e-13, down in 16 of 21 measured lines).
> Its strongest partners by |cos| (81 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUOX]] (+0.60, fdr 1e-05), [[SEPTIN1]] (+0.57, fdr 7e-05), [[SPATA1]] (+0.57, fdr 4e-04); moves opposite to [[INA]] (-0.45, fdr 7e-05), [[ZNF770]] (-0.45, fdr 1e-04), [[IPO9]] (-0.44, fdr 4e-04).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[TBX1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14206.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.98×** | +13.0 | 4e-36 | 13/20 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.26×** | +9.2 | 1e-17 | 1/4 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.45×** | +7.6 | 7e-12 | 8/11 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.31×** | +6.5 | 9e-09 | 1/5 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.07×** | +6.1 | 9e-08 | 6/10 (A-172, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.85×** | +3.7 | 0.019 | 4/10 (hTERT-HPNE, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.81×** | +3.6 | 0.029 | 1/15 (A498) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.098 | 6/15 (A-172, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.69×** | +3.2 | 0.098 | 1/20 (J82) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.29× | +3.1 | 0.12 | 6/24 (A498, C32, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14206.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.384×** | -8.1 | 4e-13 | 16/21 (A-172, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.388×** | -7.3 | 6e-11 | 19/31 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.431×** | -7.1 | 2e-10 | 20/31 (J82, SW1417, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.468×** | -6.4 | 2e-08 | 14/35 (NCI-H460, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.494×** | -5.9 | 3e-07 | 19/34 (HS-578T, LOX-IMVI, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.512×** | -5.6 | 2e-06 | 15/30 (CFPAC-1, NCI-H23, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.529×** | -5.4 | 6e-06 | 18/34 (C32, A549, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.555×** | -5.0 | 5e-05 | 12/31 (J82, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.585×** | -4.5 | 4e-04 | 14/29 (CFPAC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.591×** | -4.2 | 0.002 | 12/28 (J82, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.640×** | -3.8 | 0.009 | 7/34 (KATO III, A549, …) | top dose only |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.643×** | -3.4 | 0.027 | 7/32 (SW 900, HS-578T, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.442×** | -3.3 | 0.039 | 2/29 (LOX-IMVI, A-172) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.680×** | -3.3 | 0.046 | 9/27 (HS-578T, A-172, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.681×** | -3.2 | 0.046 | 7/33 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.684×** | -3.2 | 0.048 | 10/35 (SW1417, A549, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **0.685×** | -3.2 | 0.048 | 5/28 (J82, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.704×** | -3.0 | 0.096 | 6/34 (RKO, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14206. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 7.10 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0658× (z -12.9) |
| [[J82 (line)]] | alt | 3.96 | 0 | 1 (1 ⚠) | — | [[Cytarabine (drug)]] 5 µM 0.0774× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 1.31 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0521× (z -8.5) |
| [[A-427 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.371 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.697 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.838 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.277 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.934 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.481 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.820 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.993 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.212 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.227 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.170 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.638 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.196 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.322 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14206), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 19 of them with an alert (⚠; 19 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUOX]] | +0.60 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[SEPTIN1]] | +0.57 | +0.37 / +0.60 | both halves | 7e-05 |  |
| [[SPATA1]] | +0.57 | +0.26 / +0.66 | both halves | 4e-04 |  |
| [[COPZ2]] | +0.55 | +0.30 / +0.63 | both halves | 2e-04 |  |
| [[LANCL1-AS1]] | +0.55 | +0.27 / +0.58 | both halves | 3e-04 |  |
| [[TRIM7]] | +0.54 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[C2CD5-AS1]] | +0.53 | +0.35 / +0.43 | both halves | 1e-04 |  |
| [[CNPY2-AS1]] | +0.53 | +0.26 / +0.61 | both halves | 3e-04 |  |
| [[HOXB-AS3]] | +0.53 | +0.22 / +0.61 | both halves | 6e-04 |  |
| [[COLEC11]] | +0.53 | +0.28 / +0.53 | both halves | 3e-04 |  |
| [[CD27-AS1]] | +0.53 | +0.28 / +0.58 | both halves | 3e-04 |  |
| [[IKZF4]] | +0.52 | +0.37 / +0.55 | both halves | 8e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INA]] | -0.45 | -0.37 / -0.40 | both halves | 7e-05 |  |
| [[ZNF770]] | -0.45 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[IPO9]] | -0.44 | -0.25 / -0.60 | both halves | 4e-04 |  |
| [[CIAO1]] | -0.43 | -0.24 / -0.46 | both halves | 5e-04 |  |
| [[NAMPTP1]] | -0.43 | -0.32 / -0.40 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBX1]] | B | TNFSF12 activity raises TBX1's level | lines that do not express TNFSF12 (12) vs lines expressing it (38) | 1.27× lower at baseline in the lines without TNFSF12 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with ARID1A |

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.493). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.9, 24.7); signed map (32.1, 0.9). **Vector** length 35.6, 4.63% of its response variance represented; |z| ≥ 3 in 682 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +13.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +6.5 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.1 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +0.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.0 | +2.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.9 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.4 | -7.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -4.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.0 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | TNF superfamily member 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,548,508-7,557,890 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TWEAK, DR3LG, APO3L, TNF12 |
| Gene groups (HGNC) | Tumor necrosis factor superfamily |
| Reactome | 3 pathways, smallest: TNF receptor superfamily (TNFSF) members mediating non-canonical NF-kB pathway; TNFR2 non-canonical NF-kB pathway; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [O43508](https://www.uniprot.org/uniprotkb/O43508) (Tumor necrosis factor ligand superfamily member 12):

> Binds to FN14 and possibly also to TNRFSF12/APO3. Weak inducer of apoptosis in some cell types. Mediates NF-kappa-B activation. Promotes angiogenesis and the proliferation of endothelial cells. Also involved in induction of inflammatory cytokines. Promotes IL8 secretion.

**Summary**, from NCBI Gene [8742](https://www.ncbi.nlm.nih.gov/gene/8742):

> The protein encoded by this gene is a cytokine that belongs to the tumor necrosis factor (TNF) ligand family. This protein is a ligand for the FN14/TWEAKR receptor. This cytokine has overlapping signaling functions with TNF, but displays a much wider tissue distribution. This cytokine, which exists in both membrane-bound and secreted forms, can induce apoptosis via multiple pathways of cell death in a cell type-specific manner. This cytokine is also found to promote proliferation and migration …

**Accessions** — [HGNC:11927](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11927) · Entrez [8742](https://www.ncbi.nlm.nih.gov/gene/8742) · UniProt [O43508](https://www.uniprot.org/uniprotkb/O43508) · Ensembl [ENSG00000239697](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000239697)

## Data

Gene col 14206: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14206); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14206, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14206]; `tensor/DDL_lfc|DDL_z.npy` [14206]; `embed/gene_vectors.npy` [14206]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14206 or target_col == 14206). Every well: [[TNFSF12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFSF12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
