---
symbol: "ASIC4"
type: "gene"
col: 1010
ensembl_id: "ENSG00000072182"
name: "acid sensing ion channel subunit family member 4"
location: "2q35"
module: 38
arm: "+"
pooled_cpm: 3.43
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 16
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# ASIC4

*acid sensing ion channel subunit family member 4* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.10× (z +7.2, q 4e-10, up in 22 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.306× (z -8.1, q 3e-13, down in 29 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL20A1]] (+0.88, fdr 7e-06), [[VWCE]] (+0.74, fdr 7e-06), [[HPX]] (+0.72, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SSPOP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1010.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +7.2 | 4e-10 | 22/33 (PANC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +4.3 | 0.003 | 0/3 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.88×** | +4.3 | 0.003 | 16/41 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.79×** | +4.0 | 0.011 | 16/42 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +3.6 | 0.036 | 9/45 (NCI-H23, NCI-H1573, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.64×** | +3.4 | 0.066 | 10/41 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Lactate (calcium) (drug)]] 5 µM |  | **1.61×** | +3.2 | 0.097 | 4/41 (HepG2/C3A, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.62× | +3.1 | 0.16 | 0/6 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1010.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.306×** | -8.1 | 3e-13 | 29/44 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.360×** | -6.7 | 4e-09 | 24/40 (NCI-H23, SW480, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.380×** | -6.6 | 6e-09 | 19/24 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.523×** | -6.3 | 5e-08 | 27/42 (hTERT-HPNE, C32, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.412×** | -6.1 | 1e-07 | 24/41 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.539×** | -6.0 | 2e-07 | 23/33 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.419×** | -6.0 | 2e-07 | 22/41 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.447×** | -5.5 | 2e-06 | 22/40 (SNU-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.456×** | -5.4 | 5e-06 | 22/42 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.323×** | -4.0 | 0.003 | 15/40 (CFPAC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.582×** | -3.7 | 0.010 | 19/39 (HT-29, SW 900, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.578×** | -3.6 | 0.014 | 13/24 (NCI-H23, NCI-H1573, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.617×** | -3.3 | 0.039 | 13/40 (A-172, SW 900, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.621×** | -3.3 | 0.043 | 14/43 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.723×** | -3.2 | 0.061 | 11/44 (RPMI-7951, NCI-H23, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.623×** | -3.1 | 0.076 | 9/37 (HT-29, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.79 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1010. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.33 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0795× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 15.0 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0640× (z -12.7) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A-172 (line)]] | wt | 6.32 | 0 | 2 (1 ⚠) | — | [[Mozavaptan (drug)]] 0.5 µM 0.0528× (z -10.6) |
| [[A549 (line)]] | wt | 3.47 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0339× (z -9.9) ⚠ cell-cycle shift, explains ~40% of this change |
| [[MIA PaCa-2 (line)]] | alt | 7.64 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0860× (z -9.0) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A-427 (line)]] | wt | 5.34 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0521× (z -10.1) |
| [[HOP62 (line)]] | alt | 3.18 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0414× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 3.25 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0450× (z -9.0) |
| [[A498 (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.877 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.407 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.663 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.995 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1010), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL20A1]] | +0.88 | +0.81 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[VWCE]] | +0.74 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[HPX]] | +0.72 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[RFPL3S]] | +0.71 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[TINCR]] | +0.70 | +0.62 / +0.76 | both halves | 7e-06 |  |
| [[ATP2A1]] | +0.68 | +0.60 / +0.70 | both halves | 7e-06 | pathway: Ion channel transport |
| [[MYO15A]] | +0.68 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[GOSR2]] | +0.67 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[GAL3ST1]] | +0.67 | +0.62 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[PYGM]] | +0.67 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[SMIM41]] | +0.67 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[ISY1-RAB43]] | +0.67 | +0.63 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SSPOP]] | B | SSPOP activity raises ASIC4's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 1.68× lower at baseline in the lines without SSPOP | 0.039 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2 |
| [[SSC5D]] | B | SSC5D activity raises ASIC4's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 1.64× lower at baseline in the lines without SSC5D | 0.085 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.741). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.8, -19.1); signed map (14.0, 12.5). **Vector** length 72.4, 12.6% of its response variance represented; |z| ≥ 3 in 1,180 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +2.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.4 | +3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +0.9 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.5 | +2.3 |
|  | [[Pyridoxine (drug)]] 0.5 µM |  | +1.5 | +2.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -3.7 | -6.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.3 | -6.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -6.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -5.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -2.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.3 | -2.5 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.1 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | acid sensing ion channel subunit family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:219,514,170-219,538,772 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BNAC4; previously ACCN4 |
| Gene groups (HGNC) | Acid sensing ion channel subunits |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FT7](https://www.uniprot.org/uniprotkb/Q96FT7) (Acid-sensing ion channel 4):

> Does not exhibit measurable stand-alone pH-gated sodium channel activity but may form pH-gated heterotrimeric sodium channels. Its activity could also depend on alternative gating mechanisms.

**Summary**, from NCBI Gene [55515](https://www.ncbi.nlm.nih.gov/gene/55515):

> This gene belongs to the superfamily of acid-sensing ion channels, which are proton-gated, amiloride-sensitive sodium channels. These channels have been implicated in synaptic transmission, pain perception as well as mechanoperception. This gene is predominantly expressed in the pituitary gland, and was considered a candidate for paroxysmal dystonic choreoathetosis (PDC), a movement disorder, however, no correlation was found between mutations in this gene and PDC. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:21263](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21263) · Entrez [55515](https://www.ncbi.nlm.nih.gov/gene/55515) · UniProt [Q96FT7](https://www.uniprot.org/uniprotkb/Q96FT7) · Ensembl [ENSG00000072182](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072182)

## Data

Gene col 1010: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1010); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1010, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1010]; `tensor/DDL_lfc|DDL_z.npy` [1010]; `embed/gene_vectors.npy` [1010]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1010 or target_col == 1010). Every well: [[ASIC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASIC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
