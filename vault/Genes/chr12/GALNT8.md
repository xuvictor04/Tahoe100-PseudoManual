---
symbol: "GALNT8"
type: "gene"
col: 5018
ensembl_id: "ENSG00000130035"
name: "polypeptide N-acetylgalactosaminyltransferase 8"
location: "12p13.32"
module: 47
arm: "+"
pooled_cpm: 2.22
n_lines_expressing: 44
n_dd_up: 30
n_dd_down: 4
n_dd_up_clean: 21
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# GALNT8

*polypeptide N-acetylgalactosaminyltransferase 8* — 12p13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.91× (z +15.4, q 0e+00, up in 15 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.602× (z -5.2, q 1e-04, down in 15 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAH2]] (+0.66, fdr 9e-06), [[EPHA1-AS1]] (+0.66, fdr 7e-06), [[CACNA1E]] (+0.63, fdr 7e-06); moves opposite to [[ACSF2]] (-0.49, fdr 4e-04), [[KLHL7]] (-0.49, fdr 1e-04).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[TBX15]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5018.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.91×** | +15.4 | 0e+00 | 15/25 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.89×** | +15.3 | 0e+00 | 13/26 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.96×** | +13.5 | 3e-39 | 1/2 (SW48) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.72×** | +10.2 | 3e-22 | 1/6 (SW48) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.57×** | +9.6 | 8e-20 | 15/27 (SW480, A-427, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.21×** | +7.5 | 8e-12 | 1/4 (HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +6.5 | 8e-09 | 8/22 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +6.3 | 2e-08 | 10/32 (NCI-H1573, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +5.2 | 1e-05 | 12/37 (NCI-H2030, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +4.7 | 2e-04 | 1/8 (NCI-H460) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.34×** | +4.5 | 3e-04 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +4.3 | 8e-04 | 8/30 (A-427, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +4.1 | 0.002 | 1/8 (NCI-H460) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +3.6 | 0.015 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Naproxen (drug)]] 0.05 µM |  | **1.46×** | +3.5 | 0.015 | 2/12 (HS-578T, HT-29) | inconsistent across doses |  |
| [[Isocorydine (drug)]] 0.05 µM |  | **1.40×** | +3.4 | 0.022 | 1/33 (SHP-77) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.028 | 1/16 (J82) | inconsistent across doses |  |
| [[Rosiglitazone (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.028 | 0/16 | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.042 | 3/33 (AsPC-1, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.042 | 5/29 (LoVo, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.043 | 0/10 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +3.1 | 0.045 | 4/29 (NCI-H460, A498, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5018.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.602×** | -5.2 | 1e-04 | 15/32 (NCI-H23, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.609×** | -5.1 | 1e-04 | 11/27 (SW48, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.614×** | -5.0 | 1e-04 | 13/38 (SW48, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.696×** | -3.6 | 0.048 | 3/36 (H4, C-33 A, …) | top dose only | plate-row cell shift |
| [[Radotinib (drug)]] 5 µM |  | 0.802× | -3.2 | 0.15 | 6/31 (LoVo, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.738× | -3.1 | 0.17 | 6/22 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Ranolazine (drug)]] 0.5 µM |  | 0.746× | -3.0 | 0.19 | 6/34 (SNU-423, NCI-H2030, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 0.05 µM |  | 0.729× | -3.0 | 0.19 | 6/18 (SK-MEL-2, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5018. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 31.6 | 0 | 2 (1 ⚠) | — | [[TAK-901 (drug)]] 0.05 µM 0.0326× (z -11.7) |
| [[SK-MEL-2 (line)]] | alt | 8.72 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0741× (z -11.3) |
| [[A-172 (line)]] | wt | 0.978 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.993 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.629 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.988 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.745 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.808 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.677 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.733 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.889 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.761 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.752 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.527 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.764 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.387 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.476 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.735 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.683 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5018), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAH2]] | +0.66 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[EPHA1-AS1]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[CACNA1E]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[MTNR1A]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[FBXW10B]] | +0.62 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[SH2D4B]] | +0.62 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ADAP1]] | +0.61 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[SLC8A2]] | +0.61 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[LINC01250]] | +0.59 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[MMP25]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[NEMP2-DT]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[ITGA9]] | +0.58 | +0.62 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACSF2]] | -0.49 | -0.47 / -0.26 | both halves | 4e-04 |  |
| [[KLHL7]] | -0.49 | -0.53 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBX15]] | B | GALNT8 activity lowers TBX15's level | lines that do not express GALNT8 (6) vs lines expressing it (44) | 2.12× higher at baseline in the lines without GALNT8 | 0.054 | ⚠ within organs, on part of the lines; also absent: PRDM6, NOS1, C1orf21; maybe low, not absent |
| [[ICAM2]] | B | GALNT8 activity lowers ICAM2's level | lines that do not express GALNT8 (6) vs lines expressing it (44) | 2.67× higher at baseline in the lines without GALNT8 | 0.081 | ⚠ within organs, on part of the lines; also absent: PRDM6, NOS1, C1orf21; maybe low, not absent |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.564). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.7, -13.6); signed map (21.5, 14.1). **Vector** length 37.4, 4.45% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +15.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +13.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +10.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.3 | +2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.9 | +0.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.4 | -5.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.3 | -5.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.2 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | polypeptide N-acetylgalactosaminyltransferase 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.32 — chr12:4,720,400-4,851,927 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GALNAC-T8 |
| Gene groups (HGNC) | Polypeptide N-acetylgalactosaminyltransferases |
| Reactome | 2 pathways, smallest: O-linked glycosylation of mucins; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NY28](https://www.uniprot.org/uniprotkb/Q9NY28) (Probable polypeptide N-acetylgalactosaminyltransferase 8):

> Probably catalyzes the initial reaction in O-linked oligosaccharide biosynthesis, the transfer of an N-acetyl-D-galactosamine residue to a serine or threonine residue on the protein receptor.

**Summary**, from NCBI Gene [26290](https://www.ncbi.nlm.nih.gov/gene/26290):

> This gene encodes a member of the UDP-N-acetyl-alpha-D-galactosamine:polypeptide N-acetylgalactosaminyltransferase (GalNAc-T) family of enzymes. GalNAc-Ts initiate mucin-type O-linked glycosylation in the Golgi apparatus by catalyzing the transfer of GalNAc to serine and threonine residues on target proteins. They are characterized by an N-terminal transmembrane domain, a stem region, a lumenal catalytic domain containing a GT1 motif and Gal/GalNAc transferase motif, and a C-terminal …

**Accessions** — [HGNC:4130](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4130) · Entrez [26290](https://www.ncbi.nlm.nih.gov/gene/26290) · UniProt [Q9NY28](https://www.uniprot.org/uniprotkb/Q9NY28) · Ensembl [ENSG00000130035](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130035)

## Data

Gene col 5018: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5018); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5018, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5018]; `tensor/DDL_lfc|DDL_z.npy` [5018]; `embed/gene_vectors.npy` [5018]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5018 or target_col == 5018). Every well: [[GALNT8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALNT8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
