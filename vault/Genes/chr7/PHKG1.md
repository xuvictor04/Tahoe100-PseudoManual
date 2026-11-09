---
symbol: "PHKG1"
type: "gene"
col: 9006
ensembl_id: "ENSG00000164776"
name: "phosphorylase kinase catalytic subunit gamma 1"
location: "7p11.2"
module: 37
arm: "+"
pooled_cpm: 8.97
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# PHKG1

*phosphorylase kinase catalytic subunit gamma 1* — 7p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.59× (z +11.2, q 2e-26, up in 41 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ferulic acid (drug)]] 0.5 µM in 1 line (HS-578T 0.0655×); [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0799×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H460 0.0957×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PP2D1]] (+0.77, fdr 7e-06), [[TEX29]] (+0.77, fdr 7e-06), [[TINCR]] (+0.75, fdr 7e-06); moves opposite to [[AIFM1]] (-0.65, fdr 1e-05), [[FAM98B]] (-0.63, fdr 1e-05), [[OCRL]] (-0.61, fdr 7e-06).
> It is in [[Module 037]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9006.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.59×** | +11.2 | 2e-26 | 41/43 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.58×** | +7.9 | 1e-12 | 37/45 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.57×** | +7.5 | 8e-12 | 23/39 (NCI-H2030, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.83×** | +7.1 | 2e-10 | 25/44 (MIA PaCa-2, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.94×** | +5.5 | 5e-06 | 30/45 (BT-474, SW48, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +5.0 | 6e-05 | 21/41 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.77×** | +4.7 | 2e-04 | 23/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.68×** | +4.3 | 0.001 | 23/48 (SW48, LS 180, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.05×** | +4.2 | 0.001 | 20/47 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.65×** | +4.1 | 0.002 | 20/47 (SW480, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.60×** | +3.9 | 0.005 | 18/46 (BT-474, NCI-H460, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +3.9 | 0.005 | 19/43 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.62×** | +3.8 | 0.008 | 21/44 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +3.7 | 0.008 | 22/47 (HEC-1-A, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.55×** | +3.6 | 0.011 | 13/47 (SW480, KATO III, …) | top dose only | position effect removed |
| [[Vilanterol (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.024 | 15/47 (HCT15, HOP62, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.51×** | +3.3 | 0.032 | 19/47 (MIA PaCa-2, HEC-1-A, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.051 | 12/45 (NCI-H1573, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9006.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ferulic acid (drug)]] 0.5 µM in 1 line (HS-578T 0.0655×); [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0799×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H460 0.0957×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.893× | -3.6 | 0.11 | 9/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.743× | -3.6 | 0.11 | 17/48 (RPMI-7951, HEC-1-A, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.681× | -3.2 | 0.24 | 19/48 (LS 180, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9006. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 8.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.73× (z +11.1) | — |
| [[AsPC-1 (line)]] | alt | 8.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.68× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 6.58 | 0 | 1 | — | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM 0.0957× (z -8.6) |
| [[HS-578T (line)]] | alt | 8.48 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.5 µM 0.0655× (z -11.4) |
| [[MIA PaCa-2 (line)]] | alt | 10.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.62× (z +10.1) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H1573 (line)]] | alt | 6.44 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0799× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 5.23 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0928× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 4.68 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0957× (z -9.6) |
| [[PANC-1 (line)]] | alt | 5.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +12.5) | — |
| [[SK-MEL-2 (line)]] | alt | 6.30 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0646× (z -9.2) |
| [[SW 900 (line)]] | alt | 11.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +8.7) | — |
| [[A-172 (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.23 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.59 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9006), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PP2D1]] | +0.77 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[TEX29]] | +0.77 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[TINCR]] | +0.75 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[SPACDR]] | +0.74 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[C9orf153]] | +0.74 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[GP6]] | +0.73 | +0.67 / +0.79 | both halves | 7e-06 |  |
| [[BIRC6-AS2-1]] | +0.73 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[SNX31]] | +0.73 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[RABGEF1]] | +0.73 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[CCDC65]] | +0.72 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[CCDC62]] | +0.71 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[ZNF814]] | +0.71 | +0.62 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AIFM1]] | -0.65 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[FAM98B]] | -0.63 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[OCRL]] | -0.61 | -0.60 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.801). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.1, -18.9); signed map (11.6, 8.4). **Vector** length 83.6, 18.1% of its response variance represented; |z| ≥ 3 in 798 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +11.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.6 | +1.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | +4.0 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.8 | +2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +1.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -0.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | +0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.8 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -2.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.6 | -3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | +0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | phosphorylase kinase catalytic subunit gamma 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p11.2 — chr7:56,080,283-56,092,996 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PHKG |
| Gene groups (HGNC) | Phosphorylase kinase subunits; Phosphorylase kinase catalytic subunit gamma family |
| Hallmark sets | HYPOXIA |
| Reactome | 3 pathways, smallest: Glycogen breakdown (glycogenolysis); Glycogen metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16816](https://www.uniprot.org/uniprotkb/Q16816) (Phosphorylase b kinase gamma catalytic chain, skeletal muscle/heart isoform):

> Catalytic subunit of the phosphorylase b kinase (PHK), which mediates the neural and hormonal regulation of glycogen breakdown (glycogenolysis) by phosphorylating and thereby activating glycogen phosphorylase. In vitro, phosphorylates PYGM, TNNI3, MAPT/TAU, GAP43 and NRGN/RC3 (By similarity).

**Summary**, from NCBI Gene [5260](https://www.ncbi.nlm.nih.gov/gene/5260):

> This gene is a member of the Ser/Thr protein kinase family and encodes a protein with one protein kinase domain and two calmodulin-binding domains. This protein is the catalytic member of a 16 subunit protein kinase complex which contains equimolar ratios of 4 subunit types. The complex is a crucial glycogenolytic regulatory enzyme. This gene has two pseudogenes at chromosome 7q11.21 and one at chromosome 11p11.12. Multiple transcript variants encoding different isoforms have been found for …

**Accessions** — [HGNC:8930](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8930) · Entrez [5260](https://www.ncbi.nlm.nih.gov/gene/5260) · UniProt [Q16816](https://www.uniprot.org/uniprotkb/Q16816) · Ensembl [ENSG00000164776](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164776)

## Data

Gene col 9006: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9006); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9006, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9006]; `tensor/DDL_lfc|DDL_z.npy` [9006]; `embed/gene_vectors.npy` [9006]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9006 or target_col == 9006). Every well: [[PHKG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHKG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
