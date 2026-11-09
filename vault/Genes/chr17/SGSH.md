---
symbol: "SGSH"
type: "gene"
col: 11194
ensembl_id: "ENSG00000181523"
name: "N-sulfoglucosamine sulfohydrolase"
location: "17q25.3"
module: 138
arm: "+"
pooled_cpm: 5.59
n_lines_expressing: 48
n_dd_up: 7
n_dd_down: 3
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# SGSH

*N-sulfoglucosamine sulfohydrolase* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.46× (z +6.2, q 3e-07, up in 18 of 45 measured lines) ⚠ cell-cycle shift, explains ~57% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.69× (z +6.0, q 4e-07, up in 19 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.477× (z -4.4, q 0.005, down in 14 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPK12]] (+0.59, fdr 1e-05), [[TBKBP1]] (+0.59, fdr 2e-05), [[LPIN3]] (+0.59, fdr 3e-05); moves opposite to [[PIBF1]] (-0.52, fdr 3e-05), [[GPN3]] (-0.48, fdr 1e-04), [[COX8A]] (-0.46, fdr 6e-05).
> It is in [[Module 138]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SLC26A11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11194.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.46×** | +6.2 | 3e-07 | 18/45 (SW 900, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.69×** | +6.0 | 4e-07 | 19/45 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.49×** | +4.3 | 0.003 | 11/42 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.009 | 11/40 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +4.0 | 0.009 | 2/9 (PANC-1, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.030 | 12/43 (SK-MEL-2, H4, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.36×** | +3.5 | 0.036 | 9/43 (A-172, HS-578T, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11194.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.477×** | -4.4 | 0.005 | 14/36 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.712×** | -3.7 | 0.055 | 8/44 (SW 900, NCI-H2347, …) | top dose only | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.733×** | -3.5 | 0.073 | 12/43 (NCI-H23, C32, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.573× | -3.3 | 0.11 | 8/44 (HS-578T, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.749× | -3.3 | 0.11 | 12/45 (SNU-423, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.820× | -3.2 | 0.12 | 17/40 (C32, A549, …) | top dose only | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.756× | -3.2 | 0.12 | 9/44 (SNU-423, RKO, …) | rises with dose | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | 0.758× | -3.0 | 0.16 | 11/42 (hTERT-HPNE, LOX-IMVI, …) | top dose only | position effect removed |
| [[Allantoin (drug)]] 0.5 µM |  | 0.768× | -3.0 | 0.16 | 6/41 (SHP-77, SNU-1, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11194. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 4.87 | 0 | 2 (1 ⚠) | — | [[Radotinib (drug)]] 0.5 µM 0.0706× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 3.50 | 0 | 2 (1 ⚠) | — | [[Valdecoxib (drug)]] 0.5 µM 0.0806× (z -9.2) |
| [[SNU-423 (line)]] | alt | 15.4 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.134× (z -11.1) ⚠ cell-cycle shift, explains ~55% of this change |
| [[C32 (line)]] | wt | 8.70 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11194), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK12]] | +0.59 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[TBKBP1]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[LPIN3]] | +0.59 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[LZTR1]] | +0.58 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[MED16]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[CLCN7]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 | STRING 425 |
| [[EME2]] | +0.56 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[OPLAH]] ⚠ | +0.55 | +0.46 / +0.61 | both halves | 2e-05 | pathway: Diseases of metabolism; ⚠ in the vector space only through flagged drug-doses |
| [[AHSA2P]] | +0.55 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[PGGHG]] | +0.54 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[GBA1]] | +0.54 | +0.46 / +0.48 | both halves | 3e-05 | STRING 467 |
| [[SLC26A11]] | +0.54 | +0.56 / +0.52 | both halves | 1e-05 | pathway: Glycosaminoglycan metabolism; STRING 763; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[DUSP3]] | +0.54 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[ENGASE]] | +0.54 | +0.55 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIBF1]] | -0.52 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[GPN3]] | -0.48 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[COX8A]] | -0.46 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[WDPCP]] | -0.46 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[SLC1A1]] | -0.44 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[CMC2]] | -0.44 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[MZT1]] | -0.44 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[TXNDC17]] | -0.43 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[CALM1]] | -0.43 | -0.42 / -0.32 | both halves | 2e-04 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[PRADC1]] | -0.43 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[LGALS1]] | -0.43 | -0.36 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC26A11]] | B | SLC26A11 activity raises SGSH's level | lines that do not express SLC26A11 (5) vs lines expressing it (45) | 2.49× lower at baseline in the lines without SLC26A11 | 0.003 | ⚠ within organs, on part of the lines; also absent: DENND5B, SMAD4, MINAR1; maybe low, not absent |
| TUBB1, [[TUBB2A]], [[TUBB3]], TUBB4A, [[TUBB4B]] | B | TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B activity raises SGSH's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 lower it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets |
| [[PSMB5]] | B | PSMB5 activity lowers SGSH's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.490). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.4, -22.6); signed map (-8.9, -30.8). **Vector** length 62.0, 9.25% of its response variance represented; |z| ≥ 3 in 847 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +4.5 | +6.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.8 | +6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +3.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | +3.1 | +4.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | +2.8 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.6 | +1.5 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.2 | -3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.8 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -4.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.5 | -1.7 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.4 | -2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | N-sulfoglucosamine sulfohydrolase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:80,206,716-80,220,923 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSS, MPS3A, SFMD |
| Gene groups (HGNC) | Sulfatases |
| Reactome | 7 pathways, smallest: Mucopolysaccharidoses; HS-GAG degradation; Diseases of carbohydrate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P51688](https://www.uniprot.org/uniprotkb/P51688) (N-sulphoglucosamine sulphohydrolase):

> Catalyzes a step in lysosomal heparan sulfate degradation.

**Summary**, from NCBI Gene [6448](https://www.ncbi.nlm.nih.gov/gene/6448):

> This gene encodes the enzyme sulfamidase; one of several enzymes involved in the lysosomal degradation of heparan sulfate. Mutations in this gene are associated with the lysosomal storage disease mucopolysaccaridosis IIIA, also known as Sanfilippo syndrome A, which results from impaired degradation of heparan sulfate. Transcripts of varying sizes have been reported but their biological validity has not been determined. [provided by RefSeq, Jun 2017]

**Accessions** — [HGNC:10818](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10818) · Entrez [6448](https://www.ncbi.nlm.nih.gov/gene/6448) · UniProt [P51688](https://www.uniprot.org/uniprotkb/P51688) · Ensembl [ENSG00000181523](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181523)

## Data

Gene col 11194: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11194); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11194, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11194]; `tensor/DDL_lfc|DDL_z.npy` [11194]; `embed/gene_vectors.npy` [11194]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11194 or target_col == 11194). Every well: [[SGSH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SGSH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
