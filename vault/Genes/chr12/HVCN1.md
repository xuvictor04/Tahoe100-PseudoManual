---
symbol: "HVCN1"
type: "gene"
col: 4393
ensembl_id: "ENSG00000122986"
name: "hydrogen voltage gated channel 1"
location: "12q24.11"
module: 53
arm: "+"
pooled_cpm: 2.03
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# HVCN1

*hydrogen voltage gated channel 1* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.62× (z +21.9, q 0e+00, up in 29 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Pyridoxine (hydrochloride) (drug)]] 5 µM: 0.712× (z -4.3, q 0.009, down in 6 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA2B]] (+0.76, fdr 7e-06), [[C2CD6]] (+0.73, fdr 7e-06), [[CATSPERD]] (+0.69, fdr 7e-06); moves opposite to [[POLD2]] (-0.57, fdr 5e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4393.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.62×** | +21.9 | 0e+00 | 29/29 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **5.15×** | +20.7 | 0e+00 | 26/32 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.85×** | +11.6 | 7e-29 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.88×** | +9.5 | 5e-19 | 3/8 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.79×** | +7.4 | 2e-11 | 7/42 (HOP62, J82, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.24×** | +7.2 | 6e-11 | 14/32 (C32, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +6.3 | 2e-08 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +5.7 | 9e-07 | 8/28 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.68×** | +4.6 | 2e-04 | 12/44 (PANC-1, J82, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +4.6 | 3e-04 | 3/20 (NCI-H2030, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +4.3 | 7e-04 | 15/43 (HepG2/C3A, HT-29, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.3 | 9e-04 | 6/44 (HEC-1-A, A498, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.59×** | +4.1 | 0.002 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +4.0 | 0.003 | 1/9 (Panc 03.27) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +3.8 | 0.005 | 4/31 (LOX-IMVI, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.47×** | +3.4 | 0.019 | 6/33 (NCI-H23, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.037 | 3/32 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.89×** | +3.0 | 0.073 | 1/11 (NCI-H2347) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.58×** | +2.9 | 0.091 | 0/15 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.38×** | +2.9 | 0.091 | 0/16 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4393.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.712×** | -4.3 | 0.009 | 6/46 (SHP-77, LOX-IMVI, …) | rises with dose | position effect removed |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.663×** | -3.5 | 0.097 | 4/23 (BT-474, C32, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Vortioxetine (drug)]] 0.5 µM |  | **0.680×** | -3.5 | 0.097 | 11/42 (SNU-423, HepG2/C3A, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | 0.683× | -3.2 | 0.21 | 5/40 (A-172, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4393. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 1.94 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +8.9) | — |
| [[A498 (line)]] | wt | 0.945 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.7× (z +9.4) | — |
| [[LoVo (line)]] | wt | 2.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.0× (z +11.7) | — |
| [[A-172 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.683 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.746 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.770 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.711 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.719 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.915 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.989 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.763 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4393), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA2B]] | +0.76 | +0.76 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[C2CD6]] | +0.73 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[CATSPERD]] | +0.69 | +0.73 / +0.66 | both halves | 7e-06 | pathway: Fertilization; STRING 420 |
| [[LINC02755]] | +0.69 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[GRIK5]] | +0.68 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[SLC4A10]] | +0.68 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[SEC1P]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[AQP4-AS1]] | +0.66 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[PEBP4]] | +0.65 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[PKD2L2]] | +0.65 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[FNDC7]] | +0.65 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[PPP1R36]] | +0.64 | +0.54 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLD2]] | -0.57 | -0.53 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HVCN1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LIMS2]] | B | LIMS2 activity raises HVCN1's level | lines that do not express LIMS2 (17) vs lines expressing it (33) | 1.42× lower at baseline in the lines without LIMS2 | 0.062 | ⚠ within organs, on part of the lines; also absent: PALM, FHL1, ZNF469 |
| [[DYSF]] | B | DYSF activity raises HVCN1's level | lines that do not express DYSF (11) vs lines expressing it (39) | 1.52× lower at baseline in the lines without DYSF | 0.075 | ⚠ within organs, on part of the lines; also absent: ISM2, IRX3, DNAAF9; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.732). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.7, -9.7); signed map (22.5, 10.9). **Vector** length 47.8, 6.24% of its response variance represented; |z| ≥ 3 in 1,028 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +21.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +20.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +4.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | +2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +1.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +2.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | +2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -1.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.2 | +0.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | hydrogen voltage gated channel 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:110,627,841-110,704,950 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC15619, Hv1, VSOP |
| Gene groups (HGNC) | Hydrogen voltage gated channels |
| Reactome | 6 pathways, smallest: Sperm Motility And Taxes; Fertilization; ROS and RNS production in phagocytes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96D96](https://www.uniprot.org/uniprotkb/Q96D96) (Voltage-gated hydrogen channel 1):

> Voltage-gated proton-selective channel that conducts outward proton currents in response to intracellular acidification. Lacks a canonical ion-channel pore domain and mediates proton permeability via its voltage sensor domain. Appears to play a dominant role in regulation of CO2/HCO3(-)/H(+) equilibrium in sperm flagellum. Prevents the acidification resulting from HCO3(-) synthesis and thus sustains high HCO3(-) levels inside sperm for capacitation. Provides for proton efflux that compensates …

**Summary**, from NCBI Gene [84329](https://www.ncbi.nlm.nih.gov/gene/84329):

> This gene encodes a voltage-gated protein channel protein expressed more highly in certain cells of the immune system. Phagocytic cells produce superoxide anions which require this channel protein, and in B cells this same process facilitates antibody production. This same channel protein, however, can also regulate functions in other cells including spermatozoa. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:28240](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28240) · Entrez [84329](https://www.ncbi.nlm.nih.gov/gene/84329) · UniProt [Q96D96](https://www.uniprot.org/uniprotkb/Q96D96) · Ensembl [ENSG00000122986](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122986)

## Data

Gene col 4393: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4393); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4393, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4393]; `tensor/DDL_lfc|DDL_z.npy` [4393]; `embed/gene_vectors.npy` [4393]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4393 or target_col == 4393). Every well: [[HVCN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HVCN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
