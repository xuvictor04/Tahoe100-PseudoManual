---
module: 112
type: "module"
n_genes: 43
n_plus: 43
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: "TNF-alpha signaling via NF-kB"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 112

*TNF-alpha signaling via NF-kB · 43 genes (single-armed) · [[Module 112.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

Label from the validation stage: **TNF-alpha signaling via NF-kB** (hallmark, q 5e-09; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | TNF-alpha signaling via NF-kB | hallmark | 11/43 | 20.5 | 5e-09 |
| + | TNF-alpha signaling via NF-kB | hallmark | 11/43 | 20.5 | 5e-09 |
| all | Interleukin-10 signaling | reactome | 5/43 | 60.4 | 1e-05 |
| + | Interleukin-10 signaling | reactome | 5/43 | 60.4 | 1e-05 |
| + | KRAS signaling up | hallmark | 8/43 | 17.0 | 1e-05 |
| all | KRAS signaling up | hallmark | 8/43 | 17.0 | 1e-05 |
| all | inflammatory response | hallmark | 6/43 | 15.1 | 0.001 |
| + | inflammatory response | hallmark | 6/43 | 15.1 | 0.001 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 111), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+11.7, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+8.1, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+6.6, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+4.7); [[Harringtonine (drug)]] 0.5 µM (+4.5, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (+4.2, ⚠ toxic; transcription drop; cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+4.0, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+3.5, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+3.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+3.3, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (+2.0); [[PF-06260933 (drug)]] 5 µM (+1.7); [[Harringtonine (drug)]] 0.05 µM (+1.7); [[PH-797804 (drug)]] 5 µM (+1.5); [[Vilanterol (drug)]] 5 µM (+1.3); [[Vilanterol (drug)]] 0.5 µM (+1.3); [[9-ING-41 (drug)]] 0.5 µM (+1.3); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+1.3); [[Gemcitabine (drug)]] 0.5 µM (+1.2) (39 in all, 22 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Clobetasol propionate (drug)]] 5 µM (-4.0); [[Clobetasol propionate (drug)]] 0.5 µM (-3.9); [[Dexamethasone (drug)]] 0.5 µM (-3.6); [[Budesonide (drug)]] 5 µM (-3.5); [[Betamethasone dipropionate (drug)]] 0.05 µM (-3.4); [[Trametinib (drug)]] 5 µM (-3.3, ⚠ cell-cycle shift); [[Triamcinolone (drug)]] 0.5 µM (-3.2); [[Triamcinolone (drug)]] 5 µM (-3.2); [[Dexamethasone (drug)]] 0.05 µM (-3.2); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-2.9); [[Clobetasol propionate (drug)]] 0.05 µM (-2.9) (55 in all, 9 with an alert ⚠; shown: the 10 strongest and the 1 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[A498 (line)]], [[NCI-H460 (line)]], [[A-172 (line)]], [[HS-578T (line)]], [[HOP62 (line)]], [[J82 (line)]], [[NCI-H2347 (line)]], [[AsPC-1 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 32 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[TRAF1]] | Interleukin-10 signaling | +0.70 |
| 2 | [[IER3]] | Interleukin-4 and Interleukin-13 signaling | +0.67 |
| 3 | [[CXCL8]] | TNF-alpha signaling via NF-kB | +0.65 |
| 4 | [[IL1A]] | KRAS signaling up | +0.65 |
| 5 | [[CSF2]] | Interleukin-4 and Interleukin-13 signaling | +0.64 |
| 6 | [[LINC00973]] | Interleukin-10 signaling | +0.63 |
| 7 | [[INHBA]] | Interleukin-10 signaling | +0.63 |
| 8 | [[PTGS2]] | inflammatory response | +0.61 |
| 9 | [[MIR3142HG]] | Interleukin-10 signaling | +0.61 |
| 10 | [[FAM43A]] | inflammatory response | +0.59 |
| 11 | [[IRAK2]] | Interleukin-10 signaling | +0.58 |
| 12 | [[MIR155HG]] | Interleukin-10 signaling | +0.56 |
| 13 | [[PLAU]] | Interleukin-10 signaling | +0.56 |
| 14 | [[CYB5R2]] | Interleukin-4 and Interleukin-13 signaling | +0.56 |
| 15 | [[DSE]] | Interleukin-10 signaling | +0.55 |

## + arm (43)

| Gene | Projection | Name |
|---|---|---|
| [[TRAF1]] | 0.858 | TNF receptor associated factor 1 |
| [[LIF]] | 0.827 | LIF interleukin 6 family cytokine |
| [[IER3]] | 0.825 | immediate early response 3 |
| [[CXCL8]] | 0.820 | C-X-C motif chemokine ligand 8 |
| [[IL1A]] | 0.819 | interleukin 1 alpha |
| [[LINC00973]] | 0.794 | long independently transcribed non-coding RNA 973 |
| [[CSF2]] | 0.789 | colony stimulating factor 2 |
| [[INHBA]] | 0.761 | inhibin subunit beta A |
| [[FAM43A]] | 0.748 | family with sequence similarity 43 member A |
| [[GEM]] | 0.735 | GTP binding protein overexpressed in skeletal muscle |
| [[SYNJ2]] | 0.732 | synaptojanin 2 |
| [[PLAU]] | 0.721 | plasminogen activator, urokinase |
| [[HMGN2P46]] | 0.716 | high mobility group nucleosomal binding domain 2 pseudogene 46 |
| [[CYB5R2]] | 0.712 | cytochrome b5 reductase 2 |
| [[MIR3142HG]] | 0.709 | MIR3142 host gene |
| [[PTGS2]] | 0.709 | prostaglandin-endoperoxide synthase 2 |
| [[DUSP10]] | 0.708 | dual specificity phosphatase 10 |
| [[IRAK2]] | 0.702 | interleukin 1 receptor associated kinase 2 |
| [[NPTX1]] | 0.702 | neuronal pentraxin 1 |
| [[MIR155HG]] | 0.700 | MIR155 host gene |
| [[SOX9]] | 0.697 | SRY-box transcription factor 9 |
| [[MSANTD3]] | 0.695 | Myb/SANT DNA binding domain containing 3 |
| [[IL23A]] | 0.695 | interleukin 23 subunit alpha |
| [[FZD8]] | 0.690 | frizzled class receptor 8 |
| [[KIAA1217]] | 0.687 | KIAA1217 |
| [[CD82]] | 0.682 | CD82 molecule |
| [[ARL4C]] | 0.670 | ARF like GTPase 4C |
| [[DSE]] | 0.664 | dermatan sulfate epimerase |
| [[LIF-AS2]] | 0.663 | LIF antisense RNA 2 |
| [[ZNF267]] | 0.652 | zinc finger protein 267 |
| [[PINLYP]] | 0.651 | phospholipase A2 inhibitor and LY6/PLAUR domain containing |
| [[LHX1]] | 0.647 | LIM homeobox 1 |
| [[RUNX1]] | 0.645 | RUNX family transcription factor 1 |
| [[G0S2]] | 0.639 | G0/G1 switch 2 |
| [[CD274]] | 0.634 | CD274 molecule |
| [[DYRK3]] | 0.633 | dual specificity tyrosine phosphorylation regulated kinase 3 |
| [[CRTAC1]] | 0.587 | cartilage acidic protein 1 |
| [[RPS6KA3]] | 0.568 | ribosomal protein S6 kinase A3 |
| [[SLC43A3]] | 0.550 | solute carrier family 43 member 3 |
| [[TM4SF1-AS1]] | 0.483 | TM4SF1 antisense RNA 1 |
| [[TCF7]] | 0.450 | transcription factor 7 |
| [[MFSD4B]] | 0.381 | solute carrier family 60 member 2 |
| [[EFHD2]] | 0.350 | EF-hand domain family member D2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 112; `graph/modules.parquet` — module == 112; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [111] (drug-dose × line)
