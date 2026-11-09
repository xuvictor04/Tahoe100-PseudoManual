---
symbol: "COL20A1"
type: "gene"
col: 2095
ensembl_id: "ENSG00000101203"
name: "collagen type XX alpha 1 chain"
location: "20q13.33"
module: 38
arm: "+"
pooled_cpm: 3.74
n_lines_expressing: 48
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/038", "written"]
generated_by: "tahoemap"
---

# COL20A1

*collagen type XX alpha 1 chain* — 20q13.33

> [!summary] In one line
> COL20A1 encodes collagen XX, a barely characterised FACIT-family collagen known almost entirely from chick embryonic tissue.

## What it is

Collagen α1(XX) was cloned from chick cornea and assigned to the FACIT subfamily — fibril-associated collagens with interrupted triple helices. Interrupted collagenous stretches sit alongside fibronectin type III repeats and a von Willebrand factor A domain, the layout of a protein that decorates fibrils rather than forming them. In chick it was found in cornea, cartilage and tendon; the human gene lies at 20q13.33, expressed at low level and biased toward brain and testis. After that the record thins fast: no knockout phenotype, no validated partner, no demonstrated activity — the database annotations are inferred from domain content, and no gene-disease association is established.

## What is uncertain

Almost everything. The transcript sits low enough that ambient RNA is a live explanation, and the repetitive Gly-X-Y sequence shared across the collagen family is where multi-mapping reads land imprecisely. With no established function there is no mechanism to check a correlation against, and nothing here separates one from a few-line effect or from depth and ambient-RNA covariates. A lead for a targeted assay, not a finding.

## References

- Koch et al., 2001, Journal of Biological Chemistry — cloned α1(XX) collagen from chick cornea and assigned it to the FACIT subfamily.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.94× (z +12.6, q 9e-34, up in 36 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.387× (z -5.3, q 6e-05, down in 22 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASIC4]] (+0.88, fdr 7e-06), [[VWCE]] (+0.86, fdr 7e-06), [[RFPL3S]] (+0.80, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2095.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.94×** | +12.6 | 9e-34 | 36/36 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **3.21×** | +6.5 | 2e-08 | 27/43 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.05×** | +6.0 | 4e-07 | 23/33 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.36×** | +4.8 | 2e-04 | 23/42 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.39×** | +4.7 | 3e-04 | 18/36 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.20×** | +4.4 | 0.001 | 19/41 (HEC-1-A, SW480, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.13×** | +4.2 | 0.002 | 18/43 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.00×** | +3.9 | 0.008 | 16/43 (C-33 A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +3.6 | 0.021 | 0/3 | inconsistent across doses | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +3.6 | 0.021 | 12/34 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.55×** | +3.4 | 0.028 | 8/43 (SNU-1, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.85×** | +3.4 | 0.028 | 12/41 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +3.4 | 0.028 | 12/36 (NCI-H23, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +3.3 | 0.042 | 12/43 (A-172, PANC-1, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.87×** | +3.2 | 0.047 | 1/5 (HOP62) | inconsistent across doses | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +3.1 | 0.069 | 10/42 (MIA PaCa-2, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2095.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.387×** | -5.3 | 6e-05 | 22/43 (H4, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.520×** | -5.2 | 6e-05 | 24/43 (NCI-H2030, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.403×** | -4.9 | 2e-04 | 21/41 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.495×** | -3.9 | 0.011 | 19/44 (H4, NCI-H1573, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.509×** | -3.8 | 0.016 | 18/42 (H4, A549, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.512×** | -3.8 | 0.016 | 18/30 (H4, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.507×** | -3.6 | 0.025 | 13/39 (NCI-H23, C32, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.52 per unit of S-phase module lfc, -0.81 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2095. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 19.2 | 0 | 7 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0223× (z -12.1) |
| [[A498 (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0246× (z -12.4) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW480 (line)]] | alt | 3.94 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0679× (z -10.3) |
| [[A-172 (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.774 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.576 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2095), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASIC4]] | +0.88 | +0.81 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[VWCE]] | +0.86 | +0.87 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[RFPL3S]] | +0.80 | +0.79 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[HPX]] | +0.78 | +0.77 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[SMIM41]] | +0.77 | +0.74 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[SLC9A5]] | +0.74 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[PYGM]] | +0.74 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[GABRR2]] | +0.73 | +0.75 / +0.73 | both halves | 7e-06 |  |
| [[ISY1-RAB43]] | +0.73 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[GOLGA3]] | +0.72 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[ADCY10P1]] | +0.72 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[ATP2A1]] | +0.72 | +0.71 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers COL20A1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KCNQ1OT1]] | B | KCNQ1OT1 activity lowers COL20A1's level | lines that do not express KCNQ1OT1 (6) vs lines expressing it (44) | 1.47× higher at baseline in the lines without KCNQ1OT1 | 0.079 | ⚠ within organs, on part of the lines |
| [[NECAB2]] | C | NECAB2 activity raises COL20A1's level | lines that do not express NECAB2 (3) vs lines expressing it (47) | 2.10× lower at baseline in the lines without NECAB2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, PARP11, DLG4; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.800). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.3, -18.4); signed map (14.2, 12.1). **Vector** length 91.5, 19.5% of its response variance represented; |z| ≥ 3 in 1,184 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.4 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +1.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.2 | +1.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -4.0 | -4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.5 | -2.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -5.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | -3.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.1 | -5.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.8 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | collagen type XX alpha 1 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:63,293,186-63,334,851 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1510 |
| Gene groups (HGNC) | Fibronectin type III domain containing; Fibril associated collagens with interrupted triple helices |
| Reactome | 4 pathways, smallest: Collagen chain trimerization; Collagen biosynthesis and modifying enzymes; Collagen formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P218](https://www.uniprot.org/uniprotkb/Q9P218) (Collagen alpha-1(XX) chain):

> Probable collagen protein.

**Summary**, from NCBI Gene [57642](https://www.ncbi.nlm.nih.gov/gene/57642):

> Predicted to be located in endoplasmic reticulum lumen and extracellular matrix. Predicted to be part of collagen type XX trimer. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14670](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14670) · Entrez [57642](https://www.ncbi.nlm.nih.gov/gene/57642) · UniProt [Q9P218](https://www.uniprot.org/uniprotkb/Q9P218) · Ensembl [ENSG00000101203](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101203)

## Data

Gene col 2095: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2095); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2095, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2095]; `tensor/DDL_lfc|DDL_z.npy` [2095]; `embed/gene_vectors.npy` [2095]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2095 or target_col == 2095). Every well: [[COL20A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/COL20A1.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
