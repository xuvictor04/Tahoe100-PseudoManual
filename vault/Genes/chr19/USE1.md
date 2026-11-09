---
symbol: "USE1"
type: "gene"
col: 594
ensembl_id: "ENSG00000053501"
name: "unconventional SNARE in the ER 1"
location: "19p13.11"
module: 38
arm: "+"
pooled_cpm: 11.26
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 27
n_dd_up_clean: 1
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# USE1

*unconventional SNARE in the ER 1* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.11× (z +4.2, q 0.012, up in 5 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.61× (z +4.1, q 0.013, up in 14 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 0.554× (z -7.1, q 6e-10, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAP30BP]] (+0.73, fdr 7e-06), [[LINC02804]] (+0.65, fdr 1e-05), [[PRKAG1]] (+0.64, fdr 9e-06); moves opposite to [[TMEM123]] (-0.61, fdr 1e-05), [[KDM1A]] (-0.61, fdr 1e-05), [[CIPC]] (-0.56, fdr 1e-05).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 594.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.2 | 0.012 | 5/48 (LoVo, SNU-423, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.61×** | +4.1 | 0.013 | 14/43 (NCI-H460, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 1.29× | +3.0 | 0.40 | 11/44 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 594.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **0.554×** | -7.1 | 6e-10 | 37/48 (SW1417, RKO, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.595×** | -6.3 | 9e-08 | 29/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.597×** | -6.2 | 9e-08 | 27/47 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.710×** | -5.8 | 7e-07 | 27/47 (SK-MEL-2, RPMI-7951, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.640×** | -5.4 | 8e-06 | 26/47 (PANC-1, H4, …) | all doses, flat | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.668×** | -4.9 | 1e-04 | 22/47 (HS-578T, RKO, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.693×** | -4.4 | 8e-04 | 19/47 (SNU-423, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.701×** | -4.3 | 0.001 | 14/48 (HOP62, AN3 CA, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.507×** | -4.3 | 0.001 | 19/48 (SNU-1, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.514×** | -4.2 | 0.002 | 19/48 (HS-578T, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.716×** | -4.0 | 0.003 | 18/44 (RPMI-7951, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.726×** | -3.9 | 0.005 | 19/45 (SW48, C-33 A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.800×** | -3.8 | 0.006 | 23/47 (RPMI-7951, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.734×** | -3.7 | 0.007 | 17/48 (BT-474, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Anethole trithione (drug)]] 5 µM |  | **0.810×** | -3.6 | 0.012 | 10/48 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.574×** | -3.5 | 0.014 | 11/44 (A-172, HS-578T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 594. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 13.4 | 0 | 2 | — | [[Bestatin (drug)]] 0.05 µM 0.0632× (z -10.1) |
| [[J82 (line)]] | alt | 12.2 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.166× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.240× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 8.54 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.107× (z -10.5) |
| [[BT-474 (line)]] | alt | 18.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.171× (z -9.4) |
| [[C32 (line)]] | wt | 10.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0986× (z -9.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[COLO 205 (line)]] | alt | 9.72 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0615× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0953× (z -10.1) ⚠ transcription drop; cell-cycle shift, explains ~83% of this change |
| [[HOP62 (line)]] | alt | 11.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.153× (z -9.5) |
| [[KATO III (line)]] | alt | 5.43 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0873× (z -9.9) ⚠ toxic |
| [[LoVo (line)]] | wt | 9.53 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 10.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.255× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 19.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -10.2) |
| [[SNU-1 (line)]] | wt | 14.0 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0961× (z -8.8) |
| [[SW48 (line)]] | wt | 10.4 | 0 | 1 (1 ⚠) | — | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.0703× (z -9.8) ⚠ toxic |
| [[A-172 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 594), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAP30BP]] | +0.73 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[LINC02804]] | +0.65 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[PRKAG1]] | +0.64 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[C11orf91]] | +0.63 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[GPATCH2L]] | +0.61 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[CDKL4]] | +0.61 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[PPIEL-1]] | +0.61 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ORAI2]] | +0.61 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[CPNE9]] | +0.61 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[ZNF432]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[HCLS1]] | +0.60 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[BLZF1]] | +0.60 | +0.52 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM123]] | -0.61 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[KDM1A]] | -0.61 | -0.52 / -0.70 | both halves | 1e-05 |  |
| [[CIPC]] | -0.56 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[LRIG3]] | -0.55 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[HSF2]] | -0.54 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[SORT1]] | -0.54 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[PGAM1]] | -0.54 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[STT3B]] | -0.54 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[RFXAP]] | -0.53 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[COPS7B]] | -0.53 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[KCTD3]] | -0.53 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[LBR]] | -0.53 | -0.49 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.624). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.4, -20.3); signed map (9.7, 13.3). **Vector** length 75.8, 14.1% of its response variance represented; |z| ≥ 3 in 781 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.7 | -3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +1.6 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.8 | +2.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.8 | +3.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.2 | -6.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.1 | -4.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -5.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.0 | -4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.7 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | unconventional SNARE in the ER 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:17,215,346-17,219,829 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p31, SLT1, MDS032, D12 |
| Gene groups (HGNC) | SNAREs |
| Reactome | 5 pathways, smallest: COPI-dependent Golgi-to-ER retrograde traffic; Golgi-to-ER retrograde transport; Intra-Golgi and retrograde Golgi-to-ER traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZ43](https://www.uniprot.org/uniprotkb/Q9NZ43) (Vesicle transport protein USE1):

> SNARE that may be involved in targeting and fusion of Golgi-derived retrograde transport vesicles with the ER.

**Summary**, from NCBI Gene [55850](https://www.ncbi.nlm.nih.gov/gene/55850):

> Predicted to enable SNAP receptor activity. Predicted to be involved in several processes, including lysosomal transport; protein catabolic process; and retrograde vesicle-mediated transport, Golgi to endoplasmic reticulum. Predicted to act upstream of or within endoplasmic reticulum tubular network organization and regulation of ER to Golgi vesicle-mediated transport. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30882](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30882) · Entrez [55850](https://www.ncbi.nlm.nih.gov/gene/55850) · UniProt [Q9NZ43](https://www.uniprot.org/uniprotkb/Q9NZ43) · Ensembl [ENSG00000053501](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000053501)

## Data

Gene col 594: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 594); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 594, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 594]; `tensor/DDL_lfc|DDL_z.npy` [594]; `embed/gene_vectors.npy` [594]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 594 or target_col == 594). Every well: [[USE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
