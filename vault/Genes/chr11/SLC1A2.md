---
symbol: "SLC1A2"
type: "gene"
col: 3140
ensembl_id: "ENSG00000110436"
name: "solute carrier family 1 member 2"
location: "11p13"
module: 61
arm: "+"
pooled_cpm: 2.03
n_lines_expressing: 37
n_dd_up: 37
n_dd_down: 1
n_dd_up_clean: 27
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# SLC1A2

*solute carrier family 1 member 2* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.63× (z +16.4, q 0e+00, up in 9 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Norepinephrine (hydrochloride) (drug)]] 0.5 µM: 0.531× (z -4.3, q 0.011, down in 3 of 19 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.152×; ⚠ toxic); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0485×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGCZ]] (+0.64, fdr 1e-05), [[PKNOX2]] (+0.62, fdr 1e-05), [[OPCML]] (+0.61, fdr 1e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[STXBP5L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3140.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.63×** | +16.4 | 0e+00 | 9/11 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.37×** | +11.5 | 3e-28 | 17/22 (HepG2/C3A, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.23×** | +10.7 | 3e-24 | 1/2 (hTERT-HPNE) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.94×** | +9.2 | 6e-18 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.35×** | +8.1 | 7e-14 | 6/16 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.00×** | +7.7 | 1e-12 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.04×** | +6.8 | 1e-09 | 4/23 (HepG2/C3A, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.67×** | +6.6 | 3e-09 | 9/18 (HepG2/C3A, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.39×** | +5.8 | 4e-07 | 11/25 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.73×** | +5.2 | 1e-05 | 2/24 (PANC-1, hTERT-HPNE) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.13×** | +5.1 | 2e-05 | 7/14 (HepG2/C3A, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +4.1 | 0.002 | 1/4 (PANC-1) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +4.1 | 0.002 | 0/6 | top dose only | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.81×** | +3.9 | 0.003 | 1/12 (NCI-H460) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.78×** | +3.8 | 0.005 | 3/14 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +3.6 | 0.010 | 4/13 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.72×** | +3.6 | 0.010 | 7/21 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.71×** | +3.6 | 0.012 | 1/6 (PANC-1) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +3.5 | 0.013 | 7/24 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3140.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.152×; ⚠ toxic); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0485×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Norepinephrine (hydrochloride) (drug)]] 0.5 µM |  | **0.531×** | -4.3 | 0.011 | 3/19 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3140. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 95.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.152× (z -9.0) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 23.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0485× (z -8.7) |
| [[A-172 (line)]] | wt | 0.741 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.365 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.500 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.656 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.655 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.498 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.644 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.675 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.697 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.607 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.602 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.558 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.630 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.388 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.675 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.615 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.625 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.706 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.653 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.657 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.607 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.598 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.607 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.538 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.558 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.546 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.379 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.612 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.863 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.563 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.794 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.855 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.803 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.673 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3140), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGCZ]] | +0.64 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[PKNOX2]] | +0.62 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[OPCML]] | +0.61 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[LINC00298]] | +0.60 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[DACH2]] | +0.60 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[SORCS1]] | +0.59 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[DCC]] | +0.59 | +0.43 / +0.68 | both halves | 3e-05 |  |
| [[PLD5]] | +0.58 | +0.46 / +0.67 | both halves | 2e-05 |  |
| [[SEMA6D]] | +0.58 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[CCDC170]] | +0.58 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[RETREG1-AS1]] | +0.57 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[SFRP4]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STXBP5L]] | B | STXBP5L activity raises SLC1A2's level | lines that do not express STXBP5L (35) vs lines expressing it (15) | 1.09× lower at baseline in the lines without STXBP5L | 0.026 | ⚠ within organs, on part of the lines; also absent: PCSK1, ENSG00000287211, GABRG2; maybe low, not absent |
| [[SLC24A3]] | B | SLC24A3 activity raises SLC1A2's level | lines that do not express SLC24A3 (37) vs lines expressing it (13) | 1.14× lower at baseline in the lines without SLC24A3 | 0.060 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SLC1A2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.617). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.9, 31.8); signed map (31.9, 19.1). **Vector** length 25.1, 3.46% of its response variance represented; |z| ≥ 3 in 557 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +11.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +16.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.8 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +9.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +6.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.8 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.8 | +3.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.8 | +3.5 |
| fall | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.9 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -2.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.7 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -1.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 1 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:35,251,205-35,420,063 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GLT-1, GLT1, EAAT2, HBGT |
| Gene groups (HGNC) | Solute carrier family 1 |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Reactome | 9 pathways, smallest: Astrocytic Glutamate-Glutamine Uptake And Metabolism; Neurotransmitter uptake and metabolism In glial cells; Glutamate Neurotransmitter Release Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P43004](https://www.uniprot.org/uniprotkb/P43004) (Excitatory amino acid transporter 2):

> Sodium-dependent, high-affinity amino acid transporter that mediates the uptake of L-glutamate and also L-aspartate and D-aspartate. Functions as a symporter that transports one amino acid molecule together with two or three Na(+) ions and one proton, in parallel with the counter-transport of one K(+) ion. Mediates Cl(-) flux that is not coupled to amino acid transport; this avoids the accumulation of negative charges due to aspartate and Na(+) symport. Essential for the rapid removal of …

**Summary**, from NCBI Gene [6506](https://www.ncbi.nlm.nih.gov/gene/6506):

> This gene encodes a member of a family of solute transporter proteins. The membrane-bound protein is the principal transporter that clears the excitatory neurotransmitter glutamate from the extracellular space at synapses in the central nervous system. Glutamate clearance is necessary for proper synaptic activation and to prevent neuronal damage from excessive activation of glutamate receptors. Improper regulation of this gene is thought to be associated with several neurological disorders. …

**Accessions** — [HGNC:10940](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10940) · Entrez [6506](https://www.ncbi.nlm.nih.gov/gene/6506) · UniProt [P43004](https://www.uniprot.org/uniprotkb/P43004) · Ensembl [ENSG00000110436](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110436)

## Data

Gene col 3140: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3140); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3140, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3140]; `tensor/DDL_lfc|DDL_z.npy` [3140]; `embed/gene_vectors.npy` [3140]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3140 or target_col == 3140). Every well: [[SLC1A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC1A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
