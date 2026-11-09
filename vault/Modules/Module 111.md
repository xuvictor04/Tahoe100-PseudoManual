---
module: 111
type: "module"
n_genes: 43
n_plus: 43
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.2951186001300812
label: "Cell-Cell communication"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 111

*Cell-Cell communication · 43 genes (single-armed) · [[Module 111.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **Cell-Cell communication** (reactome, q 6e-10; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Cell-Cell communication | reactome | 13/43 | 16.6 | 6e-10 |
| + | Cell-Cell communication | reactome | 13/43 | 16.6 | 6e-10 |
| + | Signaling by Rho GTPases | reactome | 16/43 | 9.23 | 5e-09 |
| all | Signaling by Rho GTPases | reactome | 16/43 | 9.23 | 5e-09 |
| all | Signaling by Rho GTPases, Miro GTPases and RHOBTB3 | reactome | 16/43 | 9.00 | 7e-09 |
| + | Signaling by Rho GTPases, Miro GTPases and RHOBTB3 | reactome | 16/43 | 9.00 | 7e-09 |
| + | Platelet activation, signaling and aggregation | reactome | 11/43 | 18.5 | 1e-08 |
| all | Platelet activation, signaling and aggregation | reactome | 11/43 | 18.5 | 1e-08 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 110), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Dinaciclib (drug)]] 0.5 µM (+10.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+9.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+7.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Daptomycin (drug)]] 0.5 µM (+2.2, ⚠ unreliable plate only); [[Daptomycin (drug)]] 5 µM (+2.0, ⚠ unreliable plate only); [[Peretinoin (drug)]] 5 µM (+1.7); [[Niclosamide (olamine) (drug)]] 5 µM (+1.5, ⚠ toxic; cell-cycle shift); [[Peretinoin (drug)]] 0.5 µM (+1.5); [[TAK-901 (drug)]] 5 µM (+1.5, ⚠ cell-cycle shift); [[Vinblastine (sulfate) (drug)]] 5 µM (+1.4); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+1.3); [[Filgotinib (drug)]] 5 µM (+1.3); [[Larotrectinib (drug)]] 0.05 µM (+1.2); [[Mebendazole (drug)]] 5 µM (+1.2); [[Busulfan (drug)]] 0.05 µM (+1.2); [[Vinblastine (sulfate) (drug)]] 0.5 µM (+1.2); [[Retinoic acid (drug)]] 0.05 µM (+1.2) (22 in all, 9 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (-5.5, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (-3.8, ⚠ toxic; cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (-3.6, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 0.5 µM (-3.0, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (-2.2, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM (-2.2, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 5 µM (-2.0); [[Amsacrine (drug)]] 5 µM (-1.9); [[Homoharringtonine (drug)]] 0.5 µM (-1.9, ⚠ cell-cycle shift); [[Cabozantinib (S-malate) (drug)]] 5 µM (-1.8); [[Verteporfin (drug)]] 5 µM (-1.6); [[Ponatinib (drug)]] 0.5 µM (-1.4); [[Triamcinolone (drug)]] 5 µM (-1.3); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (-1.2); [[Afatinib (drug)]] 5 µM (-1.1); [[Penfluridol (drug)]] 5 µM (-1.1); [[Terfenadine (drug)]] 5 µM (-1.1) (29 in all, 17 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[HOP62 (line)]], [[A498 (line)]], [[SW480 (line)]], [[A549 (line)]], [[NCI-H1792 (line)]], [[HS-578T (line)]], [[NCI-H460 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 24 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[ACTR3]] | G-protein beta:gamma signalling | +0.65 |
| 2 | [[CDC42]] | RHO GTPases activate PKNs | +0.62 |
| 3 | [[WDR1]] | Leishmania infection | +0.62 |
| 4 | [[YWHAZ]] | EPH-Ephrin signaling | +0.58 |
| 5 | [[GNB1]] | EPHB-mediated forward signaling | +0.58 |
| 6 | [[ANXA2]] | RHOV GTPase cycle | +0.58 |
| 7 | [[MYH9]] | RHO GTPases Activate WASPs and WAVEs | +0.57 |
| 8 | [[CAPZB]] | EPHB-mediated forward signaling | +0.56 |
| 9 | [[ACTB]] | RHO GTPases activate PAKs | +0.56 |
| 10 | [[RHOA]] | RHO GTPases activate IQGAPs | +0.56 |
| 11 | [[ARPC4]] | G beta:gamma signalling through CDC42 | +0.56 |
| 12 | [[FLNA]] | FCGR3A-mediated phagocytosis | +0.54 |
| 13 | [[IQGAP1]] | RHO GTPases activate PKNs | +0.54 |
| 14 | [[TPM4]] | RHO GTPase Effectors | +0.54 |
| 15 | [[CAST]] | RHO GTPases activate CIT | +0.54 |

## + arm (43)

| Gene | Projection | Name |
|---|---|---|
| [[CDC42]] | 0.834 | cell division cycle 42 |
| [[YWHAZ]] | 0.813 | tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein zeta |
| [[ACTR3]] | 0.810 | actin related protein 3 |
| [[WDR1]] | 0.806 | WD repeat domain 1 |
| [[MYH9]] | 0.802 | myosin heavy chain 9 |
| [[TPM4]] | 0.783 | tropomyosin 4 |
| [[ANXA2]] | 0.752 | annexin A2 |
| [[ACTB]] | 0.740 | actin beta |
| [[FLNA]] | 0.730 | filamin A |
| [[RHOA]] | 0.726 | ras homolog family member A |
| [[GNB1]] | 0.722 | G protein subunit beta 1 |
| [[IQGAP1]] | 0.721 | IQ motif containing GTPase activating protein 1 |
| [[ACTN4]] | 0.718 | actinin alpha 4 |
| [[CAPNS1]] | 0.711 | calpain small subunit 1 |
| [[TMEM101]] | -0.704 | transmembrane protein 101 |
| [[CAPZB]] | 0.698 | capping actin protein of muscle Z-line subunit beta |
| [[CD151]] | 0.688 | CD151 molecule (Raph blood group) |
| [[DBNL]] | 0.644 | drebrin like |
| [[ARPC4]] | 0.630 | actin related protein 2/3 complex subunit 4 |
| [[SPTAN1]] | 0.610 | spectrin alpha, non-erythrocytic 1 |
| [[GNG12]] | 0.604 | G protein subunit gamma 12 |
| [[DSG2]] | 0.603 | desmoglein 2 |
| [[VCL]] | 0.603 | vinculin |
| [[RSU1]] | 0.600 | Ras suppressor protein 1 |
| [[PDLIM5]] | 0.592 | PDZ and LIM domain 5 |
| [[CLIC4]] | 0.591 | CLIC family member 4 |
| [[CAST]] | 0.585 | calpastatin |
| [[RAC1]] | 0.579 | Rac family small GTPase 1 |
| [[AHNAK2]] | 0.552 | AHNAK nucleoprotein 2 |
| [[TAGLN2]] | 0.552 | transgelin 2 |
| [[TMOD3]] | 0.548 | tropomodulin 3 |
| [[EIF1AX]] | 0.525 | eukaryotic translation initiation factor 1A X-linked |
| [[CAV2]] | 0.520 | caveolin 2 |
| [[MBD4]] | -0.520 | methyl-CpG binding domain 4, DNA glycosylase |
| [[AP1B1]] | 0.512 | adaptor related protein complex 1 subunit beta 1 |
| [[FLNC]] | 0.493 | filamin C |
| [[CNN2]] | 0.491 | calponin 2 |
| [[FERMT2]] | 0.426 | FERM domain containing kindlin 2 |
| [[ANXA1]] | 0.415 | annexin A1 |
| [[STK38L]] | 0.366 | serine/threonine kinase 38 like |
| [[NECTIN3]] | 0.352 | nectin cell adhesion molecule 3 |
| [[SMG1]] | 0.324 | SMG1 nonsense mediated mRNA decay associated PI3K related kinase |
| [[IL27RA]] | -0.301 | interleukin 27 receptor subunit alpha |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 111; `graph/modules.parquet` — module == 111; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [110] (drug-dose × line)
