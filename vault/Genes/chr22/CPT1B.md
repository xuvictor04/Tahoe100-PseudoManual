---
symbol: "CPT1B"
type: "gene"
col: 12990
ensembl_id: "ENSG00000205560"
name: "carnitine palmitoyltransferase 1B"
location: "22q13.33"
module: 12
arm: "+"
pooled_cpm: 4.99
n_lines_expressing: 47
n_dd_up: 2
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# CPT1B

*carnitine palmitoyltransferase 1B* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.35× (z +4.8, q 0.001, up in 15 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.517× (z -7.2, q 3e-10, down in 24 of 42 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.610× (z -5.4, q 1e-05, down in 20 of 41 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHKB]] (+0.76, fdr 7e-06, ⚠ same locus), [[AGER]] (+0.67, fdr 7e-06), [[HNRNPH1]] (+0.66, fdr 1e-05), [[CDK3]] (+0.64, fdr 1e-05); moves opposite to [[PHB1]] (-0.57, fdr 5e-05), [[ARPC5]] (-0.57, fdr 1e-05), [[LDHB]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 3 go from it, the strongest it → [[LSM14B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12990.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +4.8 | 0.001 | 15/34 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +4.5 | 0.002 | 11/34 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 1.33× | +3.2 | 0.16 | 3/43 (LS 180, SW480, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 1.35× | +3.2 | 0.16 | 4/40 (LoVo, HepG2/C3A, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.33× | +3.2 | 0.16 | 12/36 (CFPAC-1, A-427, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12990.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.517×** | -7.2 | 3e-10 | 24/42 (RPMI-7951, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.577×** | -6.0 | 5e-07 | 23/44 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.610×** | -5.4 | 1e-05 | 20/41 (AsPC-1, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.635×** | -5.0 | 9e-05 | 20/44 (NCI-H23, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.462×** | -4.4 | 0.001 | 13/38 (A498, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.683×** | -4.2 | 0.003 | 16/42 (AsPC-1, PANC-1, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.903× | -4.0 | 0.006 | 7/45 (SW480, HCT15, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.550×** | -3.4 | 0.043 | 11/36 (BT-474, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.724×** | -3.3 | 0.056 | 13/39 (J82, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.745×** | -3.2 | 0.076 | 17/43 (RPMI-7951, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~16% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12990. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.95 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.255× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 5.30 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0853× (z -9.3) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A-427 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12990), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHKB]] | +0.76 | +0.75 / +0.72 | both halves | 7e-06 | STRING 960; ⚠ same locus (0.5 kb, same strand: neighbours can correlate without regulation) |
| [[AGER]] | +0.67 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[HNRNPH1]] | +0.66 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[CDK3]] | +0.64 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[GORASP1]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[CIRBP]] | +0.60 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[GIGYF1]] | +0.59 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[ZNF213]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[KMT2B]] | +0.58 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[ZCCHC3]] | +0.57 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[PPP1R3F]] | +0.57 | +0.63 / +0.35 | both halves | 1e-04 |  |
| [[CHMP4A]] | +0.57 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[PQBP1]] | +0.56 | +0.56 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHB1]] | -0.57 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[ARPC5]] | -0.57 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[LDHB]] | -0.56 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[BANF1]] | -0.55 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[EMC4]] | -0.54 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[EIF3H]] | -0.53 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[TMED7]] | -0.53 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[PRDX1]] | -0.52 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[ATP5MC3]] ⚠ | -0.52 | -0.50 / -0.38 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[GRB2]] | -0.51 | -0.52 / -0.30 | both halves | 2e-04 |  |
| [[FABP5]] | -0.51 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[BRK1]] | -0.51 | -0.54 / -0.30 | both halves | 2e-04 |  |
| [[GLO1]] | -0.50 | -0.41 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises CPT1B's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises CPT1B's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LSM14B]] | C | CPT1B activity lowers LSM14B's level | lines that do not express CPT1B (3) vs lines expressing it (47) | 1.51× higher at baseline in the lines without CPT1B | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLEC2D, FRRS1, ENSG00000266385; maybe low, not absent; its own permutation p |
| [[ZNF213]] | C | CPT1B activity lowers ZNF213's level | lines that do not express CPT1B (3) vs lines expressing it (47) | 1.40× higher at baseline in the lines without CPT1B | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLEC2D, FRRS1, ENSG00000266385; maybe low, not absent; its own permutation p |
| [[CHKB]] | C | CPT1B activity raises CHKB's level | lines that do not express CPT1B (3) vs lines expressing it (47) | 1.73× lower at baseline in the lines without CPT1B | 0.066 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLEC2D, FRRS1, ENSG00000266385; maybe low, not absent |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.331). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (24.0, -9.7); signed map (3.4, -9.9). **Vector** length 51.7, 6.76% of its response variance represented; |z| ≥ 3 in 824 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.2 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +3.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +1.7 | +1.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +1.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.0 | -5.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -1.7 | -6.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -1.6 | -7.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.6 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.5 | -3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -3.4 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -1.1 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | carnitine palmitoyltransferase 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:50,568,861-50,578,465 (-) |
| Ensembl biotype | protein_coding |
| Also known as | M-CPT1, CPT1-M |
| Gene groups (HGNC) | Carnitine palmitoyltransferase family |
| Reactome | 3 pathways, smallest: Carnitine shuttle; Fatty acid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92523](https://www.uniprot.org/uniprotkb/Q92523) (Carnitine O-palmitoyltransferase 1, muscle isoform):

> Catalyzes the transfer of the acyl group of long-chain fatty acid-CoA conjugates onto carnitine, an essential step for the mitochondrial uptake of long-chain fatty acids and their subsequent beta-oxidation in the mitochondrion.

**Summary**, from NCBI Gene [1375](https://www.ncbi.nlm.nih.gov/gene/1375):

> The protein encoded by this gene, a member of the carnitine/choline acetyltransferase family, is the rate-controlling enzyme of the long-chain fatty acid beta-oxidation pathway in muscle mitochondria. This enzyme is required for the net transport of long-chain fatty acyl-CoAs from the cytoplasm into the mitochondria. Multiple transcript variants encoding different isoforms have been found for this gene, and read-through transcripts are expressed from the upstream locus that include exons from …

**Accessions** — [HGNC:2329](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2329) · Entrez [1375](https://www.ncbi.nlm.nih.gov/gene/1375) · UniProt [Q92523](https://www.uniprot.org/uniprotkb/Q92523) · Ensembl [ENSG00000205560](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205560)

## Data

Gene col 12990: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12990); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12990, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12990]; `tensor/DDL_lfc|DDL_z.npy` [12990]; `embed/gene_vectors.npy` [12990]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12990 or target_col == 12990). Every well: [[CPT1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPT1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
