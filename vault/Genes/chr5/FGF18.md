---
symbol: "FGF18"
type: "gene"
col: 7979
ensembl_id: "ENSG00000156427"
name: "fibroblast growth factor 18"
location: "5q35.1"
module: 38
arm: "+"
pooled_cpm: 7.9
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038", "written"]
generated_by: "tahoemap"
---

# FGF18

*fibroblast growth factor 18* — 5q35.1

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> FGF18 is a secreted fibroblast growth factor of the FGF8 subfamily, signalling through FGFR3 and FGFR4 to coordinate cartilage and bone development.

## What it is

FGF18 is a paracrine, heparin-binding ligand grouped with FGF8 and FGF17. Its best-established role is skeletal: mice lacking Fgf18 show delayed ossification, a disorganised growth plate and defective osteoblast differentiation, a phenotype overlapping Fgfr3 loss that makes FGF18 a physiological restraint on chondrocyte proliferation and a driver of osteogenesis. In adult cartilage it promotes matrix production, the rationale behind sprifermin, a recombinant FGF18 injected into knee joints in osteoarthritis trials; those showed gains in cartilage thickness on MRI without clear symptomatic benefit. In cancer it is reported as a Wnt/β-catenin-responsive gene upregulated in colorectal tumours, read as a paracrine rather than cell-autonomous signal.

## What is uncertain

Whether the association means anything. Paracrine FGF ligands are expressed in only a subset of lines here, so a pooled association can be carried by a few lines rather than a consistent relationship; the per-line table is where to tell the two apart. The slope's direction carries no interpretation either: FGF18 has no assigned p53 direction to sign it against. Its cancer biology is receptor-dependent, so even a real correlation would not point to a consequence.

## References

- Ohbayashi et al., 1998, Journal of Biological Chemistry — cloned FGF-18 and described its expression pattern.
- Liu et al., 2002, Genes & Development — Fgf18-null mice show coordinated defects in chondrogenesis and osteogenesis.
- Ohbayashi et al., 2002, Genes & Development — FGF18 is required for proliferation and differentiation during skeletal development, with phenotypes overlapping Fgfr3 loss.
- Shimokawa et al., 2003, Cancer Research — FGF18 identified as a β-catenin/TCF-responsive gene upregulated in colorectal cancer.
- Hochberg et al., 2019, JAMA — sprifermin increased cartilage thickness in knee osteoarthritis without clear symptomatic benefit.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.00× (z +16.7, q 0e+00, up in 40 of 42 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 0.264×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM72]] (+0.83, fdr 7e-06), [[LDHC]] (+0.81, fdr 7e-06), [[FNDC7]] (+0.81, fdr 7e-06); moves opposite to [[MPPE1]] (-0.59, fdr 2e-05).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7979.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **7.00×** | +16.7 | 0e+00 | 40/42 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.71×** | +8.6 | 3e-15 | 27/41 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.92×** | +8.0 | 3e-13 | 32/44 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.50×** | +7.6 | 4e-12 | 28/41 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.99×** | +6.4 | 2e-08 | 20/37 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.79×** | +6.0 | 2e-07 | 24/41 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.66×** | +5.7 | 9e-07 | 24/43 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **5.47×** | +5.4 | 5e-06 | 31/41 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **2.59×** | +5.4 | 5e-06 | 27/45 (NCI-H2347, NCI-H460, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **4.86×** | +5.0 | 3e-05 | 32/46 (PANC-1, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +4.5 | 4e-04 | 23/46 (SW480, SW1417, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.21×** | +4.4 | 4e-04 | 22/47 (LoVo, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.17×** | +4.4 | 6e-04 | 24/46 (A-172, A498, …) | rises with dose |  |
| [[Gefitinib (drug)]] 5 µM |  | **2.01×** | +3.9 | 0.004 | 18/47 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +3.9 | 0.004 | 14/35 (SNU-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.73×** | +3.3 | 0.032 | 15/46 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.048 | 7/46 (H4, NCI-H2030, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | **1.72×** | +3.1 | 0.055 | 4/46 (HEC-1-A, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 0.264×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7979. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 3.11 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 46.2× (z +16.0) | — |
| [[HEC-1-A (line)]] | alt | 17.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.09× (z +11.7) | — |
| [[PANC-1 (line)]] | alt | 7.95 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +10.2) | — |
| [[SW480 (line)]] | alt | 10.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 3.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +9.2) | — |
| [[C32 (line)]] | wt | 9.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 47.6× (z +13.3) | — |
| [[COLO 205 (line)]] | alt | 3.33 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.9× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 4.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 8.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +10.1) | — |
| [[hTERT-HPNE (line)]] | wt | 11.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.0× (z +9.7) | — |
| [[J82 (line)]] | alt | 3.00 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.3× (z +10.5) | — |
| [[LoVo (line)]] | wt | 12.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +12.9) | — |
| [[LOX-IMVI (line)]] | wt | 8.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.60× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.54 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 36.9× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 8.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.39× (z +9.3) | — |
| [[NCI-H2347 (line)]] | alt | 3.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.2× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 6.81 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 5.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 4.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.65× (z +8.8) | — |
| [[A-172 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7979), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM72]] | +0.83 | +0.84 / +0.77 | both halves | 7e-06 |  |
| [[LDHC]] | +0.81 | +0.81 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[FNDC7]] | +0.81 | +0.82 / +0.77 | both halves | 7e-06 |  |
| [[STPG4]] | +0.79 | +0.79 / +0.75 | both halves | 7e-06 |  |
| [[SELPLG]] | +0.77 | +0.79 / +0.76 | both halves | 7e-06 |  |
| [[IMPA1P1]] | +0.77 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[PYGM]] | +0.77 | +0.81 / +0.71 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.76 | +0.79 / +0.68 | both halves | 7e-06 |  |
| [[SEMA4A]] | +0.75 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[GRAMD2A]] | +0.75 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[PPP1R36]] | +0.75 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[ROPN1L]] | +0.74 | +0.79 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPPE1]] | -0.59 | -0.47 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.692). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.8, -16.3); signed map (16.2, 11.4). **Vector** length 94.5, 21.5% of its response variance represented; |z| ≥ 3 in 1,097 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +16.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +4.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.0 | +2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.8 | +3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +5.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | +3.1 | +3.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +2.6 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -1.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | -1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | +1.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.5 | -2.5 |
|  | [[Lonafarnib (drug)]] 0.05 µM |  | -2.3 | -2.8 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | -2.3 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | fibroblast growth factor 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.1 — chr5:171,419,647-171,457,626 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FGF-18, ZFGF5 |
| Gene groups (HGNC) | Fibroblast growth factor family |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 55 pathways, smallest: FGFR3b ligand binding and activation; FGFRL1 modulation of FGFR1 signaling; Activated point mutants of FGFR2 |
| Matched by | ensembl_id |

**Function**, from UniProt [O76093](https://www.uniprot.org/uniprotkb/O76093) (Fibroblast growth factor 18):

> Plays an important role in the regulation of cell proliferation, cell differentiation and cell migration. Required for normal ossification and bone development. Stimulates hepatic and intestinal proliferation.

**Summary**, from NCBI Gene [8817](https://www.ncbi.nlm.nih.gov/gene/8817):

> The protein encoded by this gene is a member of the fibroblast growth factor (FGF) family. FGF family members possess broad mitogenic and cell survival activities, and are involved in a variety of biological processes, including embryonic development, cell growth, morphogenesis, tissue repair, tumor growth, and invasion. It has been shown in vitro that this protein is able to induce neurite outgrowth in PC12 cells. Studies of the similar proteins in mouse and chick suggested that this protein …

**Accessions** — [HGNC:3674](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3674) · Entrez [8817](https://www.ncbi.nlm.nih.gov/gene/8817) · UniProt [O76093](https://www.uniprot.org/uniprotkb/O76093) · Ensembl [ENSG00000156427](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156427)

## Data

Gene col 7979: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7979); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7979, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7979]; `tensor/DDL_lfc|DDL_z.npy` [7979]; `embed/gene_vectors.npy` [7979]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7979 or target_col == 7979). Every well: [[FGF18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/FGF18.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
