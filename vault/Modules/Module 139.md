---
module: 139
type: "module"
n_genes: 34
n_plus: 34
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.2850244641304016
label: "Interleukin-4 and Interleukin-13 signaling"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 139

*Interleukin-4 and Interleukin-13 signaling · 34 genes (single-armed) · [[Module 139.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **Interleukin-4 and Interleukin-13 signaling** (reactome, q 2e-05; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Interleukin-4 and Interleukin-13 signaling | reactome | 6/34 | 33.3 | 2e-05 |
| + | Interleukin-4 and Interleukin-13 signaling | reactome | 6/34 | 33.3 | 2e-05 |
| + | Signaling by Interleukins | reactome | 8/34 | 10.1 | 5e-04 |
| all | Signaling by Interleukins | reactome | 8/34 | 10.1 | 5e-04 |
| all | Cytokine Signaling in Immune system | reactome | 10/34 | 6.73 | 7e-04 |
| + | Cytokine Signaling in Immune system | reactome | 10/34 | 6.73 | 7e-04 |
| + | interferon gamma response | hallmark | 6/34 | 15.7 | 0.001 |
| all | interferon gamma response | hallmark | 6/34 | 15.7 | 0.001 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 138), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+6.3); [[Tucidinostat (drug)]] 0.5 µM (+4.6, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+4.1, ⚠ cell-cycle shift); [[Clobetasol propionate (drug)]] 0.05 µM (+4.0); [[Clobetasol propionate (drug)]] 0.5 µM (+3.4); [[Betamethasone dipropionate (drug)]] 0.5 µM (+3.4); [[Budesonide (drug)]] 0.05 µM (+3.2); [[Betamethasone dipropionate (drug)]] 5 µM (+3.2); [[Budesonide (drug)]] 0.5 µM (+3.2); [[Triamcinolone (drug)]] 5 µM (+3.2); [[Triamcinolone (drug)]] 0.5 µM (+3.2); [[Betamethasone dipropionate (drug)]] 0.05 µM (+3.1) (53 in all, 12 with an alert ⚠; shown: the 10 strongest and the 2 next strongest without an alert)
- Lower it: [[Tofacitinib (drug)]] 5 µM (-3.8); [[Tofacitinib (drug)]] 0.5 µM (-2.8); [[Tofacitinib (citrate) (drug)]] 5 µM (-2.7); [[c-Kit-IN-1 (drug)]] 0.05 µM (-2.6, ⚠ unreliable plate only); [[Ixazomib citrate (drug)]] 5 µM (-2.6, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-2.4); [[Tofacitinib (citrate) (drug)]] 0.5 µM (-2.4); [[5-Azacytidine (drug)]] 5 µM (-2.0); [[Ponatinib (drug)]] 5 µM (-1.9); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (-1.9); [[Ixazomib citrate (drug)]] 0.5 µM (-1.5); [[TAK-733 (drug)]] 5 µM (-1.4) (30 in all, 8 with an alert ⚠; shown: the 10 strongest and the 2 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[A498 (line)]], [[HS-578T (line)]], [[HOP62 (line)]], [[J82 (line)]], [[A-172 (line)]], [[Hs 766T (line)]], [[Panc 03.27 (line)]], [[CFPAC-1 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 14 candidates, none with an alert.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[SAA2]] | Interleukin-4 and Interleukin-13 signaling | +0.63 |
| 2 | [[SAA2-SAA4]] | Interleukin-4 and Interleukin-13 signaling | +0.63 |
| 3 | [[SAA4]] | Interleukin-4 and Interleukin-13 signaling | +0.60 |
| 4 | [[BCL6]] | interferon gamma response | +0.59 |
| 5 | [[NNMT]] | Interleukin-4 and Interleukin-13 signaling | +0.57 |
| 6 | [[STOM]] | Interleukin-4 and Interleukin-13 signaling | +0.57 |
| 7 | [[SAA1]] | TNF-alpha signaling via NF-kB | +0.56 |
| 8 | [[C3]] | Interleukin-4 and Interleukin-13 signaling | +0.55 |
| 9 | [[HIF1A]] | TNF-alpha signaling via NF-kB | +0.55 |
| 10 | [[NAMPT]] | Interleukin-4 and Interleukin-13 signaling | +0.54 |
| 11 | [[C1RL]] | interferon gamma response | +0.53 |
| 12 | [[NFIL3]] | Interleukin-4 and Interleukin-13 signaling | +0.52 |
| 13 | [[SOD2]] | Interleukin-4 and Interleukin-13 signaling | +0.51 |
| 14 | [[CEBPD]] | interferon gamma response | +0.51 |

## + arm (34)

| Gene | Projection | Name |
|---|---|---|
| [[SAA2-SAA4]] | 0.917 | SAA2-SAA4 readthrough |
| [[SAA2]] | 0.908 | serum amyloid A2 |
| [[SAA4]] | 0.887 | serum amyloid A4, constitutive |
| [[BCL6]] | 0.850 | BCL6 transcription repressor |
| [[SAA1]] | 0.849 | serum amyloid A1 |
| [[C3]] | 0.806 | complement C3 |
| [[NNMT]] | 0.776 | nicotinamide N-methyltransferase |
| [[STOM]] | 0.770 | stomatin |
| [[CEBPD]] | 0.748 | CCAAT enhancer binding protein delta |
| [[NAMPT]] | 0.745 | nicotinamide phosphoribosyltransferase |
| [[C1RL]] | 0.717 | complement C1r subcomponent like |
| [[HIF1A]] | 0.717 | hypoxia inducible factor 1 subunit alpha |
| [[FGA]] | 0.711 | fibrinogen alpha chain |
| [[SLPI]] | 0.702 | secretory leukocyte peptidase inhibitor |
| [[SOD2]] | 0.699 | superoxide dismutase 2 |
| [[BIRC3]] | 0.682 | baculoviral IAP repeat containing 3 |
| [[JPH2]] | 0.677 | junctophilin 2 |
| [[NFIL3]] | 0.662 | nuclear factor, interleukin 3 regulated |
| [[STAT3]] | 0.655 | signal transducer and activator of transcription 3 |
| [[SERPINA3]] | 0.648 | serpin family A member 3 |
| [[PTPN2]] | 0.630 | protein tyrosine phosphatase non-receptor type 2 |
| [[SECTM1]] | 0.629 | secreted and transmembrane 1 |
| [[TNFSF14]] | 0.593 | TNF superfamily member 14 |
| [[NAMPTP1]] | 0.588 | nicotinamide phosphoribosyltransferase pseudogene 1 |
| [[SQOR]] | 0.574 | sulfide quinone oxidoreductase |
| [[ZC3H12A-DT]] | 0.562 | lncRNA induced by TGF-beta and antagonizes TGF-beta signaling 1 |
| [[HPS5]] | 0.549 | HPS5 biogenesis of lysosomal organelles complex 2 subunit 2 |
| [[FTH1]] | 0.547 | ferritin heavy chain 1 |
| [[THBS3-AS1]] | 0.542 | THBS3 antisense RNA 1 |
| [[JAK1]] | 0.523 | Janus kinase 1 |
| [[PROS1]] | 0.500 | protein S |
| [[SPTSSA]] | 0.491 | serine palmitoyltransferase small subunit A |
| [[TCP10L]] | -0.449 | t-complex 10 like |
| [[FNDC3B]] | 0.440 | fibronectin type III domain containing 3B |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 139; `graph/modules.parquet` — module == 139; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [138] (drug-dose × line)
