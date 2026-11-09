---
symbol: "DHPS"
type: "gene"
col: 1734
ensembl_id: "ENSG00000095059"
name: "deoxyhypusine synthase"
location: "19p13.13"
module: 3
arm: "+"
pooled_cpm: 20.54
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# DHPS

*deoxyhypusine synthase* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.25× (z +10.8, q 1e-24, up in 36 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.78× (z +5.5, q 7e-06, up in 31 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.475× (z -9.9, q 2e-20, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR2F]] (+0.77, fdr 7e-06), [[PTOV1]] (+0.74, fdr 7e-06), [[ADIPOR1]] (+0.67, fdr 7e-06); moves opposite to [[PPID]] (-0.63, fdr 1e-05), [[LACC1]] (-0.57, fdr 5e-05), [[YTHDC2]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1734.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.25×** | +10.8 | 1e-24 | 36/42 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +6.5 | 2e-08 | 25/34 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.78×** | +5.5 | 7e-06 | 31/46 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.75×** | +5.3 | 1e-05 | 32/47 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +4.9 | 1e-04 | 20/37 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.12×** | +4.7 | 3e-04 | 29/48 (LS 180, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.60×** | +4.5 | 6e-04 | 22/44 (RKO, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.56×** | +4.2 | 0.002 | 21/47 (KATO III, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.37×** | +4.1 | 0.002 | 23/48 (Hs 766T, NCI-H2347, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.34×** | +3.9 | 0.006 | 25/45 (HS-578T, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Thymol (drug)]] 0.5 µM |  | **1.31×** | +3.6 | 0.018 | 20/46 (J82, LOX-IMVI, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.5 | 0.023 | 0/48 | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.2 | 0.062 | 20/47 (NCI-H2347, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1734.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.475×** | -9.9 | 2e-20 | 40/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.619×** | -9.1 | 2e-17 | 37/47 (Panc 03.27, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.774×** | -4.9 | 2e-04 | 26/48 (LS 180, LoVo, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.723×** | -4.2 | 0.004 | 22/47 (BT-474, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Hydroxyurea (drug)]] 5 µM |  | **0.768×** | -3.4 | 0.071 | 14/47 (C32, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1734. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 22.0 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -11.5) |
| [[BT-474 (line)]] | alt | 24.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 21.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -13.9) |
| [[A-172 (line)]] | wt | 27.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.60× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 24.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -9.8) |
| [[C-33 A (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.177× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~48% of this change |
| [[H4 (line)]] | wt | 25.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -8.6) |
| [[HT-29 (line)]] | alt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -9.9) |
| [[KATO III (line)]] | alt | 16.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 18.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0992× (z -14.5) |
| [[NCI-H2347 (line)]] | alt | 18.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -10.0) |
| [[RKO (line)]] | wt | 20.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -12.0) |
| [[SNU-1 (line)]] | wt | 26.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -9.7) |
| [[SW 1271 (line)]] | alt | 34.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM 0.0536× (z -8.7) |
| [[A498 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1734), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2F]] | +0.77 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[PTOV1]] | +0.74 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[ADIPOR1]] | +0.67 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[TMEM219]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[CLPTM1]] | +0.65 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[ATF6B]] | +0.64 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[RPS11]] | +0.63 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[ALKBH7]] | +0.63 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[SMARCD2]] | +0.63 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[MARK4]] | +0.62 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[CD81]] | +0.62 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[GNPTG]] | +0.61 | +0.67 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPID]] | -0.63 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[LACC1]] | -0.57 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[YTHDC2]] | -0.57 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[TIGD2]] | -0.56 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[PBDC1]] | -0.53 | -0.65 / -0.28 | both halves | 3e-04 |  |
| [[FAM169A]] | -0.51 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[DDX52]] | -0.51 | -0.59 / -0.38 | both halves | 7e-05 |  |
| [[THOC7]] | -0.50 | -0.56 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.440). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-15.0, -18.8); signed map (-27.5, 5.5). **Vector** length 70.9, 14.0% of its response variance represented; |z| ≥ 3 in 633 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +3.9 | +5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.8 | +3.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.6 | +4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +6.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.9 | +3.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.8 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +4.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.8 | -9.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.0 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -2.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -9.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -4.9 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | deoxyhypusine synthase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:12,675,717-12,681,880 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MIG13 |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 2 pathways, smallest: Hypusine synthesis from eIF5A-lysine; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P49366](https://www.uniprot.org/uniprotkb/P49366) (Deoxyhypusine synthase):

> Catalyzes the NAD-dependent oxidative cleavage of spermidine and the subsequent transfer of the butylamine moiety of spermidine to the epsilon-amino group of a critical lysine residue of the eIF-5A precursor protein to form the intermediate deoxyhypusine residue. This is the first step of the post-translational modification of that lysine into an unusual amino acid residue named hypusine. Hypusination is unique to mature eIF-5A factor and is essential for its function.

**Summary**, from NCBI Gene [1725](https://www.ncbi.nlm.nih.gov/gene/1725):

> This gene encodes a protein that is required for the formation of hypusine, a unique amino acid formed by the posttranslational modification of only one protein, eukaryotic translation initiation factor 5A. The encoded protein catalyzes the first step in hypusine formation by transferring the butylamine moiety of spermidine to a specific lysine residue of the eukaryotic translation initiation factor 5A precursor, forming an intermediate deoxyhypusine residue. Alternatively spliced transcript …

**Accessions** — [HGNC:2869](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2869) · Entrez [1725](https://www.ncbi.nlm.nih.gov/gene/1725) · UniProt [P49366](https://www.uniprot.org/uniprotkb/P49366) · Ensembl [ENSG00000095059](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095059)

## Data

Gene col 1734: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1734); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1734, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1734]; `tensor/DDL_lfc|DDL_z.npy` [1734]; `embed/gene_vectors.npy` [1734]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1734 or target_col == 1734). Every well: [[DHPS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHPS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
