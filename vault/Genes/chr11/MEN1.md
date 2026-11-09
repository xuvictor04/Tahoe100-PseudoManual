---
symbol: "MEN1"
type: "gene"
col: 5486
ensembl_id: "ENSG00000133895"
name: "menin 1"
location: "11q13.1"
module: 127
arm: "+"
pooled_cpm: 6.85
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# MEN1

*menin 1* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.75× (z +7.8, q 4e-12, up in 26 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.465× (z -10.7, q 5e-24, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BAP1]] (+0.62, fdr 1e-05), [[ATP13A1]] (+0.61, fdr 1e-05), [[MTFR1L]] (+0.60, fdr 1e-05).
> It is in [[Module 127]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5486.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.75×** | +7.8 | 4e-12 | 26/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.72×** | +7.5 | 1e-11 | 31/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.60×** | +6.6 | 9e-09 | 15/37 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +6.2 | 7e-08 | 21/47 (NCI-H2347, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +6.1 | 1e-07 | 18/47 (SW480, A549, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.1 | 3e-05 | 17/41 (HT-29, A549, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +4.8 | 1e-04 | 7/47 (PANC-1, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.33×** | +3.9 | 0.007 | 9/30 (MIA PaCa-2, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.34×** | +3.9 | 0.007 | 14/33 (SW1417, Panc 03.27, …) | two highest doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.018 | 11/43 (HOP62, HT-29, …) | top dose only | position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.41×** | +3.4 | 0.037 | 8/26 (A498, HT-29, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.052 | 11/45 (NCI-H2030, PANC-1, …) | top dose only |  |
| [[Almonertinib (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.076 | 5/45 (COLO 205, C32, …) | inconsistent across doses | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | 1.17× | +3.1 | 0.076 | 4/47 (SNU-423, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.080 | 8/48 (SW48, SW1417, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5486.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.465×** | -10.7 | 5e-24 | 36/47 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.539×** | -8.7 | 1e-15 | 32/46 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.587×** | -7.5 | 2e-11 | 26/46 (BT-474, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.590×** | -7.4 | 2e-11 | 26/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.653×** | -5.8 | 1e-06 | 20/43 (SNU-423, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.657×** | -5.7 | 1e-06 | 18/45 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.755×** | -3.9 | 0.006 | 13/47 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.763×** | -3.8 | 0.010 | 10/47 (HS-578T, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.774×** | -3.6 | 0.019 | 15/45 (RPMI-7951, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.775×** | -3.6 | 0.019 | 14/46 (KATO III, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.785×** | -3.4 | 0.033 | 11/46 (A-427, C32, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.804×** | -3.1 | 0.098 | 12/42 (A-172, Panc 03.27, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 0.5 µM |  | 0.807× | -3.0 | 0.10 | 8/45 (J82, A-172, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.807× | -3.0 | 0.10 | 8/46 (HOP62, SW48, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5486. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 14.6 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0871× (z -12.7) |
| [[PANC-1 (line)]] | alt | 11.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.260× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -9.2) |
| [[A549 (line)]] | wt | 3.82 | 0 | 1 | — | [[Sunitinib (drug)]] 0.05 µM 0.0562× (z -10.0) |
| [[KATO III (line)]] | alt | 9.37 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.151× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 8.86 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.146× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 4.13 | 0 | 1 | — | [[Fluvoxamine (drug)]] 5 µM 0.0777× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 3.56 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.159× (z -8.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 6.18 | 0 | 1 | — | [[Methotrexate (drug)]] 0.05 µM 0.0617× (z -9.8) |
| [[SNU-423 (line)]] | alt | 5.19 | 0 | 1 (1 ⚠) | — | [[Cytarabine (drug)]] 5 µM 0.0781× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 4.71 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0715× (z -8.5) |
| [[SW1417 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[SW480 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.285× (z -10.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5486), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAP1]] | +0.62 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[ATP13A1]] | +0.61 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[MTFR1L]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[COASY]] | +0.59 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[TEX264]] | +0.59 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[ABCF3]] | +0.58 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[TBL3]] | +0.58 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[PIP4K2B]] | +0.58 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[BCS1L]] | +0.58 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[RABGGTA]] | +0.57 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[ELOA]] | +0.56 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[MAF1]] | +0.56 | +0.57 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.648). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.4, -23.2); signed map (-11.9, -27.4). **Vector** length 49.3, 5.77% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.9 | +6.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.2 | +6.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | -1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | +2.1 | +3.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +1.9 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +1.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.2 | +1.4 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.2 | +1.1 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.6 | -7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -0.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.2 | -8.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -3.6 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.3 | -0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.2 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | menin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:64,803,510-64,811,294 (-) |
| Ensembl biotype | protein_coding |
| Reactome | 19 pathways, smallest: RHO GTPases activate IQGAPs; SMAD2/SMAD3:SMAD4 heterotrimer regulates transcription; Deactivation of the beta-catenin transactivating complex |
| Matched by | ensembl_id |

**Function**, from UniProt [O00255](https://www.uniprot.org/uniprotkb/O00255) (Menin):

> Essential component of a MLL/SET1 histone methyltransferase (HMT) complex, a complex that specifically methylates 'Lys-4' of histone H3 (H3K4). Functions as a transcriptional regulator. Binds to the TERT promoter and represses telomerase expression. Plays a role in TGFB1-mediated inhibition of cell-proliferation, possibly regulating SMAD3 transcriptional activity. Represses JUND-mediated transcriptional activation on AP1 sites, as well as that mediated by NFKB subunit RELA. Positively regulates …

**Summary**, from NCBI Gene [4221](https://www.ncbi.nlm.nih.gov/gene/4221):

> This gene encodes menin, a tumor suppressor associated with a syndrome known as multiple endocrine neoplasia type 1. Menin is a scaffold protein that functions in histone modification and epigenetic gene regulation. It is thought to regulate several pathways and processes by altering chromatin structure through the modification of histones. [provided by RefSeq, May 2019]

**Accessions** — [HGNC:7010](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7010) · Entrez [4221](https://www.ncbi.nlm.nih.gov/gene/4221) · UniProt [O00255](https://www.uniprot.org/uniprotkb/O00255) · Ensembl [ENSG00000133895](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133895)

## Data

Gene col 5486: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5486); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5486, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5486]; `tensor/DDL_lfc|DDL_z.npy` [5486]; `embed/gene_vectors.npy` [5486]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5486 or target_col == 5486). Every well: [[MEN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MEN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
