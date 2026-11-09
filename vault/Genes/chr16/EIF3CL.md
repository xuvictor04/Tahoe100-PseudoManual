---
symbol: "EIF3CL"
type: "gene"
col: 12994
ensembl_id: "ENSG00000205609"
name: "eukaryotic translation initiation factor 3 subunit C like"
location: "16p12.1"
module: 33
arm: "+"
pooled_cpm: 3.1
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# EIF3CL

*eukaryotic translation initiation factor 3 subunit C like* — 16p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.54× (z +8.1, q 2e-13, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 4.89× (z +7.5, q 1e-11, up in 30 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Vandetanib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0472×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SW1417 0.0540×); [[Oxaprozin (drug)]] 0.5 µM in 1 line (KATO III 0.0822×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC12]] (+0.65, fdr 7e-06), [[TIMM23]] (+0.63, fdr 1e-05), [[CTU1]] (+0.62, fdr 1e-05); moves opposite to [[VEZF1]] (-0.63, fdr 1e-05), [[CGGBP1]] (-0.62, fdr 1e-05), [[TIA1]] (-0.62, fdr 3e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12994.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.54×** | +8.1 | 2e-13 | 1/3 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.89×** | +7.5 | 1e-11 | 30/40 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.21×** | +7.2 | 1e-10 | 19/31 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +5.7 | 2e-06 | 9/19 (KATO III, A498, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.83×** | +5.5 | 4e-06 | 12/44 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.81×** | +5.0 | 6e-05 | 1/5 (A498) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.68×** | +4.7 | 2e-04 | 13/43 (PANC-1, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.65×** | +4.5 | 4e-04 | 11/42 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.62×** | +4.4 | 7e-04 | 3/43 (NCI-H1573, HEC-1-A, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.66×** | +4.4 | 7e-04 | 9/43 (PANC-1, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.3 | 1e-03 | 11/25 (SHP-77, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.37×** | +4.1 | 0.002 | 9/30 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.55×** | +4.0 | 0.003 | 13/45 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.50×** | +3.7 | 0.010 | 4/19 (SW480, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.11×** | +3.5 | 0.015 | 1/5 (PANC-1) | top dose only | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.029 | 3/45 (A549, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.055 | 6/36 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12994.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Vandetanib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0472×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SW1417 0.0540×); [[Oxaprozin (drug)]] 0.5 µM in 1 line (KATO III 0.0822×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.713× | -3.1 | 0.81 | 11/42 (CFPAC-1, HCT15, …) | two highest doses | cell-cycle shift (explains ~16% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12994. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 3.91 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0822× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 2.38 | 0 | 1 | — | [[Vandetanib (drug)]] 0.05 µM 0.0472× (z -10.5) |
| [[SW1417 (line)]] | alt | 4.18 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0540× (z -10.3) |
| [[A-172 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.930 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12994), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC12]] | +0.65 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[TIMM23]] | +0.63 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[CTU1]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[INPP5B]] | +0.61 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[TYW1]] | +0.60 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[ZNF816-ZNF321P]] | +0.60 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[KNOP1]] | +0.59 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[TIMM23B]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 | STRING 403 |
| [[NOL10]] | +0.59 | +0.65 / +0.46 | both halves | 2e-05 |  |
| [[MFSD14CP]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[TMEM120B]] | +0.59 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[GFOD2]] | +0.58 | +0.53 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VEZF1]] | -0.63 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[CGGBP1]] | -0.62 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[TIA1]] | -0.62 | -0.66 / -0.43 | both halves | 3e-05 |  |
| [[RO60]] | -0.62 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[ARCN1]] | -0.62 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[ZBTB33]] | -0.57 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[THAP9]] | -0.56 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[SCRN1]] | -0.55 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[RHNO1]] | -0.55 | -0.67 / -0.28 | both halves | 3e-04 |  |
| [[THAP5]] | -0.54 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[NOTCH2NLB]] | -0.54 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[HNRNPK]] | -0.54 | -0.44 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.486). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-9.2, -16.6); signed map (-42.0, -17.9). **Vector** length 40.0, 4.13% of its response variance represented; |z| ≥ 3 in 849 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +1.8 | +7.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +1.7 | +5.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +1.7 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.7 | +5.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +1.6 | +4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.2 | +4.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.1 | +1.6 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.1 | +1.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +0.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.9 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -0.9 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.9 | -0.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -0.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 3 subunit C like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.1 — chr16:28,379,579-28,403,841 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [B5ME19](https://www.uniprot.org/uniprotkb/B5ME19) (Eukaryotic translation initiation factor 3 subunit C-like protein):

> Component of the eukaryotic translation initiation factor 3 (eIF-3) complex, which is required for several steps in the initiation of protein synthesis. The eIF-3 complex associates with the 40S ribosome and facilitates the recruitment of eIF-1, eIF-1A, eIF-2:GTP:methionyl-tRNAi and eIF-5 to form the 43S pre-initiation complex (43S PIC). The eIF-3 complex stimulates mRNA recruitment to the 43S PIC and scanning of the mRNA for AUG recognition. The eIF-3 complex is also required for disassembly …

**Summary**, from NCBI Gene [728689](https://www.ncbi.nlm.nih.gov/gene/728689):

> The protein encoded by this gene is a core subunit of the eukaryotic translation initiation factor 3 (eIF3) complex. The encoded protein is nearly identical to another protein, eIF3c, from a related gene. The eIF3 complex binds the 40S ribosome and mRNAs to enable translation initiation. Several transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:26347](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26347) · Entrez [728689](https://www.ncbi.nlm.nih.gov/gene/728689) · UniProt [B5ME19](https://www.uniprot.org/uniprotkb/B5ME19) · Ensembl [ENSG00000205609](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205609)

## Data

Gene col 12994: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12994); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12994, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12994]; `tensor/DDL_lfc|DDL_z.npy` [12994]; `embed/gene_vectors.npy` [12994]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12994 or target_col == 12994). Every well: [[EIF3CL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF3CL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
