---
symbol: "A3GALT2"
type: "gene"
col: 11531
ensembl_id: "ENSG00000184389"
name: "alpha 1,3-galactosyltransferase 2"
location: "1p35.1"
module: 47
arm: "+"
pooled_cpm: 2.46
n_lines_expressing: 48
n_dd_up: 8
n_dd_down: 26
n_dd_up_clean: 7
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# A3GALT2

*alpha 1,3-galactosyltransferase 2* — 1p35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.01× (z +5.3, q 7e-05, up in 18 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.256× (z -10.3, q 5e-22, down in 29 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BMP8A]] (+0.79, fdr 7e-06), [[C13orf46]] (+0.75, fdr 7e-06), [[SMIM41]] (+0.74, fdr 7e-06).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HTR7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11531.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.01×** | +5.3 | 7e-05 | 18/43 (SW48, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +4.4 | 0.003 | 9/40 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +4.2 | 0.004 | 10/43 (SW480, BT-474, …) | rises with dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | **1.70×** | +4.0 | 0.008 | 6/32 (HS-578T, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.65×** | +3.8 | 0.016 | 8/44 (RKO, HepG2/C3A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +3.4 | 0.060 | 0/2 | inconsistent across doses | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.060 | 2/40 (C-33 A, SW480) | all doses, flat | position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM |  | **1.54×** | +3.3 | 0.076 | 2/36 (C32, RPMI-7951) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.50× | +3.0 | 0.15 | 10/42 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 2 with an alert ⚠; shown: the 15 strongest. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11531.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.256×** | -10.3 | 5e-22 | 29/43 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.354×** | -7.8 | 1e-12 | 26/38 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.395×** | -7.0 | 5e-10 | 27/41 (SW 900, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.418×** | -6.1 | 2e-07 | 17/41 (C32, HEC-1-A, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.480×** | -5.5 | 4e-06 | 24/41 (H4, RPMI-7951, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.551×** | -5.5 | 4e-06 | 18/38 (C32, A549, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.507×** | -5.4 | 4e-06 | 20/44 (HepG2/C3A, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.609×** | -5.3 | 9e-06 | 18/41 (HS-578T, RKO, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.512×** | -5.0 | 3e-05 | 15/36 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | **0.502×** | -5.0 | 3e-05 | 13/35 (LOX-IMVI, hTERT-HPNE, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.520×** | -4.9 | 4e-05 | 15/37 (A-172, COLO 205, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.575×** | -4.9 | 5e-05 | 18/40 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.524×** | -4.9 | 5e-05 | 19/43 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.519×** | -4.8 | 8e-05 | 19/32 (HOP62, H4, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.525×** | -4.7 | 1e-04 | 14/35 (NCI-H2030, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11531. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 16.2 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0534× (z -10.8) |
| [[SW480 (line)]] | alt | 2.16 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0644× (z -9.3) |
| [[HOP62 (line)]] | alt | 5.03 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0485× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 1.99 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0649× (z -8.7) |
| [[A-172 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.748 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.946 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.23 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.807 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.421 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11531), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMP8A]] | +0.79 | +0.69 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[C13orf46]] | +0.75 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[SMIM41]] | +0.74 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[BLZF2P]] | +0.73 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[SLC25A51]] | +0.70 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[PDE2A]] | +0.69 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[PARVG]] | +0.69 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[FES]] | +0.67 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[SPTBN5]] | +0.67 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[NTRK1]] | +0.67 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[SPATA32]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[NPAS1]] | +0.65 | +0.56 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HTR7]] | B | HTR7 activity raises A3GALT2's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 1.53× lower at baseline in the lines without HTR7 | 0.036 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[FLT1]] | B | FLT1 activity raises A3GALT2's level | lines that do not express FLT1 (28) vs lines expressing it (22) | 1.68× lower at baseline in the lines without FLT1 | 0.053 | ⚠ within organs, on part of the lines; also absent: ZNF365, COL19A1, PDGFRB |
| [[FES]] | B | FES activity raises A3GALT2's level | lines that do not express FES (11) vs lines expressing it (39) | 1.74× lower at baseline in the lines without FES | 0.078 | ⚠ within organs, on part of the lines; also absent: RBPMS, GLRX, SEMA4A; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers A3GALT2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers A3GALT2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.731). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.6, -15.3); signed map (15.9, 15.9). **Vector** length 77.6, 15.0% of its response variance represented; |z| ≥ 3 in 1,122 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +4.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +3.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.2 | +5.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +1.7 |
|  | [[Naproxen (drug)]] 0.05 µM |  | +1.5 | +2.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.0 | -5.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.4 | -2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.3 | -5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.2 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.2 | -6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.0 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | alpha 1,3-galactosyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.1 — chr1:33,306,766-33,321,098 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IGBS3S, IGB3S; previously A3GALT2P |
| Gene groups (HGNC) | Glycosyltransferase family 6 |
| Matched by | ensembl_id |

**Function**, from UniProt [U3KPV4](https://www.uniprot.org/uniprotkb/U3KPV4) (Alpha-1,3-galactosyltransferase 2):

> Synthesizes the galactose-alpha(1,3)-galactose group on the glycosphingolipid isoglobotrihexosylceramide or isogloboside 3 (iGb3) by catalyzing the transfer of galactose from UDP-Galactose to its acceptor molecule Gal-beta-1,4-Glc-ceramide. Can also catalyze the addition of galactose to iGb3 itself to form polygalactose structures.

**Summary**, from NCBI Gene [127550](https://www.ncbi.nlm.nih.gov/gene/127550):

> Predicted to enable N-acetyllactosaminide 3-alpha-galactosyltransferase activity and alpha-1,3-galactosyltransferase activity. Predicted to be involved in glycosphingolipid biosynthetic process. Predicted to be located in Golgi cisterna membrane. Predicted to be active in Golgi apparatus and vesicle. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30005](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30005) · Entrez [127550](https://www.ncbi.nlm.nih.gov/gene/127550) · UniProt [U3KPV4](https://www.uniprot.org/uniprotkb/U3KPV4) · Ensembl [ENSG00000184389](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184389)

## Data

Gene col 11531: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11531); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11531, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11531]; `tensor/DDL_lfc|DDL_z.npy` [11531]; `embed/gene_vectors.npy` [11531]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11531 or target_col == 11531). Every well: [[A3GALT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/A3GALT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
