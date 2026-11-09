---
symbol: "ECSIT"
type: "gene"
col: 5026
ensembl_id: "ENSG00000130159"
name: "ECSIT signaling integrator"
location: "19p13.2"
module: 156
arm: "+"
pooled_cpm: 15.08
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/156"]
generated_by: "tahoemap"
---

# ECSIT

*ECSIT signaling integrator* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.81× (z +10.8, q 3e-24, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 0.747× (z -5.3, q 6e-05, down in 18 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METTL16]] (+0.75, fdr 7e-06), [[SETDB1]] (+0.73, fdr 7e-06), [[NMT1]] (+0.69, fdr 9e-06); moves opposite to [[DR1]] (-0.60, fdr 2e-05), [[EDEM1]] (-0.59, fdr 1e-05), [[EPB41L2]] (-0.58, fdr 1e-05).
> It is in [[Module 156]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5026.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.81×** | +10.8 | 3e-24 | 40/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.59×** | +8.4 | 1e-14 | 34/47 (LoVo, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.60×** | +8.0 | 2e-13 | 31/48 (PANC-1, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +6.7 | 4e-09 | 28/46 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +6.3 | 3e-08 | 21/47 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.42×** | +6.3 | 3e-08 | 25/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | 1.18× | +4.2 | 0.002 | 19/47 (RKO, MIA PaCa-2, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.61×** | +4.2 | 0.002 | 12/48 (COLO 205, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +3.9 | 0.007 | 15/42 (HT-29, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.022 | 11/46 (LoVo, SNU-423, …) | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.030 | 7/47 (SW 900, Hs 766T, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.21×** | +3.4 | 0.030 | 9/47 (NCI-H2347, BT-474, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.039 | 6/48 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.062 | 6/47 (COLO 205, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.062 | 1/48 (LoVo) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.065 | 6/44 (A549, NCI-H460, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5026.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **0.747×** | -5.3 | 6e-05 | 18/48 (SW1417, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.768×** | -4.8 | 4e-04 | 17/47 (SW480, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.770×** | -4.4 | 0.002 | 16/35 (SNU-423, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.774×** | -4.3 | 0.002 | 13/26 (NCI-H2030, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Furosemide (drug)]] 0.5 µM |  | **0.819×** | -3.7 | 0.029 | 9/47 (H4, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5026. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 24.8 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.266× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.299× (z -10.8) ⚠ cell-cycle shift, explains ~83% of this change |
| [[Panc 03.27 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -10.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 11.6 | 0 | 1 | — | [[Finasteride (drug)]] 0.05 µM 0.0738× (z -8.6) |
| [[A-172 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.69 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5026), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL16]] | +0.75 | +0.75 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[SETDB1]] | +0.73 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[NMT1]] | +0.69 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[UXT]] | +0.68 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[MAP2K7]] | +0.65 | +0.47 / +0.64 | both halves | 2e-05 | pathway: MyD88 cascade initiated on plasma membrane |
| [[TM9SF4]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[MAU2]] | +0.63 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[ALKBH1]] | +0.63 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[UBE2J2]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[IGBP1]] | +0.63 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[SMG5]] | +0.63 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[DHX57]] | +0.62 | +0.56 / +0.71 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DR1]] | -0.60 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[EDEM1]] | -0.59 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[EPB41L2]] | -0.58 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[CMTM6]] | -0.58 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[FAM199X]] | -0.57 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[CD164]] | -0.56 | -0.39 / -0.67 | both halves | 6e-05 |  |
| [[NAB1]] | -0.56 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[YWHAZ]] | -0.55 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[ZNF664]] | -0.54 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[ARL5B]] | -0.54 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[AKAP11]] | -0.52 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[SEPTIN11]] | -0.52 | -0.46 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ECSIT's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 156]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.765). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-42.7, -2.6); signed map (-6.4, -14.4). **Vector** length 66.1, 10.8% of its response variance represented; |z| ≥ 3 in 675 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +5.4 | +8.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.0 | +10.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +8.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.0 | +3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +2.7 | +6.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.7 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +0.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.6 | +3.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.6 | -1.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.0 | -4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.4 | -4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.4 | -0.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.3 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -0.8 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -1.1 | -1.3 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ECSIT signaling integrator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:11,505,929-11,529,172 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SITPEC |
| Gene groups (HGNC) | Mitochondrial complex I assembly complex |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 17 pathways, smallest: Complex I biogenesis; MyD88 cascade initiated on plasma membrane; Toll Like Receptor 10 (TLR10) Cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQ95](https://www.uniprot.org/uniprotkb/Q9BQ95) (Evolutionarily conserved signaling intermediate in Toll pathway, mitochondrial):

> Adapter protein that plays a role in different signaling pathways including TLRs and IL-1 pathways or innate antiviral induction signaling. Plays a role in the activation of NF-kappa-B by forming a signal complex with TRAF6 and TAK1/MAP3K7 to activate TAK1/MAP3K7 leading to activation of IKKs. Once ubiquitinated, interacts with the dissociated RELA and NFKB1 proteins and translocates to the nucleus where it induces NF-kappa-B-dependent gene expression. Plays a role in innate antiviral immune …

**Summary**, from NCBI Gene [51295](https://www.ncbi.nlm.nih.gov/gene/51295):

> Enables enzyme inhibitor activity and protein-macromolecule adaptor activity. Involved in mitochondrial respiratory chain complex I assembly and toll-like receptor 4 signaling pathway. Located in cytosol; mitochondrion; and nucleoplasm. Part of mitochondrial complex I intermediate assembly complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29548](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29548) · Entrez [51295](https://www.ncbi.nlm.nih.gov/gene/51295) · UniProt [Q9BQ95](https://www.uniprot.org/uniprotkb/Q9BQ95) · Ensembl [ENSG00000130159](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130159)

## Data

Gene col 5026: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5026); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5026, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5026]; `tensor/DDL_lfc|DDL_z.npy` [5026]; `embed/gene_vectors.npy` [5026]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5026 or target_col == 5026). Every well: [[ECSIT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ECSIT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
